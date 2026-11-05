---
type: Explanation
id: https://w3id.org/lmodel/nist-ai-100-1/knowledge/explanations/mappings
genre: explanation
title: Mappings
description: "What the schema crosses to: lmodel/oscal, lmodel/nist-csf-v2, lmodel/iso27001 and PROV, each read at its source. The two SSSOM sets are gone, because their rows came from a matching tool and no source confirmed them."
references:
  - https://w3id.org/lmodel/nist-ai-100-1/knowledge/datasets/neighbour-copies
sources:
  - id: readme.md
    resource: README.md
    title: Mappings
  - id: test_schema_rules.py
    resource: tests/test_schema_rules.py
    title: test_mappings_name_a_class_of_the_neighbour
generated:
  by: process:ktl-librarian
  at: "2026-11-05T02:56:32Z"
status: draft
---

# Mappings

`broad_mappings` name OSCAL's classes for the framework, a function, a category, a subcategory, a Playbook item and a resource. `related_mappings` name CSF 2.0's function, category and subcategory, since Appendix B says the frameworks share that structure.[^readme.md]

A risk has `related_mappings` to `iso27001:IsmsRisk`, and an AI actor `broad_mappings` to `prov:Agent`.[^readme.md]

`tests/test_schema_rules.py` holds each lmodel mapping to a released copy.[^test_schema_rules.py]

[^readme.md]: README.md, Mappings
[^test_schema_rules.py]: tests/test_schema_rules.py, test_mappings_name_a_class_of_the_neighbour
