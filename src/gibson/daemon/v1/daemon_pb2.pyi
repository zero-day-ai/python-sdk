import datetime

from gibson.common.v1 import gibson_common_pb2 as _gibson_common_pb2
from gibson.manifest.v1 import manifest_pb2 as _manifest_pb2
from gibson.mission.v1 import mission_definition_pb2 as _mission_definition_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from buf.validate import validate_pb2 as _validate_pb2
from gibson.auth.v1 import options_pb2 as _options_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MissionStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MISSION_STATUS_UNSPECIFIED: _ClassVar[MissionStatus]
    MISSION_STATUS_PENDING: _ClassVar[MissionStatus]
    MISSION_STATUS_RUNNING: _ClassVar[MissionStatus]
    MISSION_STATUS_PAUSED: _ClassVar[MissionStatus]
    MISSION_STATUS_COMPLETED: _ClassVar[MissionStatus]
    MISSION_STATUS_FAILED: _ClassVar[MissionStatus]
    MISSION_STATUS_CANCELLED: _ClassVar[MissionStatus]

class CheckpointSource(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CHECKPOINT_SOURCE_UNSPECIFIED: _ClassVar[CheckpointSource]
    CHECKPOINT_SOURCE_SUPER_STEP: _ClassVar[CheckpointSource]
    CHECKPOINT_SOURCE_APPROVAL_GATE: _ClassVar[CheckpointSource]
    CHECKPOINT_SOURCE_GRACEFUL_SHUTDOWN: _ClassVar[CheckpointSource]
    CHECKPOINT_SOURCE_PARALLEL_GROUP: _ClassVar[CheckpointSource]
    CHECKPOINT_SOURCE_MANUAL: _ClassVar[CheckpointSource]
MISSION_STATUS_UNSPECIFIED: MissionStatus
MISSION_STATUS_PENDING: MissionStatus
MISSION_STATUS_RUNNING: MissionStatus
MISSION_STATUS_PAUSED: MissionStatus
MISSION_STATUS_COMPLETED: MissionStatus
MISSION_STATUS_FAILED: MissionStatus
MISSION_STATUS_CANCELLED: MissionStatus
CHECKPOINT_SOURCE_UNSPECIFIED: CheckpointSource
CHECKPOINT_SOURCE_SUPER_STEP: CheckpointSource
CHECKPOINT_SOURCE_APPROVAL_GATE: CheckpointSource
CHECKPOINT_SOURCE_GRACEFUL_SHUTDOWN: CheckpointSource
CHECKPOINT_SOURCE_PARALLEL_GROUP: CheckpointSource
CHECKPOINT_SOURCE_MANUAL: CheckpointSource

class RenewCapabilityGrantRequest(_message.Message):
    __slots__ = ("agent_id", "mission_id", "task_id")
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    MISSION_ID_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    agent_id: str
    mission_id: str
    task_id: str
    def __init__(self, agent_id: _Optional[str] = ..., mission_id: _Optional[str] = ..., task_id: _Optional[str] = ...) -> None: ...

class RenewCapabilityGrantResponse(_message.Message):
    __slots__ = ("capability_grant", "expires_at_unix")
    CAPABILITY_GRANT_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_UNIX_FIELD_NUMBER: _ClassVar[int]
    capability_grant: str
    expires_at_unix: int
    def __init__(self, capability_grant: _Optional[str] = ..., expires_at_unix: _Optional[int] = ...) -> None: ...

class ConnectRequest(_message.Message):
    __slots__ = ("client_version", "client_id")
    CLIENT_VERSION_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    client_version: str
    client_id: str
    def __init__(self, client_version: _Optional[str] = ..., client_id: _Optional[str] = ...) -> None: ...

class ConnectResponse(_message.Message):
    __slots__ = ("daemon_version", "session_id", "grpc_address")
    DAEMON_VERSION_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    GRPC_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    daemon_version: str
    session_id: str
    grpc_address: str
    def __init__(self, daemon_version: _Optional[str] = ..., session_id: _Optional[str] = ..., grpc_address: _Optional[str] = ...) -> None: ...

class PingRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PingResponse(_message.Message):
    __slots__ = ("timestamp",)
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    timestamp: int
    def __init__(self, timestamp: _Optional[int] = ...) -> None: ...

class StatusRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class StatusResponse(_message.Message):
    __slots__ = ("running", "pid", "start_time", "uptime", "grpc_address", "registry_type", "registry_addr", "callback_addr", "agent_count", "mission_count", "active_mission_count")
    RUNNING_FIELD_NUMBER: _ClassVar[int]
    PID_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    UPTIME_FIELD_NUMBER: _ClassVar[int]
    GRPC_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    REGISTRY_TYPE_FIELD_NUMBER: _ClassVar[int]
    REGISTRY_ADDR_FIELD_NUMBER: _ClassVar[int]
    CALLBACK_ADDR_FIELD_NUMBER: _ClassVar[int]
    AGENT_COUNT_FIELD_NUMBER: _ClassVar[int]
    MISSION_COUNT_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_MISSION_COUNT_FIELD_NUMBER: _ClassVar[int]
    running: bool
    pid: int
    start_time: int
    uptime: str
    grpc_address: str
    registry_type: str
    registry_addr: str
    callback_addr: str
    agent_count: int
    mission_count: int
    active_mission_count: int
    def __init__(self, running: bool = ..., pid: _Optional[int] = ..., start_time: _Optional[int] = ..., uptime: _Optional[str] = ..., grpc_address: _Optional[str] = ..., registry_type: _Optional[str] = ..., registry_addr: _Optional[str] = ..., callback_addr: _Optional[str] = ..., agent_count: _Optional[int] = ..., mission_count: _Optional[int] = ..., active_mission_count: _Optional[int] = ...) -> None: ...

class OperationResult(_message.Message):
    __slots__ = ("status", "duration_ms", "started_at", "completed_at", "turns_used", "tokens_used", "nodes_executed", "nodes_failed", "findings_count", "critical_count", "high_count", "medium_count", "low_count", "error_message", "error_code")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DURATION_MS_FIELD_NUMBER: _ClassVar[int]
    STARTED_AT_FIELD_NUMBER: _ClassVar[int]
    COMPLETED_AT_FIELD_NUMBER: _ClassVar[int]
    TURNS_USED_FIELD_NUMBER: _ClassVar[int]
    TOKENS_USED_FIELD_NUMBER: _ClassVar[int]
    NODES_EXECUTED_FIELD_NUMBER: _ClassVar[int]
    NODES_FAILED_FIELD_NUMBER: _ClassVar[int]
    FINDINGS_COUNT_FIELD_NUMBER: _ClassVar[int]
    CRITICAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    HIGH_COUNT_FIELD_NUMBER: _ClassVar[int]
    MEDIUM_COUNT_FIELD_NUMBER: _ClassVar[int]
    LOW_COUNT_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ERROR_CODE_FIELD_NUMBER: _ClassVar[int]
    status: str
    duration_ms: int
    started_at: int
    completed_at: int
    turns_used: int
    tokens_used: int
    nodes_executed: int
    nodes_failed: int
    findings_count: int
    critical_count: int
    high_count: int
    medium_count: int
    low_count: int
    error_message: str
    error_code: str
    def __init__(self, status: _Optional[str] = ..., duration_ms: _Optional[int] = ..., started_at: _Optional[int] = ..., completed_at: _Optional[int] = ..., turns_used: _Optional[int] = ..., tokens_used: _Optional[int] = ..., nodes_executed: _Optional[int] = ..., nodes_failed: _Optional[int] = ..., findings_count: _Optional[int] = ..., critical_count: _Optional[int] = ..., high_count: _Optional[int] = ..., medium_count: _Optional[int] = ..., low_count: _Optional[int] = ..., error_message: _Optional[str] = ..., error_code: _Optional[str] = ...) -> None: ...

class FindingInfo(_message.Message):
    __slots__ = ("id", "title", "severity", "category", "description", "technique", "evidence", "timestamp")
    ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    SEVERITY_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TECHNIQUE_FIELD_NUMBER: _ClassVar[int]
    EVIDENCE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    id: str
    title: str
    severity: str
    category: str
    description: str
    technique: str
    evidence: str
    timestamp: int
    def __init__(self, id: _Optional[str] = ..., title: _Optional[str] = ..., severity: _Optional[str] = ..., category: _Optional[str] = ..., description: _Optional[str] = ..., technique: _Optional[str] = ..., evidence: _Optional[str] = ..., timestamp: _Optional[int] = ...) -> None: ...

class MissionEvent(_message.Message):
    __slots__ = ("event_type", "timestamp", "mission_id", "node_id", "message", "data", "error", "result")
    EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    MISSION_ID_FIELD_NUMBER: _ClassVar[int]
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    event_type: str
    timestamp: int
    mission_id: str
    node_id: str
    message: str
    data: _gibson_common_pb2.TypedMap
    error: str
    result: OperationResult
    def __init__(self, event_type: _Optional[str] = ..., timestamp: _Optional[int] = ..., mission_id: _Optional[str] = ..., node_id: _Optional[str] = ..., message: _Optional[str] = ..., data: _Optional[_Union[_gibson_common_pb2.TypedMap, _Mapping]] = ..., error: _Optional[str] = ..., result: _Optional[_Union[OperationResult, _Mapping]] = ...) -> None: ...

class AgentEvent(_message.Message):
    __slots__ = ("event_type", "timestamp", "agent_id", "agent_name", "message", "data")
    EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    AGENT_NAME_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    event_type: str
    timestamp: int
    agent_id: str
    agent_name: str
    message: str
    data: _gibson_common_pb2.TypedMap
    def __init__(self, event_type: _Optional[str] = ..., timestamp: _Optional[int] = ..., agent_id: _Optional[str] = ..., agent_name: _Optional[str] = ..., message: _Optional[str] = ..., data: _Optional[_Union[_gibson_common_pb2.TypedMap, _Mapping]] = ...) -> None: ...

class FindingEvent(_message.Message):
    __slots__ = ("event_type", "timestamp", "finding", "mission_id")
    EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    FINDING_FIELD_NUMBER: _ClassVar[int]
    MISSION_ID_FIELD_NUMBER: _ClassVar[int]
    event_type: str
    timestamp: int
    finding: FindingInfo
    mission_id: str
    def __init__(self, event_type: _Optional[str] = ..., timestamp: _Optional[int] = ..., finding: _Optional[_Union[FindingInfo, _Mapping]] = ..., mission_id: _Optional[str] = ...) -> None: ...

class ToolEvent(_message.Message):
    __slots__ = ("event_type", "timestamp", "tool_name", "agent_id", "agent_name", "mission_id", "message", "duration", "progress", "error", "error_code", "warning", "warning_severity", "data")
    EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    TOOL_NAME_FIELD_NUMBER: _ClassVar[int]
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    AGENT_NAME_FIELD_NUMBER: _ClassVar[int]
    MISSION_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ERROR_CODE_FIELD_NUMBER: _ClassVar[int]
    WARNING_FIELD_NUMBER: _ClassVar[int]
    WARNING_SEVERITY_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    event_type: str
    timestamp: int
    tool_name: str
    agent_id: str
    agent_name: str
    mission_id: str
    message: str
    duration: float
    progress: float
    error: str
    error_code: str
    warning: str
    warning_severity: str
    data: _gibson_common_pb2.TypedMap
    def __init__(self, event_type: _Optional[str] = ..., timestamp: _Optional[int] = ..., tool_name: _Optional[str] = ..., agent_id: _Optional[str] = ..., agent_name: _Optional[str] = ..., mission_id: _Optional[str] = ..., message: _Optional[str] = ..., duration: _Optional[float] = ..., progress: _Optional[float] = ..., error: _Optional[str] = ..., error_code: _Optional[str] = ..., warning: _Optional[str] = ..., warning_severity: _Optional[str] = ..., data: _Optional[_Union[_gibson_common_pb2.TypedMap, _Mapping]] = ...) -> None: ...

class LLMEvent(_message.Message):
    __slots__ = ("event_type", "timestamp", "agent_id", "agent_name", "model", "slot", "message_count", "prompt_tokens", "completion_tokens", "total_tokens", "duration_ms", "cached", "error", "error_code", "will_retry")
    EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    AGENT_NAME_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    SLOT_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_COUNT_FIELD_NUMBER: _ClassVar[int]
    PROMPT_TOKENS_FIELD_NUMBER: _ClassVar[int]
    COMPLETION_TOKENS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_TOKENS_FIELD_NUMBER: _ClassVar[int]
    DURATION_MS_FIELD_NUMBER: _ClassVar[int]
    CACHED_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ERROR_CODE_FIELD_NUMBER: _ClassVar[int]
    WILL_RETRY_FIELD_NUMBER: _ClassVar[int]
    event_type: str
    timestamp: int
    agent_id: str
    agent_name: str
    model: str
    slot: str
    message_count: int
    prompt_tokens: int
    completion_tokens: int
    total_tokens: int
    duration_ms: float
    cached: bool
    error: str
    error_code: str
    will_retry: bool
    def __init__(self, event_type: _Optional[str] = ..., timestamp: _Optional[int] = ..., agent_id: _Optional[str] = ..., agent_name: _Optional[str] = ..., model: _Optional[str] = ..., slot: _Optional[str] = ..., message_count: _Optional[int] = ..., prompt_tokens: _Optional[int] = ..., completion_tokens: _Optional[int] = ..., total_tokens: _Optional[int] = ..., duration_ms: _Optional[float] = ..., cached: bool = ..., error: _Optional[str] = ..., error_code: _Optional[str] = ..., will_retry: bool = ...) -> None: ...

class OrchestratorEvent(_message.Message):
    __slots__ = ("event_type", "timestamp", "mission_id", "iteration", "action", "target_node_id", "target_agent_name", "confidence", "reasoning", "tokens_used", "latency_ms", "approval_id", "risk", "timeout_seconds")
    EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    MISSION_ID_FIELD_NUMBER: _ClassVar[int]
    ITERATION_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    TARGET_NODE_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_AGENT_NAME_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    REASONING_FIELD_NUMBER: _ClassVar[int]
    TOKENS_USED_FIELD_NUMBER: _ClassVar[int]
    LATENCY_MS_FIELD_NUMBER: _ClassVar[int]
    APPROVAL_ID_FIELD_NUMBER: _ClassVar[int]
    RISK_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_SECONDS_FIELD_NUMBER: _ClassVar[int]
    event_type: str
    timestamp: int
    mission_id: str
    iteration: int
    action: str
    target_node_id: str
    target_agent_name: str
    confidence: float
    reasoning: str
    tokens_used: int
    latency_ms: float
    approval_id: str
    risk: str
    timeout_seconds: int
    def __init__(self, event_type: _Optional[str] = ..., timestamp: _Optional[int] = ..., mission_id: _Optional[str] = ..., iteration: _Optional[int] = ..., action: _Optional[str] = ..., target_node_id: _Optional[str] = ..., target_agent_name: _Optional[str] = ..., confidence: _Optional[float] = ..., reasoning: _Optional[str] = ..., tokens_used: _Optional[int] = ..., latency_ms: _Optional[float] = ..., approval_id: _Optional[str] = ..., risk: _Optional[str] = ..., timeout_seconds: _Optional[int] = ...) -> None: ...

class Event(_message.Message):
    __slots__ = ("event_type", "timestamp", "source", "data", "mission_event", "agent_event", "finding_event", "tool_event", "llm_event", "orchestrator_event")
    EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    MISSION_EVENT_FIELD_NUMBER: _ClassVar[int]
    AGENT_EVENT_FIELD_NUMBER: _ClassVar[int]
    FINDING_EVENT_FIELD_NUMBER: _ClassVar[int]
    TOOL_EVENT_FIELD_NUMBER: _ClassVar[int]
    LLM_EVENT_FIELD_NUMBER: _ClassVar[int]
    ORCHESTRATOR_EVENT_FIELD_NUMBER: _ClassVar[int]
    event_type: str
    timestamp: int
    source: str
    data: _gibson_common_pb2.TypedMap
    mission_event: MissionEvent
    agent_event: AgentEvent
    finding_event: FindingEvent
    tool_event: ToolEvent
    llm_event: LLMEvent
    orchestrator_event: OrchestratorEvent
    def __init__(self, event_type: _Optional[str] = ..., timestamp: _Optional[int] = ..., source: _Optional[str] = ..., data: _Optional[_Union[_gibson_common_pb2.TypedMap, _Mapping]] = ..., mission_event: _Optional[_Union[MissionEvent, _Mapping]] = ..., agent_event: _Optional[_Union[AgentEvent, _Mapping]] = ..., finding_event: _Optional[_Union[FindingEvent, _Mapping]] = ..., tool_event: _Optional[_Union[ToolEvent, _Mapping]] = ..., llm_event: _Optional[_Union[LLMEvent, _Mapping]] = ..., orchestrator_event: _Optional[_Union[OrchestratorEvent, _Mapping]] = ...) -> None: ...

class SubscribeRequest(_message.Message):
    __slots__ = ("event_types", "mission_id")
    EVENT_TYPES_FIELD_NUMBER: _ClassVar[int]
    MISSION_ID_FIELD_NUMBER: _ClassVar[int]
    event_types: _containers.RepeatedScalarFieldContainer[str]
    mission_id: str
    def __init__(self, event_types: _Optional[_Iterable[str]] = ..., mission_id: _Optional[str] = ...) -> None: ...

class SubscribeResponse(_message.Message):
    __slots__ = ("event_type", "timestamp", "source", "data", "mission_event", "agent_event", "finding_event", "tool_event", "llm_event", "orchestrator_event")
    EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    MISSION_EVENT_FIELD_NUMBER: _ClassVar[int]
    AGENT_EVENT_FIELD_NUMBER: _ClassVar[int]
    FINDING_EVENT_FIELD_NUMBER: _ClassVar[int]
    TOOL_EVENT_FIELD_NUMBER: _ClassVar[int]
    LLM_EVENT_FIELD_NUMBER: _ClassVar[int]
    ORCHESTRATOR_EVENT_FIELD_NUMBER: _ClassVar[int]
    event_type: str
    timestamp: int
    source: str
    data: _gibson_common_pb2.TypedMap
    mission_event: MissionEvent
    agent_event: AgentEvent
    finding_event: FindingEvent
    tool_event: ToolEvent
    llm_event: LLMEvent
    orchestrator_event: OrchestratorEvent
    def __init__(self, event_type: _Optional[str] = ..., timestamp: _Optional[int] = ..., source: _Optional[str] = ..., data: _Optional[_Union[_gibson_common_pb2.TypedMap, _Mapping]] = ..., mission_event: _Optional[_Union[MissionEvent, _Mapping]] = ..., agent_event: _Optional[_Union[AgentEvent, _Mapping]] = ..., finding_event: _Optional[_Union[FindingEvent, _Mapping]] = ..., tool_event: _Optional[_Union[ToolEvent, _Mapping]] = ..., llm_event: _Optional[_Union[LLMEvent, _Mapping]] = ..., orchestrator_event: _Optional[_Union[OrchestratorEvent, _Mapping]] = ...) -> None: ...

class RunMissionRequest(_message.Message):
    __slots__ = ("mission_definition_id", "target_id", "variables", "memory_continuity")
    class VariablesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    MISSION_DEFINITION_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_ID_FIELD_NUMBER: _ClassVar[int]
    VARIABLES_FIELD_NUMBER: _ClassVar[int]
    MEMORY_CONTINUITY_FIELD_NUMBER: _ClassVar[int]
    mission_definition_id: str
    target_id: str
    variables: _containers.ScalarMap[str, str]
    memory_continuity: str
    def __init__(self, mission_definition_id: _Optional[str] = ..., target_id: _Optional[str] = ..., variables: _Optional[_Mapping[str, str]] = ..., memory_continuity: _Optional[str] = ...) -> None: ...

class RunMissionResponse(_message.Message):
    __slots__ = ("event_type", "timestamp", "mission_id", "node_id", "message", "data", "error", "result")
    EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    MISSION_ID_FIELD_NUMBER: _ClassVar[int]
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    event_type: str
    timestamp: int
    mission_id: str
    node_id: str
    message: str
    data: _gibson_common_pb2.TypedMap
    error: str
    result: OperationResult
    def __init__(self, event_type: _Optional[str] = ..., timestamp: _Optional[int] = ..., mission_id: _Optional[str] = ..., node_id: _Optional[str] = ..., message: _Optional[str] = ..., data: _Optional[_Union[_gibson_common_pb2.TypedMap, _Mapping]] = ..., error: _Optional[str] = ..., result: _Optional[_Union[OperationResult, _Mapping]] = ...) -> None: ...

class ResumeMissionResponse(_message.Message):
    __slots__ = ("event_type", "timestamp", "mission_id", "node_id", "message", "data", "error", "result", "checkpoint_metadata")
    EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    MISSION_ID_FIELD_NUMBER: _ClassVar[int]
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    CHECKPOINT_METADATA_FIELD_NUMBER: _ClassVar[int]
    event_type: str
    timestamp: int
    mission_id: str
    node_id: str
    message: str
    data: _gibson_common_pb2.TypedMap
    error: str
    result: OperationResult
    checkpoint_metadata: CheckpointMetadata
    def __init__(self, event_type: _Optional[str] = ..., timestamp: _Optional[int] = ..., mission_id: _Optional[str] = ..., node_id: _Optional[str] = ..., message: _Optional[str] = ..., data: _Optional[_Union[_gibson_common_pb2.TypedMap, _Mapping]] = ..., error: _Optional[str] = ..., result: _Optional[_Union[OperationResult, _Mapping]] = ..., checkpoint_metadata: _Optional[_Union[CheckpointMetadata, _Mapping]] = ...) -> None: ...

class CheckpointMetadata(_message.Message):
    __slots__ = ("checkpoint_id", "saved_at_unix_seconds", "super_step_number", "cadence_reason", "size_bytes")
    CHECKPOINT_ID_FIELD_NUMBER: _ClassVar[int]
    SAVED_AT_UNIX_SECONDS_FIELD_NUMBER: _ClassVar[int]
    SUPER_STEP_NUMBER_FIELD_NUMBER: _ClassVar[int]
    CADENCE_REASON_FIELD_NUMBER: _ClassVar[int]
    SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    checkpoint_id: str
    saved_at_unix_seconds: int
    super_step_number: int
    cadence_reason: str
    size_bytes: int
    def __init__(self, checkpoint_id: _Optional[str] = ..., saved_at_unix_seconds: _Optional[int] = ..., super_step_number: _Optional[int] = ..., cadence_reason: _Optional[str] = ..., size_bytes: _Optional[int] = ...) -> None: ...

class StopMissionRequest(_message.Message):
    __slots__ = ("mission_id", "force")
    MISSION_ID_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    mission_id: str
    force: bool
    def __init__(self, mission_id: _Optional[str] = ..., force: bool = ...) -> None: ...

class StopMissionResponse(_message.Message):
    __slots__ = ("success", "message")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    success: bool
    message: str
    def __init__(self, success: bool = ..., message: _Optional[str] = ...) -> None: ...

class ListMissionsRequest(_message.Message):
    __slots__ = ("active_only", "limit", "offset", "status_filter", "name_pattern")
    ACTIVE_ONLY_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    STATUS_FILTER_FIELD_NUMBER: _ClassVar[int]
    NAME_PATTERN_FIELD_NUMBER: _ClassVar[int]
    active_only: bool
    limit: int
    offset: int
    status_filter: str
    name_pattern: str
    def __init__(self, active_only: bool = ..., limit: _Optional[int] = ..., offset: _Optional[int] = ..., status_filter: _Optional[str] = ..., name_pattern: _Optional[str] = ...) -> None: ...

class ListMissionsResponse(_message.Message):
    __slots__ = ("missions", "total")
    MISSIONS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    missions: _containers.RepeatedCompositeFieldContainer[MissionInfo]
    total: int
    def __init__(self, missions: _Optional[_Iterable[_Union[MissionInfo, _Mapping]]] = ..., total: _Optional[int] = ...) -> None: ...

class MissionInfo(_message.Message):
    __slots__ = ("id", "status", "start_time", "end_time", "finding_count", "name", "description", "progress", "mission_definition_id", "target_id")
    ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    FINDING_COUNT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    MISSION_DEFINITION_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    status: str
    start_time: int
    end_time: int
    finding_count: int
    name: str
    description: str
    progress: float
    mission_definition_id: str
    target_id: str
    def __init__(self, id: _Optional[str] = ..., status: _Optional[str] = ..., start_time: _Optional[int] = ..., end_time: _Optional[int] = ..., finding_count: _Optional[int] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., progress: _Optional[float] = ..., mission_definition_id: _Optional[str] = ..., target_id: _Optional[str] = ...) -> None: ...

class PauseMissionRequest(_message.Message):
    __slots__ = ("mission_id", "force")
    MISSION_ID_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    mission_id: str
    force: bool
    def __init__(self, mission_id: _Optional[str] = ..., force: bool = ...) -> None: ...

class PauseMissionResponse(_message.Message):
    __slots__ = ("success", "checkpoint_id", "message")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    CHECKPOINT_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    success: bool
    checkpoint_id: str
    message: str
    def __init__(self, success: bool = ..., checkpoint_id: _Optional[str] = ..., message: _Optional[str] = ...) -> None: ...

class ResumeMissionRequest(_message.Message):
    __slots__ = ("mission_id", "checkpoint_id", "target_checkpoint_id")
    MISSION_ID_FIELD_NUMBER: _ClassVar[int]
    CHECKPOINT_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_CHECKPOINT_ID_FIELD_NUMBER: _ClassVar[int]
    mission_id: str
    checkpoint_id: str
    target_checkpoint_id: str
    def __init__(self, mission_id: _Optional[str] = ..., checkpoint_id: _Optional[str] = ..., target_checkpoint_id: _Optional[str] = ...) -> None: ...

class GetMissionHistoryRequest(_message.Message):
    __slots__ = ("name", "limit", "offset")
    NAME_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    name: str
    limit: int
    offset: int
    def __init__(self, name: _Optional[str] = ..., limit: _Optional[int] = ..., offset: _Optional[int] = ...) -> None: ...

class GetMissionHistoryResponse(_message.Message):
    __slots__ = ("runs", "total")
    RUNS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    runs: _containers.RepeatedCompositeFieldContainer[MissionRun]
    total: int
    def __init__(self, runs: _Optional[_Iterable[_Union[MissionRun, _Mapping]]] = ..., total: _Optional[int] = ...) -> None: ...

class MissionRun(_message.Message):
    __slots__ = ("mission_id", "run_number", "status", "created_at", "completed_at", "findings_count", "previous_run_id", "trace_id")
    MISSION_ID_FIELD_NUMBER: _ClassVar[int]
    RUN_NUMBER_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    COMPLETED_AT_FIELD_NUMBER: _ClassVar[int]
    FINDINGS_COUNT_FIELD_NUMBER: _ClassVar[int]
    PREVIOUS_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    TRACE_ID_FIELD_NUMBER: _ClassVar[int]
    mission_id: str
    run_number: int
    status: str
    created_at: int
    completed_at: int
    findings_count: int
    previous_run_id: str
    trace_id: str
    def __init__(self, mission_id: _Optional[str] = ..., run_number: _Optional[int] = ..., status: _Optional[str] = ..., created_at: _Optional[int] = ..., completed_at: _Optional[int] = ..., findings_count: _Optional[int] = ..., previous_run_id: _Optional[str] = ..., trace_id: _Optional[str] = ...) -> None: ...

class GetMissionCheckpointsRequest(_message.Message):
    __slots__ = ("mission_id",)
    MISSION_ID_FIELD_NUMBER: _ClassVar[int]
    mission_id: str
    def __init__(self, mission_id: _Optional[str] = ...) -> None: ...

class GetMissionCheckpointsResponse(_message.Message):
    __slots__ = ("checkpoints",)
    CHECKPOINTS_FIELD_NUMBER: _ClassVar[int]
    checkpoints: _containers.RepeatedCompositeFieldContainer[CheckpointInfo]
    def __init__(self, checkpoints: _Optional[_Iterable[_Union[CheckpointInfo, _Mapping]]] = ...) -> None: ...

class CheckpointInfo(_message.Message):
    __slots__ = ("checkpoint_id", "created_at", "completed_nodes", "total_nodes", "findings_count", "version")
    CHECKPOINT_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    COMPLETED_NODES_FIELD_NUMBER: _ClassVar[int]
    TOTAL_NODES_FIELD_NUMBER: _ClassVar[int]
    FINDINGS_COUNT_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    checkpoint_id: str
    created_at: int
    completed_nodes: int
    total_nodes: int
    findings_count: int
    version: int
    def __init__(self, checkpoint_id: _Optional[str] = ..., created_at: _Optional[int] = ..., completed_nodes: _Optional[int] = ..., total_nodes: _Optional[int] = ..., findings_count: _Optional[int] = ..., version: _Optional[int] = ...) -> None: ...

class ListMissionDefinitionsRequest(_message.Message):
    __slots__ = ("limit", "offset")
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    limit: int
    offset: int
    def __init__(self, limit: _Optional[int] = ..., offset: _Optional[int] = ...) -> None: ...

class ListMissionDefinitionsResponse(_message.Message):
    __slots__ = ("missions", "total")
    MISSIONS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    missions: _containers.RepeatedCompositeFieldContainer[MissionDefinitionInfo]
    total: int
    def __init__(self, missions: _Optional[_Iterable[_Union[MissionDefinitionInfo, _Mapping]]] = ..., total: _Optional[int] = ...) -> None: ...

class CreateMissionDefinitionRequest(_message.Message):
    __slots__ = ("definition",)
    DEFINITION_FIELD_NUMBER: _ClassVar[int]
    definition: _mission_definition_pb2.MissionDefinition
    def __init__(self, definition: _Optional[_Union[_mission_definition_pb2.MissionDefinition, _Mapping]] = ...) -> None: ...

class CreateMissionDefinitionResponse(_message.Message):
    __slots__ = ("mission_definition_id", "info")
    MISSION_DEFINITION_ID_FIELD_NUMBER: _ClassVar[int]
    INFO_FIELD_NUMBER: _ClassVar[int]
    mission_definition_id: str
    info: MissionDefinitionInfo
    def __init__(self, mission_definition_id: _Optional[str] = ..., info: _Optional[_Union[MissionDefinitionInfo, _Mapping]] = ...) -> None: ...

class UpdateMissionDefinitionRequest(_message.Message):
    __slots__ = ("definition",)
    DEFINITION_FIELD_NUMBER: _ClassVar[int]
    definition: _mission_definition_pb2.MissionDefinition
    def __init__(self, definition: _Optional[_Union[_mission_definition_pb2.MissionDefinition, _Mapping]] = ...) -> None: ...

class UpdateMissionDefinitionResponse(_message.Message):
    __slots__ = ("mission_definition_id",)
    MISSION_DEFINITION_ID_FIELD_NUMBER: _ClassVar[int]
    mission_definition_id: str
    def __init__(self, mission_definition_id: _Optional[str] = ...) -> None: ...

class MissionDefinitionInfo(_message.Message):
    __slots__ = ("name", "version", "description", "source", "installed_at", "updated_at", "node_count")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    INSTALLED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    NODE_COUNT_FIELD_NUMBER: _ClassVar[int]
    name: str
    version: str
    description: str
    source: str
    installed_at: int
    updated_at: int
    node_count: int
    def __init__(self, name: _Optional[str] = ..., version: _Optional[str] = ..., description: _Optional[str] = ..., source: _Optional[str] = ..., installed_at: _Optional[int] = ..., updated_at: _Optional[int] = ..., node_count: _Optional[int] = ...) -> None: ...

class Mission(_message.Message):
    __slots__ = ("id", "name", "status", "target_id", "mission_definition_id", "constraints", "metrics", "checkpoint", "run_number", "created_at", "updated_at", "started_at", "completed_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TARGET_ID_FIELD_NUMBER: _ClassVar[int]
    MISSION_DEFINITION_ID_FIELD_NUMBER: _ClassVar[int]
    CONSTRAINTS_FIELD_NUMBER: _ClassVar[int]
    METRICS_FIELD_NUMBER: _ClassVar[int]
    CHECKPOINT_FIELD_NUMBER: _ClassVar[int]
    RUN_NUMBER_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    STARTED_AT_FIELD_NUMBER: _ClassVar[int]
    COMPLETED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    status: MissionStatus
    target_id: str
    mission_definition_id: str
    constraints: _mission_definition_pb2.MissionConstraints
    metrics: MissionMetrics
    checkpoint: MissionCheckpoint
    run_number: int
    created_at: int
    updated_at: int
    started_at: int
    completed_at: int
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., status: _Optional[_Union[MissionStatus, str]] = ..., target_id: _Optional[str] = ..., mission_definition_id: _Optional[str] = ..., constraints: _Optional[_Union[_mission_definition_pb2.MissionConstraints, _Mapping]] = ..., metrics: _Optional[_Union[MissionMetrics, _Mapping]] = ..., checkpoint: _Optional[_Union[MissionCheckpoint, _Mapping]] = ..., run_number: _Optional[int] = ..., created_at: _Optional[int] = ..., updated_at: _Optional[int] = ..., started_at: _Optional[int] = ..., completed_at: _Optional[int] = ...) -> None: ...

class MissionMetrics(_message.Message):
    __slots__ = ("turns_used", "nodes_executed", "nodes_failed", "findings_count", "critical_count", "high_count", "medium_count", "low_count", "tokens_used")
    TURNS_USED_FIELD_NUMBER: _ClassVar[int]
    NODES_EXECUTED_FIELD_NUMBER: _ClassVar[int]
    NODES_FAILED_FIELD_NUMBER: _ClassVar[int]
    FINDINGS_COUNT_FIELD_NUMBER: _ClassVar[int]
    CRITICAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    HIGH_COUNT_FIELD_NUMBER: _ClassVar[int]
    MEDIUM_COUNT_FIELD_NUMBER: _ClassVar[int]
    LOW_COUNT_FIELD_NUMBER: _ClassVar[int]
    TOKENS_USED_FIELD_NUMBER: _ClassVar[int]
    turns_used: int
    nodes_executed: int
    nodes_failed: int
    findings_count: int
    critical_count: int
    high_count: int
    medium_count: int
    low_count: int
    tokens_used: int
    def __init__(self, turns_used: _Optional[int] = ..., nodes_executed: _Optional[int] = ..., nodes_failed: _Optional[int] = ..., findings_count: _Optional[int] = ..., critical_count: _Optional[int] = ..., high_count: _Optional[int] = ..., medium_count: _Optional[int] = ..., low_count: _Optional[int] = ..., tokens_used: _Optional[int] = ...) -> None: ...

class MissionCheckpoint(_message.Message):
    __slots__ = ("id", "version", "completed_nodes", "total_nodes", "created_at", "state_data")
    ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    COMPLETED_NODES_FIELD_NUMBER: _ClassVar[int]
    TOTAL_NODES_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    STATE_DATA_FIELD_NUMBER: _ClassVar[int]
    id: str
    version: int
    completed_nodes: int
    total_nodes: int
    created_at: int
    state_data: bytes
    def __init__(self, id: _Optional[str] = ..., version: _Optional[int] = ..., completed_nodes: _Optional[int] = ..., total_nodes: _Optional[int] = ..., created_at: _Optional[int] = ..., state_data: _Optional[bytes] = ...) -> None: ...

class CreateMissionRequest(_message.Message):
    __slots__ = ("name", "description", "target_id", "mission_definition_id", "constraints", "metadata", "variables", "memory_continuity", "source_yaml")
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class VariablesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TARGET_ID_FIELD_NUMBER: _ClassVar[int]
    MISSION_DEFINITION_ID_FIELD_NUMBER: _ClassVar[int]
    CONSTRAINTS_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    VARIABLES_FIELD_NUMBER: _ClassVar[int]
    MEMORY_CONTINUITY_FIELD_NUMBER: _ClassVar[int]
    SOURCE_YAML_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    target_id: str
    mission_definition_id: str
    constraints: _mission_definition_pb2.MissionConstraints
    metadata: _containers.ScalarMap[str, str]
    variables: _containers.ScalarMap[str, str]
    memory_continuity: str
    source_yaml: str
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., target_id: _Optional[str] = ..., mission_definition_id: _Optional[str] = ..., constraints: _Optional[_Union[_mission_definition_pb2.MissionConstraints, _Mapping]] = ..., metadata: _Optional[_Mapping[str, str]] = ..., variables: _Optional[_Mapping[str, str]] = ..., memory_continuity: _Optional[str] = ..., source_yaml: _Optional[str] = ...) -> None: ...

