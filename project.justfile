## Add your own just recipes here. This is imported by the main justfile.

# Overriding recipes from the root justfile by adding a recipe with the same
# name in this file is not possible until a known issue in just is fixed,
# https://github.com/casey/just/issues/2540

# ============ The catalogue ============

# Write the Core into src/nist_ai_100_1/data/ai-rmf-1.0.yaml from upstream/
[group('model development')]
build-catalogue:
  uv run python scripts/build_catalogue.py

# Fail when the catalogue's Core differs from what upstream/ gives
[group('model development')]
check-catalogue:
  uv run python scripts/build_catalogue.py --check

# ============ Knowledge bundle: the adapted domain schema ============

# `.lokf/nist-ai-100-1.yaml` is the copy `lokf adapt` writes from the schema so
# that it can sit beside `.lokf/lokf.yaml` (`lokf adapt --help` lists the
# moves). The roots are the classes a knowledge concept may use as its `type`:
# what the publication lists, and AiRmfRecord with every class under it for
# what an adopter records. The recipes run the `lokf` the sidecar's floor pins
# (0.9.0 or later); LOKF_CMD runs another, such as a checkout:
# LOKF_CMD="uv run --project ../lokf lokf" just lokf-adapt
lokf_cmd := env_var_or_default("LOKF_CMD", "uv run --project .lokf lokf")
lokf_adapt_roots := "--root AiRmfFunction --root AiRmfCategory --root AiRmfSubcategory --root AiRmfTrustworthinessCharacteristic --root AiRmfDimension --root AiRmfLifecycleStage --root AiRmfActorTask --root AiRmfManagementChallenge --root AiRmfMeasurementChallenge --root AiRmfSpecificRisk --root AiRmfHumanAiIssue --root AiRmfAttribute --root AiRmfRecord"

# Rewrite .lokf/nist-ai-100-1.yaml from the schema (run after every schema change)
[group('knowledge bundle')]
lokf-adapt:
  {{lokf_cmd}} adapt {{source_schema_path}} {{lokf_adapt_roots}} --lokf .lokf/lokf.yaml -o .lokf/nist-ai-100-1.yaml

# Fail when .lokf/nist-ai-100-1.yaml is stale against the schema or .lokf/lokf.yaml
[group('knowledge bundle')]
lokf-adapt-check:
  {{lokf_cmd}} adapt {{source_schema_path}} {{lokf_adapt_roots}} --lokf .lokf/lokf.yaml -o .lokf/nist-ai-100-1.yaml --check
