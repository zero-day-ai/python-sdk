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

class PrincipalKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PRINCIPAL_KIND_UNSPECIFIED: _ClassVar[PrincipalKind]
    PRINCIPAL_KIND_AGENT: _ClassVar[PrincipalKind]
    PRINCIPAL_KIND_TOOL: _ClassVar[PrincipalKind]
    PRINCIPAL_KIND_PLUGIN: _ClassVar[PrincipalKind]

class CredentialFieldType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CREDENTIAL_FIELD_TYPE_UNSPECIFIED: _ClassVar[CredentialFieldType]
    CREDENTIAL_FIELD_TYPE_TEXT: _ClassVar[CredentialFieldType]
    CREDENTIAL_FIELD_TYPE_PASSWORD: _ClassVar[CredentialFieldType]
    CREDENTIAL_FIELD_TYPE_URL: _ClassVar[CredentialFieldType]
    CREDENTIAL_FIELD_TYPE_REGION: _ClassVar[CredentialFieldType]
    CREDENTIAL_FIELD_TYPE_BOOL: _ClassVar[CredentialFieldType]
PRINCIPAL_KIND_UNSPECIFIED: PrincipalKind
PRINCIPAL_KIND_AGENT: PrincipalKind
PRINCIPAL_KIND_TOOL: PrincipalKind
PRINCIPAL_KIND_PLUGIN: PrincipalKind
CREDENTIAL_FIELD_TYPE_UNSPECIFIED: CredentialFieldType
CREDENTIAL_FIELD_TYPE_TEXT: CredentialFieldType
CREDENTIAL_FIELD_TYPE_PASSWORD: CredentialFieldType
CREDENTIAL_FIELD_TYPE_URL: CredentialFieldType
CREDENTIAL_FIELD_TYPE_REGION: CredentialFieldType
CREDENTIAL_FIELD_TYPE_BOOL: CredentialFieldType

class ComponentGrant(_message.Message):
    __slots__ = ("component_ref", "relation")
    COMPONENT_REF_FIELD_NUMBER: _ClassVar[int]
    RELATION_FIELD_NUMBER: _ClassVar[int]
    component_ref: str
    relation: str
    def __init__(self, component_ref: _Optional[str] = ..., relation: _Optional[str] = ...) -> None: ...

class CreateAgentIdentityRequest(_message.Message):
    __slots__ = ("name", "kind", "description", "component_grants")
    NAME_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    COMPONENT_GRANTS_FIELD_NUMBER: _ClassVar[int]
    name: str
    kind: PrincipalKind
    description: str
    component_grants: _containers.RepeatedCompositeFieldContainer[ComponentGrant]
    def __init__(self, name: _Optional[str] = ..., kind: _Optional[_Union[PrincipalKind, str]] = ..., description: _Optional[str] = ..., component_grants: _Optional[_Iterable[_Union[ComponentGrant, _Mapping]]] = ...) -> None: ...

class CreateAgentIdentityResponse(_message.Message):
    __slots__ = ("principal_id", "kind", "name", "client_id", "client_secret", "gibson_url", "enroll_command")
    PRINCIPAL_ID_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_SECRET_FIELD_NUMBER: _ClassVar[int]
    GIBSON_URL_FIELD_NUMBER: _ClassVar[int]
    ENROLL_COMMAND_FIELD_NUMBER: _ClassVar[int]
    principal_id: str
    kind: PrincipalKind
    name: str
    client_id: str
    client_secret: str
    gibson_url: str
    enroll_command: str
    def __init__(self, principal_id: _Optional[str] = ..., kind: _Optional[_Union[PrincipalKind, str]] = ..., name: _Optional[str] = ..., client_id: _Optional[str] = ..., client_secret: _Optional[str] = ..., gibson_url: _Optional[str] = ..., enroll_command: _Optional[str] = ...) -> None: ...

