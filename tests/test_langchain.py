"""Tests for gibson.langchain — GibsonTool, GibsonToolRegistry, GibsonLLM, GibsonCallbackHandler."""

from __future__ import annotations

import grpc
import pytest

langchain_core = pytest.importorskip("langchain_core")  # noqa: E402

from langchain_core.messages import HumanMessage  # noqa: E402

from gibson.harness import Harness  # noqa: E402
from gibson.harness.v1 import harness_callback_pb2  # noqa: E402
from gibson.langchain import (  # noqa: E402
    GibsonCallbackHandler,
    GibsonLLM,
    GibsonTool,
    GibsonToolRegistry,
)
from tests.helpers.harness_stub import start_harness_stub_server  # noqa: E402


@pytest.fixture
def harness_with_stub():
    server, addr, servicer = start_harness_stub_server()
    servicer.llm_response_content = "LangChain response"
    servicer.tool_response_json = b'{"output": "tool result"}'
    channel = grpc.insecure_channel(addr)
    context = harness_callback_pb2.ContextInfo(task_id="t1", agent_name="lc-test")
    harness = Harness(channel, context)
    yield harness, servicer
    server.stop(grace=1.0)


# ---------------------------------------------------------------------------
# GibsonTool tests
# ---------------------------------------------------------------------------


def test_gibson_tool_name(harness_with_stub):
    harness, _ = harness_with_stub
    tool = GibsonTool(name="scanner", description="Scans URLs", harness=harness, tool_name="scanner")
    assert tool.name == "scanner"


def test_gibson_tool_run_sends_to_harness(harness_with_stub):
    harness, servicer = harness_with_stub
    tool = GibsonTool(name="scanner", description="Scans", harness=harness, tool_name="scanner")
    tool._run(url="http://example.com")
    assert len(servicer.tool_calls) == 1
    assert servicer.tool_calls[0].name == "scanner"


def test_gibson_tool_run_returns_json(harness_with_stub):
    harness, _ = harness_with_stub
    tool = GibsonTool(name="scanner", description="Scans", harness=harness, tool_name="scanner")
    result = tool._run(url="http://example.com")
    import json
    parsed = json.loads(result)
    assert parsed["output"] == "tool result"


def test_gibson_tool_run_with_string_input(harness_with_stub):
    harness, servicer = harness_with_stub
    tool = GibsonTool(name="t", description="d", harness=harness, tool_name="t")
    tool._run('{"url": "http://example.com"}')
    assert len(servicer.tool_calls) == 1


def test_gibson_tool_run_with_plain_string(harness_with_stub):
    harness, servicer = harness_with_stub
    tool = GibsonTool(name="t", description="d", harness=harness, tool_name="t")
    tool._run("plain string")
    assert len(servicer.tool_calls) == 1


# ---------------------------------------------------------------------------
# GibsonToolRegistry tests
# ---------------------------------------------------------------------------


def test_gibson_tool_registry_list_empty(harness_with_stub):
    harness, _ = harness_with_stub
    registry = GibsonToolRegistry(harness)
    tools = registry.list()
    assert isinstance(tools, list)


def test_gibson_tool_registry_calls_list_tools(harness_with_stub):
    harness, servicer = harness_with_stub
    registry = GibsonToolRegistry(harness)
    registry.list()
    assert servicer.list_tools_calls == 1


# ---------------------------------------------------------------------------
# GibsonLLM tests
# ---------------------------------------------------------------------------


def test_gibson_llm_type(harness_with_stub):
    harness, _ = harness_with_stub
    llm = GibsonLLM(harness=harness)
    assert llm._llm_type == "gibson"


def test_gibson_llm_invoke_returns_ai_message(harness_with_stub):
    from langchain_core.messages import AIMessage

    harness, _ = harness_with_stub
    llm = GibsonLLM(harness=harness)
    result = llm.invoke([HumanMessage(content="hello")])
    assert isinstance(result, AIMessage)
    assert result.content == "LangChain response"


def test_gibson_llm_sends_messages_to_harness(harness_with_stub):
    harness, servicer = harness_with_stub
    llm = GibsonLLM(harness=harness)
    llm.invoke([HumanMessage(content="test message")])
    assert len(servicer.llm_calls) == 1
    assert servicer.llm_calls[0].messages[0].content == "test message"


def test_gibson_llm_system_message_role(harness_with_stub):
    from langchain_core.messages import SystemMessage

    harness, servicer = harness_with_stub
    llm = GibsonLLM(harness=harness)
    llm.invoke([SystemMessage(content="system"), HumanMessage(content="user")])
    messages = servicer.llm_calls[0].messages
    assert messages[0].role == "system"
    assert messages[1].role == "user"


# ---------------------------------------------------------------------------
# GibsonCallbackHandler tests
# ---------------------------------------------------------------------------


def test_callback_handler_counts_llm_calls(harness_with_stub):
    from uuid import uuid4


    harness, servicer = harness_with_stub
    handler = GibsonCallbackHandler(harness)
    run_id = uuid4()
    handler.on_llm_start({}, ["prompt"], run_id=run_id)
    handler.on_llm_start({}, ["prompt2"], run_id=run_id)
    assert handler.llm_call_count == 2


def test_callback_handler_records_to_memory(harness_with_stub):
    from uuid import uuid4

    harness, servicer = harness_with_stub
    handler = GibsonCallbackHandler(harness)
    handler.on_llm_start({}, ["hello"], run_id=uuid4())
    assert len(servicer.memory_sets) == 1
    assert "_lc_llm_call_1" in servicer.memory_sets[0].key


def test_callback_handler_llm_end_counts_tokens(harness_with_stub):
    from uuid import uuid4

    from langchain_core.outputs import Generation, LLMResult

    harness, _ = harness_with_stub
    handler = GibsonCallbackHandler(harness)
    result = LLMResult(generations=[[Generation(text="hello world foo bar")]])
    handler.on_llm_end(result, run_id=uuid4())
    assert handler.token_count == 4
