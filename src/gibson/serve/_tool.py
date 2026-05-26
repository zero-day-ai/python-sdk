"""Serve a BaseTool as a gRPC ToolService."""

from __future__ import annotations

import signal
import sys
from concurrent import futures

import grpc

from gibson.tool._base import BaseTool
from gibson.tool._server import ToolServicer
from gibson.tool.v1 import tool_pb2_grpc


def serve_tool(
    tool: BaseTool,
    *,
    port: int = 50052,
    max_workers: int = 10,
) -> None:
    """Start a blocking gRPC ToolService for *tool* on *port*.

    Handles SIGTERM and SIGINT for graceful shutdown so that the process
    can be terminated cleanly by a container runtime or Ctrl-C.
    """
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=max_workers))
    tool_pb2_grpc.add_ToolServiceServicer_to_server(ToolServicer(tool), server)
    server.add_insecure_port(f"[::]:{port}")
    server.start()

    _install_signal_handlers(server)
    server.wait_for_termination()


def _install_signal_handlers(server: grpc.Server) -> None:
    def _stop(signum, frame):  # noqa: ARG001
        server.stop(grace=5.0)
        sys.exit(0)

    signal.signal(signal.SIGTERM, _stop)
    signal.signal(signal.SIGINT, _stop)
