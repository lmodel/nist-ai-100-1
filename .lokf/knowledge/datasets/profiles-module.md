---
type: Dataset
id: https://w3id.org/lmodel/nist-ai-100-1/knowledge/datasets/profiles-module
genre: reference
title: Profiles module
description: "`nist_ai_100_1_profiles.yaml`: `AiRmfProfile` and `AiRmfProfileKind`, for the use-case, current, target and cross-sectoral profiles of section 6. The publication prescribes no template, so only the kinds and the subcategories are structured."
resource: src/nist_ai_100_1/schema/nist_ai_100_1_profiles.yaml
isPartOf:
  - https://w3id.org/lmodel/nist-ai-100-1/knowledge/datasets/nist-ai-100-1-linkml-schema
sources:
  - id: profiles
    resource: src/nist_ai_100_1/schema/nist_ai_100_1_profiles.yaml
generated:
  by: process:ktl-librarian
  at: "2026-11-05T02:56:32Z"
status: draft
---

# Profiles module

`AiRmfProfile` is a record with at least one kind, a setting and the subcategories it selects.[^profiles]

The kinds are a list because a current profile of one use case is both.[^profiles]

[^profiles]: src/nist_ai_100_1/schema/nist_ai_100_1_profiles.yaml
