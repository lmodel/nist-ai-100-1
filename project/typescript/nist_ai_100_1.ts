export type NamedThingRMFId = string;
export type AiSystemId = string;
export type AiSystemDimensionId = string;
export type AiLifecycleStageId = string;
export type AiActorId = string;
export type AiActorTaskId = string;
export type RiskId = string;
export type ImpactId = string;
export type HarmId = string;
export type ResidualRiskId = string;
export type RiskToleranceId = string;
export type RiskMeasurementChallengeId = string;
export type TrustworthinessCharacteristicId = string;
export type BiasId = string;
export type FunctionId = string;
export type CategoryId = string;
export type SubcategoryId = string;
export type AiRmfProfileId = string;
export type RmfAttributeId = string;
export type AiSpecificRiskId = string;
export type HumanAiInteractionIssueId = string;
export type AiRmfDocumentId = string;
export type AiRmfFrameworkId = string;
/**
* The four high-level AI RMF Core functions. GOVERN is a
cross-cutting function applied throughout; MAP, MEASURE, and MANAGE
operate on specific AI systems and lifecycle stages.
*/
export enum FunctionEnum {
    
    /** Cultivates and implements a culture of risk management; outlines
processes, documents, and organizational schemes that anticipate,
identify, and manage AI risks. */
    GOVERN = "GOVERN",
    /** Establishes the context to frame risks related to an AI system;
identifies risks based on intended purposes, capabilities, and
contextual factors. */
    MAP = "MAP",
    /** Employs quantitative, qualitative, or mixed-method tools to
analyze, assess, benchmark, and monitor AI risk and related impacts. */
    MEASURE = "MEASURE",
    /** Allocates risk resources to mapped and measured risks on a
regular basis and as defined by the GOVERN function; risk
treatment includes plans to respond to, recover from, and
communicate about incidents or events. */
    MANAGE = "MANAGE",
};
/**
* AI lifecycle stages as defined in Figure 2 (modified from
OECD 2022). Each stage corresponds to one of the AI system
dimensions (see AiSystemDimensionEnum).
*/
export enum AiLifecycleStageEnum {
    
    /** Articulate and document the system's concept and objectives,
underlying assumptions, context, and requirements (Application
Context dimension). */
    PLAN_AND_DESIGN = "PLAN_AND_DESIGN",
    /** Gather, validate, and clean data and document the metadata and
characteristics of the dataset (Data and Input dimension). */
    COLLECT_AND_PROCESS_DATA = "COLLECT_AND_PROCESS_DATA",
    /** Create or select algorithms; train models (AI Model dimension). */
    BUILD_AND_USE_MODEL = "BUILD_AND_USE_MODEL",
    /** Verify, validate, calibrate, and interpret model output
(AI Model dimension). */
    VERIFY_AND_VALIDATE = "VERIFY_AND_VALIDATE",
    /** Pilot; check compatibility with legacy systems; verify regulatory
compliance; manage organizational change; and evaluate user
experience (Task and Output dimension). */
    DEPLOY_AND_USE = "DEPLOY_AND_USE",
    /** Operate the AI system and continuously assess its recommendations
and impacts (both intended and unintended) in light of objectives,
legal and regulatory requirements, and ethical considerations
(Application Context dimension). */
    OPERATE_AND_MONITOR = "OPERATE_AND_MONITOR",
};
/**
* Key socio-technical dimensions of an AI system (Figure 2).
People and Planet sits at the centre representing human and
societal well-being.
*/
export enum AiSystemDimensionEnum {
    
