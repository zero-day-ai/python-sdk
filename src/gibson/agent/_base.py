"""BaseAgent ABC for class-based Gibson agent authoring."""

from __future__ import annotations

from abc import ABC
from typing import Any, ClassVar

from gibson.agent._types import LLMSlotDefinition, Result, TargetSchema, Task


class BaseAgent(ABC):
    """Abstract base class for Gibson agents.

    Subclasses implement ``execute()`` and declare class attributes for
    registration metadata.

    Example::

        class ReconAgent(BaseAgent):
            name = "recon-agent"
            description = "Performs reconnaissance on a target"
            version = "1.0.0"
            capabilities = ["recon", "discovery"]

            async def execute(self, harness: Harness, task: Task) -> Result:
                response = await harness.llm.complete_async([
                    {"role": "user", "content": task.goal}
                ])
                return Result.success(response.content)
    """

    name: ClassVar[str]
    description: ClassVar[str]
    version: ClassVar[str] = "0.1.0"
    capabilities: ClassVar[list[str]] = []
    tags: ClassVar[list[str]] = []

    async def execute(self, harness: Any, task: Task) -> Result:
        """Execute the agent with a Harness and Task.

        The default implementation calls the synchronous ``execute_sync()``
        if defined, allowing agents to choose async or sync style.

        Override this method to implement async agent logic, or override
        ``execute_sync()`` for synchronous logic.
        """
        return self.execute_sync(harness, task)

    def execute_sync(self, harness: Any, task: Task) -> Result:
        raise NotImplementedError(
            f"{self.__class__.__name__} must implement execute() or execute_sync()"
        )

    def initialize(self, config: dict[str, Any]) -> None:  # noqa: B027
        """Called once before the first execution with the agent's configuration."""

    def shutdown(self) -> None:  # noqa: B027
        """Called on graceful shutdown to release resources."""

    def llm_slots(self) -> list[LLMSlotDefinition]:
        """Return LLM slot definitions for slot-based LLM routing."""
        return []

    def target_schemas(self) -> list[TargetSchema]:
        """Return target schemas this agent supports."""
        return []

    def health(self) -> str:
        """Return health status string: healthy, degraded, or unhealthy."""
        return "healthy"
