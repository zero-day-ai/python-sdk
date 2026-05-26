from gibson.common.v1 import gibson_common_pb2 as _gibson_common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ResultStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RESULT_STATUS_UNSPECIFIED: _ClassVar[ResultStatus]
    RESULT_STATUS_SUCCESS: _ClassVar[ResultStatus]
    RESULT_STATUS_FAILED: _ClassVar[ResultStatus]
    RESULT_STATUS_PARTIAL: _ClassVar[ResultStatus]
    RESULT_STATUS_CANCELLED: _ClassVar[ResultStatus]
    RESULT_STATUS_TIMEOUT: _ClassVar[ResultStatus]

class FindingSeverity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FINDING_SEVERITY_UNSPECIFIED: _ClassVar[FindingSeverity]
    FINDING_SEVERITY_CRITICAL: _ClassVar[FindingSeverity]
    FINDING_SEVERITY_HIGH: _ClassVar[FindingSeverity]
    FINDING_SEVERITY_MEDIUM: _ClassVar[FindingSeverity]
    FINDING_SEVERITY_LOW: _ClassVar[FindingSeverity]
    FINDING_SEVERITY_INFO: _ClassVar[FindingSeverity]

class FindingStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FINDING_STATUS_UNSPECIFIED: _ClassVar[FindingStatus]
    FINDING_STATUS_OPEN: _ClassVar[FindingStatus]
    FINDING_STATUS_CONFIRMED: _ClassVar[FindingStatus]
    FINDING_STATUS_CLOSED: _ClassVar[FindingStatus]
    FINDING_STATUS_FALSE_POSITIVE: _ClassVar[FindingStatus]

class EvidenceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EVIDENCE_TYPE_UNSPECIFIED: _ClassVar[EvidenceType]
    EVIDENCE_TYPE_REQUEST: _ClassVar[EvidenceType]
    EVIDENCE_TYPE_RESPONSE: _ClassVar[EvidenceType]
    EVIDENCE_TYPE_SCREENSHOT: _ClassVar[EvidenceType]
    EVIDENCE_TYPE_CODE: _ClassVar[EvidenceType]
    EVIDENCE_TYPE_LOG: _ClassVar[EvidenceType]
    EVIDENCE_TYPE_OTHER: _ClassVar[EvidenceType]

class QueryScope(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    QUERY_SCOPE_UNSPECIFIED: _ClassVar[QueryScope]
    QUERY_SCOPE_MISSION_RUN: _ClassVar[QueryScope]
    QUERY_SCOPE_MISSION: _ClassVar[QueryScope]
    QUERY_SCOPE_GLOBAL: _ClassVar[QueryScope]
RESULT_STATUS_UNSPECIFIED: ResultStatus
RESULT_STATUS_SUCCESS: ResultStatus
RESULT_STATUS_FAILED: ResultStatus
RESULT_STATUS_PARTIAL: ResultStatus
RESULT_STATUS_CANCELLED: ResultStatus
RESULT_STATUS_TIMEOUT: ResultStatus
FINDING_SEVERITY_UNSPECIFIED: FindingSeverity
FINDING_SEVERITY_CRITICAL: FindingSeverity
FINDING_SEVERITY_HIGH: FindingSeverity
FINDING_SEVERITY_MEDIUM: FindingSeverity
FINDING_SEVERITY_LOW: FindingSeverity
FINDING_SEVERITY_INFO: FindingSeverity
FINDING_STATUS_UNSPECIFIED: FindingStatus
FINDING_STATUS_OPEN: FindingStatus
FINDING_STATUS_CONFIRMED: FindingStatus
FINDING_STATUS_CLOSED: FindingStatus
FINDING_STATUS_FALSE_POSITIVE: FindingStatus
EVIDENCE_TYPE_UNSPECIFIED: EvidenceType
EVIDENCE_TYPE_REQUEST: EvidenceType
EVIDENCE_TYPE_RESPONSE: EvidenceType
EVIDENCE_TYPE_SCREENSHOT: EvidenceType
EVIDENCE_TYPE_CODE: EvidenceType
EVIDENCE_TYPE_LOG: EvidenceType
EVIDENCE_TYPE_OTHER: EvidenceType
QUERY_SCOPE_UNSPECIFIED: QueryScope
QUERY_SCOPE_MISSION_RUN: QueryScope
QUERY_SCOPE_MISSION: QueryScope
QUERY_SCOPE_GLOBAL: QueryScope

class Task(_message.Message):
    __slots__ = ("id", "goal", "context", "constraints", "metadata")
    class ContextEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _gibson_common_pb2.TypedValue
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_gibson_common_pb2.TypedValue, _Mapping]] = ...) -> None: ...
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _gibson_common_pb2.TypedValue
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_gibson_common_pb2.TypedValue, _Mapping]] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    GOAL_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    CONSTRAINTS_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    id: str
    goal: str
    context: _containers.MessageMap[str, _gibson_common_pb2.TypedValue]
    constraints: TaskConstraints
    metadata: _containers.MessageMap[str, _gibson_common_pb2.TypedValue]
    def __init__(self, id: _Optional[str] = ..., goal: _Optional[str] = ..., context: _Optional[_Mapping[str, _gibson_common_pb2.TypedValue]] = ..., constraints: _Optional[_Union[TaskConstraints, _Mapping]] = ..., metadata: _Optional[_Mapping[str, _gibson_common_pb2.TypedValue]] = ...) -> None: ...

