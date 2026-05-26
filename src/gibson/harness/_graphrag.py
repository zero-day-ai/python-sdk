"""GraphRAG namespace for the Gibson Harness."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from gibson.harness.v1 import harness_callback_pb2, harness_callback_pb2_grpc
from gibson.types.v1 import types_pb2


@dataclass
class GraphRAGResult:
    """A single result from a GraphRAG query."""

    node_id: str
    score: float
    properties: dict[str, Any] = field(default_factory=dict)


class GraphRAGNamespace:
    """Harness GraphRAG operations — store and query the mission knowledge graph."""

    def __init__(
        self,
        stub: harness_callback_pb2_grpc.HarnessCallbackServiceStub,
        context: Any,
    ) -> None:
        self._stub = stub
        self._ctx = context

    def query(self, text: str, top_k: int = 10, scope: str = "mission") -> list[GraphRAGResult]:
        """Query the GraphRAG knowledge base with natural language."""
        scope_map = {
            "mission_run": types_pb2.QUERY_SCOPE_MISSION_RUN,
            "mission": types_pb2.QUERY_SCOPE_MISSION,
            "global": types_pb2.QUERY_SCOPE_GLOBAL,
        }
        query = types_pb2.GraphQuery(
            text=text,
            top_k=top_k,
            scope=scope_map.get(scope, types_pb2.QUERY_SCOPE_MISSION),
        )
        req = harness_callback_pb2.GraphRAGQueryRequest(context=self._ctx, query=query)
        resp = self._stub.GraphRAGQuery(req)
        return [
            GraphRAGResult(
                node_id=r.node.node_id if r.HasField("node") else "",
                score=r.score if hasattr(r, "score") else 0.0,
            )
            for r in resp.results
        ]

    def store_finding(self, finding: types_pb2.Finding) -> None:
        """Submit a finding to the GraphRAG knowledge base."""
        req = harness_callback_pb2.SubmitFindingRequest(
            context=self._ctx,
            finding=finding,
        )
        self._stub.SubmitFinding(req)

    def store(self, node_id: str, properties: dict[str, Any], node_type: str = "finding") -> str:
        """Store a node in the knowledge graph. Returns the assigned node ID."""
        from gibson.harness.v1 import harness_callback_pb2 as hpb  # noqa: PLC0415

        node = hpb.GraphNode(node_id=node_id, node_type=node_type)
        req = harness_callback_pb2.StoreGraphNodeRequest(context=self._ctx, node=node)
        resp = self._stub.StoreGraphNode(req)
        return resp.node_id

    async def query_async(
        self, text: str, top_k: int = 10, scope: str = "mission"
    ) -> list[GraphRAGResult]:
        """Async GraphRAG query."""
        scope_map = {
            "mission_run": types_pb2.QUERY_SCOPE_MISSION_RUN,
            "mission": types_pb2.QUERY_SCOPE_MISSION,
            "global": types_pb2.QUERY_SCOPE_GLOBAL,
        }
        query = types_pb2.GraphQuery(
            text=text,
            top_k=top_k,
            scope=scope_map.get(scope, types_pb2.QUERY_SCOPE_MISSION),
        )
        req = harness_callback_pb2.GraphRAGQueryRequest(context=self._ctx, query=query)
        resp = await self._stub.GraphRAGQuery(req)
        return [
            GraphRAGResult(
                node_id=r.node.node_id if r.HasField("node") else "",
                score=r.score if hasattr(r, "score") else 0.0,
            )
            for r in resp.results
        ]
