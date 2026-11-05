"""Checks the whole catalogue against the schema, upstream/ and the publication.

src/nist_ai_100_1/data/ai-rmf-1.0.yaml holds the Core, which scripts/build_catalogue.py
writes from upstream/, and what Part 1 and the appendices list, written by hand.
"""

import importlib.util
import json
import re
from functools import lru_cache
from pathlib import Path

import jsonschema
import pytest
import yaml
from linkml.validator import validate
from linkml_runtime.loaders import yaml_loader
from linkml_runtime.utils.schemaview import SchemaView

import nist_ai_100_1.datamodel.nist_ai_100_1 as dataclasses_model
import nist_ai_100_1.datamodel.nist_ai_100_1_pydantic as pydantic_model

ROOT = Path(__file__).parent.parent
CATALOGUE = ROOT / "src" / "nist_ai_100_1" / "data" / "ai-rmf-1.0.yaml"
SCHEMA = ROOT / "src" / "nist_ai_100_1" / "schema" / "nist_ai_100_1.yaml"
JSON_SCHEMA = ROOT / "project" / "jsonschema" / "nist_ai_100_1.schema.json"
BUILDER = ROOT / "scripts" / "build_catalogue.py"
DEPARTURES = Path(__file__).parent / "catalog_departures.yaml"
UPSTREAM = ROOT / "upstream"

# The list each enum sorts, as a section of the catalogue and the key that names a record.
ENUM_RECORDS = {
    "AiRmfCharacteristicName": ("ai_rmf_characteristics", "ai_rmf_characteristic_name"),
    "AiRmfDimensionName": ("ai_rmf_dimensions", "ai_rmf_dimension_name"),
    "AiRmfLifecycleStageName": (
        "ai_rmf_lifecycle_stages",
        "ai_rmf_lifecycle_stage_name",
    ),
    "AiRmfActorTaskName": ("ai_rmf_actor_task_list", "ai_rmf_actor_task_name"),
    "AiRmfManagementChallengeName": (
        "ai_rmf_management_challenges",
        "ai_rmf_management_challenge_name",
    ),
}

# The publication's own counts. Only the figures say what lists Figures 2 and 3 hold.
COUNTS = {
    "ai_rmf_characteristics": 7,
    "ai_rmf_dimensions": 5,
    "ai_rmf_lifecycle_stages": 7,
    "ai_rmf_actor_task_list": 15,
    "ai_rmf_management_challenges": 4,
    "ai_rmf_specific_risks": 14,
    "ai_rmf_human_ai_issues": 4,
    "ai_rmf_attributes": 10,
}
CORE_COUNTS = {
    "GOVERN": (6, 19),
    "MAP": (5, 18),
    "MEASURE": (4, 22),
    "MANAGE": (4, 13),
}

# Enums whose titles the publication's running text states. The others are in figures.
TITLED_IN_TEXT = (
    "AiRmfCharacteristicName",
    "AiRmfActorTaskName",
    "AiRmfManagementChallengeName",
    "AiRmfMeasurementChallengeName",
)

# Where the catalog's suggested actions differ from the Playbook's: it leaves some out,
# files MANAGE 4.2's under the discussion, or words them differently. upstream/ keeps both.
ACTIONS_DIFFER_FROM_PLAYBOOK = {
    "GOVERN 1.2",
    "GOVERN 1.4",
    "GOVERN 1.7",
    "GOVERN 2.2",
    "GOVERN 2.3",
    "GOVERN 3.1",
    "GOVERN 5.2",
    "MANAGE 2.1",
    "MANAGE 2.2",
    "MANAGE 4.2",
    "MAP 1.1",
    "MAP 5.1",
    "MEASURE 1.3",
    "MEASURE 2.1",
    "MEASURE 2.10",
    "MEASURE 2.11",
}


@lru_cache(maxsize=1)
def _builder():
    spec = importlib.util.spec_from_file_location("build_catalogue", BUILDER)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@lru_cache(maxsize=1)
def _doc():
    return yaml.safe_load(CATALOGUE.read_text(encoding="utf-8"))


@lru_cache(maxsize=1)
def _view():
    return SchemaView(str(SCHEMA))


@lru_cache(maxsize=1)
def _oscal():
    path = UPSTREAM / "oscal-content" / "NIST_AI-RMF_v1_catalog.json"
    return json.loads(path.read_text(encoding="utf-8"))["catalog"]


