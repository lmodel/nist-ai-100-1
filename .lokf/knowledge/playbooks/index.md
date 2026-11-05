# Playbooks

* [Release](release.md) - How a release happens: `semantic-release.yml` reads Conventional Commits on `main`, promotes the `## [Unreleased]` section, tags and publishes. The first release needs the `v0.0.0` baseline tag on `main`, and PyPI publishing stays off.
* [Regenerate and test](regenerate-and-test.md) - How to change the schema: edit `src/nist_ai_100_1/schema/`, run `just lint`, `just gen-project`, `just gen-doc`, `just lokf-adapt` and `just test`, and commit what they write. Generated files are never edited by hand.
* [Rebuild the catalogue](rebuild-the-catalogue.md) - How to refresh the Core of `src/nist_ai_100_1/data/ai-rmf-1.0.yaml`: run `just build-catalogue` after a change in `upstream/`, read the diff, and run `just test`. `just check-catalogue` compares without writing.
* [Move to another edition](update-upstream-pins.md) - How to move the schema when the watch reports a change: read what changed, then move `upstream/`, the pins in `scripts/check_upstream_release.py` and the schema headers together, and rebuild the catalogue.
* [Knowledge sources map](knowledge-sources.md) - The librarian's scrape map: every repository location and external source this bundle derives concepts from, how to re-check each, and the tracked paths left out with their reasons.
