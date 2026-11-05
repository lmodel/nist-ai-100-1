---
type: Dataset
id: https://w3id.org/lmodel/nist-ai-100-1/knowledge/datasets/base-module
genre: reference
title: Base module
description: "`nist_ai_100_1_base.yaml`, the slice a profile can import alone: the identifier forms, the enums of trustworthiness characteristics and AI actor tasks, the `title` and `description` slots, and the abstract `AiRmfRecord`."
resource: src/nist_ai_100_1/schema/nist_ai_100_1_base.yaml
isPartOf:
  - https://w3id.org/lmodel/nist-ai-100-1/knowledge/datasets/nist-ai-100-1-linkml-schema
sources:
  - id: base
    resource: src/nist_ai_100_1/schema/nist_ai_100_1_base.yaml
  - id: changelog
    resource: CHANGELOG.md
    title: Removed
generated:
  by: process:ktl-librarian
  at: "2026-11-05T02:56:32Z"
status: draft
---

# Base module

It holds three identifier types, for a function, a category and a subcategory, each a pattern on NIST's own form.[^base]

`AiRmfCharacteristicName` holds the seven characteristics, and `AiRmfActorTaskName` the ten tasks and five additional AI actors, with an alias for each spelling the Playbook and AI 600-1 use.[^base]

`AiRmfRecord` is the base of what an adopter records.[^base] lmodel/nist-ai-600-1 vendors this module and the profiles module.[^changelog]

[^base]: src/nist_ai_100_1/schema/nist_ai_100_1_base.yaml
[^changelog]: CHANGELOG.md, Removed
