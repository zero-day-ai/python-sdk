"""Tests for gibson.cli — serve, scaffold, healthcheck commands."""

from __future__ import annotations

import os

import pytest

# Skip all CLI tests if click is not installed
click = pytest.importorskip("click")
from click.testing import CliRunner  # noqa: E402

from gibson.cli._loader import load_object  # noqa: E402
from gibson.cli._main import main  # noqa: E402
from gibson.cli._scaffold import scaffold_agent, scaffold_tool  # noqa: E402

# ---------------------------------------------------------------------------
# Loader tests
# ---------------------------------------------------------------------------


def test_load_object_invalid_ref():
    with pytest.raises(ValueError, match="Invalid reference"):
        load_object("no_colon_here")


def test_load_object_missing_attr():
    with pytest.raises(AttributeError, match="no attribute"):
        load_object("gibson.tool:_nonexistent_attr_xyz")


def test_load_object_valid():
    from gibson.tool._base import BaseTool

    obj = load_object("gibson.tool._base:BaseTool")
    assert obj is BaseTool


# ---------------------------------------------------------------------------
# Scaffold tests
# ---------------------------------------------------------------------------


def test_scaffold_tool_produces_python_code():
    code = scaffold_tool("my-scanner")
    assert "class MyScanner" in code or "def my_scanner" in code
    assert "BaseTool" not in code or "@tool" in code
    assert "serve_tool" in code


def test_scaffold_agent_produces_python_code():
    code = scaffold_agent("recon-agent")
    assert "BaseAgent" in code
    assert "serve_agent" in code
    assert "recon-agent" in code or "recon_agent" in code


def test_scaffold_tool_cmd_creates_file(tmp_path):
    runner = CliRunner()
    out_file = str(tmp_path / "my_tool.py")
    result = runner.invoke(main, ["scaffold", "tool", "my-tool", "--output", out_file])
    assert result.exit_code == 0
    assert os.path.exists(out_file)
    with open(out_file) as f:
        content = f.read()
    assert "@tool" in content or "BaseTool" in content


def test_scaffold_agent_cmd_creates_file(tmp_path):
    runner = CliRunner()
    out_file = str(tmp_path / "my_agent.py")
    result = runner.invoke(main, ["scaffold", "agent", "my-agent", "--output", out_file])
    assert result.exit_code == 0
    assert os.path.exists(out_file)
    with open(out_file) as f:
        content = f.read()
    assert "BaseAgent" in content


# ---------------------------------------------------------------------------
# CLI integration tests
# ---------------------------------------------------------------------------


def test_main_help():
    runner = CliRunner()
    result = runner.invoke(main, ["--help"])
    assert result.exit_code == 0
    assert "serve" in result.output
    assert "scaffold" in result.output
    assert "healthcheck" in result.output


def test_serve_help():
    runner = CliRunner()
    result = runner.invoke(main, ["serve", "--help"])
    assert result.exit_code == 0
    assert "tool" in result.output
    assert "agent" in result.output


def test_serve_tool_invalid_ref():
    runner = CliRunner()
    result = runner.invoke(main, ["serve", "tool", "not_a_module:nope"])
    assert result.exit_code != 0


def test_serve_tool_wrong_type():
    """Passing a non-BaseTool object should print an error and exit non-zero."""
    runner = CliRunner()
    # str is not a BaseTool
    result = runner.invoke(main, ["serve", "builtins:str"])
    assert result.exit_code != 0


def test_serve_agent_wrong_type():
    """Passing a non-BaseAgent object should print an error and exit non-zero."""
    runner = CliRunner()
    result = runner.invoke(main, ["serve", "agent", "builtins:int"])
    assert result.exit_code != 0


def test_healthcheck_tool(tmp_path):
    """healthcheck against a live gRPC server returns healthy."""
    from concurrent import futures

    import grpc
    from pydantic import BaseModel

    from gibson.tool._base import BaseTool
    from gibson.tool._server import ToolServicer
    from gibson.tool.v1 import tool_pb2_grpc

    class _Input(BaseModel):
        x: int

    class _Output(BaseModel):
        y: int

    class _Tool(BaseTool):
        name = "t"
        description = "d"
        InputModel = _Input
        OutputModel = _Output

        def execute(self, input: _Input) -> _Output:
            return _Output(y=input.x)

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
    tool_pb2_grpc.add_ToolServiceServicer_to_server(ToolServicer(_Tool()), server)
    port = server.add_insecure_port("127.0.0.1:0")
    server.start()

    runner = CliRunner()
    result = runner.invoke(main, ["healthcheck", f"127.0.0.1:{port}", "--type", "tool"])
    assert result.exit_code == 0
    assert "healthy" in result.output
    server.stop(grace=1.0)


def test_healthcheck_agent():
    """healthcheck against a live agent gRPC server returns healthy."""
    from concurrent import futures

    import grpc

    from gibson.agent._base import BaseAgent
    from gibson.agent._server import AgentServicer
    from gibson.agent._types import Result, Task
    from gibson.agent.v1 import agent_pb2_grpc
    from gibson.harness import Harness

    class _Agent(BaseAgent):
        name = "a"
        description = "d"

        def execute_sync(self, harness: Harness, task: Task) -> Result:
            return Result.success(output="ok")

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
    agent_pb2_grpc.add_AgentServiceServicer_to_server(AgentServicer(_Agent()), server)
    port = server.add_insecure_port("127.0.0.1:0")
    server.start()

    runner = CliRunner()
    result = runner.invoke(main, ["healthcheck", f"127.0.0.1:{port}", "--type", "agent"])
    assert result.exit_code == 0
    assert "healthy" in result.output
    server.stop(grace=1.0)
