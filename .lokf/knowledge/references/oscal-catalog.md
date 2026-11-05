---
type: Reference
id: https://w3id.org/lmodel/nist-ai-100-1/knowledge/references/oscal-catalog
genre: reference
title: NIST's catalog of the AI RMF in OSCAL
description: "NIST's Open Security Controls Assessment Language (OSCAL) catalog of the AI RMF 1.0 in usnistgov/oscal-content at v1.6.0: the Core with each function's overview and the Playbook's material, restated from the publication with some differences."
resource: upstream/oscal-content/NIST_AI-RMF_v1_catalog.json
about:
  - https://w3id.org/lmodel/nist-ai-100-1/knowledge/references/nist-ai-100-1
sources:
  - id: catalog
    resource: upstream/oscal-content/NIST_AI-RMF_v1_catalog.json
  - id: test_upstream.py
    resource: tests/test_upstream.py
    title: test_catalog_is_the_pinned_edition
  - id: licence
    resource: upstream/oscal-content/LICENSE.md
source:
  - https://github.com/usnistgov/oscal-content/tree/v1.6.0/nist.gov/AI100-1/ver1
generated:
  by: process:ktl-librarian
  at: "2026-11-05T02:56:32Z"
status: draft
---

# NIST's catalog of the AI RMF in OSCAL

The catalog holds 19 categories and 72 subcategories under four function groups, with suggested actions, discussion, documentation prompts and 418 back-matter resources.[^catalog]

Its metadata says version 1.0.0, status Final, and the identifier `AI_100_1_0_0`.[^test_upstream.py]

NIST dedicates the repository's work to the worldwide public domain under CC0 1.0.[^licence]

[^catalog]: upstream/oscal-content/NIST_AI-RMF_v1_catalog.json
[^test_upstream.py]: tests/test_upstream.py, test_catalog_is_the_pinned_edition
[^licence]: upstream/oscal-content/LICENSE.md
