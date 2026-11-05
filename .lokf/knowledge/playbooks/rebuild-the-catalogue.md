---
type: Playbook
id: https://w3id.org/lmodel/nist-ai-100-1/knowledge/playbooks/rebuild-the-catalogue
genre: how-to
title: Rebuild the catalogue
description: "How to refresh the Core of `src/nist_ai_100_1/data/ai-rmf-1.0.yaml`: run `just build-catalogue` after a change in `upstream/`, read the diff, and run `just test`. `just check-catalogue` compares without writing."
references:
  - https://w3id.org/lmodel/nist-ai-100-1/knowledge/datasets/catalogue
sources:
  - id: builder
    resource: scripts/build_catalogue.py
    title: the docstring
  - id: test_catalogue.py
    resource: tests/test_catalogue.py
    title: test_catalog_departs_from_the_publication_only_as_listed
generated:
  by: process:ktl-librarian
  at: "2026-11-05T02:56:32Z"
status: draft
---

# Rebuild the catalogue

1. Run `just build-catalogue`. It writes the Core and leaves Part 1 and the appendices as they are.[^builder]
2. Read the diff. A new difference from the publication fails `tests/test_catalogue.py` until `tests/catalog_departures.yaml` lists it.[^test_catalogue.py]
3. Run `just test`.[^test_catalogue.py]

[^builder]: scripts/build_catalogue.py, the docstring
[^test_catalogue.py]: tests/test_catalogue.py, test_catalog_departs_from_the_publication_only_as_listed
