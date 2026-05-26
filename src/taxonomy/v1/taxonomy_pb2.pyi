from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CoreNodeType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CORE_NODE_TYPE_UNSPECIFIED: _ClassVar[CoreNodeType]
    CORE_NODE_TYPE_MISSION: _ClassVar[CoreNodeType]
    CORE_NODE_TYPE_MISSION_RUN: _ClassVar[CoreNodeType]
    CORE_NODE_TYPE_AGENT_RUN: _ClassVar[CoreNodeType]
    CORE_NODE_TYPE_TOOL_EXECUTION: _ClassVar[CoreNodeType]
    CORE_NODE_TYPE_LLM_CALL: _ClassVar[CoreNodeType]
    CORE_NODE_TYPE_DOMAIN: _ClassVar[CoreNodeType]
    CORE_NODE_TYPE_SUBDOMAIN: _ClassVar[CoreNodeType]
    CORE_NODE_TYPE_HOST: _ClassVar[CoreNodeType]
    CORE_NODE_TYPE_PORT: _ClassVar[CoreNodeType]
    CORE_NODE_TYPE_SERVICE: _ClassVar[CoreNodeType]
    CORE_NODE_TYPE_ENDPOINT: _ClassVar[CoreNodeType]
    CORE_NODE_TYPE_TECHNOLOGY: _ClassVar[CoreNodeType]
    CORE_NODE_TYPE_CERTIFICATE: _ClassVar[CoreNodeType]
    CORE_NODE_TYPE_FINDING: _ClassVar[CoreNodeType]
    CORE_NODE_TYPE_EVIDENCE: _ClassVar[CoreNodeType]
    CORE_NODE_TYPE_TECHNIQUE: _ClassVar[CoreNodeType]
    CORE_NODE_TYPE_COMPLIANCE_SIGNAL: _ClassVar[CoreNodeType]

class CoreRelationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CORE_RELATION_TYPE_UNSPECIFIED: _ClassVar[CoreRelationType]
    CORE_RELATION_TYPE_USED_TOOL: _ClassVar[CoreRelationType]
    CORE_RELATION_TYPE_DELEGATED_TO: _ClassVar[CoreRelationType]
    CORE_RELATION_TYPE_EMITTED_SIGNAL: _ClassVar[CoreRelationType]
    CORE_RELATION_TYPE_T_R_I_G_G_E_R_E_D: _ClassVar[CoreRelationType]
    CORE_RELATION_TYPE_HAS_SUBDOMAIN: _ClassVar[CoreRelationType]
    CORE_RELATION_TYPE_RESOLVES_TO: _ClassVar[CoreRelationType]
    CORE_RELATION_TYPE_HAS_PORT: _ClassVar[CoreRelationType]
    CORE_RELATION_TYPE_RUNS_SERVICE: _ClassVar[CoreRelationType]
    CORE_RELATION_TYPE_HAS_ENDPOINT: _ClassVar[CoreRelationType]
    CORE_RELATION_TYPE_USES_TECHNOLOGY: _ClassVar[CoreRelationType]
    CORE_RELATION_TYPE_SERVES_CERTIFICATE: _ClassVar[CoreRelationType]
    CORE_RELATION_TYPE_A_F_F_E_C_T_S: _ClassVar[CoreRelationType]
    CORE_RELATION_TYPE_HAS_EVIDENCE: _ClassVar[CoreRelationType]
    CORE_RELATION_TYPE_USES_TECHNIQUE: _ClassVar[CoreRelationType]
    CORE_RELATION_TYPE_LEADS_TO: _ClassVar[CoreRelationType]