class TaskConstraints(_message.Message):
    __slots__ = ("max_turns", "max_tokens", "allowed_tools", "blocked_tools")
    MAX_TURNS_FIELD_NUMBER: _ClassVar[int]
    MAX_TOKENS_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_TOOLS_FIELD_NUMBER: _ClassVar[int]
    BLOCKED_TOOLS_FIELD_NUMBER: _ClassVar[int]
    max_turns: int
    max_tokens: int
    allowed_tools: _containers.RepeatedScalarFieldContainer[str]
    blocked_tools: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, max_turns: _Optional[int] = ..., max_tokens: _Optional[int] = ..., allowed_tools: _Optional[_Iterable[str]] = ..., blocked_tools: _Optional[_Iterable[str]] = ...) -> None: ...

class Result(_message.Message):
    __slots__ = ("status", "output", "finding_ids", "metadata", "error")
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _gibson_common_pb2.TypedValue
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_gibson_common_pb2.TypedValue, _Mapping]] = ...) -> None: ...
    STATUS_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_FIELD_NUMBER: _ClassVar[int]
    FINDING_IDS_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    status: ResultStatus
    output: _gibson_common_pb2.TypedValue
    finding_ids: _containers.RepeatedScalarFieldContainer[str]
    metadata: _containers.MessageMap[str, _gibson_common_pb2.TypedValue]
    error: ResultError
    def __init__(self, status: _Optional[_Union[ResultStatus, str]] = ..., output: _Optional[_Union[_gibson_common_pb2.TypedValue, _Mapping]] = ..., finding_ids: _Optional[_Iterable[str]] = ..., metadata: _Optional[_Mapping[str, _gibson_common_pb2.TypedValue]] = ..., error: _Optional[_Union[ResultError, _Mapping]] = ...) -> None: ...

class ResultError(_message.Message):
    __slots__ = ("code", "message", "details", "retryable")
    class DetailsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    CODE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    RETRYABLE_FIELD_NUMBER: _ClassVar[int]
    code: _gibson_common_pb2.ErrorCode
    message: str
    details: _containers.ScalarMap[str, str]
    retryable: bool
    def __init__(self, code: _Optional[_Union[_gibson_common_pb2.ErrorCode, str]] = ..., message: _Optional[str] = ..., details: _Optional[_Mapping[str, str]] = ..., retryable: bool = ...) -> None: ...

