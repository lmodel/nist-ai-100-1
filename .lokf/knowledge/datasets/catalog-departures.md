---
type: Dataset
id: https://w3id.org/lmodel/nist-ai-100-1/knowledge/datasets/catalog-departures
genre: reference
title: Where NIST's catalog departs from the publication
description: "`tests/catalog_departures.yaml`: the 44 of 91 statements that NIST's OSCAL catalog words differently from Tables 1 to 4 of the publication, each with both wordings. `tests/test_catalogue.py` fails on a new difference."
resource: tests/catalog_departures.yaml
about:
  - https://w3id.org/lmodel/nist-ai-100-1/knowledge/references/oscal-catalog
  - https://w3id.org/lmodel/nist-ai-100-1/knowledge/references/nist-ai-100-1
sources:
  - id: departures
    resource: tests/catalog_departures.yaml
  - id: about
    resource: docs/about.md
    title: Where each part comes from
generated:
  by: process:ktl-librarian
  at: "2026-11-05T02:56:32Z"
status: draft
---

# Where NIST's catalog departs from the publication

Some differences are spacing and capitals. Others change a word: MEASURE 2.6 says "implicate" where the publication says "reflect", and GOVERN 1.2 drops "and practices".[^departures]

The catalogue keeps the publication's words.[^about]

[^departures]: tests/catalog_departures.yaml
[^about]: docs/about.md, Where each part comes from
