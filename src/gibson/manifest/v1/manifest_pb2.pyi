import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from gibson.identity.v1 import identity_pb2 as _identity_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ToolIdempotency(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TOOL_IDEMPOTENCY_UNSPECIFIED: _ClassVar[ToolIdempotency]
    TOOL_IDEMPOTENCY_AT_MOST_ONCE: _ClassVar[ToolIdempotency]
    TOOL_IDEMPOTENCY_AT_LEAST_ONCE: _ClassVar[ToolIdempotency]
    TOOL_IDEMPOTENCY_EXACTLY_ONCE: _ClassVar[ToolIdempotency]
TOOL_IDEMPOTENCY_UNSPECIFIED: ToolIdempotency
TOOL_IDEMPOTENCY_AT_MOST_ONCE: ToolIdempotency
TOOL_IDEMPOTENCY_AT_LEAST_ONCE: ToolIdempotency
TOOL_IDEMPOTENCY_EXACTLY_ONCE: ToolIdempotency

class CapabilityManifest(_message.Message):
    __slots__ = ("manifest_id", "manifest_version", "tenant_id", "subject", "issued_at", "expires_at", "ttl_seconds", "tenant_context", "agents", "tools", "plugins", "cross_component_rules", "cross_component_rules_truncated", "limits", "available_llm_slots", "memory", "signature", "signing_key_id")
    MANIFEST_ID_FIELD_NUMBER: _ClassVar[int]
    MANIFEST_VERSION_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_FIELD_NUMBER: _ClassVar[int]
    ISSUED_AT_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    TTL_SECONDS_FIELD_NUMBER: _ClassVar[int]
    TENANT_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    AGENTS_FIELD_NUMBER: _ClassVar[int]
    TOOLS_FIELD_NUMBER: _ClassVar[int]
    PLUGINS_FIELD_NUMBER: _ClassVar[int]
    CROSS_COMPONENT_RULES_FIELD_NUMBER: _ClassVar[int]
    CROSS_COMPONENT_RULES_TRUNCATED_FIELD_NUMBER: _ClassVar[int]
    LIMITS_FIELD_NUMBER: _ClassVar[int]
    AVAILABLE_LLM_SLOTS_FIELD_NUMBER: _ClassVar[int]
    MEMORY_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    SIGNING_KEY_ID_FIELD_NUMBER: _ClassVar[int]
    manifest_id: str
    manifest_version: int
    tenant_id: str
    subject: str
    issued_at: _timestamp_pb2.Timestamp
    expires_at: _timestamp_pb2.Timestamp
    ttl_seconds: int
    tenant_context: TenantContext
    agents: _containers.RepeatedCompositeFieldContainer[ComponentCapability]
    tools: _containers.RepeatedCompositeFieldContainer[ComponentCapability]
    plugins: _containers.RepeatedCompositeFieldContainer[ComponentCapability]
    cross_component_rules: _containers.RepeatedCompositeFieldContainer[CrossComponentRule]
    cross_component_rules_truncated: bool
    limits: LimitsAndQuotas
    available_llm_slots: _containers.RepeatedScalarFieldContainer[str]
    memory: MemoryPermissions
    signature: bytes
    signing_key_id: str
    def __init__(self, manifest_id: _Optional[str] = ..., manifest_version: _Optional[int] = ..., tenant_id: _Optional[str] = ..., subject: _Optional[str] = ..., issued_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., expires_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., ttl_seconds: _Optional[int] = ..., tenant_context: _Optional[_Union[TenantContext, _Mapping]] = ..., agents: _Optional[_Iterable[_Union[ComponentCapability, _Mapping]]] = ..., tools: _Optional[_Iterable[_Union[ComponentCapability, _Mapping]]] = ..., plugins: _Optional[_Iterable[_Union[ComponentCapability, _Mapping]]] = ..., cross_component_rules: _Optional[_Iterable[_Union[CrossComponentRule, _Mapping]]] = ..., cross_component_rules_truncated: bool = ..., limits: _Optional[_Union[LimitsAndQuotas, _Mapping]] = ..., available_llm_slots: _Optional[_Iterable[str]] = ..., memory: _Optional[_Union[MemoryPermissions, _Mapping]] = ..., signature: _Optional[bytes] = ..., signing_key_id: _Optional[str] = ...) -> None: ...

class TenantContext(_message.Message):
    __slots__ = ("tenant_id", "tenant_display_name", "team_memberships", "is_admin")
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    TENANT_DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    TEAM_MEMBERSHIPS_FIELD_NUMBER: _ClassVar[int]
    IS_ADMIN_FIELD_NUMBER: _ClassVar[int]
    tenant_id: str
    tenant_display_name: str
    team_memberships: _containers.RepeatedScalarFieldContainer[str]
    is_admin: bool
    def __init__(self, tenant_id: _Optional[str] = ..., tenant_display_name: _Optional[str] = ..., team_memberships: _Optional[_Iterable[str]] = ..., is_admin: bool = ...) -> None: ...

class ComponentCapability(_message.Message):
    __slots__ = ("name", "kind", "component_ref", "version", "description", "is_system", "owner_tenant", "permissions", "agent_contract", "tool_contract", "plugin_contract", "liveness", "principal_kind")
    NAME_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    COMPONENT_REF_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    IS_SYSTEM_FIELD_NUMBER: _ClassVar[int]
    OWNER_TENANT_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    AGENT_CONTRACT_FIELD_NUMBER: _ClassVar[int]
    TOOL_CONTRACT_FIELD_NUMBER: _ClassVar[int]
    PLUGIN_CONTRACT_FIELD_NUMBER: _ClassVar[int]
    LIVENESS_FIELD_NUMBER: _ClassVar[int]
    PRINCIPAL_KIND_FIELD_NUMBER: _ClassVar[int]
    name: str
    kind: str
    component_ref: str
    version: str
    description: str
    is_system: bool
    owner_tenant: str
    permissions: _containers.RepeatedScalarFieldContainer[str]
    agent_contract: AgentContract
    tool_contract: ToolContract
    plugin_contract: PluginContract
    liveness: ComponentLiveness
    principal_kind: _identity_pb2.PrincipalKind
    def __init__(self, name: _Optional[str] = ..., kind: _Optional[str] = ..., component_ref: _Optional[str] = ..., version: _Optional[str] = ..., description: _Optional[str] = ..., is_system: bool = ..., owner_tenant: _Optional[str] = ..., permissions: _Optional[_Iterable[str]] = ..., agent_contract: _Optional[_Union[AgentContract, _Mapping]] = ..., tool_contract: _Optional[_Union[ToolContract, _Mapping]] = ..., plugin_contract: _Optional[_Union[PluginContract, _Mapping]] = ..., liveness: _Optional[_Union[ComponentLiveness, _Mapping]] = ..., principal_kind: _Optional[_Union[_identity_pb2.PrincipalKind, str]] = ...) -> None: ...

class AgentContract(_message.Message):
    __slots__ = ("llm_slot_names", "declared_tool_dependencies", "declared_plugin_dependencies")
    LLM_SLOT_NAMES_FIELD_NUMBER: _ClassVar[int]
    DECLARED_TOOL_DEPENDENCIES_FIELD_NUMBER: _ClassVar[int]
    DECLARED_PLUGIN_DEPENDENCIES_FIELD_NUMBER: _ClassVar[int]
    llm_slot_names: _containers.RepeatedScalarFieldContainer[str]
    declared_tool_dependencies: _containers.RepeatedScalarFieldContainer[str]
    declared_plugin_dependencies: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, llm_slot_names: _Optional[_Iterable[str]] = ..., declared_tool_dependencies: _Optional[_Iterable[str]] = ..., declared_plugin_dependencies: _Optional[_Iterable[str]] = ...) -> None: ...

