"""Checks that upstream/ holds the edition the schema renders.

upstream/ holds the publication, NIST's catalog of it in OSCAL with its licence, and the
AI RMF Playbook's file, as NIST publishes them. scripts/check_upstream_release.py compares
them with NIST's own copies. These tests make the same comparison offline.
"""

import hashlib
import importlib.util
import json
from functools import lru_cache
from pathlib import Path

import yaml

ROOT = Path(__file__).parent.parent
UPSTREAM = ROOT / "upstream"
SCHEMA = ROOT / "src" / "nist_ai_100_1" / "schema" / "nist_ai_100_1.yaml"
WATCH = ROOT / "scripts" / "check_upstream_release.py"


@lru_cache(maxsize=1)
def _watch():
    spec = importlib.util.spec_from_file_location("watch_pins", WATCH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _header():
    return yaml.safe_load(SCHEMA.read_text(encoding="utf-8"))


def _catalog():
    path = UPSTREAM / "oscal-content" / "NIST_AI-RMF_v1_catalog.json"
    return json.loads(path.read_text(encoding="utf-8"))["catalog"]


def _prop(metadata, name):
    return next(p["value"] for p in metadata["props"] if p["name"] == name)


def test_upstream_holds_only_the_pinned_files():
    """Every file in upstream/ is pinned, and nothing else is there."""
    watch = _watch()
    pinned = {f"oscal-content/{name}" for name in watch.PINNED_BLOBS}
    pinned |= set(watch.PINNED_DOWNLOADS)
    found = {
        str(path.relative_to(UPSTREAM))
        for path in UPSTREAM.rglob("*")
        if path.is_file()
    }
    assert found == pinned


def test_copies_match_the_pinned_blobs():
    """Each file from oscal-content has the git object hash the watch pins."""
    watch = _watch()
    for name, (_source, sha) in watch.PINNED_BLOBS.items():
        assert watch._blob_sha(UPSTREAM / "oscal-content" / name) == sha, name


def test_downloads_match_their_pins():
    """The publication and the Playbook have the SHA-256 the watch pins."""
    watch = _watch()
    for name, (_url, sha256) in watch.PINNED_DOWNLOADS.items():
        assert hashlib.sha256((UPSTREAM / name).read_bytes()).hexdigest() == sha256, (
            name
        )


def test_header_pins_match_the_watch():
    """The header records the release, commit and publication the watch checks."""
    watch = _watch()
    header = _header()
    notes = header["annotations"]
    assert notes["oscal_content_tag"] == watch.PINNED_TAG
    assert notes["oscal_content_commit"] == watch.PINNED_COMMIT
    assert header["source"] == f"https://doi.org/{watch.PINNED_DOI}"
    tree = f"https://github.com/usnistgov/oscal-content/tree/{watch.PINNED_TAG}/"
    assert tree + watch.PINNED_PATH.rpartition("/")[0] in header["see_also"]


def test_catalog_is_the_pinned_edition():
    """The copy is NIST's final catalog of the edition in the header."""
    metadata = _catalog()["metadata"]
    header = _header()
    assert metadata["version"] == header["version"]
    identifier = "AI_100_" + header["version"].replace(".", "_")
    assert header["annotations"]["cprt_framework_version"] == identifier
    assert _prop(metadata, "framework-version-identifier") == identifier
    assert _prop(metadata, "publication-status") == "Final"


def test_every_module_carries_the_header():
    """Each module carries the edition, the source and the licence of the umbrella."""
    header = _header()
    for path in SCHEMA.parent.glob("*.yaml"):
        module = yaml.safe_load(path.read_text(encoding="utf-8"))
        for key in ("version", "source", "license"):
            assert module[key] == header[key], (path.name, key)
