"""Tests for gibson.harness — Harness client and sub-namespaces."""

from __future__ import annotations

import grpc
import pytest

from gibson.harness import Harness, LLMResponse
from gibson.harness.v1 import harness_callback_pb2
from tests.helpers.harness_stub import start_harness_stub_server


@pytest.fixture
def harness_server():
    server, addr, servicer = start_harness_stub_server()
    channel = grpc.insecure_channel(addr)
    context = harness_callback_pb2.ContextInfo(task_id="t1", agent_name="test-agent")
    harness = Harness(channel, context)
    yield harness, servicer
    server.stop(grace=1.0)


# ---------------------------------------------------------------------------
# LLM namespace
# ---------------------------------------------------------------------------


def test_llm_complete_returns_response(harness_server):
    harness, servicer = harness_server
    servicer.llm_response_content = "hello from LLM"
    resp = harness.llm.complete([{"role": "user", "content": "hi"}])
    assert isinstance(resp, LLMResponse)
    assert resp.content == "hello from LLM"


def test_llm_complete_sends_messages(harness_server):
    harness, servicer = harness_server
    harness.llm.complete([{"role": "user", "content": "test"}])
    assert len(servicer.llm_calls) == 1
    assert servicer.llm_calls[0].messages[0].role == "user"
    assert servicer.llm_calls[0].messages[0].content == "test"


def test_llm_complete_attaches_context(harness_server):
    harness, servicer = harness_server
    harness.llm.complete([{"role": "user", "content": "x"}])
    assert servicer.llm_calls[0].context.task_id == "t1"
    assert servicer.llm_calls[0].context.agent_name == "test-agent"


def test_llm_complete_with_tools(harness_server):
    harness, servicer = harness_server
    servicer.llm_response_content = "tool response"
    resp = harness.llm.complete_with_tools(
        [{"role": "user", "content": "scan"}],
        tools=[{"name": "scanner", "description": "scans"}],
    )
    assert resp.content == "tool response"


# ---------------------------------------------------------------------------
# Tools namespace
# ---------------------------------------------------------------------------


def test_tools_call_returns_dict(harness_server):
    harness, servicer = harness_server
    servicer.tool_response_json = b'{"status": "done"}'
    result = harness.tools.call("my-tool", {"url": "http://example.com"})
    assert result == {"status": "done"}


def test_tools_call_sends_tool_name(harness_server):
    harness, servicer = harness_server
    harness.tools.call("scanner", {"url": "x"})
    assert servicer.tool_calls[0].name == "scanner"


def test_tools_list_returns_list(harness_server):
    harness, servicer = harness_server
    tools = harness.tools.list()
    assert isinstance(tools, list)
    assert servicer.list_tools_calls == 1


# ---------------------------------------------------------------------------
# Memory namespace
# ---------------------------------------------------------------------------


def test_memory_set_and_get(harness_server):
    harness, servicer = harness_server
    harness.memory.set("my-key", "hello")
    result = harness.memory.get("my-key")
    assert result == "hello"


def test_memory_get_missing_returns_none(harness_server):
    harness, servicer = harness_server
    result = harness.memory.get("nonexistent-key")
    assert result is None


def test_memory_set_records_request(harness_server):
    harness, servicer = harness_server
    harness.memory.set("k", 42)
    assert len(servicer.memory_sets) == 1
    assert servicer.memory_sets[0].key == "k"


# ---------------------------------------------------------------------------
# Findings namespace
# ---------------------------------------------------------------------------


def test_findings_emit_sends_finding(harness_server):
    harness, servicer = harness_server
    from gibson.types.v1 import types_pb2  # noqa: PLC0415

    finding = types_pb2.Finding(
        title="XSS",
        description="Reflected XSS",
        severity=types_pb2.FINDING_SEVERITY_HIGH,
    )
    harness.findings.emit(finding)
    assert len(servicer.findings) == 1
    assert servicer.findings[0].finding.title == "XSS"


# ---------------------------------------------------------------------------
# GraphRAG namespace
# ---------------------------------------------------------------------------


def test_graphrag_query_returns_list(harness_server):
    harness, servicer = harness_server
    results = harness.graphrag.query("find SQL injection patterns")
    assert isinstance(results, list)


# ---------------------------------------------------------------------------
# Harness.from_callback
# ---------------------------------------------------------------------------


def test_harness_from_callback_localhost(harness_server):
    _, servicer = harness_server
    _, addr, _ = start_harness_stub_server()
    h = Harness.from_callback(
        endpoint=addr,
        token="tok",
        task_id="t2",
        agent_name="test",
    )
    # Verify we can call through it
    h.tools.list()
    h.close()
