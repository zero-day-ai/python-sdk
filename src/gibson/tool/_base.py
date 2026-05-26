"""BaseTool ABC for class-based Gibson tool authoring."""

from __future__ import annotations

import json
from abc import ABC, abstractmethod
from typing import ClassVar

from pydantic import BaseModel


class BaseTool(ABC):
    """Abstract base class for Gibson tools.

    Subclasses define ``InputModel`` and ``OutputModel`` as Pydantic
    ``BaseModel`` subclasses, and implement ``execute()``.

    Example::

        class ScanInput(BaseModel):
            url: str
            depth: int = 1

        class ScanOutput(BaseModel):
            findings: list[str]

        class Scanner(BaseTool):
            name = "scanner"
            description = "Scans a URL for issues"
            InputModel = ScanInput
            OutputModel = ScanOutput

            def execute(self, input: ScanInput) -> ScanOutput:
                return ScanOutput(findings=["XSS at /search"])
    """

    name: ClassVar[str]
    description: ClassVar[str]
    version: ClassVar[str] = "0.1.0"
    tags: ClassVar[list[str]] = []

    InputModel: ClassVar[type[BaseModel]]
    OutputModel: ClassVar[type[BaseModel]]

    @abstractmethod
    def execute(self, input: BaseModel) -> BaseModel:
        """Execute the tool with a validated Pydantic input model instance.

        Args:
            input: An instance of ``InputModel`` deserialized from the
                request's ``input_json`` field.

        Returns:
            An instance of ``OutputModel`` to be serialized to
            ``output_json`` in the response.
        """

    def health(self) -> str:
        """Return the tool's health status string (healthy/degraded/unhealthy)."""
        return "healthy"

    def input_schema_json(self) -> str:
        """Return the JSON Schema for the input model as a string."""
        return json.dumps(self.InputModel.model_json_schema())

    def output_schema_json(self) -> str:
        """Return the JSON Schema for the output model as a string."""
        return json.dumps(self.OutputModel.model_json_schema())
