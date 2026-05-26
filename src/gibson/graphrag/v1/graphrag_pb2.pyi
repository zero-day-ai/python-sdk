from taxonomy.v1 import taxonomy_pb2 as _taxonomy_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class QueryScope(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    QUERY_SCOPE_UNSPECIFIED: _ClassVar[QueryScope]
    QUERY_SCOPE_MISSION: _ClassVar[QueryScope]
    QUERY_SCOPE_MISSION_RUN: _ClassVar[QueryScope]
    QUERY_SCOPE_GLOBAL: _ClassVar[QueryScope]
QUERY_SCOPE_UNSPECIFIED: QueryScope
QUERY_SCOPE_MISSION: QueryScope
QUERY_SCOPE_MISSION_RUN: QueryScope
QUERY_SCOPE_GLOBAL: QueryScope

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

class QueryResult(_message.Message):
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
    __slots__ = ("id", "type", "properties", "content", "mission_id", "mission_run_id", "agent_run_id", "discovered_by", "discovered_at", "created_at", "updated_at", "parent_id", "parent_type", "parent_relationship")
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
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    MISSION_ID_FIELD_NUMBER: _ClassVar[int]
    MISSION_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    AGENT_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    DISCOVERED_BY_FIELD_NUMBER: _ClassVar[int]
    DISCOVERED_AT_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    PARENT_ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    PARENT_RELATIONSHIP_FIELD_NUMBER: _ClassVar[int]
    id: str
    type: str
    properties: _containers.MessageMap[str, Value]
    content: str
    mission_id: str
    mission_run_id: str
    agent_run_id: str
    discovered_by: str
    discovered_at: int
    created_at: int
    updated_at: int
    parent_id: str
    parent_type: str
    parent_relationship: str
    def __init__(self, id: _Optional[str] = ..., type: _Optional[str] = ..., properties: _Optional[_Mapping[str, Value]] = ..., content: _Optional[str] = ..., mission_id: _Optional[str] = ..., mission_run_id: _Optional[str] = ..., agent_run_id: _Optional[str] = ..., discovered_by: _Optional[str] = ..., discovered_at: _Optional[int] = ..., created_at: _Optional[int] = ..., updated_at: _Optional[int] = ..., parent_id: _Optional[str] = ..., parent_type: _Optional[str] = ..., parent_relationship: _Optional[str] = ...) -> None: ...

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

class DiscoveryResult(_message.Message):
    __slots__ = ("hosts", "ports", "services", "endpoints", "domains", "subdomains", "technologies", "certificates", "findings", "evidence", "custom_nodes", "explicit_relationships", "compliance_signals")
    HOSTS_FIELD_NUMBER: _ClassVar[int]
    PORTS_FIELD_NUMBER: _ClassVar[int]
    SERVICES_FIELD_NUMBER: _ClassVar[int]
    ENDPOINTS_FIELD_NUMBER: _ClassVar[int]
    DOMAINS_FIELD_NUMBER: _ClassVar[int]
    SUBDOMAINS_FIELD_NUMBER: _ClassVar[int]
    TECHNOLOGIES_FIELD_NUMBER: _ClassVar[int]
    CERTIFICATES_FIELD_NUMBER: _ClassVar[int]
    FINDINGS_FIELD_NUMBER: _ClassVar[int]
    EVIDENCE_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_NODES_FIELD_NUMBER: _ClassVar[int]
    EXPLICIT_RELATIONSHIPS_FIELD_NUMBER: _ClassVar[int]
    COMPLIANCE_SIGNALS_FIELD_NUMBER: _ClassVar[int]
    hosts: _containers.RepeatedCompositeFieldContainer[Host]
    ports: _containers.RepeatedCompositeFieldContainer[Port]
    services: _containers.RepeatedCompositeFieldContainer[Service]
    endpoints: _containers.RepeatedCompositeFieldContainer[Endpoint]
    domains: _containers.RepeatedCompositeFieldContainer[Domain]
    subdomains: _containers.RepeatedCompositeFieldContainer[Subdomain]
    technologies: _containers.RepeatedCompositeFieldContainer[Technology]
    certificates: _containers.RepeatedCompositeFieldContainer[Certificate]
    findings: _containers.RepeatedCompositeFieldContainer[Finding]
    evidence: _containers.RepeatedCompositeFieldContainer[Evidence]
    custom_nodes: _containers.RepeatedCompositeFieldContainer[CustomNode]
    explicit_relationships: _containers.RepeatedCompositeFieldContainer[ExplicitRelationship]
    compliance_signals: _containers.RepeatedCompositeFieldContainer[_taxonomy_pb2.ComplianceSignal]
    def __init__(self, hosts: _Optional[_Iterable[_Union[Host, _Mapping]]] = ..., ports: _Optional[_Iterable[_Union[Port, _Mapping]]] = ..., services: _Optional[_Iterable[_Union[Service, _Mapping]]] = ..., endpoints: _Optional[_Iterable[_Union[Endpoint, _Mapping]]] = ..., domains: _Optional[_Iterable[_Union[Domain, _Mapping]]] = ..., subdomains: _Optional[_Iterable[_Union[Subdomain, _Mapping]]] = ..., technologies: _Optional[_Iterable[_Union[Technology, _Mapping]]] = ..., certificates: _Optional[_Iterable[_Union[Certificate, _Mapping]]] = ..., findings: _Optional[_Iterable[_Union[Finding, _Mapping]]] = ..., evidence: _Optional[_Iterable[_Union[Evidence, _Mapping]]] = ..., custom_nodes: _Optional[_Iterable[_Union[CustomNode, _Mapping]]] = ..., explicit_relationships: _Optional[_Iterable[_Union[ExplicitRelationship, _Mapping]]] = ..., compliance_signals: _Optional[_Iterable[_Union[_taxonomy_pb2.ComplianceSignal, _Mapping]]] = ...) -> None: ...

class Host(_message.Message):
    __slots__ = ("id", "ip", "hostname", "state", "os", "os_version", "mac_address")
    ID_FIELD_NUMBER: _ClassVar[int]
    IP_FIELD_NUMBER: _ClassVar[int]
    HOSTNAME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    OS_FIELD_NUMBER: _ClassVar[int]
    OS_VERSION_FIELD_NUMBER: _ClassVar[int]
    MAC_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    id: str
    ip: str
    hostname: str
    state: str
    os: str
    os_version: str
    mac_address: str
    def __init__(self, id: _Optional[str] = ..., ip: _Optional[str] = ..., hostname: _Optional[str] = ..., state: _Optional[str] = ..., os: _Optional[str] = ..., os_version: _Optional[str] = ..., mac_address: _Optional[str] = ...) -> None: ...

class Port(_message.Message):
    __slots__ = ("id", "host_id", "number", "protocol", "state", "reason")
    ID_FIELD_NUMBER: _ClassVar[int]
    HOST_ID_FIELD_NUMBER: _ClassVar[int]
    NUMBER_FIELD_NUMBER: _ClassVar[int]
    PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    id: str
    host_id: str
    number: int
    protocol: str
    state: str
    reason: str
    def __init__(self, id: _Optional[str] = ..., host_id: _Optional[str] = ..., number: _Optional[int] = ..., protocol: _Optional[str] = ..., state: _Optional[str] = ..., reason: _Optional[str] = ...) -> None: ...

class Service(_message.Message):
    __slots__ = ("id", "port_id", "name", "product", "version", "extra_info", "banner", "cpe")
    ID_FIELD_NUMBER: _ClassVar[int]
    PORT_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    EXTRA_INFO_FIELD_NUMBER: _ClassVar[int]
    BANNER_FIELD_NUMBER: _ClassVar[int]
    CPE_FIELD_NUMBER: _ClassVar[int]
    id: str
    port_id: str
    name: str
    product: str
    version: str
    extra_info: str
    banner: str
    cpe: str
    def __init__(self, id: _Optional[str] = ..., port_id: _Optional[str] = ..., name: _Optional[str] = ..., product: _Optional[str] = ..., version: _Optional[str] = ..., extra_info: _Optional[str] = ..., banner: _Optional[str] = ..., cpe: _Optional[str] = ...) -> None: ...

class Endpoint(_message.Message):
    __slots__ = ("id", "service_id", "url", "method", "status_code", "content_type", "content_length", "title")
    ID_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ID_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    METHOD_FIELD_NUMBER: _ClassVar[int]
    STATUS_CODE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_LENGTH_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    id: str
    service_id: str
    url: str
    method: str
    status_code: int
    content_type: str
    content_length: int
    title: str
    def __init__(self, id: _Optional[str] = ..., service_id: _Optional[str] = ..., url: _Optional[str] = ..., method: _Optional[str] = ..., status_code: _Optional[int] = ..., content_type: _Optional[str] = ..., content_length: _Optional[int] = ..., title: _Optional[str] = ...) -> None: ...

class Domain(_message.Message):
    __slots__ = ("id", "name", "registrar", "created_date", "expiry_date")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    REGISTRAR_FIELD_NUMBER: _ClassVar[int]
    CREATED_DATE_FIELD_NUMBER: _ClassVar[int]
    EXPIRY_DATE_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    registrar: str
    created_date: int
    expiry_date: int
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., registrar: _Optional[str] = ..., created_date: _Optional[int] = ..., expiry_date: _Optional[int] = ...) -> None: ...

