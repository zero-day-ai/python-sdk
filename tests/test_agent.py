"""Tests for gibson.agent — BaseAgent, AgentServicer, Task/Result types."""

from __future__ import annotations

from concurrent import futures

import grpc
import pytest

from gibson.agent import AgentServicer, BaseAgent, Result, Task
from gibson.agent.v1 import agent_pb2, agent_pb2_grpc
from gibson.harness import Harness
from gibson.types.v1 import types_pb2
from tests.helpers.harness_stub import start_harness_stub_server

# ---------------------------------------------------------------------------
# Test agent implementations
# ---------------------------------------------------------------------------


class EchoAgent(BaseAgent):
    name = "echo-agent"
    description = "Echoes the task goal back as output"
    version = "1.0.0"
    capabilities = ["echo"]

    def execute_sync(self, harness: Harness, task: Task) -> Result:
        return Result.success(output=task.goal)


class LLMAgent(BaseAgent):
    name = "llm-agent"
    description = "Calls the LLM with the task goal"

    async def execute(self, harness: Harness, task: Task) -> Result:
        resp = harness.llm.complete([{"role": "user", "content": task.goal}])
        return Result.success(output=resp.content)


class FailingAgent(BaseAgent):
    name = "failing-agent"
    description = "Always fails"

    def execute_sync(self, harness: Harness, task: Task) -> Result:
        return Result.failure("intentional failure")


# ---------------------------------------------------------------------------
# Task / Result type tests
# ---------------------------------------------------------------------------


def test_task_from_proto():
    proto = types_pb2.Task(id="t1", goal="scan http://example.com")
    task = Task.from_proto(proto)
    assert task.id == "t1"
    assert task.goal == "scan http://example.com"


def test_result_success_status():
    r = Result.success("done")
    assert r.status == "success"
    assert r.output == "done"


def test_result_failure_status():
    r = Result.failure("boom")
    assert r.status == "failed"
    assert r.error == "boom"


def test_result_to_proto_success():
    r = Result.success("hello")
    proto = r.to_proto()
    assert proto.status == types_pb2.RESULT_STATUS_SUCCESS
    assert proto.output.string_value == "hello"


def test_result_to_proto_failure():
    r = Result.failure("oops")
    proto = r.to_proto()
    assert proto.status == types_pb2.RESULT_STATUS_FAILED
    assert "oops" in proto.error.message


# ---------------------------------------------------------------------------
# AgentServicer gRPC tests
# ---------------------------------------------------------------------------


@pytest.fixture
def agent_server_with_harness():
    """Start both an AgentService server and a HarnessCallbackService stub."""
    harness_server, harness_addr, harness_servicer = start_harness_stub_server()
    harness_servicer.llm_response_content = "LLM says hi"

    agent_server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
    agent_pb2_grpc.add_AgentServiceServicer_to_server(AgentServicer(LLMAgent()), agent_server)
    port = agent_server.add_insecure_port("127.0.0.1:0")
    agent_server.start()
    agent_addr = f"127.0.0.1:{port}"

    yield agent_addr, harness_addr, harness_servicer

    agent_server.stop(grace=1.0)
    harness_server.stop(grace=1.0)


def agent_stub(addr: str) -> agent_pb2_grpc.AgentServiceStub:
    return agent_pb2_grpc.AgentServiceStub(grpc.insecure_channel(addr))


def test_get_descriptor_returns_name(agent_server_with_harness):
    addr, _, _ = agent_server_with_harness
    resp = agent_stub(addr).GetDescriptor(agent_pb2.GetDescriptorRequest())
    assert resp.name == "llm-agent"


def test_get_descriptor_returns_version(agent_server_with_harness):
    addr, _, _ = agent_server_with_harness
    resp = agent_stub(addr).GetDescriptor(agent_pb2.GetDescriptorRequest())
    assert resp.version == "0.1.0"


def test_get_slot_schema_returns_empty_for_no_slots(agent_server_with_harness):
    addr, _, _ = agent_server_with_harness
    resp = agent_stub(addr).GetSlotSchema(agent_pb2.GetSlotSchemaRequest())
    assert len(resp.slots) == 0


def test_execute_calls_agent_and_returns_result(agent_server_with_harness):
    addr, harness_addr, harness_servicer = agent_server_with_harness
    req = agent_pb2.ExecuteRequest(
        task=types_pb2.Task(id="t1", goal="say hello"),
        callback_endpoint=harness_addr,
        callback_token="",
    )
    resp = agent_stub(addr).Execute(req)
    assert resp.result.status == types_pb2.RESULT_STATUS_SUCCESS
    assert resp.result.output.string_value == "LLM says hi"


def test_execute_harness_receives_llm_call(agent_server_with_harness):
    addr, harness_addr, harness_servicer = agent_server_with_harness
    req = agent_pb2.ExecuteRequest(
        task=types_pb2.Task(id="t2", goal="test goal"),
        callback_endpoint=harness_addr,
    )
    agent_stub(addr).Execute(req)
    assert len(harness_servicer.llm_calls) == 1
    assert harness_servicer.llm_calls[0].messages[0].content == "test goal"


def test_execute_echo_agent():
    """Test echo agent without a live harness."""
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
    agent_pb2_grpc.add_AgentServiceServicer_to_server(AgentServicer(EchoAgent()), server)
    port = server.add_insecure_port("127.0.0.1:0")
    server.start()
    stub = agent_pb2_grpc.AgentServiceStub(grpc.insecure_channel(f"127.0.0.1:{port}"))

    # Echo agent doesn't use harness, so empty callback endpoint is fine
    req = agent_pb2.ExecuteRequest(
        task=types_pb2.Task(id="e1", goal="my goal"),
        callback_endpoint="",
    )
    resp = stub.Execute(req)
    assert resp.result.output.string_value == "my goal"
    server.stop(grace=1.0)


def test_execute_failing_agent_returns_failed_status():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
    agent_pb2_grpc.add_AgentServiceServicer_to_server(AgentServicer(FailingAgent()), server)
    port = server.add_insecure_port("127.0.0.1:0")
    server.start()
    stub = agent_pb2_grpc.AgentServiceStub(grpc.insecure_channel(f"127.0.0.1:{port}"))

    req = agent_pb2.ExecuteRequest(task=types_pb2.Task(id="f1", goal="fail"))
    resp = stub.Execute(req)
    assert resp.result.status == types_pb2.RESULT_STATUS_FAILED
    server.stop(grace=1.0)


def test_health_returns_healthy():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
    agent_pb2_grpc.add_AgentServiceServicer_to_server(AgentServicer(EchoAgent()), server)
    port = server.add_insecure_port("127.0.0.1:0")
    server.start()
    stub = agent_pb2_grpc.AgentServiceStub(grpc.insecure_channel(f"127.0.0.1:{port}"))
    resp = stub.Health(agent_pb2.HealthRequest())
    assert resp.status.status == "healthy"
    server.stop(grace=1.0)
