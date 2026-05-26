from gibson.graphrag.v1 import graphrag_pb2 as _graphrag_pb2
from gibson.auth.v1 import options_pb2 as _options_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DispatchMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DISPATCH_MODE_UNSPECIFIED: _ClassVar[DispatchMode]
    DISPATCH_MODE_SANDBOXED: _ClassVar[DispatchMode]
    DISPATCH_MODE_PLUGIN: _ClassVar[DispatchMode]
    DISPATCH_MODE_AGENT: _ClassVar[DispatchMode]

class ContentTrust(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CONTENT_TRUST_UNSPECIFIED: _ClassVar[ContentTrust]
    CONTENT_TRUST_TRUSTED: _ClassVar[ContentTrust]
    CONTENT_TRUST_UNTRUSTED: _ClassVar[ContentTrust]

class ParseQuality(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PARSE_QUALITY_UNSPECIFIED: _ClassVar[ParseQuality]
    PARSE_QUALITY_STRUCTURED: _ClassVar[ParseQuality]
    PARSE_QUALITY_PARTIAL: _ClassVar[ParseQuality]
    PARSE_QUALITY_RAW: _ClassVar[ParseQuality]
    PARSE_QUALITY_FAILED: _ClassVar[ParseQuality]
DISPATCH_MODE_UNSPECIFIED: DispatchMode
DISPATCH_MODE_SANDBOXED: DispatchMode
DISPATCH_MODE_PLUGIN: DispatchMode
DISPATCH_MODE_AGENT: DispatchMode
CONTENT_TRUST_UNSPECIFIED: ContentTrust
CONTENT_TRUST_TRUSTED: ContentTrust
CONTENT_TRUST_UNTRUSTED: ContentTrust
PARSE_QUALITY_UNSPECIFIED: ParseQuality
PARSE_QUALITY_STRUCTURED: ParseQuality
PARSE_QUALITY_PARTIAL: ParseQuality
PARSE_QUALITY_RAW: ParseQuality
PARSE_QUALITY_FAILED: ParseQuality

class Resources(_message.Message):
    __slots__ = ("vcpu", "memory")
    VCPU_FIELD_NUMBER: _ClassVar[int]
    MEMORY_FIELD_NUMBER: _ClassVar[int]
    vcpu: int
    memory: str
    def __init__(self, vcpu: _Optional[int] = ..., memory: _Optional[str] = ...) -> None: ...

class ComponentDescriptor(_message.Message):
    __slots__ = ("name", "version", "kind", "description", "tags", "metadata", "dispatch_mode", "image", "command", "env", "resources", "default_timeout_seconds", "input_schema_json", "output_proto_type", "default_parse_quality", "content_trust")
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class EnvEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    DISPATCH_MODE_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    ENV_FIELD_NUMBER: _ClassVar[int]
    RESOURCES_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_TIMEOUT_SECONDS_FIELD_NUMBER: _ClassVar[int]
    INPUT_SCHEMA_JSON_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_PROTO_TYPE_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_PARSE_QUALITY_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TRUST_FIELD_NUMBER: _ClassVar[int]
    name: str
    version: str
    kind: str
    description: str
    tags: _containers.RepeatedScalarFieldContainer[str]
    metadata: _containers.ScalarMap[str, str]
    dispatch_mode: DispatchMode
    image: str
    command: _containers.RepeatedScalarFieldContainer[str]
    env: _containers.ScalarMap[str, str]
    resources: Resources
    default_timeout_seconds: int
    input_schema_json: bytes
    output_proto_type: str
    default_parse_quality: ParseQuality
    content_trust: ContentTrust
    def __init__(self, name: _Optional[str] = ..., version: _Optional[str] = ..., kind: _Optional[str] = ..., description: _Optional[str] = ..., tags: _Optional[_Iterable[str]] = ..., metadata: _Optional[_Mapping[str, str]] = ..., dispatch_mode: _Optional[_Union[DispatchMode, str]] = ..., image: _Optional[str] = ..., command: _Optional[_Iterable[str]] = ..., env: _Optional[_Mapping[str, str]] = ..., resources: _Optional[_Union[Resources, _Mapping]] = ..., default_timeout_seconds: _Optional[int] = ..., input_schema_json: _Optional[bytes] = ..., output_proto_type: _Optional[str] = ..., default_parse_quality: _Optional[_Union[ParseQuality, str]] = ..., content_trust: _Optional[_Union[ContentTrust, str]] = ...) -> None: ...

class RegisterComponentRequest(_message.Message):
    __slots__ = ("kind", "name", "version", "metadata", "capabilities", "methods", "input_message_type", "output_message_type", "file_descriptor_set", "config_schema_json", "ontology_extension")
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    KIND_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    METHODS_FIELD_NUMBER: _ClassVar[int]
    INPUT_MESSAGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_MESSAGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    FILE_DESCRIPTOR_SET_FIELD_NUMBER: _ClassVar[int]
    CONFIG_SCHEMA_JSON_FIELD_NUMBER: _ClassVar[int]
    ONTOLOGY_EXTENSION_FIELD_NUMBER: _ClassVar[int]
    kind: str
    name: str
    version: str
    metadata: _containers.ScalarMap[str, str]
    capabilities: _containers.RepeatedScalarFieldContainer[str]
    methods: _containers.RepeatedScalarFieldContainer[str]
    input_message_type: str
    output_message_type: str
    file_descriptor_set: bytes
    config_schema_json: str
    ontology_extension: _graphrag_pb2.OntologyExtension
    def __init__(self, kind: _Optional[str] = ..., name: _Optional[str] = ..., version: _Optional[str] = ..., metadata: _Optional[_Mapping[str, str]] = ..., capabilities: _Optional[_Iterable[str]] = ..., methods: _Optional[_Iterable[str]] = ..., input_message_type: _Optional[str] = ..., output_message_type: _Optional[str] = ..., file_descriptor_set: _Optional[bytes] = ..., config_schema_json: _Optional[str] = ..., ontology_extension: _Optional[_Union[_graphrag_pb2.OntologyExtension, _Mapping]] = ...) -> None: ...

class RegisterComponentResponse(_message.Message):
    __slots__ = ("instance_id", "heartbeat_interval_ms", "poll_interval_ms", "poll_timeout_ms", "config")
    class ConfigEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    HEARTBEAT_INTERVAL_MS_FIELD_NUMBER: _ClassVar[int]
    POLL_INTERVAL_MS_FIELD_NUMBER: _ClassVar[int]
    POLL_TIMEOUT_MS_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    instance_id: str
    heartbeat_interval_ms: int
    poll_interval_ms: int
    poll_timeout_ms: int
    config: _containers.ScalarMap[str, str]
    def __init__(self, instance_id: _Optional[str] = ..., heartbeat_interval_ms: _Optional[int] = ..., poll_interval_ms: _Optional[int] = ..., poll_timeout_ms: _Optional[int] = ..., config: _Optional[_Mapping[str, str]] = ...) -> None: ...

class HeartbeatRequest(_message.Message):
    __slots__ = ("instance_id", "health_status", "health_message")
    INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    HEALTH_STATUS_FIELD_NUMBER: _ClassVar[int]
    HEALTH_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    instance_id: str
    health_status: str
    health_message: str
    def __init__(self, instance_id: _Optional[str] = ..., health_status: _Optional[str] = ..., health_message: _Optional[str] = ...) -> None: ...

class HeartbeatResponse(_message.Message):
    __slots__ = ("registered", "config_updates")
    class ConfigUpdatesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    REGISTERED_FIELD_NUMBER: _ClassVar[int]
    CONFIG_UPDATES_FIELD_NUMBER: _ClassVar[int]
    registered: bool
    config_updates: _containers.ScalarMap[str, str]
    def __init__(self, registered: bool = ..., config_updates: _Optional[_Mapping[str, str]] = ...) -> None: ...

class PollWorkRequest(_message.Message):
    __slots__ = ("instance_id", "timeout_ms")
    INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_MS_FIELD_NUMBER: _ClassVar[int]
    instance_id: str
    timeout_ms: int
    def __init__(self, instance_id: _Optional[str] = ..., timeout_ms: _Optional[int] = ...) -> None: ...

class PollWorkResponse(_message.Message):
    __slots__ = ("work_id", "work_type", "payload", "context", "timeout_ms")
    class ContextEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    WORK_ID_FIELD_NUMBER: _ClassVar[int]
    WORK_TYPE_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_MS_FIELD_NUMBER: _ClassVar[int]
    work_id: str
    work_type: str
    payload: bytes
    context: _containers.ScalarMap[str, str]
    timeout_ms: int
    def __init__(self, work_id: _Optional[str] = ..., work_type: _Optional[str] = ..., payload: _Optional[bytes] = ..., context: _Optional[_Mapping[str, str]] = ..., timeout_ms: _Optional[int] = ...) -> None: ...

class SubmitResultRequest(_message.Message):
    __slots__ = ("work_id", "result", "error")
    WORK_ID_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    work_id: str
    result: bytes
    error: ComponentError
    def __init__(self, work_id: _Optional[str] = ..., result: _Optional[bytes] = ..., error: _Optional[_Union[ComponentError, _Mapping]] = ...) -> None: ...

class SubmitResultResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CompleteRequest(_message.Message):
    __slots__ = ("work_id", "slot", "messages", "timeout_ms")
    WORK_ID_FIELD_NUMBER: _ClassVar[int]
    SLOT_FIELD_NUMBER: _ClassVar[int]
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_MS_FIELD_NUMBER: _ClassVar[int]
    work_id: str
    slot: str
    messages: _containers.RepeatedCompositeFieldContainer[LLMMessage]
    timeout_ms: int
    def __init__(self, work_id: _Optional[str] = ..., slot: _Optional[str] = ..., messages: _Optional[_Iterable[_Union[LLMMessage, _Mapping]]] = ..., timeout_ms: _Optional[int] = ...) -> None: ...

class LLMMessage(_message.Message):
    __slots__ = ("role", "content")
    ROLE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    role: str
    content: str
    def __init__(self, role: _Optional[str] = ..., content: _Optional[str] = ...) -> None: ...

class CompleteResponse(_message.Message):
    __slots__ = ("response", "usage")
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    USAGE_FIELD_NUMBER: _ClassVar[int]
    response: LLMMessage
    usage: TokenUsage
    def __init__(self, response: _Optional[_Union[LLMMessage, _Mapping]] = ..., usage: _Optional[_Union[TokenUsage, _Mapping]] = ...) -> None: ...

class CompleteStreamRequest(_message.Message):
    __slots__ = ("work_id", "slot", "messages", "timeout_ms")
    WORK_ID_FIELD_NUMBER: _ClassVar[int]
    SLOT_FIELD_NUMBER: _ClassVar[int]
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_MS_FIELD_NUMBER: _ClassVar[int]
    work_id: str
    slot: str
    messages: _containers.RepeatedCompositeFieldContainer[LLMMessage]
    timeout_ms: int
    def __init__(self, work_id: _Optional[str] = ..., slot: _Optional[str] = ..., messages: _Optional[_Iterable[_Union[LLMMessage, _Mapping]]] = ..., timeout_ms: _Optional[int] = ...) -> None: ...

class CompleteStreamResponse(_message.Message):
    __slots__ = ("content", "done", "usage")
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    DONE_FIELD_NUMBER: _ClassVar[int]
    USAGE_FIELD_NUMBER: _ClassVar[int]
    content: str
    done: bool
    usage: TokenUsage
    def __init__(self, content: _Optional[str] = ..., done: bool = ..., usage: _Optional[_Union[TokenUsage, _Mapping]] = ...) -> None: ...

class TokenUsage(_message.Message):
    __slots__ = ("input_tokens", "output_tokens")
    INPUT_TOKENS_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_TOKENS_FIELD_NUMBER: _ClassVar[int]
    input_tokens: int
    output_tokens: int
    def __init__(self, input_tokens: _Optional[int] = ..., output_tokens: _Optional[int] = ...) -> None: ...

class CallToolRequest(_message.Message):
    __slots__ = ("work_id", "tool_name", "input_json", "timeout_ms")
    WORK_ID_FIELD_NUMBER: _ClassVar[int]
    TOOL_NAME_FIELD_NUMBER: _ClassVar[int]
    INPUT_JSON_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_MS_FIELD_NUMBER: _ClassVar[int]
    work_id: str
    tool_name: str
    input_json: str
    timeout_ms: int
    def __init__(self, work_id: _Optional[str] = ..., tool_name: _Optional[str] = ..., input_json: _Optional[str] = ..., timeout_ms: _Optional[int] = ...) -> None: ...

class CallToolResponse(_message.Message):
    __slots__ = ("output_json", "error")
    OUTPUT_JSON_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    output_json: str
    error: ComponentError
    def __init__(self, output_json: _Optional[str] = ..., error: _Optional[_Union[ComponentError, _Mapping]] = ...) -> None: ...

class QueryPluginRequest(_message.Message):
    __slots__ = ("work_id", "plugin_name", "method", "params_json", "timeout_ms")
    WORK_ID_FIELD_NUMBER: _ClassVar[int]
    PLUGIN_NAME_FIELD_NUMBER: _ClassVar[int]
    METHOD_FIELD_NUMBER: _ClassVar[int]
    PARAMS_JSON_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_MS_FIELD_NUMBER: _ClassVar[int]
    work_id: str
    plugin_name: str
    method: str
    params_json: str
    timeout_ms: int
    def __init__(self, work_id: _Optional[str] = ..., plugin_name: _Optional[str] = ..., method: _Optional[str] = ..., params_json: _Optional[str] = ..., timeout_ms: _Optional[int] = ...) -> None: ...

class QueryPluginResponse(_message.Message):
    __slots__ = ("result_json", "error")
    RESULT_JSON_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    result_json: str
    error: ComponentError
    def __init__(self, result_json: _Optional[str] = ..., error: _Optional[_Union[ComponentError, _Mapping]] = ...) -> None: ...

class SubmitFindingRequest(_message.Message):
    __slots__ = ("work_id", "finding")
    WORK_ID_FIELD_NUMBER: _ClassVar[int]
    FINDING_FIELD_NUMBER: _ClassVar[int]
    work_id: str
    finding: bytes
    def __init__(self, work_id: _Optional[str] = ..., finding: _Optional[bytes] = ...) -> None: ...

class SubmitFindingResponse(_message.Message):
    __slots__ = ("finding_id",)
    FINDING_ID_FIELD_NUMBER: _ClassVar[int]
    finding_id: str
    def __init__(self, finding_id: _Optional[str] = ...) -> None: ...

class MemoryGetRequest(_message.Message):
    __slots__ = ("work_id", "operation", "tier", "key", "value")
    WORK_ID_FIELD_NUMBER: _ClassVar[int]
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    TIER_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    work_id: str
    operation: str
    tier: str
    key: str
    value: bytes
    def __init__(self, work_id: _Optional[str] = ..., operation: _Optional[str] = ..., tier: _Optional[str] = ..., key: _Optional[str] = ..., value: _Optional[bytes] = ...) -> None: ...

class MemorySetRequest(_message.Message):
    __slots__ = ("work_id", "operation", "tier", "key", "value")
    WORK_ID_FIELD_NUMBER: _ClassVar[int]
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    TIER_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    work_id: str
    operation: str
    tier: str
    key: str
    value: bytes
    def __init__(self, work_id: _Optional[str] = ..., operation: _Optional[str] = ..., tier: _Optional[str] = ..., key: _Optional[str] = ..., value: _Optional[bytes] = ...) -> None: ...

class MemoryRequest(_message.Message):
    __slots__ = ("work_id", "operation", "tier", "key", "value")
    WORK_ID_FIELD_NUMBER: _ClassVar[int]
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    TIER_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    work_id: str
    operation: str
    tier: str
    key: str
    value: bytes
    def __init__(self, work_id: _Optional[str] = ..., operation: _Optional[str] = ..., tier: _Optional[str] = ..., key: _Optional[str] = ..., value: _Optional[bytes] = ...) -> None: ...

class MemoryResponse(_message.Message):
    __slots__ = ("value", "found")
    VALUE_FIELD_NUMBER: _ClassVar[int]
    FOUND_FIELD_NUMBER: _ClassVar[int]
    value: bytes
    found: bool
    def __init__(self, value: _Optional[bytes] = ..., found: bool = ...) -> None: ...

class MemoryGetResponse(_message.Message):
    __slots__ = ("value", "found")
    VALUE_FIELD_NUMBER: _ClassVar[int]
    FOUND_FIELD_NUMBER: _ClassVar[int]
    value: bytes
    found: bool
    def __init__(self, value: _Optional[bytes] = ..., found: bool = ...) -> None: ...

class MemorySetResponse(_message.Message):
    __slots__ = ("value", "found")
    VALUE_FIELD_NUMBER: _ClassVar[int]
    FOUND_FIELD_NUMBER: _ClassVar[int]
    value: bytes
    found: bool
    def __init__(self, value: _Optional[bytes] = ..., found: bool = ...) -> None: ...

class MemorySearchRequest(_message.Message):
    __slots__ = ("work_id", "tier", "query", "limit")
    WORK_ID_FIELD_NUMBER: _ClassVar[int]
    TIER_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    work_id: str
    tier: str
    query: str
    limit: int
    def __init__(self, work_id: _Optional[str] = ..., tier: _Optional[str] = ..., query: _Optional[str] = ..., limit: _Optional[int] = ...) -> None: ...

class MemorySearchResponse(_message.Message):
    __slots__ = ("results",)
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[MemoryEntry]
    def __init__(self, results: _Optional[_Iterable[_Union[MemoryEntry, _Mapping]]] = ...) -> None: ...

class MemoryEntry(_message.Message):
    __slots__ = ("key", "value", "score")
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    key: str
    value: bytes
    score: float
    def __init__(self, key: _Optional[str] = ..., value: _Optional[bytes] = ..., score: _Optional[float] = ...) -> None: ...

class ComponentError(_message.Message):
    __slots__ = ("code", "message", "retryable")
    CODE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    RETRYABLE_FIELD_NUMBER: _ClassVar[int]
    code: str
    message: str
    retryable: bool
    def __init__(self, code: _Optional[str] = ..., message: _Optional[str] = ..., retryable: bool = ...) -> None: ...

class ListAvailablePluginsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListAvailablePluginsResponse(_message.Message):
    __slots__ = ("plugins",)
    PLUGINS_FIELD_NUMBER: _ClassVar[int]
    plugins: _containers.RepeatedCompositeFieldContainer[PluginCatalogEntryProto]
    def __init__(self, plugins: _Optional[_Iterable[_Union[PluginCatalogEntryProto, _Mapping]]] = ...) -> None: ...

class PluginCatalogEntryProto(_message.Message):
    __slots__ = ("name", "version", "description", "methods", "config_schema_json", "enabled", "configured", "health_status", "source", "instance_count")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    METHODS_FIELD_NUMBER: _ClassVar[int]
    CONFIG_SCHEMA_JSON_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    CONFIGURED_FIELD_NUMBER: _ClassVar[int]
    HEALTH_STATUS_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_COUNT_FIELD_NUMBER: _ClassVar[int]
    name: str
    version: str
    description: str
    methods: _containers.RepeatedScalarFieldContainer[str]
    config_schema_json: str
    enabled: bool
    configured: bool
    health_status: str
    source: str
    instance_count: int
    def __init__(self, name: _Optional[str] = ..., version: _Optional[str] = ..., description: _Optional[str] = ..., methods: _Optional[_Iterable[str]] = ..., config_schema_json: _Optional[str] = ..., enabled: bool = ..., configured: bool = ..., health_status: _Optional[str] = ..., source: _Optional[str] = ..., instance_count: _Optional[int] = ...) -> None: ...

class EnablePluginRequest(_message.Message):
    __slots__ = ("plugin_name", "config_json")
    PLUGIN_NAME_FIELD_NUMBER: _ClassVar[int]
    CONFIG_JSON_FIELD_NUMBER: _ClassVar[int]
    plugin_name: str
    config_json: str
    def __init__(self, plugin_name: _Optional[str] = ..., config_json: _Optional[str] = ...) -> None: ...

class EnablePluginResponse(_message.Message):
    __slots__ = ("success", "message")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    success: bool
    message: str
    def __init__(self, success: bool = ..., message: _Optional[str] = ...) -> None: ...

class DisablePluginRequest(_message.Message):
    __slots__ = ("plugin_name",)
    PLUGIN_NAME_FIELD_NUMBER: _ClassVar[int]
    plugin_name: str
    def __init__(self, plugin_name: _Optional[str] = ...) -> None: ...

class DisablePluginResponse(_message.Message):
    __slots__ = ("success", "message")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    success: bool
    message: str
    def __init__(self, success: bool = ..., message: _Optional[str] = ...) -> None: ...

class UpdatePluginConfigRequest(_message.Message):
    __slots__ = ("plugin_name", "config_json")
    PLUGIN_NAME_FIELD_NUMBER: _ClassVar[int]
    CONFIG_JSON_FIELD_NUMBER: _ClassVar[int]
    plugin_name: str
    config_json: str
    def __init__(self, plugin_name: _Optional[str] = ..., config_json: _Optional[str] = ...) -> None: ...

class UpdatePluginConfigResponse(_message.Message):
    __slots__ = ("success", "message")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    success: bool
    message: str
    def __init__(self, success: bool = ..., message: _Optional[str] = ...) -> None: ...

class GetPluginConfigRequest(_message.Message):
    __slots__ = ("plugin_name",)
    PLUGIN_NAME_FIELD_NUMBER: _ClassVar[int]
    plugin_name: str
    def __init__(self, plugin_name: _Optional[str] = ...) -> None: ...

class GetPluginConfigResponse(_message.Message):
    __slots__ = ("config_json", "config_schema_json")
    CONFIG_JSON_FIELD_NUMBER: _ClassVar[int]
    CONFIG_SCHEMA_JSON_FIELD_NUMBER: _ClassVar[int]
    config_json: str
    config_schema_json: str
    def __init__(self, config_json: _Optional[str] = ..., config_schema_json: _Optional[str] = ...) -> None: ...

class TestPluginConnectionRequest(_message.Message):
    __slots__ = ("plugin_name", "config_json")
    PLUGIN_NAME_FIELD_NUMBER: _ClassVar[int]
    CONFIG_JSON_FIELD_NUMBER: _ClassVar[int]
    plugin_name: str
    config_json: str
    def __init__(self, plugin_name: _Optional[str] = ..., config_json: _Optional[str] = ...) -> None: ...

class TestPluginConnectionResponse(_message.Message):
    __slots__ = ("success", "message", "latency_ms")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    LATENCY_MS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    message: str
    latency_ms: int
    def __init__(self, success: bool = ..., message: _Optional[str] = ..., latency_ms: _Optional[int] = ...) -> None: ...

class ListTenantPluginsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListTenantPluginsResponse(_message.Message):
    __slots__ = ("plugins",)
    PLUGINS_FIELD_NUMBER: _ClassVar[int]
    plugins: _containers.RepeatedCompositeFieldContainer[PluginAccessProto]
    def __init__(self, plugins: _Optional[_Iterable[_Union[PluginAccessProto, _Mapping]]] = ...) -> None: ...

class PluginAccessProto(_message.Message):
    __slots__ = ("tenant_id", "plugin_name", "enabled", "source", "configured_at", "configured_by", "has_config")
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    PLUGIN_NAME_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    CONFIGURED_AT_FIELD_NUMBER: _ClassVar[int]
    CONFIGURED_BY_FIELD_NUMBER: _ClassVar[int]
    HAS_CONFIG_FIELD_NUMBER: _ClassVar[int]
    tenant_id: str
    plugin_name: str
    enabled: bool
    source: str
    configured_at: str
    configured_by: str
    has_config: bool
    def __init__(self, tenant_id: _Optional[str] = ..., plugin_name: _Optional[str] = ..., enabled: bool = ..., source: _Optional[str] = ..., configured_at: _Optional[str] = ..., configured_by: _Optional[str] = ..., has_config: bool = ...) -> None: ...

class ToolDefinition(_message.Message):
    __slots__ = ("name", "description", "input_schema_json")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    INPUT_SCHEMA_JSON_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    input_schema_json: str
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., input_schema_json: _Optional[str] = ...) -> None: ...

class ToolCallResult(_message.Message):
    __slots__ = ("id", "name", "arguments_json")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ARGUMENTS_JSON_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    arguments_json: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., arguments_json: _Optional[str] = ...) -> None: ...

