"""Gibson harness module — connect to HarnessCallbackService from inside an agent."""

from gibson.harness._client import Harness
from gibson.harness._findings import FindingsNamespace
from gibson.harness._graphrag import GraphRAGResult
from gibson.harness._llm import LLMMessage, LLMResponse
from gibson.harness._memory import MemoryNamespace
from gibson.harness._tools import ToolDescriptor

__all__ = [
    "FindingsNamespace",
    "GraphRAGResult",
    "Harness",
    "LLMMessage",
    "LLMResponse",
    "MemoryNamespace",
    "ToolDescriptor",
]