class Finding(_message.Message):
    __slots__ = ("id", "mission_id", "agent_name", "delegated_from", "title", "description", "category", "subcategory", "severity", "confidence", "status", "mitre_attack", "mitre_atlas", "evidence", "reproduction", "cvss_score", "risk_score", "remediation", "references", "target_id", "technique", "tags", "created_at", "updated_at", "compliance_mappings")
    ID_FIELD_NUMBER: _ClassVar[int]
    MISSION_ID_FIELD_NUMBER: _ClassVar[int]
    AGENT_NAME_FIELD_NUMBER: _ClassVar[int]
    DELEGATED_FROM_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    SUBCATEGORY_FIELD_NUMBER: _ClassVar[int]
    SEVERITY_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MITRE_ATTACK_FIELD_NUMBER: _ClassVar[int]
    MITRE_ATLAS_FIELD_NUMBER: _ClassVar[int]
    EVIDENCE_FIELD_NUMBER: _ClassVar[int]
    REPRODUCTION_FIELD_NUMBER: _ClassVar[int]
    CVSS_SCORE_FIELD_NUMBER: _ClassVar[int]
    RISK_SCORE_FIELD_NUMBER: _ClassVar[int]
    REMEDIATION_FIELD_NUMBER: _ClassVar[int]
    REFERENCES_FIELD_NUMBER: _ClassVar[int]
    TARGET_ID_FIELD_NUMBER: _ClassVar[int]
    TECHNIQUE_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    COMPLIANCE_MAPPINGS_FIELD_NUMBER: _ClassVar[int]
    id: str
    mission_id: str
    agent_name: str
    delegated_from: str
    title: str
    description: str
    category: str
    subcategory: str
    severity: FindingSeverity
    confidence: float
    status: FindingStatus
    mitre_attack: MitreMapping
    mitre_atlas: MitreMapping
    evidence: _containers.RepeatedCompositeFieldContainer[Evidence]
    reproduction: _containers.RepeatedCompositeFieldContainer[ReproStep]
    cvss_score: float
    risk_score: float
    remediation: str
    references: _containers.RepeatedScalarFieldContainer[str]
    target_id: str
    technique: str
    tags: _containers.RepeatedScalarFieldContainer[str]
    created_at: int
    updated_at: int
    compliance_mappings: _containers.RepeatedCompositeFieldContainer[ComplianceMapping]
    def __init__(self, id: _Optional[str] = ..., mission_id: _Optional[str] = ..., agent_name: _Optional[str] = ..., delegated_from: _Optional[str] = ..., title: _Optional[str] = ..., description: _Optional[str] = ..., category: _Optional[str] = ..., subcategory: _Optional[str] = ..., severity: _Optional[_Union[FindingSeverity, str]] = ..., confidence: _Optional[float] = ..., status: _Optional[_Union[FindingStatus, str]] = ..., mitre_attack: _Optional[_Union[MitreMapping, _Mapping]] = ..., mitre_atlas: _Optional[_Union[MitreMapping, _Mapping]] = ..., evidence: _Optional[_Iterable[_Union[Evidence, _Mapping]]] = ..., reproduction: _Optional[_Iterable[_Union[ReproStep, _Mapping]]] = ..., cvss_score: _Optional[float] = ..., risk_score: _Optional[float] = ..., remediation: _Optional[str] = ..., references: _Optional[_Iterable[str]] = ..., target_id: _Optional[str] = ..., technique: _Optional[str] = ..., tags: _Optional[_Iterable[str]] = ..., created_at: _Optional[int] = ..., updated_at: _Optional[int] = ..., compliance_mappings: _Optional[_Iterable[_Union[ComplianceMapping, _Mapping]]] = ...) -> None: ...

class ComplianceMapping(_message.Message):
    __slots__ = ("framework", "control_id", "rationale", "evidence_ref")
    FRAMEWORK_FIELD_NUMBER: _ClassVar[int]
    CONTROL_ID_FIELD_NUMBER: _ClassVar[int]
    RATIONALE_FIELD_NUMBER: _ClassVar[int]
    EVIDENCE_REF_FIELD_NUMBER: _ClassVar[int]
    framework: str
    control_id: str
    rationale: str
    evidence_ref: str
    def __init__(self, framework: _Optional[str] = ..., control_id: _Optional[str] = ..., rationale: _Optional[str] = ..., evidence_ref: _Optional[str] = ...) -> None: ...

