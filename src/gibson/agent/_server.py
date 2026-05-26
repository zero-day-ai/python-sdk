"""gRPC AgentService servicer wrapping a BaseAgent instance."""

from __future__ import annotations

import asyncio
import logging

import grpc

from gibson.agent._base import BaseAgent
from gibson.agent._types import Result, Task
from gibson.agent.v1 import agent_pb2, agent_pb2_grpc
from gibson.common.v1 import gibson_common_pb2

logger = logging.getLogger(__name__)


class AgentServicer(agent_pb2_grpc.AgentServiceServicer):
    """gRPC servicer that hosts a single ``BaseAgent`` instance."""

    def __init__(self, agent: BaseAgent) -> None:
        self._agent = agent

    def GetDescriptor(
        self,
        request: agent_pb2.GetDescriptorRequest,
        context: grpc.ServicerContext,
    ) -> agent_pb2.GetDescriptorResponse:
        target_schemas = [
            agent_pb2.TargetSchemaProto(
                type=ts.type,
                version=ts.version,
                schema_json=ts.schema_json,
                description=ts.description,
            )
            for ts in self._agent.target_schemas()
        ]
        return agent_pb2.GetDescriptorResponse(
            name=self._agent.name,
            version=self._agent.version,
            description=self._agent.description,
            capabilities=list(self._agent.capabilities),
            target_schemas=target_schemas,
        )

    def GetSlotSchema(
        self,
        request: agent_pb2.GetSlotSchemaRequest,
        context: grpc.ServicerContext,
    ) -> agent_pb2.GetSlotSchemaResponse:
        slots = [
            agent_pb2.AgentSlotDefinition(
                name=slot.name,
                description=slot.description,
                required=slot.required,
                default_config=agent_pb2.AgentSlotConfig(
                    provider=slot.provider,
                    model=slot.model,
                ),
            )
            for slot in self._agent.llm_slots()
        ]
        return agent_pb2.GetSlotSchemaResponse(slots=slots)

    def Execute(
        self,
        request: agent_pb2.ExecuteRequest,
        context: grpc.ServicerContext,
    ) -> agent_pb2.ExecuteResponse:
        from gibson.harness._client import Harness  # noqa: PLC0415

        harness = Harness.from_callback(
            endpoint=request.callback_endpoint,
            token=request.callback_token,
            task_id=request.task.id,
            agent_name=self._agent.name,
            trace_id=request.trace_id,
            mission_run_id=request.mission_run_id,
            agent_run_id=request.agent_run_id,
            run_number=request.run_number,
        )

        task = Task.from_proto(request.task)

        try:
            loop = asyncio.new_event_loop()
            try:
                result = loop.run_until_complete(self._agent.execute(harness, task))
            finally:
                loop.close()
        except Exception as exc:  # noqa: BLE001
            logger.exception("agent %s execute failed", self._agent.name)
            result = Result.failure(str(exc))

        return agent_pb2.ExecuteResponse(result=result.to_proto())

    def Health(
        self,
        request: agent_pb2.HealthRequest,
        context: grpc.ServicerContext,
    ) -> agent_pb2.HealthResponse:
        status = self._agent.health()
        return agent_pb2.HealthResponse(
            status=gibson_common_pb2.HealthStatus(status=status)
        )