class CompleteWithToolsRequest(_message.Message):
    __slots__ = ("work_id", "slot", "messages", "tools", "timeout_ms")
    WORK_ID_FIELD_NUMBER: _ClassVar[int]
    SLOT_FIELD_NUMBER: _ClassVar[int]
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    TOOLS_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_MS_FIELD_NUMBER: _ClassVar[int]
    work_id: str
    slot: str
    messages: _containers.RepeatedCompositeFieldContainer[LLMMessage]
    tools: _containers.RepeatedCompositeFieldContainer[ToolDefinition]
    timeout_ms: int
    def __init__(self, work_id: _Optional[str] = ..., slot: _Optional[str] = ..., messages: _Optional[_Iterable[_Union[LLMMessage, _Mapping]]] = ..., tools: _Optional[_Iterable[_Union[ToolDefinition, _Mapping]]] = ..., timeout_ms: _Optional[int] = ...) -> None: ...

class CompleteWithToolsResponse(_message.Message):
    __slots__ = ("response", "usage", "tool_calls", "finish_reason")
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    USAGE_FIELD_NUMBER: _ClassVar[int]
    TOOL_CALLS_FIELD_NUMBER: _ClassVar[int]
    FINISH_REASON_FIELD_NUMBER: _ClassVar[int]
    response: LLMMessage
    usage: TokenUsage
    tool_calls: _containers.RepeatedCompositeFieldContainer[ToolCallResult]
    finish_reason: str
    def __init__(self, response: _Optional[_Union[LLMMessage, _Mapping]] = ..., usage: _Optional[_Union[TokenUsage, _Mapping]] = ..., tool_calls: _Optional[_Iterable[_Union[ToolCallResult, _Mapping]]] = ..., finish_reason: _Optional[str] = ...) -> None: ...

