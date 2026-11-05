---
type: Dataset
id: https://w3id.org/lmodel/nist-ai-100-1/knowledge/datasets/rmf-core-module
genre: reference
title: AI RMF Core module
description: "`nist_ai_100_1_rmf_core.yaml`: `AiRmfFunction`, `AiRmfCategory` and `AiRmfSubcategory`, with the Playbook material a subcategory holds, in `AiRmfSuggestedAction`, `AiRmfDocumentationItem` and `AiRmfResource`."
resource: src/nist_ai_100_1/schema/nist_ai_100_1_rmf_core.yaml
isPartOf:
  - https://w3id.org/lmodel/nist-ai-100-1/knowledge/datasets/nist-ai-100-1-linkml-schema
sources:
  - id: core
    resource: src/nist_ai_100_1/schema/nist_ai_100_1_rmf_core.yaml
generated:
  by: process:ktl-librarian
  at: "2026-11-05T02:56:32Z"
status: draft
---

# AI RMF Core module

A function holds its categories, and a category its subcategories. A subcategory's identifier and statement come from the publication.[^core]

Everything else on a subcategory comes from the Playbook: discussion, suggested actions, documentation prompts, transparency resources, references, AI actors and topics.[^core]

A suggested action's identifier may carry further numbers, as in `SA-GOVERN_1.4-1.2`, which mark a sub-item.[^core]

[^core]: src/nist_ai_100_1/schema/nist_ai_100_1_rmf_core.yaml