CORE_NODE_TYPE_UNSPECIFIED: CoreNodeType
CORE_NODE_TYPE_MISSION: CoreNodeType
CORE_NODE_TYPE_MISSION_RUN: CoreNodeType
CORE_NODE_TYPE_AGENT_RUN: CoreNodeType
CORE_NODE_TYPE_TOOL_EXECUTION: CoreNodeType
CORE_NODE_TYPE_LLM_CALL: CoreNodeType
CORE_NODE_TYPE_DOMAIN: CoreNodeType
CORE_NODE_TYPE_SUBDOMAIN: CoreNodeType
CORE_NODE_TYPE_HOST: CoreNodeType
CORE_NODE_TYPE_PORT: CoreNodeType
CORE_NODE_TYPE_SERVICE: CoreNodeType
CORE_NODE_TYPE_ENDPOINT: CoreNodeType
CORE_NODE_TYPE_TECHNOLOGY: CoreNodeType
CORE_NODE_TYPE_CERTIFICATE: CoreNodeType
CORE_NODE_TYPE_FINDING: CoreNodeType
CORE_NODE_TYPE_EVIDENCE: CoreNodeType
CORE_NODE_TYPE_TECHNIQUE: CoreNodeType
CORE_NODE_TYPE_COMPLIANCE_SIGNAL: CoreNodeType
CORE_RELATION_TYPE_UNSPECIFIED: CoreRelationType
CORE_RELATION_TYPE_USED_TOOL: CoreRelationType
CORE_RELATION_TYPE_DELEGATED_TO: CoreRelationType
CORE_RELATION_TYPE_EMITTED_SIGNAL: CoreRelationType
CORE_RELATION_TYPE_T_R_I_G_G_E_R_E_D: CoreRelationType
CORE_RELATION_TYPE_HAS_SUBDOMAIN: CoreRelationType
CORE_RELATION_TYPE_RESOLVES_TO: CoreRelationType
CORE_RELATION_TYPE_HAS_PORT: CoreRelationType
CORE_RELATION_TYPE_RUNS_SERVICE: CoreRelationType
CORE_RELATION_TYPE_HAS_ENDPOINT: CoreRelationType
CORE_RELATION_TYPE_USES_TECHNOLOGY: CoreRelationType
CORE_RELATION_TYPE_SERVES_CERTIFICATE: CoreRelationType
CORE_RELATION_TYPE_A_F_F_E_C_T_S: CoreRelationType
CORE_RELATION_TYPE_HAS_EVIDENCE: CoreRelationType
CORE_RELATION_TYPE_USES_TECHNIQUE: CoreRelationType
CORE_RELATION_TYPE_LEADS_TO: CoreRelationType

class Value(_message.Message):
    __slots__ = ("string_value", "int_value", "double_value", "bool_value", "bytes_value", "timestamp_value", "list_value", "map_value")
    STRING_VALUE_FIELD_NUMBER: _ClassVar[int]
    INT_VALUE_FIELD_NUMBER: _ClassVar[int]
    DOUBLE_VALUE_FIELD_NUMBER: _ClassVar[int]
    BOOL_VALUE_FIELD_NUMBER: _ClassVar[int]
    BYTES_VALUE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_VALUE_FIELD_NUMBER: _ClassVar[int]
    LIST_VALUE_FIELD_NUMBER: _ClassVar[int]
    MAP_VALUE_FIELD_NUMBER: _ClassVar[int]
    string_value: str
    int_value: int
    double_value: float
    bool_value: bool
    bytes_value: bytes
    timestamp_value: int
    list_value: ListValue
    map_value: MapValue
    def __init__(self, string_value: _Optional[str] = ..., int_value: _Optional[int] = ..., double_value: _Optional[float] = ..., bool_value: bool = ..., bytes_value: _Optional[bytes] = ..., timestamp_value: _Optional[int] = ..., list_value: _Optional[_Union[ListValue, _Mapping]] = ..., map_value: _Optional[_Union[MapValue, _Mapping]] = ...) -> None: ...

class ListValue(_message.Message):
    __slots__ = ("values",)
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedCompositeFieldContainer[Value]
    def __init__(self, values: _Optional[_Iterable[_Union[Value, _Mapping]]] = ...) -> None: ...

class MapValue(_message.Message):
    __slots__ = ("fields",)
    class FieldsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: Value
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[Value, _Mapping]] = ...) -> None: ...
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    fields: _containers.MessageMap[str, Value]
    def __init__(self, fields: _Optional[_Mapping[str, Value]] = ...) -> None: ...