class ListAgentIdentitiesRequest(_message.Message):
    __slots__ = ("page_size", "page_token", "kind_filter")
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    KIND_FILTER_FIELD_NUMBER: _ClassVar[int]
    page_size: int
    page_token: str
    kind_filter: PrincipalKind
    def __init__(self, page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., kind_filter: _Optional[_Union[PrincipalKind, str]] = ...) -> None: ...

class AgentIdentity(_message.Message):
    __slots__ = ("principal_id", "kind", "name", "description", "created_at", "last_authenticated_at", "revoked", "created_by_subject")
    PRINCIPAL_ID_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    LAST_AUTHENTICATED_AT_FIELD_NUMBER: _ClassVar[int]
    REVOKED_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_SUBJECT_FIELD_NUMBER: _ClassVar[int]
    principal_id: str
    kind: PrincipalKind
    name: str
    description: str
    created_at: _timestamp_pb2.Timestamp
    last_authenticated_at: _timestamp_pb2.Timestamp
    revoked: bool
    created_by_subject: str
    def __init__(self, principal_id: _Optional[str] = ..., kind: _Optional[_Union[PrincipalKind, str]] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., last_authenticated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., revoked: bool = ..., created_by_subject: _Optional[str] = ...) -> None: ...

class ListAgentIdentitiesResponse(_message.Message):
    __slots__ = ("identities", "next_page_token")
    IDENTITIES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    identities: _containers.RepeatedCompositeFieldContainer[AgentIdentity]
    next_page_token: str
    def __init__(self, identities: _Optional[_Iterable[_Union[AgentIdentity, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class RevokeAgentIdentityRequest(_message.Message):
    __slots__ = ("principal_id",)
    PRINCIPAL_ID_FIELD_NUMBER: _ClassVar[int]
    principal_id: str
    def __init__(self, principal_id: _Optional[str] = ...) -> None: ...

class RevokeAgentIdentityResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetOnboardingStateRequest(_message.Message):
    __slots__ = ("tenant_id",)
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    tenant_id: str
    def __init__(self, tenant_id: _Optional[str] = ...) -> None: ...

class GetOnboardingStateResponse(_message.Message):
    __slots__ = ("current_step", "completed_steps", "setup_tasks", "completed_at")
    class SetupTasksEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    CURRENT_STEP_FIELD_NUMBER: _ClassVar[int]
    COMPLETED_STEPS_FIELD_NUMBER: _ClassVar[int]
    SETUP_TASKS_FIELD_NUMBER: _ClassVar[int]
    COMPLETED_AT_FIELD_NUMBER: _ClassVar[int]
    current_step: str
    completed_steps: _containers.RepeatedScalarFieldContainer[str]
    setup_tasks: _containers.ScalarMap[str, str]
    completed_at: str
    def __init__(self, current_step: _Optional[str] = ..., completed_steps: _Optional[_Iterable[str]] = ..., setup_tasks: _Optional[_Mapping[str, str]] = ..., completed_at: _Optional[str] = ...) -> None: ...

class UpdateOnboardingStateRequest(_message.Message):
    __slots__ = ("tenant_id", "current_step", "completed_steps", "setup_tasks")
    class SetupTasksEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    CURRENT_STEP_FIELD_NUMBER: _ClassVar[int]
    COMPLETED_STEPS_FIELD_NUMBER: _ClassVar[int]
    SETUP_TASKS_FIELD_NUMBER: _ClassVar[int]
    tenant_id: str
    current_step: str
    completed_steps: _containers.RepeatedScalarFieldContainer[str]
    setup_tasks: _containers.ScalarMap[str, str]
    def __init__(self, tenant_id: _Optional[str] = ..., current_step: _Optional[str] = ..., completed_steps: _Optional[_Iterable[str]] = ..., setup_tasks: _Optional[_Mapping[str, str]] = ...) -> None: ...

class UpdateOnboardingStateResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetTenantQuotaRequest(_message.Message):
    __slots__ = ("tenant_id",)
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    tenant_id: str
    def __init__(self, tenant_id: _Optional[str] = ...) -> None: ...

class GetTenantQuotaResponse(_message.Message):
    __slots__ = ("concurrent_missions", "concurrent_agents", "updated_at")
    CONCURRENT_MISSIONS_FIELD_NUMBER: _ClassVar[int]
    CONCURRENT_AGENTS_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    concurrent_missions: int
    concurrent_agents: int
    updated_at: str
    def __init__(self, concurrent_missions: _Optional[int] = ..., concurrent_agents: _Optional[int] = ..., updated_at: _Optional[str] = ...) -> None: ...

class GetTenantQuotaUsageRequest(_message.Message):
    __slots__ = ("tenant_id",)
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    tenant_id: str
    def __init__(self, tenant_id: _Optional[str] = ...) -> None: ...

class GetTenantQuotaUsageResponse(_message.Message):
    __slots__ = ("missions_active", "agents_active")
    MISSIONS_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    AGENTS_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    missions_active: int
    agents_active: int
    def __init__(self, missions_active: _Optional[int] = ..., agents_active: _Optional[int] = ...) -> None: ...

class AuditEvent(_message.Message):
    __slots__ = ("event_type", "timestamp", "actor_user_id", "actor_email", "tenant_id", "target_user_id", "target_resource", "details", "trace_id")
    class DetailsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    ACTOR_USER_ID_FIELD_NUMBER: _ClassVar[int]
    ACTOR_EMAIL_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_USER_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_RESOURCE_FIELD_NUMBER: _ClassVar[int]
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    TRACE_ID_FIELD_NUMBER: _ClassVar[int]
    event_type: str
    timestamp: str
    actor_user_id: str
    actor_email: str
    tenant_id: str
    target_user_id: str
    target_resource: str
    details: _containers.ScalarMap[str, str]
    trace_id: str
    def __init__(self, event_type: _Optional[str] = ..., timestamp: _Optional[str] = ..., actor_user_id: _Optional[str] = ..., actor_email: _Optional[str] = ..., tenant_id: _Optional[str] = ..., target_user_id: _Optional[str] = ..., target_resource: _Optional[str] = ..., details: _Optional[_Mapping[str, str]] = ..., trace_id: _Optional[str] = ...) -> None: ...

class ListAuditEventsRequest(_message.Message):
    __slots__ = ("tenant_id", "event_types", "actor_user_id", "target_match", "from_time", "to_time", "limit", "cursor")
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    EVENT_TYPES_FIELD_NUMBER: _ClassVar[int]
    ACTOR_USER_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_MATCH_FIELD_NUMBER: _ClassVar[int]
    FROM_TIME_FIELD_NUMBER: _ClassVar[int]
    TO_TIME_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    tenant_id: str
    event_types: _containers.RepeatedScalarFieldContainer[str]
    actor_user_id: str
    target_match: str
    from_time: str
    to_time: str
    limit: int
    cursor: str
    def __init__(self, tenant_id: _Optional[str] = ..., event_types: _Optional[_Iterable[str]] = ..., actor_user_id: _Optional[str] = ..., target_match: _Optional[str] = ..., from_time: _Optional[str] = ..., to_time: _Optional[str] = ..., limit: _Optional[int] = ..., cursor: _Optional[str] = ...) -> None: ...

class ListAuditEventsResponse(_message.Message):
    __slots__ = ("events", "next_cursor")
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_CURSOR_FIELD_NUMBER: _ClassVar[int]
    events: _containers.RepeatedCompositeFieldContainer[AuditEvent]
    next_cursor: str
    def __init__(self, events: _Optional[_Iterable[_Union[AuditEvent, _Mapping]]] = ..., next_cursor: _Optional[str] = ...) -> None: ...

class FindingFilters(_message.Message):
    __slots__ = ("severity", "type", "mission_id", "search")
    SEVERITY_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    MISSION_ID_FIELD_NUMBER: _ClassVar[int]
    SEARCH_FIELD_NUMBER: _ClassVar[int]
    severity: _containers.RepeatedScalarFieldContainer[str]
    type: _containers.RepeatedScalarFieldContainer[str]
    mission_id: str
    search: str
    def __init__(self, severity: _Optional[_Iterable[str]] = ..., type: _Optional[_Iterable[str]] = ..., mission_id: _Optional[str] = ..., search: _Optional[str] = ...) -> None: ...

class ExportFindingsRequest(_message.Message):
    __slots__ = ("tenant_id", "format", "finding_ids", "filters", "include_remediation", "include_evidence")
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    FINDING_IDS_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_REMEDIATION_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_EVIDENCE_FIELD_NUMBER: _ClassVar[int]
    tenant_id: str
    format: str
    finding_ids: _containers.RepeatedScalarFieldContainer[str]
    filters: FindingFilters
    include_remediation: bool
    include_evidence: bool
    def __init__(self, tenant_id: _Optional[str] = ..., format: _Optional[str] = ..., finding_ids: _Optional[_Iterable[str]] = ..., filters: _Optional[_Union[FindingFilters, _Mapping]] = ..., include_remediation: bool = ..., include_evidence: bool = ...) -> None: ...

class ExportFindingsResponse(_message.Message):
    __slots__ = ("data", "format", "filename", "count")
    DATA_FIELD_NUMBER: _ClassVar[int]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    format: str
    filename: str
    count: int
    def __init__(self, data: _Optional[bytes] = ..., format: _Optional[str] = ..., filename: _Optional[str] = ..., count: _Optional[int] = ...) -> None: ...

class SaveMissionDraftRequest(_message.Message):
    __slots__ = ("tenant_id", "name", "cue_source", "draft_id")
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CUE_SOURCE_FIELD_NUMBER: _ClassVar[int]
    DRAFT_ID_FIELD_NUMBER: _ClassVar[int]
    tenant_id: str
    name: str
    cue_source: str
    draft_id: str
    def __init__(self, tenant_id: _Optional[str] = ..., name: _Optional[str] = ..., cue_source: _Optional[str] = ..., draft_id: _Optional[str] = ...) -> None: ...

class SaveMissionDraftResponse(_message.Message):
    __slots__ = ("draft_id",)
    DRAFT_ID_FIELD_NUMBER: _ClassVar[int]
    draft_id: str
    def __init__(self, draft_id: _Optional[str] = ...) -> None: ...

class ListMissionDraftsRequest(_message.Message):
    __slots__ = ("tenant_id",)
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    tenant_id: str
    def __init__(self, tenant_id: _Optional[str] = ...) -> None: ...

class MissionDraft(_message.Message):
    __slots__ = ("id", "name", "created_at", "updated_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    created_at: str
    updated_at: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., created_at: _Optional[str] = ..., updated_at: _Optional[str] = ...) -> None: ...

class ListMissionDraftsResponse(_message.Message):
    __slots__ = ("drafts",)
    DRAFTS_FIELD_NUMBER: _ClassVar[int]
    drafts: _containers.RepeatedCompositeFieldContainer[MissionDraft]
    def __init__(self, drafts: _Optional[_Iterable[_Union[MissionDraft, _Mapping]]] = ...) -> None: ...

class GetMissionDraftRequest(_message.Message):
    __slots__ = ("tenant_id", "draft_id")
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    DRAFT_ID_FIELD_NUMBER: _ClassVar[int]
    tenant_id: str
    draft_id: str
    def __init__(self, tenant_id: _Optional[str] = ..., draft_id: _Optional[str] = ...) -> None: ...

class GetMissionDraftResponse(_message.Message):
    __slots__ = ("draft",)
    DRAFT_FIELD_NUMBER: _ClassVar[int]
    draft: MissionDraftFull
    def __init__(self, draft: _Optional[_Union[MissionDraftFull, _Mapping]] = ...) -> None: ...

class MissionDraftFull(_message.Message):
    __slots__ = ("id", "name", "created_at", "updated_at", "cue_source")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    CUE_SOURCE_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    created_at: str
    updated_at: str
    cue_source: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., created_at: _Optional[str] = ..., updated_at: _Optional[str] = ..., cue_source: _Optional[str] = ...) -> None: ...

class DeleteMissionDraftRequest(_message.Message):
    __slots__ = ("tenant_id", "draft_id")
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    DRAFT_ID_FIELD_NUMBER: _ClassVar[int]
    tenant_id: str
    draft_id: str
    def __init__(self, tenant_id: _Optional[str] = ..., draft_id: _Optional[str] = ...) -> None: ...

class DeleteMissionDraftResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ProviderRecord(_message.Message):
    __slots__ = ("id", "name", "type", "default_model", "is_default", "enabled", "credentials_masked", "created_at", "updated_at")
    class CredentialsMaskedEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_MODEL_FIELD_NUMBER: _ClassVar[int]
    IS_DEFAULT_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    CREDENTIALS_MASKED_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    type: str
    default_model: str
    is_default: bool
    enabled: bool
    credentials_masked: _containers.ScalarMap[str, str]
    created_at: str
    updated_at: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., type: _Optional[str] = ..., default_model: _Optional[str] = ..., is_default: bool = ..., enabled: bool = ..., credentials_masked: _Optional[_Mapping[str, str]] = ..., created_at: _Optional[str] = ..., updated_at: _Optional[str] = ...) -> None: ...

class ProviderConfigInput(_message.Message):
    __slots__ = ("name", "type", "default_model", "credentials", "set_as_default")
    class CredentialsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_MODEL_FIELD_NUMBER: _ClassVar[int]
    CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    SET_AS_DEFAULT_FIELD_NUMBER: _ClassVar[int]
    name: str
    type: str
    default_model: str
    credentials: _containers.ScalarMap[str, str]
    set_as_default: bool
    def __init__(self, name: _Optional[str] = ..., type: _Optional[str] = ..., default_model: _Optional[str] = ..., credentials: _Optional[_Mapping[str, str]] = ..., set_as_default: bool = ...) -> None: ...

class ResponseFormat(_message.Message):
    __slots__ = ("type", "name", "schema_json", "strict")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_JSON_FIELD_NUMBER: _ClassVar[int]
    STRICT_FIELD_NUMBER: _ClassVar[int]
    type: str
    name: str
    schema_json: str
    strict: bool
    def __init__(self, type: _Optional[str] = ..., name: _Optional[str] = ..., schema_json: _Optional[str] = ..., strict: bool = ...) -> None: ...

class LLMTokenUsage(_message.Message):
    __slots__ = ("input_tokens", "output_tokens", "total_tokens")
    INPUT_TOKENS_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_TOKENS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_TOKENS_FIELD_NUMBER: _ClassVar[int]
    input_tokens: int
    output_tokens: int
    total_tokens: int
    def __init__(self, input_tokens: _Optional[int] = ..., output_tokens: _Optional[int] = ..., total_tokens: _Optional[int] = ...) -> None: ...

class LLMToolCall(_message.Message):
    __slots__ = ("id", "name", "arguments")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ARGUMENTS_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    arguments: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., arguments: _Optional[str] = ...) -> None: ...

class LLMToolResult(_message.Message):
    __slots__ = ("tool_call_id", "content", "is_error")
    TOOL_CALL_ID_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    IS_ERROR_FIELD_NUMBER: _ClassVar[int]
    tool_call_id: str
    content: str
    is_error: bool
    def __init__(self, tool_call_id: _Optional[str] = ..., content: _Optional[str] = ..., is_error: bool = ...) -> None: ...

class LLMToolDef(_message.Message):
    __slots__ = ("name", "description", "parameters_json")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_JSON_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    parameters_json: str
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., parameters_json: _Optional[str] = ...) -> None: ...

