## Add your own just recipes here. This is imported by the main justfile.

# Overriding recipes from the root justfile by adding a recipe with the same
# name in this file is not possible until a known issue in just is fixed,
# https://github.com/casey/just/issues/2540

# ============================================================================
# Test-data fixtures
#
# Hand-curated example instances live under:
#   tests/data/valid/    - must validate against the schema
#   tests/data/invalid/  - must fail validation (counter-examples)
#
# Filename-stem convention: `<TargetClass>-<short-description>.yaml` so the
# class is auto-derived by `linkml-run-examples` and by `tests/test_data.py`.
#
# The root `justfile` already runs both directories through
# `linkml-run-examples` as part of `_test-examples` (a dep of `just test`).
# The recipes below give finer-grained entry points for ad-hoc work.
# ============================================================================

# Validate every fixture under tests/data/valid against the schema
[group('model development')]
validate-test-data:
  @for f in tests/data/valid/*.yaml; do \
    tc=$(basename "$f" | cut -d- -f1); \
    printf "%-70s " "$f [$tc]"; \
    if uv run linkml-validate -s {{source_schema_path}} --target-class $tc "$f" >/dev/null 2>&1; then \
      echo OK; \
    else \
      echo FAIL; \
      uv run linkml-validate -s {{source_schema_path}} --target-class $tc "$f"; \
      exit 1; \
    fi; \
  done

# Confirm every fixture under tests/data/invalid actually fails validation
[group('model development')]
validate-counter-examples:
  @for f in tests/data/invalid/*.yaml; do \
    tc=$(basename "$f" | cut -d- -f1); \
    printf "%-70s " "$f [$tc]"; \
    if uv run linkml-validate -s {{source_schema_path}} --target-class $tc "$f" >/dev/null 2>&1; then \
      echo "UNEXPECTED-PASS"; exit 1; \
    else \
      echo "fails (expected)"; \
    fi; \
  done

# Run both fixture suites
[group('model development')]
test-data: validate-test-data validate-counter-examples

# ============================================================================
# Cross-vocabulary mappings (SSSOM)
#
# Mappings between schema elements and external vocabularies live in
# `src/nist_ai_100_1/mappings/*.sssom.tsv`. The verifier confirms each
# schema's `*_mappings:` fields are in sync with the TSV.
# ============================================================================

# Verify that *_mappings: fields in the schemas match the SSSOM TSV
[group('model development')]
verify-mappings:
  uv run python scripts/verify_mappings.py

# Strict variant - also fail if the schema has mappings that the TSV omits
[group('model development')]
verify-mappings-strict:
  uv run python scripts/verify_mappings.py --strict

# ============================================================================
# Third-party data fixtures
#
# NIST refreshes the AI RMF Playbook ~twice a year. The JSON is held under
# `tests/data/third_party/nist/` and validated via the recipes below.
#
# - `just validate-nist-playbook`  - validate the current local copy
# - `just refresh-nist-playbook`   - re-fetch from upstream and re-validate
# - `just dump-nist-playbook`      - write the transformed payload to disk
# ============================================================================

# Local path to the third-party NIST AI RMF Playbook JSON
playbook_path := "tests/data/third_party/nist/nist_ai_rmf_playbook.json"

# Upstream URL for the playbook (kept here so refreshes are reproducible)
playbook_url := "https://airc.nist.gov/AI_RMF_Knowledge_Base/Playbook/data.json"

# Validate the NIST AI RMF Playbook JSON against the schema
[group('model development')]
validate-playbook:
  uv run python scripts/validate_nist_playbook.py {{playbook_path}}

# Run only the third-party fixture tests (separate pytest invocation so
# the green per-source record-count summary stays visible).
[group('model development')]
test-third-party:
  FORCE_COLOR=1 uv run python -m pytest \
    --override-ini="addopts=" \
    tests/test_third_party_data.py -v

# Re-fetch the Playbook JSON from NIST and validate it
[group('third-party data')]
refresh-nist-playbook:
  @mkdir -p $(dirname {{playbook_path}})
  curl -fsSL {{playbook_url}} -o {{playbook_path}}
  @echo "Fetched playbook to {{playbook_path}}"
  @just validate-playbook

# Dump the transformed (renamed + wrapped) payload for inspection
[group('third-party data')]
dump-nist-playbook output="tmp/playbook-transformed.json":
  @mkdir -p $(dirname {{output}})
  uv run python scripts/validate_playbook.py \
      --keep-transformed {{output}} {{playbook_path}}
  @echo "Wrote transformed playbook to {{output}}"