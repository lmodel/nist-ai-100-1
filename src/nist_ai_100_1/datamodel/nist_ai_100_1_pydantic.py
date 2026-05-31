from __future__ import annotations

import re
import sys
from datetime import (
    date,
    datetime,
    time
)
from decimal import Decimal
from enum import Enum
from typing import (
    Any,
    ClassVar,
    Literal,
    Optional,
    Union
)

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    RootModel,
    SerializationInfo,
    SerializerFunctionWrapHandler,
    field_validator,
    model_serializer
)


metamodel_version = "1.11.0"
version = "1.0.0"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        serialize_by_alias = True,
        validate_by_name = True,
        validate_assignment = True,
        validate_default = True,
        extra = "forbid",
        arbitrary_types_allowed = True,
        use_enum_values = True,
        strict = False,
    )





class LinkMLMeta(RootModel):
    root: dict[str, Any] = {}
    model_config = ConfigDict(frozen=True)

    def __getattr__(self, key:str):
        return getattr(self.root, key)

    def __getitem__(self, key:str):
        return self.root[key]

    def __setitem__(self, key:str, value):
        self.root[key] = value

    def __contains__(self, key:str) -> bool:
        return key in self.root


linkml_meta = LinkMLMeta({'default_prefix': 'nist_ai_100_1',
     'default_range': 'string',
     'description': 'LinkML schema for the NIST AI Risk Management Framework\n'
                    '(AI RMF 1.0), published as NIST AI 100-1 (January 2023).\n'
                    '\n'
                    'Provides the structured, machine-readable taxonomy of the\n'
                    "Framework's foundational concepts (risk, impact, harm, AI "
                    'system,\n'
                    'AI actor, lifecycle), the seven characteristics of '
                    'trustworthy AI,\n'
                    'and the four Core functions (GOVERN, MAP, MEASURE, MANAGE) '
                    'together\n'
                    'with their categories and subcategories. It also models AI '
                    'RMF\n'
                    'Profiles (use-case, temporal, cross-sectoral), the design\n'
                    'attributes of the Framework, and the AI RMF Playbook '
                    'companion\n'
                    'data shape.',
     'id': 'https://w3id.org/lmodel/nist-ai-100-1',
     'imports': ['linkml:types'],
     'license': 'Apache-2.0',
     'name': 'nist-ai-100-1',
     'prefixes': {'dcterms': {'prefix_prefix': 'dcterms',
                              'prefix_reference': 'http://purl.org/dc/terms/'},
                  'doi': {'prefix_prefix': 'doi',
                          'prefix_reference': 'https://doi.org/'},
                  'foaf': {'prefix_prefix': 'foaf',
                           'prefix_reference': 'http://xmlns.com/foaf/0.1/'},
                  'gist_linkml': {'prefix_prefix': 'gist_linkml',
                                  'prefix_reference': 'https://w3id.org/lmodel/gist/'},
                  'iso27001': {'prefix_prefix': 'iso27001',
                               'prefix_reference': 'https://w3id.org/lmodel/iso27001/'},
                  'iso29100': {'prefix_prefix': 'iso29100',
                               'prefix_reference': 'https://w3id.org/lmodel/iso29100/'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'nist_ai_100_1': {'prefix_prefix': 'nist_ai_100_1',
                                    'prefix_reference': 'https://w3id.org/lmodel/nist-ai-100-1/'},
                  'nist_csf': {'prefix_prefix': 'nist_csf',
                               'prefix_reference': 'https://w3id.org/lmodel/nist-csf-v2/'},
                  'nist_sp_800_218': {'prefix_prefix': 'nist_sp_800_218',
                                      'prefix_reference': 'https://w3id.org/lmodel/nist-sp-800-218/'},
                  'nist_sp_800_53': {'prefix_prefix': 'nist_sp_800_53',
                                     'prefix_reference': 'https://w3id.org/lmodel/nist-sp-800-53/'},
                  'oscal_catalog': {'prefix_prefix': 'oscal_catalog',
                                    'prefix_reference': 'https://w3id.org/lmodel/oscal_catalog/'},
                  'oscal_profile': {'prefix_prefix': 'oscal_profile',
                                    'prefix_reference': 'https://w3id.org/lmodel/oscal_profile/'},
                  'prov': {'prefix_prefix': 'prov',
                           'prefix_reference': 'http://www.w3.org/ns/prov#'},
                  'rdf': {'prefix_prefix': 'rdf',
                          'prefix_reference': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#'},
                  'rdfs': {'prefix_prefix': 'rdfs',
                           'prefix_reference': 'http://www.w3.org/2000/01/rdf-schema#'},
                  'schema': {'prefix_prefix': 'schema',
                             'prefix_reference': 'http://schema.org/'},
                  'skos': {'prefix_prefix': 'skos',
                           'prefix_reference': 'http://www.w3.org/2004/02/skos/core#'},
                  'stix': {'prefix_prefix': 'stix',
                           'prefix_reference': 'https://w3id.org/lmodel/stix/'},
                  'xsd': {'prefix_prefix': 'xsd',
                          'prefix_reference': 'http://www.w3.org/2001/XMLSchema#'}},
     'see_also': ['https://w3id.org/lmodel/nist-ai-100-1',
                  'https://doi.org/10.6028/NIST.AI.100-1',
                  'https://www.nist.gov/itl/ai-risk-management-framework'],
     'source': 'https://doi.org/10.6028/NIST.AI.100-1',
     'source_file': 'src/nist_ai_100_1/schema/nist_ai_100_1.yaml',
     'subsets': {'ai_risk_distinctions': {'description': 'Appendix B "How AI Risks '
                                                         'Differ from Traditional '
                                                         'Software Risks" -\n'
                                                         'risks that are new or '
                                                         'increased for AI-based '
                                                         'technology (e.g.,\n'
                                                         'data quality, model '
                                                         'drift, opacity, scale '
                                                         'and complexity,\n'
                                                         'pre-trained model '
                                                         'uncertainty, emergent '
                                                         'properties, privacy\n'
                                                         'aggregation, '
                                                         'environmental cost).',
                                          'from_schema': 'https://w3id.org/lmodel/nist-ai-100-1',
                                          'name': 'ai_risk_distinctions'},
                 'attributes': {'description': 'Design attributes of the AI RMF '
                                               '(Appendix D "Attributes of the\n'
                                               'AI RMF") - the qualities the '
                                               'Framework strives to embody.',
                                'from_schema': 'https://w3id.org/lmodel/nist-ai-100-1',
                                'name': 'attributes'},
                 'base': {'description': 'Schema-infrastructure elements shared '
                                         'across the framework:\n'
                                         'identifier slots, the abstract '
                                         '`NamedThingRMF` root, publication\n'
                                         'metadata, and the top-level '
                                         '`AiRmfFramework` container. Not a\n'
                                         'section of NIST AI 100-1 itself - '
                                         'distinct from `framework_core`\n'
                                         '(Part 2, §5 "AI RMF Core").',
                          'from_schema': 'https://w3id.org/lmodel/nist-ai-100-1',
                          'name': 'base'},
                 'framework_core': {'description': 'The AI RMF Core (Part 2, §5): '
                                                   'the four high-level Functions\n'
                                                   '(GOVERN, MAP, MEASURE, MANAGE) '
                                                   'and their Categories and\n'
                                                   'Subcategories - the catalog '
                                                   'backbone of the Framework.',
                                    'from_schema': 'https://w3id.org/lmodel/nist-ai-100-1',
                                    'name': 'framework_core'},
                 'human_ai_interaction': {'description': 'Appendix C "AI Risk '
                                                         'Management and Human-AI '
                                                         'Interaction" -\n'
                                                         'considerations for human '
                                                         'roles and '
                                                         'responsibilities, '
                                                         'cognitive\n'
                                                         'and systemic biases in '
                                                         'design, variability of '
                                                         'interaction\n'
                                                         'outcomes, and '
                                                         'presentation of AI '
                                                         'information to humans.',
                                          'from_schema': 'https://w3id.org/lmodel/nist-ai-100-1',
                                          'name': 'human_ai_interaction'},
                 'lifecycle': {'description': 'AI system lifecycle stages, key '
                                              'dimensions, AI actor categories,\n'
                                              'and AI actor tasks (Part 1, §2 '
                                              'Audience; Figures 2 and 3;\n'
                                              'Appendix A "Descriptions of AI '
                                              'Actor Tasks").',
                               'from_schema': 'https://w3id.org/lmodel/nist-ai-100-1',
                               'name': 'lifecycle'},
                 'playbook': {'description': 'Companion-resource enrichment of an '
                                             'AI RMF subcategory with\n'
                                             'free-text discussion ("about"), '
                                             'suggested actions, documentation\n'
                                             'questions, and references - modelled '
                                             'after the NIST AI RMF\n'
                                             'Playbook JSON shape. (Not part of '
                                             'NIST AI 100-1 itself; cross-\n'
                                             'referenced in Part 2, §5.)',
                              'from_schema': 'https://w3id.org/lmodel/nist-ai-100-1',
                              'name': 'playbook'},
                 'profiles': {'description': 'AI RMF profile constructs (Part 2, '
                                             '§6): use-case profiles,\n'
                                             'temporal (current / target) '
                                             'profiles, and cross-sectoral '
                                             'profiles.',
                              'from_schema': 'https://w3id.org/lmodel/nist-ai-100-1',
                              'name': 'profiles'},
                 'risk_and_harm': {'description': 'Risk, impact, harm, residual '
                                                  'risk, risk tolerance, risk\n'
                                                  'measurement challenges, and '
                                                  'risk response options (Part 1, '
                                                  '§1\n'
                                                  '"Framing Risk", incl. §1.2 '
                                                  'Challenges).',
                                   'from_schema': 'https://w3id.org/lmodel/nist-ai-100-1',
                                   'name': 'risk_and_harm'},
                 'trustworthiness': {'description': 'Characteristics of '
                                                    'trustworthy AI systems (Part '
                                                    '1, §3):\n'
                                                    'Valid and Reliable, Safe, '
                                                    'Secure and Resilient, '
                                                    'Accountable and\n'
                                                    'Transparent, Explainable and '
                                                    'Interpretable, '
                                                    'Privacy-Enhanced, and\n'
                                                    'Fair with Harmful Bias '
                                                    'Managed.',
                                     'from_schema': 'https://w3id.org/lmodel/nist-ai-100-1',
                                     'name': 'trustworthiness'}},
     'title': 'NIST AI Risk Management Framework (AI RMF 1.0)',
     'types': {'CategoryCode': {'base': 'str',
                                'description': 'Identifier for a Core category '
                                               '(e.g., "GOVERN 1", "MAP 3").',
                                'from_schema': 'https://w3id.org/lmodel/nist-ai-100-1',
                                'name': 'CategoryCode',
                                'pattern': '^(GOVERN|MAP|MEASURE|MANAGE) [0-9]+$',
                                'typeof': 'string',
                                'uri': 'xsd:string'},
               'FunctionCode': {'base': 'str',
                                'description': 'Identifier of one of the four AI '
                                               'RMF Core functions.',
                                'from_schema': 'https://w3id.org/lmodel/nist-ai-100-1',
                                'name': 'FunctionCode',
                                'pattern': '^(GOVERN|MAP|MEASURE|MANAGE)$',
                                'typeof': 'string',
                                'uri': 'xsd:string'},
               'SubcategoryCode': {'base': 'str',
                                   'description': 'Identifier for a Core '
                                                  'subcategory (e.g., "GOVERN '
                                                  '1.1").',
                                   'from_schema': 'https://w3id.org/lmodel/nist-ai-100-1',
                                   'name': 'SubcategoryCode',
                                   'pattern': '^(GOVERN|MAP|MEASURE|MANAGE) '
                                              '[0-9]+\\.[0-9]+$',
                                   'typeof': 'string',
                                   'uri': 'xsd:string'}}} )

class FunctionEnum(str, Enum):
    """
    The four high-level AI RMF Core functions. GOVERN is a
cross-cutting function applied throughout; MAP, MEASURE, and MANAGE
operate on specific AI systems and lifecycle stages.
    """
    GOVERN = "GOVERN"
    """
    Cultivates and implements a culture of risk management; outlines
    processes, documents, and organizational schemes that anticipate,
    identify, and manage AI risks.
    """
    MAP = "MAP"
    """
    Establishes the context to frame risks related to an AI system;
    identifies risks based on intended purposes, capabilities, and
    contextual factors.
    """
    MEASURE = "MEASURE"
    """
    Employs quantitative, qualitative, or mixed-method tools to
    analyze, assess, benchmark, and monitor AI risk and related impacts.
    """
    MANAGE = "MANAGE"
    """
    Allocates risk resources to mapped and measured risks on a
    regular basis and as defined by the GOVERN function; risk
    treatment includes plans to respond to, recover from, and
    communicate about incidents or events.
    """


class AiLifecycleStageEnum(str, Enum):
    """
    AI lifecycle stages as defined in Figure 2 (modified from
OECD 2022). Each stage corresponds to one of the AI system
dimensions (see AiSystemDimensionEnum).
    """
    PLAN_AND_DESIGN = "PLAN_AND_DESIGN"
    """
    Articulate and document the system's concept and objectives,
    underlying assumptions, context, and requirements (Application
    Context dimension).
    """
    COLLECT_AND_PROCESS_DATA = "COLLECT_AND_PROCESS_DATA"
    """
    Gather, validate, and clean data and document the metadata and
    characteristics of the dataset (Data and Input dimension).
    """
    BUILD_AND_USE_MODEL = "BUILD_AND_USE_MODEL"
    """
    Create or select algorithms; train models (AI Model dimension).
    """
    VERIFY_AND_VALIDATE = "VERIFY_AND_VALIDATE"
    """
    Verify, validate, calibrate, and interpret model output
    (AI Model dimension).
    """
    DEPLOY_AND_USE = "DEPLOY_AND_USE"
    """
    Pilot; check compatibility with legacy systems; verify regulatory
    compliance; manage organizational change; and evaluate user
    experience (Task and Output dimension).
    """
    OPERATE_AND_MONITOR = "OPERATE_AND_MONITOR"
    """
    Operate the AI system and continuously assess its recommendations
    and impacts (both intended and unintended) in light of objectives,
    legal and regulatory requirements, and ethical considerations
    (Application Context dimension).
    """


class AiSystemDimensionEnum(str, Enum):
    """
    Key socio-technical dimensions of an AI system (Figure 2).
People and Planet sits at the centre representing human and
societal well-being.
    """
    APPLICATION_CONTEXT = "APPLICATION_CONTEXT"
    """
    The setting in which an AI system is deployed - includes legal,
    regulatory, ethical, and societal considerations.
    """
    DATA_AND_INPUT = "DATA_AND_INPUT"
    """
    The data and inputs an AI system uses, including training,
    validation, test data, and operational inputs.
    """
    AI_MODEL = "AI_MODEL"
    """
    The model(s) and algorithms at the heart of an AI system.
    """
    TASK_AND_OUTPUT = "TASK_AND_OUTPUT"
    """
    The task the AI system is designed to perform and the outputs
    it produces (predictions, recommendations, decisions).
    """
    PEOPLE_AND_PLANET = "PEOPLE_AND_PLANET"
    """
    Human rights and the broader well-being of society and the
    planet - centred in Figure 2.
    """


class AiActorTaskEnum(str, Enum):
    """
    Categories of AI actor tasks as described in Appendix A and
illustrated in Figure 3.
    """
    AI_DESIGN = "AI_DESIGN"
    """
    Performed during the Application Context and Data and Input
    phases; create the concept and objectives of AI systems and are
    responsible for planning, design, and data collection.
    """
    AI_DEVELOPMENT = "AI_DEVELOPMENT"
    """
    Performed during the AI Model phase; provide the initial
    infrastructure of AI systems (model building, selection,
    calibration, training, testing).
    """
    AI_DEPLOYMENT = "AI_DEPLOYMENT"
    """
    Performed during the Task and Output phase; responsible for
    contextual decisions on how the AI system is used and for
    assuring deployment into production.
    """
    OPERATION_AND_MONITORING = "OPERATION_AND_MONITORING"
    """
    Performed in the Application Context / Operate and Monitor
    phase; operating the AI system and regularly assessing system
    output and impacts.
    """
    TEVV = "TEVV"
    """
    Test, Evaluation, Verification, and Validation tasks performed
    throughout the AI lifecycle; examine the AI system or its
    components, and detect and remediate problems.
    """
    HUMAN_FACTORS = "HUMAN_FACTORS"
    """
    Human-centered design practices and methodologies; promoting
    active involvement of end users and other interested parties;
    incorporating context-specific norms and values.
    """
    DOMAIN_EXPERT = "DOMAIN_EXPERT"
    """
    Input from multidisciplinary practitioners or scholars who
    provide knowledge or expertise in - and about - an industry
    sector, context, or application area.
    """
    AI_IMPACT_ASSESSMENT = "AI_IMPACT_ASSESSMENT"
    """
    Assess and evaluate requirements for AI system accountability,
    combat harmful bias, examine impacts, product safety, liability,
    and security.
    """
    PROCUREMENT = "PROCUREMENT"
    """
    Conducted by AI actors with financial, legal, or policy
    management authority for acquisition of AI models, products, or
    services from a third party.
    """
    GOVERNANCE_AND_OVERSIGHT = "GOVERNANCE_AND_OVERSIGHT"
    """
    Assumed by AI actors with management, fiduciary, and legal
    authority for the organization, including senior leadership and
    the Board of Directors.
    """
    THIRD_PARTY_ENTITIES = "THIRD_PARTY_ENTITIES"
    """
    Providers, developers, vendors, and evaluators of data,
    algorithms, models, and/or systems and related services external
    to the deploying organization.
    """
    END_USERS = "END_USERS"
    """
    Individuals or groups that use the AI system for specific
    purposes; range in competency from AI experts to first-time
    users.
    """
    AFFECTED_INDIVIDUALS_OR_COMMUNITIES = "AFFECTED_INDIVIDUALS_OR_COMMUNITIES"
    """
    All individuals, groups, communities, or organizations directly
    or indirectly affected by AI systems or decisions based on the
    output of AI systems.
    """
    OTHER_AI_ACTORS = "OTHER_AI_ACTORS"
    """
    Provide formal or quasi-formal norms or guidance - includes
    trade associations, standards developing organizations, advocacy
    groups, researchers, environmental groups, and civil society
    organizations.
    """
    GENERAL_PUBLIC = "GENERAL_PUBLIC"
    """
    Most likely to directly experience positive and negative impacts
    of AI technologies; provides motivation for actions taken by
    other AI actors.
    """


class TrustworthinessCharacteristicEnum(str, Enum):
    """
    The seven characteristics of trustworthy AI systems described in
Figure 4 and Part 1 §3.
    """
    VALID_AND_RELIABLE = "VALID_AND_RELIABLE"
    """
    Confirmation that requirements for a specific intended use have
    been fulfilled (validation) and that the system performs as
    required without failure (reliability). A necessary condition of
    trustworthiness and the base for other characteristics.
    """
    SAFE = "SAFE"
    """
    The system does not, under defined conditions, lead to a state
    in which human life, health, property, or the environment is
    endangered.
    """
    SECURE_AND_RESILIENT = "SECURE_AND_RESILIENT"
    """
    The system can withstand unexpected adverse events or changes
    (resilient) and maintain confidentiality, integrity, and
    availability through protection mechanisms (secure).
    """
    ACCOUNTABLE_AND_TRANSPARENT = "ACCOUNTABLE_AND_TRANSPARENT"
    """
    Trustworthy AI depends on accountability, which presupposes
    transparency - the extent to which information about an AI
    system and its outputs is available to those interacting with
    it.
    """
    EXPLAINABLE_AND_INTERPRETABLE = "EXPLAINABLE_AND_INTERPRETABLE"
    """
    Explainability concerns the mechanisms underlying an AI system's
    operation; interpretability concerns the meaning of its output
    in context.
    """
    PRIVACY_ENHANCED = "PRIVACY_ENHANCED"
    """
    Norms and practices that help safeguard human autonomy,
    identity, and dignity - including anonymity, confidentiality,
    and control over personal information.
    """
    FAIR_WITH_HARMFUL_BIAS_MANAGED = "FAIR_WITH_HARMFUL_BIAS_MANAGED"
    """
    Concerns for equality and equity by addressing issues such as
    harmful bias and discrimination, and recognising that
    perceptions of fairness differ across cultures and
    applications.
    """


class HarmCategoryEnum(str, Enum):
    """
    High-level categories of harm related to AI systems (Figure 1).
    """
    HARM_TO_PEOPLE = "HARM_TO_PEOPLE"
    """
    Harm to individuals, groups/communities, or society at large
    (including civil liberties, rights, physical or psychological
    safety, economic opportunity, democratic participation, and
    educational access).
    """
    HARM_TO_AN_ORGANIZATION = "HARM_TO_AN_ORGANIZATION"
    """
    Harm to an organization's business operations, security
    breaches or monetary loss, or reputation.
    """
    HARM_TO_AN_ECOSYSTEM = "HARM_TO_AN_ECOSYSTEM"
    """
    Harm to interconnected and interdependent elements and
    resources, the global financial system, supply chain, natural
    resources, the environment, and the planet.
    """


class HarmToPeopleSubcategoryEnum(str, Enum):
    """
    Sub-categories of harm to people, per Figure 1.
    """
    INDIVIDUAL = "INDIVIDUAL"
    """
    Harm to a person's civil liberties, rights, physical or
    psychological safety, or economic opportunity.
    """
    GROUP_OR_COMMUNITY = "GROUP_OR_COMMUNITY"
    """
    Harm to a group such as discrimination against a population
    sub-group.
    """
    SOCIETAL = "SOCIETAL"
    """
    Harm to democratic participation or educational access.
    """


class BiasCategoryEnum(str, Enum):
    """
    The three major categories of AI bias identified by NIST
(Part 1 §3.7; see NIST SP 1270).
    """
    SYSTEMIC = "SYSTEMIC"
    """
    Bias present in AI datasets, organizational norms, practices,
    and processes across the AI lifecycle, and the broader society
    that uses AI systems.
    """
    COMPUTATIONAL_AND_STATISTICAL = "COMPUTATIONAL_AND_STATISTICAL"
    """
    Bias present in AI datasets and algorithmic processes; often
    stems from systematic errors due to non-representative samples.
    """
    HUMAN_COGNITIVE = "HUMAN_COGNITIVE"
    """
    Bias related to how an individual or group perceives AI system
    information to make a decision or fill in missing information;
    omnipresent in decision-making across the AI lifecycle.
    """


class RiskMeasurementChallengeEnum(str, Enum):
    """
    Challenges that complicate AI risk measurement (Part 1 §1.2.1).
    """
    THIRD_PARTY_SOFTWARE_HARDWARE_AND_DATA = "THIRD_PARTY_SOFTWARE_HARDWARE_AND_DATA"
    """
    Risks related to third-party software, hardware, and data,
    including misalignment of risk metrics or methodologies between
    developers, deployers, and operators.
    """
    TRACKING_EMERGENT_RISKS = "TRACKING_EMERGENT_RISKS"
    """
    Identifying and tracking emergent risks and considering
    techniques for measuring them; impact assessment helps
    understand context-specific harms.
    """
    AVAILABILITY_OF_RELIABLE_METRICS = "AVAILABILITY_OF_RELIABLE_METRICS"
    """
    Lack of consensus on robust and verifiable measurement methods
    for risk and trustworthiness, and their applicability to
    different use cases.
    """
    RISK_AT_DIFFERENT_LIFECYCLE_STAGES = "RISK_AT_DIFFERENT_LIFECYCLE_STAGES"
    """
    Measuring risk at different stages may yield different results;
    some risks may be latent and increase as systems adapt and
    evolve.
    """
    RISK_IN_REAL_WORLD_SETTINGS = "RISK_IN_REAL_WORLD_SETTINGS"
    """
    Lab measurements may differ from risks that emerge in
    operational, real-world settings.
    """
    INSCRUTABILITY = "INSCRUTABILITY"
    """
    Opaque systems with limited explainability or interpretability,
    poor documentation, or inherent uncertainty complicate risk
    measurement.
    """
    HUMAN_BASELINE = "HUMAN_BASELINE"
    """
    AI systems intended to augment or replace human activity
    require a human baseline for comparison, which is difficult to
    systematize.
    """


class RiskResponseEnum(str, Enum):
    """
    Treatment options for AI risks (MANAGE 1.3).
    """
    MITIGATING = "MITIGATING"
    """
    Reducing the likelihood or magnitude of the risk.
    """
    TRANSFERRING = "TRANSFERRING"
    """
    Shifting the risk to another party (e.g., via insurance or contract).
    """
    AVOIDING = "AVOIDING"
    """
    Choosing not to engage in the activity that creates the risk.
    """
    ACCEPTING = "ACCEPTING"
    """
    Acknowledging the risk and taking no further action.
    """


class ProfileTypeEnum(str, Enum):
    """
    Types of AI RMF Profile (§6).
    """
    USE_CASE = "USE_CASE"
    """
    Implementation of the AI RMF Core for a specific setting or
    application (e.g., a hiring profile, a fair housing profile).
    """
    TEMPORAL_CURRENT = "TEMPORAL_CURRENT"
    """
    Description of the current state of AI risk management
    activities within a sector, industry, organization, or
    application context.
    """
    TEMPORAL_TARGET = "TEMPORAL_TARGET"
    """
    Description of the desired or target state of AI risk
    management activities.
    """
    CROSS_SECTORAL = "CROSS_SECTORAL"
    """
    Risks of models or applications used across use cases or
    sectors (e.g., large language models, cloud-based services,
    acquisition).
    """


class AudienceEnum(str, Enum):
    """
    Audience categorisation for the AI RMF (Part 1 §2).
    """
    PRIMARY = "PRIMARY"
    """
    AI actors who perform or manage the design, development,
    deployment, evaluation, and use of AI systems and drive AI
    risk management efforts.
    """
    INFORMING = "INFORMING"
    """
    AI actors in the People and Planet dimension who *inform* the
    primary audience - trade associations, standards developers,
    researchers, advocacy groups, civil society organisations,
    end users, and impacted individuals or communities.
    """


class ImpactSignEnum(str, Enum):
    """
    Whether an impact of an AI system is positive, negative, or both
(Part 1 §1.1).
    """
    POSITIVE = "POSITIVE"
    """
    A beneficial impact or opportunity.
    """
    NEGATIVE = "NEGATIVE"
    """
    A harmful impact or threat.
    """
    MIXED = "MIXED"
    """
    An impact that is both positive and negative.
    """



class NamedThingRMF(ConfiguredBaseModel):
    """
    A generic grouping for any identifiable AI RMF element.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'class_uri': 'schema:Thing',
         'close_mappings': ['schema:Thing'],
         'from_schema': 'https://w3id.org/lmodel/nist-ai-100-1',
         'in_subset': ['base']})

    id: str = Field(default=..., description="""A unique identifier for an element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThingRMF'],
         'in_subset': ['base'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A short human-readable name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThingRMF'],
         'in_subset': ['base'],
         'slot_uri': 'rdfs:label'} })
    title: Optional[str] = Field(default=None, description="""A human-readable title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThingRMF', 'PlaybookEntry'],
         'in_subset': ['base'],
         'slot_uri': 'dcterms:title'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThingRMF', 'PlaybookEntry'],
         'in_subset': ['base'],
         'slot_uri': 'dcterms:description'} })
    see_also: Optional[list[str]] = Field(default=None, description="""Related references.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThingRMF'],
         'in_subset': ['base'],
         'slot_uri': 'rdfs:seeAlso'} })