class CreateMissionResponse(_message.Message):
    __slots__ = ("success", "mission", "message")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MISSION_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    success: bool
    mission: Mission
    message: str
    def __init__(self, success: bool = ..., mission: _Optional[_Union[Mission, _Mapping]] = ..., message: _Optional[str] = ...) -> None: ...

class ListAgentsRequest(_message.Message):
    __slots__ = ("kind",)
    KIND_FIELD_NUMBER: _ClassVar[int]
    kind: str
    def __init__(self, kind: _Optional[str] = ...) -> None: ...

class ListAgentsResponse(_message.Message):
    __slots__ = ("agents",)
    AGENTS_FIELD_NUMBER: _ClassVar[int]
    agents: _containers.RepeatedCompositeFieldContainer[AgentInfo]
    def __init__(self, agents: _Optional[_Iterable[_Union[AgentInfo, _Mapping]]] = ...) -> None: ...

class AgentInfo(_message.Message):
    __slots__ = ("id", "name", "kind", "version", "endpoint", "capabilities", "health", "last_seen")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    HEALTH_FIELD_NUMBER: _ClassVar[int]
    LAST_SEEN_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    kind: str
    version: str
    endpoint: str
    capabilities: _containers.RepeatedScalarFieldContainer[str]
    health: str
    last_seen: int
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., kind: _Optional[str] = ..., version: _Optional[str] = ..., endpoint: _Optional[str] = ..., capabilities: _Optional[_Iterable[str]] = ..., health: _Optional[str] = ..., last_seen: _Optional[int] = ...) -> None: ...

