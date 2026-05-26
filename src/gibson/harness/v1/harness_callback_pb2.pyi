from gibson.common.v1 import gibson_common_pb2 as _gibson_common_pb2
from gibson.types.v1 import types_pb2 as _types_pb2
from gibson.graphrag.v1 import graphrag_pb2 as _graphrag_pb2
from gibson.mission.v1 import mission_definition_pb2 as _mission_definition_pb2
from gibson.auth.v1 import options_pb2 as _options_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MemoryTier(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MEMORY_TIER_UNSPECIFIED: _ClassVar[MemoryTier]
    MEMORY_TIER_WORKING: _ClassVar[MemoryTier]
    MEMORY_TIER_MISSION: _ClassVar[MemoryTier]
    MEMORY_TIER_LONG_TERM: _ClassVar[MemoryTier]

class SpanKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SPAN_KIND_UNSPECIFIED: _ClassVar[SpanKind]
    SPAN_KIND_INTERNAL: _ClassVar[SpanKind]
    SPAN_KIND_SERVER: _ClassVar[SpanKind]
    SPAN_KIND_CLIENT: _ClassVar[SpanKind]
    SPAN_KIND_PRODUCER: _ClassVar[SpanKind]
    SPAN_KIND_CONSUMER: _ClassVar[SpanKind]

class StatusCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    STATUS_CODE_UNSPECIFIED: _ClassVar[StatusCode]
    STATUS_CODE_OK: _ClassVar[StatusCode]
    STATUS_CODE_ERROR: _ClassVar[StatusCode]

class CredentialType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CREDENTIAL_TYPE_UNSPECIFIED: _ClassVar[CredentialType]
    CREDENTIAL_TYPE_API_KEY: _ClassVar[CredentialType]
    CREDENTIAL_TYPE_BEARER: _ClassVar[CredentialType]
    CREDENTIAL_TYPE_BASIC: _ClassVar[CredentialType]
    CREDENTIAL_TYPE_OAUTH: _ClassVar[CredentialType]
    CREDENTIAL_TYPE_CUSTOM: _ClassVar[CredentialType]

class MissionStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MISSION_STATUS_UNSPECIFIED: _ClassVar[MissionStatus]
    MISSION_STATUS_PENDING: _ClassVar[MissionStatus]
    MISSION_STATUS_RUNNING: _ClassVar[MissionStatus]
    MISSION_STATUS_PAUSED: _ClassVar[MissionStatus]
    MISSION_STATUS_COMPLETED: _ClassVar[MissionStatus]
    MISSION_STATUS_FAILED: _ClassVar[MissionStatus]
    MISSION_STATUS_CANCELLED: _ClassVar[MissionStatus]
MEMORY_TIER_UNSPECIFIED: MemoryTier
MEMORY_TIER_WORKING: MemoryTier
MEMORY_TIER_MISSION: MemoryTier
MEMORY_TIER_LONG_TERM: MemoryTier
SPAN_KIND_UNSPECIFIED: SpanKind
SPAN_KIND_INTERNAL: SpanKind
SPAN_KIND_SERVER: SpanKind
SPAN_KIND_CLIENT: SpanKind
SPAN_KIND_PRODUCER: SpanKind
SPAN_KIND_CONSUMER: SpanKind
STATUS_CODE_UNSPECIFIED: StatusCode
STATUS_CODE_OK: StatusCode
STATUS_CODE_ERROR: StatusCode
CREDENTIAL_TYPE_UNSPECIFIED: CredentialType
CREDENTIAL_TYPE_API_KEY: CredentialType
CREDENTIAL_TYPE_BEARER: CredentialType
CREDENTIAL_TYPE_BASIC: CredentialType
CREDENTIAL_TYPE_OAUTH: CredentialType
CREDENTIAL_TYPE_CUSTOM: CredentialType
MISSION_STATUS_UNSPECIFIED: MissionStatus
MISSION_STATUS_PENDING: MissionStatus
MISSION_STATUS_RUNNING: MissionStatus
MISSION_STATUS_PAUSED: MissionStatus
MISSION_STATUS_COMPLETED: MissionStatus
MISSION_STATUS_FAILED: MissionStatus
MISSION_STATUS_CANCELLED: MissionStatus

class HarnessError(_message.Message):
    __slots__ = ("code", "message", "retryable")
    CODE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    RETRYABLE_FIELD_NUMBER: _ClassVar[int]
    code: _gibson_common_pb2.ErrorCode
    message: str
    retryable: bool
    def __init__(self, code: _Optional[_Union[_gibson_common_pb2.ErrorCode, str]] = ..., message: _Optional[str] = ..., retryable: bool = ...) -> None: ...

class HarnessHealthStatus(_message.Message):
    __slots__ = ("state", "message", "checked_at")
    STATE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    CHECKED_AT_FIELD_NUMBER: _ClassVar[int]
    state: str
    message: str
    checked_at: int
    def __init__(self, state: _Optional[str] = ..., message: _Optional[str] = ..., checked_at: _Optional[int] = ...) -> None: ...

class ContextInfo(_message.Message):
    __slots__ = ("task_id", "agent_name", "trace_id", "span_id", "mission_id", "mission_run_id", "agent_run_id", "run_number", "tool_execution_id")
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    AGENT_NAME_FIELD_NUMBER: _ClassVar[int]
    TRACE_ID_FIELD_NUMBER: _ClassVar[int]
    SPAN_ID_FIELD_NUMBER: _ClassVar[int]
    MISSION_ID_FIELD_NUMBER: _ClassVar[int]
    MISSION_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    AGENT_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    RUN_NUMBER_FIELD_NUMBER: _ClassVar[int]
    TOOL_EXECUTION_ID_FIELD_NUMBER: _ClassVar[int]
    task_id: str
    agent_name: str
    trace_id: str
    span_id: str
    mission_id: str
    mission_run_id: str
    agent_run_id: str
    run_number: int
    tool_execution_id: str
    def __init__(self, task_id: _Optional[str] = ..., agent_name: _Optional[str] = ..., trace_id: _Optional[str] = ..., span_id: _Optional[str] = ..., mission_id: _Optional[str] = ..., mission_run_id: _Optional[str] = ..., agent_run_id: _Optional[str] = ..., run_number: _Optional[int] = ..., tool_execution_id: _Optional[str] = ...) -> None: ...

class TokenUsage(_message.Message):
    __slots__ = ("input_tokens", "output_tokens", "total_tokens")
    INPUT_TOKENS_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_TOKENS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_TOKENS_FIELD_NUMBER: _ClassVar[int]
    input_tokens: int
    output_tokens: int
    total_tokens: int
    def __init__(self, input_tokens: _Optional[int] = ..., output_tokens: _Optional[int] = ..., total_tokens: _Optional[int] = ...) -> None: ...

class LLMMessage(_message.Message):
    __slots__ = ("role", "content", "tool_calls", "tool_results", "name")
    ROLE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    TOOL_CALLS_FIELD_NUMBER: _ClassVar[int]
    TOOL_RESULTS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    role: str
    content: str
    tool_calls: _containers.RepeatedCompositeFieldContainer[ToolCall]
    tool_results: _containers.RepeatedCompositeFieldContainer[ToolResult]
    name: str
    def __init__(self, role: _Optional[str] = ..., content: _Optional[str] = ..., tool_calls: _Optional[_Iterable[_Union[ToolCall, _Mapping]]] = ..., tool_results: _Optional[_Iterable[_Union[ToolResult, _Mapping]]] = ..., name: _Optional[str] = ...) -> None: ...

class ToolCall(_message.Message):
    __slots__ = ("id", "name", "arguments")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ARGUMENTS_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    arguments: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., arguments: _Optional[str] = ...) -> None: ...

class ToolResult(_message.Message):
    __slots__ = ("tool_call_id", "content", "is_error")
    TOOL_CALL_ID_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    IS_ERROR_FIELD_NUMBER: _ClassVar[int]
    tool_call_id: str
    content: str
    is_error: bool
    def __init__(self, tool_call_id: _Optional[str] = ..., content: _Optional[str] = ..., is_error: bool = ...) -> None: ...

class ToolDef(_message.Message):
    __slots__ = ("name", "description", "parameters")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    parameters: JSONSchemaNode
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., parameters: _Optional[_Union[JSONSchemaNode, _Mapping]] = ...) -> None: ...

class LLMCompleteRequest(_message.Message):
    __slots__ = ("context", "slot", "messages", "temperature", "max_tokens", "top_p", "stop")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    SLOT_FIELD_NUMBER: _ClassVar[int]
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
    MAX_TOKENS_FIELD_NUMBER: _ClassVar[int]
    TOP_P_FIELD_NUMBER: _ClassVar[int]
    STOP_FIELD_NUMBER: _ClassVar[int]
    context: ContextInfo
    slot: str
    messages: _containers.RepeatedCompositeFieldContainer[LLMMessage]
    temperature: float
    max_tokens: int
    top_p: float
    stop: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, context: _Optional[_Union[ContextInfo, _Mapping]] = ..., slot: _Optional[str] = ..., messages: _Optional[_Iterable[_Union[LLMMessage, _Mapping]]] = ..., temperature: _Optional[float] = ..., max_tokens: _Optional[int] = ..., top_p: _Optional[float] = ..., stop: _Optional[_Iterable[str]] = ...) -> None: ...

class LLMCompleteWithToolsRequest(_message.Message):
    __slots__ = ("context", "slot", "messages", "tools")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    SLOT_FIELD_NUMBER: _ClassVar[int]
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    TOOLS_FIELD_NUMBER: _ClassVar[int]
    context: ContextInfo
    slot: str
    messages: _containers.RepeatedCompositeFieldContainer[LLMMessage]
    tools: _containers.RepeatedCompositeFieldContainer[ToolDef]
    def __init__(self, context: _Optional[_Union[ContextInfo, _Mapping]] = ..., slot: _Optional[str] = ..., messages: _Optional[_Iterable[_Union[LLMMessage, _Mapping]]] = ..., tools: _Optional[_Iterable[_Union[ToolDef, _Mapping]]] = ...) -> None: ...

class LLMCompleteStructuredRequest(_message.Message):
    __slots__ = ("context", "slot", "messages", "schema_json")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    SLOT_FIELD_NUMBER: _ClassVar[int]
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_JSON_FIELD_NUMBER: _ClassVar[int]
    context: ContextInfo
    slot: str
    messages: _containers.RepeatedCompositeFieldContainer[LLMMessage]
    schema_json: str
    def __init__(self, context: _Optional[_Union[ContextInfo, _Mapping]] = ..., slot: _Optional[str] = ..., messages: _Optional[_Iterable[_Union[LLMMessage, _Mapping]]] = ..., schema_json: _Optional[str] = ...) -> None: ...

class LLMCompleteStructuredResponse(_message.Message):
    __slots__ = ("result", "usage", "error")
    RESULT_FIELD_NUMBER: _ClassVar[int]
    USAGE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    result: _gibson_common_pb2.TypedValue
    usage: TokenUsage
    error: HarnessError
    def __init__(self, result: _Optional[_Union[_gibson_common_pb2.TypedValue, _Mapping]] = ..., usage: _Optional[_Union[TokenUsage, _Mapping]] = ..., error: _Optional[_Union[HarnessError, _Mapping]] = ...) -> None: ...

class LLMCompleteResponse(_message.Message):
    __slots__ = ("content", "tool_calls", "finish_reason", "usage", "error")
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    TOOL_CALLS_FIELD_NUMBER: _ClassVar[int]
    FINISH_REASON_FIELD_NUMBER: _ClassVar[int]
    USAGE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    content: str
    tool_calls: _containers.RepeatedCompositeFieldContainer[ToolCall]
    finish_reason: str
    usage: TokenUsage
    error: HarnessError
    def __init__(self, content: _Optional[str] = ..., tool_calls: _Optional[_Iterable[_Union[ToolCall, _Mapping]]] = ..., finish_reason: _Optional[str] = ..., usage: _Optional[_Union[TokenUsage, _Mapping]] = ..., error: _Optional[_Union[HarnessError, _Mapping]] = ...) -> None: ...

class LLMCompleteWithToolsResponse(_message.Message):
    __slots__ = ("content", "tool_calls", "finish_reason", "usage", "error")
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    TOOL_CALLS_FIELD_NUMBER: _ClassVar[int]
    FINISH_REASON_FIELD_NUMBER: _ClassVar[int]
    USAGE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    content: str
    tool_calls: _containers.RepeatedCompositeFieldContainer[ToolCall]
    finish_reason: str
    usage: TokenUsage
    error: HarnessError
    def __init__(self, content: _Optional[str] = ..., tool_calls: _Optional[_Iterable[_Union[ToolCall, _Mapping]]] = ..., finish_reason: _Optional[str] = ..., usage: _Optional[_Union[TokenUsage, _Mapping]] = ..., error: _Optional[_Union[HarnessError, _Mapping]] = ...) -> None: ...

