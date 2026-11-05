---
type: Dataset
id: https://w3id.org/lmodel/nist-ai-100-1/knowledge/datasets/upstream-copy
genre: reference
title: Copy of the upstream
description: "`upstream/`: the publication's PDF, NIST's OSCAL catalog with its licence, and the Playbook's file, unchanged. `scripts/check_upstream_release.py` pins each by hash, and `tests/test_upstream.py` compares them offline."
resource: upstream
about:
  - https://w3id.org/lmodel/nist-ai-100-1/knowledge/references/nist-ai-100-1
  - https://w3id.org/lmodel/nist-ai-100-1/knowledge/references/oscal-catalog
  - https://w3id.org/lmodel/nist-ai-100-1/knowledge/references/ai-rmf-playbook
sources:
  - id: watch
    resource: scripts/check_upstream_release.py
    title: the pins
  - id: test_upstream.py
    resource: tests/test_upstream.py
  - resource: upstream
generated:
  by: process:ktl-librarian
  at: "2026-11-05T02:56:32Z"
status: draft
---

# Copy of the upstream

The catalog and its licence are pinned by git object hash at usnistgov/oscal-content v1.6.0. The publication and the Playbook are pinned by SHA-256, as of 2026-11-05.[^watch]

`tests/test_upstream.py` fails on a file that differs or a file nobody pinned.[^test_upstream.py]

[^watch]: scripts/check_upstream_release.py, the pins
[^test_upstream.py]: tests/test_upstream.py
