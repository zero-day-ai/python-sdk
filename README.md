# gibson-sdk

Python SDK for authoring agents, tools, and plugins on the [Gibson](https://github.com/zeroroot-ai) platform.

## Install

```bash
pip install gibson-sdk
```

For LangChain adapter support:

```bash
pip install "gibson-sdk[langchain]"
```

## Quick start — tool

```python
from pydantic import BaseModel
from gibson.tool import tool
from gibson.serve import serve_tool

class ScanInput(BaseModel):
    url: str
    depth: int = 1

class ScanOutput(BaseModel):
    findings: list[str]

@tool(name="scanner", tags=["recon"])
def scan(input: ScanInput) -> ScanOutput:
    """Scan a URL for security issues."""
    return ScanOutput(findings=[f"Found issue at {input.url}"])

if __name__ == "__main__":
    serve_tool(scan)
```

## Quick start — agent

```python
from gibson.agent import BaseAgent
from gibson.harness import Harness
from gibson.types import Task, Result

class MyAgent(BaseAgent):
    name = "my-agent"
    description = "An example agent"

    async def execute(self, harness: Harness, task: Task) -> Result:
        response = await harness.llm.complete_async(task.goal)
        return Result.success(response.text)

if __name__ == "__main__":
    from gibson.serve import serve_agent
    serve_agent(MyAgent())
```

## Configuration

| Variable | Description |
|----------|-------------|
| `GIBSON_ENDPOINT` | Gibson daemon gRPC endpoint (e.g. `daemon.example.com:443`) |
| `GIBSON_TOKEN` | Bearer token for authentication |
| `GIBSON_CLIENT_CERT` | Optional: path to mTLS client certificate |
| `GIBSON_CLIENT_KEY` | Optional: path to mTLS client private key |

## License

Apache 2.0 — see [LICENSE](LICENSE).
