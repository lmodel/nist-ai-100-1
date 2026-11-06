# Changelog

All notable changes to this project are documented here. The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

The `v0.0.0` tag is a baseline, not a release: it marks where versioning starts so the first real release is `0.1.0` rather than `1.0.0`. The schema stays below 1.0.0 until its shape settles, so a breaking change is a minor release.

## [Unreleased]

### Changed

- **The bundle's schema files sit in `.lokf/schema/`**: `lokf.yaml` and the `lokf adapt` copy `nist-ai-100-1.yaml`, as KTL v0.62.0 lays them out.

## [0.1.0] - 2026-11-05

### Added

- **The whole framework as records** in `src/nist_ai_100_1/data/ai-rmf-1.0.yaml`: the 4 functions, 19 categories and 72 subcategories with their Playbook material, and what Part 1 and the appendices list. `scripts/build_catalogue.py` writes the Core from `upstream/`.
- **`upstream/`**, holding the publication, NIST's OSCAL catalog at oscal-content v1.6.0 and the Playbook's file, with a weekly watch that reports a change to any of them. The watch reads only https addresses on NIST's hosts, at the start and after a redirect.
- **Slots for what the Core asks an adopter to document**: a system's intended purposes, deployment settings and AI actors (MAP 1.1 and 1.6), and a risk's priority and the tolerance it is judged against (MANAGE 1.2, GOVERN 1.3 and MAP 1.5).
- **Parts of the publication the schema lacked**:
  - the seventh lifecycle stage of Figure 3;
  - the examples of harm to an organization and to an ecosystem in Figure 1;
  - the affected parties of section 1.1 and the four challenges of section 1.2;
  - the additional-actor mark of Appendix A, and the representative actors of Figure 3 and Appendix A.
- **Tests** that validate the whole catalogue, hold it to the publication's counts and lists, and list each place NIST's catalog departs from the publication or the Playbook. An example per class and a counter-example per constraint, each naming where it fails.
- **`.lokf/nist-ai-100-1.yaml`, the schema's `lokf adapt` copy.** The knowledge release attaches it as `schema-<tag>-nist-ai-100-1.yaml`.
- **The repository's Knowledge Trust Ladder (KTL) knowledge bundle and its sidecar automation**, from the KTL v0.61.0 templates with the lokf floor at 0.9.0, and a knowledge website that replaces the mkdocs site.
- **The governance files**: SECURITY.md, AI_COVENANT.md, NOTICE and the CONTRIBUTING checklist.

### Changed

- **The schema splits into modules**: `nist_ai_100_1_base`, `nist_ai_100_1_foundations`, `nist_ai_100_1_rmf_core`, `nist_ai_100_1_profiles` and the umbrella. Classes and enums take the `AiRmf` prefix, slots the `ai_rmf_` prefix and values snake_case.
- **Likelihood becomes text.** The publication sets no scale, and the Playbook allows qualitative ones, so a 0-to-1 number overstated it.
- **A residual risk is the class `AiRmfResidualRisk`**, without an `is_residual` flag beside it. A harm's direction must be negative, and its example must sit under its category.
- **Each identifier is the form NIST writes**, and a category's number must be one its function has.
- **A profile's kinds are a list**, since section 6 does not make them exclusive.
- **Mappings name classes the released neighbours hold**, and tests check each.
- **The template settings** turn PyPI publishing and the docs preview off, linkml and linkml-runtime are locked at 1.12.1, and the Python project is named `nist-ai-100-1-linkml`.

### Removed

- **`nist_ai_rmf_common`**, whose place `nist_ai_100_1_base` takes. lmodel/nist-ai-600-1 and lmodel/nist-ai-rmf import the old module by address, so they must move before this merges or at the same time.
- **The `NamedThing` base, the `kind` slots beside each class and the subsets.**
- **The two SSSOM sets and their verifier**, whose rows came from a matching tool and no source confirmed. The umbrella set stays in lmodel/nist-ai-rmf.
- **`PlaybookEntry`, `PlaybookCollection` and `AiRmfDocument`.** A subcategory holds the Playbook's material, and `upstream/playbook.json` keeps NIST's file as it is.
- **The mkdocs site**, with redirects from its addresses to the new site.
