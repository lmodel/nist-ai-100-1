# Auto generated from nist_ai_100_1.yaml by pythongen.py version: 0.0.1
# Schema: nist_ai_100_1
#
# id: https://w3id.org/lmodel/nist-ai-100-1
# description: A LinkML model of the Artificial Intelligence Risk Management Framework (AI RMF 1.0), which NIST publishes as NIST AI 100-1: the Core's functions, categories and subcategories with their Playbook material, the framing of risk and harm, the trustworthiness characteristics, the lifecycle and AI actors, profiles and the lists of the appendices.
# license: Apache-2.0

import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from linkml_runtime.linkml_model.types import Boolean, Integer, String, Uri, Uriorcurie
from linkml_runtime.utils.metamodelcore import Bool, URI, URIorCURIE

metamodel_version = "1.12.0"
version = "1.0.0"

# Namespaces
ISO27001 = CurieNamespace('iso27001', 'https://w3id.org/lmodel/iso27001/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
NIST_AI_100_1 = CurieNamespace('nist_ai_100_1', 'https://w3id.org/lmodel/nist-ai-100-1/')
NIST_CSF_V2 = CurieNamespace('nist_csf_v2', 'https://w3id.org/lmodel/nist-csf-v2/')
OSCAL = CurieNamespace('oscal', 'https://w3id.org/lmodel/oscal/')
PROV = CurieNamespace('prov', 'http://www.w3.org/ns/prov#')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = NIST_AI_100_1


# Types
class AiRmfFunctionIdentifier(String):
    """ The name of one of the four Core functions, written in capitals, such as GOVERN. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "ai_rmf_function_identifier"
    type_model_uri = NIST_AI_100_1.AiRmfFunctionIdentifier


class AiRmfCategoryIdentifier(String):
    """ A category's identifier, its function's name and a number, such as GOVERN 1. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "ai_rmf_category_identifier"
    type_model_uri = NIST_AI_100_1.AiRmfCategoryIdentifier


class AiRmfSubcategoryIdentifier(String):
    """ A subcategory's identifier, its category's identifier, a dot and a number, such as GOVERN 1.1. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "ai_rmf_subcategory_identifier"
    type_model_uri = NIST_AI_100_1.AiRmfSubcategoryIdentifier


class AiRmfSuggestedActionIdentifier(String):
    """ The identifier NIST's catalog gives a Playbook suggested action, such as SA-GOVERN_1.1-1. Each further number, as in SA-GOVERN_1.4-1.2, marks a sub-item. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "ai_rmf_suggested_action_identifier"
    type_model_uri = NIST_AI_100_1.AiRmfSuggestedActionIdentifier


class AiRmfDocumentationIdentifier(String):
    """ The identifier NIST's catalog gives a Playbook documentation prompt, such as D-GOVERN_1.1-1. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "ai_rmf_documentation_identifier"
    type_model_uri = NIST_AI_100_1.AiRmfDocumentationIdentifier


# Class references
class AiRmfRecordAiRmfId(URIorCURIE):
    pass


class AiRmfSystemAiRmfId(AiRmfRecordAiRmfId):
    pass


class AiRmfActorAiRmfId(AiRmfRecordAiRmfId):
    pass


class AiRmfRiskAiRmfId(AiRmfRecordAiRmfId):
    pass


class AiRmfResidualRiskAiRmfId(AiRmfRiskAiRmfId):
    pass


class AiRmfImpactAiRmfId(AiRmfRecordAiRmfId):
    pass


class AiRmfHarmAiRmfId(AiRmfImpactAiRmfId):
    pass


class AiRmfRiskToleranceAiRmfId(AiRmfRecordAiRmfId):
    pass


class AiRmfBiasAiRmfId(AiRmfRecordAiRmfId):
    pass


class AiRmfProfileAiRmfId(AiRmfRecordAiRmfId):
    pass


@dataclass(repr=False)
class AiRmfFramework(YAMLRoot):
    """
    One edition of the AI RMF as a whole, with the Core and the lists the publication gives.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_AI_100_1["Framework"]
    class_class_curie: ClassVar[str] = "nist_ai_100_1:Framework"
    class_name: ClassVar[str] = "AiRmfFramework"
    class_model_uri: ClassVar[URIRef] = NIST_AI_100_1.AiRmfFramework

    ai_rmf_version: str = None
    ai_rmf_functions: Union[Union[dict, "AiRmfFunction"], list[Union[dict, "AiRmfFunction"]]] = None
    ai_rmf_characteristics: Optional[Union[Union[dict, "AiRmfTrustworthinessCharacteristic"], list[Union[dict, "AiRmfTrustworthinessCharacteristic"]]]] = empty_list()
    ai_rmf_dimensions: Optional[Union[Union[dict, "AiRmfDimension"], list[Union[dict, "AiRmfDimension"]]]] = empty_list()
    ai_rmf_lifecycle_stages: Optional[Union[Union[dict, "AiRmfLifecycleStage"], list[Union[dict, "AiRmfLifecycleStage"]]]] = empty_list()
    ai_rmf_actor_task_list: Optional[Union[Union[dict, "AiRmfActorTask"], list[Union[dict, "AiRmfActorTask"]]]] = empty_list()
    ai_rmf_management_challenges: Optional[Union[Union[dict, "AiRmfManagementChallenge"], list[Union[dict, "AiRmfManagementChallenge"]]]] = empty_list()
    ai_rmf_specific_risks: Optional[Union[Union[dict, "AiRmfSpecificRisk"], list[Union[dict, "AiRmfSpecificRisk"]]]] = empty_list()
    ai_rmf_human_ai_issues: Optional[Union[Union[dict, "AiRmfHumanAiIssue"], list[Union[dict, "AiRmfHumanAiIssue"]]]] = empty_list()
    ai_rmf_attributes: Optional[Union[Union[dict, "AiRmfAttribute"], list[Union[dict, "AiRmfAttribute"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.ai_rmf_version):
            self.MissingRequiredField("ai_rmf_version")
        if not isinstance(self.ai_rmf_version, str):
            self.ai_rmf_version = str(self.ai_rmf_version)

        if self._is_empty(self.ai_rmf_functions):
            self.MissingRequiredField("ai_rmf_functions")
        self._normalize_inlined_as_list(slot_name="ai_rmf_functions", slot_type=AiRmfFunction, key_name="ai_rmf_function_id", keyed=False)

        self._normalize_inlined_as_list(slot_name="ai_rmf_characteristics", slot_type=AiRmfTrustworthinessCharacteristic, key_name="ai_rmf_characteristic_name", keyed=False)

        self._normalize_inlined_as_list(slot_name="ai_rmf_dimensions", slot_type=AiRmfDimension, key_name="ai_rmf_dimension_name", keyed=False)

        self._normalize_inlined_as_list(slot_name="ai_rmf_lifecycle_stages", slot_type=AiRmfLifecycleStage, key_name="ai_rmf_lifecycle_stage_name", keyed=False)

        self._normalize_inlined_as_list(slot_name="ai_rmf_actor_task_list", slot_type=AiRmfActorTask, key_name="ai_rmf_actor_task_name", keyed=False)

        self._normalize_inlined_as_list(slot_name="ai_rmf_management_challenges", slot_type=AiRmfManagementChallenge, key_name="ai_rmf_management_challenge_name", keyed=False)

        self._normalize_inlined_as_list(slot_name="ai_rmf_specific_risks", slot_type=AiRmfSpecificRisk, key_name="title", keyed=False)

        self._normalize_inlined_as_list(slot_name="ai_rmf_human_ai_issues", slot_type=AiRmfHumanAiIssue, key_name="title", keyed=False)

        self._normalize_inlined_as_list(slot_name="ai_rmf_attributes", slot_type=AiRmfAttribute, key_name="title", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AiRmfRecord(YAMLRoot):
    """
    The base of the classes that record an adopter's own facts, such as one of its AI systems or risks, as distinct
    from what the publication itself lists.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_AI_100_1["Record"]
    class_class_curie: ClassVar[str] = "nist_ai_100_1:Record"
    class_name: ClassVar[str] = "AiRmfRecord"
    class_model_uri: ClassVar[URIRef] = NIST_AI_100_1.AiRmfRecord

    ai_rmf_id: Union[str, AiRmfRecordAiRmfId] = None
    title: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.ai_rmf_id):
            self.MissingRequiredField("ai_rmf_id")
        if not isinstance(self.ai_rmf_id, AiRmfRecordAiRmfId):
            self.ai_rmf_id = AiRmfRecordAiRmfId(self.ai_rmf_id)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AiRmfTrustworthinessCharacteristic(YAMLRoot):
    """
    A characteristic of trustworthy AI systems, each with a subsection of section 3.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_AI_100_1["TrustworthinessCharacteristic"]
    class_class_curie: ClassVar[str] = "nist_ai_100_1:TrustworthinessCharacteristic"
    class_name: ClassVar[str] = "AiRmfTrustworthinessCharacteristic"
    class_model_uri: ClassVar[URIRef] = NIST_AI_100_1.AiRmfTrustworthinessCharacteristic

    ai_rmf_characteristic_name: Union[str, "AiRmfCharacteristicName"] = None
    ai_rmf_characteristic_section: str = None
    description: Optional[str] = None
    ai_rmf_characteristic_is_base: Optional[Union[bool, Bool]] = None
    ai_rmf_characteristic_relates_to_all: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.ai_rmf_characteristic_name):
            self.MissingRequiredField("ai_rmf_characteristic_name")
        if not isinstance(self.ai_rmf_characteristic_name, AiRmfCharacteristicName):
            self.ai_rmf_characteristic_name = AiRmfCharacteristicName(self.ai_rmf_characteristic_name)

        if self._is_empty(self.ai_rmf_characteristic_section):
            self.MissingRequiredField("ai_rmf_characteristic_section")
        if not isinstance(self.ai_rmf_characteristic_section, str):
            self.ai_rmf_characteristic_section = str(self.ai_rmf_characteristic_section)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.ai_rmf_characteristic_is_base is not None and not isinstance(self.ai_rmf_characteristic_is_base, Bool):
            self.ai_rmf_characteristic_is_base = Bool(self.ai_rmf_characteristic_is_base)

        if self.ai_rmf_characteristic_relates_to_all is not None and not isinstance(self.ai_rmf_characteristic_relates_to_all, Bool):
            self.ai_rmf_characteristic_relates_to_all = Bool(self.ai_rmf_characteristic_relates_to_all)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AiRmfDimension(YAMLRoot):
    """
    One of the five key socio-technical dimensions of an AI system in Figure 2.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_AI_100_1["Dimension"]
    class_class_curie: ClassVar[str] = "nist_ai_100_1:Dimension"
    class_name: ClassVar[str] = "AiRmfDimension"
    class_model_uri: ClassVar[URIRef] = NIST_AI_100_1.AiRmfDimension

    ai_rmf_dimension_name: Union[str, "AiRmfDimensionName"] = None
    ai_rmf_dimension_audience: Union[str, "AiRmfAudience"] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.ai_rmf_dimension_name):
            self.MissingRequiredField("ai_rmf_dimension_name")
        if not isinstance(self.ai_rmf_dimension_name, AiRmfDimensionName):
            self.ai_rmf_dimension_name = AiRmfDimensionName(self.ai_rmf_dimension_name)

        if self._is_empty(self.ai_rmf_dimension_audience):
            self.MissingRequiredField("ai_rmf_dimension_audience")
        if not isinstance(self.ai_rmf_dimension_audience, AiRmfAudience):
            self.ai_rmf_dimension_audience = AiRmfAudience(self.ai_rmf_dimension_audience)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AiRmfLifecycleStage(YAMLRoot):
    """
    A stage of the AI lifecycle as a column of Figure 3 shows it, under its dimension.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_AI_100_1["LifecycleStage"]
    class_class_curie: ClassVar[str] = "nist_ai_100_1:LifecycleStage"
    class_name: ClassVar[str] = "AiRmfLifecycleStage"
    class_model_uri: ClassVar[URIRef] = NIST_AI_100_1.AiRmfLifecycleStage

    ai_rmf_lifecycle_stage_name: Union[str, "AiRmfLifecycleStageName"] = None
    ai_rmf_lifecycle_stage_dimension: Union[str, "AiRmfDimensionName"] = None
    description: Optional[str] = None
    ai_rmf_lifecycle_stage_tevv: Optional[str] = None
    ai_rmf_lifecycle_stage_representative_actors: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.ai_rmf_lifecycle_stage_name):
            self.MissingRequiredField("ai_rmf_lifecycle_stage_name")
        if not isinstance(self.ai_rmf_lifecycle_stage_name, AiRmfLifecycleStageName):
            self.ai_rmf_lifecycle_stage_name = AiRmfLifecycleStageName(self.ai_rmf_lifecycle_stage_name)

        if self._is_empty(self.ai_rmf_lifecycle_stage_dimension):
            self.MissingRequiredField("ai_rmf_lifecycle_stage_dimension")
        if not isinstance(self.ai_rmf_lifecycle_stage_dimension, AiRmfDimensionName):
            self.ai_rmf_lifecycle_stage_dimension = AiRmfDimensionName(self.ai_rmf_lifecycle_stage_dimension)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.ai_rmf_lifecycle_stage_tevv is not None and not isinstance(self.ai_rmf_lifecycle_stage_tevv, str):
            self.ai_rmf_lifecycle_stage_tevv = str(self.ai_rmf_lifecycle_stage_tevv)

        if not isinstance(self.ai_rmf_lifecycle_stage_representative_actors, list):
            self.ai_rmf_lifecycle_stage_representative_actors = [self.ai_rmf_lifecycle_stage_representative_actors] if self.ai_rmf_lifecycle_stage_representative_actors is not None else []
        self.ai_rmf_lifecycle_stage_representative_actors = [v if isinstance(v, str) else str(v) for v in self.ai_rmf_lifecycle_stage_representative_actors]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AiRmfActorTask(YAMLRoot):
    """
    A task or additional AI actor of Appendix A.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_AI_100_1["ActorTask"]
    class_class_curie: ClassVar[str] = "nist_ai_100_1:ActorTask"
    class_name: ClassVar[str] = "AiRmfActorTask"
    class_model_uri: ClassVar[URIRef] = NIST_AI_100_1.AiRmfActorTask

    ai_rmf_actor_task_name: Union[str, "AiRmfActorTaskName"] = None
    description: Optional[str] = None
    ai_rmf_actor_task_is_additional_actor: Optional[Union[bool, Bool]] = None
    ai_rmf_actor_task_representative_actors: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.ai_rmf_actor_task_name):
            self.MissingRequiredField("ai_rmf_actor_task_name")
        if not isinstance(self.ai_rmf_actor_task_name, AiRmfActorTaskName):
            self.ai_rmf_actor_task_name = AiRmfActorTaskName(self.ai_rmf_actor_task_name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.ai_rmf_actor_task_is_additional_actor is not None and not isinstance(self.ai_rmf_actor_task_is_additional_actor, Bool):
            self.ai_rmf_actor_task_is_additional_actor = Bool(self.ai_rmf_actor_task_is_additional_actor)

        if not isinstance(self.ai_rmf_actor_task_representative_actors, list):
            self.ai_rmf_actor_task_representative_actors = [self.ai_rmf_actor_task_representative_actors] if self.ai_rmf_actor_task_representative_actors is not None else []
        self.ai_rmf_actor_task_representative_actors = [v if isinstance(v, str) else str(v) for v in self.ai_rmf_actor_task_representative_actors]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AiRmfManagementChallenge(YAMLRoot):
    """
    One of the four challenges for AI risk management in section 1.2.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_AI_100_1["ManagementChallenge"]
    class_class_curie: ClassVar[str] = "nist_ai_100_1:ManagementChallenge"
    class_name: ClassVar[str] = "AiRmfManagementChallenge"
    class_model_uri: ClassVar[URIRef] = NIST_AI_100_1.AiRmfManagementChallenge

    ai_rmf_management_challenge_name: Union[str, "AiRmfManagementChallengeName"] = None
    description: Optional[str] = None
    ai_rmf_management_challenge_measurement_challenges: Optional[Union[Union[dict, "AiRmfMeasurementChallenge"], list[Union[dict, "AiRmfMeasurementChallenge"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.ai_rmf_management_challenge_name):
            self.MissingRequiredField("ai_rmf_management_challenge_name")
        if not isinstance(self.ai_rmf_management_challenge_name, AiRmfManagementChallengeName):
            self.ai_rmf_management_challenge_name = AiRmfManagementChallengeName(self.ai_rmf_management_challenge_name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        self._normalize_inlined_as_list(slot_name="ai_rmf_management_challenge_measurement_challenges", slot_type=AiRmfMeasurementChallenge, key_name="ai_rmf_measurement_challenge_name", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AiRmfMeasurementChallenge(YAMLRoot):
    """
    One of the challenges of measuring AI risk in section 1.2.1.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_AI_100_1["MeasurementChallenge"]
    class_class_curie: ClassVar[str] = "nist_ai_100_1:MeasurementChallenge"
    class_name: ClassVar[str] = "AiRmfMeasurementChallenge"
    class_model_uri: ClassVar[URIRef] = NIST_AI_100_1.AiRmfMeasurementChallenge

    ai_rmf_measurement_challenge_name: Union[str, "AiRmfMeasurementChallengeName"] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.ai_rmf_measurement_challenge_name):
            self.MissingRequiredField("ai_rmf_measurement_challenge_name")
        if not isinstance(self.ai_rmf_measurement_challenge_name, AiRmfMeasurementChallengeName):
            self.ai_rmf_measurement_challenge_name = AiRmfMeasurementChallengeName(self.ai_rmf_measurement_challenge_name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AiRmfSpecificRisk(YAMLRoot):
    """
    A risk that Appendix B says is new or increased for AI compared with traditional software.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_AI_100_1["SpecificRisk"]
    class_class_curie: ClassVar[str] = "nist_ai_100_1:SpecificRisk"
    class_name: ClassVar[str] = "AiRmfSpecificRisk"
    class_model_uri: ClassVar[URIRef] = NIST_AI_100_1.AiRmfSpecificRisk

    title: str = None
    ai_rmf_specific_risk_position: int = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self._is_empty(self.ai_rmf_specific_risk_position):
            self.MissingRequiredField("ai_rmf_specific_risk_position")
        if not isinstance(self.ai_rmf_specific_risk_position, int):
            self.ai_rmf_specific_risk_position = int(self.ai_rmf_specific_risk_position)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AiRmfHumanAiIssue(YAMLRoot):
    """
    An issue of human-AI interaction that Appendix C says merits further consideration and research.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_AI_100_1["HumanAiIssue"]
    class_class_curie: ClassVar[str] = "nist_ai_100_1:HumanAiIssue"
    class_name: ClassVar[str] = "AiRmfHumanAiIssue"
    class_model_uri: ClassVar[URIRef] = NIST_AI_100_1.AiRmfHumanAiIssue

    title: str = None
    ai_rmf_human_ai_issue_number: int = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self._is_empty(self.ai_rmf_human_ai_issue_number):
            self.MissingRequiredField("ai_rmf_human_ai_issue_number")
        if not isinstance(self.ai_rmf_human_ai_issue_number, int):
            self.ai_rmf_human_ai_issue_number = int(self.ai_rmf_human_ai_issue_number)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AiRmfAttribute(YAMLRoot):
    """
    A key attribute of the AI RMF in Appendix D, which guided its development.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_AI_100_1["Attribute"]
    class_class_curie: ClassVar[str] = "nist_ai_100_1:Attribute"
    class_name: ClassVar[str] = "AiRmfAttribute"
    class_model_uri: ClassVar[URIRef] = NIST_AI_100_1.AiRmfAttribute

    title: str = None
    ai_rmf_attribute_number: int = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self._is_empty(self.ai_rmf_attribute_number):
            self.MissingRequiredField("ai_rmf_attribute_number")
        if not isinstance(self.ai_rmf_attribute_number, int):
            self.ai_rmf_attribute_number = int(self.ai_rmf_attribute_number)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AiRmfSystem(AiRmfRecord):
    """
    A machine-based system that produces outputs such as predictions or decisions for given objectives, with varying
    autonomy.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_AI_100_1["AiSystem"]
    class_class_curie: ClassVar[str] = "nist_ai_100_1:AiSystem"
    class_name: ClassVar[str] = "AiRmfSystem"
    class_model_uri: ClassVar[URIRef] = NIST_AI_100_1.AiRmfSystem

    ai_rmf_id: Union[str, AiRmfSystemAiRmfId] = None
    ai_rmf_system_lifecycle_stages: Optional[Union[Union[str, "AiRmfLifecycleStageName"], list[Union[str, "AiRmfLifecycleStageName"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.ai_rmf_id):
            self.MissingRequiredField("ai_rmf_id")
        if not isinstance(self.ai_rmf_id, AiRmfSystemAiRmfId):
            self.ai_rmf_id = AiRmfSystemAiRmfId(self.ai_rmf_id)

        if not isinstance(self.ai_rmf_system_lifecycle_stages, list):
            self.ai_rmf_system_lifecycle_stages = [self.ai_rmf_system_lifecycle_stages] if self.ai_rmf_system_lifecycle_stages is not None else []
        self.ai_rmf_system_lifecycle_stages = [v if isinstance(v, AiRmfLifecycleStageName) else AiRmfLifecycleStageName(v) for v in self.ai_rmf_system_lifecycle_stages]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AiRmfActor(AiRmfRecord):
    """
    An organization or individual with an active role in an AI system's lifecycle.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_AI_100_1["AiActor"]
    class_class_curie: ClassVar[str] = "nist_ai_100_1:AiActor"
    class_name: ClassVar[str] = "AiRmfActor"
    class_model_uri: ClassVar[URIRef] = NIST_AI_100_1.AiRmfActor

    ai_rmf_id: Union[str, AiRmfActorAiRmfId] = None
    ai_rmf_actor_tasks: Optional[Union[Union[str, "AiRmfActorTaskName"], list[Union[str, "AiRmfActorTaskName"]]]] = empty_list()
    ai_rmf_actor_audience: Optional[Union[str, "AiRmfAudience"]] = None
    ai_rmf_actor_lifecycle_stages: Optional[Union[Union[str, "AiRmfLifecycleStageName"], list[Union[str, "AiRmfLifecycleStageName"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.ai_rmf_id):
            self.MissingRequiredField("ai_rmf_id")
        if not isinstance(self.ai_rmf_id, AiRmfActorAiRmfId):
            self.ai_rmf_id = AiRmfActorAiRmfId(self.ai_rmf_id)

        if not isinstance(self.ai_rmf_actor_tasks, list):
            self.ai_rmf_actor_tasks = [self.ai_rmf_actor_tasks] if self.ai_rmf_actor_tasks is not None else []
        self.ai_rmf_actor_tasks = [v if isinstance(v, AiRmfActorTaskName) else AiRmfActorTaskName(v) for v in self.ai_rmf_actor_tasks]

        if self.ai_rmf_actor_audience is not None and not isinstance(self.ai_rmf_actor_audience, AiRmfAudience):
            self.ai_rmf_actor_audience = AiRmfAudience(self.ai_rmf_actor_audience)

        if not isinstance(self.ai_rmf_actor_lifecycle_stages, list):
            self.ai_rmf_actor_lifecycle_stages = [self.ai_rmf_actor_lifecycle_stages] if self.ai_rmf_actor_lifecycle_stages is not None else []
        self.ai_rmf_actor_lifecycle_stages = [v if isinstance(v, AiRmfLifecycleStageName) else AiRmfLifecycleStageName(v) for v in self.ai_rmf_actor_lifecycle_stages]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AiRmfRisk(AiRmfRecord):
    """
    How likely an event is, combined with how severe its consequences are.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_AI_100_1["Risk"]
    class_class_curie: ClassVar[str] = "nist_ai_100_1:Risk"
    class_name: ClassVar[str] = "AiRmfRisk"
    class_model_uri: ClassVar[URIRef] = NIST_AI_100_1.AiRmfRisk

    ai_rmf_id: Union[str, AiRmfRiskAiRmfId] = None
    ai_rmf_likelihood: Optional[str] = None
    ai_rmf_magnitude: Optional[str] = None
    ai_rmf_risk_system: Optional[Union[str, AiRmfSystemAiRmfId]] = None
    ai_rmf_risk_impacts: Optional[Union[dict[Union[str, AiRmfImpactAiRmfId], Union[dict, "AiRmfImpact"]], list[Union[dict, "AiRmfImpact"]]]] = empty_dict()
    ai_rmf_risk_characteristics: Optional[Union[Union[str, "AiRmfCharacteristicName"], list[Union[str, "AiRmfCharacteristicName"]]]] = empty_list()
    ai_rmf_risk_lifecycle_stages: Optional[Union[Union[str, "AiRmfLifecycleStageName"], list[Union[str, "AiRmfLifecycleStageName"]]]] = empty_list()
    ai_rmf_risk_responses: Optional[Union[Union[str, "AiRmfRiskResponse"], list[Union[str, "AiRmfRiskResponse"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.ai_rmf_id):
            self.MissingRequiredField("ai_rmf_id")
        if not isinstance(self.ai_rmf_id, AiRmfRiskAiRmfId):
            self.ai_rmf_id = AiRmfRiskAiRmfId(self.ai_rmf_id)

        if self.ai_rmf_likelihood is not None and not isinstance(self.ai_rmf_likelihood, str):
            self.ai_rmf_likelihood = str(self.ai_rmf_likelihood)

        if self.ai_rmf_magnitude is not None and not isinstance(self.ai_rmf_magnitude, str):
            self.ai_rmf_magnitude = str(self.ai_rmf_magnitude)

        if self.ai_rmf_risk_system is not None and not isinstance(self.ai_rmf_risk_system, AiRmfSystemAiRmfId):
            self.ai_rmf_risk_system = AiRmfSystemAiRmfId(self.ai_rmf_risk_system)

        self._normalize_inlined_as_list(slot_name="ai_rmf_risk_impacts", slot_type=AiRmfImpact, key_name="ai_rmf_id", keyed=True)

        if not isinstance(self.ai_rmf_risk_characteristics, list):
            self.ai_rmf_risk_characteristics = [self.ai_rmf_risk_characteristics] if self.ai_rmf_risk_characteristics is not None else []
        self.ai_rmf_risk_characteristics = [v if isinstance(v, AiRmfCharacteristicName) else AiRmfCharacteristicName(v) for v in self.ai_rmf_risk_characteristics]

        if not isinstance(self.ai_rmf_risk_lifecycle_stages, list):
            self.ai_rmf_risk_lifecycle_stages = [self.ai_rmf_risk_lifecycle_stages] if self.ai_rmf_risk_lifecycle_stages is not None else []
        self.ai_rmf_risk_lifecycle_stages = [v if isinstance(v, AiRmfLifecycleStageName) else AiRmfLifecycleStageName(v) for v in self.ai_rmf_risk_lifecycle_stages]

        if not isinstance(self.ai_rmf_risk_responses, list):
            self.ai_rmf_risk_responses = [self.ai_rmf_risk_responses] if self.ai_rmf_risk_responses is not None else []
        self.ai_rmf_risk_responses = [v if isinstance(v, AiRmfRiskResponse) else AiRmfRiskResponse(v) for v in self.ai_rmf_risk_responses]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AiRmfResidualRisk(AiRmfRisk):
    """
    The risk that remains after risk treatment.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_AI_100_1["ResidualRisk"]
    class_class_curie: ClassVar[str] = "nist_ai_100_1:ResidualRisk"
    class_name: ClassVar[str] = "AiRmfResidualRisk"
    class_model_uri: ClassVar[URIRef] = NIST_AI_100_1.AiRmfResidualRisk

    ai_rmf_id: Union[str, AiRmfResidualRiskAiRmfId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.ai_rmf_id):
            self.MissingRequiredField("ai_rmf_id")
        if not isinstance(self.ai_rmf_id, AiRmfResidualRiskAiRmfId):
            self.ai_rmf_id = AiRmfResidualRiskAiRmfId(self.ai_rmf_id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AiRmfImpact(AiRmfRecord):
    """
    A consequence of an AI system, which may be an opportunity, a threat or both.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_AI_100_1["Impact"]
    class_class_curie: ClassVar[str] = "nist_ai_100_1:Impact"
    class_name: ClassVar[str] = "AiRmfImpact"
    class_model_uri: ClassVar[URIRef] = NIST_AI_100_1.AiRmfImpact

    ai_rmf_id: Union[str, AiRmfImpactAiRmfId] = None
    ai_rmf_impact_direction: Union[str, "AiRmfImpactDirection"] = None
    ai_rmf_likelihood: Optional[str] = None
    ai_rmf_magnitude: Optional[str] = None
    ai_rmf_impact_affected_parties: Optional[Union[Union[str, "AiRmfAffectedParty"], list[Union[str, "AiRmfAffectedParty"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.ai_rmf_id):
            self.MissingRequiredField("ai_rmf_id")
        if not isinstance(self.ai_rmf_id, AiRmfImpactAiRmfId):
            self.ai_rmf_id = AiRmfImpactAiRmfId(self.ai_rmf_id)

        if self._is_empty(self.ai_rmf_impact_direction):
            self.MissingRequiredField("ai_rmf_impact_direction")
        if not isinstance(self.ai_rmf_impact_direction, AiRmfImpactDirection):
            self.ai_rmf_impact_direction = AiRmfImpactDirection(self.ai_rmf_impact_direction)

        if self.ai_rmf_likelihood is not None and not isinstance(self.ai_rmf_likelihood, str):
            self.ai_rmf_likelihood = str(self.ai_rmf_likelihood)

        if self.ai_rmf_magnitude is not None and not isinstance(self.ai_rmf_magnitude, str):
            self.ai_rmf_magnitude = str(self.ai_rmf_magnitude)

        if not isinstance(self.ai_rmf_impact_affected_parties, list):
            self.ai_rmf_impact_affected_parties = [self.ai_rmf_impact_affected_parties] if self.ai_rmf_impact_affected_parties is not None else []
        self.ai_rmf_impact_affected_parties = [v if isinstance(v, AiRmfAffectedParty) else AiRmfAffectedParty(v) for v in self.ai_rmf_impact_affected_parties]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AiRmfHarm(AiRmfImpact):
    """
    A negative impact, sorted as in Figure 1 by whether it falls on people, an organization or an ecosystem.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_AI_100_1["Harm"]
    class_class_curie: ClassVar[str] = "nist_ai_100_1:Harm"
    class_name: ClassVar[str] = "AiRmfHarm"
    class_model_uri: ClassVar[URIRef] = NIST_AI_100_1.AiRmfHarm

    ai_rmf_id: Union[str, AiRmfHarmAiRmfId] = None
    ai_rmf_impact_direction: Union[str, "AiRmfImpactDirection"] = None
    ai_rmf_harm_category: Union[str, "AiRmfHarmCategory"] = None
    ai_rmf_harm_example: Optional[Union[str, "AiRmfHarmExample"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.ai_rmf_id):
            self.MissingRequiredField("ai_rmf_id")
        if not isinstance(self.ai_rmf_id, AiRmfHarmAiRmfId):
            self.ai_rmf_id = AiRmfHarmAiRmfId(self.ai_rmf_id)

        if self._is_empty(self.ai_rmf_harm_category):
            self.MissingRequiredField("ai_rmf_harm_category")
        if not isinstance(self.ai_rmf_harm_category, AiRmfHarmCategory):
            self.ai_rmf_harm_category = AiRmfHarmCategory(self.ai_rmf_harm_category)

        if self.ai_rmf_harm_example is not None and not isinstance(self.ai_rmf_harm_example, AiRmfHarmExample):
            self.ai_rmf_harm_example = AiRmfHarmExample(self.ai_rmf_harm_example)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AiRmfRiskTolerance(AiRmfRecord):
    """
    An organization's or AI actor's readiness to bear risk to achieve its objectives. The AI RMF prescribes none.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_AI_100_1["RiskTolerance"]
    class_class_curie: ClassVar[str] = "nist_ai_100_1:RiskTolerance"
    class_name: ClassVar[str] = "AiRmfRiskTolerance"
    class_model_uri: ClassVar[URIRef] = NIST_AI_100_1.AiRmfRiskTolerance

    ai_rmf_id: Union[str, AiRmfRiskToleranceAiRmfId] = None
    ai_rmf_risk_tolerance_holder: Optional[Union[str, AiRmfActorAiRmfId]] = None
    ai_rmf_risk_tolerance_influences: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.ai_rmf_id):
            self.MissingRequiredField("ai_rmf_id")
        if not isinstance(self.ai_rmf_id, AiRmfRiskToleranceAiRmfId):
            self.ai_rmf_id = AiRmfRiskToleranceAiRmfId(self.ai_rmf_id)

        if self.ai_rmf_risk_tolerance_holder is not None and not isinstance(self.ai_rmf_risk_tolerance_holder, AiRmfActorAiRmfId):
            self.ai_rmf_risk_tolerance_holder = AiRmfActorAiRmfId(self.ai_rmf_risk_tolerance_holder)

        if not isinstance(self.ai_rmf_risk_tolerance_influences, list):
            self.ai_rmf_risk_tolerance_influences = [self.ai_rmf_risk_tolerance_influences] if self.ai_rmf_risk_tolerance_influences is not None else []
        self.ai_rmf_risk_tolerance_influences = [v if isinstance(v, str) else str(v) for v in self.ai_rmf_risk_tolerance_influences]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AiRmfBias(AiRmfRecord):
    """
    A bias to consider and manage, sorted into NIST's three major categories.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_AI_100_1["Bias"]
    class_class_curie: ClassVar[str] = "nist_ai_100_1:Bias"
    class_name: ClassVar[str] = "AiRmfBias"
    class_model_uri: ClassVar[URIRef] = NIST_AI_100_1.AiRmfBias

    ai_rmf_id: Union[str, AiRmfBiasAiRmfId] = None
    ai_rmf_bias_categories: Union[Union[str, "AiRmfBiasCategory"], list[Union[str, "AiRmfBiasCategory"]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.ai_rmf_id):
            self.MissingRequiredField("ai_rmf_id")
        if not isinstance(self.ai_rmf_id, AiRmfBiasAiRmfId):
            self.ai_rmf_id = AiRmfBiasAiRmfId(self.ai_rmf_id)

        if self._is_empty(self.ai_rmf_bias_categories):
            self.MissingRequiredField("ai_rmf_bias_categories")
        if not isinstance(self.ai_rmf_bias_categories, list):
            self.ai_rmf_bias_categories = [self.ai_rmf_bias_categories] if self.ai_rmf_bias_categories is not None else []
        self.ai_rmf_bias_categories = [v if isinstance(v, AiRmfBiasCategory) else AiRmfBiasCategory(v) for v in self.ai_rmf_bias_categories]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AiRmfFunction(YAMLRoot):
    """
    One of the four functions that organize AI risk management at the highest level. GOVERN cuts across the other
    three.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_AI_100_1["Function"]
    class_class_curie: ClassVar[str] = "nist_ai_100_1:Function"
    class_name: ClassVar[str] = "AiRmfFunction"
    class_model_uri: ClassVar[URIRef] = NIST_AI_100_1.AiRmfFunction

    ai_rmf_function_id: Union[str, AiRmfFunctionIdentifier] = None
    description: Optional[str] = None
    ai_rmf_function_categories: Optional[Union[Union[dict, "AiRmfCategory"], list[Union[dict, "AiRmfCategory"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.ai_rmf_function_id):
            self.MissingRequiredField("ai_rmf_function_id")
        if not isinstance(self.ai_rmf_function_id, AiRmfFunctionIdentifier):
            self.ai_rmf_function_id = AiRmfFunctionIdentifier(self.ai_rmf_function_id)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        self._normalize_inlined_as_list(slot_name="ai_rmf_function_categories", slot_type=AiRmfCategory, key_name="ai_rmf_category_id", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AiRmfCategory(YAMLRoot):
    """
    A group of related outcomes within a function, such as GOVERN 1, which Tables 1 to 4 state.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_AI_100_1["Category"]
    class_class_curie: ClassVar[str] = "nist_ai_100_1:Category"
    class_name: ClassVar[str] = "AiRmfCategory"
    class_model_uri: ClassVar[URIRef] = NIST_AI_100_1.AiRmfCategory

    ai_rmf_category_id: Union[str, AiRmfCategoryIdentifier] = None
    description: str = None
    ai_rmf_category_subcategories: Optional[Union[Union[dict, "AiRmfSubcategory"], list[Union[dict, "AiRmfSubcategory"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.ai_rmf_category_id):
            self.MissingRequiredField("ai_rmf_category_id")
        if not isinstance(self.ai_rmf_category_id, AiRmfCategoryIdentifier):
            self.ai_rmf_category_id = AiRmfCategoryIdentifier(self.ai_rmf_category_id)

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        self._normalize_inlined_as_list(slot_name="ai_rmf_category_subcategories", slot_type=AiRmfSubcategory, key_name="ai_rmf_subcategory_id", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AiRmfSubcategory(YAMLRoot):
    """
    A specific outcome within a category, such as GOVERN 1.1, which Tables 1 to 4 state, and its Playbook material.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_AI_100_1["Subcategory"]
    class_class_curie: ClassVar[str] = "nist_ai_100_1:Subcategory"
    class_name: ClassVar[str] = "AiRmfSubcategory"
    class_model_uri: ClassVar[URIRef] = NIST_AI_100_1.AiRmfSubcategory

    ai_rmf_subcategory_id: Union[str, AiRmfSubcategoryIdentifier] = None
    description: str = None
    ai_rmf_subcategory_about: Optional[Union[str, list[str]]] = empty_list()
    ai_rmf_subcategory_suggested_actions: Optional[Union[Union[dict, "AiRmfSuggestedAction"], list[Union[dict, "AiRmfSuggestedAction"]]]] = empty_list()
    ai_rmf_subcategory_documentation: Optional[Union[Union[dict, "AiRmfDocumentationItem"], list[Union[dict, "AiRmfDocumentationItem"]]]] = empty_list()
    ai_rmf_subcategory_transparency_resources: Optional[Union[Union[dict, "AiRmfResource"], list[Union[dict, "AiRmfResource"]]]] = empty_list()
    ai_rmf_subcategory_references: Optional[Union[Union[dict, "AiRmfResource"], list[Union[dict, "AiRmfResource"]]]] = empty_list()
    ai_rmf_subcategory_ai_actors: Optional[Union[Union[str, "AiRmfActorTaskName"], list[Union[str, "AiRmfActorTaskName"]]]] = empty_list()
    ai_rmf_subcategory_topics: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.ai_rmf_subcategory_id):
            self.MissingRequiredField("ai_rmf_subcategory_id")
        if not isinstance(self.ai_rmf_subcategory_id, AiRmfSubcategoryIdentifier):
            self.ai_rmf_subcategory_id = AiRmfSubcategoryIdentifier(self.ai_rmf_subcategory_id)

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.ai_rmf_subcategory_about, list):
            self.ai_rmf_subcategory_about = [self.ai_rmf_subcategory_about] if self.ai_rmf_subcategory_about is not None else []
        self.ai_rmf_subcategory_about = [v if isinstance(v, str) else str(v) for v in self.ai_rmf_subcategory_about]

        self._normalize_inlined_as_list(slot_name="ai_rmf_subcategory_suggested_actions", slot_type=AiRmfSuggestedAction, key_name="ai_rmf_suggested_action_id", keyed=False)

        self._normalize_inlined_as_list(slot_name="ai_rmf_subcategory_documentation", slot_type=AiRmfDocumentationItem, key_name="ai_rmf_documentation_id", keyed=False)

        self._normalize_inlined_as_list(slot_name="ai_rmf_subcategory_transparency_resources", slot_type=AiRmfResource, key_name="title", keyed=False)

        self._normalize_inlined_as_list(slot_name="ai_rmf_subcategory_references", slot_type=AiRmfResource, key_name="title", keyed=False)

        if not isinstance(self.ai_rmf_subcategory_ai_actors, list):
            self.ai_rmf_subcategory_ai_actors = [self.ai_rmf_subcategory_ai_actors] if self.ai_rmf_subcategory_ai_actors is not None else []
        self.ai_rmf_subcategory_ai_actors = [v if isinstance(v, AiRmfActorTaskName) else AiRmfActorTaskName(v) for v in self.ai_rmf_subcategory_ai_actors]

        if not isinstance(self.ai_rmf_subcategory_topics, list):
            self.ai_rmf_subcategory_topics = [self.ai_rmf_subcategory_topics] if self.ai_rmf_subcategory_topics is not None else []
        self.ai_rmf_subcategory_topics = [v if isinstance(v, str) else str(v) for v in self.ai_rmf_subcategory_topics]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AiRmfSuggestedAction(YAMLRoot):
    """
    One step the Playbook suggests towards a subcategory's outcome.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_AI_100_1["SuggestedAction"]
    class_class_curie: ClassVar[str] = "nist_ai_100_1:SuggestedAction"
    class_name: ClassVar[str] = "AiRmfSuggestedAction"
    class_model_uri: ClassVar[URIRef] = NIST_AI_100_1.AiRmfSuggestedAction

    ai_rmf_suggested_action_id: Union[str, AiRmfSuggestedActionIdentifier] = None
    description: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.ai_rmf_suggested_action_id):
            self.MissingRequiredField("ai_rmf_suggested_action_id")
        if not isinstance(self.ai_rmf_suggested_action_id, AiRmfSuggestedActionIdentifier):
            self.ai_rmf_suggested_action_id = AiRmfSuggestedActionIdentifier(self.ai_rmf_suggested_action_id)

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AiRmfDocumentationItem(YAMLRoot):
    """
    One thing the Playbook suggests an organization document for a subcategory.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_AI_100_1["DocumentationItem"]
    class_class_curie: ClassVar[str] = "nist_ai_100_1:DocumentationItem"
    class_name: ClassVar[str] = "AiRmfDocumentationItem"
    class_model_uri: ClassVar[URIRef] = NIST_AI_100_1.AiRmfDocumentationItem

    ai_rmf_documentation_id: Union[str, AiRmfDocumentationIdentifier] = None
    description: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.ai_rmf_documentation_id):
            self.MissingRequiredField("ai_rmf_documentation_id")
        if not isinstance(self.ai_rmf_documentation_id, AiRmfDocumentationIdentifier):
            self.ai_rmf_documentation_id = AiRmfDocumentationIdentifier(self.ai_rmf_documentation_id)

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AiRmfResource(YAMLRoot):
    """
    A source the Playbook points to, by the title and address NIST's catalog gives it.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_AI_100_1["Resource"]
    class_class_curie: ClassVar[str] = "nist_ai_100_1:Resource"
    class_name: ClassVar[str] = "AiRmfResource"
    class_model_uri: ClassVar[URIRef] = NIST_AI_100_1.AiRmfResource

    title: str = None
    ai_rmf_resource_uuid: str = None
    ai_rmf_resource_address: Optional[Union[str, URI]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self._is_empty(self.ai_rmf_resource_uuid):
            self.MissingRequiredField("ai_rmf_resource_uuid")
        if not isinstance(self.ai_rmf_resource_uuid, str):
            self.ai_rmf_resource_uuid = str(self.ai_rmf_resource_uuid)

        if self.ai_rmf_resource_address is not None and not isinstance(self.ai_rmf_resource_address, URI):
            self.ai_rmf_resource_address = URI(self.ai_rmf_resource_address)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AiRmfProfile(AiRmfRecord):
    """
    An implementation of the Core's functions, categories and subcategories for a setting, application or technology,
    based on the adopter's requirements, risk tolerance and resources.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_AI_100_1["Profile"]
    class_class_curie: ClassVar[str] = "nist_ai_100_1:Profile"
    class_name: ClassVar[str] = "AiRmfProfile"
    class_model_uri: ClassVar[URIRef] = NIST_AI_100_1.AiRmfProfile

    ai_rmf_id: Union[str, AiRmfProfileAiRmfId] = None
    ai_rmf_profile_kinds: Union[Union[str, "AiRmfProfileKind"], list[Union[str, "AiRmfProfileKind"]]] = None
    ai_rmf_profile_setting: Optional[str] = None
    ai_rmf_profile_subcategories: Optional[Union[Union[str, AiRmfSubcategoryIdentifier], list[Union[str, AiRmfSubcategoryIdentifier]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.ai_rmf_id):
            self.MissingRequiredField("ai_rmf_id")
        if not isinstance(self.ai_rmf_id, AiRmfProfileAiRmfId):
            self.ai_rmf_id = AiRmfProfileAiRmfId(self.ai_rmf_id)

        if self._is_empty(self.ai_rmf_profile_kinds):
            self.MissingRequiredField("ai_rmf_profile_kinds")
        if not isinstance(self.ai_rmf_profile_kinds, list):
            self.ai_rmf_profile_kinds = [self.ai_rmf_profile_kinds] if self.ai_rmf_profile_kinds is not None else []
        self.ai_rmf_profile_kinds = [v if isinstance(v, AiRmfProfileKind) else AiRmfProfileKind(v) for v in self.ai_rmf_profile_kinds]

        if self.ai_rmf_profile_setting is not None and not isinstance(self.ai_rmf_profile_setting, str):
            self.ai_rmf_profile_setting = str(self.ai_rmf_profile_setting)

        if not isinstance(self.ai_rmf_profile_subcategories, list):
            self.ai_rmf_profile_subcategories = [self.ai_rmf_profile_subcategories] if self.ai_rmf_profile_subcategories is not None else []
        self.ai_rmf_profile_subcategories = [v if isinstance(v, AiRmfSubcategoryIdentifier) else AiRmfSubcategoryIdentifier(v) for v in self.ai_rmf_profile_subcategories]

        super().__post_init__(**kwargs)


# Enumerations
class AiRmfCharacteristicName(EnumDefinitionImpl):
    """
    The seven characteristics of trustworthy AI systems in section 3 of the publication.
    """
    valid_and_reliable = PermissibleValue(
        text="valid_and_reliable",
        title="Valid and Reliable",
        description="""Shown by evidence to meet the needs of its intended use, and works without failure over time. Figure 4 makes it a necessary condition for the others.""")
    safe = PermissibleValue(
        text="safe",
        title="Safe",
        description="Keeps people, property and the environment out of danger under defined conditions.")
    secure_and_resilient = PermissibleValue(
        text="secure_and_resilient",
        title="Secure and Resilient",
        description="""Withstands adverse events and recovers from them, and keeps confidentiality, integrity and availability through protections against attack.""")
    accountable_and_transparent = PermissibleValue(
        text="accountable_and_transparent",
        title="Accountable and Transparent",
        description="""Answerable for outcomes, which rests on people being able to get information about the system and its outputs. Figure 4 shows it relating to all the others.""")
    explainable_and_interpretable = PermissibleValue(
        text="explainable_and_interpretable",
        title="Explainable and Interpretable",
        description="""Its working can be represented (how a decision was made) and its output understood in context (why, and what it means for the user).""")
    privacy_enhanced = PermissibleValue(
        text="privacy_enhanced",
        title="Privacy-Enhanced",
        description="""Guided by the norms and practices that protect human autonomy, identity and dignity, such as anonymity, confidentiality and control.""")
    fair_with_harmful_bias_managed = PermissibleValue(
        text="fair_with_harmful_bias_managed",
        title="Fair – with Harmful Bias Managed",
        description="""Addresses equality and equity, including harmful bias and discrimination, knowing that views of fairness differ across cultures and applications.""")

    _defn = EnumDefinition(
        name="AiRmfCharacteristicName",
        description="The seven characteristics of trustworthy AI systems in section 3 of the publication.",
    )

class AiRmfActorTaskName(EnumDefinitionImpl):
    """
    The ten AI actor tasks and five additional AI actors of Appendix A.
    """
    ai_design = PermissibleValue(
        text="ai_design",
        title="AI Design",
        description="""Setting what the system is for, planning and designing it, and gathering and preparing its data.""")
    ai_development = PermissibleValue(
        text="ai_development",
        title="AI Development",
        description="""Providing the initial infrastructure, and creating, selecting, calibrating, training and testing models.""")
    ai_deployment = PermissibleValue(
        text="ai_deployment",
        title="AI Deployment",
        description="""Deciding how the system is used and putting it into production, including pilots and compliance checks.""")
    operation_and_monitoring = PermissibleValue(
        text="operation_and_monitoring",
        title="Operation and Monitoring",
        description="Running the system and regularly assessing its output and impacts.")
    tevv = PermissibleValue(
        text="tevv",
        title="Test, Evaluation, Verification, and Validation (TEVV)",
        description="""Examining the system or its components and finding and fixing problems, throughout the lifecycle.""")
    human_factors = PermissibleValue(
        text="human_factors",
        title="Human Factors",
        description="""Human-centered design and evaluation, involving end users and bringing context-specific norms and values into design.""")
    domain_expert = PermissibleValue(
        text="domain_expert",
        title="Domain Expert",
        description="Giving knowledge of the sector or setting where the system is used.")
    ai_impact_assessment = PermissibleValue(
        text="ai_impact_assessment",
        title="AI Impact Assessment",
        description="Assessing accountability, harmful bias, impacts, product safety, liability and security.")
    procurement = PermissibleValue(
        text="procurement",
        title="Procurement",
        description="Acquiring AI from another party, under financial, legal or policy authority.")
    governance_and_oversight = PermissibleValue(
        text="governance_and_oversight",
        title="Governance and Oversight",
        description="""Holding management, fiduciary and legal authority for the organization where the system is designed, developed or deployed.""")
    third_party_entities = PermissibleValue(
        text="third_party_entities",
        title="Third-party entities",
        description="""Outside organizations that supply or evaluate the data, models, systems or services an organization acquires.""")
    end_users = PermissibleValue(
        text="end_users",
        title="End users",
        description="The people or groups who use the system, whether new to technology or expert in AI.")
    affected_individuals_and_communities = PermissibleValue(
        text="affected_individuals_and_communities",
        title="Affected individuals/communities",
        description="""Those directly or indirectly affected by the system or its output, whether or not they interact with it.""")
    other_ai_actors = PermissibleValue(
        text="other_ai_actors",
        title="Other AI actors",
        description="""Those who may provide norms or guidance on AI risk, such as standards bodies, advocacy groups and researchers.""")
    general_public = PermissibleValue(
        text="general_public",
        title="General public",
        description="""Those most likely to experience the impacts directly, who may motivate what other AI actors do.""")

    _defn = EnumDefinition(
        name="AiRmfActorTaskName",
        description="The ten AI actor tasks and five additional AI actors of Appendix A.",
    )

class AiRmfDimensionName(EnumDefinitionImpl):
    """
    The key dimensions of an AI system in Figure 2.
    """
    application_context = PermissibleValue(
        text="application_context",
        title="Application Context",
        description="The setting the system is planned for and operated in.")
    data_and_input = PermissibleValue(
        text="data_and_input",
        title="Data and Input",
        description="The data the system is built from and takes in.")
    ai_model = PermissibleValue(
        text="ai_model",
        title="AI Model",
        description="The models built, used, verified and validated.")
    task_and_output = PermissibleValue(
        text="task_and_output",
        title="Task and Output",
        description="What the system does and produces once deployed.")
    people_and_planet = PermissibleValue(
        text="people_and_planet",
        title="People and Planet",
        description="Human rights and the well-being of society and the planet, at the center of Figure 2.")

    _defn = EnumDefinition(
        name="AiRmfDimensionName",
        description="The key dimensions of an AI system in Figure 2.",
    )

class AiRmfLifecycleStageName(EnumDefinitionImpl):
    """
    The AI lifecycle stages in Figure 3, of which Figure 2 shows the first six.
    """
    plan_and_design = PermissibleValue(
        text="plan_and_design",
        title="Plan and Design",
        description="Documenting the concept, objectives, assumptions, context and requirements.")
    collect_and_process_data = PermissibleValue(
        text="collect_and_process_data",
        title="Collect and Process Data",
        description="Gathering, validating and cleaning data, and recording what it holds.")
    build_and_use_model = PermissibleValue(
        text="build_and_use_model",
        title="Build and Use Model",
        description="Creating or selecting algorithms and training models.")
    verify_and_validate = PermissibleValue(
        text="verify_and_validate",
        title="Verify and Validate",
        description="Verifying, validating, calibrating and interpreting model output.")
    deploy_and_use = PermissibleValue(
        text="deploy_and_use",
        title="Deploy and Use",
        description="""Piloting, checking compatibility and compliance, managing change and evaluating user experience.""")
    operate_and_monitor = PermissibleValue(
        text="operate_and_monitor",
        title="Operate and Monitor",
        description="Operating the system and continually assessing its recommendations and impacts.")
    use_or_impacted_by = PermissibleValue(
        text="use_or_impacted_by",
        title="Use or Impacted by",
        description="Using the technology or being affected by it, which Figure 3 places under People and Planet.")

    _defn = EnumDefinition(
        name="AiRmfLifecycleStageName",
        description="The AI lifecycle stages in Figure 3, of which Figure 2 shows the first six.",
    )

class AiRmfAudience(EnumDefinitionImpl):
    """
    The two AI RMF audiences of section 2.
    """
    primary = PermissibleValue(
        text="primary",
        title="Primary audience",
        description="AI actors who carry out or manage work on AI systems and drive their risk management.")
    informing = PermissibleValue(
        text="informing",
        title="Informing audience",
        description="AI actors in the People and Planet dimension, who inform the primary audience.")

    _defn = EnumDefinition(
        name="AiRmfAudience",
        description="The two AI RMF audiences of section 2.",
    )

class AiRmfManagementChallengeName(EnumDefinitionImpl):
    """
    The challenges for AI risk management in section 1.2.
    """
    risk_measurement = PermissibleValue(
        text="risk_measurement",
        title="Risk Measurement",
        description="""AI risks that are poorly defined or understood are hard to measure, which does not mean they are high or low.""")
    risk_tolerance = PermissibleValue(
        text="risk_tolerance",
        title="Risk Tolerance",
        description="""The AI RMF can prioritize risk but prescribes no tolerance, which depends on context and changes over time.""")
    risk_prioritization = PermissibleValue(
        text="risk_prioritization",
        title="Risk Prioritization",
        description="""Eliminating all negative risk is unrealistic, so effort goes first to the highest risks in a context of use.""")
    organizational_integration_and_management_of_risk = PermissibleValue(
        text="organizational_integration_and_management_of_risk",
        title="Organizational Integration and Management of Risk",
        description="""AI risk belongs inside broader enterprise risk management, with accountability and commitment from senior levels.""")

    _defn = EnumDefinition(
        name="AiRmfManagementChallengeName",
        description="The challenges for AI risk management in section 1.2.",
    )

class AiRmfMeasurementChallengeName(EnumDefinitionImpl):
    """
    The challenges of measuring AI risk in section 1.2.1.
    """
    third_party_software_hardware_and_data = PermissibleValue(
        text="third_party_software_hardware_and_data",
        title="Risks related to third-party software, hardware, and data",
        description="""Third-party parts can speed work, but their metrics may not match or be disclosed, and how they are used adds risk.""")
    tracking_emergent_risks = PermissibleValue(
        text="tracking_emergent_risks",
        title="Tracking emergent risks",
        description="New risks need identifying, tracking and measuring, which impact assessment helps with.")
    availability_of_reliable_metrics = PermissibleValue(
        text="availability_of_reliable_metrics",
        title="Availability of reliable metrics",
        description="""There is no consensus on robust, verifiable methods, and metrics can be oversimplified or gamed.""")
    risk_at_different_lifecycle_stages = PermissibleValue(
        text="risk_at_different_lifecycle_stages",
        title="Risk at different stages of the AI lifecycle",
        description="Results differ by stage, some risks stay latent, and AI actors see risk differently.")
    risk_in_real_world_settings = PermissibleValue(
        text="risk_in_real_world_settings",
        title="Risk in real-world settings",
        description="What a laboratory measures may differ from what emerges in operation.")
    inscrutability = PermissibleValue(
        text="inscrutability",
        title="Inscrutability",
        description="Opaque systems, poor documentation and inherent uncertainty complicate measurement.")
    human_baseline = PermissibleValue(
        text="human_baseline",
        title="Human baseline",
        description="""A system that augments or replaces human activity needs a baseline, which is hard to systematize.""")

    _defn = EnumDefinition(
        name="AiRmfMeasurementChallengeName",
        description="The challenges of measuring AI risk in section 1.2.1.",
    )

class AiRmfRiskResponse(EnumDefinitionImpl):
    """
    The risk response options MANAGE 1.3 names.
    """
    mitigating = PermissibleValue(
        text="mitigating",
        title="Mitigating",
        description="Reducing the likelihood or magnitude of the risk.")
    transferring = PermissibleValue(
        text="transferring",
        title="Transferring",
        description="Shifting the risk to another party.")
    avoiding = PermissibleValue(
        text="avoiding",
        title="Avoiding",
        description="Not carrying out what creates the risk.")
    accepting = PermissibleValue(
        text="accepting",
        title="Accepting",
        description="Bearing the risk without further action.")

    _defn = EnumDefinition(
        name="AiRmfRiskResponse",
        description="The risk response options MANAGE 1.3 names.",
    )

class AiRmfImpactDirection(EnumDefinitionImpl):
    """
    Whether an impact is positive, negative or both, as section 1.1 puts it.
    """
    positive = PermissibleValue(
        text="positive",
        title="Positive",
        description="An opportunity or benefit.")
    negative = PermissibleValue(
        text="negative",
        title="Negative",
        description="A threat or harm.")
    both = PermissibleValue(
        text="both",
        title="Both",
        description="Positive and negative at once.")

    _defn = EnumDefinition(
        name="AiRmfImpactDirection",
        description="Whether an impact is positive, negative or both, as section 1.1 puts it.",
    )

class AiRmfAffectedParty(EnumDefinitionImpl):
    """
    Who section 1.1 says can experience negative impact or harm.
    """
    individuals = PermissibleValue(
        text="individuals",
        title="Individuals",
        description="Particular people.")
    groups = PermissibleValue(
        text="groups",
        title="Groups",
        description="Groups of people.")
    communities = PermissibleValue(
        text="communities",
        title="Communities",
        description="Communities of people.")
    organizations = PermissibleValue(
        text="organizations",
        title="Organizations",
        description="Organizations.")
    society = PermissibleValue(
        text="society",
        title="Society",
        description="Society at large.")
    environment = PermissibleValue(
        text="environment",
        title="The environment",
        description="The natural environment.")
    planet = PermissibleValue(
        text="planet",
        title="The planet",
        description="The planet as a whole.")

    _defn = EnumDefinition(
        name="AiRmfAffectedParty",
        description="Who section 1.1 says can experience negative impact or harm.",
    )

class AiRmfHarmCategory(EnumDefinitionImpl):
    """
    The three headings of Figure 1.
    """
    people = PermissibleValue(
        text="people",
        title="Harm to People",
        description="Harm that falls on individuals, groups, communities or society.")
    organization = PermissibleValue(
        text="organization",
        title="Harm to an Organization",
        description="Harm that falls on an organization.")
    ecosystem = PermissibleValue(
        text="ecosystem",
        title="Harm to an Ecosystem",
        description="Harm that falls on interconnected systems and resources.")

    _defn = EnumDefinition(
        name="AiRmfHarmCategory",
        description="The three headings of Figure 1.",
    )

class AiRmfHarmExample(EnumDefinitionImpl):
    """
    The examples of potential harm in Figure 1, which NIST offers as examples and not as a closed list.
    """
    individual = PermissibleValue(
        text="individual",
        title="Individual",
        description="To a person's civil liberties, rights, safety or economic opportunity.")
    group_or_community = PermissibleValue(
        text="group_or_community",
        title="Group/Community",
        description="To a group, such as discrimination against a sub-group of a population.")
    societal = PermissibleValue(
        text="societal",
        title="Societal",
        description="To democratic participation or educational access.")
    business_operations = PermissibleValue(
        text="business_operations",
        title="Business operations",
        description="To how an organization operates.")
    security_breach_or_monetary_loss = PermissibleValue(
        text="security_breach_or_monetary_loss",
        title="Security breaches or monetary loss",
        description="To an organization through a breach of security or a loss of money.")
    reputation = PermissibleValue(
        text="reputation",
        title="Reputation",
        description="To an organization's standing.")
    interdependent_elements = PermissibleValue(
        text="interdependent_elements",
        title="Interconnected and interdependent elements and resources",
        description="To parts and resources that depend on each other.")
    financial_or_supply_systems = PermissibleValue(
        text="financial_or_supply_systems",
        title="Global financial system, supply chain, or interrelated systems",
        description="To large systems that link organizations.")
    natural_resources_and_environment = PermissibleValue(
        text="natural_resources_and_environment",
        title="Natural resources, the environment, and planet",
        description="To the natural world.")

    _defn = EnumDefinition(
        name="AiRmfHarmExample",
        description="The examples of potential harm in Figure 1, which NIST offers as examples and not as a closed list.",
    )

class AiRmfBiasCategory(EnumDefinitionImpl):
    """
    The three major categories of AI bias in section 3.7, each of which can occur without prejudice or discriminatory
    intent.
    """
    systemic = PermissibleValue(
        text="systemic",
        title="Systemic",
        description="In datasets, in organizational norms and processes, and in the wider society that uses AI.")
    computational_and_statistical = PermissibleValue(
        text="computational_and_statistical",
        title="Computational and statistical",
        description="""In datasets and algorithms, often from systematic errors due to samples that are not representative.""")
    human_cognitive = PermissibleValue(
        text="human_cognitive",
        title="Human-cognitive",
        description="In how people perceive system information to decide, or think about what a system is for.")

    _defn = EnumDefinition(
        name="AiRmfBiasCategory",
        description="""The three major categories of AI bias in section 3.7, each of which can occur without prejudice or discriminatory intent.""",
    )

class AiRmfProfileKind(EnumDefinitionImpl):
    """
    The kinds of AI RMF profile that section 6 names.
    """
    use_case = PermissibleValue(
        text="use_case",
        title="Use-case profile",
        description="The Core implemented for a specific setting or application.")
    current = PermissibleValue(
        text="current",
        title="Current Profile",
        description="""A temporal profile saying how AI is managed today and the related risks, in terms of current outcomes.""")
    target = PermissibleValue(
        text="target",
        title="Target Profile",
        description="A temporal profile saying which outcomes the desired risk management goals need.")
    cross_sectoral = PermissibleValue(
        text="cross_sectoral",
        title="Cross-sectoral profile",
        description="""Covers risks of models or applications used across use cases or sectors, or activities common to them, such as using large language models.""")

    _defn = EnumDefinition(
        name="AiRmfProfileKind",
        description="The kinds of AI RMF profile that section 6 names.",
    )

# Slots
class slots:
    pass

slots.ai_rmf_id = Slot(uri=NIST_AI_100_1.ai_rmf_id, name="ai_rmf_id", curie=NIST_AI_100_1.curie('ai_rmf_id'),
                   model_uri=NIST_AI_100_1.ai_rmf_id, domain=None, range=URIRef)

slots.ai_rmf_subcategory_id = Slot(uri=NIST_AI_100_1.ai_rmf_subcategory_id, name="ai_rmf_subcategory_id", curie=NIST_AI_100_1.curie('ai_rmf_subcategory_id'),
                   model_uri=NIST_AI_100_1.ai_rmf_subcategory_id, domain=None, range=Union[str, AiRmfSubcategoryIdentifier])

slots.title = Slot(uri=SCHEMA.name, name="title", curie=SCHEMA.curie('name'),
                   model_uri=NIST_AI_100_1.title, domain=None, range=Optional[str])

slots.description = Slot(uri=SCHEMA.description, name="description", curie=SCHEMA.curie('description'),
                   model_uri=NIST_AI_100_1.description, domain=None, range=Optional[str])

slots.ai_rmf_likelihood = Slot(uri=NIST_AI_100_1.ai_rmf_likelihood, name="ai_rmf_likelihood", curie=NIST_AI_100_1.curie('ai_rmf_likelihood'),
                   model_uri=NIST_AI_100_1.ai_rmf_likelihood, domain=None, range=Optional[str])

slots.ai_rmf_magnitude = Slot(uri=NIST_AI_100_1.ai_rmf_magnitude, name="ai_rmf_magnitude", curie=NIST_AI_100_1.curie('ai_rmf_magnitude'),
                   model_uri=NIST_AI_100_1.ai_rmf_magnitude, domain=None, range=Optional[str])

slots.ai_rmf_function_id = Slot(uri=NIST_AI_100_1.ai_rmf_function_id, name="ai_rmf_function_id", curie=NIST_AI_100_1.curie('ai_rmf_function_id'),
                   model_uri=NIST_AI_100_1.ai_rmf_function_id, domain=None, range=Union[str, AiRmfFunctionIdentifier])

slots.ai_rmf_category_id = Slot(uri=NIST_AI_100_1.ai_rmf_category_id, name="ai_rmf_category_id", curie=NIST_AI_100_1.curie('ai_rmf_category_id'),
                   model_uri=NIST_AI_100_1.ai_rmf_category_id, domain=None, range=Union[str, AiRmfCategoryIdentifier])

slots.ai_rmf_suggested_action_id = Slot(uri=NIST_AI_100_1.ai_rmf_suggested_action_id, name="ai_rmf_suggested_action_id", curie=NIST_AI_100_1.curie('ai_rmf_suggested_action_id'),
                   model_uri=NIST_AI_100_1.ai_rmf_suggested_action_id, domain=None, range=Union[str, AiRmfSuggestedActionIdentifier])

slots.ai_rmf_documentation_id = Slot(uri=NIST_AI_100_1.ai_rmf_documentation_id, name="ai_rmf_documentation_id", curie=NIST_AI_100_1.curie('ai_rmf_documentation_id'),
                   model_uri=NIST_AI_100_1.ai_rmf_documentation_id, domain=None, range=Union[str, AiRmfDocumentationIdentifier])

slots.aiRmfFramework__ai_rmf_version = Slot(uri=NIST_AI_100_1.ai_rmf_version, name="aiRmfFramework__ai_rmf_version", curie=NIST_AI_100_1.curie('ai_rmf_version'),
                   model_uri=NIST_AI_100_1.aiRmfFramework__ai_rmf_version, domain=None, range=str,
                   pattern=re.compile(r'^[0-9]+\.[0-9]+$'))

slots.aiRmfFramework__ai_rmf_functions = Slot(uri=NIST_AI_100_1.ai_rmf_functions, name="aiRmfFramework__ai_rmf_functions", curie=NIST_AI_100_1.curie('ai_rmf_functions'),
                   model_uri=NIST_AI_100_1.aiRmfFramework__ai_rmf_functions, domain=None, range=Union[Union[dict, AiRmfFunction], list[Union[dict, AiRmfFunction]]])

slots.aiRmfFramework__ai_rmf_characteristics = Slot(uri=NIST_AI_100_1.ai_rmf_characteristics, name="aiRmfFramework__ai_rmf_characteristics", curie=NIST_AI_100_1.curie('ai_rmf_characteristics'),
                   model_uri=NIST_AI_100_1.aiRmfFramework__ai_rmf_characteristics, domain=None, range=Optional[Union[Union[dict, AiRmfTrustworthinessCharacteristic], list[Union[dict, AiRmfTrustworthinessCharacteristic]]]])

slots.aiRmfFramework__ai_rmf_dimensions = Slot(uri=NIST_AI_100_1.ai_rmf_dimensions, name="aiRmfFramework__ai_rmf_dimensions", curie=NIST_AI_100_1.curie('ai_rmf_dimensions'),
                   model_uri=NIST_AI_100_1.aiRmfFramework__ai_rmf_dimensions, domain=None, range=Optional[Union[Union[dict, AiRmfDimension], list[Union[dict, AiRmfDimension]]]])

slots.aiRmfFramework__ai_rmf_lifecycle_stages = Slot(uri=NIST_AI_100_1.ai_rmf_lifecycle_stages, name="aiRmfFramework__ai_rmf_lifecycle_stages", curie=NIST_AI_100_1.curie('ai_rmf_lifecycle_stages'),
                   model_uri=NIST_AI_100_1.aiRmfFramework__ai_rmf_lifecycle_stages, domain=None, range=Optional[Union[Union[dict, AiRmfLifecycleStage], list[Union[dict, AiRmfLifecycleStage]]]])

slots.aiRmfFramework__ai_rmf_actor_task_list = Slot(uri=NIST_AI_100_1.ai_rmf_actor_task_list, name="aiRmfFramework__ai_rmf_actor_task_list", curie=NIST_AI_100_1.curie('ai_rmf_actor_task_list'),
                   model_uri=NIST_AI_100_1.aiRmfFramework__ai_rmf_actor_task_list, domain=None, range=Optional[Union[Union[dict, AiRmfActorTask], list[Union[dict, AiRmfActorTask]]]])

slots.aiRmfFramework__ai_rmf_management_challenges = Slot(uri=NIST_AI_100_1.ai_rmf_management_challenges, name="aiRmfFramework__ai_rmf_management_challenges", curie=NIST_AI_100_1.curie('ai_rmf_management_challenges'),
                   model_uri=NIST_AI_100_1.aiRmfFramework__ai_rmf_management_challenges, domain=None, range=Optional[Union[Union[dict, AiRmfManagementChallenge], list[Union[dict, AiRmfManagementChallenge]]]])

slots.aiRmfFramework__ai_rmf_specific_risks = Slot(uri=NIST_AI_100_1.ai_rmf_specific_risks, name="aiRmfFramework__ai_rmf_specific_risks", curie=NIST_AI_100_1.curie('ai_rmf_specific_risks'),
                   model_uri=NIST_AI_100_1.aiRmfFramework__ai_rmf_specific_risks, domain=None, range=Optional[Union[Union[dict, AiRmfSpecificRisk], list[Union[dict, AiRmfSpecificRisk]]]])

slots.aiRmfFramework__ai_rmf_human_ai_issues = Slot(uri=NIST_AI_100_1.ai_rmf_human_ai_issues, name="aiRmfFramework__ai_rmf_human_ai_issues", curie=NIST_AI_100_1.curie('ai_rmf_human_ai_issues'),
                   model_uri=NIST_AI_100_1.aiRmfFramework__ai_rmf_human_ai_issues, domain=None, range=Optional[Union[Union[dict, AiRmfHumanAiIssue], list[Union[dict, AiRmfHumanAiIssue]]]])

slots.aiRmfFramework__ai_rmf_attributes = Slot(uri=NIST_AI_100_1.ai_rmf_attributes, name="aiRmfFramework__ai_rmf_attributes", curie=NIST_AI_100_1.curie('ai_rmf_attributes'),
                   model_uri=NIST_AI_100_1.aiRmfFramework__ai_rmf_attributes, domain=None, range=Optional[Union[Union[dict, AiRmfAttribute], list[Union[dict, AiRmfAttribute]]]])

slots.aiRmfTrustworthinessCharacteristic__ai_rmf_characteristic_name = Slot(uri=NIST_AI_100_1.ai_rmf_characteristic_name, name="aiRmfTrustworthinessCharacteristic__ai_rmf_characteristic_name", curie=NIST_AI_100_1.curie('ai_rmf_characteristic_name'),
                   model_uri=NIST_AI_100_1.aiRmfTrustworthinessCharacteristic__ai_rmf_characteristic_name, domain=None, range=Union[str, "AiRmfCharacteristicName"])

slots.aiRmfTrustworthinessCharacteristic__ai_rmf_characteristic_section = Slot(uri=NIST_AI_100_1.ai_rmf_characteristic_section, name="aiRmfTrustworthinessCharacteristic__ai_rmf_characteristic_section", curie=NIST_AI_100_1.curie('ai_rmf_characteristic_section'),
                   model_uri=NIST_AI_100_1.aiRmfTrustworthinessCharacteristic__ai_rmf_characteristic_section, domain=None, range=str,
                   pattern=re.compile(r'^3\.[1-7]$'))

slots.aiRmfTrustworthinessCharacteristic__ai_rmf_characteristic_is_base = Slot(uri=NIST_AI_100_1.ai_rmf_characteristic_is_base, name="aiRmfTrustworthinessCharacteristic__ai_rmf_characteristic_is_base", curie=NIST_AI_100_1.curie('ai_rmf_characteristic_is_base'),
                   model_uri=NIST_AI_100_1.aiRmfTrustworthinessCharacteristic__ai_rmf_characteristic_is_base, domain=None, range=Optional[Union[bool, Bool]])

slots.aiRmfTrustworthinessCharacteristic__ai_rmf_characteristic_relates_to_all = Slot(uri=NIST_AI_100_1.ai_rmf_characteristic_relates_to_all, name="aiRmfTrustworthinessCharacteristic__ai_rmf_characteristic_relates_to_all", curie=NIST_AI_100_1.curie('ai_rmf_characteristic_relates_to_all'),
                   model_uri=NIST_AI_100_1.aiRmfTrustworthinessCharacteristic__ai_rmf_characteristic_relates_to_all, domain=None, range=Optional[Union[bool, Bool]])

slots.aiRmfDimension__ai_rmf_dimension_name = Slot(uri=NIST_AI_100_1.ai_rmf_dimension_name, name="aiRmfDimension__ai_rmf_dimension_name", curie=NIST_AI_100_1.curie('ai_rmf_dimension_name'),
                   model_uri=NIST_AI_100_1.aiRmfDimension__ai_rmf_dimension_name, domain=None, range=Union[str, "AiRmfDimensionName"])

slots.aiRmfDimension__ai_rmf_dimension_audience = Slot(uri=NIST_AI_100_1.ai_rmf_dimension_audience, name="aiRmfDimension__ai_rmf_dimension_audience", curie=NIST_AI_100_1.curie('ai_rmf_dimension_audience'),
                   model_uri=NIST_AI_100_1.aiRmfDimension__ai_rmf_dimension_audience, domain=None, range=Union[str, "AiRmfAudience"])

slots.aiRmfLifecycleStage__ai_rmf_lifecycle_stage_name = Slot(uri=NIST_AI_100_1.ai_rmf_lifecycle_stage_name, name="aiRmfLifecycleStage__ai_rmf_lifecycle_stage_name", curie=NIST_AI_100_1.curie('ai_rmf_lifecycle_stage_name'),
                   model_uri=NIST_AI_100_1.aiRmfLifecycleStage__ai_rmf_lifecycle_stage_name, domain=None, range=Union[str, "AiRmfLifecycleStageName"])

slots.aiRmfLifecycleStage__ai_rmf_lifecycle_stage_dimension = Slot(uri=NIST_AI_100_1.ai_rmf_lifecycle_stage_dimension, name="aiRmfLifecycleStage__ai_rmf_lifecycle_stage_dimension", curie=NIST_AI_100_1.curie('ai_rmf_lifecycle_stage_dimension'),
                   model_uri=NIST_AI_100_1.aiRmfLifecycleStage__ai_rmf_lifecycle_stage_dimension, domain=None, range=Union[str, "AiRmfDimensionName"])

slots.aiRmfLifecycleStage__ai_rmf_lifecycle_stage_tevv = Slot(uri=NIST_AI_100_1.ai_rmf_lifecycle_stage_tevv, name="aiRmfLifecycleStage__ai_rmf_lifecycle_stage_tevv", curie=NIST_AI_100_1.curie('ai_rmf_lifecycle_stage_tevv'),
                   model_uri=NIST_AI_100_1.aiRmfLifecycleStage__ai_rmf_lifecycle_stage_tevv, domain=None, range=Optional[str])

slots.aiRmfLifecycleStage__ai_rmf_lifecycle_stage_representative_actors = Slot(uri=NIST_AI_100_1.ai_rmf_lifecycle_stage_representative_actors, name="aiRmfLifecycleStage__ai_rmf_lifecycle_stage_representative_actors", curie=NIST_AI_100_1.curie('ai_rmf_lifecycle_stage_representative_actors'),
                   model_uri=NIST_AI_100_1.aiRmfLifecycleStage__ai_rmf_lifecycle_stage_representative_actors, domain=None, range=Optional[Union[str, list[str]]])

slots.aiRmfActorTask__ai_rmf_actor_task_name = Slot(uri=NIST_AI_100_1.ai_rmf_actor_task_name, name="aiRmfActorTask__ai_rmf_actor_task_name", curie=NIST_AI_100_1.curie('ai_rmf_actor_task_name'),
                   model_uri=NIST_AI_100_1.aiRmfActorTask__ai_rmf_actor_task_name, domain=None, range=Union[str, "AiRmfActorTaskName"])

slots.aiRmfActorTask__ai_rmf_actor_task_is_additional_actor = Slot(uri=NIST_AI_100_1.ai_rmf_actor_task_is_additional_actor, name="aiRmfActorTask__ai_rmf_actor_task_is_additional_actor", curie=NIST_AI_100_1.curie('ai_rmf_actor_task_is_additional_actor'),
                   model_uri=NIST_AI_100_1.aiRmfActorTask__ai_rmf_actor_task_is_additional_actor, domain=None, range=Optional[Union[bool, Bool]])

slots.aiRmfActorTask__ai_rmf_actor_task_representative_actors = Slot(uri=NIST_AI_100_1.ai_rmf_actor_task_representative_actors, name="aiRmfActorTask__ai_rmf_actor_task_representative_actors", curie=NIST_AI_100_1.curie('ai_rmf_actor_task_representative_actors'),
                   model_uri=NIST_AI_100_1.aiRmfActorTask__ai_rmf_actor_task_representative_actors, domain=None, range=Optional[Union[str, list[str]]])

slots.aiRmfManagementChallenge__ai_rmf_management_challenge_name = Slot(uri=NIST_AI_100_1.ai_rmf_management_challenge_name, name="aiRmfManagementChallenge__ai_rmf_management_challenge_name", curie=NIST_AI_100_1.curie('ai_rmf_management_challenge_name'),
                   model_uri=NIST_AI_100_1.aiRmfManagementChallenge__ai_rmf_management_challenge_name, domain=None, range=Union[str, "AiRmfManagementChallengeName"])

slots.aiRmfManagementChallenge__ai_rmf_management_challenge_measurement_challenges = Slot(uri=NIST_AI_100_1.ai_rmf_management_challenge_measurement_challenges, name="aiRmfManagementChallenge__ai_rmf_management_challenge_measurement_challenges", curie=NIST_AI_100_1.curie('ai_rmf_management_challenge_measurement_challenges'),
                   model_uri=NIST_AI_100_1.aiRmfManagementChallenge__ai_rmf_management_challenge_measurement_challenges, domain=None, range=Optional[Union[Union[dict, AiRmfMeasurementChallenge], list[Union[dict, AiRmfMeasurementChallenge]]]])

slots.aiRmfMeasurementChallenge__ai_rmf_measurement_challenge_name = Slot(uri=NIST_AI_100_1.ai_rmf_measurement_challenge_name, name="aiRmfMeasurementChallenge__ai_rmf_measurement_challenge_name", curie=NIST_AI_100_1.curie('ai_rmf_measurement_challenge_name'),
                   model_uri=NIST_AI_100_1.aiRmfMeasurementChallenge__ai_rmf_measurement_challenge_name, domain=None, range=Union[str, "AiRmfMeasurementChallengeName"])

slots.aiRmfSpecificRisk__ai_rmf_specific_risk_position = Slot(uri=NIST_AI_100_1.ai_rmf_specific_risk_position, name="aiRmfSpecificRisk__ai_rmf_specific_risk_position", curie=NIST_AI_100_1.curie('ai_rmf_specific_risk_position'),
                   model_uri=NIST_AI_100_1.aiRmfSpecificRisk__ai_rmf_specific_risk_position, domain=None, range=int)

slots.aiRmfHumanAiIssue__ai_rmf_human_ai_issue_number = Slot(uri=NIST_AI_100_1.ai_rmf_human_ai_issue_number, name="aiRmfHumanAiIssue__ai_rmf_human_ai_issue_number", curie=NIST_AI_100_1.curie('ai_rmf_human_ai_issue_number'),
                   model_uri=NIST_AI_100_1.aiRmfHumanAiIssue__ai_rmf_human_ai_issue_number, domain=None, range=int)

slots.aiRmfAttribute__ai_rmf_attribute_number = Slot(uri=NIST_AI_100_1.ai_rmf_attribute_number, name="aiRmfAttribute__ai_rmf_attribute_number", curie=NIST_AI_100_1.curie('ai_rmf_attribute_number'),
                   model_uri=NIST_AI_100_1.aiRmfAttribute__ai_rmf_attribute_number, domain=None, range=int)

slots.aiRmfSystem__ai_rmf_system_lifecycle_stages = Slot(uri=NIST_AI_100_1.ai_rmf_system_lifecycle_stages, name="aiRmfSystem__ai_rmf_system_lifecycle_stages", curie=NIST_AI_100_1.curie('ai_rmf_system_lifecycle_stages'),
                   model_uri=NIST_AI_100_1.aiRmfSystem__ai_rmf_system_lifecycle_stages, domain=None, range=Optional[Union[Union[str, "AiRmfLifecycleStageName"], list[Union[str, "AiRmfLifecycleStageName"]]]])

slots.aiRmfActor__ai_rmf_actor_tasks = Slot(uri=NIST_AI_100_1.ai_rmf_actor_tasks, name="aiRmfActor__ai_rmf_actor_tasks", curie=NIST_AI_100_1.curie('ai_rmf_actor_tasks'),
                   model_uri=NIST_AI_100_1.aiRmfActor__ai_rmf_actor_tasks, domain=None, range=Optional[Union[Union[str, "AiRmfActorTaskName"], list[Union[str, "AiRmfActorTaskName"]]]])

slots.aiRmfActor__ai_rmf_actor_audience = Slot(uri=NIST_AI_100_1.ai_rmf_actor_audience, name="aiRmfActor__ai_rmf_actor_audience", curie=NIST_AI_100_1.curie('ai_rmf_actor_audience'),
                   model_uri=NIST_AI_100_1.aiRmfActor__ai_rmf_actor_audience, domain=None, range=Optional[Union[str, "AiRmfAudience"]])

slots.aiRmfActor__ai_rmf_actor_lifecycle_stages = Slot(uri=NIST_AI_100_1.ai_rmf_actor_lifecycle_stages, name="aiRmfActor__ai_rmf_actor_lifecycle_stages", curie=NIST_AI_100_1.curie('ai_rmf_actor_lifecycle_stages'),
                   model_uri=NIST_AI_100_1.aiRmfActor__ai_rmf_actor_lifecycle_stages, domain=None, range=Optional[Union[Union[str, "AiRmfLifecycleStageName"], list[Union[str, "AiRmfLifecycleStageName"]]]])

slots.aiRmfRisk__ai_rmf_risk_system = Slot(uri=NIST_AI_100_1.ai_rmf_risk_system, name="aiRmfRisk__ai_rmf_risk_system", curie=NIST_AI_100_1.curie('ai_rmf_risk_system'),
                   model_uri=NIST_AI_100_1.aiRmfRisk__ai_rmf_risk_system, domain=None, range=Optional[Union[str, AiRmfSystemAiRmfId]])

slots.aiRmfRisk__ai_rmf_risk_impacts = Slot(uri=NIST_AI_100_1.ai_rmf_risk_impacts, name="aiRmfRisk__ai_rmf_risk_impacts", curie=NIST_AI_100_1.curie('ai_rmf_risk_impacts'),
                   model_uri=NIST_AI_100_1.aiRmfRisk__ai_rmf_risk_impacts, domain=None, range=Optional[Union[dict[Union[str, AiRmfImpactAiRmfId], Union[dict, AiRmfImpact]], list[Union[dict, AiRmfImpact]]]])

slots.aiRmfRisk__ai_rmf_risk_characteristics = Slot(uri=NIST_AI_100_1.ai_rmf_risk_characteristics, name="aiRmfRisk__ai_rmf_risk_characteristics", curie=NIST_AI_100_1.curie('ai_rmf_risk_characteristics'),
                   model_uri=NIST_AI_100_1.aiRmfRisk__ai_rmf_risk_characteristics, domain=None, range=Optional[Union[Union[str, "AiRmfCharacteristicName"], list[Union[str, "AiRmfCharacteristicName"]]]])

slots.aiRmfRisk__ai_rmf_risk_lifecycle_stages = Slot(uri=NIST_AI_100_1.ai_rmf_risk_lifecycle_stages, name="aiRmfRisk__ai_rmf_risk_lifecycle_stages", curie=NIST_AI_100_1.curie('ai_rmf_risk_lifecycle_stages'),
                   model_uri=NIST_AI_100_1.aiRmfRisk__ai_rmf_risk_lifecycle_stages, domain=None, range=Optional[Union[Union[str, "AiRmfLifecycleStageName"], list[Union[str, "AiRmfLifecycleStageName"]]]])

slots.aiRmfRisk__ai_rmf_risk_responses = Slot(uri=NIST_AI_100_1.ai_rmf_risk_responses, name="aiRmfRisk__ai_rmf_risk_responses", curie=NIST_AI_100_1.curie('ai_rmf_risk_responses'),
                   model_uri=NIST_AI_100_1.aiRmfRisk__ai_rmf_risk_responses, domain=None, range=Optional[Union[Union[str, "AiRmfRiskResponse"], list[Union[str, "AiRmfRiskResponse"]]]])

slots.aiRmfImpact__ai_rmf_impact_direction = Slot(uri=NIST_AI_100_1.ai_rmf_impact_direction, name="aiRmfImpact__ai_rmf_impact_direction", curie=NIST_AI_100_1.curie('ai_rmf_impact_direction'),
                   model_uri=NIST_AI_100_1.aiRmfImpact__ai_rmf_impact_direction, domain=None, range=Union[str, "AiRmfImpactDirection"])

slots.aiRmfImpact__ai_rmf_impact_affected_parties = Slot(uri=NIST_AI_100_1.ai_rmf_impact_affected_parties, name="aiRmfImpact__ai_rmf_impact_affected_parties", curie=NIST_AI_100_1.curie('ai_rmf_impact_affected_parties'),
                   model_uri=NIST_AI_100_1.aiRmfImpact__ai_rmf_impact_affected_parties, domain=None, range=Optional[Union[Union[str, "AiRmfAffectedParty"], list[Union[str, "AiRmfAffectedParty"]]]])

slots.aiRmfHarm__ai_rmf_harm_category = Slot(uri=NIST_AI_100_1.ai_rmf_harm_category, name="aiRmfHarm__ai_rmf_harm_category", curie=NIST_AI_100_1.curie('ai_rmf_harm_category'),
                   model_uri=NIST_AI_100_1.aiRmfHarm__ai_rmf_harm_category, domain=None, range=Union[str, "AiRmfHarmCategory"])

slots.aiRmfHarm__ai_rmf_harm_example = Slot(uri=NIST_AI_100_1.ai_rmf_harm_example, name="aiRmfHarm__ai_rmf_harm_example", curie=NIST_AI_100_1.curie('ai_rmf_harm_example'),
                   model_uri=NIST_AI_100_1.aiRmfHarm__ai_rmf_harm_example, domain=None, range=Optional[Union[str, "AiRmfHarmExample"]])

slots.aiRmfRiskTolerance__ai_rmf_risk_tolerance_holder = Slot(uri=NIST_AI_100_1.ai_rmf_risk_tolerance_holder, name="aiRmfRiskTolerance__ai_rmf_risk_tolerance_holder", curie=NIST_AI_100_1.curie('ai_rmf_risk_tolerance_holder'),
                   model_uri=NIST_AI_100_1.aiRmfRiskTolerance__ai_rmf_risk_tolerance_holder, domain=None, range=Optional[Union[str, AiRmfActorAiRmfId]])

slots.aiRmfRiskTolerance__ai_rmf_risk_tolerance_influences = Slot(uri=NIST_AI_100_1.ai_rmf_risk_tolerance_influences, name="aiRmfRiskTolerance__ai_rmf_risk_tolerance_influences", curie=NIST_AI_100_1.curie('ai_rmf_risk_tolerance_influences'),
                   model_uri=NIST_AI_100_1.aiRmfRiskTolerance__ai_rmf_risk_tolerance_influences, domain=None, range=Optional[Union[str, list[str]]])

slots.aiRmfBias__ai_rmf_bias_categories = Slot(uri=NIST_AI_100_1.ai_rmf_bias_categories, name="aiRmfBias__ai_rmf_bias_categories", curie=NIST_AI_100_1.curie('ai_rmf_bias_categories'),
                   model_uri=NIST_AI_100_1.aiRmfBias__ai_rmf_bias_categories, domain=None, range=Union[Union[str, "AiRmfBiasCategory"], list[Union[str, "AiRmfBiasCategory"]]])

slots.aiRmfFunction__ai_rmf_function_categories = Slot(uri=NIST_AI_100_1.ai_rmf_function_categories, name="aiRmfFunction__ai_rmf_function_categories", curie=NIST_AI_100_1.curie('ai_rmf_function_categories'),
                   model_uri=NIST_AI_100_1.aiRmfFunction__ai_rmf_function_categories, domain=None, range=Optional[Union[Union[dict, AiRmfCategory], list[Union[dict, AiRmfCategory]]]])

slots.aiRmfCategory__ai_rmf_category_subcategories = Slot(uri=NIST_AI_100_1.ai_rmf_category_subcategories, name="aiRmfCategory__ai_rmf_category_subcategories", curie=NIST_AI_100_1.curie('ai_rmf_category_subcategories'),
                   model_uri=NIST_AI_100_1.aiRmfCategory__ai_rmf_category_subcategories, domain=None, range=Optional[Union[Union[dict, AiRmfSubcategory], list[Union[dict, AiRmfSubcategory]]]])

slots.aiRmfSubcategory__ai_rmf_subcategory_about = Slot(uri=NIST_AI_100_1.ai_rmf_subcategory_about, name="aiRmfSubcategory__ai_rmf_subcategory_about", curie=NIST_AI_100_1.curie('ai_rmf_subcategory_about'),
                   model_uri=NIST_AI_100_1.aiRmfSubcategory__ai_rmf_subcategory_about, domain=None, range=Optional[Union[str, list[str]]])

slots.aiRmfSubcategory__ai_rmf_subcategory_suggested_actions = Slot(uri=NIST_AI_100_1.ai_rmf_subcategory_suggested_actions, name="aiRmfSubcategory__ai_rmf_subcategory_suggested_actions", curie=NIST_AI_100_1.curie('ai_rmf_subcategory_suggested_actions'),
                   model_uri=NIST_AI_100_1.aiRmfSubcategory__ai_rmf_subcategory_suggested_actions, domain=None, range=Optional[Union[Union[dict, AiRmfSuggestedAction], list[Union[dict, AiRmfSuggestedAction]]]])

slots.aiRmfSubcategory__ai_rmf_subcategory_documentation = Slot(uri=NIST_AI_100_1.ai_rmf_subcategory_documentation, name="aiRmfSubcategory__ai_rmf_subcategory_documentation", curie=NIST_AI_100_1.curie('ai_rmf_subcategory_documentation'),
                   model_uri=NIST_AI_100_1.aiRmfSubcategory__ai_rmf_subcategory_documentation, domain=None, range=Optional[Union[Union[dict, AiRmfDocumentationItem], list[Union[dict, AiRmfDocumentationItem]]]])

slots.aiRmfSubcategory__ai_rmf_subcategory_transparency_resources = Slot(uri=NIST_AI_100_1.ai_rmf_subcategory_transparency_resources, name="aiRmfSubcategory__ai_rmf_subcategory_transparency_resources", curie=NIST_AI_100_1.curie('ai_rmf_subcategory_transparency_resources'),
                   model_uri=NIST_AI_100_1.aiRmfSubcategory__ai_rmf_subcategory_transparency_resources, domain=None, range=Optional[Union[Union[dict, AiRmfResource], list[Union[dict, AiRmfResource]]]])

slots.aiRmfSubcategory__ai_rmf_subcategory_references = Slot(uri=NIST_AI_100_1.ai_rmf_subcategory_references, name="aiRmfSubcategory__ai_rmf_subcategory_references", curie=NIST_AI_100_1.curie('ai_rmf_subcategory_references'),
                   model_uri=NIST_AI_100_1.aiRmfSubcategory__ai_rmf_subcategory_references, domain=None, range=Optional[Union[Union[dict, AiRmfResource], list[Union[dict, AiRmfResource]]]])

slots.aiRmfSubcategory__ai_rmf_subcategory_ai_actors = Slot(uri=NIST_AI_100_1.ai_rmf_subcategory_ai_actors, name="aiRmfSubcategory__ai_rmf_subcategory_ai_actors", curie=NIST_AI_100_1.curie('ai_rmf_subcategory_ai_actors'),
                   model_uri=NIST_AI_100_1.aiRmfSubcategory__ai_rmf_subcategory_ai_actors, domain=None, range=Optional[Union[Union[str, "AiRmfActorTaskName"], list[Union[str, "AiRmfActorTaskName"]]]])

slots.aiRmfSubcategory__ai_rmf_subcategory_topics = Slot(uri=NIST_AI_100_1.ai_rmf_subcategory_topics, name="aiRmfSubcategory__ai_rmf_subcategory_topics", curie=NIST_AI_100_1.curie('ai_rmf_subcategory_topics'),
                   model_uri=NIST_AI_100_1.aiRmfSubcategory__ai_rmf_subcategory_topics, domain=None, range=Optional[Union[str, list[str]]])

slots.aiRmfResource__ai_rmf_resource_uuid = Slot(uri=NIST_AI_100_1.ai_rmf_resource_uuid, name="aiRmfResource__ai_rmf_resource_uuid", curie=NIST_AI_100_1.curie('ai_rmf_resource_uuid'),
                   model_uri=NIST_AI_100_1.aiRmfResource__ai_rmf_resource_uuid, domain=None, range=str,
                   pattern=re.compile(r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$'))

slots.aiRmfResource__ai_rmf_resource_address = Slot(uri=NIST_AI_100_1.ai_rmf_resource_address, name="aiRmfResource__ai_rmf_resource_address", curie=NIST_AI_100_1.curie('ai_rmf_resource_address'),
                   model_uri=NIST_AI_100_1.aiRmfResource__ai_rmf_resource_address, domain=None, range=Optional[Union[str, URI]])

slots.aiRmfProfile__ai_rmf_profile_kinds = Slot(uri=NIST_AI_100_1.ai_rmf_profile_kinds, name="aiRmfProfile__ai_rmf_profile_kinds", curie=NIST_AI_100_1.curie('ai_rmf_profile_kinds'),
                   model_uri=NIST_AI_100_1.aiRmfProfile__ai_rmf_profile_kinds, domain=None, range=Union[Union[str, "AiRmfProfileKind"], list[Union[str, "AiRmfProfileKind"]]])

slots.aiRmfProfile__ai_rmf_profile_setting = Slot(uri=NIST_AI_100_1.ai_rmf_profile_setting, name="aiRmfProfile__ai_rmf_profile_setting", curie=NIST_AI_100_1.curie('ai_rmf_profile_setting'),
                   model_uri=NIST_AI_100_1.aiRmfProfile__ai_rmf_profile_setting, domain=None, range=Optional[str])

slots.aiRmfProfile__ai_rmf_profile_subcategories = Slot(uri=NIST_AI_100_1.ai_rmf_profile_subcategories, name="aiRmfProfile__ai_rmf_profile_subcategories", curie=NIST_AI_100_1.curie('ai_rmf_profile_subcategories'),
                   model_uri=NIST_AI_100_1.aiRmfProfile__ai_rmf_profile_subcategories, domain=None, range=Optional[Union[Union[str, AiRmfSubcategoryIdentifier], list[Union[str, AiRmfSubcategoryIdentifier]]]])

slots.AiRmfSpecificRisk_title = Slot(uri=SCHEMA.name, name="AiRmfSpecificRisk_title", curie=SCHEMA.curie('name'),
                   model_uri=NIST_AI_100_1.AiRmfSpecificRisk_title, domain=AiRmfSpecificRisk, range=str)

slots.AiRmfHumanAiIssue_title = Slot(uri=SCHEMA.name, name="AiRmfHumanAiIssue_title", curie=SCHEMA.curie('name'),
                   model_uri=NIST_AI_100_1.AiRmfHumanAiIssue_title, domain=AiRmfHumanAiIssue, range=str)

slots.AiRmfAttribute_title = Slot(uri=SCHEMA.name, name="AiRmfAttribute_title", curie=SCHEMA.curie('name'),
                   model_uri=NIST_AI_100_1.AiRmfAttribute_title, domain=AiRmfAttribute, range=str)

slots.AiRmfFunction_description = Slot(uri=SCHEMA.description, name="AiRmfFunction_description", curie=SCHEMA.curie('description'),
                   model_uri=NIST_AI_100_1.AiRmfFunction_description, domain=AiRmfFunction, range=Optional[str])

slots.AiRmfCategory_description = Slot(uri=SCHEMA.description, name="AiRmfCategory_description", curie=SCHEMA.curie('description'),
                   model_uri=NIST_AI_100_1.AiRmfCategory_description, domain=AiRmfCategory, range=str,
                   pattern=re.compile(r'^\s*\S'))

slots.AiRmfSubcategory_description = Slot(uri=SCHEMA.description, name="AiRmfSubcategory_description", curie=SCHEMA.curie('description'),
                   model_uri=NIST_AI_100_1.AiRmfSubcategory_description, domain=AiRmfSubcategory, range=str,
                   pattern=re.compile(r'^\s*\S'))

slots.AiRmfSuggestedAction_description = Slot(uri=SCHEMA.description, name="AiRmfSuggestedAction_description", curie=SCHEMA.curie('description'),
                   model_uri=NIST_AI_100_1.AiRmfSuggestedAction_description, domain=AiRmfSuggestedAction, range=str,
                   pattern=re.compile(r'^\s*\S'))

slots.AiRmfDocumentationItem_description = Slot(uri=SCHEMA.description, name="AiRmfDocumentationItem_description", curie=SCHEMA.curie('description'),
                   model_uri=NIST_AI_100_1.AiRmfDocumentationItem_description, domain=AiRmfDocumentationItem, range=str,
                   pattern=re.compile(r'^\s*\S'))

slots.AiRmfResource_title = Slot(uri=SCHEMA.name, name="AiRmfResource_title", curie=SCHEMA.curie('name'),
                   model_uri=NIST_AI_100_1.AiRmfResource_title, domain=AiRmfResource, range=str)
