---
name: build
description: "Generate a working AI prototype from a product requirements doc (PRD). Reads product_requirements.md and produces a complete, runnable project using Claude API or Agent SDK. Use when a user has a PRD or spec and wants working code, when /brainstorm has just completed, or when someone says 'build it', 'generate the code', or 'make it work'. Also use after /sprint runs the brainstorm phase. Works alongside the /claude-api skill for correct API patterns."
---

# /build — PRD → Working Prototype

Read the product requirements doc and generate a complete, runnable project that uses Claude's API or Agent SDK. The output should work out of the box — a founder should be able to clone, install, and run it.

## How It Works

1. **Find the PRD.** Look for `product_requirements.md` in the current directory. If it doesn't exist, tell the user to run `/brainstorm` first, or ask them to describe what they want (and write a minimal PRD before building).

2. **Pick the right surface.** Choose the simplest architecture that fits the PRD. Start with a single Claude API call and only add complexity when the task genuinely requires it — tool use when the model needs to take actions, an agentic loop when it needs to make decisions across multiple steps, the Agent SDK only when it needs file, web, or terminal access. If you're unsure, go simpler: a single well-prompted API call solves more than most founders expect.

   **Confirm before generating.** Tell the founder: "Based on the PRD, I'm going to build this as [architecture] using [model]. Here's why: [one sentence]. Sound right?" Wait for confirmation. This is fast to say and prevents wasted builds.

3. **Generate the project.** Create a complete project structure that runs with a single command. Always include:
   - A clear entry point — name it after what it does (e.g., `briefing.py`, `triage.py`, `extract.py`). Use `main.py` only if no descriptive name fits.
   - A `pyproject.toml` (Python) or `package.json` (TypeScript) with all dependencies declared
   - A `README.md` with a one-liner to run: `uv run <entry_point>.py` or `npx tsx <entry_point>.ts`
   - A `.env.example` with required environment variables (never include real keys)
   - Working code that runs end-to-end

4. **Verify it works.** After generating, run the prototype yourself — don't wait to be asked. This is not optional. Do it proactively, every time.

   **Create synthetic test data first.** Don't wait for the founder to provide real data. Generate realistic sample inputs yourself — a CSV, a JSON file, a sample document, whatever the prototype expects — and run against that. The goal is to verify the code works and that the AI output looks sensible, not to validate with production data.

   - If `uv` is available: `uv run <entry_point>.py` (uv installs deps automatically)
   - If `uv` is not available or pip fails (e.g., "externally managed environment" error): create a venv:
     ```bash
     python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
     .venv/bin/python <entry_point>.py [test args]
     ```
   - Fix any import errors, missing dependencies, or syntax issues before presenting.
   - Test as much as possible without an API key (CLI help, input validation, file parsing). Then test the AI calls if `ANTHROPIC_API_KEY` is in the environment.
   - Report what you tested and what the output looked like. "I ran it against a sample CSV with 5 transactions — Claude categorized 4 correctly and flagged 1 for review" is useful. "It runs" is not.

   **Never ask the founder to paste their API key into the chat.** If a live key is needed and not in the environment, tell them: "Run `export ANTHROPIC_API_KEY=sk-ant-...` in your terminal, then run [command]." Do not solicit the key in conversation.

5. **Hand off with clear instructions.** After the code is generated, present the founder with everything they need:

   ```
   ## Your prototype is ready.

   ### Run it
   [exact command — copy-pasteable, e.g.:]
   export ANTHROPIC_API_KEY=your-key
   uv run briefing.py "Sarah Chen" "Sequoia Capital"

   [fallback for non-uv users:]
   pip install -r requirements.txt
   python briefing.py "Sarah Chen" "Sequoia Capital"

   ### What it does
   [1-2 sentences — input, output, what happens in between]

   ### What to look for
   [2-3 specific things to evaluate, tied to the hypothesis under test]

   ### Files generated
   [List every file with a one-line description]
   ```

   Don't assume they'll read the generated README. Give them the run command right here in the conversation. The prototype is useless if they can't run it in 30 seconds.

## Project Structure

Generate a clean, minimal project. The goal: clone, set API key, run one command.

### Python (default)

```
project-name/
├── README.md              ← "uv run <entry_point>.py" is the first line
├── pyproject.toml         ← Dependencies + inline script metadata
├── .env.example           ← ANTHROPIC_API_KEY=your-key-here
├── <entry_point>.py       ← Named after what it does (e.g., briefing.py, triage.py)
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
uv run <entry_point>.py [args]
```

No `uv`? Use `pip install -r requirements.txt && python <entry_point>.py` instead.
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

**Important:** Server-side web search requires Sonnet 4.6 or Opus 4.6 — Haiku does not support it. If the prototype uses web search, default to Sonnet 4.6 (not Haiku).

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
