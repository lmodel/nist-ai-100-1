---
type: Dataset
id: https://w3id.org/lmodel/nist-ai-100-1/knowledge/datasets/neighbour-copies
genre: reference
title: Neighbours' adapt copies
description: The adapt copies of 19 released lmodel repositories in `tests/neighbours/`, among them oscal, nist-csf-v2 and iso27001, each pinned by its SHA-256, against which `tests/test_schema_rules.py` holds this schema's copy apart and checks the mappings.
resource: tests/neighbours
references:
  - https://w3id.org/lmodel/nist-ai-100-1/knowledge/datasets/adapt-copy
sources:
  - id: test_schema_rules.py
    resource: tests/test_schema_rules.py
  - resource: tests/neighbours
generated:
  by: process:ktl-librarian
  at: "2026-11-05T02:56:32Z"
status: draft
---

# Neighbours' adapt copies

Each file is the schema asset of a lmodel release, pinned in `tests/test_schema_rules.py` by its checksum.[^test_schema_rules.py]

The test fails on a shared class, enum, type or subset, and on a shared key it does not list.[^test_schema_rules.py]

[^test_schema_rules.py]: tests/test_schema_rules.py
