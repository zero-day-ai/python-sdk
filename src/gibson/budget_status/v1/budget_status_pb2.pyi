from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BudgetScope(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BUDGET_SCOPE_UNSPECIFIED: _ClassVar[BudgetScope]
    BUDGET_SCOPE_USER: _ClassVar[BudgetScope]
    BUDGET_SCOPE_TEAM: _ClassVar[BudgetScope]
    BUDGET_SCOPE_TENANT: _ClassVar[BudgetScope]
BUDGET_SCOPE_UNSPECIFIED: BudgetScope
BUDGET_SCOPE_USER: BudgetScope
BUDGET_SCOPE_TEAM: BudgetScope
BUDGET_SCOPE_TENANT: BudgetScope

class BudgetExceeded(_message.Message):
    __slots__ = ("scope", "dimension", "current_usage", "limit", "period_reset_at_unix", "subject_id")
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    DIMENSION_FIELD_NUMBER: _ClassVar[int]
    CURRENT_USAGE_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    PERIOD_RESET_AT_UNIX_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    scope: BudgetScope
    dimension: str
    current_usage: int
    limit: int
    period_reset_at_unix: int
    subject_id: str
    def __init__(self, scope: _Optional[_Union[BudgetScope, str]] = ..., dimension: _Optional[str] = ..., current_usage: _Optional[int] = ..., limit: _Optional[int] = ..., period_reset_at_unix: _Optional[int] = ..., subject_id: _Optional[str] = ...) -> None: ...