class GraphNode(_message.Message):
    __slots__ = ("id", "type", "properties", "parent_id", "parent_type", "parent_relationship", "mission_id", "mission_run_id", "agent_run_id", "discovered_by", "discovered_at", "created_at", "updated_at")
    class PropertiesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: Value
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[Value, _Mapping]] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    PARENT_ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    PARENT_RELATIONSHIP_FIELD_NUMBER: _ClassVar[int]
    MISSION_ID_FIELD_NUMBER: _ClassVar[int]
    MISSION_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    AGENT_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    DISCOVERED_BY_FIELD_NUMBER: _ClassVar[int]
    DISCOVERED_AT_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    type: str
    properties: _containers.MessageMap[str, Value]
    parent_id: str
    parent_type: str
    parent_relationship: str
    mission_id: str
    mission_run_id: str
    agent_run_id: str
    discovered_by: str
    discovered_at: int
    created_at: int
    updated_at: int
    def __init__(self, id: _Optional[str] = ..., type: _Optional[str] = ..., properties: _Optional[_Mapping[str, Value]] = ..., parent_id: _Optional[str] = ..., parent_type: _Optional[str] = ..., parent_relationship: _Optional[str] = ..., mission_id: _Optional[str] = ..., mission_run_id: _Optional[str] = ..., agent_run_id: _Optional[str] = ..., discovered_by: _Optional[str] = ..., discovered_at: _Optional[int] = ..., created_at: _Optional[int] = ..., updated_at: _Optional[int] = ...) -> None: ...

class Relationship(_message.Message):
    __slots__ = ("id", "from_id", "to_id", "type", "properties", "weight", "mission_id", "mission_run_id", "created_at")
    class PropertiesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: Value
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[Value, _Mapping]] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    FROM_ID_FIELD_NUMBER: _ClassVar[int]
    TO_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    WEIGHT_FIELD_NUMBER: _ClassVar[int]
    MISSION_ID_FIELD_NUMBER: _ClassVar[int]
    MISSION_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    from_id: str
    to_id: str
    type: str
    properties: _containers.MessageMap[str, Value]
    weight: float
    mission_id: str
    mission_run_id: str
    created_at: int
    def __init__(self, id: _Optional[str] = ..., from_id: _Optional[str] = ..., to_id: _Optional[str] = ..., type: _Optional[str] = ..., properties: _Optional[_Mapping[str, Value]] = ..., weight: _Optional[float] = ..., mission_id: _Optional[str] = ..., mission_run_id: _Optional[str] = ..., created_at: _Optional[int] = ...) -> None: ...

class Mission(_message.Message):
    __slots__ = ("id", "name", "target", "status", "description", "started_at", "completed_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    STARTED_AT_FIELD_NUMBER: _ClassVar[int]
    COMPLETED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    target: str
    status: str
    description: str
    started_at: int
    completed_at: int
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., target: _Optional[str] = ..., status: _Optional[str] = ..., description: _Optional[str] = ..., started_at: _Optional[int] = ..., completed_at: _Optional[int] = ...) -> None: ...

class MissionRun(_message.Message):
    __slots__ = ("id", "run_number", "status", "started_at", "completed_at", "actor_id", "actor_tenant_id", "api_key_id", "mission_yaml_digest", "parent_mission_id")
    ID_FIELD_NUMBER: _ClassVar[int]
    RUN_NUMBER_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    STARTED_AT_FIELD_NUMBER: _ClassVar[int]
    COMPLETED_AT_FIELD_NUMBER: _ClassVar[int]
    ACTOR_ID_FIELD_NUMBER: _ClassVar[int]
    ACTOR_TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    API_KEY_ID_FIELD_NUMBER: _ClassVar[int]
    MISSION_YAML_DIGEST_FIELD_NUMBER: _ClassVar[int]
    PARENT_MISSION_ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    run_number: int
    status: str
    started_at: int
    completed_at: int
    actor_id: str
    actor_tenant_id: str
    api_key_id: str
    mission_yaml_digest: str
    parent_mission_id: str
    def __init__(self, id: _Optional[str] = ..., run_number: _Optional[int] = ..., status: _Optional[str] = ..., started_at: _Optional[int] = ..., completed_at: _Optional[int] = ..., actor_id: _Optional[str] = ..., actor_tenant_id: _Optional[str] = ..., api_key_id: _Optional[str] = ..., mission_yaml_digest: _Optional[str] = ..., parent_mission_id: _Optional[str] = ...) -> None: ...