    /** The setting in which an AI system is deployed - includes legal,
regulatory, ethical, and societal considerations. */
    APPLICATION_CONTEXT = "APPLICATION_CONTEXT",
    /** The data and inputs an AI system uses, including training,
validation, test data, and operational inputs. */
    DATA_AND_INPUT = "DATA_AND_INPUT",
    /** The model(s) and algorithms at the heart of an AI system. */
    AI_MODEL = "AI_MODEL",
    /** The task the AI system is designed to perform and the outputs
it produces (predictions, recommendations, decisions). */
    TASK_AND_OUTPUT = "TASK_AND_OUTPUT",
    /** Human rights and the broader well-being of society and the
planet - centred in Figure 2. */
    PEOPLE_AND_PLANET = "PEOPLE_AND_PLANET",
};
/**
* Categories of AI actor tasks as described in Appendix A and
illustrated in Figure 3.
*/
export enum AiActorTaskEnum {
    
    /** Performed during the Application Context and Data and Input
phases; create the concept and objectives of AI systems and are
responsible for planning, design, and data collection. */
    AI_DESIGN = "AI_DESIGN",
    /** Performed during the AI Model phase; provide the initial
infrastructure of AI systems (model building, selection,
calibration, training, testing). */
    AI_DEVELOPMENT = "AI_DEVELOPMENT",
    /** Performed during the Task and Output phase; responsible for
contextual decisions on how the AI system is used and for
assuring deployment into production. */
    AI_DEPLOYMENT = "AI_DEPLOYMENT",
    /** Performed in the Application Context / Operate and Monitor
phase; operating the AI system and regularly assessing system
output and impacts. */
    OPERATION_AND_MONITORING = "OPERATION_AND_MONITORING",
    /** Test, Evaluation, Verification, and Validation tasks performed
throughout the AI lifecycle; examine the AI system or its
components, and detect and remediate problems. */
    TEVV = "TEVV",
    /** Human-centered design practices and methodologies; promoting
active involvement of end users and other interested parties;
incorporating context-specific norms and values. */
    HUMAN_FACTORS = "HUMAN_FACTORS",
    /** Input from multidisciplinary practitioners or scholars who
provide knowledge or expertise in - and about - an industry
sector, context, or application area. */
    DOMAIN_EXPERT = "DOMAIN_EXPERT",
    /** Assess and evaluate requirements for AI system accountability,
combat harmful bias, examine impacts, product safety, liability,
and security. */
    AI_IMPACT_ASSESSMENT = "AI_IMPACT_ASSESSMENT",
    /** Conducted by AI actors with financial, legal, or policy
management authority for acquisition of AI models, products, or
services from a third party. */
    PROCUREMENT = "PROCUREMENT",
    /** Assumed by AI actors with management, fiduciary, and legal
authority for the organization, including senior leadership and
the Board of Directors. */
    GOVERNANCE_AND_OVERSIGHT = "GOVERNANCE_AND_OVERSIGHT",
    /** Providers, developers, vendors, and evaluators of data,
algorithms, models, and/or systems and related services external
to the deploying organization. */
    THIRD_PARTY_ENTITIES = "THIRD_PARTY_ENTITIES",
    /** Individuals or groups that use the AI system for specific
purposes; range in competency from AI experts to first-time
users. */
    END_USERS = "END_USERS",
    /** All individuals, groups, communities, or organizations directly
or indirectly affected by AI systems or decisions based on the
output of AI systems. */
    AFFECTED_INDIVIDUALS_OR_COMMUNITIES = "AFFECTED_INDIVIDUALS_OR_COMMUNITIES",
    /** Provide formal or quasi-formal norms or guidance - includes
trade associations, standards developing organizations, advocacy
groups, researchers, environmental groups, and civil society
organizations. */
    OTHER_AI_ACTORS = "OTHER_AI_ACTORS",
    /** Most likely to directly experience positive and negative impacts
of AI technologies; provides motivation for actions taken by
other AI actors. */
    GENERAL_PUBLIC = "GENERAL_PUBLIC",
};
/**
* The seven characteristics of trustworthy AI systems described in
Figure 4 and Part 1 §3.
*/
export enum TrustworthinessCharacteristicEnum {
    
