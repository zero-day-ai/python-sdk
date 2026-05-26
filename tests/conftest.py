"""Shared pytest fixtures for the Gibson Python SDK test suite."""

from __future__ import annotations

from concurrent import futures

import grpc
import pytest

from gibson.tool import BaseTool, ToolServicer
from gibson.tool.v1 import tool_pb2_grpc


def _start_tool_server(tool: BaseTool) -> tuple[grpc.Server, str]:
    """Start an in-process gRPC server hosting a tool; return (server, address)."""
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
    tool_pb2_grpc.add_ToolServiceServicer_to_server(ToolServicer(tool), server)
    port = server.add_insecure_port("127.0.0.1:0")
    server.start()
    return server, f"127.0.0.1:{port}"


@pytest.fixture
def tool_server(request):
    """Fixture that starts an in-process gRPC ToolService server.

    Parameterize with a BaseTool instance via ``pytest.param``.
    Usage::

        @pytest.fixture
        def my_tool_server(tool_server):
            return tool_server(my_tool_instance)

    Or use the fixture factory directly in the test.
    """
    servers: list[grpc.Server] = []

    def factory(tool: BaseTool) -> tuple[grpc.Server, grpc.Channel, str]:
        server, addr = _start_tool_server(tool)
        servers.append(server)
        channel = grpc.insecure_channel(addr)
        return server, channel, addr

    yield factory

    for srv in servers:
        srv.stop(grace=1.0)
