from gibson.auth.v1 import options_pb2 as _options_pb2
from gibson.capability.v1 import capability_pb2 as _capability_pb2
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
PRINCIPAL_KIND_UNSPECIFIED: PrincipalKind
PRINCIPAL_KIND_AGENT: PrincipalKind
PRINCIPAL_KIND_TOOL: PrincipalKind
PRINCIPAL_KIND_PLUGIN: PrincipalKind

class WhoAmIRequest(_message.Message):
    __slots__ = ("target_principal_id",)
    TARGET_PRINCIPAL_ID_FIELD_NUMBER: _ClassVar[int]
    target_principal_id: str
    def __init__(self, target_principal_id: _Optional[str] = ...) -> None: ...

class WhoAmIResponse(_message.Message):
    __slots__ = ("principal_id", "kind", "name", "tenant_id", "component_grants", "plugin_grants", "active_capability_grants", "truncated")
    PRINCIPAL_ID_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    COMPONENT_GRANTS_FIELD_NUMBER: _ClassVar[int]
    PLUGIN_GRANTS_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_CAPABILITY_GRANTS_FIELD_NUMBER: _ClassVar[int]
    TRUNCATED_FIELD_NUMBER: _ClassVar[int]
    principal_id: str
    kind: PrincipalKind
    name: str
    tenant_id: str
    component_grants: _containers.RepeatedCompositeFieldContainer[ComponentGrantEffective]
    plugin_grants: _containers.RepeatedCompositeFieldContainer[PluginGrantEffective]
    active_capability_grants: _containers.RepeatedCompositeFieldContainer[_capability_pb2.CapabilityGrantInfo]
    truncated: bool
    def __init__(self, principal_id: _Optional[str] = ..., kind: _Optional[_Union[PrincipalKind, str]] = ..., name: _Optional[str] = ..., tenant_id: _Optional[str] = ..., component_grants: _Optional[_Iterable[_Union[ComponentGrantEffective, _Mapping]]] = ..., plugin_grants: _Optional[_Iterable[_Union[PluginGrantEffective, _Mapping]]] = ..., active_capability_grants: _Optional[_Iterable[_Union[_capability_pb2.CapabilityGrantInfo, _Mapping]]] = ..., truncated: bool = ...) -> None: ...

class ComponentGrantEffective(_message.Message):
    __slots__ = ("component_ref", "can_read", "can_configure", "can_execute", "sources")
    COMPONENT_REF_FIELD_NUMBER: _ClassVar[int]
    CAN_READ_FIELD_NUMBER: _ClassVar[int]
    CAN_CONFIGURE_FIELD_NUMBER: _ClassVar[int]
    CAN_EXECUTE_FIELD_NUMBER: _ClassVar[int]
    SOURCES_FIELD_NUMBER: _ClassVar[int]
    component_ref: str
    can_read: bool
    can_configure: bool
    can_execute: bool
    sources: _containers.RepeatedCompositeFieldContainer[GrantSource]
    def __init__(self, component_ref: _Optional[str] = ..., can_read: bool = ..., can_configure: bool = ..., can_execute: bool = ..., sources: _Optional[_Iterable[_Union[GrantSource, _Mapping]]] = ...) -> None: ...

class PluginGrantEffective(_message.Message):
    __slots__ = ("plugin_ref", "sources")
    PLUGIN_REF_FIELD_NUMBER: _ClassVar[int]
    SOURCES_FIELD_NUMBER: _ClassVar[int]
    plugin_ref: str
    sources: _containers.RepeatedCompositeFieldContainer[GrantSource]
    def __init__(self, plugin_ref: _Optional[str] = ..., sources: _Optional[_Iterable[_Union[GrantSource, _Mapping]]] = ...) -> None: ...

class GrantSource(_message.Message):
    __slots__ = ("kind", "source_object")
    class Kind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        KIND_UNSPECIFIED: _ClassVar[GrantSource.Kind]
        KIND_DIRECT: _ClassVar[GrantSource.Kind]
        KIND_TENANT_MEMBER: _ClassVar[GrantSource.Kind]
        KIND_TEAM_MEMBER: _ClassVar[GrantSource.Kind]
        KIND_OWNER: _ClassVar[GrantSource.Kind]
    KIND_UNSPECIFIED: GrantSource.Kind
    KIND_DIRECT: GrantSource.Kind
    KIND_TENANT_MEMBER: GrantSource.Kind
    KIND_TEAM_MEMBER: GrantSource.Kind
    KIND_OWNER: GrantSource.Kind
    KIND_FIELD_NUMBER: _ClassVar[int]
    SOURCE_OBJECT_FIELD_NUMBER: _ClassVar[int]
    kind: GrantSource.Kind
    source_object: str
    def __init__(self, kind: _Optional[_Union[GrantSource.Kind, str]] = ..., source_object: _Optional[str] = ...) -> None: ...