    /** Confirmation that requirements for a specific intended use have
been fulfilled (validation) and that the system performs as
required without failure (reliability). A necessary condition of
trustworthiness and the base for other characteristics. */
    VALID_AND_RELIABLE = "VALID_AND_RELIABLE",
    /** The system does not, under defined conditions, lead to a state
in which human life, health, property, or the environment is
endangered. */
    SAFE = "SAFE",
    /** The system can withstand unexpected adverse events or changes
(resilient) and maintain confidentiality, integrity, and
availability through protection mechanisms (secure). */
    SECURE_AND_RESILIENT = "SECURE_AND_RESILIENT",
    /** Trustworthy AI depends on accountability, which presupposes
transparency - the extent to which information about an AI
system and its outputs is available to those interacting with
it. */
    ACCOUNTABLE_AND_TRANSPARENT = "ACCOUNTABLE_AND_TRANSPARENT",
    /** Explainability concerns the mechanisms underlying an AI system's
operation; interpretability concerns the meaning of its output
in context. */
    EXPLAINABLE_AND_INTERPRETABLE = "EXPLAINABLE_AND_INTERPRETABLE",
    /** Norms and practices that help safeguard human autonomy,
identity, and dignity - including anonymity, confidentiality,
and control over personal information. */
    PRIVACY_ENHANCED = "PRIVACY_ENHANCED",
    /** Concerns for equality and equity by addressing issues such as
harmful bias and discrimination, and recognising that
perceptions of fairness differ across cultures and
applications. */
    FAIR_WITH_HARMFUL_BIAS_MANAGED = "FAIR_WITH_HARMFUL_BIAS_MANAGED",
};
/**
* High-level categories of harm related to AI systems (Figure 1).
*/
export enum HarmCategoryEnum {
    
    /** Harm to individuals, groups/communities, or society at large
(including civil liberties, rights, physical or psychological
safety, economic opportunity, democratic participation, and
educational access). */
    HARM_TO_PEOPLE = "HARM_TO_PEOPLE",
    /** Harm to an organization's business operations, security
breaches or monetary loss, or reputation. */
    HARM_TO_AN_ORGANIZATION = "HARM_TO_AN_ORGANIZATION",
    /** Harm to interconnected and interdependent elements and
resources, the global financial system, supply chain, natural
resources, the environment, and the planet. */
    HARM_TO_AN_ECOSYSTEM = "HARM_TO_AN_ECOSYSTEM",
};
/**
* Sub-categories of harm to people, per Figure 1.
*/
export enum HarmToPeopleSubcategoryEnum {
    
    /** Harm to a person's civil liberties, rights, physical or
psychological safety, or economic opportunity. */
    INDIVIDUAL = "INDIVIDUAL",
    /** Harm to a group such as discrimination against a population
sub-group. */
    GROUP_OR_COMMUNITY = "GROUP_OR_COMMUNITY",
    /** Harm to democratic participation or educational access. */
    SOCIETAL = "SOCIETAL",
};
/**
* The three major categories of AI bias identified by NIST
(Part 1 §3.7; see NIST SP 1270).
*/
export enum BiasCategoryEnum {
    
    /** Bias present in AI datasets, organizational norms, practices,
and processes across the AI lifecycle, and the broader society
that uses AI systems. */
    SYSTEMIC = "SYSTEMIC",
    /** Bias present in AI datasets and algorithmic processes; often
stems from systematic errors due to non-representative samples. */
    COMPUTATIONAL_AND_STATISTICAL = "COMPUTATIONAL_AND_STATISTICAL",
    /** Bias related to how an individual or group perceives AI system
information to make a decision or fill in missing information;
omnipresent in decision-making across the AI lifecycle. */
    HUMAN_COGNITIVE = "HUMAN_COGNITIVE",
};
/**
* Challenges that complicate AI risk measurement (Part 1 §1.2.1).
*/
export enum RiskMeasurementChallengeEnum {
    