class CompleteStructuredRequest(_message.Message):
    __slots__ = ("work_id", "slot", "messages", "schema_json", "timeout_ms")
    WORK_ID_FIELD_NUMBER: _ClassVar[int]
    SLOT_FIELD_NUMBER: _ClassVar[int]
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_JSON_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_MS_FIELD_NUMBER: _ClassVar[int]
    work_id: str
    slot: str
    messages: _containers.RepeatedCompositeFieldContainer[LLMMessage]
    schema_json: str
    timeout_ms: int
    def __init__(self, work_id: _Optional[str] = ..., slot: _Optional[str] = ..., messages: _Optional[_Iterable[_Union[LLMMessage, _Mapping]]] = ..., schema_json: _Optional[str] = ..., timeout_ms: _Optional[int] = ...) -> None: ...

class CompleteStructuredResponse(_message.Message):
    __slots__ = ("result_json", "usage")
    RESULT_JSON_FIELD_NUMBER: _ClassVar[int]
    USAGE_FIELD_NUMBER: _ClassVar[int]
    result_json: str
    usage: TokenUsage
    def __init__(self, result_json: _Optional[str] = ..., usage: _Optional[_Union[TokenUsage, _Mapping]] = ...) -> None: ...

class CallToolStreamRequest(_message.Message):
    __slots__ = ("work_id", "tool_name", "input_json", "timeout_ms")
    WORK_ID_FIELD_NUMBER: _ClassVar[int]
    TOOL_NAME_FIELD_NUMBER: _ClassVar[int]
    INPUT_JSON_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_MS_FIELD_NUMBER: _ClassVar[int]
    work_id: str
    tool_name: str
    input_json: str
    timeout_ms: int
    def __init__(self, work_id: _Optional[str] = ..., tool_name: _Optional[str] = ..., input_json: _Optional[str] = ..., timeout_ms: _Optional[int] = ...) -> None: ...

