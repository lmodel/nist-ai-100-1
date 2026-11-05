# nist-ai-100-1

This project is a LinkML model of the Artificial Intelligence Risk Management Framework (AI RMF 1.0), which the National Institute of Standards and Technology (NIST) publishes as NIST AI 100-1. It holds the Core's functions, categories and subcategories, the Playbook's material for each subcategory, and what Part 1 and the appendices list. `src/nist_ai_100_1/data/ai-rmf-1.0.yaml` holds all of it as records.

- [Schema documentation](elements/index.md), generated from the schema
- [About](about.md): how the classes fit together, where each part comes from and what the model leaves out
- [`nist_ai_100_1.yaml`](schema/nist_ai_100_1.yaml): the schema, with its modules merged

## Validating a framework document

```bash
uv run linkml-validate -s src/nist_ai_100_1/schema/nist_ai_100_1.yaml -C AiRmfFramework src/nist_ai_100_1/data/ai-rmf-1.0.yaml
```

`project/jsonschema/nist_ai_100_1.schema.json` is the same schema for anyone without LinkML.

## What the catalogue holds

| Part | Records |
| --- | --- |
| Functions, categories and subcategories of section 5 | 4, 19 and 72 |
| Suggested actions, as NIST's catalog gives them | 575 |
| Documentation prompts | 292 |
| Trustworthiness characteristics of section 3 | 7 |
| Key dimensions of Figure 2 and lifecycle stages of Figure 3 | 5 and 7 |
| AI actor tasks and additional AI actors of Appendix A | 10 and 5 |
| Challenges of section 1.2, and of measuring risk in section 1.2.1 | 4 and 7 |
| AI-specific risks of Appendix B | 14 |
| Human-AI interaction issues of Appendix C | 4 |
| Attributes of the AI RMF in Appendix D | 10 |

`tests/test_catalogue.py` holds these counts, validates the whole file with `linkml-validate` and the committed JSON Schema, and loads it into the generated dataclasses and Pydantic models.

## What the validator does not check

JSON Schema looks at one value at a time. It does not check that a subcategory sits under the category its identifier names, or that an enum and the list it names hold the same values. `tests/test_catalogue.py` checks both. The generated Pydantic models check no pattern a type carries, and neither generated model checks the rules on `AiRmfHarm`.