class Subdomain(_message.Message):
    __slots__ = ("id", "domain_id", "name", "full_name")
    ID_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    FULL_NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    domain_id: str
    name: str
    full_name: str
    def __init__(self, id: _Optional[str] = ..., domain_id: _Optional[str] = ..., name: _Optional[str] = ..., full_name: _Optional[str] = ...) -> None: ...

class Technology(_message.Message):
    __slots__ = ("id", "name", "version", "category", "confidence", "cpe", "parent_id", "parent_type")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    CPE_FIELD_NUMBER: _ClassVar[int]
    PARENT_ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    version: str
    category: str
    confidence: int
    cpe: str
    parent_id: str
    parent_type: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., version: _Optional[str] = ..., category: _Optional[str] = ..., confidence: _Optional[int] = ..., cpe: _Optional[str] = ..., parent_id: _Optional[str] = ..., parent_type: _Optional[str] = ...) -> None: ...

class Certificate(_message.Message):
    __slots__ = ("id", "subject", "issuer", "serial_number", "not_before", "not_after", "fingerprint_sha256", "san", "parent_id", "parent_type")
    ID_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_FIELD_NUMBER: _ClassVar[int]
    ISSUER_FIELD_NUMBER: _ClassVar[int]
    SERIAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    NOT_BEFORE_FIELD_NUMBER: _ClassVar[int]
    NOT_AFTER_FIELD_NUMBER: _ClassVar[int]
    FINGERPRINT_SHA256_FIELD_NUMBER: _ClassVar[int]
    SAN_FIELD_NUMBER: _ClassVar[int]
    PARENT_ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    id: str
    subject: str
    issuer: str
    serial_number: str
    not_before: int
    not_after: int
    fingerprint_sha256: str
    san: str
    parent_id: str
    parent_type: str
    def __init__(self, id: _Optional[str] = ..., subject: _Optional[str] = ..., issuer: _Optional[str] = ..., serial_number: _Optional[str] = ..., not_before: _Optional[int] = ..., not_after: _Optional[int] = ..., fingerprint_sha256: _Optional[str] = ..., san: _Optional[str] = ..., parent_id: _Optional[str] = ..., parent_type: _Optional[str] = ...) -> None: ...