class CallToolStreamResponse(_message.Message):
    __slots__ = ("event_type", "payload_json", "done", "error")
    EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_JSON_FIELD_NUMBER: _ClassVar[int]
    DONE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    event_type: str
    payload_json: str
    done: bool
    error: ComponentError
    def __init__(self, event_type: _Optional[str] = ..., payload_json: _Optional[str] = ..., done: bool = ..., error: _Optional[_Union[ComponentError, _Mapping]] = ...) -> None: ...

class QueueToolWorkRequest(_message.Message):
    __slots__ = ("work_id", "tool_name", "inputs_json")
    WORK_ID_FIELD_NUMBER: _ClassVar[int]
    TOOL_NAME_FIELD_NUMBER: _ClassVar[int]
    INPUTS_JSON_FIELD_NUMBER: _ClassVar[int]
    work_id: str
    tool_name: str
    inputs_json: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, work_id: _Optional[str] = ..., tool_name: _Optional[str] = ..., inputs_json: _Optional[_Iterable[str]] = ...) -> None: ...

class QueueToolWorkResponse(_message.Message):
    __slots__ = ("job_id",)
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    job_id: str
    def __init__(self, job_id: _Optional[str] = ...) -> None: ...

class ToolResultsRequest(_message.Message):
    __slots__ = ("work_id", "job_id")
    WORK_ID_FIELD_NUMBER: _ClassVar[int]
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    work_id: str
    job_id: str
    def __init__(self, work_id: _Optional[str] = ..., job_id: _Optional[str] = ...) -> None: ...

