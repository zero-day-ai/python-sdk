import datetime

from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from gibson.types.v1 import types_pb2 as _types_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NodeType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NODE_TYPE_UNSPECIFIED: _ClassVar[NodeType]
    NODE_TYPE_AGENT: _ClassVar[NodeType]
    NODE_TYPE_TOOL: _ClassVar[NodeType]
    NODE_TYPE_PLUGIN: _ClassVar[NodeType]
    NODE_TYPE_CONDITION: _ClassVar[NodeType]
    NODE_TYPE_PARALLEL: _ClassVar[NodeType]
    NODE_TYPE_JOIN: _ClassVar[NodeType]

class Language(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LANGUAGE_UNSPECIFIED: _ClassVar[Language]
    LANGUAGE_CEL: _ClassVar[Language]

class MergeStrategy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MERGE_STRATEGY_UNSPECIFIED: _ClassVar[MergeStrategy]
    MERGE_STRATEGY_CONCAT: _ClassVar[MergeStrategy]
    MERGE_STRATEGY_REDUCE: _ClassVar[MergeStrategy]
    MERGE_STRATEGY_FIRST: _ClassVar[MergeStrategy]
    MERGE_STRATEGY_LAST: _ClassVar[MergeStrategy]
    MERGE_STRATEGY_CUSTOM: _ClassVar[MergeStrategy]

class BackoffStrategy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BACKOFF_STRATEGY_UNSPECIFIED: _ClassVar[BackoffStrategy]
    BACKOFF_STRATEGY_CONSTANT: _ClassVar[BackoffStrategy]
    BACKOFF_STRATEGY_LINEAR: _ClassVar[BackoffStrategy]
    BACKOFF_STRATEGY_EXPONENTIAL: _ClassVar[BackoffStrategy]
NODE_TYPE_UNSPECIFIED: NodeType
NODE_TYPE_AGENT: NodeType
NODE_TYPE_TOOL: NodeType
NODE_TYPE_PLUGIN: NodeType
NODE_TYPE_CONDITION: NodeType
NODE_TYPE_PARALLEL: NodeType
NODE_TYPE_JOIN: NodeType
LANGUAGE_UNSPECIFIED: Language
LANGUAGE_CEL: Language
MERGE_STRATEGY_UNSPECIFIED: MergeStrategy
MERGE_STRATEGY_CONCAT: MergeStrategy
MERGE_STRATEGY_REDUCE: MergeStrategy
MERGE_STRATEGY_FIRST: MergeStrategy
MERGE_STRATEGY_LAST: MergeStrategy
MERGE_STRATEGY_CUSTOM: MergeStrategy
BACKOFF_STRATEGY_UNSPECIFIED: BackoffStrategy
BACKOFF_STRATEGY_CONSTANT: BackoffStrategy
BACKOFF_STRATEGY_LINEAR: BackoffStrategy
BACKOFF_STRATEGY_EXPONENTIAL: BackoffStrategy

class MissionDefinition(_message.Message):
    __slots__ = ("id", "name", "description", "version", "target_ref", "nodes", "edges", "entry_points", "exit_points", "metadata", "dependencies", "source", "installed_at", "created_at", "workspace", "constraints")
    class NodesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: MissionNode
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[MissionNode, _Mapping]] = ...) -> None: ...
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    TARGET_REF_FIELD_NUMBER: _ClassVar[int]
    NODES_FIELD_NUMBER: _ClassVar[int]
    EDGES_FIELD_NUMBER: _ClassVar[int]
    ENTRY_POINTS_FIELD_NUMBER: _ClassVar[int]
    EXIT_POINTS_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    DEPENDENCIES_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    INSTALLED_AT_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    WORKSPACE_FIELD_NUMBER: _ClassVar[int]
    CONSTRAINTS_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: str
    version: str
    target_ref: str
    nodes: _containers.MessageMap[str, MissionNode]
    edges: _containers.RepeatedCompositeFieldContainer[MissionEdge]
    entry_points: _containers.RepeatedScalarFieldContainer[str]
    exit_points: _containers.RepeatedScalarFieldContainer[str]
    metadata: _containers.ScalarMap[str, str]
    dependencies: MissionDependencies
    source: str
    installed_at: _timestamp_pb2.Timestamp
    created_at: _timestamp_pb2.Timestamp
    workspace: WorkspaceConfig
    constraints: MissionConstraints
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., version: _Optional[str] = ..., target_ref: _Optional[str] = ..., nodes: _Optional[_Mapping[str, MissionNode]] = ..., edges: _Optional[_Iterable[_Union[MissionEdge, _Mapping]]] = ..., entry_points: _Optional[_Iterable[str]] = ..., exit_points: _Optional[_Iterable[str]] = ..., metadata: _Optional[_Mapping[str, str]] = ..., dependencies: _Optional[_Union[MissionDependencies, _Mapping]] = ..., source: _Optional[str] = ..., installed_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., workspace: _Optional[_Union[WorkspaceConfig, _Mapping]] = ..., constraints: _Optional[_Union[MissionConstraints, _Mapping]] = ...) -> None: ...

