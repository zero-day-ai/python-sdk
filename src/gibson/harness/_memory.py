"""Memory namespace for the Gibson Harness."""

from __future__ import annotations

from typing import Any

from gibson.agent._types import _python_to_typed_value, _typed_value_to_python
from gibson.harness.v1 import harness_callback_pb2, harness_callback_pb2_grpc

_TIER_MAP = {
    "working": harness_callback_pb2.MEMORY_TIER_WORKING,
    "mission": harness_callback_pb2.MEMORY_TIER_MISSION,
    "long_term": harness_callback_pb2.MEMORY_TIER_LONG_TERM,
}


class MemoryNamespace:
    """Harness memory operations — mission-scoped key/value store."""

    def __init__(
        self,
        stub: harness_callback_pb2_grpc.HarnessCallbackServiceStub,
        context: Any,
    ) -> None:
        self._stub = stub
        self._ctx = context

    def get(self, key: str, tier: str = "working") -> Any | None:
        """Retrieve a value by key. Returns None if the key is not set."""
        req = harness_callback_pb2.MemoryGetRequest(
            context=self._ctx,
            key=key,
            tier=_TIER_MAP.get(tier, harness_callback_pb2.MEMORY_TIER_WORKING),
        )
        resp = self._stub.MemoryGet(req)
        if not resp.found:
            return None
        return _typed_value_to_python(resp.value)

    def set(self, key: str, value: Any, tier: str = "working") -> None:
        """Store a value by key."""
        req = harness_callback_pb2.MemorySetRequest(
            context=self._ctx,
            key=key,
            value=_python_to_typed_value(value),
            tier=_TIER_MAP.get(tier, harness_callback_pb2.MEMORY_TIER_WORKING),
        )
        self._stub.MemorySet(req)

    async def get_async(self, key: str, tier: str = "working") -> Any | None:
        """Async retrieve a value by key."""
        req = harness_callback_pb2.MemoryGetRequest(
            context=self._ctx,
            key=key,
            tier=_TIER_MAP.get(tier, harness_callback_pb2.MEMORY_TIER_WORKING),
        )
        resp = await self._stub.MemoryGet(req)
        if not resp.found:
            return None
        return _typed_value_to_python(resp.value)

    async def set_async(self, key: str, value: Any, tier: str = "working") -> None:
        """Async store a value by key."""
        req = harness_callback_pb2.MemorySetRequest(
            context=self._ctx,
            key=key,
            value=_python_to_typed_value(value),
            tier=_TIER_MAP.get(tier, harness_callback_pb2.MEMORY_TIER_WORKING),
        )
        await self._stub.MemorySet(req)