class LLMStreamRequest(_message.Message):
    __slots__ = ("context", "slot", "messages", "temperature", "max_tokens", "top_p", "stop")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    SLOT_FIELD_NUMBER: _ClassVar[int]
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
    MAX_TOKENS_FIELD_NUMBER: _ClassVar[int]
    TOP_P_FIELD_NUMBER: _ClassVar[int]
    STOP_FIELD_NUMBER: _ClassVar[int]
    context: ContextInfo
    slot: str
    messages: _containers.RepeatedCompositeFieldContainer[LLMMessage]
    temperature: float
    max_tokens: int
    top_p: float
    stop: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, context: _Optional[_Union[ContextInfo, _Mapping]] = ..., slot: _Optional[str] = ..., messages: _Optional[_Iterable[_Union[LLMMessage, _Mapping]]] = ..., temperature: _Optional[float] = ..., max_tokens: _Optional[int] = ..., top_p: _Optional[float] = ..., stop: _Optional[_Iterable[str]] = ...) -> None: ...

class LLMStreamResponse(_message.Message):
    __slots__ = ("delta", "tool_calls", "finish_reason", "usage", "error")
    DELTA_FIELD_NUMBER: _ClassVar[int]
    TOOL_CALLS_FIELD_NUMBER: _ClassVar[int]
    FINISH_REASON_FIELD_NUMBER: _ClassVar[int]
    USAGE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    delta: str
    tool_calls: _containers.RepeatedCompositeFieldContainer[ToolCall]
    finish_reason: str
    usage: TokenUsage
    error: HarnessError
    def __init__(self, delta: _Optional[str] = ..., tool_calls: _Optional[_Iterable[_Union[ToolCall, _Mapping]]] = ..., finish_reason: _Optional[str] = ..., usage: _Optional[_Union[TokenUsage, _Mapping]] = ..., error: _Optional[_Union[HarnessError, _Mapping]] = ...) -> None: ...

class CallToolProtoRequest(_message.Message):
    __slots__ = ("context", "name", "input_json", "input_type", "output_type")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    INPUT_JSON_FIELD_NUMBER: _ClassVar[int]
    INPUT_TYPE_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_TYPE_FIELD_NUMBER: _ClassVar[int]
    context: ContextInfo
    name: str
    input_json: bytes
    input_type: str
    output_type: str
    def __init__(self, context: _Optional[_Union[ContextInfo, _Mapping]] = ..., name: _Optional[str] = ..., input_json: _Optional[bytes] = ..., input_type: _Optional[str] = ..., output_type: _Optional[str] = ...) -> None: ...

class CallToolProtoResponse(_message.Message):
    __slots__ = ("output_json", "error")
    OUTPUT_JSON_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    output_json: bytes
    error: HarnessError
    def __init__(self, output_json: _Optional[bytes] = ..., error: _Optional[_Union[HarnessError, _Mapping]] = ...) -> None: ...

class CallToolProtoStreamRequest(_message.Message):
    __slots__ = ("context", "name", "input_json", "input_type", "output_type", "timeout_ms")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    INPUT_JSON_FIELD_NUMBER: _ClassVar[int]
    INPUT_TYPE_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_TYPE_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_MS_FIELD_NUMBER: _ClassVar[int]
    context: ContextInfo
    name: str
    input_json: bytes
    input_type: str
    output_type: str
    timeout_ms: int
    def __init__(self, context: _Optional[_Union[ContextInfo, _Mapping]] = ..., name: _Optional[str] = ..., input_json: _Optional[bytes] = ..., input_type: _Optional[str] = ..., output_type: _Optional[str] = ..., timeout_ms: _Optional[int] = ...) -> None: ...

class CallToolProtoStreamResponse(_message.Message):
    __slots__ = ("progress", "partial", "warning", "complete", "error", "trace_id", "span_id", "sequence", "timestamp_ms")
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    PARTIAL_FIELD_NUMBER: _ClassVar[int]
    WARNING_FIELD_NUMBER: _ClassVar[int]
    COMPLETE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    TRACE_ID_FIELD_NUMBER: _ClassVar[int]
    SPAN_ID_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_MS_FIELD_NUMBER: _ClassVar[int]
    progress: ToolProgressEvent
    partial: ToolPartialResultEvent
    warning: ToolWarningEvent
    complete: ToolCompleteEvent
    error: ToolErrorEvent
    trace_id: str
    span_id: str
    sequence: int
    timestamp_ms: int
    def __init__(self, progress: _Optional[_Union[ToolProgressEvent, _Mapping]] = ..., partial: _Optional[_Union[ToolPartialResultEvent, _Mapping]] = ..., warning: _Optional[_Union[ToolWarningEvent, _Mapping]] = ..., complete: _Optional[_Union[ToolCompleteEvent, _Mapping]] = ..., error: _Optional[_Union[ToolErrorEvent, _Mapping]] = ..., trace_id: _Optional[str] = ..., span_id: _Optional[str] = ..., sequence: _Optional[int] = ..., timestamp_ms: _Optional[int] = ...) -> None: ...

class ToolProgressEvent(_message.Message):
    __slots__ = ("percent", "stage", "message")
    PERCENT_FIELD_NUMBER: _ClassVar[int]
    STAGE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    percent: int
    stage: str
    message: str
    def __init__(self, percent: _Optional[int] = ..., stage: _Optional[str] = ..., message: _Optional[str] = ...) -> None: ...

class ToolPartialResultEvent(_message.Message):
    __slots__ = ("output_json", "description")
    OUTPUT_JSON_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    output_json: bytes
    description: str
    def __init__(self, output_json: _Optional[bytes] = ..., description: _Optional[str] = ...) -> None: ...

class ToolWarningEvent(_message.Message):
    __slots__ = ("message", "code")
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    message: str
    code: str
    def __init__(self, message: _Optional[str] = ..., code: _Optional[str] = ...) -> None: ...

class ToolCompleteEvent(_message.Message):
    __slots__ = ("output_json",)
    OUTPUT_JSON_FIELD_NUMBER: _ClassVar[int]
    output_json: bytes
    def __init__(self, output_json: _Optional[bytes] = ...) -> None: ...

class ToolErrorEvent(_message.Message):
    __slots__ = ("error", "fatal")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    FATAL_FIELD_NUMBER: _ClassVar[int]
    error: HarnessError
    fatal: bool
    def __init__(self, error: _Optional[_Union[HarnessError, _Mapping]] = ..., fatal: bool = ...) -> None: ...

class ListToolsRequest(_message.Message):
    __slots__ = ("context",)
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    context: ContextInfo
    def __init__(self, context: _Optional[_Union[ContextInfo, _Mapping]] = ...) -> None: ...

class ListToolsResponse(_message.Message):
    __slots__ = ("tools", "error")
    TOOLS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    tools: _containers.RepeatedCompositeFieldContainer[HarnessToolDescriptor]
    error: HarnessError
    def __init__(self, tools: _Optional[_Iterable[_Union[HarnessToolDescriptor, _Mapping]]] = ..., error: _Optional[_Union[HarnessError, _Mapping]] = ...) -> None: ...

class HarnessToolDescriptor(_message.Message):
    __slots__ = ("name", "description", "input_schema", "output_schema")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    INPUT_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    input_schema: JSONSchemaNode
    output_schema: JSONSchemaNode
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., input_schema: _Optional[_Union[JSONSchemaNode, _Mapping]] = ..., output_schema: _Optional[_Union[JSONSchemaNode, _Mapping]] = ...) -> None: ...

class QueueToolWorkRequest(_message.Message):
    __slots__ = ("context", "tool_name", "input_jsons", "input_type", "output_type")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    TOOL_NAME_FIELD_NUMBER: _ClassVar[int]
    INPUT_JSONS_FIELD_NUMBER: _ClassVar[int]
    INPUT_TYPE_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_TYPE_FIELD_NUMBER: _ClassVar[int]
    context: ContextInfo
    tool_name: str
    input_jsons: _containers.RepeatedScalarFieldContainer[str]
    input_type: str
    output_type: str
    def __init__(self, context: _Optional[_Union[ContextInfo, _Mapping]] = ..., tool_name: _Optional[str] = ..., input_jsons: _Optional[_Iterable[str]] = ..., input_type: _Optional[str] = ..., output_type: _Optional[str] = ...) -> None: ...

class QueueToolWorkResponse(_message.Message):
    __slots__ = ("job_id", "error")
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    job_id: str
    error: HarnessError
    def __init__(self, job_id: _Optional[str] = ..., error: _Optional[_Union[HarnessError, _Mapping]] = ...) -> None: ...

class ToolResultsRequest(_message.Message):
    __slots__ = ("context", "job_id")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    context: ContextInfo
    job_id: str
    def __init__(self, context: _Optional[_Union[ContextInfo, _Mapping]] = ..., job_id: _Optional[str] = ...) -> None: ...

class ToolResultsResponse(_message.Message):
    __slots__ = ("index", "output_json", "output_type", "error", "is_final")
    INDEX_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_JSON_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_TYPE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    IS_FINAL_FIELD_NUMBER: _ClassVar[int]
    index: int
    output_json: str
    output_type: str
    error: HarnessError
    is_final: bool
    def __init__(self, index: _Optional[int] = ..., output_json: _Optional[str] = ..., output_type: _Optional[str] = ..., error: _Optional[_Union[HarnessError, _Mapping]] = ..., is_final: bool = ...) -> None: ...

class JSONSchemaNode(_message.Message):
    __slots__ = ("type", "description", "properties", "required", "items", "enum_values", "format", "minimum", "maximum", "min_length", "max_length", "min_items", "max_items", "pattern", "default_value", "nullable", "taxonomy")
    class PropertiesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: JSONSchemaNode
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[JSONSchemaNode, _Mapping]] = ...) -> None: ...
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    ENUM_VALUES_FIELD_NUMBER: _ClassVar[int]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    MINIMUM_FIELD_NUMBER: _ClassVar[int]
    MAXIMUM_FIELD_NUMBER: _ClassVar[int]
    MIN_LENGTH_FIELD_NUMBER: _ClassVar[int]
    MAX_LENGTH_FIELD_NUMBER: _ClassVar[int]
    MIN_ITEMS_FIELD_NUMBER: _ClassVar[int]
    MAX_ITEMS_FIELD_NUMBER: _ClassVar[int]
    PATTERN_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_VALUE_FIELD_NUMBER: _ClassVar[int]
    NULLABLE_FIELD_NUMBER: _ClassVar[int]
    TAXONOMY_FIELD_NUMBER: _ClassVar[int]
    type: str
    description: str
    properties: _containers.MessageMap[str, JSONSchemaNode]
    required: _containers.RepeatedScalarFieldContainer[str]
    items: JSONSchemaNode
    enum_values: _containers.RepeatedScalarFieldContainer[str]
    format: str
    minimum: float
    maximum: float
    min_length: int
    max_length: int
    min_items: int
    max_items: int
    pattern: str
    default_value: str
    nullable: bool
    taxonomy: TaxonomyMapping
    def __init__(self, type: _Optional[str] = ..., description: _Optional[str] = ..., properties: _Optional[_Mapping[str, JSONSchemaNode]] = ..., required: _Optional[_Iterable[str]] = ..., items: _Optional[_Union[JSONSchemaNode, _Mapping]] = ..., enum_values: _Optional[_Iterable[str]] = ..., format: _Optional[str] = ..., minimum: _Optional[float] = ..., maximum: _Optional[float] = ..., min_length: _Optional[int] = ..., max_length: _Optional[int] = ..., min_items: _Optional[int] = ..., max_items: _Optional[int] = ..., pattern: _Optional[str] = ..., default_value: _Optional[str] = ..., nullable: bool = ..., taxonomy: _Optional[_Union[TaxonomyMapping, _Mapping]] = ...) -> None: ...

class TaxonomyMapping(_message.Message):
    __slots__ = ("node_type", "identifying_properties", "properties", "relationships")
    class IdentifyingPropertiesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NODE_TYPE_FIELD_NUMBER: _ClassVar[int]
    IDENTIFYING_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    RELATIONSHIPS_FIELD_NUMBER: _ClassVar[int]
    node_type: str
    identifying_properties: _containers.ScalarMap[str, str]
    properties: _containers.RepeatedCompositeFieldContainer[PropertyMapping]
    relationships: _containers.RepeatedCompositeFieldContainer[RelationshipMapping]
    def __init__(self, node_type: _Optional[str] = ..., identifying_properties: _Optional[_Mapping[str, str]] = ..., properties: _Optional[_Iterable[_Union[PropertyMapping, _Mapping]]] = ..., relationships: _Optional[_Iterable[_Union[RelationshipMapping, _Mapping]]] = ...) -> None: ...

