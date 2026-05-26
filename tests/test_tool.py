"""Tests for gibson.tool — BaseTool, @tool decorator, and ToolServicer."""

from __future__ import annotations

import json

import grpc
import pytest
from pydantic import BaseModel

from gibson.tool import BaseTool, tool
from gibson.tool.v1 import tool_pb2, tool_pb2_grpc

# ---------------------------------------------------------------------------
# Test fixtures — models and tools
# ---------------------------------------------------------------------------


class ScanInput(BaseModel):
    url: str
    depth: int = 1


class ScanOutput(BaseModel):
    findings: list[str]
    scanned: bool = True


class EchoInput(BaseModel):
    message: str


class EchoOutput(BaseModel):
    echo: str


@tool
def echo_tool(input: EchoInput) -> EchoOutput:
    """Echoes the input message back."""
    return EchoOutput(echo=input.message)


class ScannerTool(BaseTool):
    name = "scanner"
    description = "Scans a URL for security issues"
    version = "1.0.0"
    tags = ["recon", "scan"]
    InputModel = ScanInput
    OutputModel = ScanOutput

    def execute(self, input: ScanInput) -> ScanOutput:
        return ScanOutput(findings=[f"XSS at {input.url}"])


# ---------------------------------------------------------------------------
# BaseTool tests
# ---------------------------------------------------------------------------


def test_base_tool_name():
    t = ScannerTool()
    assert t.name == "scanner"


def test_base_tool_description():
    t = ScannerTool()
    assert "Scans" in t.description


def test_base_tool_tags():
    t = ScannerTool()
    assert "recon" in t.tags


def test_base_tool_input_schema_is_valid_json():
    t = ScannerTool()
    schema = json.loads(t.input_schema_json())
    assert "properties" in schema
    assert "url" in schema["properties"]


def test_base_tool_output_schema_is_valid_json():
    t = ScannerTool()
    schema = json.loads(t.output_schema_json())
    assert "properties" in schema
    assert "findings" in schema["properties"]


def test_base_tool_execute_returns_output_model():
    t = ScannerTool()
    result = t.execute(ScanInput(url="http://example.com"))
    assert isinstance(result, ScanOutput)
    assert len(result.findings) > 0


def test_base_tool_health_defaults_healthy():
    t = ScannerTool()
    assert t.health() == "healthy"


# ---------------------------------------------------------------------------
# @tool decorator tests
# ---------------------------------------------------------------------------


def test_tool_decorator_creates_base_tool():
    assert isinstance(echo_tool, BaseTool)


def test_tool_decorator_name_from_function():
    assert echo_tool.name == "echo_tool"


def test_tool_decorator_description_from_docstring():
    assert "Echoes" in echo_tool.description


def test_tool_decorator_with_explicit_params():
    @tool(name="custom-echo", description="A custom echo", tags=["util"])
    def my_echo(input: EchoInput) -> EchoOutput:
        return EchoOutput(echo=input.message)

    assert my_echo.name == "custom-echo"
    assert my_echo.description == "A custom echo"
    assert "util" in my_echo.tags


def test_tool_decorator_rejects_non_pydantic_input():
    with pytest.raises(TypeError, match="pydantic.BaseModel"):

        @tool
        def bad_tool(input: str) -> EchoOutput:  # type: ignore[misc]
            return EchoOutput(echo=input)


def test_tool_decorator_rejects_missing_return_type():
    with pytest.raises(TypeError, match="pydantic.BaseModel"):

        @tool
        def bad_tool2(input: EchoInput):  # type: ignore[return]
            return EchoOutput(echo=input.message)


def test_tool_decorator_execute():
    result = echo_tool.execute(EchoInput(message="hello"))
    assert isinstance(result, EchoOutput)
    assert result.echo == "hello"


# ---------------------------------------------------------------------------
# ToolServicer (gRPC) tests
# ---------------------------------------------------------------------------


@pytest.fixture
def scanner_channel(tool_server):
    _, channel, _ = tool_server(ScannerTool())
    return channel


def stub(channel: grpc.Channel) -> tool_pb2_grpc.ToolServiceStub:
    return tool_pb2_grpc.ToolServiceStub(channel)


def test_get_descriptor_returns_name(scanner_channel):
    resp = stub(scanner_channel).GetDescriptor(tool_pb2.GetDescriptorRequest())
    assert resp.name == "scanner"


def test_get_descriptor_returns_version(scanner_channel):
    resp = stub(scanner_channel).GetDescriptor(tool_pb2.GetDescriptorRequest())
    assert resp.version == "1.0.0"


def test_get_descriptor_returns_tags(scanner_channel):
    resp = stub(scanner_channel).GetDescriptor(tool_pb2.GetDescriptorRequest())
    assert "recon" in resp.tags


def test_get_descriptor_input_schema_valid_json(scanner_channel):
    resp = stub(scanner_channel).GetDescriptor(tool_pb2.GetDescriptorRequest())
    schema = json.loads(resp.input_schema.json)
    assert "url" in schema["properties"]


def test_get_descriptor_output_schema_valid_json(scanner_channel):
    resp = stub(scanner_channel).GetDescriptor(tool_pb2.GetDescriptorRequest())
    schema = json.loads(resp.output_schema.json)
    assert "findings" in schema["properties"]


def test_execute_valid_input_returns_output(scanner_channel):
    req = tool_pb2.ExecuteRequest(input_json=json.dumps({"url": "http://example.com", "depth": 2}))
    resp = stub(scanner_channel).Execute(req)
    assert resp.output_json
    output = json.loads(resp.output_json)
    assert "findings" in output
    assert len(output["findings"]) > 0


def test_execute_invalid_json_returns_error(scanner_channel):
    req = tool_pb2.ExecuteRequest(input_json="not-json")
    resp = stub(scanner_channel).Execute(req)
    assert resp.error.code == "INVALID_ARGUMENT"


def test_execute_missing_required_field_returns_error(scanner_channel):
    req = tool_pb2.ExecuteRequest(input_json=json.dumps({"depth": 1}))
    resp = stub(scanner_channel).Execute(req)
    assert resp.error.code == "INVALID_ARGUMENT"


def test_health_returns_healthy(scanner_channel):
    resp = stub(scanner_channel).Health(tool_pb2.HealthRequest())
    assert resp.status.status == "healthy"