    /** Risks related to third-party software, hardware, and data,
including misalignment of risk metrics or methodologies between
developers, deployers, and operators. */
    THIRD_PARTY_SOFTWARE_HARDWARE_AND_DATA = "THIRD_PARTY_SOFTWARE_HARDWARE_AND_DATA",
    /** Identifying and tracking emergent risks and considering
techniques for measuring them; impact assessment helps
understand context-specific harms. */
    TRACKING_EMERGENT_RISKS = "TRACKING_EMERGENT_RISKS",
    /** Lack of consensus on robust and verifiable measurement methods
for risk and trustworthiness, and their applicability to
different use cases. */
    AVAILABILITY_OF_RELIABLE_METRICS = "AVAILABILITY_OF_RELIABLE_METRICS",
    /** Measuring risk at different stages may yield different results;
some risks may be latent and increase as systems adapt and
evolve. */
    RISK_AT_DIFFERENT_LIFECYCLE_STAGES = "RISK_AT_DIFFERENT_LIFECYCLE_STAGES",
    /** Lab measurements may differ from risks that emerge in
operational, real-world settings. */
    RISK_IN_REAL_WORLD_SETTINGS = "RISK_IN_REAL_WORLD_SETTINGS",
    /** Opaque systems with limited explainability or interpretability,
poor documentation, or inherent uncertainty complicate risk
measurement. */
    INSCRUTABILITY = "INSCRUTABILITY",
    /** AI systems intended to augment or replace human activity
require a human baseline for comparison, which is difficult to
systematize. */
    HUMAN_BASELINE = "HUMAN_BASELINE",
};
/**
* Treatment options for AI risks (MANAGE 1.3).
*/
export enum RiskResponseEnum {
    
    /** Reducing the likelihood or magnitude of the risk. */
    MITIGATING = "MITIGATING",
    /** Shifting the risk to another party (e.g., via insurance or contract). */
    TRANSFERRING = "TRANSFERRING",
    /** Choosing not to engage in the activity that creates the risk. */
    AVOIDING = "AVOIDING",
    /** Acknowledging the risk and taking no further action. */
    ACCEPTING = "ACCEPTING",
};
/**
* Types of AI RMF Profile (§6).
*/
export enum ProfileTypeEnum {
    
    /** Implementation of the AI RMF Core for a specific setting or
application (e.g., a hiring profile, a fair housing profile). */
    USE_CASE = "USE_CASE",
    /** Description of the current state of AI risk management
activities within a sector, industry, organization, or
application context. */
    TEMPORAL_CURRENT = "TEMPORAL_CURRENT",
    /** Description of the desired or target state of AI risk
management activities. */
    TEMPORAL_TARGET = "TEMPORAL_TARGET",
    /** Risks of models or applications used across use cases or
sectors (e.g., large language models, cloud-based services,
acquisition). */
    CROSS_SECTORAL = "CROSS_SECTORAL",
};
/**
* Audience categorisation for the AI RMF (Part 1 §2).
*/
export enum AudienceEnum {
    
    /** AI actors who perform or manage the design, development,
deployment, evaluation, and use of AI systems and drive AI
risk management efforts. */
    PRIMARY = "PRIMARY",
    /** AI actors in the People and Planet dimension who *inform* the
primary audience - trade associations, standards developers,
researchers, advocacy groups, civil society organisations,
end users, and impacted individuals or communities. */
    INFORMING = "INFORMING",
};
/**
* Whether an impact of an AI system is positive, negative, or both
(Part 1 §1.1).
*/
export enum ImpactSignEnum {
    
    /** A beneficial impact or opportunity. */
    POSITIVE = "POSITIVE",
    /** A harmful impact or threat. */
    NEGATIVE = "NEGATIVE",
    /** An impact that is both positive and negative. */
    MIXED = "MIXED",
};


/**
 * A generic grouping for any identifiable AI RMF element.
 */
export interface NamedThingRMF {
    /** A unique identifier for an element. */
    id: string,
    /** A short human-readable name. */
    name?: string,
    /** A human-readable title. */
    title?: string,
    /** A human-readable description. */
    description?: string,
    /** Related references. */
    see_also?: string[],
}


