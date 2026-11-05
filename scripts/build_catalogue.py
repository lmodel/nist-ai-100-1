#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = ["pdfplumber>=0.11.7", "pyyaml>=6"]
# ///
"""Write the AI RMF Core into src/nist_ai_100_1/data/ai-rmf-1.0.yaml.

The Core comes from three files in upstream/, which this script never changes:

- the publication's Tables 1 to 4 give each category's and subcategory's statement;
- NIST's OSCAL catalog gives each function's overview and the Playbook's suggested
  actions, discussion, documentation prompts and resources;
- the Playbook's own file gives the AI actor and topic tags, which the catalog lacks.

The rest of the catalogue file, what Part 1 and the appendices list, is written by hand
and stays as it is. With --check the script writes nothing and exits 1 when the file's
Core differs from what the three sources give.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

import pdfplumber
import yaml

ROOT = Path(__file__).resolve().parent.parent
PDF = ROOT / "upstream" / "NIST.AI.100-1.pdf"
OSCAL = ROOT / "upstream" / "oscal-content" / "NIST_AI-RMF_v1_catalog.json"
PLAYBOOK = ROOT / "upstream" / "playbook.json"
CATALOGUE = ROOT / "src" / "nist_ai_100_1" / "data" / "ai-rmf-1.0.yaml"
SCHEMA_DIR = ROOT / "src" / "nist_ai_100_1" / "schema"

FUNCTIONS = ("GOVERN", "MAP", "MEASURE", "MANAGE")
CATEGORY_ID = r"(?:GOVERN|MAP|MEASURE|MANAGE) \d+"
SUBCATEGORY_ID = CATEGORY_ID + r"\.\d+"

# A tag the Playbook files under AI Actors that is a topic, not an actor or a task.
NOT_AN_ACTOR = {"Fairness and Bias"}


def table_columns(pdf_path: Path = PDF) -> tuple[str, str]:
    """The left (categories) and right (subcategories) columns of Tables 1 to 4."""
    left, right = [], []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            words = page.extract_words(x_tolerance=1)
            headers = [w for w in words if w["text"] == "Subcategories"]
            if not headers:
                continue
            split = headers[0]["x0"] - 5
            top = headers[0]["bottom"] + 1
            ends = [w["top"] for w in words if w["text"] == "Continued"]
            ends += [
                w["top"]
                for w in words
                if re.fullmatch(r"5\.\d|6\.", w["text"]) and w["x0"] < split and w["top"] > top
            ]
            bottom = min(ends) - 1 if ends else page.height - 40
            left.append(page.crop((0, top, split, bottom)).extract_text(x_tolerance=1) or "")
            right.append(
                page.crop((split, top, page.width, bottom)).extract_text(x_tolerance=1) or ""
            )
    return "\n".join(left), "\n".join(right)


def known_words(*texts: str) -> set[str]:
    """Every word that appears unbroken, hyphenated or not, lowercased."""
    words: set[str] = set()
    for text in texts:
        for line in text.splitlines():
            for word in line.split():
                words.add(word.strip("(),.;:“”\"'’").lower())
    return words


def unbreak(text: str, known: set[str]) -> str:
    """Join the lines of a statement, undoing the typesetter's line-end hyphens.

    A word broken at a line end keeps its hyphen only when the hyphenated form appears
    unbroken somewhere in the Core and the joined form does not.
    """

    def join(match: re.Match[str]) -> str:
        head, tail = match.group(1), match.group(2)
        joined = (head + tail).strip("(),.;:“”\"'’").lower()
        hyphened = (head + "-" + tail).strip("(),.;:“”\"'’").lower()
        if hyphened in known and joined not in known:
            return head + "-" + tail
        return head + tail

    text = re.sub(r"(\S+)-\n(\S+)", join, text)
    return re.sub(r"\s+", " ", text).strip()


def split_statements(text: str, pattern: str, known: set[str]) -> dict[str, str]:
    """The statement after each identifier in a column."""
    pieces = re.split(rf"\n?(?=(?:{pattern}):)", text)
    statements = {}
    for piece in pieces:
        match = re.match(rf"({pattern}):\s*(.*)", piece, flags=re.S)
        if match:
            statements[match.group(1)] = unbreak(match.group(2), known)
    return statements


def publication_statements() -> tuple[dict[str, str], dict[str, str]]:
    """Each category's and each subcategory's statement in the publication."""
    left, right = table_columns()
    oscal = OSCAL.read_text(encoding="utf-8")
    prose = " ".join(re.findall(r'"prose": "([^"]*)"', oscal))
    known = known_words(left, right, prose)
    return (
        split_statements(left, CATEGORY_ID, known),
        split_statements(right, SUBCATEGORY_ID, known),
    )


def _items(part: dict) -> list[dict]:
    """A part's items, in order, flattening a sub-item after its parent."""
    found = []
    for child in part.get("parts", []):
        if child.get("prose"):
            found.append(child)
        found.extend(_items(child))
    return found


