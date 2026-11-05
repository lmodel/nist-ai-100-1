# About nist-ai-100-1

This page is for anyone reading the [LinkML](https://linkml.io) schema's elements: it says how they fit together, where each part comes from and what the model leaves out.

## How the classes fit together

`AiRmfFramework` holds one edition of the framework. Under it, the Core runs from `AiRmfFunction` to `AiRmfCategory` to `AiRmfSubcategory`, and a subcategory holds its Playbook material. Beside the Core sit the lists of Part 1 and the appendices, such as `AiRmfTrustworthinessCharacteristic` and `AiRmfSpecificRisk`.

Classes under `AiRmfRecord` are for an adopter's own facts: `AiRmfSystem`, `AiRmfActor`, `AiRmfRisk`, `AiRmfResidualRisk`, `AiRmfImpact`, `AiRmfHarm`, `AiRmfRiskTolerance`, `AiRmfBias` and `AiRmfProfile`. Each carries an identifier of the adopter's choosing, so one can name another, as a risk names its system. The publication holds none of these records.

The modules follow that split. `nist_ai_100_1_base` holds the identifier forms, the names of the characteristics and of the AI actor tasks, and `AiRmfRecord`. `nist_ai_100_1_foundations` holds Part 1 and the appendices, `nist_ai_100_1_rmf_core` the Core and `nist_ai_100_1_profiles` the profile. A profile of the AI RMF, such as lmodel/nist-ai-600-1, imports the base and profiles modules alone.

## Where each part comes from

NIST publishes the Core in three places, and they differ. On this page, "the catalogue" is this project's file of records, and "NIST's catalog" is NIST's OSCAL file.

- **The publication's Tables 1 to 4** state each category and subcategory. The catalogue keeps these words, since the schema renders the publication.
- **NIST's catalog in the Open Security Controls Assessment Language (OSCAL)** restates them and departs from the Tables in 44 of the 91 statements. Many are small, but some change a word: MEASURE 2.6 says "implicate" where the publication says "reflect", and GOVERN 1.2 drops "and practices". `tests/catalog_departures.yaml` lists all 44. The catalog also gives each function's one-sentence overview and the Playbook's suggested actions, discussion, documentation prompts and resources, which the catalogue takes from it.
- **The Playbook's own file** adds the AI actor and topic tags, which the catalog lacks. For 16 subcategories its suggested actions differ from the catalog's. In MANAGE 4.2 the catalog files the actions under the discussion, and the catalogue keeps them where the catalog puts them. `upstream/` holds all three files unchanged.

`scripts/build_catalogue.py` writes the Core from those files. Everything else in the catalogue, Part 1 and the appendices, is written by hand, and tests hold it to the publication's lists. Appendix B's items carry names of this project's own, because the publication gives them none.

The schema's descriptions are this project's own words. The enums' titles and the catalogue's Core and Playbook text are NIST's. [NOTICE](https://github.com/lmodel/nist-ai-100-1/blob/main/NOTICE) says on what terms.

## Choices worth knowing

- **Likelihood and magnitude are text.** The publication sets no scale, and the Playbook allows qualitative ones, so neither is a number.
- **One enum holds AI actor tasks and additional AI actors.** Appendix A separates them, but the Playbook's AI Actors key and AI 600-1's AI Actor Tasks tag both kinds together. The record for each says which it is. The Playbook also files a topic, Fairness and Bias, under AI Actors for GOVERN 4.3, and the catalogue leaves that one tag out.
- **Figure 3 has seven lifecycle stages.** Figure 2 shows six, and Figure 3 adds Use or Impacted by, under People and Planet.
- **A profile's kinds are a list.** Section 6 describes use-case, temporal and cross-sectoral profiles without saying they exclude each other, and a current profile of one use case is both.

## What is left out

The schema holds none of the publication's running prose, such as the discussion of each trustworthiness characteristic or the benefits section 4 expects. It holds no definition quoted from ISO, the Organisation for Economic Co-operation and Development (OECD) or other third parties. The list of what existing frameworks cannot do, in Appendix B, is prose too. NIST's crosswalks to other frameworks and the AI RMF Roadmap are separate documents. The Generative AI Profile is lmodel/nist-ai-600-1.

## Reference

- [NIST AI 100-1](https://doi.org/10.6028/NIST.AI.100-1)
- [The AI RMF site](https://www.nist.gov/itl/ai-risk-management-framework)
- [The NIST AI RMF Playbook](https://airc.nist.gov/airmf-resources/playbook/)
- [NIST's catalog of the AI RMF in OSCAL](https://github.com/usnistgov/oscal-content/tree/v1.6.0/nist.gov/AI100-1/ver1)