class PropertyMapping(_message.Message):
    __slots__ = ("source", "target", "default_value", "transform")
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_VALUE_FIELD_NUMBER: _ClassVar[int]
    TRANSFORM_FIELD_NUMBER: _ClassVar[int]
    source: str
    target: str
    default_value: str
    transform: str
    def __init__(self, source: _Optional[str] = ..., target: _Optional[str] = ..., default_value: _Optional[str] = ..., transform: _Optional[str] = ...) -> None: ...

class NodeReference(_message.Message):
    __slots__ = ("type", "properties")
    class PropertiesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    TYPE_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    type: str
    properties: _containers.ScalarMap[str, str]
    def __init__(self, type: _Optional[str] = ..., properties: _Optional[_Mapping[str, str]] = ...) -> None: ...

class RelationshipMapping(_message.Message):
    __slots__ = ("type", "to", "condition", "rel_properties")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    FROM_FIELD_NUMBER: _ClassVar[int]
    TO_FIELD_NUMBER: _ClassVar[int]
    CONDITION_FIELD_NUMBER: _ClassVar[int]
    REL_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    type: str
    to: NodeReference
    condition: str
    rel_properties: _containers.RepeatedCompositeFieldContainer[PropertyMapping]
    def __init__(self, type: _Optional[str] = ..., to: _Optional[_Union[NodeReference, _Mapping]] = ..., condition: _Optional[str] = ..., rel_properties: _Optional[_Iterable[_Union[PropertyMapping, _Mapping]]] = ..., **kwargs) -> None: ...

class QueryPluginRequest(_message.Message):
    __slots__ = ("context", "name", "method", "params")
    class ParamsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _gibson_common_pb2.TypedValue
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_gibson_common_pb2.TypedValue, _Mapping]] = ...) -> None: ...
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    METHOD_FIELD_NUMBER: _ClassVar[int]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    context: ContextInfo
    name: str
    method: str
    params: _containers.MessageMap[str, _gibson_common_pb2.TypedValue]
    def __init__(self, context: _Optional[_Union[ContextInfo, _Mapping]] = ..., name: _Optional[str] = ..., method: _Optional[str] = ..., params: _Optional[_Mapping[str, _gibson_common_pb2.TypedValue]] = ...) -> None: ...

class QueryPluginResponse(_message.Message):
    __slots__ = ("result", "error")
    RESULT_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    result: _gibson_common_pb2.TypedValue
    error: HarnessError
    def __init__(self, result: _Optional[_Union[_gibson_common_pb2.TypedValue, _Mapping]] = ..., error: _Optional[_Union[HarnessError, _Mapping]] = ...) -> None: ...

class ListPluginsRequest(_message.Message):
    __slots__ = ("context",)
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    context: ContextInfo
    def __init__(self, context: _Optional[_Union[ContextInfo, _Mapping]] = ...) -> None: ...

class ListPluginsResponse(_message.Message):
    __slots__ = ("plugins", "error")
    PLUGINS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    plugins: _containers.RepeatedCompositeFieldContainer[HarnessPluginDescriptor]
    error: HarnessError
    def __init__(self, plugins: _Optional[_Iterable[_Union[HarnessPluginDescriptor, _Mapping]]] = ..., error: _Optional[_Union[HarnessError, _Mapping]] = ...) -> None: ...

class HarnessPluginDescriptor(_message.Message):
    __slots__ = ("name", "description", "version", "methods")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    METHODS_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    version: str
    methods: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., version: _Optional[str] = ..., methods: _Optional[_Iterable[str]] = ...) -> None: ...

class DelegateToAgentRequest(_message.Message):
    __slots__ = ("context", "name", "task")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TASK_FIELD_NUMBER: _ClassVar[int]
    context: ContextInfo
    name: str
    task: _types_pb2.Task
    def __init__(self, context: _Optional[_Union[ContextInfo, _Mapping]] = ..., name: _Optional[str] = ..., task: _Optional[_Union[_types_pb2.Task, _Mapping]] = ...) -> None: ...

class DelegateToAgentResponse(_message.Message):
    __slots__ = ("result", "error")
    RESULT_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    result: _types_pb2.Result
    error: HarnessError
    def __init__(self, result: _Optional[_Union[_types_pb2.Result, _Mapping]] = ..., error: _Optional[_Union[HarnessError, _Mapping]] = ...) -> None: ...

class ListAgentsRequest(_message.Message):
    __slots__ = ("context",)
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    context: ContextInfo
    def __init__(self, context: _Optional[_Union[ContextInfo, _Mapping]] = ...) -> None: ...

class ListAgentsResponse(_message.Message):
    __slots__ = ("agents", "error")
    AGENTS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    agents: _containers.RepeatedCompositeFieldContainer[HarnessAgentDescriptor]
    error: HarnessError
    def __init__(self, agents: _Optional[_Iterable[_Union[HarnessAgentDescriptor, _Mapping]]] = ..., error: _Optional[_Union[HarnessError, _Mapping]] = ...) -> None: ...

class HarnessAgentDescriptor(_message.Message):
    __slots__ = ("name", "version", "description", "capabilities", "target_types", "technique_types")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    TARGET_TYPES_FIELD_NUMBER: _ClassVar[int]
    TECHNIQUE_TYPES_FIELD_NUMBER: _ClassVar[int]
    name: str
    version: str
    description: str
    capabilities: _containers.RepeatedScalarFieldContainer[str]
    target_types: _containers.RepeatedScalarFieldContainer[str]
    technique_types: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, name: _Optional[str] = ..., version: _Optional[str] = ..., description: _Optional[str] = ..., capabilities: _Optional[_Iterable[str]] = ..., target_types: _Optional[_Iterable[str]] = ..., technique_types: _Optional[_Iterable[str]] = ...) -> None: ...

class SubmitFindingRequest(_message.Message):
    __slots__ = ("context", "finding")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    FINDING_FIELD_NUMBER: _ClassVar[int]
    context: ContextInfo
    finding: _types_pb2.Finding
    def __init__(self, context: _Optional[_Union[ContextInfo, _Mapping]] = ..., finding: _Optional[_Union[_types_pb2.Finding, _Mapping]] = ...) -> None: ...

class SubmitFindingResponse(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: HarnessError
    def __init__(self, error: _Optional[_Union[HarnessError, _Mapping]] = ...) -> None: ...

class GetFindingsRequest(_message.Message):
    __slots__ = ("context", "filter")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    context: ContextInfo
    filter: FindingFilter
    def __init__(self, context: _Optional[_Union[ContextInfo, _Mapping]] = ..., filter: _Optional[_Union[FindingFilter, _Mapping]] = ...) -> None: ...

class GetFindingsResponse(_message.Message):
    __slots__ = ("findings", "error")
    FINDINGS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    findings: _containers.RepeatedCompositeFieldContainer[_types_pb2.Finding]
    error: HarnessError
    def __init__(self, findings: _Optional[_Iterable[_Union[_types_pb2.Finding, _Mapping]]] = ..., error: _Optional[_Union[HarnessError, _Mapping]] = ...) -> None: ...

class FindingFilter(_message.Message):
    __slots__ = ("mission_id", "agent_name", "severity", "status", "tags")
    MISSION_ID_FIELD_NUMBER: _ClassVar[int]
    AGENT_NAME_FIELD_NUMBER: _ClassVar[int]
    SEVERITY_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    mission_id: str
    agent_name: str
    severity: _types_pb2.FindingSeverity
    status: _types_pb2.FindingStatus
    tags: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, mission_id: _Optional[str] = ..., agent_name: _Optional[str] = ..., severity: _Optional[_Union[_types_pb2.FindingSeverity, str]] = ..., status: _Optional[_Union[_types_pb2.FindingStatus, str]] = ..., tags: _Optional[_Iterable[str]] = ...) -> None: ...

class MemoryGetRequest(_message.Message):
    __slots__ = ("context", "key", "tier")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    TIER_FIELD_NUMBER: _ClassVar[int]
    context: ContextInfo
    key: str
    tier: MemoryTier
    def __init__(self, context: _Optional[_Union[ContextInfo, _Mapping]] = ..., key: _Optional[str] = ..., tier: _Optional[_Union[MemoryTier, str]] = ...) -> None: ...

class MemoryGetResponse(_message.Message):
    __slots__ = ("value", "found", "error", "metadata", "created_at", "updated_at")
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _gibson_common_pb2.TypedValue
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_gibson_common_pb2.TypedValue, _Mapping]] = ...) -> None: ...
    VALUE_FIELD_NUMBER: _ClassVar[int]
    FOUND_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    value: _gibson_common_pb2.TypedValue
    found: bool
    error: HarnessError
    metadata: _containers.MessageMap[str, _gibson_common_pb2.TypedValue]
    created_at: str
    updated_at: str
    def __init__(self, value: _Optional[_Union[_gibson_common_pb2.TypedValue, _Mapping]] = ..., found: bool = ..., error: _Optional[_Union[HarnessError, _Mapping]] = ..., metadata: _Optional[_Mapping[str, _gibson_common_pb2.TypedValue]] = ..., created_at: _Optional[str] = ..., updated_at: _Optional[str] = ...) -> None: ...

class MemorySetRequest(_message.Message):
    __slots__ = ("context", "key", "value", "tier", "metadata")
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _gibson_common_pb2.TypedValue
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_gibson_common_pb2.TypedValue, _Mapping]] = ...) -> None: ...
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    TIER_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    context: ContextInfo
    key: str
    value: _gibson_common_pb2.TypedValue
    tier: MemoryTier
    metadata: _containers.MessageMap[str, _gibson_common_pb2.TypedValue]
    def __init__(self, context: _Optional[_Union[ContextInfo, _Mapping]] = ..., key: _Optional[str] = ..., value: _Optional[_Union[_gibson_common_pb2.TypedValue, _Mapping]] = ..., tier: _Optional[_Union[MemoryTier, str]] = ..., metadata: _Optional[_Mapping[str, _gibson_common_pb2.TypedValue]] = ...) -> None: ...

class MemorySetResponse(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: HarnessError
    def __init__(self, error: _Optional[_Union[HarnessError, _Mapping]] = ...) -> None: ...

class MemoryDeleteRequest(_message.Message):
    __slots__ = ("context", "key", "tier")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    TIER_FIELD_NUMBER: _ClassVar[int]
    context: ContextInfo
    key: str
    tier: MemoryTier
    def __init__(self, context: _Optional[_Union[ContextInfo, _Mapping]] = ..., key: _Optional[str] = ..., tier: _Optional[_Union[MemoryTier, str]] = ...) -> None: ...

class MemoryDeleteResponse(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: HarnessError
    def __init__(self, error: _Optional[_Union[HarnessError, _Mapping]] = ...) -> None: ...

class MemoryListRequest(_message.Message):
    __slots__ = ("context", "prefix", "tier")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    PREFIX_FIELD_NUMBER: _ClassVar[int]
    TIER_FIELD_NUMBER: _ClassVar[int]
    context: ContextInfo
    prefix: str
    tier: MemoryTier
    def __init__(self, context: _Optional[_Union[ContextInfo, _Mapping]] = ..., prefix: _Optional[str] = ..., tier: _Optional[_Union[MemoryTier, str]] = ...) -> None: ...

class MemoryListResponse(_message.Message):
    __slots__ = ("keys", "error")
    KEYS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    keys: _containers.RepeatedScalarFieldContainer[str]
    error: HarnessError
    def __init__(self, keys: _Optional[_Iterable[str]] = ..., error: _Optional[_Union[HarnessError, _Mapping]] = ...) -> None: ...

class MissionMemorySearchRequest(_message.Message):
    __slots__ = ("context", "query", "limit")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    context: ContextInfo
    query: str
    limit: int
    def __init__(self, context: _Optional[_Union[ContextInfo, _Mapping]] = ..., query: _Optional[str] = ..., limit: _Optional[int] = ...) -> None: ...

class MissionMemorySearchResponse(_message.Message):
    __slots__ = ("results", "error")
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[MissionMemoryResult]
    error: HarnessError
    def __init__(self, results: _Optional[_Iterable[_Union[MissionMemoryResult, _Mapping]]] = ..., error: _Optional[_Union[HarnessError, _Mapping]] = ...) -> None: ...

class MissionMemoryResult(_message.Message):
    __slots__ = ("key", "value", "metadata", "score", "created_at", "updated_at")
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _gibson_common_pb2.TypedValue
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_gibson_common_pb2.TypedValue, _Mapping]] = ...) -> None: ...
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    key: str
    value: _gibson_common_pb2.TypedValue
    metadata: _containers.MessageMap[str, _gibson_common_pb2.TypedValue]
    score: float
    created_at: str
    updated_at: str
    def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_gibson_common_pb2.TypedValue, _Mapping]] = ..., metadata: _Optional[_Mapping[str, _gibson_common_pb2.TypedValue]] = ..., score: _Optional[float] = ..., created_at: _Optional[str] = ..., updated_at: _Optional[str] = ...) -> None: ...