class MissionConstraints(_message.Message):
    __slots__ = ("max_duration", "max_tokens", "max_cost", "max_findings", "severity_threshold", "require_evidence", "blocked_tools", "blocked_domains", "max_turns_per_agent", "allowed_techniques", "blocked_techniques", "max_tokens_per_call")
    MAX_DURATION_FIELD_NUMBER: _ClassVar[int]
    MAX_TOKENS_FIELD_NUMBER: _ClassVar[int]
    MAX_COST_FIELD_NUMBER: _ClassVar[int]
    MAX_FINDINGS_FIELD_NUMBER: _ClassVar[int]
    SEVERITY_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    REQUIRE_EVIDENCE_FIELD_NUMBER: _ClassVar[int]
    BLOCKED_TOOLS_FIELD_NUMBER: _ClassVar[int]
    BLOCKED_DOMAINS_FIELD_NUMBER: _ClassVar[int]
    MAX_TURNS_PER_AGENT_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_TECHNIQUES_FIELD_NUMBER: _ClassVar[int]
    BLOCKED_TECHNIQUES_FIELD_NUMBER: _ClassVar[int]
    MAX_TOKENS_PER_CALL_FIELD_NUMBER: _ClassVar[int]
    max_duration: _duration_pb2.Duration
    max_tokens: int
    max_cost: float
    max_findings: int
    severity_threshold: str
    require_evidence: bool
    blocked_tools: _containers.RepeatedScalarFieldContainer[str]
    blocked_domains: _containers.RepeatedScalarFieldContainer[str]
    max_turns_per_agent: int
    allowed_techniques: _containers.RepeatedScalarFieldContainer[str]
    blocked_techniques: _containers.RepeatedScalarFieldContainer[str]
    max_tokens_per_call: int
    def __init__(self, max_duration: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ..., max_tokens: _Optional[int] = ..., max_cost: _Optional[float] = ..., max_findings: _Optional[int] = ..., severity_threshold: _Optional[str] = ..., require_evidence: bool = ..., blocked_tools: _Optional[_Iterable[str]] = ..., blocked_domains: _Optional[_Iterable[str]] = ..., max_turns_per_agent: _Optional[int] = ..., allowed_techniques: _Optional[_Iterable[str]] = ..., blocked_techniques: _Optional[_Iterable[str]] = ..., max_tokens_per_call: _Optional[int] = ...) -> None: ...

class MissionDependencies(_message.Message):
    __slots__ = ("agents", "tools", "plugins")
    AGENTS_FIELD_NUMBER: _ClassVar[int]
    TOOLS_FIELD_NUMBER: _ClassVar[int]
    PLUGINS_FIELD_NUMBER: _ClassVar[int]
    agents: _containers.RepeatedScalarFieldContainer[str]
    tools: _containers.RepeatedScalarFieldContainer[str]
    plugins: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, agents: _Optional[_Iterable[str]] = ..., tools: _Optional[_Iterable[str]] = ..., plugins: _Optional[_Iterable[str]] = ...) -> None: ...

