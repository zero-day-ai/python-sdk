from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NullValue(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NULL_VALUE_UNSPECIFIED: _ClassVar[NullValue]

class ErrorCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ERROR_CODE_UNSPECIFIED: _ClassVar[ErrorCode]
    ERROR_CODE_INTERNAL: _ClassVar[ErrorCode]
    ERROR_CODE_INVALID_ARGUMENT: _ClassVar[ErrorCode]
    ERROR_CODE_NOT_FOUND: _ClassVar[ErrorCode]
    ERROR_CODE_TIMEOUT: _ClassVar[ErrorCode]
    ERROR_CODE_UNAVAILABLE: _ClassVar[ErrorCode]
    ERROR_CODE_PERMISSION_DENIED: _ClassVar[ErrorCode]
    ERROR_CODE_ALREADY_EXISTS: _ClassVar[ErrorCode]
    ERROR_CODE_RESOURCE_EXHAUSTED: _ClassVar[ErrorCode]
    ERROR_CODE_CANCELLED: _ClassVar[ErrorCode]
    ERROR_CODE_AGENT_TIMEOUT: _ClassVar[ErrorCode]
    ERROR_CODE_AGENT_PANIC: _ClassVar[ErrorCode]
    ERROR_CODE_AGENT_INIT_FAILED: _ClassVar[ErrorCode]
    ERROR_CODE_LLM_RATE_LIMITED: _ClassVar[ErrorCode]
    ERROR_CODE_LLM_CONTEXT_EXCEEDED: _ClassVar[ErrorCode]
    ERROR_CODE_LLM_API_ERROR: _ClassVar[ErrorCode]
    ERROR_CODE_LLM_PARSE_ERROR: _ClassVar[ErrorCode]
    ERROR_CODE_TOOL_NOT_FOUND: _ClassVar[ErrorCode]
    ERROR_CODE_TOOL_TIMEOUT: _ClassVar[ErrorCode]
    ERROR_CODE_TOOL_EXEC_FAILED: _ClassVar[ErrorCode]
    ERROR_CODE_NETWORK_TIMEOUT: _ClassVar[ErrorCode]
    ERROR_CODE_NETWORK_UNREACHABLE: _ClassVar[ErrorCode]
    ERROR_CODE_TLS_ERROR: _ClassVar[ErrorCode]
    ERROR_CODE_DELEGATION_FAILED: _ClassVar[ErrorCode]
    ERROR_CODE_CHILD_AGENT_FAILED: _ClassVar[ErrorCode]
    ERROR_CODE_CONFIG_ERROR: _ClassVar[ErrorCode]

class HealthState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    HEALTH_STATE_UNSPECIFIED: _ClassVar[HealthState]
    HEALTH_STATE_HEALTHY: _ClassVar[HealthState]
    HEALTH_STATE_DEGRADED: _ClassVar[HealthState]
    HEALTH_STATE_UNHEALTHY: _ClassVar[HealthState]
NULL_VALUE_UNSPECIFIED: NullValue
ERROR_CODE_UNSPECIFIED: ErrorCode
ERROR_CODE_INTERNAL: ErrorCode
ERROR_CODE_INVALID_ARGUMENT: ErrorCode
ERROR_CODE_NOT_FOUND: ErrorCode
ERROR_CODE_TIMEOUT: ErrorCode
ERROR_CODE_UNAVAILABLE: ErrorCode
ERROR_CODE_PERMISSION_DENIED: ErrorCode
ERROR_CODE_ALREADY_EXISTS: ErrorCode
ERROR_CODE_RESOURCE_EXHAUSTED: ErrorCode
ERROR_CODE_CANCELLED: ErrorCode
ERROR_CODE_AGENT_TIMEOUT: ErrorCode
ERROR_CODE_AGENT_PANIC: ErrorCode
ERROR_CODE_AGENT_INIT_FAILED: ErrorCode
ERROR_CODE_LLM_RATE_LIMITED: ErrorCode
ERROR_CODE_LLM_CONTEXT_EXCEEDED: ErrorCode
ERROR_CODE_LLM_API_ERROR: ErrorCode
ERROR_CODE_LLM_PARSE_ERROR: ErrorCode
ERROR_CODE_TOOL_NOT_FOUND: ErrorCode
ERROR_CODE_TOOL_TIMEOUT: ErrorCode
ERROR_CODE_TOOL_EXEC_FAILED: ErrorCode
ERROR_CODE_NETWORK_TIMEOUT: ErrorCode
ERROR_CODE_NETWORK_UNREACHABLE: ErrorCode
ERROR_CODE_TLS_ERROR: ErrorCode
ERROR_CODE_DELEGATION_FAILED: ErrorCode
ERROR_CODE_CHILD_AGENT_FAILED: ErrorCode
ERROR_CODE_CONFIG_ERROR: ErrorCode
HEALTH_STATE_UNSPECIFIED: HealthState
HEALTH_STATE_HEALTHY: HealthState
HEALTH_STATE_DEGRADED: HealthState
HEALTH_STATE_UNHEALTHY: HealthState

class HealthStatus(_message.Message):
    __slots__ = ("status", "message", "checked_at")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    CHECKED_AT_FIELD_NUMBER: _ClassVar[int]
    status: str
    message: str
    checked_at: int
    def __init__(self, status: _Optional[str] = ..., message: _Optional[str] = ..., checked_at: _Optional[int] = ...) -> None: ...

class JSONSchema(_message.Message):
    __slots__ = ("json",)
    JSON_FIELD_NUMBER: _ClassVar[int]
    json: str
    def __init__(self, json: _Optional[str] = ...) -> None: ...

class Error(_message.Message):
    __slots__ = ("code", "message", "details", "retryable")
    CODE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    RETRYABLE_FIELD_NUMBER: _ClassVar[int]
    code: str
    message: str
    details: str
    retryable: bool
    def __init__(self, code: _Optional[str] = ..., message: _Optional[str] = ..., details: _Optional[str] = ..., retryable: bool = ...) -> None: ...

class TypedValue(_message.Message):
    __slots__ = ("null_value", "string_value", "int_value", "double_value", "bool_value", "bytes_value", "array_value", "map_value")
    NULL_VALUE_FIELD_NUMBER: _ClassVar[int]
    STRING_VALUE_FIELD_NUMBER: _ClassVar[int]
    INT_VALUE_FIELD_NUMBER: _ClassVar[int]
    DOUBLE_VALUE_FIELD_NUMBER: _ClassVar[int]
    BOOL_VALUE_FIELD_NUMBER: _ClassVar[int]
    BYTES_VALUE_FIELD_NUMBER: _ClassVar[int]
    ARRAY_VALUE_FIELD_NUMBER: _ClassVar[int]
    MAP_VALUE_FIELD_NUMBER: _ClassVar[int]
    null_value: NullValue
    string_value: str
    int_value: int
    double_value: float
    bool_value: bool
    bytes_value: bytes
    array_value: TypedArray
    map_value: TypedMap
    def __init__(self, null_value: _Optional[_Union[NullValue, str]] = ..., string_value: _Optional[str] = ..., int_value: _Optional[int] = ..., double_value: _Optional[float] = ..., bool_value: bool = ..., bytes_value: _Optional[bytes] = ..., array_value: _Optional[_Union[TypedArray, _Mapping]] = ..., map_value: _Optional[_Union[TypedMap, _Mapping]] = ...) -> None: ...

class TypedArray(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[TypedValue]
    def __init__(self, items: _Optional[_Iterable[_Union[TypedValue, _Mapping]]] = ...) -> None: ...

class TypedMap(_message.Message):
    __slots__ = ("entries",)
    class EntriesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: TypedValue
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[TypedValue, _Mapping]] = ...) -> None: ...
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    entries: _containers.MessageMap[str, TypedValue]
    def __init__(self, entries: _Optional[_Mapping[str, TypedValue]] = ...) -> None: ...

class Metadata(_message.Message):
    __slots__ = ("labels", "annotations")
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class AnnotationsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    LABELS_FIELD_NUMBER: _ClassVar[int]
    ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    labels: _containers.ScalarMap[str, str]
    annotations: _containers.ScalarMap[str, str]
    def __init__(self, labels: _Optional[_Mapping[str, str]] = ..., annotations: _Optional[_Mapping[str, str]] = ...) -> None: ...