class MissionMemoryHistoryRequest(_message.Message):
    __slots__ = ("context", "limit")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    context: ContextInfo
    limit: int
    def __init__(self, context: _Optional[_Union[ContextInfo, _Mapping]] = ..., limit: _Optional[int] = ...) -> None: ...

class MissionMemoryHistoryResponse(_message.Message):
    __slots__ = ("items", "error")
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[MissionMemoryItem]
    error: HarnessError
    def __init__(self, items: _Optional[_Iterable[_Union[MissionMemoryItem, _Mapping]]] = ..., error: _Optional[_Union[HarnessError, _Mapping]] = ...) -> None: ...

class MissionMemoryItem(_message.Message):
    __slots__ = ("key", "value", "metadata", "created_at", "updated_at")
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _gibson_common_pb2.TypedValue
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_gibson_common_pb2.TypedValue, _Mapping]] = ...) -> None: ...
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    key: str
    value: _gibson_common_pb2.TypedValue
    metadata: _containers.MessageMap[str, _gibson_common_pb2.TypedValue]
    created_at: str
    updated_at: str
    def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_gibson_common_pb2.TypedValue, _Mapping]] = ..., metadata: _Optional[_Mapping[str, _gibson_common_pb2.TypedValue]] = ..., created_at: _Optional[str] = ..., updated_at: _Optional[str] = ...) -> None: ...

class MissionMemoryGetPreviousRunValueRequest(_message.Message):
    __slots__ = ("context", "key")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    context: ContextInfo
    key: str
    def __init__(self, context: _Optional[_Union[ContextInfo, _Mapping]] = ..., key: _Optional[str] = ...) -> None: ...

class MissionMemoryGetPreviousRunValueResponse(_message.Message):
    __slots__ = ("value", "found", "error")
    VALUE_FIELD_NUMBER: _ClassVar[int]
    FOUND_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    value: _gibson_common_pb2.TypedValue
    found: bool
    error: HarnessError
    def __init__(self, value: _Optional[_Union[_gibson_common_pb2.TypedValue, _Mapping]] = ..., found: bool = ..., error: _Optional[_Union[HarnessError, _Mapping]] = ...) -> None: ...

class MissionMemoryGetValueHistoryRequest(_message.Message):
    __slots__ = ("context", "key")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    context: ContextInfo
    key: str
    def __init__(self, context: _Optional[_Union[ContextInfo, _Mapping]] = ..., key: _Optional[str] = ...) -> None: ...

class MissionMemoryGetValueHistoryResponse(_message.Message):
    __slots__ = ("values", "error")
    VALUES_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedCompositeFieldContainer[HistoricalValueItem]
    error: HarnessError
    def __init__(self, values: _Optional[_Iterable[_Union[HistoricalValueItem, _Mapping]]] = ..., error: _Optional[_Union[HarnessError, _Mapping]] = ...) -> None: ...

class HistoricalValueItem(_message.Message):
    __slots__ = ("value", "run_number", "mission_id", "stored_at")
    VALUE_FIELD_NUMBER: _ClassVar[int]
    RUN_NUMBER_FIELD_NUMBER: _ClassVar[int]
    MISSION_ID_FIELD_NUMBER: _ClassVar[int]
    STORED_AT_FIELD_NUMBER: _ClassVar[int]
    value: _gibson_common_pb2.TypedValue
    run_number: int
    mission_id: str
    stored_at: str
    def __init__(self, value: _Optional[_Union[_gibson_common_pb2.TypedValue, _Mapping]] = ..., run_number: _Optional[int] = ..., mission_id: _Optional[str] = ..., stored_at: _Optional[str] = ...) -> None: ...

class MissionMemoryContinuityModeRequest(_message.Message):
    __slots__ = ("context",)
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    context: ContextInfo
    def __init__(self, context: _Optional[_Union[ContextInfo, _Mapping]] = ...) -> None: ...

class MissionMemoryContinuityModeResponse(_message.Message):
    __slots__ = ("mode", "error")
    MODE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    mode: str
    error: HarnessError
    def __init__(self, mode: _Optional[str] = ..., error: _Optional[_Union[HarnessError, _Mapping]] = ...) -> None: ...

class LongTermMemoryStoreRequest(_message.Message):
    __slots__ = ("context", "content", "metadata")
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _gibson_common_pb2.TypedValue
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_gibson_common_pb2.TypedValue, _Mapping]] = ...) -> None: ...
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    context: ContextInfo
    content: str
    metadata: _containers.MessageMap[str, _gibson_common_pb2.TypedValue]
    def __init__(self, context: _Optional[_Union[ContextInfo, _Mapping]] = ..., content: _Optional[str] = ..., metadata: _Optional[_Mapping[str, _gibson_common_pb2.TypedValue]] = ...) -> None: ...

class LongTermMemoryStoreResponse(_message.Message):
    __slots__ = ("id", "error")
    ID_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    id: str
    error: HarnessError
    def __init__(self, id: _Optional[str] = ..., error: _Optional[_Union[HarnessError, _Mapping]] = ...) -> None: ...

class LongTermMemorySearchRequest(_message.Message):
    __slots__ = ("context", "query", "top_k", "filters")
    class FiltersEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _gibson_common_pb2.TypedValue
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_gibson_common_pb2.TypedValue, _Mapping]] = ...) -> None: ...
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    TOP_K_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    context: ContextInfo
    query: str
    top_k: int
    filters: _containers.MessageMap[str, _gibson_common_pb2.TypedValue]
    def __init__(self, context: _Optional[_Union[ContextInfo, _Mapping]] = ..., query: _Optional[str] = ..., top_k: _Optional[int] = ..., filters: _Optional[_Mapping[str, _gibson_common_pb2.TypedValue]] = ...) -> None: ...

class LongTermMemorySearchResponse(_message.Message):
    __slots__ = ("results", "error")
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[LongTermMemoryResult]
    error: HarnessError
    def __init__(self, results: _Optional[_Iterable[_Union[LongTermMemoryResult, _Mapping]]] = ..., error: _Optional[_Union[HarnessError, _Mapping]] = ...) -> None: ...

class LongTermMemoryResult(_message.Message):
    __slots__ = ("id", "content", "metadata", "score", "created_at")
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _gibson_common_pb2.TypedValue
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_gibson_common_pb2.TypedValue, _Mapping]] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    content: str
    metadata: _containers.MessageMap[str, _gibson_common_pb2.TypedValue]
    score: float
    created_at: str
    def __init__(self, id: _Optional[str] = ..., content: _Optional[str] = ..., metadata: _Optional[_Mapping[str, _gibson_common_pb2.TypedValue]] = ..., score: _Optional[float] = ..., created_at: _Optional[str] = ...) -> None: ...

class LongTermMemoryDeleteRequest(_message.Message):
    __slots__ = ("context", "id")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    context: ContextInfo
    id: str
    def __init__(self, context: _Optional[_Union[ContextInfo, _Mapping]] = ..., id: _Optional[str] = ...) -> None: ...

class LongTermMemoryDeleteResponse(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: HarnessError
    def __init__(self, error: _Optional[_Union[HarnessError, _Mapping]] = ...) -> None: ...

class GraphRAGQueryRequest(_message.Message):
    __slots__ = ("context", "query")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    context: ContextInfo
    query: _types_pb2.GraphQuery
    def __init__(self, context: _Optional[_Union[ContextInfo, _Mapping]] = ..., query: _Optional[_Union[_types_pb2.GraphQuery, _Mapping]] = ...) -> None: ...

class GraphRAGQueryResponse(_message.Message):
    __slots__ = ("results", "error")
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[GraphRAGResult]
    error: HarnessError
    def __init__(self, results: _Optional[_Iterable[_Union[GraphRAGResult, _Mapping]]] = ..., error: _Optional[_Union[HarnessError, _Mapping]] = ...) -> None: ...

class GraphRAGResult(_message.Message):
    __slots__ = ("node", "score", "vector_score", "graph_score", "path", "distance")
    NODE_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    VECTOR_SCORE_FIELD_NUMBER: _ClassVar[int]
    GRAPH_SCORE_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    DISTANCE_FIELD_NUMBER: _ClassVar[int]
    node: GraphNode
    score: float
    vector_score: float
    graph_score: float
    path: _containers.RepeatedScalarFieldContainer[str]
    distance: int
    def __init__(self, node: _Optional[_Union[GraphNode, _Mapping]] = ..., score: _Optional[float] = ..., vector_score: _Optional[float] = ..., graph_score: _Optional[float] = ..., path: _Optional[_Iterable[str]] = ..., distance: _Optional[int] = ...) -> None: ...

class GraphNode(_message.Message):
    __slots__ = ("id", "type", "properties", "content", "mission_id", "agent_name", "created_at", "updated_at")
    class PropertiesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _gibson_common_pb2.TypedValue
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_gibson_common_pb2.TypedValue, _Mapping]] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    MISSION_ID_FIELD_NUMBER: _ClassVar[int]
    AGENT_NAME_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    type: str
    properties: _containers.MessageMap[str, _gibson_common_pb2.TypedValue]
    content: str
    mission_id: str
    agent_name: str
    created_at: int
    updated_at: int
    def __init__(self, id: _Optional[str] = ..., type: _Optional[str] = ..., properties: _Optional[_Mapping[str, _gibson_common_pb2.TypedValue]] = ..., content: _Optional[str] = ..., mission_id: _Optional[str] = ..., agent_name: _Optional[str] = ..., created_at: _Optional[int] = ..., updated_at: _Optional[int] = ...) -> None: ...

class FindSimilarAttacksRequest(_message.Message):
    __slots__ = ("context", "content", "top_k")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    TOP_K_FIELD_NUMBER: _ClassVar[int]
    context: ContextInfo
    content: str
    top_k: int
    def __init__(self, context: _Optional[_Union[ContextInfo, _Mapping]] = ..., content: _Optional[str] = ..., top_k: _Optional[int] = ...) -> None: ...

class FindSimilarAttacksResponse(_message.Message):
    __slots__ = ("attacks", "error")
    ATTACKS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    attacks: _containers.RepeatedCompositeFieldContainer[AttackPattern]
    error: HarnessError
    def __init__(self, attacks: _Optional[_Iterable[_Union[AttackPattern, _Mapping]]] = ..., error: _Optional[_Union[HarnessError, _Mapping]] = ...) -> None: ...

class AttackPattern(_message.Message):
    __slots__ = ("technique_id", "name", "description", "tactics", "platforms", "similarity")
    TECHNIQUE_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TACTICS_FIELD_NUMBER: _ClassVar[int]
    PLATFORMS_FIELD_NUMBER: _ClassVar[int]
    SIMILARITY_FIELD_NUMBER: _ClassVar[int]
    technique_id: str
    name: str
    description: str
    tactics: _containers.RepeatedScalarFieldContainer[str]
    platforms: _containers.RepeatedScalarFieldContainer[str]
    similarity: float
    def __init__(self, technique_id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., tactics: _Optional[_Iterable[str]] = ..., platforms: _Optional[_Iterable[str]] = ..., similarity: _Optional[float] = ...) -> None: ...

class FindSimilarFindingsRequest(_message.Message):
    __slots__ = ("context", "finding_id", "top_k")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    FINDING_ID_FIELD_NUMBER: _ClassVar[int]
    TOP_K_FIELD_NUMBER: _ClassVar[int]
    context: ContextInfo
    finding_id: str
    top_k: int
    def __init__(self, context: _Optional[_Union[ContextInfo, _Mapping]] = ..., finding_id: _Optional[str] = ..., top_k: _Optional[int] = ...) -> None: ...

class FindSimilarFindingsResponse(_message.Message):
    __slots__ = ("findings", "error")
    FINDINGS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    findings: _containers.RepeatedCompositeFieldContainer[FindingNode]
    error: HarnessError
    def __init__(self, findings: _Optional[_Iterable[_Union[FindingNode, _Mapping]]] = ..., error: _Optional[_Union[HarnessError, _Mapping]] = ...) -> None: ...

class FindingNode(_message.Message):
    __slots__ = ("id", "title", "description", "severity", "category", "confidence", "similarity")
    ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SEVERITY_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    SIMILARITY_FIELD_NUMBER: _ClassVar[int]
    id: str
    title: str
    description: str
    severity: str
    category: str
    confidence: float
    similarity: float
    def __init__(self, id: _Optional[str] = ..., title: _Optional[str] = ..., description: _Optional[str] = ..., severity: _Optional[str] = ..., category: _Optional[str] = ..., confidence: _Optional[float] = ..., similarity: _Optional[float] = ...) -> None: ...