class AiSystem(NamedThingRMF):
    """
    An engineered or machine-based system that can, for a given set
    of objectives, generate outputs such as predictions,
    recommendations, or decisions influencing real or virtual
    environments. AI systems are designed to operate with varying
    levels of autonomy (Adapted from OECD Recommendation on AI:2019;
    ISO/IEC 22989:2022).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'close_mappings': ['schema:SoftwareApplication'],
         'from_schema': 'https://w3id.org/lmodel/nist-ai-100-1',
         'in_subset': ['lifecycle']})

    lifecycle_stage: Optional[list[AiLifecycleStageEnum]] = Field(default=None, description="""The AI lifecycle stage(s) the element applies to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiSystem', 'AiActor', 'AiActorTask', 'Risk', 'Subcategory'],
         'in_subset': ['lifecycle']} })
    ai_dimension: Optional[list[AiSystemDimensionEnum]] = Field(default=None, description="""The AI system dimension the element applies to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiSystem', 'AiActorTask'], 'in_subset': ['lifecycle']} })
    id: str = Field(default=..., description="""A unique identifier for an element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThingRMF'],
         'in_subset': ['base'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A short human-readable name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThingRMF'],
         'in_subset': ['base'],
         'slot_uri': 'rdfs:label'} })
    title: Optional[str] = Field(default=None, description="""A human-readable title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThingRMF', 'PlaybookEntry'],
         'in_subset': ['base'],
         'slot_uri': 'dcterms:title'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThingRMF', 'PlaybookEntry'],
         'in_subset': ['base'],
         'slot_uri': 'dcterms:description'} })
    see_also: Optional[list[str]] = Field(default=None, description="""Related references.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThingRMF'],
         'in_subset': ['base'],
         'slot_uri': 'rdfs:seeAlso'} })