class ToolResultsResponse(_message.Message):
    __slots__ = ("index", "output_json", "error", "done")
    INDEX_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_JSON_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    DONE_FIELD_NUMBER: _ClassVar[int]
    index: int
    output_json: str
    error: ComponentError
    done: bool
    def __init__(self, index: _Optional[int] = ..., output_json: _Optional[str] = ..., error: _Optional[_Union[ComponentError, _Mapping]] = ..., done: bool = ...) -> None: ...

class ListToolsRequest(_message.Message):
    __slots__ = ("work_id",)
    WORK_ID_FIELD_NUMBER: _ClassVar[int]
    work_id: str
    def __init__(self, work_id: _Optional[str] = ...) -> None: ...

class ToolDescriptorProto(_message.Message):
    __slots__ = ("name", "version", "description", "tags", "input_message_type", "output_message_type")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    INPUT_MESSAGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_MESSAGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    name: str
    version: str
    description: str
    tags: _containers.RepeatedScalarFieldContainer[str]
    input_message_type: str
    output_message_type: str
    def __init__(self, name: _Optional[str] = ..., version: _Optional[str] = ..., description: _Optional[str] = ..., tags: _Optional[_Iterable[str]] = ..., input_message_type: _Optional[str] = ..., output_message_type: _Optional[str] = ...) -> None: ...