class GetAttackChainsRequest(_message.Message):
    __slots__ = ("context", "technique_id", "max_depth")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    TECHNIQUE_ID_FIELD_NUMBER: _ClassVar[int]
    MAX_DEPTH_FIELD_NUMBER: _ClassVar[int]
    context: ContextInfo
    technique_id: str
    max_depth: int
    def __init__(self, context: _Optional[_Union[ContextInfo, _Mapping]] = ..., technique_id: _Optional[str] = ..., max_depth: _Optional[int] = ...) -> None: ...

class GetAttackChainsResponse(_message.Message):
    __slots__ = ("chains", "error")
    CHAINS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    chains: _containers.RepeatedCompositeFieldContainer[AttackChain]
    error: HarnessError
    def __init__(self, chains: _Optional[_Iterable[_Union[AttackChain, _Mapping]]] = ..., error: _Optional[_Union[HarnessError, _Mapping]] = ...) -> None: ...

class AttackChain(_message.Message):
    __slots__ = ("id", "name", "severity", "steps")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SEVERITY_FIELD_NUMBER: _ClassVar[int]
    STEPS_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    severity: str
    steps: _containers.RepeatedCompositeFieldContainer[AttackStep]
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., severity: _Optional[str] = ..., steps: _Optional[_Iterable[_Union[AttackStep, _Mapping]]] = ...) -> None: ...

class AttackStep(_message.Message):
    __slots__ = ("order", "technique_id", "node_id", "description", "confidence")
    ORDER_FIELD_NUMBER: _ClassVar[int]
    TECHNIQUE_ID_FIELD_NUMBER: _ClassVar[int]
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    order: int
    technique_id: str
    node_id: str
    description: str
    confidence: float
    def __init__(self, order: _Optional[int] = ..., technique_id: _Optional[str] = ..., node_id: _Optional[str] = ..., description: _Optional[str] = ..., confidence: _Optional[float] = ...) -> None: ...

class GetRelatedFindingsRequest(_message.Message):
    __slots__ = ("context", "finding_id")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    FINDING_ID_FIELD_NUMBER: _ClassVar[int]
    context: ContextInfo
    finding_id: str
    def __init__(self, context: _Optional[_Union[ContextInfo, _Mapping]] = ..., finding_id: _Optional[str] = ...) -> None: ...

class GetRelatedFindingsResponse(_message.Message):
    __slots__ = ("findings", "error")
    FINDINGS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    findings: _containers.RepeatedCompositeFieldContainer[FindingNode]
    error: HarnessError
    def __init__(self, findings: _Optional[_Iterable[_Union[FindingNode, _Mapping]]] = ..., error: _Optional[_Union[HarnessError, _Mapping]] = ...) -> None: ...

class StoreGraphNodeRequest(_message.Message):
    __slots__ = ("context", "node")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    NODE_FIELD_NUMBER: _ClassVar[int]
    context: ContextInfo
    node: GraphNode
    def __init__(self, context: _Optional[_Union[ContextInfo, _Mapping]] = ..., node: _Optional[_Union[GraphNode, _Mapping]] = ...) -> None: ...

class StoreGraphNodeResponse(_message.Message):
    __slots__ = ("node_id", "error")
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    node_id: str
    error: HarnessError
    def __init__(self, node_id: _Optional[str] = ..., error: _Optional[_Union[HarnessError, _Mapping]] = ...) -> None: ...

class CreateGraphRelationshipRequest(_message.Message):
    __slots__ = ("context", "relationship")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    RELATIONSHIP_FIELD_NUMBER: _ClassVar[int]
    context: ContextInfo
    relationship: Relationship
    def __init__(self, context: _Optional[_Union[ContextInfo, _Mapping]] = ..., relationship: _Optional[_Union[Relationship, _Mapping]] = ...) -> None: ...

class CreateGraphRelationshipResponse(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: HarnessError
    def __init__(self, error: _Optional[_Union[HarnessError, _Mapping]] = ...) -> None: ...

class Relationship(_message.Message):
    __slots__ = ("from_id", "to_id", "type", "properties", "bidirectional")
    class PropertiesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _gibson_common_pb2.TypedValue
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_gibson_common_pb2.TypedValue, _Mapping]] = ...) -> None: ...
    FROM_ID_FIELD_NUMBER: _ClassVar[int]
    TO_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    BIDIRECTIONAL_FIELD_NUMBER: _ClassVar[int]
    from_id: str
    to_id: str
    type: str
    properties: _containers.MessageMap[str, _gibson_common_pb2.TypedValue]
    bidirectional: bool
    def __init__(self, from_id: _Optional[str] = ..., to_id: _Optional[str] = ..., type: _Optional[str] = ..., properties: _Optional[_Mapping[str, _gibson_common_pb2.TypedValue]] = ..., bidirectional: bool = ...) -> None: ...

class StoreGraphBatchRequest(_message.Message):
    __slots__ = ("context", "nodes", "relationships")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    NODES_FIELD_NUMBER: _ClassVar[int]
    RELATIONSHIPS_FIELD_NUMBER: _ClassVar[int]
    context: ContextInfo
    nodes: _containers.RepeatedCompositeFieldContainer[GraphNode]
    relationships: _containers.RepeatedCompositeFieldContainer[Relationship]
    def __init__(self, context: _Optional[_Union[ContextInfo, _Mapping]] = ..., nodes: _Optional[_Iterable[_Union[GraphNode, _Mapping]]] = ..., relationships: _Optional[_Iterable[_Union[Relationship, _Mapping]]] = ...) -> None: ...

class StoreGraphBatchResponse(_message.Message):
    __slots__ = ("node_ids", "error")
    NODE_IDS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    node_ids: _containers.RepeatedScalarFieldContainer[str]
    error: HarnessError
    def __init__(self, node_ids: _Optional[_Iterable[str]] = ..., error: _Optional[_Union[HarnessError, _Mapping]] = ...) -> None: ...

class TraverseGraphRequest(_message.Message):
    __slots__ = ("context", "start_node_id", "options")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    START_NODE_ID_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    context: ContextInfo
    start_node_id: str
    options: TraversalOptions
    def __init__(self, context: _Optional[_Union[ContextInfo, _Mapping]] = ..., start_node_id: _Optional[str] = ..., options: _Optional[_Union[TraversalOptions, _Mapping]] = ...) -> None: ...

class TraverseGraphResponse(_message.Message):
    __slots__ = ("results", "error")
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[TraversalResult]
    error: HarnessError
    def __init__(self, results: _Optional[_Iterable[_Union[TraversalResult, _Mapping]]] = ..., error: _Optional[_Union[HarnessError, _Mapping]] = ...) -> None: ...

class TraversalOptions(_message.Message):
    __slots__ = ("max_depth", "relationship_types", "node_types", "direction")
    MAX_DEPTH_FIELD_NUMBER: _ClassVar[int]
    RELATIONSHIP_TYPES_FIELD_NUMBER: _ClassVar[int]
    NODE_TYPES_FIELD_NUMBER: _ClassVar[int]
    DIRECTION_FIELD_NUMBER: _ClassVar[int]
    max_depth: int
    relationship_types: _containers.RepeatedScalarFieldContainer[str]
    node_types: _containers.RepeatedScalarFieldContainer[str]
    direction: str
    def __init__(self, max_depth: _Optional[int] = ..., relationship_types: _Optional[_Iterable[str]] = ..., node_types: _Optional[_Iterable[str]] = ..., direction: _Optional[str] = ...) -> None: ...

class TraversalResult(_message.Message):
    __slots__ = ("node", "path", "distance")
    NODE_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    DISTANCE_FIELD_NUMBER: _ClassVar[int]
    node: GraphNode
    path: _containers.RepeatedScalarFieldContainer[str]
    distance: int
    def __init__(self, node: _Optional[_Union[GraphNode, _Mapping]] = ..., path: _Optional[_Iterable[str]] = ..., distance: _Optional[int] = ...) -> None: ...

class GraphRAGHealthRequest(_message.Message):
    __slots__ = ("context",)
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    context: ContextInfo
    def __init__(self, context: _Optional[_Union[ContextInfo, _Mapping]] = ...) -> None: ...

class GraphRAGHealthResponse(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: HarnessHealthStatus
    def __init__(self, status: _Optional[_Union[HarnessHealthStatus, _Mapping]] = ...) -> None: ...

class StoreNodeRequest(_message.Message):
    __slots__ = ("context", "node")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    NODE_FIELD_NUMBER: _ClassVar[int]
    context: ContextInfo
    node: _graphrag_pb2.GraphNode
    def __init__(self, context: _Optional[_Union[ContextInfo, _Mapping]] = ..., node: _Optional[_Union[_graphrag_pb2.GraphNode, _Mapping]] = ...) -> None: ...

class StoreNodeResponse(_message.Message):
    __slots__ = ("node_id", "error")
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    node_id: str
    error: HarnessError
    def __init__(self, node_id: _Optional[str] = ..., error: _Optional[_Union[HarnessError, _Mapping]] = ...) -> None: ...

class QueryNodesRequest(_message.Message):
    __slots__ = ("context", "query")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    context: ContextInfo
    query: _graphrag_pb2.GraphQuery
    def __init__(self, context: _Optional[_Union[ContextInfo, _Mapping]] = ..., query: _Optional[_Union[_graphrag_pb2.GraphQuery, _Mapping]] = ...) -> None: ...

class QueryNodesResponse(_message.Message):
    __slots__ = ("results", "error")
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[_graphrag_pb2.QueryResult]
    error: HarnessError
    def __init__(self, results: _Optional[_Iterable[_Union[_graphrag_pb2.QueryResult, _Mapping]]] = ..., error: _Optional[_Union[HarnessError, _Mapping]] = ...) -> None: ...

class GetPlanContextRequest(_message.Message):
    __slots__ = ("context",)
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    context: ContextInfo
    def __init__(self, context: _Optional[_Union[ContextInfo, _Mapping]] = ...) -> None: ...

class GetPlanContextResponse(_message.Message):
    __slots__ = ("plan_context", "error")
    PLAN_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    plan_context: PlanContext
    error: HarnessError
    def __init__(self, plan_context: _Optional[_Union[PlanContext, _Mapping]] = ..., error: _Optional[_Union[HarnessError, _Mapping]] = ...) -> None: ...

class PlanContext(_message.Message):
    __slots__ = ("current_step_index", "total_steps", "remaining_steps", "step_budget", "mission_budget_remaining")
    CURRENT_STEP_INDEX_FIELD_NUMBER: _ClassVar[int]
    TOTAL_STEPS_FIELD_NUMBER: _ClassVar[int]
    REMAINING_STEPS_FIELD_NUMBER: _ClassVar[int]
    STEP_BUDGET_FIELD_NUMBER: _ClassVar[int]
    MISSION_BUDGET_REMAINING_FIELD_NUMBER: _ClassVar[int]
    current_step_index: int
    total_steps: int
    remaining_steps: _containers.RepeatedScalarFieldContainer[str]
    step_budget: int
    mission_budget_remaining: int
    def __init__(self, current_step_index: _Optional[int] = ..., total_steps: _Optional[int] = ..., remaining_steps: _Optional[_Iterable[str]] = ..., step_budget: _Optional[int] = ..., mission_budget_remaining: _Optional[int] = ...) -> None: ...

class ReportStepHintsRequest(_message.Message):
    __slots__ = ("context", "hints")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    HINTS_FIELD_NUMBER: _ClassVar[int]
    context: ContextInfo
    hints: StepHints
    def __init__(self, context: _Optional[_Union[ContextInfo, _Mapping]] = ..., hints: _Optional[_Union[StepHints, _Mapping]] = ...) -> None: ...

class ReportStepHintsResponse(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: HarnessError
    def __init__(self, error: _Optional[_Union[HarnessError, _Mapping]] = ...) -> None: ...

class StepHints(_message.Message):
    __slots__ = ("confidence", "suggested_next", "replan_reason", "key_findings")
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    SUGGESTED_NEXT_FIELD_NUMBER: _ClassVar[int]
    REPLAN_REASON_FIELD_NUMBER: _ClassVar[int]
    KEY_FINDINGS_FIELD_NUMBER: _ClassVar[int]
    confidence: float
    suggested_next: _containers.RepeatedScalarFieldContainer[str]
    replan_reason: str
    key_findings: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, confidence: _Optional[float] = ..., suggested_next: _Optional[_Iterable[str]] = ..., replan_reason: _Optional[str] = ..., key_findings: _Optional[_Iterable[str]] = ...) -> None: ...

class AnyValue(_message.Message):
    __slots__ = ("string_value", "bool_value", "int_value", "double_value", "bytes_value")
    STRING_VALUE_FIELD_NUMBER: _ClassVar[int]
    BOOL_VALUE_FIELD_NUMBER: _ClassVar[int]
    INT_VALUE_FIELD_NUMBER: _ClassVar[int]
    DOUBLE_VALUE_FIELD_NUMBER: _ClassVar[int]
    BYTES_VALUE_FIELD_NUMBER: _ClassVar[int]
    string_value: str
    bool_value: bool
    int_value: int
    double_value: float
    bytes_value: bytes
    def __init__(self, string_value: _Optional[str] = ..., bool_value: bool = ..., int_value: _Optional[int] = ..., double_value: _Optional[float] = ..., bytes_value: _Optional[bytes] = ...) -> None: ...

class KeyValue(_message.Message):
    __slots__ = ("key", "value")
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    key: str
    value: AnyValue
    def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[AnyValue, _Mapping]] = ...) -> None: ...