class MitreMapping(_message.Message):
    __slots__ = ("matrix", "tactic_id", "tactic_name", "technique_id", "technique_name", "sub_techniques")
    MATRIX_FIELD_NUMBER: _ClassVar[int]
    TACTIC_ID_FIELD_NUMBER: _ClassVar[int]
    TACTIC_NAME_FIELD_NUMBER: _ClassVar[int]
    TECHNIQUE_ID_FIELD_NUMBER: _ClassVar[int]
    TECHNIQUE_NAME_FIELD_NUMBER: _ClassVar[int]
    SUB_TECHNIQUES_FIELD_NUMBER: _ClassVar[int]
    matrix: str
    tactic_id: str
    tactic_name: str
    technique_id: str
    technique_name: str
    sub_techniques: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, matrix: _Optional[str] = ..., tactic_id: _Optional[str] = ..., tactic_name: _Optional[str] = ..., technique_id: _Optional[str] = ..., technique_name: _Optional[str] = ..., sub_techniques: _Optional[_Iterable[str]] = ...) -> None: ...

class Evidence(_message.Message):
    __slots__ = ("title", "type", "content", "metadata")
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    TITLE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    title: str
    type: EvidenceType
    content: str
    metadata: _containers.ScalarMap[str, str]
    def __init__(self, title: _Optional[str] = ..., type: _Optional[_Union[EvidenceType, str]] = ..., content: _Optional[str] = ..., metadata: _Optional[_Mapping[str, str]] = ...) -> None: ...

class ReproStep(_message.Message):
    __slots__ = ("order", "description", "input", "output")
    ORDER_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    INPUT_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_FIELD_NUMBER: _ClassVar[int]
    order: int
    description: str
    input: str
    output: str
    def __init__(self, order: _Optional[int] = ..., description: _Optional[str] = ..., input: _Optional[str] = ..., output: _Optional[str] = ...) -> None: ...

class GraphQuery(_message.Message):
    __slots__ = ("text", "embedding", "top_k", "node_types", "min_score", "max_score", "mission_id", "mission_run_id", "scope", "filters", "vector_weight", "graph_weight")
    class FiltersEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    TEXT_FIELD_NUMBER: _ClassVar[int]
    EMBEDDING_FIELD_NUMBER: _ClassVar[int]
    TOP_K_FIELD_NUMBER: _ClassVar[int]
    NODE_TYPES_FIELD_NUMBER: _ClassVar[int]
    MIN_SCORE_FIELD_NUMBER: _ClassVar[int]
    MAX_SCORE_FIELD_NUMBER: _ClassVar[int]
    MISSION_ID_FIELD_NUMBER: _ClassVar[int]
    MISSION_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    VECTOR_WEIGHT_FIELD_NUMBER: _ClassVar[int]
    GRAPH_WEIGHT_FIELD_NUMBER: _ClassVar[int]
    text: str
    embedding: _containers.RepeatedScalarFieldContainer[float]
    top_k: int
    node_types: _containers.RepeatedScalarFieldContainer[str]
    min_score: float
    max_score: float
    mission_id: str
    mission_run_id: str
    scope: QueryScope
    filters: _containers.ScalarMap[str, str]
    vector_weight: float
    graph_weight: float
    def __init__(self, text: _Optional[str] = ..., embedding: _Optional[_Iterable[float]] = ..., top_k: _Optional[int] = ..., node_types: _Optional[_Iterable[str]] = ..., min_score: _Optional[float] = ..., max_score: _Optional[float] = ..., mission_id: _Optional[str] = ..., mission_run_id: _Optional[str] = ..., scope: _Optional[_Union[QueryScope, str]] = ..., filters: _Optional[_Mapping[str, str]] = ..., vector_weight: _Optional[float] = ..., graph_weight: _Optional[float] = ...) -> None: ...
