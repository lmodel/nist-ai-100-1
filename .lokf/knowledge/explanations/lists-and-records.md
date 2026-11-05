---
type: Explanation
id: https://w3id.org/lmodel/nist-ai-100-1/knowledge/explanations/lists-and-records
genre: explanation
title: What the publication lists and what an adopter records
description: "Two groups of classes in one schema: those that render what the publication lists, with one record per item in the catalogue, and those under `AiRmfRecord` for an adopter's own AI systems, risks and profiles, which the publication holds none of."
references:
  - https://w3id.org/lmodel/nist-ai-100-1/knowledge/datasets/catalogue
  - https://w3id.org/lmodel/nist-ai-100-1/knowledge/datasets/foundations-module
sources:
  - id: about
    resource: docs/about.md
    title: How the classes fit together
generated:
  by: process:ktl-librarian
  at: "2026-11-05T02:56:32Z"
status: draft
---

# What the publication lists and what an adopter records

Classes such as `AiRmfSubcategory` and `AiRmfLifecycleStage` have records in the catalogue.[^about]

Classes under `AiRmfRecord` have none. An adopter gives each record an identifier, so that one can name another, as a risk names its system.[^about]

[^about]: docs/about.md, How the classes fit together
