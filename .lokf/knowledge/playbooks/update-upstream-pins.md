---
type: Playbook
id: https://w3id.org/lmodel/nist-ai-100-1/knowledge/playbooks/update-upstream-pins
genre: how-to
title: Move to another edition
description: "How to move the schema when the watch reports a change: read what changed, then move `upstream/`, the pins in `scripts/check_upstream_release.py` and the schema headers together, and rebuild the catalogue."
references:
  - https://w3id.org/lmodel/nist-ai-100-1/knowledge/workflows/upstream-watch
  - https://w3id.org/lmodel/nist-ai-100-1/knowledge/datasets/upstream-copy
sources:
  - id: watch
    resource: scripts/check_upstream_release.py
    title: the pins
  - id: test_upstream.py
    resource: tests/test_upstream.py
  - id: contributing.md
    resource: CONTRIBUTING.md
    title: Before opening a pull request
generated:
  by: process:ktl-librarian
  at: "2026-11-05T02:56:32Z"
status: draft
---

# Move to another edition

1. Read the watch's report and what NIST changed. A person decides whether the schema moves.[^watch]
2. Replace the file in `upstream/`, and move its pin in `scripts/check_upstream_release.py`.[^watch]
3. Move `version`, `source` and the annotations in the schema headers. `tests/test_upstream.py` holds them to the pins.[^test_upstream.py]
4. Run `just build-catalogue` and `just test`.[^contributing.md]

[^watch]: scripts/check_upstream_release.py, the pins
[^test_upstream.py]: tests/test_upstream.py
[^contributing.md]: CONTRIBUTING.md, Before opening a pull request