class AiSystemDimension(NamedThingRMF):
    """
    A socio-technical dimension of an AI system (Figure 2):
    Application Context, Data and Input, AI Model, Task and Output,
    or People and Planet.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/nist-ai-100-1',
         'in_subset': ['lifecycle']})

    dimension_kind: AiSystemDimensionEnum = Field(default=..., description="""Which AI system dimension an `AiSystemDimension` instance represents.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiSystemDimension'], 'in_subset': ['lifecycle']} })
    id: str = Field(default=..., description="""A unique identifier for an element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThingRMF'],
         'in_subset': ['base'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A short human-readable name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThingRMF'],
         'in_subset': ['base'],
         'slot_uri': 'rdfs:label'} })
    title: Optional[str] = Field(default=None, description="""A human-readable title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThingRMF', 'PlaybookEntry'],
         'in_subset': ['base'],
         'slot_uri': 'dcterms:title'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThingRMF', 'PlaybookEntry'],
         'in_subset': ['base'],
         'slot_uri': 'dcterms:description'} })
    see_also: Optional[list[str]] = Field(default=None, description="""Related references.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThingRMF'],
         'in_subset': ['base'],
         'slot_uri': 'rdfs:seeAlso'} })


class AiLifecycleStage(NamedThingRMF):
    """
    A stage of the AI lifecycle (Figure 2): Plan and Design,
    Collect and Process Data, Build and Use Model, Verify and
    Validate, Deploy and Use, or Operate and Monitor.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/nist-ai-100-1',
         'in_subset': ['lifecycle']})

    stage_kind: AiLifecycleStageEnum = Field(default=..., description="""Which AI lifecycle stage an `AiLifecycleStage` instance represents.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiLifecycleStage'], 'in_subset': ['lifecycle']} })
    includes_tevv: Optional[bool] = Field(default=None, description="""Whether the lifecycle stage incorporates TEVV activities.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiLifecycleStage'], 'in_subset': ['lifecycle']} })
    id: str = Field(default=..., description="""A unique identifier for an element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThingRMF'],
         'in_subset': ['base'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A short human-readable name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThingRMF'],
         'in_subset': ['base'],
         'slot_uri': 'rdfs:label'} })
    title: Optional[str] = Field(default=None, description="""A human-readable title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThingRMF', 'PlaybookEntry'],
         'in_subset': ['base'],
         'slot_uri': 'dcterms:title'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThingRMF', 'PlaybookEntry'],
         'in_subset': ['base'],
         'slot_uri': 'dcterms:description'} })
    see_also: Optional[list[str]] = Field(default=None, description="""Related references.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThingRMF'],
         'in_subset': ['base'],
         'slot_uri': 'rdfs:seeAlso'} })


class AiActor(NamedThingRMF):
    """
    An organization or individual that plays an active role in the AI
    system lifecycle. AI actors include those who deploy or operate
    AI as well as those who inform via formal or quasi-formal norms
    and guidance (OECD 2019).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'close_mappings': ['prov:Agent', 'foaf:Agent'],
         'from_schema': 'https://w3id.org/lmodel/nist-ai-100-1',
         'in_subset': ['lifecycle'],
         'related_mappings': ['stix:Identity', 'iso27001:InterestedParty']})

    actor_task: Optional[list[AiActorTaskEnum]] = Field(default=None, description="""AI actor task category.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiActor'], 'in_subset': ['lifecycle']} })
    lifecycle_stage: Optional[list[AiLifecycleStageEnum]] = Field(default=None, description="""The AI lifecycle stage(s) the element applies to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiSystem', 'AiActor', 'AiActorTask', 'Risk', 'Subcategory'],
         'in_subset': ['lifecycle']} })
    is_tevv: Optional[bool] = Field(default=None, description="""Whether the actor or task is a Test, Evaluation, Verification, and
Validation (TEVV) actor / task.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiActor'], 'in_subset': ['lifecycle']} })
    audience: Optional[AudienceEnum] = Field(default=None, description="""Whether the actor is part of the *primary* AI RMF audience or the
*informing* People-and-Planet audience.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiActor'], 'in_subset': ['lifecycle']} })
    id: str = Field(default=..., description="""A unique identifier for an element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThingRMF'],
         'in_subset': ['base'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A short human-readable name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThingRMF'],
         'in_subset': ['base'],
         'slot_uri': 'rdfs:label'} })
    title: Optional[str] = Field(default=None, description="""A human-readable title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThingRMF', 'PlaybookEntry'],
         'in_subset': ['base'],
         'slot_uri': 'dcterms:title'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThingRMF', 'PlaybookEntry'],
         'in_subset': ['base'],
         'slot_uri': 'dcterms:description'} })
    see_also: Optional[list[str]] = Field(default=None, description="""Related references.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThingRMF'],
         'in_subset': ['base'],
         'slot_uri': 'rdfs:seeAlso'} })


class AiActorTask(NamedThingRMF):
    """
    A category of task performed by AI actors (Appendix A). Each
    task is associated with one or more lifecycle stages and a
    typical set of actor roles.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/nist-ai-100-1',
         'in_subset': ['lifecycle']})

    task_kind: AiActorTaskEnum = Field(default=..., description="""Which AI actor task category an `AiActorTask` instance represents.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiActorTask'], 'in_subset': ['lifecycle']} })
    typical_actors: Optional[list[str]] = Field(default=None, description="""Representative actor roles that perform an AI actor task.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiActorTask'], 'in_subset': ['lifecycle']} })
    lifecycle_stage: Optional[list[AiLifecycleStageEnum]] = Field(default=None, description="""The AI lifecycle stage(s) the element applies to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiSystem', 'AiActor', 'AiActorTask', 'Risk', 'Subcategory'],
         'in_subset': ['lifecycle']} })
    ai_dimension: Optional[list[AiSystemDimensionEnum]] = Field(default=None, description="""The AI system dimension the element applies to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiSystem', 'AiActorTask'], 'in_subset': ['lifecycle']} })
    id: str = Field(default=..., description="""A unique identifier for an element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThingRMF'],
         'in_subset': ['base'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A short human-readable name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThingRMF'],
         'in_subset': ['base'],
         'slot_uri': 'rdfs:label'} })
    title: Optional[str] = Field(default=None, description="""A human-readable title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThingRMF', 'PlaybookEntry'],
         'in_subset': ['base'],
         'slot_uri': 'dcterms:title'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThingRMF', 'PlaybookEntry'],
         'in_subset': ['base'],
         'slot_uri': 'dcterms:description'} })
    see_also: Optional[list[str]] = Field(default=None, description="""Related references.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThingRMF'],
         'in_subset': ['base'],
         'slot_uri': 'rdfs:seeAlso'} })


class Risk(NamedThingRMF):
    """
    The composite measure of an event's probability of occurring and
    the magnitude or degree of the consequences of that event. When
    considering negative impact, risk is a function of (1) the
    negative impact or magnitude of harm and (2) the likelihood of
    occurrence (Adapted from ISO 31000:2018; OMB Circular A-130:2016).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['iso27001:Risk'],
         'from_schema': 'https://w3id.org/lmodel/nist-ai-100-1',
         'in_subset': ['risk_and_harm'],
         'related_mappings': ['iso29100:PrivacyRisk']})

    likelihood: Optional[float] = Field(default=None, description="""Estimated probability of the event occurring (0.0 to 1.0). The
AI RMF leaves quantification approaches to the implementer.""", ge=0.0, le=1.0, json_schema_extra = { "linkml_meta": {'close_mappings': ['iso27001:LikelihoodRating'],
         'domain_of': ['Risk', 'Impact'],
         'in_subset': ['risk_and_harm']} })
    magnitude: Optional[str] = Field(default=None, description="""Magnitude or degree of consequences if the event occurs (free
text or qualitative scale).""", json_schema_extra = { "linkml_meta": {'close_mappings': ['iso27001:ImpactRating'],
         'domain_of': ['Risk', 'Impact', 'Harm'],
         'in_subset': ['risk_and_harm']} })
    impact_sign: Optional[ImpactSignEnum] = Field(default=None, description="""Whether the impact is positive, negative, or both.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Risk', 'Impact'], 'in_subset': ['risk_and_harm']} })
    is_residual: Optional[bool] = Field(default=None, description="""Whether this risk represents risk remaining after risk treatment
(residual risk per ISO Guide 73).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Risk'], 'in_subset': ['risk_and_harm']} })
    risk_response: Optional[RiskResponseEnum] = Field(default=None, description="""The chosen risk treatment option.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Risk'],
         'exact_mappings': ['iso27001:RiskTreatmentOption'],
         'in_subset': ['risk_and_harm']} })
    lifecycle_stage: Optional[list[AiLifecycleStageEnum]] = Field(default=None, description="""The AI lifecycle stage(s) the element applies to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiSystem', 'AiActor', 'AiActorTask', 'Risk', 'Subcategory'],
         'in_subset': ['lifecycle']} })
    trustworthiness_characteristic: Optional[list[TrustworthinessCharacteristicEnum]] = Field(default=None, description="""Trustworthiness characteristic(s) the element pertains to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Risk', 'Subcategory'], 'in_subset': ['trustworthiness']} })
    related_impacts: Optional[list[Impact]] = Field(default=None, description="""The impacts that contribute to a risk.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Risk'], 'in_subset': ['risk_and_harm']} })
    affects_system: Optional[str] = Field(default=None, description="""The AI system a risk pertains to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Risk'], 'in_subset': ['risk_and_harm']} })
    id: str = Field(default=..., description="""A unique identifier for an element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThingRMF'],
         'in_subset': ['base'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A short human-readable name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThingRMF'],
         'in_subset': ['base'],
         'slot_uri': 'rdfs:label'} })
    title: Optional[str] = Field(default=None, description="""A human-readable title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThingRMF', 'PlaybookEntry'],
         'in_subset': ['base'],
         'slot_uri': 'dcterms:title'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThingRMF', 'PlaybookEntry'],
         'in_subset': ['base'],
         'slot_uri': 'dcterms:description'} })
    see_also: Optional[list[str]] = Field(default=None, description="""Related references.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThingRMF'],
         'in_subset': ['base'],
         'slot_uri': 'rdfs:seeAlso'} })