class Finding(_message.Message):
    __slots__ = ("id", "title", "description", "severity", "confidence", "category", "remediation", "cvss_score", "cve_ids", "parent_id", "parent_type")
    ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SEVERITY_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    REMEDIATION_FIELD_NUMBER: _ClassVar[int]
    CVSS_SCORE_FIELD_NUMBER: _ClassVar[int]
    CVE_IDS_FIELD_NUMBER: _ClassVar[int]
    PARENT_ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    id: str
    title: str
    description: str
    severity: str
    confidence: float
    category: str
    remediation: str
    cvss_score: float
    cve_ids: str
    parent_id: str
    parent_type: str
    def __init__(self, id: _Optional[str] = ..., title: _Optional[str] = ..., description: _Optional[str] = ..., severity: _Optional[str] = ..., confidence: _Optional[float] = ..., category: _Optional[str] = ..., remediation: _Optional[str] = ..., cvss_score: _Optional[float] = ..., cve_ids: _Optional[str] = ..., parent_id: _Optional[str] = ..., parent_type: _Optional[str] = ...) -> None: ...

class Evidence(_message.Message):
    __slots__ = ("id", "finding_id", "type", "content", "url")
    ID_FIELD_NUMBER: _ClassVar[int]
    FINDING_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    id: str
    finding_id: str
    type: str
    content: str
    url: str
    def __init__(self, id: _Optional[str] = ..., finding_id: _Optional[str] = ..., type: _Optional[str] = ..., content: _Optional[str] = ..., url: _Optional[str] = ...) -> None: ...