/**
 * An engineered or machine-based system that can, for a given set
of objectives, generate outputs such as predictions,
recommendations, or decisions influencing real or virtual
environments. AI systems are designed to operate with varying
levels of autonomy (Adapted from OECD Recommendation on AI:2019;
ISO/IEC 22989:2022).
 */
export interface AiSystem extends NamedThingRMF {
    /** The AI lifecycle stage(s) the element applies to. */
    lifecycle_stage?: string,
    /** The AI system dimension the element applies to. */
    ai_dimension?: string,
}


/**
 * A socio-technical dimension of an AI system (Figure 2):
Application Context, Data and Input, AI Model, Task and Output,
or People and Planet.
 */
export interface AiSystemDimension extends NamedThingRMF {
    /** Which AI system dimension an `AiSystemDimension` instance represents. */
    dimension_kind: string,
}


/**
 * A stage of the AI lifecycle (Figure 2): Plan and Design,
Collect and Process Data, Build and Use Model, Verify and
Validate, Deploy and Use, or Operate and Monitor.
 */
export interface AiLifecycleStage extends NamedThingRMF {
    /** Which AI lifecycle stage an `AiLifecycleStage` instance represents. */
    stage_kind: string,
    /** Whether the lifecycle stage incorporates TEVV activities. */
    includes_tevv?: boolean,
}


/**
 * An organization or individual that plays an active role in the AI
system lifecycle. AI actors include those who deploy or operate
AI as well as those who inform via formal or quasi-formal norms
and guidance (OECD 2019).
 */
export interface AiActor extends NamedThingRMF {
    /** AI actor task category. */
    actor_task?: string,
    /** The AI lifecycle stage(s) the element applies to. */
    lifecycle_stage?: string,
    /** Whether the actor or task is a Test, Evaluation, Verification, and
Validation (TEVV) actor / task. */
    is_tevv?: boolean,
    /** Whether the actor is part of the *primary* AI RMF audience or the
*informing* People-and-Planet audience. */
    audience?: string,
}


/**
 * A category of task performed by AI actors (Appendix A). Each
task is associated with one or more lifecycle stages and a
typical set of actor roles.
 */
export interface AiActorTask extends NamedThingRMF {
    /** Which AI actor task category an `AiActorTask` instance represents. */
    task_kind: string,
    /** Representative actor roles that perform an AI actor task. */
    typical_actors?: string[],
    /** The AI lifecycle stage(s) the element applies to. */
    lifecycle_stage?: string,
    /** The AI system dimension the element applies to. */
    ai_dimension?: string,
}


/**
 * The composite measure of an event's probability of occurring and
the magnitude or degree of the consequences of that event. When
considering negative impact, risk is a function of (1) the
negative impact or magnitude of harm and (2) the likelihood of
occurrence (Adapted from ISO 31000:2018; OMB Circular A-130:2016).
 */
export interface Risk extends NamedThingRMF {
    /** Estimated probability of the event occurring (0.0 to 1.0). The
AI RMF leaves quantification approaches to the implementer. */
    likelihood?: number,
    /** Magnitude or degree of consequences if the event occurs (free
text or qualitative scale). */
    magnitude?: string,
    /** Whether the impact is positive, negative, or both. */
    impact_sign?: string,
    /** Whether this risk represents risk remaining after risk treatment
(residual risk per ISO Guide 73). */
    is_residual?: boolean,
    /** The chosen risk treatment option. */
    risk_response?: string,
    /** The AI lifecycle stage(s) the element applies to. */
    lifecycle_stage?: string,
    /** Trustworthiness characteristic(s) the element pertains to. */
    trustworthiness_characteristic?: string,
    /** The impacts that contribute to a risk. */
    related_impacts?: Impact[],
    /** The AI system a risk pertains to. */
    affects_system?: AiSystemId,
}