class ListToolsResponse(_message.Message):
    __slots__ = ("tools",)
    TOOLS_FIELD_NUMBER: _ClassVar[int]
    tools: _containers.RepeatedCompositeFieldContainer[ToolDescriptorProto]
    def __init__(self, tools: _Optional[_Iterable[_Union[ToolDescriptorProto, _Mapping]]] = ...) -> None: ...

class DelegateToAgentRequest(_message.Message):
    __slots__ = ("work_id", "agent_name", "task_json")
    WORK_ID_FIELD_NUMBER: _ClassVar[int]
    AGENT_NAME_FIELD_NUMBER: _ClassVar[int]
    TASK_JSON_FIELD_NUMBER: _ClassVar[int]
    work_id: str
    agent_name: str
    task_json: bytes
    def __init__(self, work_id: _Optional[str] = ..., agent_name: _Optional[str] = ..., task_json: _Optional[bytes] = ...) -> None: ...

class DelegateToAgentResponse(_message.Message):
    __slots__ = ("result_json",)
    RESULT_JSON_FIELD_NUMBER: _ClassVar[int]
    result_json: bytes
    def __init__(self, result_json: _Optional[bytes] = ...) -> None: ...

class ListAgentsRequest(_message.Message):
    __slots__ = ("work_id",)
    WORK_ID_FIELD_NUMBER: _ClassVar[int]
    work_id: str
    def __init__(self, work_id: _Optional[str] = ...) -> None: ...

class AgentDescriptorProto(_message.Message):
    __slots__ = ("name", "version", "description", "capabilities", "target_types")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    TARGET_TYPES_FIELD_NUMBER: _ClassVar[int]
    name: str
    version: str
    description: str
    capabilities: _containers.RepeatedScalarFieldContainer[str]
    target_types: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, name: _Optional[str] = ..., version: _Optional[str] = ..., description: _Optional[str] = ..., capabilities: _Optional[_Iterable[str]] = ..., target_types: _Optional[_Iterable[str]] = ...) -> None: ...

class ListAgentsResponse(_message.Message):
    __slots__ = ("agents",)
    AGENTS_FIELD_NUMBER: _ClassVar[int]
    agents: _containers.RepeatedCompositeFieldContainer[AgentDescriptorProto]
    def __init__(self, agents: _Optional[_Iterable[_Union[AgentDescriptorProto, _Mapping]]] = ...) -> None: ...

class QueryNodesRequest(_message.Message):
    __slots__ = ("work_id", "query")
    WORK_ID_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    work_id: str
    query: _graphrag_pb2.GraphQuery
    def __init__(self, work_id: _Optional[str] = ..., query: _Optional[_Union[_graphrag_pb2.GraphQuery, _Mapping]] = ...) -> None: ...

class QueryNodesResponse(_message.Message):
    __slots__ = ("results",)
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[_graphrag_pb2.QueryResult]
    def __init__(self, results: _Optional[_Iterable[_Union[_graphrag_pb2.QueryResult, _Mapping]]] = ...) -> None: ...

class StoreNodeRequest(_message.Message):
    __slots__ = ("work_id", "node")
    WORK_ID_FIELD_NUMBER: _ClassVar[int]
    NODE_FIELD_NUMBER: _ClassVar[int]
    work_id: str
    node: _graphrag_pb2.GraphNode
    def __init__(self, work_id: _Optional[str] = ..., node: _Optional[_Union[_graphrag_pb2.GraphNode, _Mapping]] = ...) -> None: ...

class StoreNodeResponse(_message.Message):
    __slots__ = ("node_id",)
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    node_id: str
    def __init__(self, node_id: _Optional[str] = ...) -> None: ...

class FindSimilarAttacksRequest(_message.Message):
    __slots__ = ("work_id", "content", "top_k")
    WORK_ID_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    TOP_K_FIELD_NUMBER: _ClassVar[int]
    work_id: str
    content: str
    top_k: int
    def __init__(self, work_id: _Optional[str] = ..., content: _Optional[str] = ..., top_k: _Optional[int] = ...) -> None: ...

class FindSimilarAttacksResponse(_message.Message):
    __slots__ = ("results_json",)
    RESULTS_JSON_FIELD_NUMBER: _ClassVar[int]
    results_json: bytes
    def __init__(self, results_json: _Optional[bytes] = ...) -> None: ...

class GetAttackChainsRequest(_message.Message):
    __slots__ = ("work_id", "technique_id", "max_depth")
    WORK_ID_FIELD_NUMBER: _ClassVar[int]
    TECHNIQUE_ID_FIELD_NUMBER: _ClassVar[int]
    MAX_DEPTH_FIELD_NUMBER: _ClassVar[int]
    work_id: str
    technique_id: str
    max_depth: int
    def __init__(self, work_id: _Optional[str] = ..., technique_id: _Optional[str] = ..., max_depth: _Optional[int] = ...) -> None: ...

class GetAttackChainsResponse(_message.Message):
    __slots__ = ("results_json",)
    RESULTS_JSON_FIELD_NUMBER: _ClassVar[int]
    results_json: bytes
    def __init__(self, results_json: _Optional[bytes] = ...) -> None: ...

class FindSimilarFindingsRequest(_message.Message):
    __slots__ = ("work_id", "finding_id", "top_k")
    WORK_ID_FIELD_NUMBER: _ClassVar[int]
    FINDING_ID_FIELD_NUMBER: _ClassVar[int]
    TOP_K_FIELD_NUMBER: _ClassVar[int]
    work_id: str
    finding_id: str
    top_k: int
    def __init__(self, work_id: _Optional[str] = ..., finding_id: _Optional[str] = ..., top_k: _Optional[int] = ...) -> None: ...