class AgentRun(_message.Message):
    __slots__ = ("id", "agent_name", "mission_run_id", "status", "started_at", "completed_at", "error_message", "actor_id", "actor_tenant_id", "api_key_id", "component_name", "component_version", "system_owned", "parent_agent_run_id", "delegation_depth")
    ID_FIELD_NUMBER: _ClassVar[int]
    AGENT_NAME_FIELD_NUMBER: _ClassVar[int]
    MISSION_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    STARTED_AT_FIELD_NUMBER: _ClassVar[int]
    COMPLETED_AT_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ACTOR_ID_FIELD_NUMBER: _ClassVar[int]
    ACTOR_TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    API_KEY_ID_FIELD_NUMBER: _ClassVar[int]
    COMPONENT_NAME_FIELD_NUMBER: _ClassVar[int]
    COMPONENT_VERSION_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_OWNED_FIELD_NUMBER: _ClassVar[int]
    PARENT_AGENT_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    DELEGATION_DEPTH_FIELD_NUMBER: _ClassVar[int]
    id: str
    agent_name: str
    mission_run_id: str
    status: str
    started_at: int
    completed_at: int
    error_message: str
    actor_id: str
    actor_tenant_id: str
    api_key_id: str
    component_name: str
    component_version: str
    system_owned: bool
    parent_agent_run_id: str
    delegation_depth: int
    def __init__(self, id: _Optional[str] = ..., agent_name: _Optional[str] = ..., mission_run_id: _Optional[str] = ..., status: _Optional[str] = ..., started_at: _Optional[int] = ..., completed_at: _Optional[int] = ..., error_message: _Optional[str] = ..., actor_id: _Optional[str] = ..., actor_tenant_id: _Optional[str] = ..., api_key_id: _Optional[str] = ..., component_name: _Optional[str] = ..., component_version: _Optional[str] = ..., system_owned: bool = ..., parent_agent_run_id: _Optional[str] = ..., delegation_depth: _Optional[int] = ...) -> None: ...

class ToolExecution(_message.Message):
    __slots__ = ("id", "tool_name", "command", "exit_code", "started_at", "completed_at", "stdout", "stderr", "actor_id", "actor_tenant_id", "api_key_id", "component_name", "component_version", "system_owned", "parent_agent_run_id")
    ID_FIELD_NUMBER: _ClassVar[int]
    TOOL_NAME_FIELD_NUMBER: _ClassVar[int]
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    EXIT_CODE_FIELD_NUMBER: _ClassVar[int]
    STARTED_AT_FIELD_NUMBER: _ClassVar[int]
    COMPLETED_AT_FIELD_NUMBER: _ClassVar[int]
    STDOUT_FIELD_NUMBER: _ClassVar[int]
    STDERR_FIELD_NUMBER: _ClassVar[int]
    ACTOR_ID_FIELD_NUMBER: _ClassVar[int]
    ACTOR_TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    API_KEY_ID_FIELD_NUMBER: _ClassVar[int]
    COMPONENT_NAME_FIELD_NUMBER: _ClassVar[int]
    COMPONENT_VERSION_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_OWNED_FIELD_NUMBER: _ClassVar[int]
    PARENT_AGENT_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    tool_name: str
    command: str
    exit_code: int
    started_at: int
    completed_at: int
    stdout: str
    stderr: str
    actor_id: str
    actor_tenant_id: str
    api_key_id: str
    component_name: str
    component_version: str
    system_owned: bool
    parent_agent_run_id: str
    def __init__(self, id: _Optional[str] = ..., tool_name: _Optional[str] = ..., command: _Optional[str] = ..., exit_code: _Optional[int] = ..., started_at: _Optional[int] = ..., completed_at: _Optional[int] = ..., stdout: _Optional[str] = ..., stderr: _Optional[str] = ..., actor_id: _Optional[str] = ..., actor_tenant_id: _Optional[str] = ..., api_key_id: _Optional[str] = ..., component_name: _Optional[str] = ..., component_version: _Optional[str] = ..., system_owned: bool = ..., parent_agent_run_id: _Optional[str] = ...) -> None: ...

