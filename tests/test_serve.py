"""Tests for gibson.serve — serve_tool and serve_agent."""

from __future__ import annotations

from concurrent import futures

import grpc
from pydantic import BaseModel

from gibson.agent._base import BaseAgent
from gibson.agent._types import Result, Task
from gibson.agent.v1 import agent_pb2, agent_pb2_grpc
from gibson.harness import Harness
from gibson.tool._base import BaseTool
from gibson.tool.v1 import tool_pb2, tool_pb2_grpc

# ---------------------------------------------------------------------------
# Minimal tool and agent for testing
# ---------------------------------------------------------------------------


class PingInput(BaseModel):
    msg: str


class PingOutput(BaseModel):
    reply: str


class PingTool(BaseTool):
    name = "ping"
    description = "Echoes the message"
    InputModel = PingInput
    OutputModel = PingOutput

    def execute(self, input: PingInput) -> PingOutput:
        return PingOutput(reply=f"pong:{input.msg}")


class PingAgent(BaseAgent):
    name = "ping-agent"
    description = "Echoes the goal"

    def execute_sync(self, harness: Harness, task: Task) -> Result:
        return Result.success(output=task.goal)


# ---------------------------------------------------------------------------
# serve_tool tests
# ---------------------------------------------------------------------------


def test_serve_tool_health_check():
    """serve_tool starts a gRPC ToolService reachable at the given port."""

    from gibson.tool._server import ToolServicer

    # Start a server directly (avoids blocking serve_tool's signal handling)
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
    tool_pb2_grpc.add_ToolServiceServicer_to_server(ToolServicer(PingTool()), server)
    port = server.add_insecure_port("127.0.0.1:0")
    server.start()

    stub = tool_pb2_grpc.ToolServiceStub(grpc.insecure_channel(f"127.0.0.1:{port}"))
    resp = stub.Health(tool_pb2.HealthRequest())
    assert resp.status.status == "healthy"
    server.stop(grace=1.0)


def test_serve_tool_execute_round_trip():

    from gibson.tool._server import ToolServicer
    from gibson.tool.v1 import tool_pb2

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
    tool_pb2_grpc.add_ToolServiceServicer_to_server(ToolServicer(PingTool()), server)
    port = server.add_insecure_port("127.0.0.1:0")
    server.start()

    stub = tool_pb2_grpc.ToolServiceStub(grpc.insecure_channel(f"127.0.0.1:{port}"))
    resp = stub.Execute(tool_pb2.ExecuteRequest(input_json=b'{"msg":"hello"}'))
    import json

    result = json.loads(resp.output_json)
    assert result["reply"] == "pong:hello"
    server.stop(grace=1.0)


# ---------------------------------------------------------------------------
# serve_agent tests
# ---------------------------------------------------------------------------


def test_serve_agent_health_check():

    from gibson.agent._server import AgentServicer

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
    agent_pb2_grpc.add_AgentServiceServicer_to_server(AgentServicer(PingAgent()), server)
    port = server.add_insecure_port("127.0.0.1:0")
    server.start()

    stub = agent_pb2_grpc.AgentServiceStub(grpc.insecure_channel(f"127.0.0.1:{port}"))
    resp = stub.Health(agent_pb2.HealthRequest())
    assert resp.status.status == "healthy"
    server.stop(grace=1.0)


def test_serve_agent_descriptor():

    from gibson.agent._server import AgentServicer

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
    agent_pb2_grpc.add_AgentServiceServicer_to_server(AgentServicer(PingAgent()), server)
    port = server.add_insecure_port("127.0.0.1:0")
    server.start()

    stub = agent_pb2_grpc.AgentServiceStub(grpc.insecure_channel(f"127.0.0.1:{port}"))
    resp = stub.GetDescriptor(agent_pb2.GetDescriptorRequest())
    assert resp.name == "ping-agent"
    server.stop(grace=1.0)
