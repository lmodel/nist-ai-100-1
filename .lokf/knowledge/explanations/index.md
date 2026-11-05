# Explanations

* [Where each part comes from](where-each-part-comes-from.md) - NIST publishes the Core in three places that differ: the publication's tables, its OSCAL catalog and the Playbook's file. The publication decides a statement, the catalog gives the Playbook's material, and the Playbook's file gives the tags.
* [Modelling choices](modelling-choices.md) - Why likelihood and magnitude are text, why one enum holds AI actor tasks and additional AI actors, why Figure 3 gives seven lifecycle stages, and why a profile's kinds are a list.
* [What the publication lists and what an adopter records](lists-and-records.md) - Two groups of classes in one schema: those that render what the publication lists, with one record per item in the catalogue, and those under `AiRmfRecord` for an adopter's own AI systems, risks and profiles, which the publication holds none of.
* [Scope](scope.md) - What the schema leaves out: the publication's running prose, definitions quoted from ISO or other third parties, NIST's crosswalks and the AI RMF Roadmap. The Generative AI Profile is lmodel/nist-ai-600-1.
* [Mappings](mappings.md) - What the schema crosses to: lmodel/oscal, lmodel/nist-csf-v2, lmodel/iso27001 and PROV, each read at its source. The two SSSOM sets are gone, because their rows came from a matching tool and no source confirmed them.