class LlmCall(_message.Message):
    __slots__ = ("id", "model", "provider", "slot_name", "agent_run_id", "prompt_tokens", "completion_tokens", "total_tokens", "latency_ms", "started_at", "actor_id", "actor_tenant_id", "api_key_id", "component_name", "component_version", "model_id")
    ID_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_FIELD_NUMBER: _ClassVar[int]
    SLOT_NAME_FIELD_NUMBER: _ClassVar[int]
    AGENT_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    PROMPT_TOKENS_FIELD_NUMBER: _ClassVar[int]
    COMPLETION_TOKENS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_TOKENS_FIELD_NUMBER: _ClassVar[int]
    LATENCY_MS_FIELD_NUMBER: _ClassVar[int]
    STARTED_AT_FIELD_NUMBER: _ClassVar[int]
    ACTOR_ID_FIELD_NUMBER: _ClassVar[int]
    ACTOR_TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    API_KEY_ID_FIELD_NUMBER: _ClassVar[int]
    COMPONENT_NAME_FIELD_NUMBER: _ClassVar[int]
    COMPONENT_VERSION_FIELD_NUMBER: _ClassVar[int]
    MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    model: str
    provider: str
    slot_name: str
    agent_run_id: str
    prompt_tokens: int
    completion_tokens: int
    total_tokens: int
    latency_ms: int
    started_at: int
    actor_id: str
    actor_tenant_id: str
    api_key_id: str
    component_name: str
    component_version: str
    model_id: str
    def __init__(self, id: _Optional[str] = ..., model: _Optional[str] = ..., provider: _Optional[str] = ..., slot_name: _Optional[str] = ..., agent_run_id: _Optional[str] = ..., prompt_tokens: _Optional[int] = ..., completion_tokens: _Optional[int] = ..., total_tokens: _Optional[int] = ..., latency_ms: _Optional[int] = ..., started_at: _Optional[int] = ..., actor_id: _Optional[str] = ..., actor_tenant_id: _Optional[str] = ..., api_key_id: _Optional[str] = ..., component_name: _Optional[str] = ..., component_version: _Optional[str] = ..., model_id: _Optional[str] = ...) -> None: ...

class Domain(_message.Message):
    __slots__ = ("id", "name", "registrar", "created_date", "expiry_date", "nameservers")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    REGISTRAR_FIELD_NUMBER: _ClassVar[int]
    CREATED_DATE_FIELD_NUMBER: _ClassVar[int]
    EXPIRY_DATE_FIELD_NUMBER: _ClassVar[int]
    NAMESERVERS_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    registrar: str
    created_date: int
    expiry_date: int
    nameservers: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., registrar: _Optional[str] = ..., created_date: _Optional[int] = ..., expiry_date: _Optional[int] = ..., nameservers: _Optional[str] = ...) -> None: ...

class Subdomain(_message.Message):
    __slots__ = ("id", "name", "full_name", "parent_domain_id")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    FULL_NAME_FIELD_NUMBER: _ClassVar[int]
    PARENT_DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    full_name: str
    parent_domain_id: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., full_name: _Optional[str] = ..., parent_domain_id: _Optional[str] = ...) -> None: ...

