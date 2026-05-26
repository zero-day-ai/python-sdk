"""Findings namespace for the Gibson Harness."""

from __future__ import annotations

from typing import Any

from gibson.harness.v1 import harness_callback_pb2, harness_callback_pb2_grpc
from gibson.types.v1 import types_pb2


class FindingsNamespace:
    """Harness findings operations — emit structured security findings."""

    def __init__(
        self,
        stub: harness_callback_pb2_grpc.HarnessCallbackServiceStub,
        context: Any,
    ) -> None:
        self._stub = stub
        self._ctx = context

    def emit(self, finding: types_pb2.Finding) -> None:
        """Emit a structured finding to the platform finding store.

        Args:
            finding: A ``types_pb2.Finding`` proto message. Use the types
                from ``gibson.types.v1.types_pb2`` to construct one.
        """
        req = harness_callback_pb2.SubmitFindingRequest(
            context=self._ctx,
            finding=finding,
        )
        self._stub.SubmitFinding(req)

    async def emit_async(self, finding: types_pb2.Finding) -> None:
        """Async emit a structured finding."""
        req = harness_callback_pb2.SubmitFindingRequest(
            context=self._ctx,
            finding=finding,
        )
        await self._stub.SubmitFinding(req)