class Impact(NamedThingRMF):
    """
    A positive, negative, or both consequence of an AI system. Impacts
    can manifest as opportunities (positive) or threats (negative).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/nist-ai-100-1',
         'in_subset': ['risk_and_harm'],
         'narrow_mappings': ['iso27001:ImpactRating']})

    impact_sign: Optional[ImpactSignEnum] = Field(default=None, description="""Whether the impact is positive, negative, or both.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Risk', 'Impact'], 'in_subset': ['risk_and_harm']} })
    magnitude: Optional[str] = Field(default=None, description="""Magnitude or degree of consequences if the event occurs (free
text or qualitative scale).""", json_schema_extra = { "linkml_meta": {'close_mappings': ['iso27001:ImpactRating'],
         'domain_of': ['Risk', 'Impact', 'Harm'],
         'in_subset': ['risk_and_harm']} })
    likelihood: Optional[float] = Field(default=None, description="""Estimated probability of the event occurring (0.0 to 1.0). The
AI RMF leaves quantification approaches to the implementer.""", ge=0.0, le=1.0, json_schema_extra = { "linkml_meta": {'close_mappings': ['iso27001:LikelihoodRating'],
         'domain_of': ['Risk', 'Impact'],
         'in_subset': ['risk_and_harm']} })
    affects: Optional[list[str]] = Field(default=None, description="""Entities (people, organizations, ecosystems) the risk or harm
may affect.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Impact', 'Harm'], 'in_subset': ['risk_and_harm']} })
    id: str = Field(default=..., description="""A unique identifier for an element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThingRMF'],
         'in_subset': ['base'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A short human-readable name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThingRMF'],
         'in_subset': ['base'],
         'slot_uri': 'rdfs:label'} })
    title: Optional[str] = Field(default=None, description="""A human-readable title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThingRMF', 'PlaybookEntry'],
         'in_subset': ['base'],
         'slot_uri': 'dcterms:title'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThingRMF', 'PlaybookEntry'],
         'in_subset': ['base'],
         'slot_uri': 'dcterms:description'} })
    see_also: Optional[list[str]] = Field(default=None, description="""Related references.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThingRMF'],
         'in_subset': ['base'],
         'slot_uri': 'rdfs:seeAlso'} })


