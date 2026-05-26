import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from gibson.auth.v1 import options_pb2 as _options_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FindingCountGroupBy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FINDING_COUNT_GROUP_BY_UNSPECIFIED: _ClassVar[FindingCountGroupBy]
    SEVERITY: _ClassVar[FindingCountGroupBy]
    CATEGORY: _ClassVar[FindingCountGroupBy]
FINDING_COUNT_GROUP_BY_UNSPECIFIED: FindingCountGroupBy
SEVERITY: FindingCountGroupBy
CATEGORY: FindingCountGroupBy

class Node(_message.Message):
    __slots__ = ("id", "labels", "properties", "first_seen_at", "severity")
    class PropertiesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    FIRST_SEEN_AT_FIELD_NUMBER: _ClassVar[int]
    SEVERITY_FIELD_NUMBER: _ClassVar[int]
    id: str
    labels: _containers.RepeatedScalarFieldContainer[str]
    properties: _containers.ScalarMap[str, str]
    first_seen_at: _timestamp_pb2.Timestamp
    severity: str
    def __init__(self, id: _Optional[str] = ..., labels: _Optional[_Iterable[str]] = ..., properties: _Optional[_Mapping[str, str]] = ..., first_seen_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., severity: _Optional[str] = ...) -> None: ...

class Edge(_message.Message):
    __slots__ = ("id", "source_id", "target_id", "type", "properties")
    class PropertiesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    id: str
    source_id: str
    target_id: str
    type: str
    properties: _containers.ScalarMap[str, str]
    def __init__(self, id: _Optional[str] = ..., source_id: _Optional[str] = ..., target_id: _Optional[str] = ..., type: _Optional[str] = ..., properties: _Optional[_Mapping[str, str]] = ...) -> None: ...

class Path(_message.Message):
    __slots__ = ("node_ids", "edge_ids")
    NODE_IDS_FIELD_NUMBER: _ClassVar[int]
    EDGE_IDS_FIELD_NUMBER: _ClassVar[int]
    node_ids: _containers.RepeatedScalarFieldContainer[str]
    edge_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, node_ids: _Optional[_Iterable[str]] = ..., edge_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class GetTenantGraphRequest(_message.Message):
    __slots__ = ("limit", "include_labels")
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_LABELS_FIELD_NUMBER: _ClassVar[int]
    limit: int
    include_labels: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, limit: _Optional[int] = ..., include_labels: _Optional[_Iterable[str]] = ...) -> None: ...

class GetTenantGraphResponse(_message.Message):
    __slots__ = ("nodes", "edges", "truncated", "total_node_count")
    NODES_FIELD_NUMBER: _ClassVar[int]
    EDGES_FIELD_NUMBER: _ClassVar[int]
    TRUNCATED_FIELD_NUMBER: _ClassVar[int]
    TOTAL_NODE_COUNT_FIELD_NUMBER: _ClassVar[int]
    nodes: _containers.RepeatedCompositeFieldContainer[Node]
    edges: _containers.RepeatedCompositeFieldContainer[Edge]
    truncated: bool
    total_node_count: int
    def __init__(self, nodes: _Optional[_Iterable[_Union[Node, _Mapping]]] = ..., edges: _Optional[_Iterable[_Union[Edge, _Mapping]]] = ..., truncated: bool = ..., total_node_count: _Optional[int] = ...) -> None: ...

class GetMissionGraphRequest(_message.Message):
    __slots__ = ("mission_id",)
    MISSION_ID_FIELD_NUMBER: _ClassVar[int]
    mission_id: str
    def __init__(self, mission_id: _Optional[str] = ...) -> None: ...

class GetMissionGraphResponse(_message.Message):
    __slots__ = ("nodes", "edges")
    NODES_FIELD_NUMBER: _ClassVar[int]
    EDGES_FIELD_NUMBER: _ClassVar[int]
    nodes: _containers.RepeatedCompositeFieldContainer[Node]
    edges: _containers.RepeatedCompositeFieldContainer[Edge]
    def __init__(self, nodes: _Optional[_Iterable[_Union[Node, _Mapping]]] = ..., edges: _Optional[_Iterable[_Union[Edge, _Mapping]]] = ...) -> None: ...

class QueryPathsRequest(_message.Message):
    __slots__ = ("from_node_id", "to_node_id", "to_node_kind", "max_depth")
    FROM_NODE_ID_FIELD_NUMBER: _ClassVar[int]
    TO_NODE_ID_FIELD_NUMBER: _ClassVar[int]
    TO_NODE_KIND_FIELD_NUMBER: _ClassVar[int]
    MAX_DEPTH_FIELD_NUMBER: _ClassVar[int]
    from_node_id: str
    to_node_id: str
    to_node_kind: str
    max_depth: int
    def __init__(self, from_node_id: _Optional[str] = ..., to_node_id: _Optional[str] = ..., to_node_kind: _Optional[str] = ..., max_depth: _Optional[int] = ...) -> None: ...