class FindSimilarFindingsResponse(_message.Message):
    __slots__ = ("results_json",)
    RESULTS_JSON_FIELD_NUMBER: _ClassVar[int]
    results_json: bytes
    def __init__(self, results_json: _Optional[bytes] = ...) -> None: ...

class GetRelatedFindingsRequest(_message.Message):
    __slots__ = ("work_id", "finding_id")
    WORK_ID_FIELD_NUMBER: _ClassVar[int]
    FINDING_ID_FIELD_NUMBER: _ClassVar[int]
    work_id: str
    finding_id: str
    def __init__(self, work_id: _Optional[str] = ..., finding_id: _Optional[str] = ...) -> None: ...

class GetRelatedFindingsResponse(_message.Message):
    __slots__ = ("results_json",)
    RESULTS_JSON_FIELD_NUMBER: _ClassVar[int]
    results_json: bytes
    def __init__(self, results_json: _Optional[bytes] = ...) -> None: ...

class GetFindingsRequest(_message.Message):
    __slots__ = ("work_id", "filter_json")
    WORK_ID_FIELD_NUMBER: _ClassVar[int]
    FILTER_JSON_FIELD_NUMBER: _ClassVar[int]
    work_id: str
    filter_json: bytes
    def __init__(self, work_id: _Optional[str] = ..., filter_json: _Optional[bytes] = ...) -> None: ...

class GetFindingsResponse(_message.Message):
    __slots__ = ("findings_json",)
    FINDINGS_JSON_FIELD_NUMBER: _ClassVar[int]
    findings_json: bytes
    def __init__(self, findings_json: _Optional[bytes] = ...) -> None: ...

class GetRunFindingsRequest(_message.Message):
    __slots__ = ("work_id", "scope", "filter_json")
    WORK_ID_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    FILTER_JSON_FIELD_NUMBER: _ClassVar[int]
    work_id: str
    scope: str
    filter_json: bytes
    def __init__(self, work_id: _Optional[str] = ..., scope: _Optional[str] = ..., filter_json: _Optional[bytes] = ...) -> None: ...

class GetRunFindingsResponse(_message.Message):
    __slots__ = ("findings_json",)
    FINDINGS_JSON_FIELD_NUMBER: _ClassVar[int]
    findings_json: bytes
    def __init__(self, findings_json: _Optional[bytes] = ...) -> None: ...

class MemoryDeleteRequest(_message.Message):
    __slots__ = ("work_id", "tier", "key")
    WORK_ID_FIELD_NUMBER: _ClassVar[int]
    TIER_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    work_id: str
    tier: str
    key: str
    def __init__(self, work_id: _Optional[str] = ..., tier: _Optional[str] = ..., key: _Optional[str] = ...) -> None: ...

class MemoryDeleteResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class MemoryClearRequest(_message.Message):
    __slots__ = ("work_id", "tier")
    WORK_ID_FIELD_NUMBER: _ClassVar[int]
    TIER_FIELD_NUMBER: _ClassVar[int]
    work_id: str
    tier: str
    def __init__(self, work_id: _Optional[str] = ..., tier: _Optional[str] = ...) -> None: ...

class MemoryClearResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class MemoryKeysRequest(_message.Message):
    __slots__ = ("work_id", "tier")
    WORK_ID_FIELD_NUMBER: _ClassVar[int]
    TIER_FIELD_NUMBER: _ClassVar[int]
    work_id: str
    tier: str
    def __init__(self, work_id: _Optional[str] = ..., tier: _Optional[str] = ...) -> None: ...

class MemoryKeysResponse(_message.Message):
    __slots__ = ("keys",)
    KEYS_FIELD_NUMBER: _ClassVar[int]
    keys: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, keys: _Optional[_Iterable[str]] = ...) -> None: ...

class MemoryHistoryRequest(_message.Message):
    __slots__ = ("work_id", "limit")
    WORK_ID_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    work_id: str
    limit: int
    def __init__(self, work_id: _Optional[str] = ..., limit: _Optional[int] = ...) -> None: ...

class MemoryHistoryResponse(_message.Message):
    __slots__ = ("items_json",)
    ITEMS_JSON_FIELD_NUMBER: _ClassVar[int]
    items_json: bytes
    def __init__(self, items_json: _Optional[bytes] = ...) -> None: ...

class MemoryGetPreviousRunValueRequest(_message.Message):
    __slots__ = ("work_id", "key")
    WORK_ID_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    work_id: str
    key: str
    def __init__(self, work_id: _Optional[str] = ..., key: _Optional[str] = ...) -> None: ...

class MemoryGetPreviousRunValueResponse(_message.Message):
    __slots__ = ("value", "found")
    VALUE_FIELD_NUMBER: _ClassVar[int]
    FOUND_FIELD_NUMBER: _ClassVar[int]
    value: bytes
    found: bool
    def __init__(self, value: _Optional[bytes] = ..., found: bool = ...) -> None: ...

class MemoryGetValueHistoryRequest(_message.Message):
    __slots__ = ("work_id", "key")
    WORK_ID_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    work_id: str
    key: str
    def __init__(self, work_id: _Optional[str] = ..., key: _Optional[str] = ...) -> None: ...

class MemoryGetValueHistoryResponse(_message.Message):
    __slots__ = ("history_json",)
    HISTORY_JSON_FIELD_NUMBER: _ClassVar[int]
    history_json: bytes
    def __init__(self, history_json: _Optional[bytes] = ...) -> None: ...

class CreateMissionRequest(_message.Message):
    __slots__ = ("work_id", "mission_definition_json", "target_id", "opts_json")
    WORK_ID_FIELD_NUMBER: _ClassVar[int]
    MISSION_DEFINITION_JSON_FIELD_NUMBER: _ClassVar[int]
    TARGET_ID_FIELD_NUMBER: _ClassVar[int]
    OPTS_JSON_FIELD_NUMBER: _ClassVar[int]
    work_id: str
    mission_definition_json: bytes
    target_id: str
    opts_json: bytes
    def __init__(self, work_id: _Optional[str] = ..., mission_definition_json: _Optional[bytes] = ..., target_id: _Optional[str] = ..., opts_json: _Optional[bytes] = ...) -> None: ...

