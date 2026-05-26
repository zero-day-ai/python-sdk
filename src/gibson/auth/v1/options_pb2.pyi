from google.protobuf import descriptor_pb2 as _descriptor_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class IdentityClass(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    IDENTITY_CLASS_UNSPECIFIED: _ClassVar[IdentityClass]
    IDENTITY_CLASS_USER: _ClassVar[IdentityClass]
    IDENTITY_CLASS_SERVICE: _ClassVar[IdentityClass]
    IDENTITY_CLASS_COMPONENT: _ClassVar[IdentityClass]
    IDENTITY_CLASS_PLATFORM_OPERATOR: _ClassVar[IdentityClass]
IDENTITY_CLASS_UNSPECIFIED: IdentityClass
IDENTITY_CLASS_USER: IdentityClass
IDENTITY_CLASS_SERVICE: IdentityClass
IDENTITY_CLASS_COMPONENT: IdentityClass
IDENTITY_CLASS_PLATFORM_OPERATOR: IdentityClass
AUTHZ_FIELD_NUMBER: _ClassVar[int]
authz: _descriptor.FieldDescriptor

class AuthOptions(_message.Message):
    __slots__ = ("relation", "object_type", "object_deriver", "allowed_identities", "unauthenticated", "self")
    RELATION_FIELD_NUMBER: _ClassVar[int]
    OBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_DERIVER_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_IDENTITIES_FIELD_NUMBER: _ClassVar[int]
    UNAUTHENTICATED_FIELD_NUMBER: _ClassVar[int]
    SELF_FIELD_NUMBER: _ClassVar[int]
    relation: str
    object_type: str
    object_deriver: str
    allowed_identities: int
    unauthenticated: bool
    self: bool
    def __init__(self_, relation: _Optional[str] = ..., object_type: _Optional[str] = ..., object_deriver: _Optional[str] = ..., allowed_identities: _Optional[int] = ..., unauthenticated: bool = ..., self: bool = ...) -> None: ...