class Harm(NamedThingRMF):
    """
    A negative impact that may be experienced by individuals,
    groups, communities, organizations, society, the environment, or
    the planet (Figure 1).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/nist-ai-100-1',
         'in_subset': ['risk_and_harm']})

    harm_category: Optional[HarmCategoryEnum] = Field(default=None, description="""The high-level harm category (people / organization / ecosystem).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Harm'], 'in_subset': ['risk_and_harm']} })
    harm_to_people_subcategory: Optional[HarmToPeopleSubcategoryEnum] = Field(default=None, description="""The sub-category when harm is to people (individual / group / societal).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Harm'], 'in_subset': ['risk_and_harm']} })
    magnitude: Optional[str] = Field(default=None, description="""Magnitude or degree of consequences if the event occurs (free
text or qualitative scale).""", json_schema_extra = { "linkml_meta": {'close_mappings': ['iso27001:ImpactRating'],
         'domain_of': ['Risk', 'Impact', 'Harm'],
         'in_subset': ['risk_and_harm']} })
    affects: Optional[list[str]] = Field(default=None, description="""Entities (people, organizations, ecosystems) the risk or harm
may affect.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Impact', 'Harm'], 'in_subset': ['risk_and_harm']} })
    id: str = Field(default=..., description="""A unique identifier for an element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThingRMF'],
         'in_subset': ['base'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A short human-readable name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThingRMF'],
         'in_subset': ['base'],
         'slot_uri': 'rdfs:label'} })
    title: Optional[str] = Field(default=None, description="""A human-readable title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThingRMF', 'PlaybookEntry'],
         'in_subset': ['base'],
         'slot_uri': 'dcterms:title'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThingRMF', 'PlaybookEntry'],
         'in_subset': ['base'],
         'slot_uri': 'dcterms:description'} })
    see_also: Optional[list[str]] = Field(default=None, description="""Related references.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThingRMF'],
         'in_subset': ['base'],
         'slot_uri': 'rdfs:seeAlso'} })


class ResidualRisk(Risk):
    """
    Risk remaining after risk treatment (ISO Guide 73). Documenting
    residual risks helps system providers consider risks of deploying
    the AI product and informs end users about potential negative
    impacts.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/nist-ai-100-1',
         'in_subset': ['risk_and_harm'],
         'narrow_mappings': ['iso27001:Risk'],
         'slot_usage': {'is_residual': {'ifabsent': 'True', 'name': 'is_residual'}}})

    likelihood: Optional[float] = Field(default=None, description="""Estimated probability of the event occurring (0.0 to 1.0). The
AI RMF leaves quantification approaches to the implementer.""", ge=0.0, le=1.0, json_schema_extra = { "linkml_meta": {'close_mappings': ['iso27001:LikelihoodRating'],
         'domain_of': ['Risk', 'Impact'],
         'in_subset': ['risk_and_harm']} })
    magnitude: Optional[str] = Field(default=None, description="""Magnitude or degree of consequences if the event occurs (free
text or qualitative scale).""", json_schema_extra = { "linkml_meta": {'close_mappings': ['iso27001:ImpactRating'],
         'domain_of': ['Risk', 'Impact', 'Harm'],
         'in_subset': ['risk_and_harm']} })
    impact_sign: Optional[ImpactSignEnum] = Field(default=None, description="""Whether the impact is positive, negative, or both.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Risk', 'Impact'], 'in_subset': ['risk_and_harm']} })
    is_residual: Optional[bool] = Field(default=True, description="""Whether this risk represents risk remaining after risk treatment
(residual risk per ISO Guide 73).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Risk'], 'ifabsent': 'True', 'in_subset': ['risk_and_harm']} })
    risk_response: Optional[RiskResponseEnum] = Field(default=None, description="""The chosen risk treatment option.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Risk'],
         'exact_mappings': ['iso27001:RiskTreatmentOption'],
         'in_subset': ['risk_and_harm']} })
    lifecycle_stage: Optional[list[AiLifecycleStageEnum]] = Field(default=None, description="""The AI lifecycle stage(s) the element applies to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiSystem', 'AiActor', 'AiActorTask', 'Risk', 'Subcategory'],
         'in_subset': ['lifecycle']} })
    trustworthiness_characteristic: Optional[list[TrustworthinessCharacteristicEnum]] = Field(default=None, description="""Trustworthiness characteristic(s) the element pertains to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Risk', 'Subcategory'], 'in_subset': ['trustworthiness']} })
    related_impacts: Optional[list[Impact]] = Field(default=None, description="""The impacts that contribute to a risk.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Risk'], 'in_subset': ['risk_and_harm']} })
    affects_system: Optional[str] = Field(default=None, description="""The AI system a risk pertains to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Risk'], 'in_subset': ['risk_and_harm']} })
    id: str = Field(default=..., description="""A unique identifier for an element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThingRMF'],
         'in_subset': ['base'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A short human-readable name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThingRMF'],
         'in_subset': ['base'],
         'slot_uri': 'rdfs:label'} })
    title: Optional[str] = Field(default=None, description="""A human-readable title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThingRMF', 'PlaybookEntry'],
         'in_subset': ['base'],
         'slot_uri': 'dcterms:title'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThingRMF', 'PlaybookEntry'],
         'in_subset': ['base'],
         'slot_uri': 'dcterms:description'} })
    see_also: Optional[list[str]] = Field(default=None, description="""Related references.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThingRMF'],
         'in_subset': ['base'],
         'slot_uri': 'rdfs:seeAlso'} })


class RiskTolerance(NamedThingRMF):
    """
    The organization's or AI actor's readiness to bear risk in order
    to achieve its objectives (Adapted from ISO Guide 73). Risk
    tolerance is highly contextual and application- and use-case
    specific.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'close_mappings': ['iso27001:RiskLevel'],
         'from_schema': 'https://w3id.org/lmodel/nist-ai-100-1',
         'in_subset': ['risk_and_harm']})

    tolerance_statement: Optional[str] = Field(default=None, description="""Free-text statement of a risk tolerance level or threshold.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RiskTolerance'], 'in_subset': ['risk_and_harm']} })
    legal_basis: Optional[str] = Field(default=None, description="""Legal or regulatory requirements influencing a risk tolerance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RiskTolerance'], 'in_subset': ['risk_and_harm']} })
    id: str = Field(default=..., description="""A unique identifier for an element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThingRMF'],
         'in_subset': ['base'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A short human-readable name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThingRMF'],
         'in_subset': ['base'],
         'slot_uri': 'rdfs:label'} })
    title: Optional[str] = Field(default=None, description="""A human-readable title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThingRMF', 'PlaybookEntry'],
         'in_subset': ['base'],
         'slot_uri': 'dcterms:title'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThingRMF', 'PlaybookEntry'],
         'in_subset': ['base'],
         'slot_uri': 'dcterms:description'} })
    see_also: Optional[list[str]] = Field(default=None, description="""Related references.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThingRMF'],
         'in_subset': ['base'],
         'slot_uri': 'rdfs:seeAlso'} })


