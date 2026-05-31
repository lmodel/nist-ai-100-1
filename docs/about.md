# About nist-ai-100-1

LinkML schema for the **NIST Artificial Intelligence Risk Management Framework (AI RMF 1.0)**, published as [NIST AI 100-1](https://doi.org/10.6028/NIST.AI.100-1) (January 2023).

This module covers the AI RMF 1.0 core publication. The Generative AI Profile (NIST AI 600-1) lives in the sibling `nist-ai-600-1` repository, and the umbrella distribution that bundles both lives in `nist-ai-rmf`.

## Design

The schema is split into two import modules so the framework has one canonical base instead of colliding copies re-inlined per repo:

- **`nist_ai_rmf_common`** ([`schema/nist_ai_rmf_common.yaml`](https://github.com/lmodel/nist-ai-100-1/blob/main/src/nist_ai_100_1/schema/nist_ai_rmf_common.yaml)) — the shared base vocabulary: the abstract `NamedThing` root, the `id`/`name`/`title`/`description`/`see_also` slots, the `SubcategoryCode` type, and `TrustworthinessCharacteristicEnum`. Hosted here and imported by `nist-ai-600-1` and the `nist-ai-rmf` umbrella.
- **`nist_ai_100_1`** — the AI RMF 1.0 content, importing common. All concept classes derive from `NamedThing`.

## Status

| Aspect | State |
|---|---|
| Schema id | `https://w3id.org/lmodel/nist-ai-100-1` |
| Schema version | `1.0.0` |
| Tree root | `AiRmfFramework` |
| Source document | NIST AI 100-1 (January 2023), DOI [10.6028/NIST.AI.100-1](https://doi.org/10.6028/NIST.AI.100-1) |
| Coverage | Part 1 (Framing Risk, Audience, Trustworthiness), Part 2 (AI RMF Core, Profiles), Appendix A (Actor Tasks), Appendix B (AI vs traditional software risk), Appendix C (Human-AI interaction), Appendix D (Framework attributes), plus the AI RMF Playbook companion data shape |
| Size | 25 classes, 77 slots, 13 enums, 3 types, 10 subsets |
| Lint | Clean (`linkml-lint`) |
| Tests | 6 valid fixtures pass (`pytest` via `just test`); 4 counter-example fixtures fail as expected (`just test-data`); third-party NIST AI RMF Playbook (72 records) validated as `PlaybookCollection` in a separate pytest run (`just test-third-party`, also wired into `just test`) |
| Mappings | SSSOM TSV at `src/nist_ai_100_1/mappings/nist_ai_100_1.sssom.tsv`; `scripts/verify_mappings.py --strict` reports `missing=0 extra=0 unknown=0` against NIST CSF v2, NIST SP 800-53, OSCAL catalog/profile, ISO 27001, ISO 29100, GIST, schema.org, PROV, FOAF, DCTERMS |
| Last verified | 2026-05-28 |

## Subsets

The schema is partitioned into ten subsets so consumers can adopt only the parts they need:

- `base`, `framework_core` (Part 2 §5),
- `trustworthiness` (Part 1 §3),
- `lifecycle` (Part 1 §2, Figures 2-3, Appendix A),
- `risk_and_harm` (Part 1 §1),
- `profiles` (Part 2 §6),
- `attributes` (Appendix D),
- `ai_risk_distinctions` (Appendix B),
- `human_ai_interaction` (Appendix C),
- `playbook` (companion resource).

## References

- [NIST AI 100-1](https://nvlpubs.nist.gov/nistpubs/ai/nist.ai.100-1.pdf)
- [NIST AIRC Playbook](https://airc.nist.gov/airmf-resources/playbook/)
- [NIST AI RMF Website](https://www.nist.gov/itl/ai-risk-management-framework)
- Related schemas: [nist-ai-600-1](https://github.com/lmodel/nist-ai-600-1) (Generative AI Profile), [nist-ai-rmf](https://github.com/lmodel/nist-ai-rmf) (umbrella distribution)
