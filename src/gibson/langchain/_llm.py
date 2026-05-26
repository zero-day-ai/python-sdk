"""GibsonLLM — LangChain BaseChatModel backed by Harness.llm."""

from __future__ import annotations

from typing import Any

try:
    from langchain_core.language_models.chat_models import BaseChatModel
    from langchain_core.messages import AIMessage, BaseMessage, HumanMessage, SystemMessage
    from langchain_core.outputs import ChatGeneration, ChatResult
except ImportError as exc:  # pragma: no cover
    raise ImportError(
        "langchain-core is required for gibson.langchain. "
        "Install it with: pip install gibson-sdk[langchain]"
    ) from exc
from pydantic import ConfigDict


def _to_harness_messages(messages: list[BaseMessage]) -> list[dict[str, str]]:
    result = []
    for msg in messages:
        if isinstance(msg, HumanMessage):
            role = "user"
        elif isinstance(msg, AIMessage):
            role = "assistant"
        elif isinstance(msg, SystemMessage):
            role = "system"
        else:
            role = "user"
        content = msg.content if isinstance(msg.content, str) else str(msg.content)
        result.append({"role": role, "content": content})
    return result


class GibsonLLM(BaseChatModel):
    """LangChain chat model that routes completions through Gibson's Harness LLM."""

    model_config = ConfigDict(arbitrary_types_allowed=True)

    harness: Any  # Harness — arbitrary_types_allowed

    @property
    def _llm_type(self) -> str:
        return "gibson"

    def _generate(
        self,
        messages: list[BaseMessage],
        stop: list[str] | None = None,
        run_manager: Any = None,
        **kwargs: Any,
    ) -> ChatResult:
        harness_msgs = _to_harness_messages(messages)
        resp = self.harness.llm.complete(harness_msgs)
        message = AIMessage(content=resp.content)
        generation = ChatGeneration(message=message)
        return ChatResult(generations=[generation])

    async def _agenerate(
        self,
        messages: list[BaseMessage],
        stop: list[str] | None = None,
        run_manager: Any = None,
        **kwargs: Any,
    ) -> ChatResult:
        harness_msgs = _to_harness_messages(messages)
        resp = await self.harness.llm.complete_async(harness_msgs)
        message = AIMessage(content=resp.content)
        generation = ChatGeneration(message=message)
        return ChatResult(generations=[generation])