class CreateMissionResponse(_message.Message):
    __slots__ = ("mission_json",)
    MISSION_JSON_FIELD_NUMBER: _ClassVar[int]
    mission_json: bytes
    def __init__(self, mission_json: _Optional[bytes] = ...) -> None: ...

class RunMissionRequest(_message.Message):
    __slots__ = ("work_id", "mission_id", "opts_json")
    WORK_ID_FIELD_NUMBER: _ClassVar[int]
    MISSION_ID_FIELD_NUMBER: _ClassVar[int]
    OPTS_JSON_FIELD_NUMBER: _ClassVar[int]
    work_id: str
    mission_id: str
    opts_json: bytes
    def __init__(self, work_id: _Optional[str] = ..., mission_id: _Optional[str] = ..., opts_json: _Optional[bytes] = ...) -> None: ...

class RunMissionResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetMissionStatusRequest(_message.Message):
    __slots__ = ("work_id", "mission_id")
    WORK_ID_FIELD_NUMBER: _ClassVar[int]
    MISSION_ID_FIELD_NUMBER: _ClassVar[int]
    work_id: str
    mission_id: str
    def __init__(self, work_id: _Optional[str] = ..., mission_id: _Optional[str] = ...) -> None: ...

class GetMissionStatusResponse(_message.Message):
    __slots__ = ("status_json",)
    STATUS_JSON_FIELD_NUMBER: _ClassVar[int]
    status_json: bytes
    def __init__(self, status_json: _Optional[bytes] = ...) -> None: ...

class WaitMissionRequest(_message.Message):
    __slots__ = ("work_id", "mission_id", "timeout_ms")
    WORK_ID_FIELD_NUMBER: _ClassVar[int]
    MISSION_ID_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_MS_FIELD_NUMBER: _ClassVar[int]
    work_id: str
    mission_id: str
    timeout_ms: int
    def __init__(self, work_id: _Optional[str] = ..., mission_id: _Optional[str] = ..., timeout_ms: _Optional[int] = ...) -> None: ...

class WaitMissionResponse(_message.Message):
    __slots__ = ("result_json",)
    RESULT_JSON_FIELD_NUMBER: _ClassVar[int]
    result_json: bytes
    def __init__(self, result_json: _Optional[bytes] = ...) -> None: ...

class ListMissionsRequest(_message.Message):
    __slots__ = ("work_id", "filter_json")
    WORK_ID_FIELD_NUMBER: _ClassVar[int]
    FILTER_JSON_FIELD_NUMBER: _ClassVar[int]
    work_id: str
    filter_json: bytes
    def __init__(self, work_id: _Optional[str] = ..., filter_json: _Optional[bytes] = ...) -> None: ...

class ListMissionsResponse(_message.Message):
    __slots__ = ("missions_json",)
    MISSIONS_JSON_FIELD_NUMBER: _ClassVar[int]
    missions_json: bytes
    def __init__(self, missions_json: _Optional[bytes] = ...) -> None: ...

class CancelMissionRequest(_message.Message):
    __slots__ = ("work_id", "mission_id")
    WORK_ID_FIELD_NUMBER: _ClassVar[int]
    MISSION_ID_FIELD_NUMBER: _ClassVar[int]
    work_id: str
    mission_id: str
    def __init__(self, work_id: _Optional[str] = ..., mission_id: _Optional[str] = ...) -> None: ...

class CancelMissionResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetMissionResultsRequest(_message.Message):
    __slots__ = ("work_id", "mission_id")
    WORK_ID_FIELD_NUMBER: _ClassVar[int]
    MISSION_ID_FIELD_NUMBER: _ClassVar[int]
    work_id: str
    mission_id: str
    def __init__(self, work_id: _Optional[str] = ..., mission_id: _Optional[str] = ...) -> None: ...

class GetMissionResultsResponse(_message.Message):
    __slots__ = ("result_json",)
    RESULT_JSON_FIELD_NUMBER: _ClassVar[int]
    result_json: bytes
    def __init__(self, result_json: _Optional[bytes] = ...) -> None: ...

class GetCredentialRequest(_message.Message):
    __slots__ = ("work_id", "name")
    WORK_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    work_id: str
    name: str
    def __init__(self, work_id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class GetCredentialResponse(_message.Message):
    __slots__ = ("credential_json",)
    CREDENTIAL_JSON_FIELD_NUMBER: _ClassVar[int]
    credential_json: bytes
    def __init__(self, credential_json: _Optional[bytes] = ...) -> None: ...

class GetTaxonomySchemaRequest(_message.Message):
    __slots__ = ("work_id",)
    WORK_ID_FIELD_NUMBER: _ClassVar[int]
    work_id: str
    def __init__(self, work_id: _Optional[str] = ...) -> None: ...

class GetTaxonomySchemaResponse(_message.Message):
    __slots__ = ("schema_json",)
    SCHEMA_JSON_FIELD_NUMBER: _ClassVar[int]
    schema_json: bytes
    def __init__(self, schema_json: _Optional[bytes] = ...) -> None: ...

class GetMissionRunHistoryRequest(_message.Message):
    __slots__ = ("work_id",)
    WORK_ID_FIELD_NUMBER: _ClassVar[int]
    work_id: str
    def __init__(self, work_id: _Optional[str] = ...) -> None: ...

class GetMissionRunHistoryResponse(_message.Message):
    __slots__ = ("runs_json",)
    RUNS_JSON_FIELD_NUMBER: _ClassVar[int]
    runs_json: bytes
    def __init__(self, runs_json: _Optional[bytes] = ...) -> None: ...

class ReportStepHintsRequest(_message.Message):
    __slots__ = ("work_id", "hints_json")
    WORK_ID_FIELD_NUMBER: _ClassVar[int]
    HINTS_JSON_FIELD_NUMBER: _ClassVar[int]
    work_id: str
    hints_json: bytes
    def __init__(self, work_id: _Optional[str] = ..., hints_json: _Optional[bytes] = ...) -> None: ...

class ReportStepHintsResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
