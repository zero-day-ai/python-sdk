"""LLM namespace for the Gibson Harness."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from gibson.harness.v1 import harness_callback_pb2, harness_callback_pb2_grpc


@dataclass
class LLMResponse:
    """Response from an LLM completion call."""

    content: str
    tool_calls: list[dict[str, str]] = field(default_factory=list)
    finish_reason: str = ""
    input_tokens: int = 0
    output_tokens: int = 0


@dataclass
class LLMMessage:
    """A single LLM conversation message."""

    role: str
    content: str


def _to_proto_messages(
    messages: list[LLMMessage | dict[str, str]],
) -> list[harness_callback_pb2.LLMMessage]:
    result = []
    for msg in messages:
        if isinstance(msg, dict):
            result.append(harness_callback_pb2.LLMMessage(role=msg["role"], content=msg.get("content", "")))
        else:
            result.append(harness_callback_pb2.LLMMessage(role=msg.role, content=msg.content))
    return result


def _parse_response(resp: harness_callback_pb2.LLMCompleteResponse) -> LLMResponse:
    tool_calls = [
        {"id": tc.id, "name": tc.name, "arguments": tc.arguments}
        for tc in resp.tool_calls
    ]
    return LLMResponse(
        content=resp.content,
        tool_calls=tool_calls,
        finish_reason=resp.finish_reason,
        input_tokens=resp.usage.input_tokens,
        output_tokens=resp.usage.output_tokens,
    )


class LLMNamespace:
    """Harness LLM operations — route completions through the daemon's budget/observability pipeline."""

    def __init__(
        self,
        stub: harness_callback_pb2_grpc.HarnessCallbackServiceStub,
        context: Any,
    ) -> None:
        self._stub = stub
        self._ctx = context

    def complete(
        self,
        messages: list[LLMMessage | dict[str, str]],
        slot: str = "default",
        temperature: float = 0.0,
        max_tokens: int = 0,
    ) -> LLMResponse:
        """Blocking LLM completion."""
        req = harness_callback_pb2.LLMCompleteRequest(
            context=self._ctx,
            slot=slot,
            messages=_to_proto_messages(messages),
            temperature=temperature,
            max_tokens=max_tokens,
        )
        resp = self._stub.LLMComplete(req)
        return _parse_response(resp)

    async def complete_async(
        self,
        messages: list[LLMMessage | dict[str, str]],
        slot: str = "default",
        temperature: float = 0.0,
        max_tokens: int = 0,
    ) -> LLMResponse:
        """Async LLM completion using grpc.aio."""

        req = harness_callback_pb2.LLMCompleteRequest(
            context=self._ctx,
            slot=slot,
            messages=_to_proto_messages(messages),
            temperature=temperature,
            max_tokens=max_tokens,
        )
        resp = await self._stub.LLMComplete(req)
        return _parse_response(resp)

    def complete_with_tools(
        self,
        messages: list[LLMMessage | dict[str, str]],
        tools: list[dict[str, Any]],
        slot: str = "default",
    ) -> LLMResponse:
        """LLM completion with tool definitions for function-calling."""
        tool_defs = [
            harness_callback_pb2.ToolDef(name=t["name"], description=t.get("description", ""))
            for t in tools
        ]
        req = harness_callback_pb2.LLMCompleteWithToolsRequest(
            context=self._ctx,
            slot=slot,
            messages=_to_proto_messages(messages),
            tools=tool_defs,
        )
        resp = self._stub.LLMCompleteWithTools(req)
        return _parse_response(resp)

    def stream(
        self,
        messages: list[LLMMessage | dict[str, str]],
        slot: str = "default",
    ):
        """Streaming LLM completion — yields text chunks as strings."""
        req = harness_callback_pb2.LLMStreamRequest(
            context=self._ctx,
            slot=slot,
            messages=_to_proto_messages(messages),
        )
        for chunk in self._stub.LLMStream(req):
            if chunk.content:
                yield chunk.content
