"""Gibson CLI — serve and scaffold tools/agents."""

from __future__ import annotations

import sys

try:
    import click
except ImportError:
    print(  # noqa: T201
        "The 'click' package is required for the CLI. "
        "Install it with: pip install gibson-sdk[cli]",
        file=sys.stderr,
    )
    sys.exit(1)

from gibson.cli._loader import load_object
from gibson.cli._scaffold import scaffold_agent, scaffold_tool


@click.group()
def main() -> None:
    """Gibson SDK command-line interface."""


# ---------------------------------------------------------------------------
# serve
# ---------------------------------------------------------------------------


@main.group()
def serve() -> None:
    """Start a gRPC service for a tool or agent."""


@serve.command("tool")
@click.argument("ref")
@click.option("--port", default=50052, show_default=True, help="Port to listen on.")
@click.option("--workers", default=10, show_default=True, help="gRPC thread pool size.")
def serve_tool_cmd(ref: str, port: int, workers: int) -> None:
    """Serve the tool at REF (module:attribute) as a gRPC ToolService.

    Example: gibson serve tool my_scanner:scanner
    """
    from gibson.serve import serve_tool
    from gibson.tool._base import BaseTool

    obj = load_object(ref)
    if not isinstance(obj, BaseTool):
        click.echo(f"Error: {ref!r} is not a BaseTool instance.", err=True)
        sys.exit(1)

    click.echo(f"Serving tool '{obj.name}' on :{port}")
    serve_tool(obj, port=port, max_workers=workers)


@serve.command("agent")
@click.argument("ref")
@click.option("--port", default=50051, show_default=True, help="Port to listen on.")
@click.option("--workers", default=10, show_default=True, help="gRPC thread pool size.")
def serve_agent_cmd(ref: str, port: int, workers: int) -> None:
    """Serve the agent at REF (module:attribute) as a gRPC AgentService.

    Example: gibson serve agent my_agent:agent
    """
    from gibson.agent._base import BaseAgent
    from gibson.serve import serve_agent

    obj = load_object(ref)
    if not isinstance(obj, BaseAgent):
        click.echo(f"Error: {ref!r} is not a BaseAgent instance.", err=True)
        sys.exit(1)

    click.echo(f"Serving agent '{obj.name}' on :{port}")
    serve_agent(obj, port=port, max_workers=workers)


# ---------------------------------------------------------------------------
# scaffold
# ---------------------------------------------------------------------------


@main.group()
def scaffold() -> None:
    """Generate starter code for a new tool or agent."""


@scaffold.command("tool")
@click.argument("name")
@click.option("--output", "-o", default=None, help="Output file path (default: <name>.py).")
def scaffold_tool_cmd(name: str, output: str | None) -> None:
    """Generate a starter tool file named NAME."""
    path = output or f"{name.replace('-', '_')}.py"
    code = scaffold_tool(name)
    with open(path, "w") as f:
        f.write(code)
    click.echo(f"Created {path}")


@scaffold.command("agent")
@click.argument("name")
@click.option("--output", "-o", default=None, help="Output file path (default: <name>.py).")
def scaffold_agent_cmd(name: str, output: str | None) -> None:
    """Generate a starter agent file named NAME."""
    path = output or f"{name.replace('-', '_')}.py"
    code = scaffold_agent(name)
    with open(path, "w") as f:
        f.write(code)
    click.echo(f"Created {path}")


# ---------------------------------------------------------------------------
# healthcheck
# ---------------------------------------------------------------------------


@main.command()
@click.argument("endpoint")
@click.option(
    "--type",
    "service_type",
    type=click.Choice(["tool", "agent"]),
    default="agent",
    show_default=True,
)
def healthcheck(endpoint: str, service_type: str) -> None:
    """Check health of a tool or agent at ENDPOINT (host:port)."""
    import grpc

    if service_type == "tool":
        from gibson.tool.v1 import tool_pb2, tool_pb2_grpc

        channel = grpc.insecure_channel(endpoint)
        stub = tool_pb2_grpc.ToolServiceStub(channel)
        resp = stub.Health(tool_pb2.HealthRequest())
        click.echo(f"Tool health: {resp.status.status}")
    else:
        from gibson.agent.v1 import agent_pb2, agent_pb2_grpc

        channel = grpc.insecure_channel(endpoint)
        stub = agent_pb2_grpc.AgentServiceStub(channel)
        resp = stub.Health(agent_pb2.HealthRequest())
        click.echo(f"Agent health: {resp.status.status}")
