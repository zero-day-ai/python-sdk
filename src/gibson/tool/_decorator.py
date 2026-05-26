"""@tool decorator for function-based Gibson tool authoring."""

from __future__ import annotations

import inspect
from collections.abc import Callable
from typing import get_type_hints

from pydantic import BaseModel

from gibson.tool._base import BaseTool


def tool(
    fn: Callable | None = None,
    *,
    name: str | None = None,
    description: str | None = None,
    version: str = "0.1.0",
    tags: list[str] | None = None,
) -> BaseTool | Callable[[Callable], BaseTool]:
    """Decorate a function as a Gibson tool.

    The decorated function must:
    - Accept a single argument typed as a ``pydantic.BaseModel`` subclass.
    - Return a ``pydantic.BaseModel`` subclass instance.

    Can be used with or without arguments::

        @tool
        def scan(input: ScanInput) -> ScanOutput:
            ...

        @tool(name="scanner", tags=["recon"])
        def scan(input: ScanInput) -> ScanOutput:
            ...

    Args:
        fn: The function to wrap (when used without parentheses).
        name: Tool name; defaults to the function name.
        description: Tool description; defaults to the function docstring.
        version: Semantic version string; defaults to ``"0.1.0"``.
        tags: Optional list of categorization tags.

    Returns:
        A ``BaseTool`` instance wrapping the function.
    """

    def decorator(func: Callable) -> BaseTool:
        hints = get_type_hints(func)
        params = list(inspect.signature(func).parameters.values())

        if not params:
            raise TypeError(
                f"@tool function '{func.__name__}' must accept an input parameter typed "
                "as a pydantic.BaseModel subclass"
            )

        input_type = hints.get(params[0].name)
        output_type = hints.get("return")

        if input_type is None or not (
            isinstance(input_type, type) and issubclass(input_type, BaseModel)
        ):
            raise TypeError(
                f"@tool function '{func.__name__}' first parameter must be typed as "
                f"a pydantic.BaseModel subclass, got {input_type!r}"
            )

        if output_type is None or not (
            isinstance(output_type, type) and issubclass(output_type, BaseModel)
        ):
            raise TypeError(
                f"@tool function '{func.__name__}' return type must be a "
                f"pydantic.BaseModel subclass, got {output_type!r}"
            )

        tool_name = name or func.__name__
        tool_description = description or (inspect.getdoc(func) or tool_name)

        _func = func
        _version = version
        _tags = list(tags or [])

        class FunctionTool(BaseTool):
            name = tool_name
            description = tool_description
            version = _version
            tags = _tags
            InputModel = input_type
            OutputModel = output_type

            def execute(self, input: BaseModel) -> BaseModel:
                return _func(input)

        FunctionTool.__name__ = f"FunctionTool({tool_name})"

        return FunctionTool()

    if fn is not None:
        return decorator(fn)
    return decorator