class Host(_message.Message):
    __slots__ = ("id", "ip", "hostname", "os", "os_version", "mac_address", "state")
    ID_FIELD_NUMBER: _ClassVar[int]
    IP_FIELD_NUMBER: _ClassVar[int]
    HOSTNAME_FIELD_NUMBER: _ClassVar[int]
    OS_FIELD_NUMBER: _ClassVar[int]
    OS_VERSION_FIELD_NUMBER: _ClassVar[int]
    MAC_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    id: str
    ip: str
    hostname: str
    os: str
    os_version: str
    mac_address: str
    state: str
    def __init__(self, id: _Optional[str] = ..., ip: _Optional[str] = ..., hostname: _Optional[str] = ..., os: _Optional[str] = ..., os_version: _Optional[str] = ..., mac_address: _Optional[str] = ..., state: _Optional[str] = ...) -> None: ...

class Port(_message.Message):
    __slots__ = ("id", "number", "protocol", "state", "reason", "parent_host_id")
    ID_FIELD_NUMBER: _ClassVar[int]
    NUMBER_FIELD_NUMBER: _ClassVar[int]
    PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    PARENT_HOST_ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    number: int
    protocol: str
    state: str
    reason: str
    parent_host_id: str
    def __init__(self, id: _Optional[str] = ..., number: _Optional[int] = ..., protocol: _Optional[str] = ..., state: _Optional[str] = ..., reason: _Optional[str] = ..., parent_host_id: _Optional[str] = ...) -> None: ...

class Service(_message.Message):
    __slots__ = ("id", "name", "product", "version", "extra_info", "banner", "cpe", "parent_port_id")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    EXTRA_INFO_FIELD_NUMBER: _ClassVar[int]
    BANNER_FIELD_NUMBER: _ClassVar[int]
    CPE_FIELD_NUMBER: _ClassVar[int]
    PARENT_PORT_ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    product: str
    version: str
    extra_info: str
    banner: str
    cpe: str
    parent_port_id: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., product: _Optional[str] = ..., version: _Optional[str] = ..., extra_info: _Optional[str] = ..., banner: _Optional[str] = ..., cpe: _Optional[str] = ..., parent_port_id: _Optional[str] = ...) -> None: ...

class Endpoint(_message.Message):
    __slots__ = ("id", "url", "method", "status_code", "content_type", "content_length", "title", "parent_service_id")
    ID_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    METHOD_FIELD_NUMBER: _ClassVar[int]
    STATUS_CODE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_LENGTH_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    PARENT_SERVICE_ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    url: str
    method: str
    status_code: int
    content_type: str
    content_length: int
    title: str
    parent_service_id: str
    def __init__(self, id: _Optional[str] = ..., url: _Optional[str] = ..., method: _Optional[str] = ..., status_code: _Optional[int] = ..., content_type: _Optional[str] = ..., content_length: _Optional[int] = ..., title: _Optional[str] = ..., parent_service_id: _Optional[str] = ...) -> None: ...

class Technology(_message.Message):
    __slots__ = ("id", "name", "version", "category", "confidence", "cpe")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    CPE_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    version: str
    category: str
    confidence: int
    cpe: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., version: _Optional[str] = ..., category: _Optional[str] = ..., confidence: _Optional[int] = ..., cpe: _Optional[str] = ...) -> None: ...

class Certificate(_message.Message):
    __slots__ = ("id", "subject", "issuer", "serial_number", "not_before", "not_after", "fingerprint_sha256", "san")
    ID_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_FIELD_NUMBER: _ClassVar[int]
    ISSUER_FIELD_NUMBER: _ClassVar[int]
    SERIAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    NOT_BEFORE_FIELD_NUMBER: _ClassVar[int]
    NOT_AFTER_FIELD_NUMBER: _ClassVar[int]
    FINGERPRINT_SHA256_FIELD_NUMBER: _ClassVar[int]
    SAN_FIELD_NUMBER: _ClassVar[int]
    id: str
    subject: str
    issuer: str
    serial_number: str
    not_before: int
    not_after: int
    fingerprint_sha256: str
    san: str
    def __init__(self, id: _Optional[str] = ..., subject: _Optional[str] = ..., issuer: _Optional[str] = ..., serial_number: _Optional[str] = ..., not_before: _Optional[int] = ..., not_after: _Optional[int] = ..., fingerprint_sha256: _Optional[str] = ..., san: _Optional[str] = ...) -> None: ...

