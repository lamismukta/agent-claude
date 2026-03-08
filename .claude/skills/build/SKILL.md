---
name: build
description: "Generate a working AI prototype from a product requirements doc (PRD). Reads product_requirements.md and produces a complete, runnable project using Claude API or Agent SDK. Use when a user has a PRD or spec and wants working code, when /brainstorm has just completed, or when someone says 'build it', 'generate the code', or 'make it work'. Also use after /prototype runs the brainstorm phase. Works alongside the /claude-api skill for correct API patterns."
---

# /build — PRD → Working Prototype

Read the product requirements doc and generate a complete, runnable project that uses Claude's API or Agent SDK. The output should work out of the box — a founder should be able to clone, install, and run it.

## How It Works

1. **Find the PRD.** Look for `product_requirements.md` in the current directory. If it doesn't exist, tell the user to run `/brainstorm` first, or ask them to describe what they want (and write a minimal PRD before building).

2. **Pick the right surface.** Based on what the PRD describes, choose the simplest architecture that works:

   | What the PRD describes | Build with |
   |------------------------|-----------|
   | Single task (classify, summarise, extract) | Claude API — one call |
   | Multi-step pipeline with fixed logic | Claude API + tool use |
   | Open-ended agent that makes decisions | Claude API + tool use (agentic loop) |
   | Agent that needs file/web/terminal access | Agent SDK |

   Start simple. A multi-step workflow doesn't need the Agent SDK. An agent that just calls two APIs doesn't need file system access. Only reach for heavier tools when the task genuinely requires them.

3. **Generate the project.** Create a complete project structure that runs with a single command. Always include:
   - A clear entry point (`main.py`, `app.py`, or equivalent)
   - A `pyproject.toml` (Python) or `package.json` (TypeScript) with all dependencies declared
   - A `README.md` with a one-liner to run: `uv run main.py` or `npx tsx main.ts`
   - A `.env.example` with required environment variables (never include real keys)
   - Working code that runs end-to-end

4. **Verify it works.** After generating, try to run or at least lint the code. Fix any import errors, missing dependencies, or obvious bugs before presenting it to the user.

## Project Structure

Generate a clean, minimal project. The goal: clone, set API key, run one command.

### Python (default)

```
project-name/
├── README.md              ← "uv run main.py" is the first line
├── pyproject.toml         ← Dependencies + inline script metadata
├── .env.example           ← ANTHROPIC_API_KEY=your-key-here
├── main.py                ← Entry point
├── [modules as needed]    ← Only if genuinely complex enough to split
└── product_requirements.md ← Copy of the PRD (for reference)
```

Always generate a `pyproject.toml` — it lets `uv run` install dependencies automatically:

```toml
[project]
name = "project-name"
version = "0.1.0"
description = "One-line description from the PRD"
requires-python = ">=3.11"
dependencies = [
    "anthropic",
]

[project.scripts]
project-name = "main:main"
```

The README should start with:
```markdown
## Quick Start

```bash
export ANTHROPIC_API_KEY=your-key
uv run main.py [args]
```

No `uv`? Use `pip install -r requirements.txt && python main.py` instead.
```

Also generate a `requirements.txt` as a fallback for founders who don't have `uv`.

### TypeScript

```
project-name/
├── README.md
├── package.json           ← Dependencies
├── .env.example
├── main.ts                ← Entry point
└── product_requirements.md
```

README should show: `npx tsx main.ts [args]`

## Code Guidelines

These aren't arbitrary rules — they prevent the most common problems founders hit when prototyping with Claude's API.

### Model and Configuration

- Default to `claude-sonnet-4-6` for prototypes. It's fast, cheap, and good enough for most tasks. Note in a comment where to upgrade to `claude-opus-4-6` if quality matters more than speed.
- Use adaptive thinking for anything that requires reasoning: `thinking={"type": "adaptive"}`.
- Stream responses when `max_tokens` is high or the task might take a while. Use `.stream()` with `.get_final_message()`.

### Tool Use

When the PRD requires tools, use the Tool Runner pattern — it handles the agentic loop automatically:

**Python:**
```python
from anthropic import Anthropic, beta_tool

client = Anthropic()

@beta_tool
def search_web(query: str) -> str:
    """Search the web for information."""
    # implementation
    return results

response = client.beta.messages.tool_runner(
    model="claude-sonnet-4-6",
    max_tokens=4096,
    tools=[search_web],
    messages=[{"role": "user", "content": prompt}],
)
```

**TypeScript:**
```typescript
import Anthropic from "@anthropic-ai/sdk";
import { betaZodTool } from "@anthropic-ai/sdk/helpers/tools";
import { z } from "zod";

const client = new Anthropic();

const searchWeb = betaZodTool({
  name: "search_web",
  description: "Search the web for information.",
  schema: z.object({ query: z.string() }),
  execute: async ({ query }) => {
    // implementation
    return results;
  },
});

const response = await client.beta.messages.tool_runner({
  model: "claude-sonnet-4-6",
  max_tokens: 4096,
  tools: [searchWeb],
  messages: [{ role: "user", content: prompt }],
});
```

If the project needs web search or code execution, use server-side tools — they're free with the API:
```python
tools = [
    {"type": "web_search_20260209", "name": "web_search"},
    {"type": "code_execution_20260120", "name": "code_execution"},
]
```

### Agent SDK

When the PRD calls for an agent with file, web, or terminal access:

```python
from claude_agent_sdk import query, ClaudeAgentOptions, ResultMessage

async for message in query(
    prompt="Your task here",
    options=ClaudeAgentOptions(
        allowed_tools=["Read", "Glob", "Grep", "WebSearch", "Bash"],
        permission_mode="acceptEdits",
    )
):
    if isinstance(message, ResultMessage):
        print(message.result)
```

### Structured Output

When the PRD specifies structured output (JSON schemas, typed responses):
```python
response = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=4096,
    messages=[{"role": "user", "content": prompt}],
    output_config={
        "format": {
            "type": "json_schema",
            "json_schema": your_schema,
        }
    },
)
```

### Common Pitfalls to Avoid

- Don't use `budget_tokens` on Opus/Sonnet 4.6 — use adaptive thinking instead
- Don't use `output_format` — it's deprecated; use `output_config: {format: {...}}`
- Don't build a manual tool-use loop when Tool Runner exists
- Don't hardcode API keys — always use environment variables
- Parse tool input with `json.loads()`, never string-match

## Iteration Mode

When the PRD has `[UPDATED]` tags (from `/brainstorm` iteration mode):

1. Read the existing project code alongside the updated PRD.
2. Modify only what changed — don't regenerate from scratch.
3. If the architecture needs to change (e.g., adding tools to what was a single API call), explain the change to the user before making it.

## Language Detection

Check the current directory for existing project files to match the founder's preferred language:
- `*.py`, `requirements.txt` → Python
- `*.ts`, `package.json` → TypeScript
- No existing files → default to Python, mention TypeScript is also supported

## What This Skill Does NOT Do

- It doesn't deploy anything. The output is local, runnable code.
- It doesn't write tests (that's in the ideas backlog).
- It doesn't manage infrastructure, databases, or hosting.
- The goal is a working prototype, not production code. Favour clarity over robustness.