class GetAgentStatusRequest(_message.Message):
    __slots__ = ("agent_id",)
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    agent_id: str
    def __init__(self, agent_id: _Optional[str] = ...) -> None: ...

class GetAgentStatusResponse(_message.Message):
    __slots__ = ("agent", "active", "current_task", "task_start_time")
    AGENT_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    CURRENT_TASK_FIELD_NUMBER: _ClassVar[int]
    TASK_START_TIME_FIELD_NUMBER: _ClassVar[int]
    agent: AgentInfo
    active: bool
    current_task: str
    task_start_time: int
    def __init__(self, agent: _Optional[_Union[AgentInfo, _Mapping]] = ..., active: bool = ..., current_task: _Optional[str] = ..., task_start_time: _Optional[int] = ...) -> None: ...

class ListToolsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListToolsResponse(_message.Message):
    __slots__ = ("tools",)
    TOOLS_FIELD_NUMBER: _ClassVar[int]
    tools: _containers.RepeatedCompositeFieldContainer[ToolInfo]
    def __init__(self, tools: _Optional[_Iterable[_Union[ToolInfo, _Mapping]]] = ...) -> None: ...

class Capabilities(_message.Message):
    __slots__ = ("has_root", "has_sudo", "can_raw_socket", "features", "blocked_args", "arg_alternatives")
    class FeaturesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: bool
        def __init__(self, key: _Optional[str] = ..., value: bool = ...) -> None: ...
    class ArgAlternativesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    HAS_ROOT_FIELD_NUMBER: _ClassVar[int]
    HAS_SUDO_FIELD_NUMBER: _ClassVar[int]
    CAN_RAW_SOCKET_FIELD_NUMBER: _ClassVar[int]
    FEATURES_FIELD_NUMBER: _ClassVar[int]
    BLOCKED_ARGS_FIELD_NUMBER: _ClassVar[int]
    ARG_ALTERNATIVES_FIELD_NUMBER: _ClassVar[int]
    has_root: bool
    has_sudo: bool
    can_raw_socket: bool
    features: _containers.ScalarMap[str, bool]
    blocked_args: _containers.RepeatedScalarFieldContainer[str]
    arg_alternatives: _containers.ScalarMap[str, str]
    def __init__(self, has_root: bool = ..., has_sudo: bool = ..., can_raw_socket: bool = ..., features: _Optional[_Mapping[str, bool]] = ..., blocked_args: _Optional[_Iterable[str]] = ..., arg_alternatives: _Optional[_Mapping[str, str]] = ...) -> None: ...

