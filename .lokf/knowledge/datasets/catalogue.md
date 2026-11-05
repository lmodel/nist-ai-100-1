---
type: Dataset
id: https://w3id.org/lmodel/nist-ai-100-1/knowledge/datasets/catalogue
genre: reference
title: The catalogue
description: "`src/nist_ai_100_1/data/ai-rmf-1.0.yaml`, the whole framework as one `AiRmfFramework` record: 4 functions, 19 categories, 72 subcategories, 575 suggested actions and 292 documentation prompts, and the lists of Part 1 and the appendices."
resource: src/nist_ai_100_1/data/ai-rmf-1.0.yaml
derivedFrom:
  - https://w3id.org/lmodel/nist-ai-100-1/knowledge/references/nist-ai-100-1
  - https://w3id.org/lmodel/nist-ai-100-1/knowledge/references/oscal-catalog
  - https://w3id.org/lmodel/nist-ai-100-1/knowledge/references/ai-rmf-playbook
sources:
  - id: builder
    resource: scripts/build_catalogue.py
    title: the docstring
  - id: test_catalogue.py
    resource: tests/test_catalogue.py
  - resource: project.justfile
    title: the catalogue recipes
generated:
  by: process:ktl-librarian
  at: "2026-11-05T02:56:32Z"
status: draft
---

# The catalogue

`scripts/build_catalogue.py` writes the Core: the statements from the publication's Tables 1 to 4, the rest from NIST's catalog, and the tags from the Playbook's file.[^builder]

Part 1 and the appendices are written by hand.[^builder]

`tests/test_catalogue.py` validates the file with `linkml-validate` and the committed JSON Schema, loads it into both generated models, and holds it to the publication's counts and titles.[^test_catalogue.py]

[^builder]: scripts/build_catalogue.py, the docstring
[^test_catalogue.py]: tests/test_catalogue.py