def _words(text):
    """A text's words, lower-cased and each between spaces, so a title matches whole
    words and line breaks and hyphens fall away."""
    return (
        " " + " ".join(re.findall(r"[a-z0-9]+", re.sub(r"-\n", "", text.lower()))) + " "
    )


@lru_cache(maxsize=1)
def _publication_words():
    """The publication's words."""
    import pdfplumber

    with pdfplumber.open(UPSTREAM / "NIST.AI.100-1.pdf") as pdf:
        return _words(
            "\n".join(page.extract_text(x_tolerance=1) or "" for page in pdf.pages)
        )


def _subcategories():
    for function in _doc()["ai_rmf_functions"]:
        for category in function["ai_rmf_function_categories"]:
            yield from category["ai_rmf_category_subcategories"]


def _oscal_controls():
    for group in _oscal()["groups"]:
        for category in group["controls"]:
            yield category
            yield from category["controls"]


def test_catalogue_passes_the_validator():
    """`linkml-validate` passes the whole catalogue, with its format checks."""
    report = validate(_doc(), str(SCHEMA), "AiRmfFramework")
    assert not report.results, [r.message for r in report.results][:5]


def test_catalogue_passes_the_committed_json_schema():
    """The JSON Schema a consumer takes from project/ passes it too."""
    schema = json.loads(JSON_SCHEMA.read_text(encoding="utf-8"))
    errors = list(jsonschema.Draft202012Validator(schema).iter_errors(_doc()))
    assert not errors, [e.message for e in errors][:5]


def test_generated_models_load_the_catalogue():
    """The generated dataclasses and Pydantic models load all of it."""
    framework = yaml_loader.load(
        str(CATALOGUE), target_class=dataclasses_model.AiRmfFramework
    )
    assert len(framework.ai_rmf_functions) == 4
    assert (
        len(pydantic_model.AiRmfFramework.model_validate(_doc()).ai_rmf_functions) == 4
    )


def test_core_is_what_upstream_gives():
    """The catalogue's Core is what the builder writes from upstream/."""
    assert _doc()["ai_rmf_functions"] == _builder().core()


def test_counts_are_the_publications():
    """Four functions, 19 categories and 72 subcategories, and each list's length."""
    for section, count in COUNTS.items():
        assert len(_doc()[section]) == count, section
    found = {
        function["ai_rmf_function_id"]: (
            len(function["ai_rmf_function_categories"]),
            sum(
                len(category["ai_rmf_category_subcategories"])
                for category in function["ai_rmf_function_categories"]
            ),
        )
        for function in _doc()["ai_rmf_functions"]
    }
    assert found == CORE_COUNTS
    assert list(found) == list(CORE_COUNTS)


def test_identifiers_nest():
    """A category names its function, and a subcategory its category, in order."""
    for function in _doc()["ai_rmf_functions"]:
        name = function["ai_rmf_function_id"]
        for number, category in enumerate(function["ai_rmf_function_categories"], 1):
            assert category["ai_rmf_category_id"] == f"{name} {number}"
            for inner, sub in enumerate(category["ai_rmf_category_subcategories"], 1):
                assert sub["ai_rmf_subcategory_id"] == f"{name} {number}.{inner}"


@pytest.mark.parametrize("enum", ENUM_RECORDS)
def test_each_enum_value_has_one_record(enum):
    """An enum and the list it names hold the same values, in the same order."""
    section, key = ENUM_RECORDS[enum]
    values = list(_view().get_enum(enum).permissible_values)
    assert [record[key] for record in _doc()[section]] == values


def test_measurement_challenges_sit_under_risk_measurement():
    """Section 1.2.1 lists them, so only that challenge holds them, and each once."""
    holders = [
        record
        for record in _doc()["ai_rmf_management_challenges"]
        if "ai_rmf_management_challenge_measurement_challenges" in record
    ]
    assert [h["ai_rmf_management_challenge_name"] for h in holders] == [
        "risk_measurement"
    ]
    names = [
        item["ai_rmf_measurement_challenge_name"]
        for item in holders[0]["ai_rmf_management_challenge_measurement_challenges"]
    ]
    enum = _view().get_enum("AiRmfMeasurementChallengeName")
    assert names == list(enum.permissible_values)


