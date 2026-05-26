"""Harness client — connects to HarnessCallbackService and exposes sub-namespaces."""

from __future__ import annotations

import grpc

from gibson.harness._findings import FindingsNamespace
from gibson.harness._graphrag import GraphRAGNamespace
from gibson.harness._llm import LLMNamespace
from gibson.harness._memory import MemoryNamespace
from gibson.harness._planning import PlanningNamespace
from gibson.harness._tools import ToolsNamespace
from gibson.harness.v1 import harness_callback_pb2, harness_callback_pb2_grpc


class Harness:
    """Connects to the daemon's HarnessCallbackService and exposes sub-namespaces.

    Instantiated by the AgentServicer from the callback_endpoint and token
    provided in each ExecuteRequest.  Not intended to be constructed manually
    outside of tests.

    Sub-namespaces::

        harness.llm         — LLM completions
        harness.tools       — invoke registered tools
        harness.graphrag    — knowledge graph queries and storage
        harness.findings    — emit security findings
        harness.memory      — mission-scoped key/value store
        harness.planning    — plan context access
    """

    def __init__(
        self,
        channel: grpc.Channel,
        context: harness_callback_pb2.ContextInfo,
    ) -> None:
        stub = harness_callback_pb2_grpc.HarnessCallbackServiceStub(channel)
        self.llm = LLMNamespace(stub, context)
        self.tools = ToolsNamespace(stub, context)
        self.graphrag = GraphRAGNamespace(stub, context)
        self.findings = FindingsNamespace(stub, context)
        self.memory = MemoryNamespace(stub, context)
        self.planning = PlanningNamespace(stub, context)
        self._channel = channel
        self._context = context

    @classmethod
    def from_callback(
        cls,
        endpoint: str,
        token: str,
        task_id: str = "",
        agent_name: str = "",
        trace_id: str = "",
        mission_run_id: str = "",
        agent_run_id: str = "",
        run_number: int = 0,
    ) -> Harness:
        """Create a Harness from a callback endpoint and bearer token.

        This is called by AgentServicer when the daemon provides the
        callback_endpoint and callback_token in ExecuteRequest.
        An insecure channel is used when the endpoint starts with
        ``localhost`` or ``127.0.0.1``; otherwise TLS is used.
        """
        from gibson.auth._credentials import channel_credentials  # noqa: PLC0415

        if endpoint.startswith(("localhost:", "127.0.0.1:")):
            channel = grpc.insecure_channel(endpoint)
        else:
            creds = channel_credentials(token)
            channel = grpc.secure_channel(endpoint, creds)

        context = harness_callback_pb2.ContextInfo(
            task_id=task_id,
            agent_name=agent_name,
            trace_id=trace_id,
            mission_run_id=mission_run_id,
            agent_run_id=agent_run_id,
            run_number=run_number,
        )
        return cls(channel, context)

    def close(self) -> None:
        """Close the underlying gRPC channel."""
        self._channel.close()