class ToolContract(_message.Message):
    __slots__ = ("input_proto_name", "output_proto_name", "input_schema_json", "output_schema_json", "idempotency")
    INPUT_PROTO_NAME_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_PROTO_NAME_FIELD_NUMBER: _ClassVar[int]
    INPUT_SCHEMA_JSON_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_SCHEMA_JSON_FIELD_NUMBER: _ClassVar[int]
    IDEMPOTENCY_FIELD_NUMBER: _ClassVar[int]
    input_proto_name: str
    output_proto_name: str
    input_schema_json: str
    output_schema_json: str
    idempotency: ToolIdempotency
    def __init__(self, input_proto_name: _Optional[str] = ..., output_proto_name: _Optional[str] = ..., input_schema_json: _Optional[str] = ..., output_schema_json: _Optional[str] = ..., idempotency: _Optional[_Union[ToolIdempotency, str]] = ...) -> None: ...

class PluginContract(_message.Message):
    __slots__ = ("methods",)
    METHODS_FIELD_NUMBER: _ClassVar[int]
    methods: _containers.RepeatedCompositeFieldContainer[PluginMethod]
    def __init__(self, methods: _Optional[_Iterable[_Union[PluginMethod, _Mapping]]] = ...) -> None: ...

class PluginMethod(_message.Message):
    __slots__ = ("name", "params_schema_json", "result_schema_json", "can_invoke")
    NAME_FIELD_NUMBER: _ClassVar[int]
    PARAMS_SCHEMA_JSON_FIELD_NUMBER: _ClassVar[int]
    RESULT_SCHEMA_JSON_FIELD_NUMBER: _ClassVar[int]
    CAN_INVOKE_FIELD_NUMBER: _ClassVar[int]
    name: str
    params_schema_json: str
    result_schema_json: str
    can_invoke: bool
    def __init__(self, name: _Optional[str] = ..., params_schema_json: _Optional[str] = ..., result_schema_json: _Optional[str] = ..., can_invoke: bool = ...) -> None: ...