class MissionNode(_message.Message):
    __slots__ = ("id", "type", "name", "description", "agent_config", "tool_config", "plugin_config", "condition_config", "parallel_config", "join_config", "dependencies", "timeout", "retry_policy", "data_policy", "metadata", "reuse_policy")
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    AGENT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    TOOL_CONFIG_FIELD_NUMBER: _ClassVar[int]
    PLUGIN_CONFIG_FIELD_NUMBER: _ClassVar[int]
    CONDITION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    PARALLEL_CONFIG_FIELD_NUMBER: _ClassVar[int]
    JOIN_CONFIG_FIELD_NUMBER: _ClassVar[int]
    DEPENDENCIES_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    RETRY_POLICY_FIELD_NUMBER: _ClassVar[int]
    DATA_POLICY_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    REUSE_POLICY_FIELD_NUMBER: _ClassVar[int]
    id: str
    type: NodeType
    name: str
    description: str
    agent_config: AgentNodeConfig
    tool_config: ToolNodeConfig
    plugin_config: PluginNodeConfig
    condition_config: ConditionNodeConfig
    parallel_config: ParallelNodeConfig
    join_config: JoinNodeConfig
    dependencies: _containers.RepeatedScalarFieldContainer[str]
    timeout: _duration_pb2.Duration
    retry_policy: RetryPolicy
    data_policy: DataPolicy
    metadata: _containers.ScalarMap[str, str]
    reuse_policy: ReusePolicy
    def __init__(self, id: _Optional[str] = ..., type: _Optional[_Union[NodeType, str]] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., agent_config: _Optional[_Union[AgentNodeConfig, _Mapping]] = ..., tool_config: _Optional[_Union[ToolNodeConfig, _Mapping]] = ..., plugin_config: _Optional[_Union[PluginNodeConfig, _Mapping]] = ..., condition_config: _Optional[_Union[ConditionNodeConfig, _Mapping]] = ..., parallel_config: _Optional[_Union[ParallelNodeConfig, _Mapping]] = ..., join_config: _Optional[_Union[JoinNodeConfig, _Mapping]] = ..., dependencies: _Optional[_Iterable[str]] = ..., timeout: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ..., retry_policy: _Optional[_Union[RetryPolicy, _Mapping]] = ..., data_policy: _Optional[_Union[DataPolicy, _Mapping]] = ..., metadata: _Optional[_Mapping[str, str]] = ..., reuse_policy: _Optional[_Union[ReusePolicy, _Mapping]] = ...) -> None: ...

class AgentNodeConfig(_message.Message):
    __slots__ = ("agent_name", "task", "max_tokens_per_call")
    AGENT_NAME_FIELD_NUMBER: _ClassVar[int]
    TASK_FIELD_NUMBER: _ClassVar[int]
    MAX_TOKENS_PER_CALL_FIELD_NUMBER: _ClassVar[int]
    agent_name: str
    task: _types_pb2.Task
    max_tokens_per_call: int
    def __init__(self, agent_name: _Optional[str] = ..., task: _Optional[_Union[_types_pb2.Task, _Mapping]] = ..., max_tokens_per_call: _Optional[int] = ...) -> None: ...

class ToolNodeConfig(_message.Message):
    __slots__ = ("tool_name", "input", "max_tokens_per_call")
    class InputEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    TOOL_NAME_FIELD_NUMBER: _ClassVar[int]
    INPUT_FIELD_NUMBER: _ClassVar[int]
    MAX_TOKENS_PER_CALL_FIELD_NUMBER: _ClassVar[int]
    tool_name: str
    input: _containers.ScalarMap[str, str]
    max_tokens_per_call: int
    def __init__(self, tool_name: _Optional[str] = ..., input: _Optional[_Mapping[str, str]] = ..., max_tokens_per_call: _Optional[int] = ...) -> None: ...