class ToolInfo(_message.Message):
    __slots__ = ("id", "name", "version", "endpoint", "description", "health", "last_seen", "capabilities")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    HEALTH_FIELD_NUMBER: _ClassVar[int]
    LAST_SEEN_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    version: str
    endpoint: str
    description: str
    health: str
    last_seen: int
    capabilities: Capabilities
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., version: _Optional[str] = ..., endpoint: _Optional[str] = ..., description: _Optional[str] = ..., health: _Optional[str] = ..., last_seen: _Optional[int] = ..., capabilities: _Optional[_Union[Capabilities, _Mapping]] = ...) -> None: ...

class ListPluginsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListPluginsResponse(_message.Message):
    __slots__ = ("plugins",)
    PLUGINS_FIELD_NUMBER: _ClassVar[int]
    plugins: _containers.RepeatedCompositeFieldContainer[PluginInfo]
    def __init__(self, plugins: _Optional[_Iterable[_Union[PluginInfo, _Mapping]]] = ...) -> None: ...

class PluginInfo(_message.Message):
    __slots__ = ("id", "name", "version", "endpoint", "description", "health", "last_seen")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    HEALTH_FIELD_NUMBER: _ClassVar[int]
    LAST_SEEN_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    version: str
    endpoint: str
    description: str
    health: str
    last_seen: int
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., version: _Optional[str] = ..., endpoint: _Optional[str] = ..., description: _Optional[str] = ..., health: _Optional[str] = ..., last_seen: _Optional[int] = ...) -> None: ...