class Finding(_message.Message):
    __slots__ = ("id", "title", "description", "severity", "confidence", "category", "subcategory", "remediation", "cvss_score", "cve_ids", "cwe_ids", "compliance_mappings")
    ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SEVERITY_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    SUBCATEGORY_FIELD_NUMBER: _ClassVar[int]
    REMEDIATION_FIELD_NUMBER: _ClassVar[int]
    CVSS_SCORE_FIELD_NUMBER: _ClassVar[int]
    CVE_IDS_FIELD_NUMBER: _ClassVar[int]
    CWE_IDS_FIELD_NUMBER: _ClassVar[int]
    COMPLIANCE_MAPPINGS_FIELD_NUMBER: _ClassVar[int]
    id: str
    title: str
    description: str
    severity: str
    confidence: float
    category: str
    subcategory: str
    remediation: str
    cvss_score: float
    cve_ids: str
    cwe_ids: str
    compliance_mappings: _containers.RepeatedCompositeFieldContainer[ComplianceMapping]
    def __init__(self, id: _Optional[str] = ..., title: _Optional[str] = ..., description: _Optional[str] = ..., severity: _Optional[str] = ..., confidence: _Optional[float] = ..., category: _Optional[str] = ..., subcategory: _Optional[str] = ..., remediation: _Optional[str] = ..., cvss_score: _Optional[float] = ..., cve_ids: _Optional[str] = ..., cwe_ids: _Optional[str] = ..., compliance_mappings: _Optional[_Iterable[_Union[ComplianceMapping, _Mapping]]] = ...) -> None: ...

class Evidence(_message.Message):
    __slots__ = ("id", "type", "content", "content_type", "url", "parent_finding_id")
    ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    PARENT_FINDING_ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    type: str
    content: str
    content_type: str
    url: str
    parent_finding_id: str
    def __init__(self, id: _Optional[str] = ..., type: _Optional[str] = ..., content: _Optional[str] = ..., content_type: _Optional[str] = ..., url: _Optional[str] = ..., parent_finding_id: _Optional[str] = ...) -> None: ...

class Technique(_message.Message):
    __slots__ = ("id", "technique_id", "name", "taxonomy", "tactic", "description", "url")
    ID_FIELD_NUMBER: _ClassVar[int]
    TECHNIQUE_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TAXONOMY_FIELD_NUMBER: _ClassVar[int]
    TACTIC_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    id: str
    technique_id: str
    name: str
    taxonomy: str
    tactic: str
    description: str
    url: str
    def __init__(self, id: _Optional[str] = ..., technique_id: _Optional[str] = ..., name: _Optional[str] = ..., taxonomy: _Optional[str] = ..., tactic: _Optional[str] = ..., description: _Optional[str] = ..., url: _Optional[str] = ...) -> None: ...

