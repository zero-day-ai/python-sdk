"""GibsonTool and GibsonToolRegistry — wrap Gibson tools as LangChain tools."""

from __future__ import annotations

import json
from typing import Any

try:
    from langchain_core.tools import BaseTool as LCBaseTool
    from langchain_core.tools import ToolException
except ImportError as exc:  # pragma: no cover
    raise ImportError(
        "langchain-core is required for gibson.langchain. "
        "Install it with: pip install gibson-sdk[langchain]"
    ) from exc
from pydantic import ConfigDict

from gibson.harness import Harness


class GibsonTool(LCBaseTool):
    """A LangChain tool that delegates execution to a Gibson tool via Harness."""

    model_config = ConfigDict(arbitrary_types_allowed=True)

    name: str
    description: str
    harness: Any  # Harness — not annotated as Harness to avoid pydantic field issues
    tool_name: str

    def _run(self, *args: Any, **kwargs: Any) -> str:
        """Execute the Gibson tool synchronously."""
        input_dict = kwargs if kwargs else (args[0] if args else {})
        if isinstance(input_dict, str):
            try:
                input_dict = json.loads(input_dict)
            except json.JSONDecodeError:
                input_dict = {"input": input_dict}

        try:
            result = self.harness.tools.call(self.tool_name, input_dict)
            return json.dumps(result)
        except Exception as exc:
            raise ToolException(str(exc)) from exc

    async def _arun(self, *args: Any, **kwargs: Any) -> str:
        """Execute the Gibson tool asynchronously."""
        input_dict = kwargs if kwargs else (args[0] if args else {})
        if isinstance(input_dict, str):
            try:
                input_dict = json.loads(input_dict)
            except json.JSONDecodeError:
                input_dict = {"input": input_dict}

        try:
            result = await self.harness.tools.call_async(self.tool_name, input_dict)
            return json.dumps(result)
        except Exception as exc:
            raise ToolException(str(exc)) from exc


class GibsonToolRegistry:
    """Build a list of GibsonTool instances from the tools available via Harness."""

    def __init__(self, harness: Harness) -> None:
        self._harness = harness

    def list(self) -> list[GibsonTool]:
        """Return a GibsonTool for every tool registered with the harness."""
        descriptors = self._harness.tools.list()
        return [
            GibsonTool(
                name=d.name,
                description=d.description or d.name,
                harness=self._harness,
                tool_name=d.name,
            )
            for d in descriptors
        ]