class PluginNodeConfig(_message.Message):
    __slots__ = ("plugin_name", "method", "params", "max_tokens_per_call")
    class ParamsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    PLUGIN_NAME_FIELD_NUMBER: _ClassVar[int]
    METHOD_FIELD_NUMBER: _ClassVar[int]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    MAX_TOKENS_PER_CALL_FIELD_NUMBER: _ClassVar[int]
    plugin_name: str
    method: str
    params: _containers.ScalarMap[str, str]
    max_tokens_per_call: int
    def __init__(self, plugin_name: _Optional[str] = ..., method: _Optional[str] = ..., params: _Optional[_Mapping[str, str]] = ..., max_tokens_per_call: _Optional[int] = ...) -> None: ...

class ConditionNodeConfig(_message.Message):
    __slots__ = ("expression", "true_branch", "false_branch", "language")
    EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    TRUE_BRANCH_FIELD_NUMBER: _ClassVar[int]
    FALSE_BRANCH_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    expression: str
    true_branch: _containers.RepeatedScalarFieldContainer[str]
    false_branch: _containers.RepeatedScalarFieldContainer[str]
    language: Language
    def __init__(self, expression: _Optional[str] = ..., true_branch: _Optional[_Iterable[str]] = ..., false_branch: _Optional[_Iterable[str]] = ..., language: _Optional[_Union[Language, str]] = ...) -> None: ...

class ParallelNodeConfig(_message.Message):
    __slots__ = ("sub_nodes", "max_concurrency")
    SUB_NODES_FIELD_NUMBER: _ClassVar[int]
    MAX_CONCURRENCY_FIELD_NUMBER: _ClassVar[int]
    sub_nodes: _containers.RepeatedCompositeFieldContainer[MissionNode]
    max_concurrency: int
    def __init__(self, sub_nodes: _Optional[_Iterable[_Union[MissionNode, _Mapping]]] = ..., max_concurrency: _Optional[int] = ...) -> None: ...

class JoinNodeConfig(_message.Message):
    __slots__ = ("wait_for", "strategy", "aggregator")
    WAIT_FOR_FIELD_NUMBER: _ClassVar[int]
    STRATEGY_FIELD_NUMBER: _ClassVar[int]
    AGGREGATOR_FIELD_NUMBER: _ClassVar[int]
    wait_for: _containers.RepeatedScalarFieldContainer[str]
    strategy: MergeStrategy
    aggregator: str
    def __init__(self, wait_for: _Optional[_Iterable[str]] = ..., strategy: _Optional[_Union[MergeStrategy, str]] = ..., aggregator: _Optional[str] = ...) -> None: ...

class WorkspaceConfig(_message.Message):
    __slots__ = ("repositories", "settings")
    REPOSITORIES_FIELD_NUMBER: _ClassVar[int]
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    repositories: _containers.RepeatedCompositeFieldContainer[RepositoryConfig]
    settings: WorkspaceSettings
    def __init__(self, repositories: _Optional[_Iterable[_Union[RepositoryConfig, _Mapping]]] = ..., settings: _Optional[_Union[WorkspaceSettings, _Mapping]] = ...) -> None: ...

class RepositoryConfig(_message.Message):
    __slots__ = ("name", "url", "branch", "credential_name", "shallow", "depends_on")
    NAME_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    BRANCH_FIELD_NUMBER: _ClassVar[int]
    CREDENTIAL_NAME_FIELD_NUMBER: _ClassVar[int]
    SHALLOW_FIELD_NUMBER: _ClassVar[int]
    DEPENDS_ON_FIELD_NUMBER: _ClassVar[int]
    name: str
    url: str
    branch: str
    credential_name: str
    shallow: bool
    depends_on: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, name: _Optional[str] = ..., url: _Optional[str] = ..., branch: _Optional[str] = ..., credential_name: _Optional[str] = ..., shallow: bool = ..., depends_on: _Optional[_Iterable[str]] = ...) -> None: ...