class CustomNode(_message.Message):
    __slots__ = ("node_type", "id_properties", "properties", "parent_type", "parent_id", "relationship_type")
    class IdPropertiesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class PropertiesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class ParentIdEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NODE_TYPE_FIELD_NUMBER: _ClassVar[int]
    ID_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    PARENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    PARENT_ID_FIELD_NUMBER: _ClassVar[int]
    RELATIONSHIP_TYPE_FIELD_NUMBER: _ClassVar[int]
    node_type: str
    id_properties: _containers.ScalarMap[str, str]
    properties: _containers.ScalarMap[str, str]
    parent_type: str
    parent_id: _containers.ScalarMap[str, str]
    relationship_type: str
    def __init__(self, node_type: _Optional[str] = ..., id_properties: _Optional[_Mapping[str, str]] = ..., properties: _Optional[_Mapping[str, str]] = ..., parent_type: _Optional[str] = ..., parent_id: _Optional[_Mapping[str, str]] = ..., relationship_type: _Optional[str] = ...) -> None: ...

class ExplicitRelationship(_message.Message):
    __slots__ = ("from_type", "from_id", "to_type", "to_id", "relationship_type", "properties")
    class FromIdEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class ToIdEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class PropertiesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    FROM_TYPE_FIELD_NUMBER: _ClassVar[int]
    FROM_ID_FIELD_NUMBER: _ClassVar[int]
    TO_TYPE_FIELD_NUMBER: _ClassVar[int]
    TO_ID_FIELD_NUMBER: _ClassVar[int]
    RELATIONSHIP_TYPE_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    from_type: str
    from_id: _containers.ScalarMap[str, str]
    to_type: str
    to_id: _containers.ScalarMap[str, str]
    relationship_type: str
    properties: _containers.ScalarMap[str, str]
    def __init__(self, from_type: _Optional[str] = ..., from_id: _Optional[_Mapping[str, str]] = ..., to_type: _Optional[str] = ..., to_id: _Optional[_Mapping[str, str]] = ..., relationship_type: _Optional[str] = ..., properties: _Optional[_Mapping[str, str]] = ...) -> None: ...

class HierarchyDef(_message.Message):
    __slots__ = ("node_type", "label", "sub_class_of")
    NODE_TYPE_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    SUB_CLASS_OF_FIELD_NUMBER: _ClassVar[int]
    node_type: str
    label: str
    sub_class_of: str
    def __init__(self, node_type: _Optional[str] = ..., label: _Optional[str] = ..., sub_class_of: _Optional[str] = ...) -> None: ...

class IFPDef(_message.Message):
    __slots__ = ("node_type", "property")
    NODE_TYPE_FIELD_NUMBER: _ClassVar[int]
    PROPERTY_FIELD_NUMBER: _ClassVar[int]
    node_type: str
    property: str
    def __init__(self, node_type: _Optional[str] = ..., property: _Optional[str] = ...) -> None: ...

class SameAsPair(_message.Message):
    __slots__ = ("iri_a", "iri_b")
    IRI_A_FIELD_NUMBER: _ClassVar[int]
    IRI_B_FIELD_NUMBER: _ClassVar[int]
    iri_a: str
    iri_b: str
    def __init__(self, iri_a: _Optional[str] = ..., iri_b: _Optional[str] = ...) -> None: ...

class OntologyExtension(_message.Message):
    __slots__ = ("prefixes", "hierarchies", "equivalences", "ifps", "raw_triples")
    class PrefixesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    PREFIXES_FIELD_NUMBER: _ClassVar[int]
    HIERARCHIES_FIELD_NUMBER: _ClassVar[int]
    EQUIVALENCES_FIELD_NUMBER: _ClassVar[int]
    IFPS_FIELD_NUMBER: _ClassVar[int]
    RAW_TRIPLES_FIELD_NUMBER: _ClassVar[int]
    prefixes: _containers.ScalarMap[str, str]
    hierarchies: _containers.RepeatedCompositeFieldContainer[HierarchyDef]
    equivalences: _containers.RepeatedCompositeFieldContainer[SameAsPair]
    ifps: _containers.RepeatedCompositeFieldContainer[IFPDef]
    raw_triples: bytes
    def __init__(self, prefixes: _Optional[_Mapping[str, str]] = ..., hierarchies: _Optional[_Iterable[_Union[HierarchyDef, _Mapping]]] = ..., equivalences: _Optional[_Iterable[_Union[SameAsPair, _Mapping]]] = ..., ifps: _Optional[_Iterable[_Union[IFPDef, _Mapping]]] = ..., raw_triples: _Optional[bytes] = ...) -> None: ...
