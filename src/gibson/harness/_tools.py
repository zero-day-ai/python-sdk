"""Tools namespace for the Gibson Harness."""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from typing import Any

from gibson.harness.v1 import harness_callback_pb2, harness_callback_pb2_grpc


@dataclass
class ToolDescriptor:
    """Descriptor for a tool registered with the daemon."""

    name: str
    description: str
    version: str
    tags: list[str] = field(default_factory=list)
    input_schema: dict[str, Any] = field(default_factory=dict)
    output_schema: dict[str, Any] = field(default_factory=dict)


class ToolsNamespace:
    """Harness tool invocation — call tools registered with the daemon."""

    def __init__(
        self,
        stub: harness_callback_pb2_grpc.HarnessCallbackServiceStub,
        context: Any,
    ) -> None:
        self._stub = stub
        self._ctx = context

    def call(self, name: str, input: dict[str, Any]) -> dict[str, Any]:
        """Call a tool by name with a dict input, returns a dict output."""
        req = harness_callback_pb2.CallToolProtoRequest(
            context=self._ctx,
            name=name,
            input_json=json.dumps(input).encode(),
        )
        resp = self._stub.CallToolProto(req)
        if resp.error and resp.error.message:
            raise RuntimeError(f"tool {name!r} error: {resp.error.message}")
        return json.loads(resp.output_json) if resp.output_json else {}

    async def call_async(self, name: str, input: dict[str, Any]) -> dict[str, Any]:
        """Async call a tool by name."""
        req = harness_callback_pb2.CallToolProtoRequest(
            context=self._ctx,
            name=name,
            input_json=json.dumps(input).encode(),
        )
        resp = await self._stub.CallToolProto(req)
        if resp.error and resp.error.message:
            raise RuntimeError(f"tool {name!r} error: {resp.error.message}")
        return json.loads(resp.output_json) if resp.output_json else {}

    def list(self) -> list[ToolDescriptor]:
        """List all tools registered with the daemon."""
        req = harness_callback_pb2.ListToolsRequest(context=self._ctx)
        resp = self._stub.ListTools(req)
        result = []
        for t in resp.tools:
            result.append(
                ToolDescriptor(
                    name=t.name,
                    description=t.description,
                    version=t.version,
                )
            )
        return result
