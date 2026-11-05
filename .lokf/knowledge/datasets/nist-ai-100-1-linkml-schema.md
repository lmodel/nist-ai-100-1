---
type: Dataset
id: https://w3id.org/lmodel/nist-ai-100-1/knowledge/datasets/nist-ai-100-1-linkml-schema
genre: reference
title: nist-ai-100-1 LinkML schema
description: "The LinkML model of NIST AI 100-1, `src/nist_ai_100_1/schema/nist_ai_100_1.yaml`: an umbrella over four modules that holds the tree root `AiRmfFramework`, with the `AiRmf` class prefix and the `ai_rmf_` slot prefix."
resource: src/nist_ai_100_1/schema/nist_ai_100_1.yaml
derivedFrom:
  - https://w3id.org/lmodel/nist-ai-100-1/knowledge/references/nist-ai-100-1
hasPart:
  - https://w3id.org/lmodel/nist-ai-100-1/knowledge/datasets/base-module
  - https://w3id.org/lmodel/nist-ai-100-1/knowledge/datasets/foundations-module
  - https://w3id.org/lmodel/nist-ai-100-1/knowledge/datasets/rmf-core-module
  - https://w3id.org/lmodel/nist-ai-100-1/knowledge/datasets/profiles-module
sources:
  - id: schema
    resource: src/nist_ai_100_1/schema/nist_ai_100_1.yaml
  - id: test_upstream.py
    resource: tests/test_upstream.py
    title: test_header_pins_match_the_watch
generated:
  by: process:ktl-librarian
  at: "2026-11-05T02:56:32Z"
status: draft
---

# nist-ai-100-1 LinkML schema

The umbrella imports `nist_ai_100_1_base`, `nist_ai_100_1_foundations`, `nist_ai_100_1_rmf_core` and `nist_ai_100_1_profiles`, and declares `AiRmfFramework`, the document that holds one edition.[^schema]

The header's `version` is the edition and `source` the publication's digital object identifier. `tests/test_upstream.py` holds them to the watch's pins.[^test_upstream.py]

[^schema]: src/nist_ai_100_1/schema/nist_ai_100_1.yaml
[^test_upstream.py]: tests/test_upstream.py, test_header_pins_match_the_watch