/**
 * A positive, negative, or both consequence of an AI system. Impacts
can manifest as opportunities (positive) or threats (negative).
 */
export interface Impact extends NamedThingRMF {
    /** Whether the impact is positive, negative, or both. */
    impact_sign?: string,
    /** Magnitude or degree of consequences if the event occurs (free
text or qualitative scale). */
    magnitude?: string,
    /** Estimated probability of the event occurring (0.0 to 1.0). The
AI RMF leaves quantification approaches to the implementer. */
    likelihood?: number,
    /** Entities (people, organizations, ecosystems) the risk or harm
may affect. */
    affects?: NamedThingRMFId[],
}


/**
 * A negative impact that may be experienced by individuals,
groups, communities, organizations, society, the environment, or
the planet (Figure 1).
 */
export interface Harm extends NamedThingRMF {
    /** The high-level harm category (people / organization / ecosystem). */
    harm_category?: string,
    /** The sub-category when harm is to people (individual / group / societal). */
    harm_to_people_subcategory?: string,
    /** Magnitude or degree of consequences if the event occurs (free
text or qualitative scale). */
    magnitude?: string,
    /** Entities (people, organizations, ecosystems) the risk or harm
may affect. */
    affects?: NamedThingRMFId[],
}


/**
 * Risk remaining after risk treatment (ISO Guide 73). Documenting
residual risks helps system providers consider risks of deploying
the AI product and informs end users about potential negative
impacts.
 */
export interface ResidualRisk extends Risk {
}


/**
 * The organization's or AI actor's readiness to bear risk in order
to achieve its objectives (Adapted from ISO Guide 73). Risk
tolerance is highly contextual and application- and use-case
specific.
 */
export interface RiskTolerance extends NamedThingRMF {
    /** Free-text statement of a risk tolerance level or threshold. */
    tolerance_statement?: string,
    /** Legal or regulatory requirements influencing a risk tolerance. */
    legal_basis?: string,
}


/**
 * A challenge that complicates measurement of AI risks
(Part 1 §1.2.1).
 */
export interface RiskMeasurementChallenge extends NamedThingRMF {
    /** Which risk-measurement challenge a `RiskMeasurementChallenge` represents. */
    challenge_kind: string,
}


/**
 * A characteristic of a trustworthy AI system (Figure 4 / Part 1
§3). The seven characteristics are inter-related; addressing them
individually does not guarantee trustworthiness, and tradeoffs
are usually involved.
 */
export interface TrustworthinessCharacteristic extends NamedThingRMF {
    /** Which trustworthiness characteristic a `TrustworthinessCharacteristic` represents. */
    characteristic_kind: string,
    /** True when this characteristic is a necessary condition for
trustworthiness (per Figure 4 - Valid and Reliable is the base
of all others). */
    is_base_condition?: boolean,
    /** True when this characteristic relates to all others
(Accountable and Transparent; shown vertically in Figure 4). */
    is_cross_cutting?: boolean,
}


/**
 * A form of AI bias - a deviation that may be perpetuated or
amplified by AI systems. NIST identifies three major categories:
systemic, computational/statistical, and human-cognitive
(Part 1 §3.7; NIST SP 1270).
 */
export interface Bias extends NamedThingRMF {
    /** Category or categories of bias addressed. */
    bias_category?: string,
}


/**
 * A top-level AI RMF Core function. Each function organizes AI risk
management activities at the highest level. GOVERN applies across
all stages; MAP, MEASURE, and MANAGE apply to AI-system-specific
contexts and lifecycle stages.
 */
export interface Function extends NamedThingRMF {
    /** The function code (GOVERN, MAP, MEASURE, or MANAGE). */
    function_code: string,
    /** Categories that belong to a Function. */
    categories?: Category[],
}


/**
 * A category within an AI RMF Core function (e.g., "GOVERN 1:
Policies, processes, procedures, and practices ... are in place,
transparent, and implemented effectively"). Categories group
related subcategories.
 */
