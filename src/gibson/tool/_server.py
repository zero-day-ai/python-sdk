"""gRPC ToolService servicer wrapping a BaseTool instance."""

from __future__ import annotations

import json
import logging

import grpc
from pydantic import ValidationError

from gibson.common.v1 import gibson_common_pb2
from gibson.tool._base import BaseTool
from gibson.tool.v1 import tool_pb2, tool_pb2_grpc

logger = logging.getLogger(__name__)


class ToolServicer(tool_pb2_grpc.ToolServiceServicer):
    """gRPC servicer that hosts a single ``BaseTool`` instance."""

    def __init__(self, tool: BaseTool) -> None:
        self._tool = tool

    def GetDescriptor(
        self,
        request: tool_pb2.GetDescriptorRequest,
        context: grpc.ServicerContext,
    ) -> tool_pb2.GetDescriptorResponse:
        return tool_pb2.GetDescriptorResponse(
            name=self._tool.name,
            description=self._tool.description,
            version=self._tool.version,
            tags=list(self._tool.tags),
            input_schema=gibson_common_pb2.JSONSchema(json=self._tool.input_schema_json()),
            output_schema=gibson_common_pb2.JSONSchema(json=self._tool.output_schema_json()),
        )

    def Execute(
        self,
        request: tool_pb2.ExecuteRequest,
        context: grpc.ServicerContext,
    ) -> tool_pb2.ExecuteResponse:
        try:
            raw = json.loads(request.input_json)
        except json.JSONDecodeError as exc:
            return tool_pb2.ExecuteResponse(
                error=gibson_common_pb2.Error(
                    code="INVALID_ARGUMENT",
                    message=f"input_json is not valid JSON: {exc}",
                )
            )

        try:
            validated = self._tool.InputModel.model_validate(raw)
        except ValidationError as exc:
            return tool_pb2.ExecuteResponse(
                error=gibson_common_pb2.Error(
                    code="INVALID_ARGUMENT",
                    message=str(exc),
                )
            )

        try:
            result = self._tool.execute(validated)
        except Exception as exc:  # noqa: BLE001
            logger.exception("tool %s execute failed", self._tool.name)
            return tool_pb2.ExecuteResponse(
                error=gibson_common_pb2.Error(
                    code="INTERNAL",
                    message=str(exc),
                    retryable=False,
                )
            )

        return tool_pb2.ExecuteResponse(
            output_json=result.model_dump_json()
        )

    def Health(
        self,
        request: tool_pb2.HealthRequest,
        context: grpc.ServicerContext,
    ) -> tool_pb2.HealthResponse:
        status = self._tool.health()
        return tool_pb2.HealthResponse(
            status=gibson_common_pb2.HealthStatus(status=status)
        )

    def StreamExecute(
        self,
        request_iterator,
        context: grpc.ServicerContext,
    ):
        """Streaming execute — receives a ToolStartRequest, yields ToolComplete.

        Full streaming with ToolProgress/ToolPartialResult is out of scope for
        v1; this implementation satisfies the proto contract by yielding a
        single ToolComplete response.
        """
        start_req: tool_pb2.ToolStartRequest | None = None
        for req in request_iterator:
            if req.HasField("start"):
                start_req = req.start
                break
            if req.HasField("cancel"):
                return

        if start_req is None:
            yield tool_pb2.StreamExecuteResponse(
                error=tool_pb2.ToolError(
                    error=gibson_common_pb2.Error(
                        code="INVALID_ARGUMENT",
                        message="expected ToolStartRequest as first message",
                    ),
                    fatal=True,
                )
            )
            return

        execute_req = tool_pb2.ExecuteRequest(
            input_json=start_req.input_json,
            timeout_ms=start_req.timeout_ms,
        )
        resp = self.Execute(execute_req, context)

        if resp.HasField("error") and resp.error.code:
            yield tool_pb2.StreamExecuteResponse(
                error=tool_pb2.ToolError(error=resp.error, fatal=True)
            )
        else:
            yield tool_pb2.StreamExecuteResponse(
                complete=tool_pb2.ToolComplete(output_json=resp.output_json)
            )
