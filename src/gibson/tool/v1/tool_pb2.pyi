from gibson.common.v1 import gibson_common_pb2 as _gibson_common_pb2
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

class GetDescriptorResponse(_message.Message):
    __slots__ = ("name", "description", "version", "tags", "input_schema", "output_schema")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    INPUT_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    version: str
    tags: _containers.RepeatedScalarFieldContainer[str]
    input_schema: _gibson_common_pb2.JSONSchema
    output_schema: _gibson_common_pb2.JSONSchema
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., version: _Optional[str] = ..., tags: _Optional[_Iterable[str]] = ..., input_schema: _Optional[_Union[_gibson_common_pb2.JSONSchema, _Mapping]] = ..., output_schema: _Optional[_Union[_gibson_common_pb2.JSONSchema, _Mapping]] = ...) -> None: ...

class ExecuteRequest(_message.Message):
    __slots__ = ("input_json", "timeout_ms")
    INPUT_JSON_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_MS_FIELD_NUMBER: _ClassVar[int]
    input_json: str
    timeout_ms: int
    def __init__(self, input_json: _Optional[str] = ..., timeout_ms: _Optional[int] = ...) -> None: ...

class ExecuteResponse(_message.Message):
    __slots__ = ("output_json", "error")
    OUTPUT_JSON_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    output_json: str
    error: _gibson_common_pb2.Error
    def __init__(self, output_json: _Optional[str] = ..., error: _Optional[_Union[_gibson_common_pb2.Error, _Mapping]] = ...) -> None: ...

class HealthRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class HealthResponse(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: _gibson_common_pb2.HealthStatus
    def __init__(self, status: _Optional[_Union[_gibson_common_pb2.HealthStatus, _Mapping]] = ...) -> None: ...

class StreamExecuteRequest(_message.Message):
    __slots__ = ("start", "cancel")
    START_FIELD_NUMBER: _ClassVar[int]
    CANCEL_FIELD_NUMBER: _ClassVar[int]
    start: ToolStartRequest
    cancel: ToolCancelRequest
    def __init__(self, start: _Optional[_Union[ToolStartRequest, _Mapping]] = ..., cancel: _Optional[_Union[ToolCancelRequest, _Mapping]] = ...) -> None: ...

class ToolStartRequest(_message.Message):
    __slots__ = ("input_json", "timeout_ms", "trace_id", "parent_span_id")
    INPUT_JSON_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_MS_FIELD_NUMBER: _ClassVar[int]
    TRACE_ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_SPAN_ID_FIELD_NUMBER: _ClassVar[int]
    input_json: str
    timeout_ms: int
    trace_id: str
    parent_span_id: str
    def __init__(self, input_json: _Optional[str] = ..., timeout_ms: _Optional[int] = ..., trace_id: _Optional[str] = ..., parent_span_id: _Optional[str] = ...) -> None: ...

class ToolCancelRequest(_message.Message):
    __slots__ = ("reason",)
    REASON_FIELD_NUMBER: _ClassVar[int]
    reason: str
    def __init__(self, reason: _Optional[str] = ...) -> None: ...

class StreamExecuteResponse(_message.Message):
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
    progress: ToolProgress
    partial: ToolPartialResult
    warning: ToolWarning
    complete: ToolComplete
    error: ToolError
    trace_id: str
    span_id: str
    sequence: int
    timestamp_ms: int
    def __init__(self, progress: _Optional[_Union[ToolProgress, _Mapping]] = ..., partial: _Optional[_Union[ToolPartialResult, _Mapping]] = ..., warning: _Optional[_Union[ToolWarning, _Mapping]] = ..., complete: _Optional[_Union[ToolComplete, _Mapping]] = ..., error: _Optional[_Union[ToolError, _Mapping]] = ..., trace_id: _Optional[str] = ..., span_id: _Optional[str] = ..., sequence: _Optional[int] = ..., timestamp_ms: _Optional[int] = ...) -> None: ...

class ToolProgress(_message.Message):
    __slots__ = ("percent", "stage", "message")
    PERCENT_FIELD_NUMBER: _ClassVar[int]
    STAGE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    percent: int
    stage: str
    message: str
    def __init__(self, percent: _Optional[int] = ..., stage: _Optional[str] = ..., message: _Optional[str] = ...) -> None: ...

class ToolPartialResult(_message.Message):
    __slots__ = ("output_json", "description")
    OUTPUT_JSON_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    output_json: str
    description: str
    def __init__(self, output_json: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...

class ToolWarning(_message.Message):
    __slots__ = ("message", "code")
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    message: str
    code: str
    def __init__(self, message: _Optional[str] = ..., code: _Optional[str] = ...) -> None: ...

class ToolComplete(_message.Message):
    __slots__ = ("output_json",)
    OUTPUT_JSON_FIELD_NUMBER: _ClassVar[int]
    output_json: str
    def __init__(self, output_json: _Optional[str] = ...) -> None: ...

class ToolError(_message.Message):
    __slots__ = ("error", "fatal")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    FATAL_FIELD_NUMBER: _ClassVar[int]
    error: _gibson_common_pb2.Error
    fatal: bool
    def __init__(self, error: _Optional[_Union[_gibson_common_pb2.Error, _Mapping]] = ..., fatal: bool = ...) -> None: ...
