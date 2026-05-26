from google.protobuf import any_pb2 as _any_pb2
from gibson.auth.v1 import options_pb2 as _options_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PluginInvokeRequest(_message.Message):
    __slots__ = ("plugin_name", "method", "request", "deadline_ms")
    PLUGIN_NAME_FIELD_NUMBER: _ClassVar[int]
    METHOD_FIELD_NUMBER: _ClassVar[int]
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    DEADLINE_MS_FIELD_NUMBER: _ClassVar[int]
    plugin_name: str
    method: str
    request: _any_pb2.Any
    deadline_ms: int
    def __init__(self, plugin_name: _Optional[str] = ..., method: _Optional[str] = ..., request: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., deadline_ms: _Optional[int] = ...) -> None: ...

class PluginInvokeResponse(_message.Message):
    __slots__ = ("result", "error")
    RESULT_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    result: _any_pb2.Any
    error: PluginError
    def __init__(self, result: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., error: _Optional[_Union[PluginError, _Mapping]] = ...) -> None: ...

class PluginError(_message.Message):
    __slots__ = ("kind", "message")
    class Kind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PLUGIN_ERROR_KIND_UNSPECIFIED: _ClassVar[PluginError.Kind]
        PLUGIN_ERROR_KIND_UNAVAILABLE: _ClassVar[PluginError.Kind]
        PLUGIN_ERROR_KIND_UNAUTHORIZED: _ClassVar[PluginError.Kind]
        PLUGIN_ERROR_KIND_METHOD_NOT_FOUND: _ClassVar[PluginError.Kind]
        PLUGIN_ERROR_KIND_DEADLINE_EXCEEDED: _ClassVar[PluginError.Kind]
        PLUGIN_ERROR_KIND_HANDLER_FAILED: _ClassVar[PluginError.Kind]
        PLUGIN_ERROR_KIND_INTERNAL: _ClassVar[PluginError.Kind]
    PLUGIN_ERROR_KIND_UNSPECIFIED: PluginError.Kind
    PLUGIN_ERROR_KIND_UNAVAILABLE: PluginError.Kind
    PLUGIN_ERROR_KIND_UNAUTHORIZED: PluginError.Kind
    PLUGIN_ERROR_KIND_METHOD_NOT_FOUND: PluginError.Kind
    PLUGIN_ERROR_KIND_DEADLINE_EXCEEDED: PluginError.Kind
    PLUGIN_ERROR_KIND_HANDLER_FAILED: PluginError.Kind
    PLUGIN_ERROR_KIND_INTERNAL: PluginError.Kind
    KIND_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    kind: PluginError.Kind
    message: str
    def __init__(self, kind: _Optional[_Union[PluginError.Kind, str]] = ..., message: _Optional[str] = ...) -> None: ...