class ComplianceSignal(_message.Message):
    __slots__ = ("id", "signal_id", "actor_id", "actor_tenant_id", "api_key_id", "on_behalf_of", "roles_snapshot", "mission_id", "mission_run_id", "agent_run_id", "parent_agent_run_id", "delegation_depth", "trace_id", "caller_chain", "caller_component", "caller_component_version", "target_component", "target_component_version", "system_owned", "action", "effect", "resource_type", "resource_node_id", "resource_uri", "decision", "policy_id", "decision_reason", "success", "error_code", "latency_ms", "bytes_in", "bytes_out", "tokens_prompt", "tokens_completion", "occurred_at", "resource_tags", "custom", "control_ids")
    ID_FIELD_NUMBER: _ClassVar[int]
    SIGNAL_ID_FIELD_NUMBER: _ClassVar[int]
    ACTOR_ID_FIELD_NUMBER: _ClassVar[int]
    ACTOR_TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    API_KEY_ID_FIELD_NUMBER: _ClassVar[int]
    ON_BEHALF_OF_FIELD_NUMBER: _ClassVar[int]
    ROLES_SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    MISSION_ID_FIELD_NUMBER: _ClassVar[int]
    MISSION_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    AGENT_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_AGENT_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    DELEGATION_DEPTH_FIELD_NUMBER: _ClassVar[int]
    TRACE_ID_FIELD_NUMBER: _ClassVar[int]
    CALLER_CHAIN_FIELD_NUMBER: _ClassVar[int]
    CALLER_COMPONENT_FIELD_NUMBER: _ClassVar[int]
    CALLER_COMPONENT_VERSION_FIELD_NUMBER: _ClassVar[int]
    TARGET_COMPONENT_FIELD_NUMBER: _ClassVar[int]
    TARGET_COMPONENT_VERSION_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_OWNED_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    EFFECT_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_NODE_ID_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_URI_FIELD_NUMBER: _ClassVar[int]
    DECISION_FIELD_NUMBER: _ClassVar[int]
    POLICY_ID_FIELD_NUMBER: _ClassVar[int]
    DECISION_REASON_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_CODE_FIELD_NUMBER: _ClassVar[int]
    LATENCY_MS_FIELD_NUMBER: _ClassVar[int]
    BYTES_IN_FIELD_NUMBER: _ClassVar[int]
    BYTES_OUT_FIELD_NUMBER: _ClassVar[int]
    TOKENS_PROMPT_FIELD_NUMBER: _ClassVar[int]
    TOKENS_COMPLETION_FIELD_NUMBER: _ClassVar[int]
    OCCURRED_AT_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_TAGS_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELD_NUMBER: _ClassVar[int]
    CONTROL_IDS_FIELD_NUMBER: _ClassVar[int]
    id: str
    signal_id: str
    actor_id: str
    actor_tenant_id: str
    api_key_id: str
    on_behalf_of: str
    roles_snapshot: _containers.RepeatedScalarFieldContainer[str]
    mission_id: str
    mission_run_id: str
    agent_run_id: str
    parent_agent_run_id: str
    delegation_depth: int
    trace_id: str
    caller_chain: _containers.RepeatedScalarFieldContainer[str]
    caller_component: str
    caller_component_version: str
    target_component: str
    target_component_version: str
    system_owned: bool
    action: str
    effect: str
    resource_type: str
    resource_node_id: str
    resource_uri: str
    decision: str
    policy_id: str
    decision_reason: str
    success: bool
    error_code: str
    latency_ms: int
    bytes_in: int
    bytes_out: int
    tokens_prompt: int
    tokens_completion: int
    occurred_at: int
    resource_tags: str
    custom: str
    control_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, id: _Optional[str] = ..., signal_id: _Optional[str] = ..., actor_id: _Optional[str] = ..., actor_tenant_id: _Optional[str] = ..., api_key_id: _Optional[str] = ..., on_behalf_of: _Optional[str] = ..., roles_snapshot: _Optional[_Iterable[str]] = ..., mission_id: _Optional[str] = ..., mission_run_id: _Optional[str] = ..., agent_run_id: _Optional[str] = ..., parent_agent_run_id: _Optional[str] = ..., delegation_depth: _Optional[int] = ..., trace_id: _Optional[str] = ..., caller_chain: _Optional[_Iterable[str]] = ..., caller_component: _Optional[str] = ..., caller_component_version: _Optional[str] = ..., target_component: _Optional[str] = ..., target_component_version: _Optional[str] = ..., system_owned: bool = ..., action: _Optional[str] = ..., effect: _Optional[str] = ..., resource_type: _Optional[str] = ..., resource_node_id: _Optional[str] = ..., resource_uri: _Optional[str] = ..., decision: _Optional[str] = ..., policy_id: _Optional[str] = ..., decision_reason: _Optional[str] = ..., success: bool = ..., error_code: _Optional[str] = ..., latency_ms: _Optional[int] = ..., bytes_in: _Optional[int] = ..., bytes_out: _Optional[int] = ..., tokens_prompt: _Optional[int] = ..., tokens_completion: _Optional[int] = ..., occurred_at: _Optional[int] = ..., resource_tags: _Optional[str] = ..., custom: _Optional[str] = ..., control_ids: _Optional[_Iterable[str]] = ...) -> None: ...

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