export interface Category extends NamedThingRMF {
    /** Identifier of a Category (e.g., "GOVERN 1"). */
    category_id?: string,
    /** The outcome statement of a Category or Subcategory - the desired
result of carrying out its actions. */
    outcome?: string,
    /** Subcategories that belong to a Category. */
    subcategories?: Subcategory[],
}


/**
 * A subcategory within an AI RMF Core category (e.g., "GOVERN 1.1:
Legal and regulatory requirements involving AI are understood,
managed, and documented"). Subcategories express specific
outcomes.
 */
export interface Subcategory extends NamedThingRMF {
    /** Identifier of a Subcategory (e.g., "GOVERN 1.1"). */
    subcategory_id?: string,
    /** The outcome statement of a Category or Subcategory - the desired
result of carrying out its actions. */
    outcome?: string,
    /** Trustworthiness characteristic(s) the element pertains to. */
    trustworthiness_characteristic?: string,
    /** The AI lifecycle stage(s) the element applies to. */
    lifecycle_stage?: string,
    /** Free-text discussion of the subcategory or related concept.
Corresponds to the AI RMF Playbook "About" section. */
    about_text?: string,
    /** Free-text bulleted list of suggested actions an organization can
take. Corresponds to the AI RMF Playbook "Actions" section. */
    suggested_actions_text?: string,
    /** Free-text documentation questions and transparency resources.
Corresponds to the AI RMF Playbook "Documentation" section. */
    documentation_questions?: string,
    /** Free-text list of references, citations, and supporting
resources. Corresponds to the AI RMF Playbook "References"
section. */
    references_text?: string,
    /** Free-text topic tags applied to a playbook entry (e.g.,
"Governance", "Trustworthy Characteristics", "Validity and
Reliability"). */
    topics?: string[],
    /** Free-text list of AI Actor categories the entry applies to,
preserving the original case used in the AI RMF Playbook
(e.g., "Governance and Oversight", "TEVV"). For controlled
enum values see `actor_task` (range AiActorTaskEnum). */
    ai_actor_categories?: string[],
}


/**
 * An implementation of the AI RMF Functions, Categories, and
Subcategories for a specific setting or application based on the
requirements, risk tolerance, and resources of the user (§6).
Profiles may be use-case-specific, temporal (current or target),
or cross-sectoral.
 */
export interface AiRmfProfile extends NamedThingRMF {
    /** The kind of AI RMF Profile. */
    profile_type: string,
    /** For temporal current profiles - how AI is currently being managed
and related risks in terms of current outcomes. */
    current_state?: string,
    /** For temporal target profiles - the outcomes needed to achieve the
desired AI risk management goals. */
    target_state?: string,
    /** The sector, industry, technology, or end-use application a
profile addresses (e.g., "hiring", "fair housing"). */
    sector?: string,
    /** Subcategories that a profile implements or addresses. */
    addresses?: SubcategoryId[],
}


/**
 * A design attribute of the AI RMF (Appendix D) - one of the
qualities the Framework strives to embody (e.g., risk-based,
consensus-driven, plain language, common language, easily usable,
universally applicable, outcome-focused, leveraging existing
standards, law- and regulation-agnostic, living document).
 */
export interface RmfAttribute extends NamedThingRMF {
}


/**
 * A risk that is new or increased for AI-based technology compared
to traditional software (Appendix B) - e.g., data quality, model
drift, opacity, scale and complexity, pre-trained model
uncertainty, emergent properties, privacy aggregation, or
environmental cost.
 */
export interface AiSpecificRisk extends NamedThingRMF {
}


/**
 * An issue that merits further consideration in human-AI
interaction (Appendix C) - e.g., clear human roles and
responsibilities, systemic and human-cognitive biases in design,
variability of human-AI interaction outcomes, complexity of
presenting AI system information to humans.
 */
export interface HumanAiInteractionIssue extends NamedThingRMF {
}