class LLMMessageContent(_message.Message):
    __slots__ = ("role", "content", "tool_calls", "tool_results", "name")
    ROLE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    TOOL_CALLS_FIELD_NUMBER: _ClassVar[int]
    TOOL_RESULTS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    role: str
    content: str
    tool_calls: _containers.RepeatedCompositeFieldContainer[LLMToolCall]
    tool_results: _containers.RepeatedCompositeFieldContainer[LLMToolResult]
    name: str
    def __init__(self, role: _Optional[str] = ..., content: _Optional[str] = ..., tool_calls: _Optional[_Iterable[_Union[LLMToolCall, _Mapping]]] = ..., tool_results: _Optional[_Iterable[_Union[LLMToolResult, _Mapping]]] = ..., name: _Optional[str] = ...) -> None: ...

class ListProvidersRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListProvidersResponse(_message.Message):
    __slots__ = ("providers",)
    PROVIDERS_FIELD_NUMBER: _ClassVar[int]
    providers: _containers.RepeatedCompositeFieldContainer[ProviderRecord]
    def __init__(self, providers: _Optional[_Iterable[_Union[ProviderRecord, _Mapping]]] = ...) -> None: ...

class GetProviderRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class GetProviderResponse(_message.Message):
    __slots__ = ("provider",)
    PROVIDER_FIELD_NUMBER: _ClassVar[int]
    provider: ProviderRecord
    def __init__(self, provider: _Optional[_Union[ProviderRecord, _Mapping]] = ...) -> None: ...

