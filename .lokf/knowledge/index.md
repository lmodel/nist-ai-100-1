---
lokf_version: "0.2"
okf_version: "0.2"
base_iri: https://w3id.org/lmodel/nist-ai-100-1/knowledge/
context: https://w3id.org/lokf/context.jsonld
title: nist-ai-100-1 Knowledge Bundle
description: NIST AI 100-1 AI Risk Management Framework (AI RMF) 1.0 (LinkML)
license: https://creativecommons.org/licenses/by/4.0/
publisher:
  type: Person
  id: https://w3id.org/lmodel/nist-ai-100-1/knowledge/person/noel-mcloughlin
  name: Noel McLoughlin
---

# nist-ai-100-1 Knowledge Bundle

A [LOKF](https://lokf.nolan-nichols.com) knowledge base for nist-ai-100-1. Every Markdown file under `knowledge/` is one concept; together they form a queryable knowledge graph, derived from this repository's code and docs.

# Services

* [Documentation site](services/documentation-site.md) - The knowledge website in `website/`, an Astro Starlight site that the Knowledge website workflow publishes to GitHub Pages at `https://lmodel.github.io/nist-ai-100-1`, built from the README, `docs/`, the schema's pages and the bundle. It replaces the mkdocs site.

# Workflows

* [Knowledge librarian (knowledge-librarian.yaml)](workflows/knowledge-librarian.md) - The sidecar's scheduled agent run that keeps the bundle in step with the repository and opens a pull request for a person to review. It is inert until `KNOWLEDGE_LIBRARIAN_ENABLED` is `true`.
* [Knowledge registrar (knowledge-registrar.yaml)](workflows/knowledge-registrar.md) - The gate on the bundle: it validates the bundle on each pull request that touches it and weekly, and checks that each new `human:` event in a pull request is backed by an approval or a signature. It never judges whether content is true.
* [Knowledge release (knowledge-release.yaml)](workflows/knowledge-release.md) - The workflow that attaches the bundle, a Copilot skill and the schema's adapt copy to a GitHub release, each with a checksum. It starts by hand or, once `KNOWLEDGE_RELEASE_ENABLED` is `true`, on each published release.
* [Knowledge sync (knowledge-sync.yaml)](workflows/knowledge-sync.md) - The weekly workflow that keeps the sidecar's copies and the skills pin at the newest release of Knowledge Trust Ladder, by one pull request that a person merges.
* [Knowledge website (knowledge-website.yaml)](workflows/knowledge-website.md) - The workflow that builds `website/` on each pull request that touches its inputs, and deploys the default branch's build to GitHub Pages once `KNOWLEDGE_WEBSITE_ENABLED` is `true`.
* [Lint and docs (lint-and-docs.yaml)](workflows/lint-and-docs.md) - The static checks on pull requests, on `main` and every Monday: ShellCheck, actionlint, the word budgets of CONTRIBUTING.md and SECURITY.md, markdownlint, lychee and codespell.
* [Semantic release (semantic-release.yml)](workflows/semantic-release.md) - The workflow that computes the next version from Conventional Commits on `main`, promotes the changelog, tags and publishes a GitHub Release, and dispatches the knowledge release once `KNOWLEDGE_RELEASE_ENABLED` is `true`.
* [Build and test (main.yaml)](workflows/main.md) - The Build and test workflow: on every pull request and push to `main`, it runs `just test` on Python 3.10 to 3.14, and lints the schema and checks the adapt copy on 3.13.
* [Upstream watch (upstream-watch.yaml)](workflows/upstream-watch.md) - The weekly check that `scripts/check_upstream_release.py` runs: another edition, a changed catalog, a moved tag or changed bytes in the publication or the Playbook fails the run and opens or updates an issue.

# Playbooks

* [Release](playbooks/release.md) - How a release happens: `semantic-release.yml` reads Conventional Commits on `main`, promotes the `## [Unreleased]` section, tags and publishes. The first release needs the `v0.0.0` baseline tag on `main`, and PyPI publishing stays off.
* [Regenerate and test](playbooks/regenerate-and-test.md) - How to change the schema: edit `src/nist_ai_100_1/schema/`, run `just lint`, `just gen-project`, `just gen-doc`, `just lokf-adapt` and `just test`, and commit what they write. Generated files are never edited by hand.
* [Rebuild the catalogue](playbooks/rebuild-the-catalogue.md) - How to refresh the Core of `src/nist_ai_100_1/data/ai-rmf-1.0.yaml`: run `just build-catalogue` after a change in `upstream/`, read the diff, and run `just test`. `just check-catalogue` compares without writing.
* [Move to another edition](playbooks/update-upstream-pins.md) - How to move the schema when the watch reports a change: read what changed, then move `upstream/`, the pins in `scripts/check_upstream_release.py` and the schema headers together, and rebuild the catalogue.
* [Knowledge sources map](playbooks/knowledge-sources.md) - The librarian's scrape map: every repository location and external source this bundle derives concepts from, how to re-check each, and the tracked paths left out with their reasons.

# Glossary

* [Adapt copy](glossary/adapt-copy.md) - An adapt copy: the copy of a published LinkML schema that `lokf adapt` writes so that it can sit beside LOKF's `lokf.yaml` in a domain schema, with its chosen roots on `Concept`.
* [AI RMF](glossary/ai-rmf.md) - The AI Risk Management Framework: NIST's voluntary framework for managing the risks of AI systems, published as NIST AI 100-1. Its Core has four functions.
* [Function](glossary/function.md) - A function of the AI RMF Core: GOVERN, MAP, MEASURE or MANAGE, which organize AI risk management at the highest level. GOVERN cuts across the other three.
* [Subcategory](glossary/subcategory.md) - A specific outcome in the AI RMF Core, such as GOVERN 1.1, named by its category's identifier and a number. There are 72.
* [Trustworthiness characteristic](glossary/trustworthiness-characteristic.md) - One of seven characteristics of trustworthy AI systems in section 3, from valid and reliable to fair with harmful bias managed. Figure 4 makes valid and reliable the base.
* [AI actor](glossary/ai-actor.md) - An organization or individual with an active role in an AI system's lifecycle. Appendix A describes ten AI actor tasks and five additional AI actors.
* [Playbook](glossary/playbook.md) - The NIST AI RMF Playbook: an online companion that suggests actions and resources for each subcategory, voluntary and updated apart from the publication.
* [AI RMF profile](glossary/profile.md) - An implementation of the Core for a setting, application or technology, or a description of a current or target state, or a treatment of risks across sectors. Section 6 prescribes no template.
* [Residual risk](glossary/residual-risk.md) - The risk that remains after treatment, in section 1.2.3. MANAGE 1.4 calls negative residual risks the sum of all unmitigated risks, so the publication has two definitions.

# Policies

* [AI covenant](policies/ai-covenant.md) - The rules for AI-assisted work here: whoever submits owns the contribution, an element says what the publication says, a rule states only what the publication states, a mapping is read at its source, and no commit carries an AI co-authorship trailer.
* [Security policy](policies/security-policy.md) - How to report a vulnerability in this repository, by GitHub's private reporting, what executes here and what holds each surface. A problem in NIST's own text belongs with NIST.
* [Licence and attribution](policies/license-and-attribution.md) - Whose work each part is: the code and the schema under Apache-2.0, the bundle under CC BY 4.0, NIST's catalog under CC0 1.0, and the publication and the Playbook under NIST's statement, which allows reprints worldwide with its citation. No endorsement by NIST is implied.

# Datasets

* [Generated artefacts](datasets/generated-artefacts.md) - What `just gen-project` and `just gen-doc` generate from the schema: the projections in `project/`, the Python models in `src/nist_ai_100_1/datamodel/`, and the merged schema in `docs/schema/`. None is edited by hand.
* [Neighbours' adapt copies](datasets/neighbour-copies.md) - The adapt copies of 19 released lmodel repositories in `tests/neighbours/`, among them oscal, nist-csf-v2 and iso27001, each pinned by its SHA-256, against which `tests/test_schema_rules.py` holds this schema's copy apart and checks the mappings.
* [Example data](datasets/example-data.md) - The examples `tests/test_data.py` checks: a valid example of each class that is not abstract, and a counter-example for each constraint, whose first line names where it must fail.
* [nist-ai-100-1 LinkML schema](datasets/nist-ai-100-1-linkml-schema.md) - The LinkML model of NIST AI 100-1, `src/nist_ai_100_1/schema/nist_ai_100_1.yaml`: an umbrella over four modules that holds the tree root `AiRmfFramework`, with the `AiRmf` class prefix and the `ai_rmf_` slot prefix.
* [Base module](datasets/base-module.md) - `nist_ai_100_1_base.yaml`, the slice a profile can import alone: the identifier forms, the enums of trustworthiness characteristics and AI actor tasks, the `title` and `description` slots, and the abstract `AiRmfRecord`.
* [Foundations module](datasets/foundations-module.md) - `nist_ai_100_1_foundations.yaml`: classes and enums for Part 1 and Appendices A to D, such as lifecycle stages, measurement challenges and AI-specific risks, and the classes under `AiRmfRecord` for an adopter's systems, actors, risks, impacts, harms, tolerances and biases.
* [AI RMF Core module](datasets/rmf-core-module.md) - `nist_ai_100_1_rmf_core.yaml`: `AiRmfFunction`, `AiRmfCategory` and `AiRmfSubcategory`, with the Playbook material a subcategory holds, in `AiRmfSuggestedAction`, `AiRmfDocumentationItem` and `AiRmfResource`.
* [Profiles module](datasets/profiles-module.md) - `nist_ai_100_1_profiles.yaml`: `AiRmfProfile` and `AiRmfProfileKind`, for the use-case, current, target and cross-sectoral profiles of section 6. The publication prescribes no template, so only the kinds and the subcategories are structured.
* [The catalogue](datasets/catalogue.md) - `src/nist_ai_100_1/data/ai-rmf-1.0.yaml`, the whole framework as one `AiRmfFramework` record: 4 functions, 19 categories, 72 subcategories, 575 suggested actions and 292 documentation prompts, and the lists of Part 1 and the appendices.
* [Copy of the upstream](datasets/upstream-copy.md) - `upstream/`: the publication's PDF, NIST's OSCAL catalog with its licence, and the Playbook's file, unchanged. `scripts/check_upstream_release.py` pins each by hash, and `tests/test_upstream.py` compares them offline.
* [Where NIST's catalog departs from the publication](datasets/catalog-departures.md) - `tests/catalog_departures.yaml`: the 44 of 91 statements that NIST's OSCAL catalog words differently from Tables 1 to 4 of the publication, each with both wordings. `tests/test_catalogue.py` fails on a new difference.
* [The schema's adapt copy](datasets/adapt-copy.md) - `.lokf/nist-ai-100-1.yaml`, the copy `just lokf-adapt` writes from the schema so that it sits beside LOKF's `lokf.yaml`: 13 classes rooted on `Concept`, `ai_rmf_id` dropped for LOKF's `id`, and `title` and `description` folded into LOKF's.
* [GOVERN 1.1](datasets/example-subcategory.md) - Subcategory GOVERN 1.1 of the AI RMF, written as a concept of type `AiRmfSubcategory` in the adapt copy's keys. It shows that the domain schema admits a subcategory as a concept.

# References

* [NIST AI 100-1, the AI RMF 1.0](references/nist-ai-100-1.md) - The publication this schema renders: Artificial Intelligence Risk Management Framework (AI RMF 1.0), NIST AI 100-1, January 2023, with Part 1, the Core and profiles in Part 2, and Appendices A to D. `upstream/NIST.AI.100-1.pdf` holds it.
* [NIST's catalog of the AI RMF in OSCAL](references/oscal-catalog.md) - NIST's Open Security Controls Assessment Language (OSCAL) catalog of the AI RMF 1.0 in usnistgov/oscal-content at v1.6.0: the Core with each function's overview and the Playbook's material, restated from the publication with some differences.
* [The NIST AI RMF Playbook](references/ai-rmf-playbook.md) - The online companion to the AI RMF, with suggested actions and resources for each subcategory. `upstream/playbook.json` holds its file, which adds the AI actor and topic tags that NIST's catalog lacks. NIST updates it apart from the publication.

# Explanations

* [Where each part comes from](explanations/where-each-part-comes-from.md) - NIST publishes the Core in three places that differ: the publication's tables, its OSCAL catalog and the Playbook's file. The publication decides a statement, the catalog gives the Playbook's material, and the Playbook's file gives the tags.
* [Modelling choices](explanations/modelling-choices.md) - Why likelihood and magnitude are text, why one enum holds AI actor tasks and additional AI actors, why Figure 3 gives seven lifecycle stages, and why a profile's kinds are a list.
* [What the publication lists and what an adopter records](explanations/lists-and-records.md) - Two groups of classes in one schema: those that render what the publication lists, with one record per item in the catalogue, and those under `AiRmfRecord` for an adopter's own AI systems, risks and profiles, which the publication holds none of.
* [Scope](explanations/scope.md) - What the schema leaves out: the publication's running prose, definitions quoted from ISO or other third parties, NIST's crosswalks and the AI RMF Roadmap. The Generative AI Profile is lmodel/nist-ai-600-1.
* [Mappings](explanations/mappings.md) - What the schema crosses to: lmodel/oscal, lmodel/nist-csf-v2, lmodel/iso27001 and PROV, each read at its source. The two SSSOM sets are gone, because their rows came from a matching tool and no source confirmed them.