class QueryPluginRequest(_message.Message):
    __slots__ = ("name", "method", "params", "timeout_ms")
    NAME_FIELD_NUMBER: _ClassVar[int]
    METHOD_FIELD_NUMBER: _ClassVar[int]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_MS_FIELD_NUMBER: _ClassVar[int]
    name: str
    method: str
    params: _gibson_common_pb2.TypedMap
    timeout_ms: int
    def __init__(self, name: _Optional[str] = ..., method: _Optional[str] = ..., params: _Optional[_Union[_gibson_common_pb2.TypedMap, _Mapping]] = ..., timeout_ms: _Optional[int] = ...) -> None: ...

class QueryPluginResponse(_message.Message):
    __slots__ = ("result", "error", "duration_ms")
    RESULT_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    DURATION_MS_FIELD_NUMBER: _ClassVar[int]
    result: _gibson_common_pb2.TypedValue
    error: str
    duration_ms: int
    def __init__(self, result: _Optional[_Union[_gibson_common_pb2.TypedValue, _Mapping]] = ..., error: _Optional[str] = ..., duration_ms: _Optional[int] = ...) -> None: ...

class StartComponentRequest(_message.Message):
    __slots__ = ("kind", "name")
    KIND_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    kind: str
    name: str
    def __init__(self, kind: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class StartComponentResponse(_message.Message):
    __slots__ = ("success", "pid", "port", "message", "log_path")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    PID_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    LOG_PATH_FIELD_NUMBER: _ClassVar[int]
    success: bool
    pid: int
    port: int
    message: str
    log_path: str
    def __init__(self, success: bool = ..., pid: _Optional[int] = ..., port: _Optional[int] = ..., message: _Optional[str] = ..., log_path: _Optional[str] = ...) -> None: ...

class StopComponentRequest(_message.Message):
    __slots__ = ("kind", "name", "force")
    KIND_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    kind: str
    name: str
    force: bool
    def __init__(self, kind: _Optional[str] = ..., name: _Optional[str] = ..., force: bool = ...) -> None: ...

class StopComponentResponse(_message.Message):
    __slots__ = ("success", "stopped_count", "total_count", "message")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    STOPPED_COUNT_FIELD_NUMBER: _ClassVar[int]
    TOTAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    success: bool
    stopped_count: int
    total_count: int
    message: str
    def __init__(self, success: bool = ..., stopped_count: _Optional[int] = ..., total_count: _Optional[int] = ..., message: _Optional[str] = ...) -> None: ...

class BuildComponentRequest(_message.Message):
    __slots__ = ("kind", "name")
    KIND_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    kind: str
    name: str
    def __init__(self, kind: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class BuildComponentResponse(_message.Message):
    __slots__ = ("success", "stdout", "stderr", "duration_ms", "message")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    STDOUT_FIELD_NUMBER: _ClassVar[int]
    STDERR_FIELD_NUMBER: _ClassVar[int]
    DURATION_MS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    success: bool
    stdout: str
    stderr: str
    duration_ms: int
    message: str
    def __init__(self, success: bool = ..., stdout: _Optional[str] = ..., stderr: _Optional[str] = ..., duration_ms: _Optional[int] = ..., message: _Optional[str] = ...) -> None: ...

class ShowComponentRequest(_message.Message):
    __slots__ = ("kind", "name")
    KIND_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    kind: str
    name: str
    def __init__(self, kind: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class ShowComponentResponse(_message.Message):
    __slots__ = ("success", "name", "version", "kind", "status", "source", "repo_path", "bin_path", "port", "pid", "created_at", "updated_at", "started_at", "stopped_at", "manifest_info", "message")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    REPO_PATH_FIELD_NUMBER: _ClassVar[int]
    BIN_PATH_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    PID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    STARTED_AT_FIELD_NUMBER: _ClassVar[int]
    STOPPED_AT_FIELD_NUMBER: _ClassVar[int]
    MANIFEST_INFO_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    success: bool
    name: str
    version: str
    kind: str
    status: str
    source: str
    repo_path: str
    bin_path: str
    port: int
    pid: int
    created_at: int
    updated_at: int
    started_at: int
    stopped_at: int
    manifest_info: str
    message: str
    def __init__(self, success: bool = ..., name: _Optional[str] = ..., version: _Optional[str] = ..., kind: _Optional[str] = ..., status: _Optional[str] = ..., source: _Optional[str] = ..., repo_path: _Optional[str] = ..., bin_path: _Optional[str] = ..., port: _Optional[int] = ..., pid: _Optional[int] = ..., created_at: _Optional[int] = ..., updated_at: _Optional[int] = ..., started_at: _Optional[int] = ..., stopped_at: _Optional[int] = ..., manifest_info: _Optional[str] = ..., message: _Optional[str] = ...) -> None: ...

class GetComponentLogsRequest(_message.Message):
    __slots__ = ("kind", "name", "follow", "lines")
    KIND_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    FOLLOW_FIELD_NUMBER: _ClassVar[int]
    LINES_FIELD_NUMBER: _ClassVar[int]
    kind: str
    name: str
    follow: bool
    lines: int
    def __init__(self, kind: _Optional[str] = ..., name: _Optional[str] = ..., follow: bool = ..., lines: _Optional[int] = ...) -> None: ...

class LogEntry(_message.Message):
    __slots__ = ("timestamp", "level", "message", "fields")
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    timestamp: int
    level: str
    message: str
    fields: _gibson_common_pb2.TypedMap
    def __init__(self, timestamp: _Optional[int] = ..., level: _Optional[str] = ..., message: _Optional[str] = ..., fields: _Optional[_Union[_gibson_common_pb2.TypedMap, _Mapping]] = ...) -> None: ...

class GetComponentLogsResponse(_message.Message):
    __slots__ = ("timestamp", "level", "message", "fields")
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    timestamp: int
    level: str
    message: str
    fields: _gibson_common_pb2.TypedMap
    def __init__(self, timestamp: _Optional[int] = ..., level: _Optional[str] = ..., message: _Optional[str] = ..., fields: _Optional[_Union[_gibson_common_pb2.TypedMap, _Mapping]] = ...) -> None: ...

class GetMyPermissionsRequest(_message.Message):
    __slots__ = ("tenant_id",)
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    tenant_id: str
    def __init__(self, tenant_id: _Optional[str] = ...) -> None: ...

class PermissionComponentGrant(_message.Message):
    __slots__ = ("component_ref", "actions")
    COMPONENT_REF_FIELD_NUMBER: _ClassVar[int]
    ACTIONS_FIELD_NUMBER: _ClassVar[int]
    component_ref: str
    actions: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, component_ref: _Optional[str] = ..., actions: _Optional[_Iterable[str]] = ...) -> None: ...

class PermissionTeamMembership(_message.Message):
    __slots__ = ("team_id", "team_name", "is_admin")
    TEAM_ID_FIELD_NUMBER: _ClassVar[int]
    TEAM_NAME_FIELD_NUMBER: _ClassVar[int]
    IS_ADMIN_FIELD_NUMBER: _ClassVar[int]
    team_id: str
    team_name: str
    is_admin: bool
    def __init__(self, team_id: _Optional[str] = ..., team_name: _Optional[str] = ..., is_admin: bool = ...) -> None: ...

class GetMyPermissionsResponse(_message.Message):
    __slots__ = ("tenant_id", "role", "is_admin", "component_grants", "team_memberships")
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    IS_ADMIN_FIELD_NUMBER: _ClassVar[int]
    COMPONENT_GRANTS_FIELD_NUMBER: _ClassVar[int]
    TEAM_MEMBERSHIPS_FIELD_NUMBER: _ClassVar[int]
    tenant_id: str
    role: str
    is_admin: bool
    component_grants: _containers.RepeatedCompositeFieldContainer[PermissionComponentGrant]
    team_memberships: _containers.RepeatedCompositeFieldContainer[PermissionTeamMembership]
    def __init__(self, tenant_id: _Optional[str] = ..., role: _Optional[str] = ..., is_admin: bool = ..., component_grants: _Optional[_Iterable[_Union[PermissionComponentGrant, _Mapping]]] = ..., team_memberships: _Optional[_Iterable[_Union[PermissionTeamMembership, _Mapping]]] = ...) -> None: ...

class ListMyMembershipsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class Membership(_message.Message):
    __slots__ = ("tenant_id", "tenant_name", "role")
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    TENANT_NAME_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    tenant_id: str
    tenant_name: str
    role: str
    def __init__(self, tenant_id: _Optional[str] = ..., tenant_name: _Optional[str] = ..., role: _Optional[str] = ...) -> None: ...

class ListMyMembershipsResponse(_message.Message):
    __slots__ = ("memberships",)
    MEMBERSHIPS_FIELD_NUMBER: _ClassVar[int]
    memberships: _containers.RepeatedCompositeFieldContainer[Membership]
    def __init__(self, memberships: _Optional[_Iterable[_Union[Membership, _Mapping]]] = ...) -> None: ...

class GetMissionDefinitionRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class GetMissionDefinitionResponse(_message.Message):
    __slots__ = ("definition",)
    DEFINITION_FIELD_NUMBER: _ClassVar[int]
    definition: _mission_definition_pb2.MissionDefinition
    def __init__(self, definition: _Optional[_Union[_mission_definition_pb2.MissionDefinition, _Mapping]] = ...) -> None: ...

class CheckpointSummary(_message.Message):
    __slots__ = ("checkpoint_id", "mission_id", "super_step", "captured_at", "size_bytes", "source", "in_flight_idempotency", "parallel_group_id", "expires_at")
    CHECKPOINT_ID_FIELD_NUMBER: _ClassVar[int]
    MISSION_ID_FIELD_NUMBER: _ClassVar[int]
    SUPER_STEP_FIELD_NUMBER: _ClassVar[int]
    CAPTURED_AT_FIELD_NUMBER: _ClassVar[int]
    SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    IN_FLIGHT_IDEMPOTENCY_FIELD_NUMBER: _ClassVar[int]
    PARALLEL_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    checkpoint_id: str
    mission_id: str
    super_step: int
    captured_at: _timestamp_pb2.Timestamp
    size_bytes: int
    source: CheckpointSource
    in_flight_idempotency: _manifest_pb2.ToolIdempotency
    parallel_group_id: str
    expires_at: _timestamp_pb2.Timestamp
    def __init__(self, checkpoint_id: _Optional[str] = ..., mission_id: _Optional[str] = ..., super_step: _Optional[int] = ..., captured_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., size_bytes: _Optional[int] = ..., source: _Optional[_Union[CheckpointSource, str]] = ..., in_flight_idempotency: _Optional[_Union[_manifest_pb2.ToolIdempotency, str]] = ..., parallel_group_id: _Optional[str] = ..., expires_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ListCheckpointsRequest(_message.Message):
    __slots__ = ("mission_id", "page_size", "page_token", "order")
    class Order(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ORDER_UNSPECIFIED: _ClassVar[ListCheckpointsRequest.Order]
        ORDER_NEWEST_FIRST: _ClassVar[ListCheckpointsRequest.Order]
        ORDER_OLDEST_FIRST: _ClassVar[ListCheckpointsRequest.Order]
    ORDER_UNSPECIFIED: ListCheckpointsRequest.Order
    ORDER_NEWEST_FIRST: ListCheckpointsRequest.Order
    ORDER_OLDEST_FIRST: ListCheckpointsRequest.Order
    MISSION_ID_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    mission_id: str
    page_size: int
    page_token: str
    order: ListCheckpointsRequest.Order
    def __init__(self, mission_id: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., order: _Optional[_Union[ListCheckpointsRequest.Order, str]] = ...) -> None: ...

class ListCheckpointsResponse(_message.Message):
    __slots__ = ("checkpoints", "next_page_token", "total_count")
    CHECKPOINTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TOTAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    checkpoints: _containers.RepeatedCompositeFieldContainer[CheckpointSummary]
    next_page_token: str
    total_count: int
    def __init__(self, checkpoints: _Optional[_Iterable[_Union[CheckpointSummary, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., total_count: _Optional[int] = ...) -> None: ...

class GetCheckpointRequest(_message.Message):
    __slots__ = ("mission_id", "checkpoint_id", "include_blobs")
    MISSION_ID_FIELD_NUMBER: _ClassVar[int]
    CHECKPOINT_ID_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_BLOBS_FIELD_NUMBER: _ClassVar[int]
    mission_id: str
    checkpoint_id: str
    include_blobs: bool
    def __init__(self, mission_id: _Optional[str] = ..., checkpoint_id: _Optional[str] = ..., include_blobs: bool = ...) -> None: ...

class GetCheckpointResponse(_message.Message):
    __slots__ = ("checkpoint",)
    CHECKPOINT_FIELD_NUMBER: _ClassVar[int]
    checkpoint: Checkpoint
    def __init__(self, checkpoint: _Optional[_Union[Checkpoint, _Mapping]] = ...) -> None: ...

class Checkpoint(_message.Message):
    __slots__ = ("summary", "working_memory", "mission_memory", "steps", "findings", "parallel_groups")
    class ParallelGroupsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: ParallelGroupState
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[ParallelGroupState, _Mapping]] = ...) -> None: ...
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    WORKING_MEMORY_FIELD_NUMBER: _ClassVar[int]
    MISSION_MEMORY_FIELD_NUMBER: _ClassVar[int]
    STEPS_FIELD_NUMBER: _ClassVar[int]
    FINDINGS_FIELD_NUMBER: _ClassVar[int]
    PARALLEL_GROUPS_FIELD_NUMBER: _ClassVar[int]
    summary: CheckpointSummary
    working_memory: bytes
    mission_memory: bytes
    steps: _containers.RepeatedCompositeFieldContainer[DagStep]
    findings: _containers.RepeatedCompositeFieldContainer[FindingSnapshot]
    parallel_groups: _containers.MessageMap[str, ParallelGroupState]
    def __init__(self, summary: _Optional[_Union[CheckpointSummary, _Mapping]] = ..., working_memory: _Optional[bytes] = ..., mission_memory: _Optional[bytes] = ..., steps: _Optional[_Iterable[_Union[DagStep, _Mapping]]] = ..., findings: _Optional[_Iterable[_Union[FindingSnapshot, _Mapping]]] = ..., parallel_groups: _Optional[_Mapping[str, ParallelGroupState]] = ...) -> None: ...

class DagStep(_message.Message):
    __slots__ = ("node_id", "state", "started_at", "finished_at", "inputs", "outputs")
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    STARTED_AT_FIELD_NUMBER: _ClassVar[int]
    FINISHED_AT_FIELD_NUMBER: _ClassVar[int]
    INPUTS_FIELD_NUMBER: _ClassVar[int]
    OUTPUTS_FIELD_NUMBER: _ClassVar[int]
    node_id: str
    state: str
    started_at: _timestamp_pb2.Timestamp
    finished_at: _timestamp_pb2.Timestamp
    inputs: bytes
    outputs: bytes
    def __init__(self, node_id: _Optional[str] = ..., state: _Optional[str] = ..., started_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., finished_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., inputs: _Optional[bytes] = ..., outputs: _Optional[bytes] = ...) -> None: ...

class FindingSnapshot(_message.Message):
    __slots__ = ("finding_id", "severity", "payload")
    FINDING_ID_FIELD_NUMBER: _ClassVar[int]
    SEVERITY_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    finding_id: str
    severity: str
    payload: bytes
    def __init__(self, finding_id: _Optional[str] = ..., severity: _Optional[str] = ..., payload: _Optional[bytes] = ...) -> None: ...

class ParallelGroupState(_message.Message):
    __slots__ = ("group_id", "expected", "completed", "completed_node_ids")
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_FIELD_NUMBER: _ClassVar[int]
    COMPLETED_FIELD_NUMBER: _ClassVar[int]
    COMPLETED_NODE_IDS_FIELD_NUMBER: _ClassVar[int]
    group_id: str
    expected: int
    completed: int
    completed_node_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, group_id: _Optional[str] = ..., expected: _Optional[int] = ..., completed: _Optional[int] = ..., completed_node_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class BlobReference(_message.Message):
    __slots__ = ("checkpoint_id", "blob_key", "size_bytes")
    CHECKPOINT_ID_FIELD_NUMBER: _ClassVar[int]
    BLOB_KEY_FIELD_NUMBER: _ClassVar[int]
    SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    checkpoint_id: str
    blob_key: str
    size_bytes: int
    def __init__(self, checkpoint_id: _Optional[str] = ..., blob_key: _Optional[str] = ..., size_bytes: _Optional[int] = ...) -> None: ...

class DiffCheckpointsRequest(_message.Message):
    __slots__ = ("mission_id", "checkpoint_a_id", "checkpoint_b_id")
    MISSION_ID_FIELD_NUMBER: _ClassVar[int]
    CHECKPOINT_A_ID_FIELD_NUMBER: _ClassVar[int]
    CHECKPOINT_B_ID_FIELD_NUMBER: _ClassVar[int]
    mission_id: str
    checkpoint_a_id: str
    checkpoint_b_id: str
    def __init__(self, mission_id: _Optional[str] = ..., checkpoint_a_id: _Optional[str] = ..., checkpoint_b_id: _Optional[str] = ...) -> None: ...

class DiffCheckpointsResponse(_message.Message):
    __slots__ = ("diff",)
    DIFF_FIELD_NUMBER: _ClassVar[int]
    diff: CheckpointDiff
    def __init__(self, diff: _Optional[_Union[CheckpointDiff, _Mapping]] = ...) -> None: ...

class CheckpointDiff(_message.Message):
    __slots__ = ("working_memory_deltas", "mission_memory_deltas", "dag_step_deltas", "finding_deltas", "parallel_group_deltas")
    WORKING_MEMORY_DELTAS_FIELD_NUMBER: _ClassVar[int]
    MISSION_MEMORY_DELTAS_FIELD_NUMBER: _ClassVar[int]
    DAG_STEP_DELTAS_FIELD_NUMBER: _ClassVar[int]
    FINDING_DELTAS_FIELD_NUMBER: _ClassVar[int]
    PARALLEL_GROUP_DELTAS_FIELD_NUMBER: _ClassVar[int]
    working_memory_deltas: _containers.RepeatedCompositeFieldContainer[MemoryKeyDelta]
    mission_memory_deltas: _containers.RepeatedCompositeFieldContainer[MemoryKeyDelta]
    dag_step_deltas: _containers.RepeatedCompositeFieldContainer[DagStepDelta]
    finding_deltas: _containers.RepeatedCompositeFieldContainer[FindingDelta]
    parallel_group_deltas: _containers.RepeatedCompositeFieldContainer[ParallelGroupDelta]
    def __init__(self, working_memory_deltas: _Optional[_Iterable[_Union[MemoryKeyDelta, _Mapping]]] = ..., mission_memory_deltas: _Optional[_Iterable[_Union[MemoryKeyDelta, _Mapping]]] = ..., dag_step_deltas: _Optional[_Iterable[_Union[DagStepDelta, _Mapping]]] = ..., finding_deltas: _Optional[_Iterable[_Union[FindingDelta, _Mapping]]] = ..., parallel_group_deltas: _Optional[_Iterable[_Union[ParallelGroupDelta, _Mapping]]] = ...) -> None: ...

class MemoryKeyDelta(_message.Message):
    __slots__ = ("key", "op", "before", "after")
    class Op(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        OP_UNSPECIFIED: _ClassVar[MemoryKeyDelta.Op]
        OP_ADDED: _ClassVar[MemoryKeyDelta.Op]
        OP_REMOVED: _ClassVar[MemoryKeyDelta.Op]
        OP_CHANGED: _ClassVar[MemoryKeyDelta.Op]
    OP_UNSPECIFIED: MemoryKeyDelta.Op
    OP_ADDED: MemoryKeyDelta.Op
    OP_REMOVED: MemoryKeyDelta.Op
    OP_CHANGED: MemoryKeyDelta.Op
    KEY_FIELD_NUMBER: _ClassVar[int]
    OP_FIELD_NUMBER: _ClassVar[int]
    BEFORE_FIELD_NUMBER: _ClassVar[int]
    AFTER_FIELD_NUMBER: _ClassVar[int]
    key: str
    op: MemoryKeyDelta.Op
    before: bytes
    after: bytes
    def __init__(self, key: _Optional[str] = ..., op: _Optional[_Union[MemoryKeyDelta.Op, str]] = ..., before: _Optional[bytes] = ..., after: _Optional[bytes] = ...) -> None: ...

class DagStepDelta(_message.Message):
    __slots__ = ("node_id", "op", "before", "after")
    class Op(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        OP_UNSPECIFIED: _ClassVar[DagStepDelta.Op]
        OP_ADDED: _ClassVar[DagStepDelta.Op]
        OP_REMOVED: _ClassVar[DagStepDelta.Op]
        OP_CHANGED: _ClassVar[DagStepDelta.Op]
    OP_UNSPECIFIED: DagStepDelta.Op
    OP_ADDED: DagStepDelta.Op
    OP_REMOVED: DagStepDelta.Op
    OP_CHANGED: DagStepDelta.Op
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    OP_FIELD_NUMBER: _ClassVar[int]
    BEFORE_FIELD_NUMBER: _ClassVar[int]
    AFTER_FIELD_NUMBER: _ClassVar[int]
    node_id: str
    op: DagStepDelta.Op
    before: bytes
    after: bytes
    def __init__(self, node_id: _Optional[str] = ..., op: _Optional[_Union[DagStepDelta.Op, str]] = ..., before: _Optional[bytes] = ..., after: _Optional[bytes] = ...) -> None: ...

class FindingDelta(_message.Message):
    __slots__ = ("finding_id", "op", "before", "after")
    class Op(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        OP_UNSPECIFIED: _ClassVar[FindingDelta.Op]
        OP_ADDED: _ClassVar[FindingDelta.Op]
        OP_REMOVED: _ClassVar[FindingDelta.Op]
        OP_CHANGED: _ClassVar[FindingDelta.Op]
    OP_UNSPECIFIED: FindingDelta.Op
    OP_ADDED: FindingDelta.Op
    OP_REMOVED: FindingDelta.Op
    OP_CHANGED: FindingDelta.Op
    FINDING_ID_FIELD_NUMBER: _ClassVar[int]
    OP_FIELD_NUMBER: _ClassVar[int]
    BEFORE_FIELD_NUMBER: _ClassVar[int]
    AFTER_FIELD_NUMBER: _ClassVar[int]
    finding_id: str
    op: FindingDelta.Op
    before: bytes
    after: bytes
    def __init__(self, finding_id: _Optional[str] = ..., op: _Optional[_Union[FindingDelta.Op, str]] = ..., before: _Optional[bytes] = ..., after: _Optional[bytes] = ...) -> None: ...

class ParallelGroupDelta(_message.Message):
    __slots__ = ("group_id", "op", "before", "after")
    class Op(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        OP_UNSPECIFIED: _ClassVar[ParallelGroupDelta.Op]
        OP_ADDED: _ClassVar[ParallelGroupDelta.Op]
        OP_REMOVED: _ClassVar[ParallelGroupDelta.Op]
        OP_CHANGED: _ClassVar[ParallelGroupDelta.Op]
    OP_UNSPECIFIED: ParallelGroupDelta.Op
    OP_ADDED: ParallelGroupDelta.Op
    OP_REMOVED: ParallelGroupDelta.Op
    OP_CHANGED: ParallelGroupDelta.Op
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    OP_FIELD_NUMBER: _ClassVar[int]
    BEFORE_FIELD_NUMBER: _ClassVar[int]
    AFTER_FIELD_NUMBER: _ClassVar[int]
    group_id: str
    op: ParallelGroupDelta.Op
    before: bytes
    after: bytes
    def __init__(self, group_id: _Optional[str] = ..., op: _Optional[_Union[ParallelGroupDelta.Op, str]] = ..., before: _Optional[bytes] = ..., after: _Optional[bytes] = ...) -> None: ...

class CUEDiagnostic(_message.Message):
    __slots__ = ("line", "col", "message", "severity")
    LINE_FIELD_NUMBER: _ClassVar[int]
    COL_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    SEVERITY_FIELD_NUMBER: _ClassVar[int]
    line: int
    col: int
    message: str
    severity: str
    def __init__(self, line: _Optional[int] = ..., col: _Optional[int] = ..., message: _Optional[str] = ..., severity: _Optional[str] = ...) -> None: ...

class CUECompletionItem(_message.Message):
    __slots__ = ("label", "detail", "documentation", "kind")
    LABEL_FIELD_NUMBER: _ClassVar[int]
    DETAIL_FIELD_NUMBER: _ClassVar[int]
    DOCUMENTATION_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    label: str
    detail: str
    documentation: str
    kind: str
    def __init__(self, label: _Optional[str] = ..., detail: _Optional[str] = ..., documentation: _Optional[str] = ..., kind: _Optional[str] = ...) -> None: ...

class ValidateMissionCUERequest(_message.Message):
    __slots__ = ("cue_source",)
    CUE_SOURCE_FIELD_NUMBER: _ClassVar[int]
    cue_source: str
    def __init__(self, cue_source: _Optional[str] = ...) -> None: ...

class ValidateMissionCUEResponse(_message.Message):
    __slots__ = ("diagnostics", "compiled_definition")
    DIAGNOSTICS_FIELD_NUMBER: _ClassVar[int]
    COMPILED_DEFINITION_FIELD_NUMBER: _ClassVar[int]
    diagnostics: _containers.RepeatedCompositeFieldContainer[CUEDiagnostic]
    compiled_definition: _mission_definition_pb2.MissionDefinition
    def __init__(self, diagnostics: _Optional[_Iterable[_Union[CUEDiagnostic, _Mapping]]] = ..., compiled_definition: _Optional[_Union[_mission_definition_pb2.MissionDefinition, _Mapping]] = ...) -> None: ...

class CompleteMissionCUERequest(_message.Message):
    __slots__ = ("cue_source", "line", "col")
    CUE_SOURCE_FIELD_NUMBER: _ClassVar[int]
    LINE_FIELD_NUMBER: _ClassVar[int]
    COL_FIELD_NUMBER: _ClassVar[int]
    cue_source: str
    line: int
    col: int
    def __init__(self, cue_source: _Optional[str] = ..., line: _Optional[int] = ..., col: _Optional[int] = ...) -> None: ...

class CompleteMissionCUEResponse(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[CUECompletionItem]
    def __init__(self, items: _Optional[_Iterable[_Union[CUECompletionItem, _Mapping]]] = ...) -> None: ...

class HoverMissionCUERequest(_message.Message):
    __slots__ = ("cue_source", "line", "col")
    CUE_SOURCE_FIELD_NUMBER: _ClassVar[int]
    LINE_FIELD_NUMBER: _ClassVar[int]
    COL_FIELD_NUMBER: _ClassVar[int]
    cue_source: str
    line: int
    col: int
    def __init__(self, cue_source: _Optional[str] = ..., line: _Optional[int] = ..., col: _Optional[int] = ...) -> None: ...

class HoverMissionCUEResponse(_message.Message):
    __slots__ = ("markdown",)
    MARKDOWN_FIELD_NUMBER: _ClassVar[int]
    markdown: str
    def __init__(self, markdown: _Optional[str] = ...) -> None: ...