class CreateProviderRequest(_message.Message):
    __slots__ = ("input",)
    INPUT_FIELD_NUMBER: _ClassVar[int]
    input: ProviderConfigInput
    def __init__(self, input: _Optional[_Union[ProviderConfigInput, _Mapping]] = ...) -> None: ...

class CreateProviderResponse(_message.Message):
    __slots__ = ("provider",)
    PROVIDER_FIELD_NUMBER: _ClassVar[int]
    provider: ProviderRecord
    def __init__(self, provider: _Optional[_Union[ProviderRecord, _Mapping]] = ...) -> None: ...

class UpdateProviderRequest(_message.Message):
    __slots__ = ("name", "input")
    NAME_FIELD_NUMBER: _ClassVar[int]
    INPUT_FIELD_NUMBER: _ClassVar[int]
    name: str
    input: ProviderConfigInput
    def __init__(self, name: _Optional[str] = ..., input: _Optional[_Union[ProviderConfigInput, _Mapping]] = ...) -> None: ...

class UpdateProviderResponse(_message.Message):
    __slots__ = ("provider",)
    PROVIDER_FIELD_NUMBER: _ClassVar[int]
    provider: ProviderRecord
    def __init__(self, provider: _Optional[_Union[ProviderRecord, _Mapping]] = ...) -> None: ...

class DeleteProviderRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class DeleteProviderResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class TestProviderRequest(_message.Message):
    __slots__ = ("input",)
    INPUT_FIELD_NUMBER: _ClassVar[int]
    input: ProviderConfigInput
    def __init__(self, input: _Optional[_Union[ProviderConfigInput, _Mapping]] = ...) -> None: ...

class TestProviderResponse(_message.Message):
    __slots__ = ("ok", "latency_ms", "model", "error", "models")
    OK_FIELD_NUMBER: _ClassVar[int]
    LATENCY_MS_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    MODELS_FIELD_NUMBER: _ClassVar[int]
    ok: bool
    latency_ms: int
    model: str
    error: str
    models: _containers.RepeatedCompositeFieldContainer[ModelDescriptor]
    def __init__(self, ok: bool = ..., latency_ms: _Optional[int] = ..., model: _Optional[str] = ..., error: _Optional[str] = ..., models: _Optional[_Iterable[_Union[ModelDescriptor, _Mapping]]] = ...) -> None: ...

class GetSupportedProvidersRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetSupportedProvidersResponse(_message.Message):
    __slots__ = ("providers",)
    PROVIDERS_FIELD_NUMBER: _ClassVar[int]
    providers: _containers.RepeatedCompositeFieldContainer[SupportedProvider]
    def __init__(self, providers: _Optional[_Iterable[_Union[SupportedProvider, _Mapping]]] = ...) -> None: ...

class ListProviderModelsRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListProviderModelsResponse(_message.Message):
    __slots__ = ("ok", "error_message", "error_class", "models", "latency_ms")
    OK_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ERROR_CLASS_FIELD_NUMBER: _ClassVar[int]
    MODELS_FIELD_NUMBER: _ClassVar[int]
    LATENCY_MS_FIELD_NUMBER: _ClassVar[int]
    ok: bool
    error_message: str
    error_class: str
    models: _containers.RepeatedCompositeFieldContainer[ModelDescriptor]
    latency_ms: int
    def __init__(self, ok: bool = ..., error_message: _Optional[str] = ..., error_class: _Optional[str] = ..., models: _Optional[_Iterable[_Union[ModelDescriptor, _Mapping]]] = ..., latency_ms: _Optional[int] = ...) -> None: ...

class SupportedProvider(_message.Message):
    __slots__ = ("type", "display_name", "docs_url", "self_hosted", "credentials", "default_models")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DOCS_URL_FIELD_NUMBER: _ClassVar[int]
    SELF_HOSTED_FIELD_NUMBER: _ClassVar[int]
    CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_MODELS_FIELD_NUMBER: _ClassVar[int]
    type: str
    display_name: str
    docs_url: str
    self_hosted: bool
    credentials: _containers.RepeatedCompositeFieldContainer[CredentialField]
    default_models: _containers.RepeatedCompositeFieldContainer[ModelDescriptor]
    def __init__(self, type: _Optional[str] = ..., display_name: _Optional[str] = ..., docs_url: _Optional[str] = ..., self_hosted: bool = ..., credentials: _Optional[_Iterable[_Union[CredentialField, _Mapping]]] = ..., default_models: _Optional[_Iterable[_Union[ModelDescriptor, _Mapping]]] = ...) -> None: ...

