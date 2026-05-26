"""Planning namespace for the Gibson Harness."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from gibson.harness.v1 import harness_callback_pb2, harness_callback_pb2_grpc


@dataclass
class PlanContext:
    """Current plan context for the executing agent."""

    current_step_index: int = 0
    total_steps: int = 0
    plan_id: str = ""


class PlanningNamespace:
    """Harness planning operations — read plan context for multi-step agents."""

    def __init__(
        self,
        stub: harness_callback_pb2_grpc.HarnessCallbackServiceStub,
        context: Any,
    ) -> None:
        self._stub = stub
        self._ctx = context

    def get_context(self) -> PlanContext:
        """Retrieve the current plan context."""
        req = harness_callback_pb2.GetPlanContextRequest(context=self._ctx)
        resp = self._stub.GetPlanContext(req)
        pc = resp.plan_context
        return PlanContext(
            current_step_index=pc.current_step_index,
            total_steps=pc.total_steps if hasattr(pc, "total_steps") else 0,
        )

    async def get_context_async(self) -> PlanContext:
        """Async retrieve the current plan context."""
        req = harness_callback_pb2.GetPlanContextRequest(context=self._ctx)
        resp = await self._stub.GetPlanContext(req)
        pc = resp.plan_context
        return PlanContext(
            current_step_index=pc.current_step_index,
            total_steps=pc.total_steps if hasattr(pc, "total_steps") else 0,
        )