class SpanEvent(_message.Message):
    __slots__ = ("name", "time_unix_nano", "attributes")
    NAME_FIELD_NUMBER: _ClassVar[int]
    TIME_UNIX_NANO_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    name: str
    time_unix_nano: int
    attributes: _containers.RepeatedCompositeFieldContainer[KeyValue]
    def __init__(self, name: _Optional[str] = ..., time_unix_nano: _Optional[int] = ..., attributes: _Optional[_Iterable[_Union[KeyValue, _Mapping]]] = ...) -> None: ...

class Span(_message.Message):
    __slots__ = ("trace_id", "span_id", "parent_span_id", "start_time_unix_nano", "end_time_unix_nano", "name", "kind", "status_code", "status_message", "attributes", "events")
    TRACE_ID_FIELD_NUMBER: _ClassVar[int]
    SPAN_ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_SPAN_ID_FIELD_NUMBER: _ClassVar[int]
    START_TIME_UNIX_NANO_FIELD_NUMBER: _ClassVar[int]
    END_TIME_UNIX_NANO_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    STATUS_CODE_FIELD_NUMBER: _ClassVar[int]
    STATUS_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    trace_id: str
    span_id: str
    parent_span_id: str
    start_time_unix_nano: int
    end_time_unix_nano: int
    name: str
    kind: SpanKind
    status_code: StatusCode
    status_message: str
    attributes: _containers.RepeatedCompositeFieldContainer[KeyValue]
    events: _containers.RepeatedCompositeFieldContainer[SpanEvent]
    def __init__(self, trace_id: _Optional[str] = ..., span_id: _Optional[str] = ..., parent_span_id: _Optional[str] = ..., start_time_unix_nano: _Optional[int] = ..., end_time_unix_nano: _Optional[int] = ..., name: _Optional[str] = ..., kind: _Optional[_Union[SpanKind, str]] = ..., status_code: _Optional[_Union[StatusCode, str]] = ..., status_message: _Optional[str] = ..., attributes: _Optional[_Iterable[_Union[KeyValue, _Mapping]]] = ..., events: _Optional[_Iterable[_Union[SpanEvent, _Mapping]]] = ...) -> None: ...

class RecordSpanRequest(_message.Message):
    __slots__ = ("context", "span")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    SPAN_FIELD_NUMBER: _ClassVar[int]
    context: ContextInfo
    span: Span
    def __init__(self, context: _Optional[_Union[ContextInfo, _Mapping]] = ..., span: _Optional[_Union[Span, _Mapping]] = ...) -> None: ...

class RecordSpanResponse(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: HarnessError
    def __init__(self, error: _Optional[_Union[HarnessError, _Mapping]] = ...) -> None: ...

class RecordSpansRequest(_message.Message):
    __slots__ = ("context", "spans")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    SPANS_FIELD_NUMBER: _ClassVar[int]
    context: ContextInfo
    spans: _containers.RepeatedCompositeFieldContainer[Span]
    def __init__(self, context: _Optional[_Union[ContextInfo, _Mapping]] = ..., spans: _Optional[_Iterable[_Union[Span, _Mapping]]] = ...) -> None: ...

class RecordSpansResponse(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: HarnessError
    def __init__(self, error: _Optional[_Union[HarnessError, _Mapping]] = ...) -> None: ...

class GetCredentialRequest(_message.Message):
    __slots__ = ("context", "name")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    context: ContextInfo
    name: str
    def __init__(self, context: _Optional[_Union[ContextInfo, _Mapping]] = ..., name: _Optional[str] = ...) -> None: ...

class GetCredentialResponse(_message.Message):
    __slots__ = ("credential", "error")
    CREDENTIAL_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    credential: Credential
    error: HarnessError
    def __init__(self, credential: _Optional[_Union[Credential, _Mapping]] = ..., error: _Optional[_Union[HarnessError, _Mapping]] = ...) -> None: ...

class Credential(_message.Message):
    __slots__ = ("name", "type", "api_key", "bearer_token", "basic", "oauth", "custom_secret", "metadata")
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _gibson_common_pb2.TypedValue
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_gibson_common_pb2.TypedValue, _Mapping]] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    API_KEY_FIELD_NUMBER: _ClassVar[int]
    BEARER_TOKEN_FIELD_NUMBER: _ClassVar[int]
    BASIC_FIELD_NUMBER: _ClassVar[int]
    OAUTH_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_SECRET_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    name: str
    type: CredentialType
    api_key: str
    bearer_token: str
    basic: BasicAuth
    oauth: OAuthCredential
    custom_secret: str
    metadata: _containers.MessageMap[str, _gibson_common_pb2.TypedValue]
    def __init__(self, name: _Optional[str] = ..., type: _Optional[_Union[CredentialType, str]] = ..., api_key: _Optional[str] = ..., bearer_token: _Optional[str] = ..., basic: _Optional[_Union[BasicAuth, _Mapping]] = ..., oauth: _Optional[_Union[OAuthCredential, _Mapping]] = ..., custom_secret: _Optional[str] = ..., metadata: _Optional[_Mapping[str, _gibson_common_pb2.TypedValue]] = ...) -> None: ...

class BasicAuth(_message.Message):
    __slots__ = ("username", "password")
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    username: str
    password: str
    def __init__(self, username: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...

class OAuthCredential(_message.Message):
    __slots__ = ("access_token", "refresh_token", "token_type", "expires_at")
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    REFRESH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TOKEN_TYPE_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    access_token: str
    refresh_token: str
    token_type: str
    expires_at: int
    def __init__(self, access_token: _Optional[str] = ..., refresh_token: _Optional[str] = ..., token_type: _Optional[str] = ..., expires_at: _Optional[int] = ...) -> None: ...

class GetTaxonomySchemaRequest(_message.Message):
    __slots__ = ("context",)
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    context: ContextInfo
    def __init__(self, context: _Optional[_Union[ContextInfo, _Mapping]] = ...) -> None: ...

class GetTaxonomySchemaResponse(_message.Message):
    __slots__ = ("version", "node_types", "relationship_types", "techniques", "target_types", "technique_types", "capabilities", "error")
    VERSION_FIELD_NUMBER: _ClassVar[int]
    NODE_TYPES_FIELD_NUMBER: _ClassVar[int]
    RELATIONSHIP_TYPES_FIELD_NUMBER: _ClassVar[int]
    TECHNIQUES_FIELD_NUMBER: _ClassVar[int]
    TARGET_TYPES_FIELD_NUMBER: _ClassVar[int]
    TECHNIQUE_TYPES_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    version: str
    node_types: _containers.RepeatedCompositeFieldContainer[TaxonomyNodeType]
    relationship_types: _containers.RepeatedCompositeFieldContainer[TaxonomyRelationshipType]
    techniques: _containers.RepeatedCompositeFieldContainer[TaxonomyTechnique]
    target_types: _containers.RepeatedCompositeFieldContainer[TaxonomyTargetType]
    technique_types: _containers.RepeatedCompositeFieldContainer[TaxonomyTechniqueType]
    capabilities: _containers.RepeatedCompositeFieldContainer[TaxonomyCapability]
    error: HarnessError
    def __init__(self, version: _Optional[str] = ..., node_types: _Optional[_Iterable[_Union[TaxonomyNodeType, _Mapping]]] = ..., relationship_types: _Optional[_Iterable[_Union[TaxonomyRelationshipType, _Mapping]]] = ..., techniques: _Optional[_Iterable[_Union[TaxonomyTechnique, _Mapping]]] = ..., target_types: _Optional[_Iterable[_Union[TaxonomyTargetType, _Mapping]]] = ..., technique_types: _Optional[_Iterable[_Union[TaxonomyTechniqueType, _Mapping]]] = ..., capabilities: _Optional[_Iterable[_Union[TaxonomyCapability, _Mapping]]] = ..., error: _Optional[_Union[HarnessError, _Mapping]] = ...) -> None: ...

class TaxonomyNodeType(_message.Message):
    __slots__ = ("id", "name", "type", "category", "description", "identifying_properties", "properties")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    IDENTIFYING_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    type: str
    category: str
    description: str
    identifying_properties: _containers.RepeatedScalarFieldContainer[str]
    properties: _containers.RepeatedCompositeFieldContainer[TaxonomyProperty]
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., type: _Optional[str] = ..., category: _Optional[str] = ..., description: _Optional[str] = ..., identifying_properties: _Optional[_Iterable[str]] = ..., properties: _Optional[_Iterable[_Union[TaxonomyProperty, _Mapping]]] = ...) -> None: ...

class TaxonomyRelationshipType(_message.Message):
    __slots__ = ("id", "name", "type", "category", "description", "from_types", "to_types", "properties", "bidirectional")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    FROM_TYPES_FIELD_NUMBER: _ClassVar[int]
    TO_TYPES_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    BIDIRECTIONAL_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    type: str
    category: str
    description: str
    from_types: _containers.RepeatedScalarFieldContainer[str]
    to_types: _containers.RepeatedScalarFieldContainer[str]
    properties: _containers.RepeatedCompositeFieldContainer[TaxonomyProperty]
    bidirectional: bool
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., type: _Optional[str] = ..., category: _Optional[str] = ..., description: _Optional[str] = ..., from_types: _Optional[_Iterable[str]] = ..., to_types: _Optional[_Iterable[str]] = ..., properties: _Optional[_Iterable[_Union[TaxonomyProperty, _Mapping]]] = ..., bidirectional: bool = ...) -> None: ...

class TaxonomyTechnique(_message.Message):
    __slots__ = ("technique_id", "name", "taxonomy", "category", "description", "tactic", "platforms", "mitre_mapping")
    TECHNIQUE_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TAXONOMY_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TACTIC_FIELD_NUMBER: _ClassVar[int]
    PLATFORMS_FIELD_NUMBER: _ClassVar[int]
    MITRE_MAPPING_FIELD_NUMBER: _ClassVar[int]
    technique_id: str
    name: str
    taxonomy: str
    category: str
    description: str
    tactic: str
    platforms: _containers.RepeatedScalarFieldContainer[str]
    mitre_mapping: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, technique_id: _Optional[str] = ..., name: _Optional[str] = ..., taxonomy: _Optional[str] = ..., category: _Optional[str] = ..., description: _Optional[str] = ..., tactic: _Optional[str] = ..., platforms: _Optional[_Iterable[str]] = ..., mitre_mapping: _Optional[_Iterable[str]] = ...) -> None: ...

class TaxonomyTargetType(_message.Message):
    __slots__ = ("id", "type", "name", "category", "description", "required_fields", "optional_fields")
    ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_FIELDS_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_FIELDS_FIELD_NUMBER: _ClassVar[int]
    id: str
    type: str
    name: str
    category: str
    description: str
    required_fields: _containers.RepeatedScalarFieldContainer[str]
    optional_fields: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, id: _Optional[str] = ..., type: _Optional[str] = ..., name: _Optional[str] = ..., category: _Optional[str] = ..., description: _Optional[str] = ..., required_fields: _Optional[_Iterable[str]] = ..., optional_fields: _Optional[_Iterable[str]] = ...) -> None: ...

class TaxonomyTechniqueType(_message.Message):
    __slots__ = ("id", "type", "name", "category", "description", "mitre_ids", "default_severity")
    ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    MITRE_IDS_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_SEVERITY_FIELD_NUMBER: _ClassVar[int]
    id: str
    type: str
    name: str
    category: str
    description: str
    mitre_ids: _containers.RepeatedScalarFieldContainer[str]
    default_severity: str
    def __init__(self, id: _Optional[str] = ..., type: _Optional[str] = ..., name: _Optional[str] = ..., category: _Optional[str] = ..., description: _Optional[str] = ..., mitre_ids: _Optional[_Iterable[str]] = ..., default_severity: _Optional[str] = ...) -> None: ...

