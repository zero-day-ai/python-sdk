"""Scaffold templates for new tools and agents."""

from __future__ import annotations

TOOL_TEMPLATE = '''\
"""Gibson tool: {name}."""

from __future__ import annotations

from pydantic import BaseModel

from gibson.tool import tool


class {class_name}Input(BaseModel):
    # TODO: define your input fields
    value: str


class {class_name}Output(BaseModel):
    # TODO: define your output fields
    result: str


@tool
def {name}(input: {class_name}Input) -> {class_name}Output:
    """{description}"""
    # TODO: implement your tool logic
    return {class_name}Output(result=input.value)


if __name__ == "__main__":
    from gibson.serve import serve_tool
    serve_tool({name})
'''

AGENT_TEMPLATE = '''\
"""Gibson agent: {name}."""

from __future__ import annotations

from gibson.agent import BaseAgent, Result, Task
from gibson.harness import Harness


class {class_name}(BaseAgent):
    name = "{name}"
    description = "{description}"

    def execute_sync(self, harness: Harness, task: Task) -> Result:
        # TODO: implement your agent logic
        response = harness.llm.complete([
            {{"role": "user", "content": task.goal}},
        ])
        return Result.success(output=response.content)


{var_name} = {class_name}()


if __name__ == "__main__":
    from gibson.serve import serve_agent
    serve_agent({var_name})
'''


def _class_name(name: str) -> str:
    return "".join(part.capitalize() for part in name.replace("-", "_").split("_"))


def scaffold_tool(name: str) -> str:
    return TOOL_TEMPLATE.format(
        name=name,
        class_name=_class_name(name),
        description=f"A Gibson tool named {name}.",
    )


def scaffold_agent(name: str) -> str:
    return AGENT_TEMPLATE.format(
        name=name,
        class_name=_class_name(name),
        description=f"A Gibson agent named {name}.",
        var_name=name.replace("-", "_"),
    )
