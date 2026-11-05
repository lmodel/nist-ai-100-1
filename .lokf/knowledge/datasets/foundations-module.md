---
type: Dataset
id: https://w3id.org/lmodel/nist-ai-100-1/knowledge/datasets/foundations-module
genre: reference
title: Foundations module
description: "`nist_ai_100_1_foundations.yaml`: classes and enums for Part 1 and Appendices A to D, such as lifecycle stages, measurement challenges and AI-specific risks, and the classes under `AiRmfRecord` for an adopter's systems, actors, risks, impacts, harms, tolerances and biases."
resource: src/nist_ai_100_1/schema/nist_ai_100_1_foundations.yaml
isPartOf:
  - https://w3id.org/lmodel/nist-ai-100-1/knowledge/datasets/nist-ai-100-1-linkml-schema
sources:
  - id: foundations
    resource: src/nist_ai_100_1/schema/nist_ai_100_1_foundations.yaml
generated:
  by: process:ktl-librarian
  at: "2026-11-05T02:56:32Z"
status: draft
---

# Foundations module

One group of classes renders what the publication lists: `AiRmfTrustworthinessCharacteristic`, `AiRmfDimension`, `AiRmfLifecycleStage`, `AiRmfActorTask`, `AiRmfManagementChallenge`, `AiRmfMeasurementChallenge`, `AiRmfSpecificRisk`, `AiRmfHumanAiIssue` and `AiRmfAttribute`.[^foundations]

The other group sits under `AiRmfRecord`: `AiRmfSystem`, `AiRmfActor`, `AiRmfRisk`, `AiRmfResidualRisk`, `AiRmfImpact`, `AiRmfHarm`, `AiRmfRiskTolerance` and `AiRmfBias`.[^foundations]

Rules on `AiRmfHarm` hold a harm's direction to negative and its example to its category.[^foundations]

[^foundations]: src/nist_ai_100_1/schema/nist_ai_100_1_foundations.yaml