class CredentialField(_message.Message):
    __slots__ = ("key", "label", "required", "secret", "placeholder", "help", "type")
    KEY_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_FIELD_NUMBER: _ClassVar[int]
    SECRET_FIELD_NUMBER: _ClassVar[int]
    PLACEHOLDER_FIELD_NUMBER: _ClassVar[int]
    HELP_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    key: str
    label: str
    required: bool
    secret: bool
    placeholder: str
    help: str
    type: CredentialFieldType
    def __init__(self, key: _Optional[str] = ..., label: _Optional[str] = ..., required: bool = ..., secret: bool = ..., placeholder: _Optional[str] = ..., help: _Optional[str] = ..., type: _Optional[_Union[CredentialFieldType, str]] = ...) -> None: ...

class ModelDescriptor(_message.Message):
    __slots__ = ("name", "family", "context_window")
    NAME_FIELD_NUMBER: _ClassVar[int]
    FAMILY_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_WINDOW_FIELD_NUMBER: _ClassVar[int]
    name: str
    family: str
    context_window: int
    def __init__(self, name: _Optional[str] = ..., family: _Optional[str] = ..., context_window: _Optional[int] = ...) -> None: ...

class GetProviderHealthRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class GetProviderHealthResponse(_message.Message):
    __slots__ = ("healthy", "last_checked_at", "error")
    HEALTHY_FIELD_NUMBER: _ClassVar[int]
    LAST_CHECKED_AT_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    healthy: bool
    last_checked_at: str
    error: str
    def __init__(self, healthy: bool = ..., last_checked_at: _Optional[str] = ..., error: _Optional[str] = ...) -> None: ...

class GetDefaultProviderRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetDefaultProviderResponse(_message.Message):
    __slots__ = ("provider",)
    PROVIDER_FIELD_NUMBER: _ClassVar[int]
    provider: ProviderRecord
    def __init__(self, provider: _Optional[_Union[ProviderRecord, _Mapping]] = ...) -> None: ...

class SetDefaultProviderRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class SetDefaultProviderResponse(_message.Message):
    __slots__ = ("provider",)
    PROVIDER_FIELD_NUMBER: _ClassVar[int]
    provider: ProviderRecord
    def __init__(self, provider: _Optional[_Union[ProviderRecord, _Mapping]] = ...) -> None: ...

