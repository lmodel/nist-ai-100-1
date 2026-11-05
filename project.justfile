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
