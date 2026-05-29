"""Third-party data tests.

Validates JSON fixtures supplied by external publishers (e.g., NIST)
that live under ``tests/data/third_party/<publisher>/``.

The NIST AI RMF Playbook is published as a top-level JSON array with
attribute keys containing spaces (``"AI Actors"``, ``"Topic"``). It is
transformed in-memory via :mod:`scripts.validate_playbook` and then
validated against the ``PlaybookCollection`` class so the upstream
file is never edited.

Any additional ``<TargetClass>-<short-description>.json`` files dropped
into ``tests/data/third_party/nist/`` are auto-discovered and validated
directly (no transform).
"""

from __future__ import annotations

import glob
import importlib.util
import json
import os
import sys
import tempfile
from pathlib import Path

import pytest

import nist_ai_100_1.datamodel.nist_ai_100_1
from linkml_runtime.loaders import json_loader

REPO_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR_THIRD_PARTY = REPO_ROOT / "tests" / "data" / "third_party" / "nist"
PLAYBOOK_JSON = DATA_DIR_THIRD_PARTY / "nist_ai_rmf_playbook.json"

# Per-fixture record counts, harvested by the `pytest_terminal_summary`
# hook in conftest.py to print a green per-source summary at the end of
# the (separate) third-party pytest run.
THIRD_PARTY_RECORD_COUNTS: dict[str, int] = {}


def _load_validate_playbook_module():
    """Import ``scripts/validate_playbook.py`` without a package init."""
    spec = importlib.util.spec_from_file_location(
        "_validate_playbook", REPO_ROOT / "scripts" / "validate_playbook.py"
    )
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


@pytest.mark.skipif(
    not PLAYBOOK_JSON.exists(),
    reason=f"NIST AI RMF Playbook JSON not present at {PLAYBOOK_JSON}",
)
def test_nist_ai_rmf_playbook_validates():
    """Transform the upstream Playbook JSON and validate it as a PlaybookCollection."""
    vp = _load_validate_playbook_module()
    payload = vp.load_and_transform(PLAYBOOK_JSON)

    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".json", prefix="playbook-", delete=False
    ) as tmp:
        json.dump(payload, tmp)
        tmp_path = Path(tmp.name)
    try:
        obj = json_loader.load(
            str(tmp_path),
            target_class=nist_ai_100_1.datamodel.nist_ai_100_1.PlaybookCollection,
        )
    finally:
        tmp_path.unlink(missing_ok=True)
    assert obj
    assert obj.entries, "Playbook payload contained no entries"
    THIRD_PARTY_RECORD_COUNTS[PLAYBOOK_JSON.name] = len(obj.entries)


# Auto-discover any other third-party JSON fixtures that follow the
# `<TargetClass>-<desc>.json` filename convention used by the YAML
# fixtures. The upstream Playbook file above is excluded because it
# needs the dedicated transform.
_OTHER_THIRD_PARTY_JSON = [
    p
    for p in glob.glob(os.path.join(DATA_DIR_THIRD_PARTY, "*.json"))
    if Path(p).name != PLAYBOOK_JSON.name
]


@pytest.mark.parametrize("filepath", _OTHER_THIRD_PARTY_JSON)
def test_third_party_nist_json(filepath):
    """Validate a third-party NIST JSON fixture against the schema."""
    target_class_name = Path(filepath).stem.split("-")[0]
    tgt_class = getattr(
        nist_ai_100_1.datamodel.nist_ai_100_1,
        target_class_name,
    )
    obj = json_loader.load(filepath, target_class=tgt_class)
    assert obj
    # Best-effort record count for the summary: prefer a multivalued
    # container slot if present, otherwise fall back to "1 record".
    count = 1
    for attr in ("entries", "items", "records"):
        value = getattr(obj, attr, None)
        if isinstance(value, list):
            count = len(value)
            break
    THIRD_PARTY_RECORD_COUNTS[Path(filepath).name] = count
