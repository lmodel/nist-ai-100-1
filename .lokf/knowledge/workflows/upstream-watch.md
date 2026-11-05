---
type: Service
id: https://w3id.org/lmodel/nist-ai-100-1/knowledge/workflows/upstream-watch
genre: reference
title: Upstream watch (upstream-watch.yaml)
description: "The weekly check that `scripts/check_upstream_release.py` runs: another edition, a changed catalog, a moved tag or changed bytes in the publication or the Playbook fails the run and opens or updates an issue."
resource: .github/workflows/upstream-watch.yaml
about:
  - https://w3id.org/lmodel/nist-ai-100-1/knowledge/references/nist-ai-100-1
  - https://w3id.org/lmodel/nist-ai-100-1/knowledge/references/oscal-catalog
  - https://w3id.org/lmodel/nist-ai-100-1/knowledge/references/ai-rmf-playbook
sources:
  - id: upstream-watch.yaml
    resource: .github/workflows/upstream-watch.yaml
  - id: watch
    resource: scripts/check_upstream_release.py
    title: the docstring
  - id: test_watch.py
    resource: tests/test_watch.py
    title: the docstring
  - resource: .github/scripts/report-issue.sh
    title: how the issue is opened
generated:
  by: process:ktl-librarian
  at: "2026-11-05T03:29:55Z"
status: draft
---

# Upstream watch (upstream-watch.yaml)

The workflow runs every Monday, and a failing check opens an issue or comments on the one already open.[^upstream-watch.yaml]

The script asks the GitHub API about usnistgov/oscal-content, sending its token there alone, and downloads the publication and the Playbook with no token, following a redirect only over https to those hosts and reading at most 20 MB.[^watch]

`tests/test_watch.py` runs it against stubbed answers.[^test_watch.py]

[^upstream-watch.yaml]: .github/workflows/upstream-watch.yaml
[^watch]: scripts/check_upstream_release.py, the docstring
[^test_watch.py]: tests/test_watch.py, the docstring
