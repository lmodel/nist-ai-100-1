<a href="https://github.com/linkml/linkml-project-copier"><img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-grayscale-inverted-border-teal.json" alt="Copier Badge" style="max-width:100%;"/></a>

# nist-ai-100-1

NIST AI 100-1 AI Risk Management Framework (AI RMF) 1.0 (LinkML)

> **Only want to ask?** Install `ktl-docent` into any agent you use, by a route from [the install page](https://w3id.org/ktl/docs/install/), and ask it about this project. It answers from the bundle and says how far each answer has been checked.
>
> **Agents:** if `.lokf/knowledge/index.md` exists, read it first. `llms.txt` says how to weigh it.

## Documentation Website

[https://lmodel.github.io/nist-ai-100-1](https://lmodel.github.io/nist-ai-100-1)

## What it models

The schema renders [NIST AI 100-1](https://doi.org/10.6028/NIST.AI.100-1), the AI RMF 1.0 of January 2023: the Core, the Playbook's material for each subcategory, and the framing, lifecycle, trustworthiness and appendix lists of the publication. Classes under `AiRmfRecord` let an adopter record its own AI systems, risks and profiles in the same terms.

`src/nist_ai_100_1/data/` holds the whole framework as records, and `upstream/` holds NIST's three sources, pinned by hash. Tests hold the records to those sources, and a weekly workflow opens an issue when one changes. NIST's sources disagree in places, so [docs/about.md](docs/about.md) says which one decides.

## Mappings

* **[lmodel/oscal](https://github.com/lmodel/oscal)**: `broad_mappings` from the framework, a function, a category, a subcategory, a Playbook item and a resource, and `related_mappings` from a profile. `tests/test_schema_rules.py` checks each against the released copy.
* **[lmodel/nist-csf-v2](https://github.com/lmodel/nist-csf-v2)**: `related_mappings` from a function, a category and a subcategory, since Appendix B says the two share that structure. `tests/test_schema_rules.py` checks each.
* **[lmodel/iso27001](https://github.com/lmodel/iso27001)**: `related_mappings` from a risk to `IsmsRisk`. `tests/test_schema_rules.py` checks it.
* **[PROV](https://www.w3.org/TR/prov-o/)**: `broad_mappings` from an AI actor to `prov:Agent`.

The schema is the one home for mappings. The hand-kept SSSOM sets are gone, since no source confirmed their rows.

## Repository Structure

* [docs/](docs/): the website's own pages
* [project/](project/): generated project files (do not edit them)
* [scripts/](scripts/): the catalogue's builder and the upstream watch
* [src/nist_ai_100_1/schema/](src/nist_ai_100_1/schema): the LinkML schema, the umbrella and four modules (edit these)
* [src/nist_ai_100_1/data/](src/nist_ai_100_1/data): the whole framework as records
* [src/nist_ai_100_1/datamodel/](src/nist_ai_100_1/datamodel): the generated Python datamodel
* [tests/](tests/): Python tests, with example data in [data/](tests/data) and the neighbours' adapt copies in [neighbours/](tests/neighbours)
* [upstream/](upstream/): the publication, NIST's catalog and the Playbook's file, unchanged
* [website/](website/): the Astro Starlight site built from the README, `docs/`, the schema's pages and the knowledge bundle

## Developer Tools

Run `just` to list the project's [just](https://github.com/casey/just/) recipes.

## Knowledge Trust Ladder (KTL)

`.lokf/` holds this project's [KTL](https://w3id.org/ktl/) knowledge bundle. Its domain schema, `.lokf/schema/nist-ai-100-1.yaml`, is the copy `just lokf-adapt` writes from `src/nist_ai_100_1/schema/nist_ai_100_1.yaml`, and `just lokf-adapt-check` says when it is stale. Edit the source, never the copy. A release carries the copy as `schema-<tag>-nist-ai-100-1.yaml`, on the terms [CONTRIBUTING.md](CONTRIBUTING.md#releasing-maintainers) gives.

The copy roots what the publication lists and `AiRmfRecord` on `Concept`. In Obsidian, add these to the *Known LOKF types* setting of the KTL Registrar and KTL Curator plugins:

```text
AiRmfFunction, AiRmfCategory, AiRmfSubcategory, AiRmfTrustworthinessCharacteristic, AiRmfDimension, AiRmfLifecycleStage, AiRmfActorTask, AiRmfManagementChallenge, AiRmfMeasurementChallenge, AiRmfSpecificRisk, AiRmfHumanAiIssue, AiRmfAttribute, AiRmfSystem, AiRmfActor, AiRmfRisk, AiRmfResidualRisk, AiRmfImpact, AiRmfHarm, AiRmfRiskTolerance, AiRmfBias, AiRmfProfile
```

The copy drops `ai_rmf_id` for LOKF's `id`, and folds `title` and `description` into LOKF's. Every other key starts with `ai_rmf_`, so no key is LOKF's or another released copy's. `tests/test_schema_rules.py` holds all this.

## License

The schema and the code are under the Apache License 2.0 ([LICENSE](LICENSE)), and the knowledge bundle in [.lokf/knowledge/](.lokf/knowledge) is under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

NIST's works are free to reprint under its statement, and its catalog is under CC0 1.0: see [NOTICE](NOTICE), which gives the citation. This is not a NIST project, and its use implies no endorsement by NIST.

## Contributing and security

[CONTRIBUTING.md](CONTRIBUTING.md) is the checklist for pull requests and
releases, [AI_COVENANT.md](AI_COVENANT.md) sets the rules for AI-assisted work,
[SECURITY.md](SECURITY.md) says how to report a vulnerability, and
[CHANGELOG.md](CHANGELOG.md) records the changes.

## Credits

Built from the [linkml-project-copier](https://github.com/linkml/linkml-project-copier) template ([doi:10.5281/zenodo.15163584](https://doi.org/10.5281/zenodo.15163584)).
