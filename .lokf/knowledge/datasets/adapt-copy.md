---
type: Dataset
id: https://w3id.org/lmodel/nist-ai-100-1/knowledge/datasets/adapt-copy
genre: reference
title: The schema's adapt copy
description: "`.lokf/schema/nist-ai-100-1.yaml`, the copy `just lokf-adapt` writes from the schema so that it sits beside LOKF's `lokf.yaml`: 13 classes rooted on `Concept`, `ai_rmf_id` dropped for LOKF's `id`, and `title` and `description` folded into LOKF's."
resource: .lokf/schema/nist-ai-100-1.yaml
derivedFrom:
  - https://w3id.org/lmodel/nist-ai-100-1/knowledge/datasets/nist-ai-100-1-linkml-schema
about:
  - https://w3id.org/lmodel/nist-ai-100-1/knowledge/glossary/adapt-copy
sources:
  - id: project.justfile
    resource: project.justfile
    title: the comment above the recipes
  - id: readme.md
    resource: README.md
    title: the Knowledge Trust Ladder (KTL) section
  - resource: .lokf/schema/nist-ai-100-1.yaml
  - resource: .lokf/justfile
    title: the schema line
  - resource: .lokf/pyproject.toml
    title: the schema setting
generated:
  by: process:ktl-librarian
  at: "2026-11-06T21:22:01Z"
status: draft
---

# The schema's adapt copy

`just lokf-adapt` writes `.lokf/schema/nist-ai-100-1.yaml` from the umbrella, and `just lokf-adapt-check` fails when it is stale. CI runs the check.[^project.justfile]

The roots are what the publication lists, and `AiRmfRecord` with the classes under it. The README lists them for the *Known LOKF types* setting.[^readme.md]

A release attaches the copy as `schema-<tag>-nist-ai-100-1.yaml`.[^readme.md]

[^project.justfile]: project.justfile, the comment above the recipes
[^readme.md]: README.md, the Knowledge Trust Ladder (KTL) section