/**
 * A single AI RMF Playbook entry - an enrichment of a Core
subcategory with prose discussion, suggested actions,
documentation questions, references, and topic tags.

Attribute names use the same identifiers found in the published
NIST AI RMF Playbook JSON (e.g., `section_about`,
`section_actions`) so that the data can be loaded directly.
 */
export interface PlaybookEntry {
    /** Function label as serialised in the published Playbook JSON
(Title case - "Govern", "Map", "Measure", "Manage"). For
the controlled enum see `function_kind`. */
    type?: string,
    /** Subcategory identifier (e.g., "GOVERN 1.1"). Mirrors the
AI RMF Subcategory `subcategory_id`. */
    title?: string,
    /** Category code in the form "FUNCTION-N" (e.g., "GOVERN-1")
as used in the Playbook. */
    category?: string,
    /** Outcome statement of the subcategory. */
    description?: string,
    /** Free-text discussion ("About" section). */
    section_about?: string,
    /** Bulleted suggested actions ("Actions" section). */
    section_actions?: string,
    /** Documentation questions and transparency resources
("Documentation" section). */
    section_doc?: string,
    /** References and citations ("References" section). */
    section_ref?: string,
    /** AI actor categories the entry applies to. Free-text to
preserve the casing of the source data (e.g., "Governance
and Oversight"). */
    ai_actors?: string[],
    /** Topic tags (e.g., "Legal and Regulatory", "Validity and
Reliability"). */
    topic?: string[],
}


/**
 * A container for a set of PlaybookEntry instances - the
serialisation root for an AI RMF Playbook companion document.
Validate with ``linkml-validate --target-class PlaybookCollection``;
the canonical tree-root for the schema is ``AiRmfFramework``.
 */
export interface PlaybookCollection {
    /** The Playbook entries in a `PlaybookCollection`. */
    entries?: PlaybookEntry[],
}


/**
 * Publication metadata for an instance of the AI RMF (e.g., NIST
AI 100-1, January 2023). The Framework is intended to be a
living document, employing a two-number versioning system (major.minor).
 */
export interface AiRmfDocument extends NamedThingRMF {
    /** Version identifier of the document. */
    version?: string,
    /** The publisher of the document (e.g., NIST). */
    publisher?: string,
    /** Digital Object Identifier for the document. */
    doi?: string,
    /** Date the document was published. */
    published_date?: date,
    /** Reference to the source of the element (typically the document
or section it originated from). */
    source?: string,
}


/**
 * Root container that bundles the AI RMF Core (Functions) with
foundational concepts (trustworthiness characteristics,
lifecycle, actors, risks, harms), profiles, and Framework
attributes. Designed for serialising the Framework or a tailored
instance of it as a single JSON / YAML document.
 */
export interface AiRmfFramework extends NamedThingRMF {
    /** Publication metadata of the framework instance. */
    document?: AiRmfDocument,
    /** The four AI RMF Core functions and their content. */
    functions?: Function[],
    /** The seven characteristics of trustworthy AI. */
    trustworthiness_characteristics?: TrustworthinessCharacteristic[],
    /** The AI lifecycle stages (Figure 2). */
    lifecycle_stages?: AiLifecycleStage[],
    /** The AI system dimensions (Figure 2). */
    dimensions?: AiSystemDimension[],
    /** AI actor task categories (Appendix A). */
    actor_tasks?: AiActorTask[],
    /** AI RMF profiles defined alongside this Framework instance. */
    profiles?: AiRmfProfile[],
    /** Design attributes of the AI RMF (Appendix D). */
    attributes_?: RmfAttribute[],
    /** Identified challenges in measuring AI risk. */
    risk_measurement_challenges?: RiskMeasurementChallenge[],
    /** AI-specific risks compared to traditional software (Appendix B). */
    ai_specific_risks?: AiSpecificRisk[],
    /** Human-AI interaction considerations (Appendix C). */
    human_ai_interaction_issues?: HumanAiInteractionIssue[],
}



