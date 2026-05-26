from gibson.common.v1 import gibson_common_pb2 as _gibson_common_pb2
from gibson.types.v1 import types_pb2 as _types_pb2
from gibson.auth.v1 import options_pb2 as _options_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetDescriptorRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class TargetSchemaProto(_message.Message):
    __slots__ = ("type", "version", "schema_json", "description")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_JSON_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    type: str
    version: str
    schema_json: str
    description: str
    def __init__(self, type: _Optional[str] = ..., version: _Optional[str] = ..., schema_json: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...

class GetDescriptorResponse(_message.Message):
    __slots__ = ("name", "version", "description", "capabilities", "target_schemas", "technique_types", "target_types")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    TARGET_SCHEMAS_FIELD_NUMBER: _ClassVar[int]
    TECHNIQUE_TYPES_FIELD_NUMBER: _ClassVar[int]
    TARGET_TYPES_FIELD_NUMBER: _ClassVar[int]
    name: str
    version: str
    description: str
    capabilities: _containers.RepeatedScalarFieldContainer[str]
    target_schemas: _containers.RepeatedCompositeFieldContainer[TargetSchemaProto]
    technique_types: _containers.RepeatedScalarFieldContainer[str]
    target_types: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, name: _Optional[str] = ..., version: _Optional[str] = ..., description: _Optional[str] = ..., capabilities: _Optional[_Iterable[str]] = ..., target_schemas: _Optional[_Iterable[_Union[TargetSchemaProto, _Mapping]]] = ..., technique_types: _Optional[_Iterable[str]] = ..., target_types: _Optional[_Iterable[str]] = ...) -> None: ...

class AgentSlotDefinition(_message.Message):
    __slots__ = ("name", "description", "required", "default_config", "constraints")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    CONSTRAINTS_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    required: bool
    default_config: AgentSlotConfig
    constraints: AgentSlotConstraints
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., required: bool = ..., default_config: _Optional[_Union[AgentSlotConfig, _Mapping]] = ..., constraints: _Optional[_Union[AgentSlotConstraints, _Mapping]] = ...) -> None: ...

class AgentSlotConfig(_message.Message):
    __slots__ = ("provider", "model", "temperature", "max_tokens")
    PROVIDER_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
    MAX_TOKENS_FIELD_NUMBER: _ClassVar[int]
    provider: str
    model: str
    temperature: float
    max_tokens: int
    def __init__(self, provider: _Optional[str] = ..., model: _Optional[str] = ..., temperature: _Optional[float] = ..., max_tokens: _Optional[int] = ...) -> None: ...

class AgentSlotConstraints(_message.Message):
    __slots__ = ("min_context_window", "required_features")
    MIN_CONTEXT_WINDOW_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_FEATURES_FIELD_NUMBER: _ClassVar[int]
    min_context_window: int
    required_features: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, min_context_window: _Optional[int] = ..., required_features: _Optional[_Iterable[str]] = ...) -> None: ...

class GetSlotSchemaRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetSlotSchemaResponse(_message.Message):
    __slots__ = ("slots",)
    SLOTS_FIELD_NUMBER: _ClassVar[int]
    slots: _containers.RepeatedCompositeFieldContainer[AgentSlotDefinition]
    def __init__(self, slots: _Optional[_Iterable[_Union[AgentSlotDefinition, _Mapping]]] = ...) -> None: ...

class ExecuteRequest(_message.Message):
    __slots__ = ("task", "timeout_ms", "callback_endpoint", "callback_token", "mission", "target", "trace_id", "parent_span_id", "mission_run_id", "agent_run_id", "run_number")
    TASK_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_MS_FIELD_NUMBER: _ClassVar[int]
    CALLBACK_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    CALLBACK_TOKEN_FIELD_NUMBER: _ClassVar[int]
    MISSION_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    TRACE_ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_SPAN_ID_FIELD_NUMBER: _ClassVar[int]
    MISSION_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    AGENT_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    RUN_NUMBER_FIELD_NUMBER: _ClassVar[int]
    task: _types_pb2.Task
    timeout_ms: int
    callback_endpoint: str
    callback_token: str
    mission: _gibson_common_pb2.TypedMap
    target: _gibson_common_pb2.TypedMap
    trace_id: str
    parent_span_id: str
    mission_run_id: str
    agent_run_id: str
    run_number: int
    def __init__(self, task: _Optional[_Union[_types_pb2.Task, _Mapping]] = ..., timeout_ms: _Optional[int] = ..., callback_endpoint: _Optional[str] = ..., callback_token: _Optional[str] = ..., mission: _Optional[_Union[_gibson_common_pb2.TypedMap, _Mapping]] = ..., target: _Optional[_Union[_gibson_common_pb2.TypedMap, _Mapping]] = ..., trace_id: _Optional[str] = ..., parent_span_id: _Optional[str] = ..., mission_run_id: _Optional[str] = ..., agent_run_id: _Optional[str] = ..., run_number: _Optional[int] = ...) -> None: ...

class ExecuteResponse(_message.Message):
    __slots__ = ("result", "error")
    RESULT_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    result: _types_pb2.Result
    error: _gibson_common_pb2.Error
    def __init__(self, result: _Optional[_Union[_types_pb2.Result, _Mapping]] = ..., error: _Optional[_Union[_gibson_common_pb2.Error, _Mapping]] = ...) -> None: ...

class HealthRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class HealthResponse(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: _gibson_common_pb2.HealthStatus
    def __init__(self, status: _Optional[_Union[_gibson_common_pb2.HealthStatus, _Mapping]] = ...) -> None: ...
