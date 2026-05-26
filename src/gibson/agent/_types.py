"""Python types for agent Task and Result, mirroring the Go SDK wire types."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from gibson.common.v1 import gibson_common_pb2
from gibson.types.v1 import types_pb2


@dataclass
class Task:
    """Goal-oriented task passed to an agent's execute() method."""

    id: str
    goal: str
    context: dict[str, Any] = field(default_factory=dict)
    metadata: dict[str, Any] = field(default_factory=dict)

    @classmethod
    def from_proto(cls, proto: types_pb2.Task) -> Task:
        return cls(
            id=proto.id,
            goal=proto.goal,
            context=_typed_map_to_dict(proto.context),
            metadata=_typed_map_to_dict(proto.metadata),
        )


@dataclass
class Result:
    """Outcome of an agent's execute() method."""

    status: str = "success"
    output: Any = None
    finding_ids: list[str] = field(default_factory=list)
    error: str | None = None
    error_code: str | None = None

    @classmethod
    def success(cls, output: Any = None) -> Result:
        return cls(status="success", output=output)

    @classmethod
    def failure(cls, error: str, code: str = "INTERNAL") -> Result:
        return cls(status="failed", error=error, error_code=code)

    def to_proto(self) -> types_pb2.Result:
        status_map = {
            "success": types_pb2.RESULT_STATUS_SUCCESS,
            "failed": types_pb2.RESULT_STATUS_FAILED,
            "partial": types_pb2.RESULT_STATUS_PARTIAL,
            "cancelled": types_pb2.RESULT_STATUS_CANCELLED,
            "timeout": types_pb2.RESULT_STATUS_TIMEOUT,
        }
        status = status_map.get(self.status, types_pb2.RESULT_STATUS_UNSPECIFIED)

        result = types_pb2.Result(
            status=status,
            finding_ids=self.finding_ids,
        )

        if self.output is not None:
            result.output.CopyFrom(_python_to_typed_value(self.output))

        if self.error:
            from gibson.common.v1 import gibson_common_pb2  # noqa: PLC0415

            code_map = {
                "INTERNAL": gibson_common_pb2.ERROR_CODE_INTERNAL,
                "INVALID_ARGUMENT": gibson_common_pb2.ERROR_CODE_INVALID_ARGUMENT,
                "TIMEOUT": gibson_common_pb2.ERROR_CODE_TIMEOUT,
                "AGENT_TIMEOUT": gibson_common_pb2.ERROR_CODE_AGENT_TIMEOUT,
            }
            result.error.CopyFrom(
                types_pb2.ResultError(
                    code=code_map.get(self.error_code or "INTERNAL", gibson_common_pb2.ERROR_CODE_INTERNAL),
                    message=self.error,
                )
            )

        return result


@dataclass
class LLMSlotDefinition:
    """LLM slot definition for an agent."""

    name: str
    description: str = ""
    required: bool = False
    provider: str = ""
    model: str = ""


@dataclass
class TargetSchema:
    """Target schema supported by an agent."""

    type: str
    version: str = ""
    schema_json: str = ""
    description: str = ""


# ---------------------------------------------------------------------------
# TypedValue / TypedMap helpers
# ---------------------------------------------------------------------------


def _typed_value_to_python(tv: gibson_common_pb2.TypedValue) -> Any:
    kind = tv.WhichOneof("kind")
    if kind == "null_value":
        return None
    if kind == "string_value":
        return tv.string_value
    if kind == "int_value":
        return tv.int_value
    if kind == "double_value":
        return tv.double_value
    if kind == "bool_value":
        return tv.bool_value
    if kind == "bytes_value":
        return tv.bytes_value
    if kind == "array_value":
        return [_typed_value_to_python(item) for item in tv.array_value.items]
    if kind == "map_value":
        return {k: _typed_value_to_python(v) for k, v in tv.map_value.entries.items()}
    return None


def _typed_map_to_dict(typed_map: Any) -> dict[str, Any]:
    return {k: _typed_value_to_python(v) for k, v in typed_map.items()}


def _python_to_typed_value(value: Any) -> gibson_common_pb2.TypedValue:
    tv = gibson_common_pb2.TypedValue()
    if value is None:
        tv.null_value = gibson_common_pb2.NULL_VALUE_UNSPECIFIED
    elif isinstance(value, bool):
        tv.bool_value = value
    elif isinstance(value, int):
        tv.int_value = value
    elif isinstance(value, float):
        tv.double_value = value
    elif isinstance(value, str):
        tv.string_value = value
    elif isinstance(value, bytes):
        tv.bytes_value = value
    elif isinstance(value, list):
        tv.array_value.items.extend([_python_to_typed_value(item) for item in value])
    elif isinstance(value, dict):
        for k, v in value.items():
            tv.map_value.entries[k].CopyFrom(_python_to_typed_value(v))
    else:
        tv.string_value = str(value)
    return tv