class QueryPathsResponse(_message.Message):
    __slots__ = ("paths", "nodes", "edges", "truncated_paths")
    PATHS_FIELD_NUMBER: _ClassVar[int]
    NODES_FIELD_NUMBER: _ClassVar[int]
    EDGES_FIELD_NUMBER: _ClassVar[int]
    TRUNCATED_PATHS_FIELD_NUMBER: _ClassVar[int]
    paths: _containers.RepeatedCompositeFieldContainer[Path]
    nodes: _containers.RepeatedCompositeFieldContainer[Node]
    edges: _containers.RepeatedCompositeFieldContainer[Edge]
    truncated_paths: bool
    def __init__(self, paths: _Optional[_Iterable[_Union[Path, _Mapping]]] = ..., nodes: _Optional[_Iterable[_Union[Node, _Mapping]]] = ..., edges: _Optional[_Iterable[_Union[Edge, _Mapping]]] = ..., truncated_paths: bool = ...) -> None: ...

class WatchGraphUpdatesRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GraphUpdate(_message.Message):
    __slots__ = ("kind", "node", "edge", "at")
    class Kind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        KIND_UNSPECIFIED: _ClassVar[GraphUpdate.Kind]
        NODE_ADDED: _ClassVar[GraphUpdate.Kind]
        EDGE_ADDED: _ClassVar[GraphUpdate.Kind]
        NODE_UPDATED: _ClassVar[GraphUpdate.Kind]
    KIND_UNSPECIFIED: GraphUpdate.Kind
    NODE_ADDED: GraphUpdate.Kind
    EDGE_ADDED: GraphUpdate.Kind
    NODE_UPDATED: GraphUpdate.Kind
    KIND_FIELD_NUMBER: _ClassVar[int]
    NODE_FIELD_NUMBER: _ClassVar[int]
    EDGE_FIELD_NUMBER: _ClassVar[int]
    AT_FIELD_NUMBER: _ClassVar[int]
    kind: GraphUpdate.Kind
    node: Node
    edge: Edge
    at: _timestamp_pb2.Timestamp
    def __init__(self, kind: _Optional[_Union[GraphUpdate.Kind, str]] = ..., node: _Optional[_Union[Node, _Mapping]] = ..., edge: _Optional[_Union[Edge, _Mapping]] = ..., at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class GetFindingCountsRequest(_message.Message):
    __slots__ = ("group_by", "time_window_seconds")
    GROUP_BY_FIELD_NUMBER: _ClassVar[int]
    TIME_WINDOW_SECONDS_FIELD_NUMBER: _ClassVar[int]
    group_by: FindingCountGroupBy
    time_window_seconds: int
    def __init__(self, group_by: _Optional[_Union[FindingCountGroupBy, str]] = ..., time_window_seconds: _Optional[int] = ...) -> None: ...

class CountBucket(_message.Message):
    __slots__ = ("label", "count")
    LABEL_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    label: str
    count: int
    def __init__(self, label: _Optional[str] = ..., count: _Optional[int] = ...) -> None: ...

class GetFindingCountsResponse(_message.Message):
    __slots__ = ("buckets",)
    BUCKETS_FIELD_NUMBER: _ClassVar[int]
    buckets: _containers.RepeatedCompositeFieldContainer[CountBucket]
    def __init__(self, buckets: _Optional[_Iterable[_Union[CountBucket, _Mapping]]] = ...) -> None: ...

class GetFindingTimeSeriesRequest(_message.Message):
    __slots__ = ("days",)
    DAYS_FIELD_NUMBER: _ClassVar[int]
    days: int
    def __init__(self, days: _Optional[int] = ...) -> None: ...

class TimeSeriesPoint(_message.Message):
    __slots__ = ("date", "count")
    DATE_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    date: _timestamp_pb2.Timestamp
    count: int
    def __init__(self, date: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., count: _Optional[int] = ...) -> None: ...

class GetFindingTimeSeriesResponse(_message.Message):
    __slots__ = ("points",)
    POINTS_FIELD_NUMBER: _ClassVar[int]
    points: _containers.RepeatedCompositeFieldContainer[TimeSeriesPoint]
    def __init__(self, points: _Optional[_Iterable[_Union[TimeSeriesPoint, _Mapping]]] = ...) -> None: ...

class GetGraphStatsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class NodeCountByLabel(_message.Message):
    __slots__ = ("label", "count")
    LABEL_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    label: str
    count: int
    def __init__(self, label: _Optional[str] = ..., count: _Optional[int] = ...) -> None: ...

class GetGraphStatsResponse(_message.Message):
    __slots__ = ("by_label", "total_nodes", "total_edges", "last_write_at")
    BY_LABEL_FIELD_NUMBER: _ClassVar[int]
    TOTAL_NODES_FIELD_NUMBER: _ClassVar[int]
    TOTAL_EDGES_FIELD_NUMBER: _ClassVar[int]
    LAST_WRITE_AT_FIELD_NUMBER: _ClassVar[int]
    by_label: _containers.RepeatedCompositeFieldContainer[NodeCountByLabel]
    total_nodes: int
    total_edges: int
    last_write_at: _timestamp_pb2.Timestamp
    def __init__(self, by_label: _Optional[_Iterable[_Union[NodeCountByLabel, _Mapping]]] = ..., total_nodes: _Optional[int] = ..., total_edges: _Optional[int] = ..., last_write_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class GetGraphSummaryRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GraphSummaryStats(_message.Message):
    __slots__ = ("hosts", "services", "findings", "vulnerabilities", "missions")
    HOSTS_FIELD_NUMBER: _ClassVar[int]
    SERVICES_FIELD_NUMBER: _ClassVar[int]
    FINDINGS_FIELD_NUMBER: _ClassVar[int]
    VULNERABILITIES_FIELD_NUMBER: _ClassVar[int]
    MISSIONS_FIELD_NUMBER: _ClassVar[int]
    hosts: int
    services: int
    findings: int
    vulnerabilities: int
    missions: int
    def __init__(self, hosts: _Optional[int] = ..., services: _Optional[int] = ..., findings: _Optional[int] = ..., vulnerabilities: _Optional[int] = ..., missions: _Optional[int] = ...) -> None: ...

class GetGraphSummaryResponse(_message.Message):
    __slots__ = ("summary", "stats")
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    STATS_FIELD_NUMBER: _ClassVar[int]
    summary: str
    stats: GraphSummaryStats
    def __init__(self, summary: _Optional[str] = ..., stats: _Optional[_Union[GraphSummaryStats, _Mapping]] = ...) -> None: ...

class GetGraphContextRequest(_message.Message):
    __slots__ = ("node_id", "hops", "max_nodes")
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    HOPS_FIELD_NUMBER: _ClassVar[int]
    MAX_NODES_FIELD_NUMBER: _ClassVar[int]
    node_id: str
    hops: int
    max_nodes: int
    def __init__(self, node_id: _Optional[str] = ..., hops: _Optional[int] = ..., max_nodes: _Optional[int] = ...) -> None: ...

class NeighborEdge(_message.Message):
    __slots__ = ("node", "relationship", "direction")
    NODE_FIELD_NUMBER: _ClassVar[int]
    RELATIONSHIP_FIELD_NUMBER: _ClassVar[int]
    DIRECTION_FIELD_NUMBER: _ClassVar[int]
    node: Node
    relationship: str
    direction: str
    def __init__(self, node: _Optional[_Union[Node, _Mapping]] = ..., relationship: _Optional[str] = ..., direction: _Optional[str] = ...) -> None: ...

class GetGraphContextResponse(_message.Message):
    __slots__ = ("focus_node", "neighbors", "summary")
    FOCUS_NODE_FIELD_NUMBER: _ClassVar[int]
    NEIGHBORS_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    focus_node: Node
    neighbors: _containers.RepeatedCompositeFieldContainer[NeighborEdge]
    summary: str
    def __init__(self, focus_node: _Optional[_Union[Node, _Mapping]] = ..., neighbors: _Optional[_Iterable[_Union[NeighborEdge, _Mapping]]] = ..., summary: _Optional[str] = ...) -> None: ...

class Finding(_message.Message):
    __slots__ = ("id", "name", "description", "type", "severity", "mission_id", "created_at", "properties", "labels")
    class PropertiesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SEVERITY_FIELD_NUMBER: _ClassVar[int]
    MISSION_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: str
    type: str
    severity: str
    mission_id: str
    created_at: _timestamp_pb2.Timestamp
    properties: _containers.ScalarMap[str, str]
    labels: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., type: _Optional[str] = ..., severity: _Optional[str] = ..., mission_id: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., properties: _Optional[_Mapping[str, str]] = ..., labels: _Optional[_Iterable[str]] = ...) -> None: ...

class GetFindingsRequest(_message.Message):
    __slots__ = ("severity_filter", "category_filter", "mission_id", "search", "limit", "offset")
    SEVERITY_FILTER_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FILTER_FIELD_NUMBER: _ClassVar[int]
    MISSION_ID_FIELD_NUMBER: _ClassVar[int]
    SEARCH_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    severity_filter: str
    category_filter: str
    mission_id: str
    search: str
    limit: int
    offset: int
    def __init__(self, severity_filter: _Optional[str] = ..., category_filter: _Optional[str] = ..., mission_id: _Optional[str] = ..., search: _Optional[str] = ..., limit: _Optional[int] = ..., offset: _Optional[int] = ...) -> None: ...

class GetFindingsResponse(_message.Message):
    __slots__ = ("findings", "total", "truncated")
    FINDINGS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    TRUNCATED_FIELD_NUMBER: _ClassVar[int]
    findings: _containers.RepeatedCompositeFieldContainer[Finding]
    total: int
    truncated: bool
    def __init__(self, findings: _Optional[_Iterable[_Union[Finding, _Mapping]]] = ..., total: _Optional[int] = ..., truncated: bool = ...) -> None: ...
