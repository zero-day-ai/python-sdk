from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RecipientClass(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RECIPIENT_CLASS_UNSPECIFIED: _ClassVar[RecipientClass]
    RECIPIENT_CLASS_AGENT: _ClassVar[RecipientClass]
    RECIPIENT_CLASS_TOOL: _ClassVar[RecipientClass]
    RECIPIENT_CLASS_PLUGIN: _ClassVar[RecipientClass]
RECIPIENT_CLASS_UNSPECIFIED: RecipientClass
RECIPIENT_CLASS_AGENT: RecipientClass
RECIPIENT_CLASS_TOOL: RecipientClass
RECIPIENT_CLASS_PLUGIN: RecipientClass

class CapabilityGrantInfo(_message.Message):
    __slots__ = ("jti", "recipient_install_id", "recipient_class", "recipient_name", "allowed_rpcs", "mission_id", "task_id", "issued_at_unix", "expires_at_unix", "near_expiry")
    JTI_FIELD_NUMBER: _ClassVar[int]
    RECIPIENT_INSTALL_ID_FIELD_NUMBER: _ClassVar[int]
    RECIPIENT_CLASS_FIELD_NUMBER: _ClassVar[int]
    RECIPIENT_NAME_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_RPCS_FIELD_NUMBER: _ClassVar[int]
    MISSION_ID_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    ISSUED_AT_UNIX_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_UNIX_FIELD_NUMBER: _ClassVar[int]
    NEAR_EXPIRY_FIELD_NUMBER: _ClassVar[int]
    jti: str
    recipient_install_id: str
    recipient_class: RecipientClass
    recipient_name: str
    allowed_rpcs: _containers.RepeatedScalarFieldContainer[str]
    mission_id: str
    task_id: str
    issued_at_unix: int
    expires_at_unix: int
    near_expiry: bool
    def __init__(self, jti: _Optional[str] = ..., recipient_install_id: _Optional[str] = ..., recipient_class: _Optional[_Union[RecipientClass, str]] = ..., recipient_name: _Optional[str] = ..., allowed_rpcs: _Optional[_Iterable[str]] = ..., mission_id: _Optional[str] = ..., task_id: _Optional[str] = ..., issued_at_unix: _Optional[int] = ..., expires_at_unix: _Optional[int] = ..., near_expiry: bool = ...) -> None: ...