class TaxonomyCapability(_message.Message):
    __slots__ = ("id", "name", "description", "technique_types")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TECHNIQUE_TYPES_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: str
    technique_types: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., technique_types: _Optional[_Iterable[str]] = ...) -> None: ...

class TaxonomyProperty(_message.Message):
    __slots__ = ("name", "type", "required", "description", "enum_values", "default_value")
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ENUM_VALUES_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_VALUE_FIELD_NUMBER: _ClassVar[int]
    name: str
    type: str
    required: bool
    description: str
    enum_values: _containers.RepeatedScalarFieldContainer[str]
    default_value: str
    def __init__(self, name: _Optional[str] = ..., type: _Optional[str] = ..., required: bool = ..., description: _Optional[str] = ..., enum_values: _Optional[_Iterable[str]] = ..., default_value: _Optional[str] = ...) -> None: ...

class GenerateNodeIDRequest(_message.Message):
    __slots__ = ("context", "node_type", "properties")
    class PropertiesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _gibson_common_pb2.TypedValue
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_gibson_common_pb2.TypedValue, _Mapping]] = ...) -> None: ...
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    NODE_TYPE_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    context: ContextInfo
    node_type: str
    properties: _containers.MessageMap[str, _gibson_common_pb2.TypedValue]
    def __init__(self, context: _Optional[_Union[ContextInfo, _Mapping]] = ..., node_type: _Optional[str] = ..., properties: _Optional[_Mapping[str, _gibson_common_pb2.TypedValue]] = ...) -> None: ...

class GenerateNodeIDResponse(_message.Message):
    __slots__ = ("node_id", "error")
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    node_id: str
    error: HarnessError
    def __init__(self, node_id: _Optional[str] = ..., error: _Optional[_Union[HarnessError, _Mapping]] = ...) -> None: ...

class ValidateFindingRequest(_message.Message):
    __slots__ = ("context", "finding")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    FINDING_FIELD_NUMBER: _ClassVar[int]
    context: ContextInfo
    finding: _types_pb2.Finding
    def __init__(self, context: _Optional[_Union[ContextInfo, _Mapping]] = ..., finding: _Optional[_Union[_types_pb2.Finding, _Mapping]] = ...) -> None: ...

class ValidateGraphNodeRequest(_message.Message):
    __slots__ = ("context", "node_type", "properties")
    class PropertiesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _gibson_common_pb2.TypedValue
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_gibson_common_pb2.TypedValue, _Mapping]] = ...) -> None: ...
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    NODE_TYPE_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    context: ContextInfo
    node_type: str
    properties: _containers.MessageMap[str, _gibson_common_pb2.TypedValue]
    def __init__(self, context: _Optional[_Union[ContextInfo, _Mapping]] = ..., node_type: _Optional[str] = ..., properties: _Optional[_Mapping[str, _gibson_common_pb2.TypedValue]] = ...) -> None: ...

class ValidateRelationshipRequest(_message.Message):
    __slots__ = ("context", "relationship_type", "from_node_type", "to_node_type", "properties")
    class PropertiesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _gibson_common_pb2.TypedValue
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_gibson_common_pb2.TypedValue, _Mapping]] = ...) -> None: ...
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    RELATIONSHIP_TYPE_FIELD_NUMBER: _ClassVar[int]
    FROM_NODE_TYPE_FIELD_NUMBER: _ClassVar[int]
    TO_NODE_TYPE_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    context: ContextInfo
    relationship_type: str
    from_node_type: str
    to_node_type: str
    properties: _containers.MessageMap[str, _gibson_common_pb2.TypedValue]
    def __init__(self, context: _Optional[_Union[ContextInfo, _Mapping]] = ..., relationship_type: _Optional[str] = ..., from_node_type: _Optional[str] = ..., to_node_type: _Optional[str] = ..., properties: _Optional[_Mapping[str, _gibson_common_pb2.TypedValue]] = ...) -> None: ...

class ValidationResponse(_message.Message):
    __slots__ = ("valid", "errors", "warnings", "error")
    VALID_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    valid: bool
    errors: _containers.RepeatedCompositeFieldContainer[ValidationError]
    warnings: _containers.RepeatedScalarFieldContainer[str]
    error: HarnessError
    def __init__(self, valid: bool = ..., errors: _Optional[_Iterable[_Union[ValidationError, _Mapping]]] = ..., warnings: _Optional[_Iterable[str]] = ..., error: _Optional[_Union[HarnessError, _Mapping]] = ...) -> None: ...

class ValidateFindingResponse(_message.Message):
    __slots__ = ("valid", "errors", "warnings", "error")
    VALID_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    valid: bool
    errors: _containers.RepeatedCompositeFieldContainer[ValidationError]
    warnings: _containers.RepeatedScalarFieldContainer[str]
    error: HarnessError
    def __init__(self, valid: bool = ..., errors: _Optional[_Iterable[_Union[ValidationError, _Mapping]]] = ..., warnings: _Optional[_Iterable[str]] = ..., error: _Optional[_Union[HarnessError, _Mapping]] = ...) -> None: ...

class ValidateGraphNodeResponse(_message.Message):
    __slots__ = ("valid", "errors", "warnings", "error")
    VALID_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    valid: bool
    errors: _containers.RepeatedCompositeFieldContainer[ValidationError]
    warnings: _containers.RepeatedScalarFieldContainer[str]
    error: HarnessError
    def __init__(self, valid: bool = ..., errors: _Optional[_Iterable[_Union[ValidationError, _Mapping]]] = ..., warnings: _Optional[_Iterable[str]] = ..., error: _Optional[_Union[HarnessError, _Mapping]] = ...) -> None: ...

class ValidateRelationshipResponse(_message.Message):
    __slots__ = ("valid", "errors", "warnings", "error")
    VALID_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    valid: bool
    errors: _containers.RepeatedCompositeFieldContainer[ValidationError]
    warnings: _containers.RepeatedScalarFieldContainer[str]
    error: HarnessError
    def __init__(self, valid: bool = ..., errors: _Optional[_Iterable[_Union[ValidationError, _Mapping]]] = ..., warnings: _Optional[_Iterable[str]] = ..., error: _Optional[_Union[HarnessError, _Mapping]] = ...) -> None: ...

class ValidationError(_message.Message):
    __slots__ = ("field", "message", "code")
    FIELD_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    field: str
    message: str
    code: str
    def __init__(self, field: _Optional[str] = ..., message: _Optional[str] = ..., code: _Optional[str] = ...) -> None: ...

class MissionConstraints(_message.Message):
    __slots__ = ("max_duration_ms", "max_tokens", "max_cost", "max_findings")
    MAX_DURATION_MS_FIELD_NUMBER: _ClassVar[int]
    MAX_TOKENS_FIELD_NUMBER: _ClassVar[int]
    MAX_COST_FIELD_NUMBER: _ClassVar[int]
    MAX_FINDINGS_FIELD_NUMBER: _ClassVar[int]
    max_duration_ms: int
    max_tokens: int
    max_cost: float
    max_findings: int
    def __init__(self, max_duration_ms: _Optional[int] = ..., max_tokens: _Optional[int] = ..., max_cost: _Optional[float] = ..., max_findings: _Optional[int] = ...) -> None: ...

class MissionMetrics(_message.Message):
    __slots__ = ("duration_ms", "tokens_used", "tool_calls", "agent_calls", "findings_count")
    DURATION_MS_FIELD_NUMBER: _ClassVar[int]
    TOKENS_USED_FIELD_NUMBER: _ClassVar[int]
    TOOL_CALLS_FIELD_NUMBER: _ClassVar[int]
    AGENT_CALLS_FIELD_NUMBER: _ClassVar[int]
    FINDINGS_COUNT_FIELD_NUMBER: _ClassVar[int]
    duration_ms: int
    tokens_used: int
    tool_calls: int
    agent_calls: int
    findings_count: int
    def __init__(self, duration_ms: _Optional[int] = ..., tokens_used: _Optional[int] = ..., tool_calls: _Optional[int] = ..., agent_calls: _Optional[int] = ..., findings_count: _Optional[int] = ...) -> None: ...

class MissionInfo(_message.Message):
    __slots__ = ("id", "name", "status", "target_id", "parent_mission_id", "created_at", "tags")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TARGET_ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_MISSION_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    status: MissionStatus
    target_id: str
    parent_mission_id: str
    created_at: int
    tags: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., status: _Optional[_Union[MissionStatus, str]] = ..., target_id: _Optional[str] = ..., parent_mission_id: _Optional[str] = ..., created_at: _Optional[int] = ..., tags: _Optional[_Iterable[str]] = ...) -> None: ...

class MissionStatusInfo(_message.Message):
    __slots__ = ("status", "progress", "phase", "finding_counts", "token_usage", "duration_ms", "error")
    class FindingCountsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    STATUS_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    PHASE_FIELD_NUMBER: _ClassVar[int]
    FINDING_COUNTS_FIELD_NUMBER: _ClassVar[int]
    TOKEN_USAGE_FIELD_NUMBER: _ClassVar[int]
    DURATION_MS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    status: MissionStatus
    progress: float
    phase: str
    finding_counts: _containers.ScalarMap[str, int]
    token_usage: int
    duration_ms: int
    error: str
    def __init__(self, status: _Optional[_Union[MissionStatus, str]] = ..., progress: _Optional[float] = ..., phase: _Optional[str] = ..., finding_counts: _Optional[_Mapping[str, int]] = ..., token_usage: _Optional[int] = ..., duration_ms: _Optional[int] = ..., error: _Optional[str] = ...) -> None: ...

class MissionResult(_message.Message):
    __slots__ = ("mission_id", "status", "findings", "output", "metrics", "error", "completed_at")
    class OutputEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _gibson_common_pb2.TypedValue
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_gibson_common_pb2.TypedValue, _Mapping]] = ...) -> None: ...
    MISSION_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    FINDINGS_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_FIELD_NUMBER: _ClassVar[int]
    METRICS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    COMPLETED_AT_FIELD_NUMBER: _ClassVar[int]
    mission_id: str
    status: MissionStatus
    findings: _containers.RepeatedCompositeFieldContainer[_types_pb2.Finding]
    output: _containers.MessageMap[str, _gibson_common_pb2.TypedValue]
    metrics: MissionMetrics
    error: str
    completed_at: int
    def __init__(self, mission_id: _Optional[str] = ..., status: _Optional[_Union[MissionStatus, str]] = ..., findings: _Optional[_Iterable[_Union[_types_pb2.Finding, _Mapping]]] = ..., output: _Optional[_Mapping[str, _gibson_common_pb2.TypedValue]] = ..., metrics: _Optional[_Union[MissionMetrics, _Mapping]] = ..., error: _Optional[str] = ..., completed_at: _Optional[int] = ...) -> None: ...

class MissionFilter(_message.Message):
    __slots__ = ("status", "target_id", "parent_mission_id", "created_after", "created_before", "tags", "limit", "offset")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TARGET_ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_MISSION_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AFTER_FIELD_NUMBER: _ClassVar[int]
    CREATED_BEFORE_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    status: MissionStatus
    target_id: str
    parent_mission_id: str
    created_after: int
    created_before: int
    tags: _containers.RepeatedScalarFieldContainer[str]
    limit: int
    offset: int
    def __init__(self, status: _Optional[_Union[MissionStatus, str]] = ..., target_id: _Optional[str] = ..., parent_mission_id: _Optional[str] = ..., created_after: _Optional[int] = ..., created_before: _Optional[int] = ..., tags: _Optional[_Iterable[str]] = ..., limit: _Optional[int] = ..., offset: _Optional[int] = ...) -> None: ...

class CreateMissionRequest(_message.Message):
    __slots__ = ("context", "mission_definition_json", "target_id", "name", "constraints", "metadata", "tags", "canonical_constraints")
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _gibson_common_pb2.TypedValue
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_gibson_common_pb2.TypedValue, _Mapping]] = ...) -> None: ...
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    MISSION_DEFINITION_JSON_FIELD_NUMBER: _ClassVar[int]
    TARGET_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CONSTRAINTS_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    CANONICAL_CONSTRAINTS_FIELD_NUMBER: _ClassVar[int]
    context: ContextInfo
    mission_definition_json: bytes
    target_id: str
    name: str
    constraints: MissionConstraints
    metadata: _containers.MessageMap[str, _gibson_common_pb2.TypedValue]
    tags: _containers.RepeatedScalarFieldContainer[str]
    canonical_constraints: _mission_definition_pb2.MissionConstraints
    def __init__(self, context: _Optional[_Union[ContextInfo, _Mapping]] = ..., mission_definition_json: _Optional[bytes] = ..., target_id: _Optional[str] = ..., name: _Optional[str] = ..., constraints: _Optional[_Union[MissionConstraints, _Mapping]] = ..., metadata: _Optional[_Mapping[str, _gibson_common_pb2.TypedValue]] = ..., tags: _Optional[_Iterable[str]] = ..., canonical_constraints: _Optional[_Union[_mission_definition_pb2.MissionConstraints, _Mapping]] = ...) -> None: ...