class CrossComponentRule(_message.Message):
    __slots__ = ("source_component_ref", "target_component_ref", "effect", "reason")
    class Effect(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        EFFECT_UNSPECIFIED: _ClassVar[CrossComponentRule.Effect]
        EFFECT_ALLOW: _ClassVar[CrossComponentRule.Effect]
        EFFECT_DENY: _ClassVar[CrossComponentRule.Effect]
    EFFECT_UNSPECIFIED: CrossComponentRule.Effect
    EFFECT_ALLOW: CrossComponentRule.Effect
    EFFECT_DENY: CrossComponentRule.Effect
    SOURCE_COMPONENT_REF_FIELD_NUMBER: _ClassVar[int]
    TARGET_COMPONENT_REF_FIELD_NUMBER: _ClassVar[int]
    EFFECT_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    source_component_ref: str
    target_component_ref: str
    effect: CrossComponentRule.Effect
    reason: str
    def __init__(self, source_component_ref: _Optional[str] = ..., target_component_ref: _Optional[str] = ..., effect: _Optional[_Union[CrossComponentRule.Effect, str]] = ..., reason: _Optional[str] = ...) -> None: ...

class LimitsAndQuotas(_message.Message):
    __slots__ = ("max_tokens_per_call", "max_tokens_per_session", "rate_limit_per_minute", "max_spend_usd")
    MAX_TOKENS_PER_CALL_FIELD_NUMBER: _ClassVar[int]
    MAX_TOKENS_PER_SESSION_FIELD_NUMBER: _ClassVar[int]
    RATE_LIMIT_PER_MINUTE_FIELD_NUMBER: _ClassVar[int]
    MAX_SPEND_USD_FIELD_NUMBER: _ClassVar[int]
    max_tokens_per_call: int
    max_tokens_per_session: int
    rate_limit_per_minute: int
    max_spend_usd: str
    def __init__(self, max_tokens_per_call: _Optional[int] = ..., max_tokens_per_session: _Optional[int] = ..., rate_limit_per_minute: _Optional[int] = ..., max_spend_usd: _Optional[str] = ...) -> None: ...

class MemoryPermissions(_message.Message):
    __slots__ = ("working", "mission", "longterm")
    WORKING_FIELD_NUMBER: _ClassVar[int]
    MISSION_FIELD_NUMBER: _ClassVar[int]
    LONGTERM_FIELD_NUMBER: _ClassVar[int]
    working: str
    mission: str
    longterm: str
    def __init__(self, working: _Optional[str] = ..., mission: _Optional[str] = ..., longterm: _Optional[str] = ...) -> None: ...

class ComponentLiveness(_message.Message):
    __slots__ = ("status", "last_heartbeat", "instance_count")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    LAST_HEARTBEAT_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_COUNT_FIELD_NUMBER: _ClassVar[int]
    status: str
    last_heartbeat: _timestamp_pb2.Timestamp
    instance_count: int
    def __init__(self, status: _Optional[str] = ..., last_heartbeat: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., instance_count: _Optional[int] = ...) -> None: ...

class GetCapabilityManifestRequest(_message.Message):
    __slots__ = ("agent_principal_id",)
    AGENT_PRINCIPAL_ID_FIELD_NUMBER: _ClassVar[int]
    agent_principal_id: str
    def __init__(self, agent_principal_id: _Optional[str] = ...) -> None: ...

class GetCapabilityManifestResponse(_message.Message):
    __slots__ = ("manifest",)
    MANIFEST_FIELD_NUMBER: _ClassVar[int]
    manifest: CapabilityManifest
    def __init__(self, manifest: _Optional[_Union[CapabilityManifest, _Mapping]] = ...) -> None: ...

class WatchManifestInvalidationsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class WatchManifestInvalidationsResponse(_message.Message):
    __slots__ = ("event",)
    EVENT_FIELD_NUMBER: _ClassVar[int]
    event: ManifestInvalidationEvent
    def __init__(self, event: _Optional[_Union[ManifestInvalidationEvent, _Mapping]] = ...) -> None: ...

class ManifestInvalidationEvent(_message.Message):
    __slots__ = ("event_type", "tenant_id", "reason", "new_manifest_version", "emitted_at")
    class EventType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        EVENT_TYPE_UNSPECIFIED: _ClassVar[ManifestInvalidationEvent.EventType]
        EVENT_TYPE_HEARTBEAT: _ClassVar[ManifestInvalidationEvent.EventType]
        EVENT_TYPE_INVALIDATED: _ClassVar[ManifestInvalidationEvent.EventType]
    EVENT_TYPE_UNSPECIFIED: ManifestInvalidationEvent.EventType
    EVENT_TYPE_HEARTBEAT: ManifestInvalidationEvent.EventType
    EVENT_TYPE_INVALIDATED: ManifestInvalidationEvent.EventType
    EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    NEW_MANIFEST_VERSION_FIELD_NUMBER: _ClassVar[int]
    EMITTED_AT_FIELD_NUMBER: _ClassVar[int]
    event_type: ManifestInvalidationEvent.EventType
    tenant_id: str
    reason: str
    new_manifest_version: int
    emitted_at: _timestamp_pb2.Timestamp
    def __init__(self, event_type: _Optional[_Union[ManifestInvalidationEvent.EventType, str]] = ..., tenant_id: _Optional[str] = ..., reason: _Optional[str] = ..., new_manifest_version: _Optional[int] = ..., emitted_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
