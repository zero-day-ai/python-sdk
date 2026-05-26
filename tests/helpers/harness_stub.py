"""In-process HarnessCallbackService stub for tests."""

from __future__ import annotations

from concurrent import futures

import grpc

from gibson.harness.v1 import harness_callback_pb2, harness_callback_pb2_grpc


class RecordingHarnessServicer(harness_callback_pb2_grpc.HarnessCallbackServiceServicer):
    """Records calls and returns configurable responses for tests."""

    def __init__(self) -> None:
        self.llm_calls: list[harness_callback_pb2.LLMCompleteRequest] = []
        self.tool_calls: list[harness_callback_pb2.CallToolProtoRequest] = []
        self.memory_sets: list[harness_callback_pb2.MemorySetRequest] = []
        self.memory_gets: list[harness_callback_pb2.MemoryGetRequest] = []
        self.findings: list[harness_callback_pb2.SubmitFindingRequest] = []
        self.list_tools_calls: int = 0

        self.llm_response_content = "mocked LLM response"
        self.memory_store: dict[str, harness_callback_pb2.MemoryGetResponse] = {}
        self.tool_response_json: bytes = b'{"result": "ok"}'

    def LLMComplete(self, request, context):
        self.llm_calls.append(request)
        return harness_callback_pb2.LLMCompleteResponse(
            content=self.llm_response_content,
            finish_reason="stop",
        )

    def LLMCompleteWithTools(self, request, context):
        self.llm_calls.append(request)
        return harness_callback_pb2.LLMCompleteWithToolsResponse(
            content=self.llm_response_content,
        )

    def CallToolProto(self, request, context):
        self.tool_calls.append(request)
        return harness_callback_pb2.CallToolProtoResponse(
            output_json=self.tool_response_json,
        )

    def ListTools(self, request, context):
        self.list_tools_calls += 1
        return harness_callback_pb2.ListToolsResponse(tools=[])

    def MemoryGet(self, request, context):
        self.memory_gets.append(request)
        return self.memory_store.get(
            request.key,
            harness_callback_pb2.MemoryGetResponse(found=False),
        )

    def MemorySet(self, request, context):
        self.memory_sets.append(request)

        self.memory_store[request.key] = harness_callback_pb2.MemoryGetResponse(
            found=True,
            value=request.value,
        )
        return harness_callback_pb2.MemorySetResponse()

    def SubmitFinding(self, request, context):
        self.findings.append(request)
        return harness_callback_pb2.SubmitFindingResponse()

    def GraphRAGQuery(self, request, context):
        return harness_callback_pb2.GraphRAGQueryResponse(results=[])

    def StoreGraphNode(self, request, context):
        return harness_callback_pb2.StoreGraphNodeResponse(node_id="test-node-id")

    def GetPlanContext(self, request, context):
        pc = harness_callback_pb2.PlanContext(current_step_index=0)
        return harness_callback_pb2.GetPlanContextResponse(plan_context=pc)


def start_harness_stub_server() -> tuple[grpc.Server, str, RecordingHarnessServicer]:
    """Start an in-process HarnessCallbackService stub; return (server, addr, servicer)."""
    servicer = RecordingHarnessServicer()
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
    harness_callback_pb2_grpc.add_HarnessCallbackServiceServicer_to_server(servicer, server)
    port = server.add_insecure_port("127.0.0.1:0")
    server.start()
    return server, f"127.0.0.1:{port}", servicer