class WorkspaceSettings(_message.Message):
    __slots__ = ("cleanup_on_complete", "use_worktrees", "lsp_enabled", "lsp_timeout", "base_directory")
    CLEANUP_ON_COMPLETE_FIELD_NUMBER: _ClassVar[int]
    USE_WORKTREES_FIELD_NUMBER: _ClassVar[int]
    LSP_ENABLED_FIELD_NUMBER: _ClassVar[int]
    LSP_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    BASE_DIRECTORY_FIELD_NUMBER: _ClassVar[int]
    cleanup_on_complete: bool
    use_worktrees: bool
    lsp_enabled: bool
    lsp_timeout: _duration_pb2.Duration
    base_directory: str
    def __init__(self, cleanup_on_complete: bool = ..., use_worktrees: bool = ..., lsp_enabled: bool = ..., lsp_timeout: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ..., base_directory: _Optional[str] = ...) -> None: ...

class ReusePolicy(_message.Message):
    __slots__ = ("output_scope", "input_scope", "reuse")
    OUTPUT_SCOPE_FIELD_NUMBER: _ClassVar[int]
    INPUT_SCOPE_FIELD_NUMBER: _ClassVar[int]
    REUSE_FIELD_NUMBER: _ClassVar[int]
    output_scope: str
    input_scope: str
    reuse: str
    def __init__(self, output_scope: _Optional[str] = ..., input_scope: _Optional[str] = ..., reuse: _Optional[str] = ...) -> None: ...

class RetryPolicy(_message.Message):
    __slots__ = ("max_retries", "backoff_strategy", "initial_delay", "max_delay", "multiplier")
    MAX_RETRIES_FIELD_NUMBER: _ClassVar[int]
    BACKOFF_STRATEGY_FIELD_NUMBER: _ClassVar[int]
    INITIAL_DELAY_FIELD_NUMBER: _ClassVar[int]
    MAX_DELAY_FIELD_NUMBER: _ClassVar[int]
    MULTIPLIER_FIELD_NUMBER: _ClassVar[int]
    max_retries: int
    backoff_strategy: BackoffStrategy
    initial_delay: _duration_pb2.Duration
    max_delay: _duration_pb2.Duration
    multiplier: float
    def __init__(self, max_retries: _Optional[int] = ..., backoff_strategy: _Optional[_Union[BackoffStrategy, str]] = ..., initial_delay: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ..., max_delay: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ..., multiplier: _Optional[float] = ...) -> None: ...

class DataPolicy(_message.Message):
    __slots__ = ("store_input", "store_output", "retention", "encryption", "access_control")
    STORE_INPUT_FIELD_NUMBER: _ClassVar[int]
    STORE_OUTPUT_FIELD_NUMBER: _ClassVar[int]
    RETENTION_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_FIELD_NUMBER: _ClassVar[int]
    ACCESS_CONTROL_FIELD_NUMBER: _ClassVar[int]
    store_input: bool
    store_output: bool
    retention: _duration_pb2.Duration
    encryption: bool
    access_control: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, store_input: bool = ..., store_output: bool = ..., retention: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ..., encryption: bool = ..., access_control: _Optional[_Iterable[str]] = ...) -> None: ...

class MissionEdge(_message.Message):
    __slots__ = ("to", "condition", "metadata")
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    FROM_FIELD_NUMBER: _ClassVar[int]
    TO_FIELD_NUMBER: _ClassVar[int]
    CONDITION_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    to: str
    condition: str
    metadata: _containers.ScalarMap[str, str]
    def __init__(self, to: _Optional[str] = ..., condition: _Optional[str] = ..., metadata: _Optional[_Mapping[str, str]] = ..., **kwargs) -> None: ...