class CreateMissionResponse(_message.Message):
    __slots__ = ("mission", "error")
    MISSION_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    mission: MissionInfo
    error: HarnessError
    def __init__(self, mission: _Optional[_Union[MissionInfo, _Mapping]] = ..., error: _Optional[_Union[HarnessError, _Mapping]] = ...) -> None: ...

class RunMissionRequest(_message.Message):
    __slots__ = ("context", "mission_id", "wait", "timeout_ms")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    MISSION_ID_FIELD_NUMBER: _ClassVar[int]
    WAIT_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_MS_FIELD_NUMBER: _ClassVar[int]
    context: ContextInfo
    mission_id: str
    wait: bool
    timeout_ms: int
    def __init__(self, context: _Optional[_Union[ContextInfo, _Mapping]] = ..., mission_id: _Optional[str] = ..., wait: bool = ..., timeout_ms: _Optional[int] = ...) -> None: ...

class RunMissionResponse(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: HarnessError
    def __init__(self, error: _Optional[_Union[HarnessError, _Mapping]] = ...) -> None: ...

class GetMissionStatusRequest(_message.Message):
    __slots__ = ("context", "mission_id")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    MISSION_ID_FIELD_NUMBER: _ClassVar[int]
    context: ContextInfo
    mission_id: str
    def __init__(self, context: _Optional[_Union[ContextInfo, _Mapping]] = ..., mission_id: _Optional[str] = ...) -> None: ...

class GetMissionStatusResponse(_message.Message):
    __slots__ = ("status", "error")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    status: MissionStatusInfo
    error: HarnessError
    def __init__(self, status: _Optional[_Union[MissionStatusInfo, _Mapping]] = ..., error: _Optional[_Union[HarnessError, _Mapping]] = ...) -> None: ...

class WaitForMissionRequest(_message.Message):
    __slots__ = ("context", "mission_id", "timeout_ms")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    MISSION_ID_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_MS_FIELD_NUMBER: _ClassVar[int]
    context: ContextInfo
    mission_id: str
    timeout_ms: int
    def __init__(self, context: _Optional[_Union[ContextInfo, _Mapping]] = ..., mission_id: _Optional[str] = ..., timeout_ms: _Optional[int] = ...) -> None: ...

class WaitForMissionResponse(_message.Message):
    __slots__ = ("result", "error")
    RESULT_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    result: MissionResult
    error: HarnessError
    def __init__(self, result: _Optional[_Union[MissionResult, _Mapping]] = ..., error: _Optional[_Union[HarnessError, _Mapping]] = ...) -> None: ...

class ListMissionsRequest(_message.Message):
    __slots__ = ("context", "filter")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    context: ContextInfo
    filter: MissionFilter
    def __init__(self, context: _Optional[_Union[ContextInfo, _Mapping]] = ..., filter: _Optional[_Union[MissionFilter, _Mapping]] = ...) -> None: ...

class ListMissionsResponse(_message.Message):
    __slots__ = ("missions", "error")
    MISSIONS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    missions: _containers.RepeatedCompositeFieldContainer[MissionInfo]
    error: HarnessError
    def __init__(self, missions: _Optional[_Iterable[_Union[MissionInfo, _Mapping]]] = ..., error: _Optional[_Union[HarnessError, _Mapping]] = ...) -> None: ...

class CancelMissionRequest(_message.Message):
    __slots__ = ("context", "mission_id")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    MISSION_ID_FIELD_NUMBER: _ClassVar[int]
    context: ContextInfo
    mission_id: str
    def __init__(self, context: _Optional[_Union[ContextInfo, _Mapping]] = ..., mission_id: _Optional[str] = ...) -> None: ...

class CancelMissionResponse(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: HarnessError
    def __init__(self, error: _Optional[_Union[HarnessError, _Mapping]] = ...) -> None: ...

class GetMissionResultsRequest(_message.Message):
    __slots__ = ("context", "mission_id")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    MISSION_ID_FIELD_NUMBER: _ClassVar[int]
    context: ContextInfo
    mission_id: str
    def __init__(self, context: _Optional[_Union[ContextInfo, _Mapping]] = ..., mission_id: _Optional[str] = ...) -> None: ...

class GetMissionResultsResponse(_message.Message):
    __slots__ = ("result", "error")
    RESULT_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    result: MissionResult
    error: HarnessError
    def __init__(self, result: _Optional[_Union[MissionResult, _Mapping]] = ..., error: _Optional[_Union[HarnessError, _Mapping]] = ...) -> None: ...

class AuthorizeRequest(_message.Message):
    __slots__ = ("run_id", "action", "resource")
    RUN_ID_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    run_id: str
    action: str
    resource: str
    def __init__(self, run_id: _Optional[str] = ..., action: _Optional[str] = ..., resource: _Optional[str] = ...) -> None: ...

class AuthorizeResponse(_message.Message):
    __slots__ = ("allowed", "reason")
    ALLOWED_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    allowed: bool
    reason: str
    def __init__(self, allowed: bool = ..., reason: _Optional[str] = ...) -> None: ...

class MissionRunSummary(_message.Message):
    __slots__ = ("mission_id", "run_number", "status", "findings_count", "created_at_unix", "completed_at_unix")
    MISSION_ID_FIELD_NUMBER: _ClassVar[int]
    RUN_NUMBER_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    FINDINGS_COUNT_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_UNIX_FIELD_NUMBER: _ClassVar[int]
    COMPLETED_AT_UNIX_FIELD_NUMBER: _ClassVar[int]
    mission_id: str
    run_number: int
    status: str
    findings_count: int
    created_at_unix: int
    completed_at_unix: int
    def __init__(self, mission_id: _Optional[str] = ..., run_number: _Optional[int] = ..., status: _Optional[str] = ..., findings_count: _Optional[int] = ..., created_at_unix: _Optional[int] = ..., completed_at_unix: _Optional[int] = ...) -> None: ...

class GetMissionRunHistoryRequest(_message.Message):
    __slots__ = ("context", "limit")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    context: ContextInfo
    limit: int
    def __init__(self, context: _Optional[_Union[ContextInfo, _Mapping]] = ..., limit: _Optional[int] = ...) -> None: ...

class GetMissionRunHistoryResponse(_message.Message):
    __slots__ = ("runs", "error")
    RUNS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    runs: _containers.RepeatedCompositeFieldContainer[MissionRunSummary]
    error: HarnessError
    def __init__(self, runs: _Optional[_Iterable[_Union[MissionRunSummary, _Mapping]]] = ..., error: _Optional[_Union[HarnessError, _Mapping]] = ...) -> None: ...

class GetPreviousRunFindingsRequest(_message.Message):
    __slots__ = ("context", "filter")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    context: ContextInfo
    filter: FindingFilter
    def __init__(self, context: _Optional[_Union[ContextInfo, _Mapping]] = ..., filter: _Optional[_Union[FindingFilter, _Mapping]] = ...) -> None: ...

class GetPreviousRunFindingsResponse(_message.Message):
    __slots__ = ("findings", "error")
    FINDINGS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    findings: _containers.RepeatedCompositeFieldContainer[_types_pb2.Finding]
    error: HarnessError
    def __init__(self, findings: _Optional[_Iterable[_Union[_types_pb2.Finding, _Mapping]]] = ..., error: _Optional[_Union[HarnessError, _Mapping]] = ...) -> None: ...

class GetAllRunFindingsRequest(_message.Message):
    __slots__ = ("context", "filter", "page_size", "page_token")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    context: ContextInfo
    filter: FindingFilter
    page_size: int
    page_token: str
    def __init__(self, context: _Optional[_Union[ContextInfo, _Mapping]] = ..., filter: _Optional[_Union[FindingFilter, _Mapping]] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class GetAllRunFindingsResponse(_message.Message):
    __slots__ = ("findings", "next_page_token", "error")
    FINDINGS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    findings: _containers.RepeatedCompositeFieldContainer[_types_pb2.Finding]
    next_page_token: str
    error: HarnessError
    def __init__(self, findings: _Optional[_Iterable[_Union[_types_pb2.Finding, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., error: _Optional[_Union[HarnessError, _Mapping]] = ...) -> None: ...

class WorkspaceInfo(_message.Message):
    __slots__ = ("name", "path")
    NAME_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    name: str
    path: str
    def __init__(self, name: _Optional[str] = ..., path: _Optional[str] = ...) -> None: ...

class WorkspaceListRequest(_message.Message):
    __slots__ = ("context",)
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    context: ContextInfo
    def __init__(self, context: _Optional[_Union[ContextInfo, _Mapping]] = ...) -> None: ...

class WorkspaceListResponse(_message.Message):
    __slots__ = ("workspaces",)
    WORKSPACES_FIELD_NUMBER: _ClassVar[int]
    workspaces: _containers.RepeatedCompositeFieldContainer[WorkspaceInfo]
    def __init__(self, workspaces: _Optional[_Iterable[_Union[WorkspaceInfo, _Mapping]]] = ...) -> None: ...

class WorkspaceGetInfoRequest(_message.Message):
    __slots__ = ("context", "name")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    context: ContextInfo
    name: str
    def __init__(self, context: _Optional[_Union[ContextInfo, _Mapping]] = ..., name: _Optional[str] = ...) -> None: ...

class WorkspaceGetInfoResponse(_message.Message):
    __slots__ = ("workspace",)
    WORKSPACE_FIELD_NUMBER: _ClassVar[int]
    workspace: WorkspaceInfo
    def __init__(self, workspace: _Optional[_Union[WorkspaceInfo, _Mapping]] = ...) -> None: ...

class WorkspaceReadFileRequest(_message.Message):
    __slots__ = ("context", "workspace_name", "path")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    WORKSPACE_NAME_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    context: ContextInfo
    workspace_name: str
    path: str
    def __init__(self, context: _Optional[_Union[ContextInfo, _Mapping]] = ..., workspace_name: _Optional[str] = ..., path: _Optional[str] = ...) -> None: ...

class WorkspaceReadFileResponse(_message.Message):
    __slots__ = ("content",)
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    content: bytes
    def __init__(self, content: _Optional[bytes] = ...) -> None: ...

class WorkspaceWriteFileRequest(_message.Message):
    __slots__ = ("context", "workspace_name", "path", "content")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    WORKSPACE_NAME_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    context: ContextInfo
    workspace_name: str
    path: str
    content: bytes
    def __init__(self, context: _Optional[_Union[ContextInfo, _Mapping]] = ..., workspace_name: _Optional[str] = ..., path: _Optional[str] = ..., content: _Optional[bytes] = ...) -> None: ...

class WorkspaceWriteFileResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class WorkspaceListFilesRequest(_message.Message):
    __slots__ = ("context", "workspace_name", "pattern")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    WORKSPACE_NAME_FIELD_NUMBER: _ClassVar[int]
    PATTERN_FIELD_NUMBER: _ClassVar[int]
    context: ContextInfo
    workspace_name: str
    pattern: str
    def __init__(self, context: _Optional[_Union[ContextInfo, _Mapping]] = ..., workspace_name: _Optional[str] = ..., pattern: _Optional[str] = ...) -> None: ...

class WorkspaceListFilesResponse(_message.Message):
    __slots__ = ("paths", "truncated")
    PATHS_FIELD_NUMBER: _ClassVar[int]
    TRUNCATED_FIELD_NUMBER: _ClassVar[int]
    paths: _containers.RepeatedScalarFieldContainer[str]
    truncated: bool
    def __init__(self, paths: _Optional[_Iterable[str]] = ..., truncated: bool = ...) -> None: ...

class WorkspaceCommitRequest(_message.Message):
    __slots__ = ("context", "workspace_name", "message")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    WORKSPACE_NAME_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    context: ContextInfo
    workspace_name: str
    message: str
    def __init__(self, context: _Optional[_Union[ContextInfo, _Mapping]] = ..., workspace_name: _Optional[str] = ..., message: _Optional[str] = ...) -> None: ...

class WorkspaceCommitResponse(_message.Message):
    __slots__ = ("commit_sha",)
    COMMIT_SHA_FIELD_NUMBER: _ClassVar[int]
    commit_sha: str
    def __init__(self, commit_sha: _Optional[str] = ...) -> None: ...

class WorkspacePushRequest(_message.Message):
    __slots__ = ("context", "workspace_name")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    WORKSPACE_NAME_FIELD_NUMBER: _ClassVar[int]
    context: ContextInfo
    workspace_name: str
    def __init__(self, context: _Optional[_Union[ContextInfo, _Mapping]] = ..., workspace_name: _Optional[str] = ...) -> None: ...

class WorkspacePushResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