class RiskMeasurementChallenge(NamedThingRMF):
    """
    A challenge that complicates measurement of AI risks
    (Part 1 §1.2.1).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/nist-ai-100-1',
         'in_subset': ['risk_and_harm']})

    challenge_kind: RiskMeasurementChallengeEnum = Field(default=..., description="""Which risk-measurement challenge a `RiskMeasurementChallenge` represents.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RiskMeasurementChallenge'], 'in_subset': ['risk_and_harm']} })
    id: str = Field(default=..., description="""A unique identifier for an element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThingRMF'],
         'in_subset': ['base'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A short human-readable name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThingRMF'],
         'in_subset': ['base'],
         'slot_uri': 'rdfs:label'} })
    title: Optional[str] = Field(default=None, description="""A human-readable title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThingRMF', 'PlaybookEntry'],
         'in_subset': ['base'],
         'slot_uri': 'dcterms:title'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThingRMF', 'PlaybookEntry'],
         'in_subset': ['base'],
         'slot_uri': 'dcterms:description'} })
    see_also: Optional[list[str]] = Field(default=None, description="""Related references.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThingRMF'],
         'in_subset': ['base'],
         'slot_uri': 'rdfs:seeAlso'} })


class TrustworthinessCharacteristic(NamedThingRMF):
    """
    A characteristic of a trustworthy AI system (Figure 4 / Part 1
    §3). The seven characteristics are inter-related; addressing them
    individually does not guarantee trustworthiness, and tradeoffs
    are usually involved.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/nist-ai-100-1',
         'in_subset': ['trustworthiness']})

    characteristic_kind: TrustworthinessCharacteristicEnum = Field(default=..., description="""Which trustworthiness characteristic a `TrustworthinessCharacteristic` represents.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TrustworthinessCharacteristic'],
         'in_subset': ['trustworthiness']} })
    is_base_condition: Optional[bool] = Field(default=None, description="""True when this characteristic is a necessary condition for
trustworthiness (per Figure 4 - Valid and Reliable is the base
of all others).""", json_schema_extra = { "linkml_meta": {'domain_of': ['TrustworthinessCharacteristic'],
         'in_subset': ['trustworthiness']} })
    is_cross_cutting: Optional[bool] = Field(default=None, description="""True when this characteristic relates to all others
(Accountable and Transparent; shown vertically in Figure 4).""", json_schema_extra = { "linkml_meta": {'domain_of': ['TrustworthinessCharacteristic'],
         'in_subset': ['trustworthiness']} })
    id: str = Field(default=..., description="""A unique identifier for an element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThingRMF'],
         'in_subset': ['base'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A short human-readable name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThingRMF'],
         'in_subset': ['base'],
         'slot_uri': 'rdfs:label'} })
    title: Optional[str] = Field(default=None, description="""A human-readable title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThingRMF', 'PlaybookEntry'],
         'in_subset': ['base'],
         'slot_uri': 'dcterms:title'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThingRMF', 'PlaybookEntry'],
         'in_subset': ['base'],
         'slot_uri': 'dcterms:description'} })
    see_also: Optional[list[str]] = Field(default=None, description="""Related references.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThingRMF'],
         'in_subset': ['base'],
         'slot_uri': 'rdfs:seeAlso'} })


