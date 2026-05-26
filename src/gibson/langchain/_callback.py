"""GibsonCallbackHandler — emit LangChain events to Gibson findings/memory."""

from __future__ import annotations

from typing import Any
from uuid import UUID

try:
    from langchain_core.callbacks.base import BaseCallbackHandler
    from langchain_core.outputs import LLMResult
except ImportError as exc:  # pragma: no cover
    raise ImportError(
        "langchain-core is required for gibson.langchain. "
        "Install it with: pip install gibson-sdk[langchain]"
    ) from exc

from gibson.harness import Harness


class GibsonCallbackHandler(BaseCallbackHandler):
    """LangChain callback handler that records LLM calls to Gibson memory."""

    def __init__(self, harness: Harness) -> None:
        super().__init__()
        self._harness = harness
        self.llm_call_count: int = 0
        self.token_count: int = 0

    def on_llm_start(
        self,
        serialized: dict[str, Any],
        prompts: list[str],
        *,
        run_id: UUID,
        parent_run_id: UUID | None = None,
        **kwargs: Any,
    ) -> None:
        self.llm_call_count += 1
        self._harness.memory.set(
            f"_lc_llm_call_{self.llm_call_count}",
            {"prompts": prompts, "run_id": str(run_id)},
        )

    def on_llm_end(
        self,
        response: LLMResult,
        *,
        run_id: UUID,
        parent_run_id: UUID | None = None,
        **kwargs: Any,
    ) -> None:
        for generations in response.generations:
            for gen in generations:
                text = getattr(gen, "text", "")
                self.token_count += len(text.split())

    def on_llm_error(
        self,
        error: BaseException,
        *,
        run_id: UUID,
        parent_run_id: UUID | None = None,
        **kwargs: Any,
    ) -> None:
        self._harness.memory.set(
            f"_lc_llm_error_{self.llm_call_count}",
            {"error": str(error), "run_id": str(run_id)},
        )

    def on_chain_start(
        self,
        serialized: dict[str, Any],
        inputs: dict[str, Any],
        *,
        run_id: UUID,
        parent_run_id: UUID | None = None,
        **kwargs: Any,
    ) -> None:
        pass

    def on_chain_end(
        self,
        outputs: dict[str, Any],
        *,
        run_id: UUID,
        parent_run_id: UUID | None = None,
        **kwargs: Any,
    ) -> None:
        pass

    def on_tool_start(
        self,
        serialized: dict[str, Any],
        input_str: str,
        *,
        run_id: UUID,
        parent_run_id: UUID | None = None,
        **kwargs: Any,
    ) -> None:
        pass

    def on_tool_end(
        self,
        output: Any,
        *,
        run_id: UUID,
        parent_run_id: UUID | None = None,
        **kwargs: Any,
    ) -> None:
        pass