def test_lists_number_from_one():
    """Each numbered list counts from one with no gap."""
    for section, key in (
        ("ai_rmf_specific_risks", "ai_rmf_specific_risk_position"),
        ("ai_rmf_human_ai_issues", "ai_rmf_human_ai_issue_number"),
        ("ai_rmf_attributes", "ai_rmf_attribute_number"),
    ):
        numbers = [record[key] for record in _doc()[section]]
        assert numbers == list(range(1, len(numbers) + 1)), section


def test_figure_four_marks_two_characteristics():
    """Valid and Reliable is the base, and Accountable and Transparent relates to all."""
    base = [
        r["ai_rmf_characteristic_name"]
        for r in _doc()["ai_rmf_characteristics"]
        if r.get("ai_rmf_characteristic_is_base")
    ]
    related = [
        r["ai_rmf_characteristic_name"]
        for r in _doc()["ai_rmf_characteristics"]
        if r.get("ai_rmf_characteristic_relates_to_all")
    ]
    assert base == ["valid_and_reliable"]
    assert related == ["accountable_and_transparent"]


@pytest.mark.parametrize("enum", TITLED_IN_TEXT)
def test_titles_are_the_publications(enum):
    """Each title is the publication's wording, so a typing slip fails here."""
    words = _publication_words()
    for value, entry in _view().get_enum(enum).permissible_values.items():
        if value == "tevv":
            continue  # Appendix A writes this title with its bold running on.
        assert _words(entry.title) in words, (enum, value)


def test_catalog_departs_from_the_publication_only_as_listed():
    """NIST's catalog restates the Tables' statements with differences in 44 of the 91.

    The catalogue keeps the publication's words. Each difference is listed with both
    wordings, so a new one in a later catalog fails here and gets read.
    """
    statements = {}
    for function in _doc()["ai_rmf_functions"]:
        for category in function["ai_rmf_function_categories"]:
            statements[category["ai_rmf_category_id"]] = category["description"]
            for sub in category["ai_rmf_category_subcategories"]:
                statements[sub["ai_rmf_subcategory_id"]] = sub["description"]
    found = {}
    for control in _oscal_controls():
        prose = next(
            p["prose"]
            for p in control["parts"]
            if p["name"] in ("overview", "statement") and p.get("prose")
        )
        if prose.split() != statements[control["title"]].split():
            found[control["title"]] = {
                "catalog": prose,
                "publication": statements[control["title"]],
            }
    assert found == yaml.safe_load(DEPARTURES.read_text(encoding="utf-8"))
    assert len(found) == 44


def test_catalog_actions_depart_from_the_playbook_only_as_listed():
    """The catalog's suggested actions match the Playbook's but for the listed ones."""
    playbook = json.loads((UPSTREAM / "playbook.json").read_text(encoding="utf-8"))
    letters = lambda text: re.sub(r"\W+", "", text).lower()  # noqa: E731
    by_title = {entry["title"]: letters(entry["section_actions"]) for entry in playbook}
    differing = set()
    for sub in _subcategories():
        actions = sub.get("ai_rmf_subcategory_suggested_actions", [])
        text = letters("".join(a["description"] for a in actions))
        if text != by_title[sub["ai_rmf_subcategory_id"]]:
            differing.add(sub["ai_rmf_subcategory_id"])
    assert differing == ACTIONS_DIFFER_FROM_PLAYBOOK


def test_every_playbook_tag_has_a_home():
    """Each AI actor tag names a value, but for the one topic filed under AI Actors."""
    builder = _builder()
    names = builder.actor_names()
    playbook = json.loads((UPSTREAM / "playbook.json").read_text(encoding="utf-8"))
    stray = {
        (entry["title"], tag)
        for entry in playbook
        for tag in entry["AI Actors"]
        if tag not in names
    }
    assert stray == {("GOVERN 4.3", "Fairness and Bias")}
    assert builder.NOT_AN_ACTOR == {"Fairness and Bias"}


def test_a_new_catalog_resource_is_read():
    """Only the catalog's N/A addresses go without an address."""
    empty = [
        r
        for r in _oscal()["back-matter"]["resources"]
        if r["rlinks"][0]["href"] == "N/A"
    ]
    assert len(empty) == 19
    for sub in _subcategories():
        for key in (
            "ai_rmf_subcategory_transparency_resources",
            "ai_rmf_subcategory_references",
        ):
            for resource in sub.get(key, []):
                assert resource.get("ai_rmf_resource_address", "https://").startswith(
                    "http"
                )
