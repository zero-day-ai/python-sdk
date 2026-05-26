"""Serve a BaseAgent as a gRPC AgentService."""

from __future__ import annotations

import signal
import sys
from concurrent import futures

import grpc

from gibson.agent._base import BaseAgent
from gibson.agent._server import AgentServicer
from gibson.agent.v1 import agent_pb2_grpc


def serve_agent(
    agent: BaseAgent,
    *,
    port: int = 50051,
    max_workers: int = 10,
) -> None:
    """Start a blocking gRPC AgentService for *agent* on *port*.

    Handles SIGTERM and SIGINT for graceful shutdown.
    """
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=max_workers))
    agent_pb2_grpc.add_AgentServiceServicer_to_server(AgentServicer(agent), server)
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