def _resource(uuid: str, resources: dict[str, dict]) -> dict:
    resource = resources[uuid]
    entry = {"title": resource["title"], "ai_rmf_resource_uuid": uuid}
    address = resource["rlinks"][0]["href"]
    if address != "N/A":
        entry["ai_rmf_resource_address"] = address
    return entry


def actor_names() -> dict[str, str]:
    """Each spelling of an AI actor tag, with the permissible value it names."""
    enum = yaml.safe_load((SCHEMA_DIR / "nist_ai_100_1_base.yaml").read_text(encoding="utf-8"))[
        "enums"
    ]["AiRmfActorTaskName"]["permissible_values"]
    names = {}
    for value, entry in enum.items():
        names[entry["title"]] = value
        for alias in entry.get("aliases", []):
            names[alias] = value
    return names


def subcategory_record(control: dict, statement: str, playbook: dict, resources: dict) -> dict:
    """One subcategory from its statement, its catalog control and its Playbook entry."""
    record = {"ai_rmf_subcategory_id": control["title"], "description": statement}
    parts = control["parts"]
    about = [p["prose"] for p in parts if p.get("class") == "about"]
    if about:
        record["ai_rmf_subcategory_about"] = about
    actions = [
        {"ai_rmf_suggested_action_id": item["id"], "description": item["prose"]}
        for part in parts
        if part["name"] == "statement"
        for item in _items(part)
    ]
    if actions:
        record["ai_rmf_subcategory_suggested_actions"] = actions
    documents = [
        {"ai_rmf_documentation_id": p["id"], "description": p["prose"]}
        for p in parts
        if p.get("class") == "documentation"
    ]
    if documents:
        record["ai_rmf_subcategory_documentation"] = documents
    for rel, key in (
        ("resource", "ai_rmf_subcategory_transparency_resources"),
        ("reference", "ai_rmf_subcategory_references"),
    ):
        links = [
            _resource(link["href"].removeprefix("#"), resources)
            for link in control.get("links", [])
            if link["rel"] == rel
        ]
        if links:
            record[key] = links
    names = actor_names()
    actors = [names[tag] for tag in playbook["AI Actors"] if tag not in NOT_AN_ACTOR]
    if actors:
        record["ai_rmf_subcategory_ai_actors"] = actors
    if playbook["Topic"]:
        record["ai_rmf_subcategory_topics"] = playbook["Topic"]
    return record


def core() -> list[dict]:
    """The four functions in the publication's order, with everything under them."""
    catalog = json.loads(OSCAL.read_text(encoding="utf-8"))["catalog"]
    playbook = {
        entry["title"]: entry for entry in json.loads(PLAYBOOK.read_text(encoding="utf-8"))
    }
    resources = {r["uuid"]: r for r in catalog["back-matter"]["resources"]}
    groups = {group["id"]: group for group in catalog["groups"]}
    categories, subcategories = publication_statements()
    functions = []
    for name in FUNCTIONS:
        group = groups[name]
        overview = next(p["prose"] for p in group["parts"] if p["name"] == "overview")
        function = {
            "ai_rmf_function_id": name,
            "description": overview,
            "ai_rmf_function_categories": [],
        }
        for control in group["controls"]:
            category = {
                "ai_rmf_category_id": control["title"],
                "description": categories[control["title"]],
                "ai_rmf_category_subcategories": [
                    subcategory_record(
                        sub, subcategories[sub["title"]], playbook[sub["title"]], resources
                    )
                    for sub in control["controls"]
                ],
            }
            function["ai_rmf_function_categories"].append(category)
        functions.append(function)
    return functions


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--check", action="store_true", help="compare, and write nothing")
    args = parser.parse_args()
    document = yaml.safe_load(CATALOGUE.read_text(encoding="utf-8"))
    built = core()
    if args.check:
        if document["ai_rmf_functions"] != built:
            print(f"{CATALOGUE} differs from what upstream/ gives", file=sys.stderr)
            return 1
        return 0
    document["ai_rmf_functions"] = built
    CATALOGUE.write_text(
        yaml.safe_dump(document, sort_keys=False, allow_unicode=True, width=100), encoding="utf-8"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
