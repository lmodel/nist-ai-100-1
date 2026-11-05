---
type: Explanation
id: https://w3id.org/lmodel/nist-ai-100-1/knowledge/explanations/where-each-part-comes-from
genre: explanation
title: Where each part comes from
description: "NIST publishes the Core in three places that differ: the publication's tables, its OSCAL catalog and the Playbook's file. The publication decides a statement, the catalog gives the Playbook's material, and the Playbook's file gives the tags."
references:
  - https://w3id.org/lmodel/nist-ai-100-1/knowledge/datasets/catalogue
  - https://w3id.org/lmodel/nist-ai-100-1/knowledge/datasets/catalog-departures
sources:
  - id: about
    resource: docs/about.md
    title: Where each part comes from
  - id: builder
    resource: scripts/build_catalogue.py
    title: the docstring
generated:
  by: process:ktl-librarian
  at: "2026-11-05T02:56:32Z"
status: draft
---

# Where each part comes from

The schema renders the publication, so a statement in the catalogue is the publication's wording, although NIST's catalog differs in 44 of the 91.[^about]

The publication has no suggested actions, so those come from NIST's catalog. The catalog has no AI actor or topic tags, so those come from the Playbook's file.[^builder]

For 16 subcategories the catalog's suggested actions differ from the Playbook's. In MANAGE 4.2 the catalog files the actions under the discussion, and the catalogue keeps them there. `upstream/` holds both files.[^about]

[^about]: docs/about.md, Where each part comes from
[^builder]: scripts/build_catalogue.py, the docstring