class Bias(NamedThingRMF):
    """
    A form of AI bias - a deviation that may be perpetuated or
    amplified by AI systems. NIST identifies three major categories:
    systemic, computational/statistical, and human-cognitive
    (Part 1 §3.7; NIST SP 1270).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/nist-ai-100-1',
         'in_subset': ['trustworthiness'],
         'related_mappings': ['iso29100:PrivacyPrinciple']})

    bias_category: Optional[list[BiasCategoryEnum]] = Field(default=None, description="""Category or categories of bias addressed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Bias'], 'in_subset': ['trustworthiness']} })
    id: str = Field(default=..., description="""A unique identifier for an element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThingRMF'],
         'in_subset': ['base'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A short human-readable name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThingRMF'],
         'in_subset': ['base'],
         'slot_uri': 'rdfs:label'} })
    title: Optional[str] = Field(default=None, description="""A human-readable title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThingRMF', 'PlaybookEntry'],
         'in_subset': ['base'],
         'slot_uri': 'dcterms:title'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThingRMF', 'PlaybookEntry'],
         'in_subset': ['base'],
         'slot_uri': 'dcterms:description'} })
    see_also: Optional[list[str]] = Field(default=None, description="""Related references.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThingRMF'],
         'in_subset': ['base'],
         'slot_uri': 'rdfs:seeAlso'} })


class Function(NamedThingRMF):
    """
    A top-level AI RMF Core function. Each function organizes AI risk
    management activities at the highest level. GOVERN applies across
    all stages; MAP, MEASURE, and MANAGE apply to AI-system-specific
    contexts and lifecycle stages.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['nist_csf:CSFFunction'],
         'from_schema': 'https://w3id.org/lmodel/nist-ai-100-1',
         'in_subset': ['framework_core'],
         'related_mappings': ['gist_linkml:Function'],
         'slot_usage': {'categories': {'inlined': True,
                                       'inlined_as_list': True,
                                       'multivalued': True,
                                       'name': 'categories',
                                       'range': 'Category'}}})

    function_code: str = Field(default=..., description="""The function code (GOVERN, MAP, MEASURE, or MANAGE).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Function'], 'in_subset': ['framework_core']} })
    categories: Optional[list[Category]] = Field(default=None, description="""Categories that belong to a Function.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Function'], 'in_subset': ['framework_core']} })
    id: str = Field(default=..., description="""A unique identifier for an element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThingRMF'],
         'in_subset': ['base'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A short human-readable name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThingRMF'],
         'in_subset': ['base'],
         'slot_uri': 'rdfs:label'} })
    title: Optional[str] = Field(default=None, description="""A human-readable title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThingRMF', 'PlaybookEntry'],
         'in_subset': ['base'],
         'slot_uri': 'dcterms:title'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThingRMF', 'PlaybookEntry'],
         'in_subset': ['base'],
         'slot_uri': 'dcterms:description'} })
    see_also: Optional[list[str]] = Field(default=None, description="""Related references.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThingRMF'],
         'in_subset': ['base'],
         'slot_uri': 'rdfs:seeAlso'} })


class Category(NamedThingRMF):
    """
    A category within an AI RMF Core function (e.g., \"GOVERN 1:
    Policies, processes, procedures, and practices ... are in place,
    transparent, and implemented effectively\"). Categories group
    related subcategories.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['nist_csf:CSFCategory'],
         'from_schema': 'https://w3id.org/lmodel/nist-ai-100-1',
         'in_subset': ['framework_core'],
         'slot_usage': {'id': {'description': 'Identifier for the category, typically '
                                              'using the\n'
                                              '"FUNCTION N" form (e.g., "GOVERN 1").',
                               'name': 'id'},
                        'subcategories': {'inlined': True,
                                          'inlined_as_list': True,
                                          'multivalued': True,
                                          'name': 'subcategories',
                                          'range': 'Subcategory'}}})

    category_id: Optional[str] = Field(default=None, description="""Identifier of a Category (e.g., \"GOVERN 1\").""", json_schema_extra = { "linkml_meta": {'domain_of': ['Category'], 'in_subset': ['framework_core']} })
    outcome: Optional[str] = Field(default=None, description="""The outcome statement of a Category or Subcategory - the desired
result of carrying out its actions.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['nist_csf:prose'],
         'domain_of': ['Category', 'Subcategory'],
         'in_subset': ['framework_core']} })
    subcategories: Optional[list[Subcategory]] = Field(default=None, description="""Subcategories that belong to a Category.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Category'], 'in_subset': ['framework_core']} })
    id: str = Field(default=..., description="""Identifier for the category, typically using the
\"FUNCTION N\" form (e.g., \"GOVERN 1\").""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThingRMF'],
         'in_subset': ['base'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A short human-readable name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThingRMF'],
         'in_subset': ['base'],
         'slot_uri': 'rdfs:label'} })
    title: Optional[str] = Field(default=None, description="""A human-readable title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThingRMF', 'PlaybookEntry'],
         'in_subset': ['base'],
         'slot_uri': 'dcterms:title'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThingRMF', 'PlaybookEntry'],
         'in_subset': ['base'],
         'slot_uri': 'dcterms:description'} })
    see_also: Optional[list[str]] = Field(default=None, description="""Related references.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThingRMF'],
         'in_subset': ['base'],
         'slot_uri': 'rdfs:seeAlso'} })


class Subcategory(NamedThingRMF):
    """
    A subcategory within an AI RMF Core category (e.g., \"GOVERN 1.1:
    Legal and regulatory requirements involving AI are understood,
    managed, and documented\"). Subcategories express specific
    outcomes.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'close_mappings': ['oscal_catalog:Control', 'nist_sp_800_53:Control'],
         'exact_mappings': ['nist_csf:CSFSubcategory'],
         'from_schema': 'https://w3id.org/lmodel/nist-ai-100-1',
         'in_subset': ['framework_core'],
         'slot_usage': {'id': {'description': 'Identifier for the subcategory in the '
                                              '"FUNCTION N.M" form\n'
                                              '(e.g., "GOVERN 1.1").',
                               'name': 'id'}}})

    subcategory_id: Optional[str] = Field(default=None, description="""Identifier of a Subcategory (e.g., \"GOVERN 1.1\").""", json_schema_extra = { "linkml_meta": {'domain_of': ['Subcategory'], 'in_subset': ['framework_core']} })
    outcome: Optional[str] = Field(default=None, description="""The outcome statement of a Category or Subcategory - the desired
result of carrying out its actions.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['nist_csf:prose'],
         'domain_of': ['Category', 'Subcategory'],
         'in_subset': ['framework_core']} })
    trustworthiness_characteristic: Optional[list[TrustworthinessCharacteristicEnum]] = Field(default=None, description="""Trustworthiness characteristic(s) the element pertains to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Risk', 'Subcategory'], 'in_subset': ['trustworthiness']} })
    lifecycle_stage: Optional[list[AiLifecycleStageEnum]] = Field(default=None, description="""The AI lifecycle stage(s) the element applies to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiSystem', 'AiActor', 'AiActorTask', 'Risk', 'Subcategory'],
         'in_subset': ['lifecycle']} })
    about_text: Optional[str] = Field(default=None, description="""Free-text discussion of the subcategory or related concept.
Corresponds to the AI RMF Playbook \"About\" section.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Subcategory'], 'in_subset': ['playbook']} })
    suggested_actions_text: Optional[str] = Field(default=None, description="""Free-text bulleted list of suggested actions an organization can
take. Corresponds to the AI RMF Playbook \"Actions\" section.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Subcategory'], 'in_subset': ['playbook']} })
    documentation_questions: Optional[str] = Field(default=None, description="""Free-text documentation questions and transparency resources.
Corresponds to the AI RMF Playbook \"Documentation\" section.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Subcategory'], 'in_subset': ['playbook']} })
    references_text: Optional[str] = Field(default=None, description="""Free-text list of references, citations, and supporting
resources. Corresponds to the AI RMF Playbook \"References\"
section.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Subcategory'], 'in_subset': ['playbook']} })
    topics: Optional[list[str]] = Field(default=None, description="""Free-text topic tags applied to a playbook entry (e.g.,
\"Governance\", \"Trustworthy Characteristics\", \"Validity and
Reliability\").""", json_schema_extra = { "linkml_meta": {'domain_of': ['Subcategory'], 'in_subset': ['playbook']} })
    ai_actor_categories: Optional[list[str]] = Field(default=None, description="""Free-text list of AI Actor categories the entry applies to,
preserving the original case used in the AI RMF Playbook
(e.g., \"Governance and Oversight\", \"TEVV\"). For controlled
enum values see `actor_task` (range AiActorTaskEnum).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Subcategory'], 'in_subset': ['playbook']} })
    id: str = Field(default=..., description="""Identifier for the subcategory in the \"FUNCTION N.M\" form
(e.g., \"GOVERN 1.1\").""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThingRMF'],
         'in_subset': ['base'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A short human-readable name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThingRMF'],
         'in_subset': ['base'],
         'slot_uri': 'rdfs:label'} })
    title: Optional[str] = Field(default=None, description="""A human-readable title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThingRMF', 'PlaybookEntry'],
         'in_subset': ['base'],
         'slot_uri': 'dcterms:title'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThingRMF', 'PlaybookEntry'],
         'in_subset': ['base'],
         'slot_uri': 'dcterms:description'} })
    see_also: Optional[list[str]] = Field(default=None, description="""Related references.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThingRMF'],
         'in_subset': ['base'],
         'slot_uri': 'rdfs:seeAlso'} })


class AiRmfProfile(NamedThingRMF):
    """
    An implementation of the AI RMF Functions, Categories, and
    Subcategories for a specific setting or application based on the
    requirements, risk tolerance, and resources of the user (§6).
    Profiles may be use-case-specific, temporal (current or target),
    or cross-sectoral.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'close_mappings': ['nist_sp_800_53:ProfileDocument'],
         'exact_mappings': ['oscal_profile:Profile'],
         'from_schema': 'https://w3id.org/lmodel/nist-ai-100-1',
         'in_subset': ['profiles']})

    profile_type: ProfileTypeEnum = Field(default=..., description="""The kind of AI RMF Profile.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiRmfProfile'], 'in_subset': ['profiles']} })
    current_state: Optional[str] = Field(default=None, description="""For temporal current profiles - how AI is currently being managed
and related risks in terms of current outcomes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiRmfProfile'], 'in_subset': ['profiles']} })
    target_state: Optional[str] = Field(default=None, description="""For temporal target profiles - the outcomes needed to achieve the
desired AI risk management goals.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiRmfProfile'], 'in_subset': ['profiles']} })
    sector: Optional[str] = Field(default=None, description="""The sector, industry, technology, or end-use application a
profile addresses (e.g., \"hiring\", \"fair housing\").""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiRmfProfile'], 'in_subset': ['profiles']} })
    addresses: Optional[list[str]] = Field(default=None, description="""Subcategories that a profile implements or addresses.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiRmfProfile'], 'in_subset': ['profiles']} })
    id: str = Field(default=..., description="""A unique identifier for an element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThingRMF'],
         'in_subset': ['base'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A short human-readable name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThingRMF'],
         'in_subset': ['base'],
         'slot_uri': 'rdfs:label'} })
    title: Optional[str] = Field(default=None, description="""A human-readable title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThingRMF', 'PlaybookEntry'],
         'in_subset': ['base'],
         'slot_uri': 'dcterms:title'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThingRMF', 'PlaybookEntry'],
         'in_subset': ['base'],
         'slot_uri': 'dcterms:description'} })
    see_also: Optional[list[str]] = Field(default=None, description="""Related references.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThingRMF'],
         'in_subset': ['base'],
         'slot_uri': 'rdfs:seeAlso'} })


class RmfAttribute(NamedThingRMF):
    """
    A design attribute of the AI RMF (Appendix D) - one of the
    qualities the Framework strives to embody (e.g., risk-based,
    consensus-driven, plain language, common language, easily usable,
    universally applicable, outcome-focused, leveraging existing
    standards, law- and regulation-agnostic, living document).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/nist-ai-100-1',
         'in_subset': ['attributes'],
         'related_mappings': ['nist_csf:CSFProperty']})

    id: str = Field(default=..., description="""A unique identifier for an element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThingRMF'],
         'in_subset': ['base'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A short human-readable name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThingRMF'],
         'in_subset': ['base'],
         'slot_uri': 'rdfs:label'} })
    title: Optional[str] = Field(default=None, description="""A human-readable title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThingRMF', 'PlaybookEntry'],
         'in_subset': ['base'],
         'slot_uri': 'dcterms:title'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThingRMF', 'PlaybookEntry'],
         'in_subset': ['base'],
         'slot_uri': 'dcterms:description'} })
    see_also: Optional[list[str]] = Field(default=None, description="""Related references.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThingRMF'],
         'in_subset': ['base'],
         'slot_uri': 'rdfs:seeAlso'} })


class AiSpecificRisk(NamedThingRMF):
    """
    A risk that is new or increased for AI-based technology compared
    to traditional software (Appendix B) - e.g., data quality, model
    drift, opacity, scale and complexity, pre-trained model
    uncertainty, emergent properties, privacy aggregation, or
    environmental cost.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'broad_mappings': ['iso27001:Risk'],
         'from_schema': 'https://w3id.org/lmodel/nist-ai-100-1',
         'in_subset': ['ai_risk_distinctions']})

    id: str = Field(default=..., description="""A unique identifier for an element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThingRMF'],
         'in_subset': ['base'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A short human-readable name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThingRMF'],
         'in_subset': ['base'],
         'slot_uri': 'rdfs:label'} })
    title: Optional[str] = Field(default=None, description="""A human-readable title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThingRMF', 'PlaybookEntry'],
         'in_subset': ['base'],
         'slot_uri': 'dcterms:title'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThingRMF', 'PlaybookEntry'],
         'in_subset': ['base'],
         'slot_uri': 'dcterms:description'} })
    see_also: Optional[list[str]] = Field(default=None, description="""Related references.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThingRMF'],
         'in_subset': ['base'],
         'slot_uri': 'rdfs:seeAlso'} })


class HumanAiInteractionIssue(NamedThingRMF):
    """
    An issue that merits further consideration in human-AI
    interaction (Appendix C) - e.g., clear human roles and
    responsibilities, systemic and human-cognitive biases in design,
    variability of human-AI interaction outcomes, complexity of
    presenting AI system information to humans.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/nist-ai-100-1',
         'in_subset': ['human_ai_interaction'],
         'related_mappings': ['iso27001:InterestedParty']})

    id: str = Field(default=..., description="""A unique identifier for an element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThingRMF'],
         'in_subset': ['base'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A short human-readable name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThingRMF'],
         'in_subset': ['base'],
         'slot_uri': 'rdfs:label'} })
    title: Optional[str] = Field(default=None, description="""A human-readable title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThingRMF', 'PlaybookEntry'],
         'in_subset': ['base'],
         'slot_uri': 'dcterms:title'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThingRMF', 'PlaybookEntry'],
         'in_subset': ['base'],
         'slot_uri': 'dcterms:description'} })
    see_also: Optional[list[str]] = Field(default=None, description="""Related references.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThingRMF'],
         'in_subset': ['base'],
         'slot_uri': 'rdfs:seeAlso'} })


class PlaybookEntry(ConfiguredBaseModel):
    """
    A single AI RMF Playbook entry - an enrichment of a Core
    subcategory with prose discussion, suggested actions,
    documentation questions, references, and topic tags.

    Attribute names use the same identifiers found in the published
    NIST AI RMF Playbook JSON (e.g., `section_about`,
    `section_actions`) so that the data can be loaded directly.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'close_mappings': ['nist_csf:CSFSubcategory'],
         'from_schema': 'https://w3id.org/lmodel/nist-ai-100-1',
         'in_subset': ['playbook'],
         'unique_keys': {'primary': {'unique_key_name': 'primary',
                                     'unique_key_slots': ['title']}}})

    type: Optional[str] = Field(default=None, description="""Function label as serialised in the published Playbook JSON
(Title case - \"Govern\", \"Map\", \"Measure\", \"Manage\"). For
the controlled enum see `function_kind`.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PlaybookEntry']} })
    title: Optional[str] = Field(default=None, description="""Subcategory identifier (e.g., \"GOVERN 1.1\"). Mirrors the
AI RMF Subcategory `subcategory_id`.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThingRMF', 'PlaybookEntry']} })
    category: Optional[str] = Field(default=None, description="""Category code in the form \"FUNCTION-N\" (e.g., \"GOVERN-1\")
as used in the Playbook.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PlaybookEntry']} })
    description: Optional[str] = Field(default=None, description="""Outcome statement of the subcategory.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThingRMF', 'PlaybookEntry']} })
    section_about: Optional[str] = Field(default=None, description="""Free-text discussion (\"About\" section).""", json_schema_extra = { "linkml_meta": {'domain_of': ['PlaybookEntry']} })
    section_actions: Optional[str] = Field(default=None, description="""Bulleted suggested actions (\"Actions\" section).""", json_schema_extra = { "linkml_meta": {'domain_of': ['PlaybookEntry']} })
    section_doc: Optional[str] = Field(default=None, description="""Documentation questions and transparency resources
(\"Documentation\" section).""", json_schema_extra = { "linkml_meta": {'domain_of': ['PlaybookEntry']} })
    section_ref: Optional[str] = Field(default=None, description="""References and citations (\"References\" section).""", json_schema_extra = { "linkml_meta": {'domain_of': ['PlaybookEntry']} })
    ai_actors: Optional[list[str]] = Field(default=None, description="""AI actor categories the entry applies to. Free-text to
preserve the casing of the source data (e.g., \"Governance
and Oversight\").""", json_schema_extra = { "linkml_meta": {'domain_of': ['PlaybookEntry']} })
    topic: Optional[list[str]] = Field(default=None, description="""Topic tags (e.g., \"Legal and Regulatory\", \"Validity and
Reliability\").""", json_schema_extra = { "linkml_meta": {'domain_of': ['PlaybookEntry']} })


class PlaybookCollection(ConfiguredBaseModel):
    """
    A container for a set of PlaybookEntry instances - the
    serialisation root for an AI RMF Playbook companion document.
    Validate with ``linkml-validate --target-class PlaybookCollection``;
    the canonical tree-root for the schema is ``AiRmfFramework``.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/nist-ai-100-1',
         'in_subset': ['playbook']})

    entries: Optional[list[PlaybookEntry]] = Field(default=None, description="""The Playbook entries in a `PlaybookCollection`.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PlaybookCollection'], 'in_subset': ['playbook']} })


class AiRmfDocument(NamedThingRMF):
    """
    Publication metadata for an instance of the AI RMF (e.g., NIST
    AI 100-1, January 2023). The Framework is intended to be a
    living document, employing a two-number versioning system (major.minor).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'close_mappings': ['nist_csf:CSFMetadata'],
         'from_schema': 'https://w3id.org/lmodel/nist-ai-100-1',
         'in_subset': ['base'],
         'related_mappings': ['schema:CreativeWork']})

    version: Optional[str] = Field(default=None, description="""Version identifier of the document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiRmfDocument'],
         'in_subset': ['base'],
         'slot_uri': 'schema:version'} })
    publisher: Optional[str] = Field(default=None, description="""The publisher of the document (e.g., NIST).""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiRmfDocument'],
         'in_subset': ['base'],
         'slot_uri': 'dcterms:publisher'} })
    doi: Optional[str] = Field(default=None, description="""Digital Object Identifier for the document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiRmfDocument'], 'in_subset': ['base']} })
    published_date: Optional[date] = Field(default=None, description="""Date the document was published.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiRmfDocument'],
         'in_subset': ['base'],
         'slot_uri': 'dcterms:issued'} })
    source: Optional[str] = Field(default=None, description="""Reference to the source of the element (typically the document
or section it originated from).""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiRmfDocument'],
         'in_subset': ['base'],
         'slot_uri': 'dcterms:source'} })
    id: str = Field(default=..., description="""A unique identifier for an element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThingRMF'],
         'in_subset': ['base'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A short human-readable name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThingRMF'],
         'in_subset': ['base'],
         'slot_uri': 'rdfs:label'} })
    title: Optional[str] = Field(default=None, description="""A human-readable title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThingRMF', 'PlaybookEntry'],
         'in_subset': ['base'],
         'slot_uri': 'dcterms:title'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThingRMF', 'PlaybookEntry'],
         'in_subset': ['base'],
         'slot_uri': 'dcterms:description'} })
    see_also: Optional[list[str]] = Field(default=None, description="""Related references.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThingRMF'],
         'in_subset': ['base'],
         'slot_uri': 'rdfs:seeAlso'} })


class AiRmfFramework(NamedThingRMF):
    """
    Root container that bundles the AI RMF Core (Functions) with
    foundational concepts (trustworthiness characteristics,
    lifecycle, actors, risks, harms), profiles, and Framework
    attributes. Designed for serialising the Framework or a tailored
    instance of it as a single JSON / YAML document.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'close_mappings': ['nist_csf:CSFDocument',
                            'oscal_catalog:Catalog',
                            'nist_sp_800_53:Catalog'],
         'from_schema': 'https://w3id.org/lmodel/nist-ai-100-1',
         'in_subset': ['base'],
         'tree_root': True})

    document: Optional[AiRmfDocument] = Field(default=None, description="""Publication metadata of the framework instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiRmfFramework'], 'in_subset': ['base']} })
    functions: Optional[list[Function]] = Field(default=None, description="""The four AI RMF Core functions and their content.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiRmfFramework'], 'in_subset': ['framework_core']} })
    trustworthiness_characteristics: Optional[list[TrustworthinessCharacteristic]] = Field(default=None, description="""The seven characteristics of trustworthy AI.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiRmfFramework'], 'in_subset': ['trustworthiness']} })
    lifecycle_stages: Optional[list[AiLifecycleStage]] = Field(default=None, description="""The AI lifecycle stages (Figure 2).""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiRmfFramework'], 'in_subset': ['lifecycle']} })
    dimensions: Optional[list[AiSystemDimension]] = Field(default=None, description="""The AI system dimensions (Figure 2).""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiRmfFramework'], 'in_subset': ['lifecycle']} })
    actor_tasks: Optional[list[AiActorTask]] = Field(default=None, description="""AI actor task categories (Appendix A).""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiRmfFramework'], 'in_subset': ['lifecycle']} })
    profiles: Optional[list[AiRmfProfile]] = Field(default=None, description="""AI RMF profiles defined alongside this Framework instance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiRmfFramework'], 'in_subset': ['profiles']} })
    attributes_: Optional[list[RmfAttribute]] = Field(default=None, description="""Design attributes of the AI RMF (Appendix D).""", json_schema_extra = { "linkml_meta": {'aliases': ['rmf_attributes'],
         'domain_of': ['AiRmfFramework'],
         'in_subset': ['attributes'],
         'slot_uri': 'nist_ai_100_1:attributes'} })
    risk_measurement_challenges: Optional[list[RiskMeasurementChallenge]] = Field(default=None, description="""Identified challenges in measuring AI risk.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiRmfFramework'], 'in_subset': ['risk_and_harm']} })
    ai_specific_risks: Optional[list[AiSpecificRisk]] = Field(default=None, description="""AI-specific risks compared to traditional software (Appendix B).""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiRmfFramework'], 'in_subset': ['ai_risk_distinctions']} })
    human_ai_interaction_issues: Optional[list[HumanAiInteractionIssue]] = Field(default=None, description="""Human-AI interaction considerations (Appendix C).""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiRmfFramework'], 'in_subset': ['human_ai_interaction']} })
    id: str = Field(default=..., description="""A unique identifier for an element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThingRMF'],
         'in_subset': ['base'],
         'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A short human-readable name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThingRMF'],
         'in_subset': ['base'],
         'slot_uri': 'rdfs:label'} })
    title: Optional[str] = Field(default=None, description="""A human-readable title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThingRMF', 'PlaybookEntry'],
         'in_subset': ['base'],
         'slot_uri': 'dcterms:title'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThingRMF', 'PlaybookEntry'],
         'in_subset': ['base'],
         'slot_uri': 'dcterms:description'} })
    see_also: Optional[list[str]] = Field(default=None, description="""Related references.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThingRMF'],
         'in_subset': ['base'],
         'slot_uri': 'rdfs:seeAlso'} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
NamedThingRMF.model_rebuild()
AiSystem.model_rebuild()
AiSystemDimension.model_rebuild()
AiLifecycleStage.model_rebuild()
AiActor.model_rebuild()
AiActorTask.model_rebuild()
Risk.model_rebuild()
Impact.model_rebuild()
Harm.model_rebuild()
ResidualRisk.model_rebuild()
RiskTolerance.model_rebuild()
RiskMeasurementChallenge.model_rebuild()
TrustworthinessCharacteristic.model_rebuild()
Bias.model_rebuild()
Function.model_rebuild()
Category.model_rebuild()
Subcategory.model_rebuild()
AiRmfProfile.model_rebuild()
RmfAttribute.model_rebuild()
AiSpecificRisk.model_rebuild()
HumanAiInteractionIssue.model_rebuild()
PlaybookEntry.model_rebuild()
PlaybookCollection.model_rebuild()
AiRmfDocument.model_rebuild()
AiRmfFramework.model_rebuild()