class ExecuteLLMRequest(_message.Message):
    __slots__ = ("provider_name", "model", "messages", "tools", "response_format", "temperature", "max_tokens", "top_p", "stop")
    PROVIDER_NAME_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    TOOLS_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_FORMAT_FIELD_NUMBER: _ClassVar[int]
    TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
    MAX_TOKENS_FIELD_NUMBER: _ClassVar[int]
    TOP_P_FIELD_NUMBER: _ClassVar[int]
    STOP_FIELD_NUMBER: _ClassVar[int]
    provider_name: str
    model: str
    messages: _containers.RepeatedCompositeFieldContainer[LLMMessageContent]
    tools: _containers.RepeatedCompositeFieldContainer[LLMToolDef]
    response_format: ResponseFormat
    temperature: float
    max_tokens: int
    top_p: float
    stop: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, provider_name: _Optional[str] = ..., model: _Optional[str] = ..., messages: _Optional[_Iterable[_Union[LLMMessageContent, _Mapping]]] = ..., tools: _Optional[_Iterable[_Union[LLMToolDef, _Mapping]]] = ..., response_format: _Optional[_Union[ResponseFormat, _Mapping]] = ..., temperature: _Optional[float] = ..., max_tokens: _Optional[int] = ..., top_p: _Optional[float] = ..., stop: _Optional[_Iterable[str]] = ...) -> None: ...

class ExecuteLLMResponse(_message.Message):
    __slots__ = ("content", "tool_calls", "finish_reason", "usage")
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    TOOL_CALLS_FIELD_NUMBER: _ClassVar[int]
    FINISH_REASON_FIELD_NUMBER: _ClassVar[int]
    USAGE_FIELD_NUMBER: _ClassVar[int]
    content: str
    tool_calls: _containers.RepeatedCompositeFieldContainer[LLMToolCall]
    finish_reason: str
    usage: LLMTokenUsage
    def __init__(self, content: _Optional[str] = ..., tool_calls: _Optional[_Iterable[_Union[LLMToolCall, _Mapping]]] = ..., finish_reason: _Optional[str] = ..., usage: _Optional[_Union[LLMTokenUsage, _Mapping]] = ...) -> None: ...

class GetTenantLangfuseCredentialsRequest(_message.Message):
    __slots__ = ("tenant_id",)
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    tenant_id: str
    def __init__(self, tenant_id: _Optional[str] = ...) -> None: ...

class GetTenantLangfuseCredentialsResponse(_message.Message):
    __slots__ = ("public_key", "secret_key", "host", "project_id")
    PUBLIC_KEY_FIELD_NUMBER: _ClassVar[int]
    SECRET_KEY_FIELD_NUMBER: _ClassVar[int]
    HOST_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    public_key: str
    secret_key: str
    host: str
    project_id: str
    def __init__(self, public_key: _Optional[str] = ..., secret_key: _Optional[str] = ..., host: _Optional[str] = ..., project_id: _Optional[str] = ...) -> None: ...

class SetTenantLangfuseCredentialsRequest(_message.Message):
    __slots__ = ("tenant_id", "public_key", "secret_key", "host", "project_id")
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_KEY_FIELD_NUMBER: _ClassVar[int]
    SECRET_KEY_FIELD_NUMBER: _ClassVar[int]
    HOST_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    tenant_id: str
    public_key: str
    secret_key: str
    host: str
    project_id: str
    def __init__(self, tenant_id: _Optional[str] = ..., public_key: _Optional[str] = ..., secret_key: _Optional[str] = ..., host: _Optional[str] = ..., project_id: _Optional[str] = ...) -> None: ...

class SetTenantLangfuseCredentialsResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteTenantLangfuseCredentialsRequest(_message.Message):
    __slots__ = ("tenant_id",)
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    tenant_id: str
    def __init__(self, tenant_id: _Optional[str] = ...) -> None: ...

class DeleteTenantLangfuseCredentialsResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
