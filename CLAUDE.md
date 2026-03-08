# agent-claude

A Claude Code skill (`/prototype`) that helps founders go from idea to working AI prototype. It interviews you, writes a PRD, then generates a working project built on Claude's API or Agent SDK — with best-practice patterns baked in. Run it again to iterate based on user feedback.

This repo is a take-home submission for the Claude Evangelist (Startups) role at Anthropic.

---

## What We're Building

### Deliverable 1: Technical Artifact
A GitHub repo containing:
1. The `/prototype` skill — a `SKILL.md` installable in Claude Code
2. A walkthrough example showing the full flow: interview → PRD → generated code → iteration
3. A blog-post-style README explaining what it does, why it matters, and walking through the example

### Deliverable 2: Founder Email
A Google Doc with an email to the YC W26 batch (~200 companies, 2-4 person technical teams, 60% building AI products), linking to this repo.

---

## The Assignment Brief

**Role:** Claude Evangelist for Startups at Anthropic
**Scenario:** YC W26 batch just kicked off. ~200 companies, most 2-4 person technical teams actively deciding which AI platform to build on. Many have experimented with OpenAI, Gemini, and Claude but are not yet Anthropic customers.
**Task:** Send the batch an introductory email that gets them building on Claude, backed by a technical resource you've created.

**Deliverable 1 — Technical Artifact:**
- Create a technical resource that would get a startup founder excited about building on Claude
- Could be a blog post with working code samples, a repo with a tutorial-style README, a video tutorial, or something else entirely
- Built on: Claude API or Claude Agent SDK
- Use case: Your choice. Pick something relevant to early-stage teams.

**Deliverable 2 — Founder Email:**
- Write the email you would send to the YC W26 batch
- Should reference the technical artifact
- Format: Google Doc with subject line and body

**Logistics:**
- Open book, can use AI for research and collaborate
- They want to read the take-home in your writing and communication style
- $25 API credits on console.anthropic.com
- Submit via Greenhouse

**Reference materials provided:**
- Anthropic Engineering Blog: https://www.anthropic.com/engineering
- Anthropic YouTube: https://www.youtube.com/@anthropic-ai
- Claude API Docs: https://platform.claude.com/docs/en/home
- Anthropic GitHub: https://github.com/anthropics
- X accounts: @trq212, @bcherny, @alexalbert__

---

## How /prototype Works

### Flow

```
Founder runs /prototype
    → Discovery Interview (what are you building? what does the AI do? who are your users?)
    → PRD Generation (product_requirements.md with architecture decision, tools, model config, cost estimate)
    → Code Generation (working project using Claude API or Agent SDK, with best-practice patterns)
    → Iteration (founder learns from users, runs /prototype again, PRD and code update)
```

### What Makes It Opinionated (Not Just "Ask Claude to Code")

The skill enforces best practices from Anthropic's own documentation:

1. **Right surface for the job.** Follows Anthropic's decision tree: single API call vs workflow vs Claude API agent vs Agent SDK.
2. **Tool Runner or Agent SDK, not manual loops.** `@beta_tool` in Python, `betaZodTool` in TS for Claude API path. `ClaudeSDKClient` for Agent SDK path.
3. **Adaptive thinking.** `thinking: {type: "adaptive"}` on Opus/Sonnet 4.6 — not `budget_tokens` (deprecated).
4. **Effort control.** `output_config: {effort: "low"|"medium"|"high"}` to control cost per task.
5. **Structured outputs.** `output_config: {format: {...}}` with strict JSON schemas for data extraction.
6. **Streaming by default.** `.stream()` + `.get_final_message()` for anything with long I/O.
7. **Server-side tools.** `web_search_20260209`, `web_fetch_20260209`, `code_execution_20260120` where appropriate.
8. **SDK types.** `Anthropic.MessageParam`, `Anthropic.Tool` etc. — not hand-rolled types.
9. **Cost estimate.** Every generated project includes a cost breakdown.

### Surface Selection

| Use Case | Surface |
|----------|---------|
| Single LLM call (classify, extract, summarise) | Claude API |
| Multi-step pipeline, code-controlled logic | Claude API + tool use |
| Custom agent with your own domain tools | Claude API + tool runner |
| Agent needing file/web/terminal access | Agent SDK |
| Agent needing MCP integrations | Agent SDK |

### Language Detection

Detects from project files (same as Anthropic's `/claude-api` skill):
- `*.py`, `pyproject.toml` → Python
- `*.ts`, `package.json` → TypeScript
- `*.go`, `go.mod` → Go
- `*.java`, `pom.xml` → Java
- `*.rb`, `Gemfile` → Ruby
- No project files → ask, default Python

### Tool Runner & Agent SDK by Language

| Language | Tool Runner | Agent SDK |
|----------|------------|-----------|
| Python | Yes (`@beta_tool`) | Yes |
| TypeScript | Yes (`betaZodTool` + Zod) | Yes |
| Java | Yes (annotated classes) | No |
| Go | Yes (`BetaToolRunner`) | No |
| Ruby | Yes (`BaseTool`) | No |
| C#, PHP | No (manual loop) | No |

### Relationship to `/claude-api` Skill

`/prototype` complements Anthropic's `/claude-api` skill — doesn't duplicate it.
- `/claude-api` = "how to write Claude API code correctly"
- `/prototype` = "what to build and why" → interview, PRD, architecture decision, scaffold, iteration

The SKILL.md should check if `/claude-api` is installed and reference it if available.

---

## Anthropic API Quick Reference (for code generation)

### Current Models (as of Feb 2026)

| Model | ID | Context | Input $/1M | Output $/1M |
|-------|-----|---------|-----------|------------|
| Opus 4.6 | `claude-opus-4-6` | 200K (1M beta) | $5.00 | $25.00 |
| Sonnet 4.6 | `claude-sonnet-4-6` | 200K (1M beta) | $3.00 | $15.00 |
| Haiku 4.5 | `claude-haiku-4-5` | 200K | $1.00 | $5.00 |

### Thinking & Effort
- Opus 4.6 / Sonnet 4.6: Use `thinking: {type: "adaptive"}`. Do NOT use `budget_tokens` (deprecated).
- Effort: `output_config: {effort: "low"|"medium"|"high"|"max"}` (max is Opus 4.6 only). Default is high.
- Older models (if explicitly requested): `thinking: {type: "enabled", budget_tokens: N}`.

### Structured Outputs
- Use `output_config: {format: {...}}` — NOT the deprecated `output_format` parameter.
- Use `client.messages.parse()` for automatic validation.

### Tool Use — Tool Runner (Recommended)
```python
# Python
from anthropic import beta_tool

@beta_tool
def my_tool(param: str) -> str:
    """Description."""
    return result

for message in client.beta.messages.tool_runner(
    model="claude-opus-4-6",
    max_tokens=4096,
    tools=[my_tool],
    messages=[{"role": "user", "content": "..."}],
):
    print(message)
```

### Tool Use — Manual Loop (when you need fine-grained control)
```python
while True:
    response = client.messages.create(model=..., tools=..., messages=messages)
    if response.stop_reason == "end_turn":
        break
    if response.stop_reason == "pause_turn":
        messages = [{"role": "user", "content": user_query}, {"role": "assistant", "content": response.content}]
        continue
    tool_use_blocks = [b for b in response.content if b.type == "tool_use"]
    messages.append({"role": "assistant", "content": response.content})
    tool_results = [{"type": "tool_result", "tool_use_id": t.id, "content": execute(t.name, t.input)} for t in tool_use_blocks]
    messages.append({"role": "user", "content": tool_results})
```

### Server-Side Tools
```python
# Web search + fetch (with dynamic filtering, Opus/Sonnet 4.6)
tools = [
    {"type": "web_search_20260209", "name": "web_search"},
    {"type": "web_fetch_20260209", "name": "web_fetch"},
]

# Code execution (free when paired with web search)
tools.append({"type": "code_execution_20260120", "name": "code_execution"})
```

### Agent SDK (Python)
```python
from claude_agent_sdk import query, ClaudeAgentOptions, ResultMessage

async for message in query(
    prompt="...",
    options=ClaudeAgentOptions(
        allowed_tools=["Read", "Glob", "Grep", "WebSearch"],
        permission_mode="acceptEdits",
    )
):
    if isinstance(message, ResultMessage):
        print(message.result)
```

### Agent SDK — Custom Tools (Python)
```python
from claude_agent_sdk import tool, create_sdk_mcp_server, ClaudeSDKClient, ClaudeAgentOptions

@tool("my_tool", "Description", {"param": str})
async def my_tool(args):
    return {"content": [{"type": "text", "text": f"Result: {args['param']}"}]}

server = create_sdk_mcp_server("my-tools", tools=[my_tool])
options = ClaudeAgentOptions(mcp_servers={"tools": server})

async with ClaudeSDKClient(options=options) as client:
    await client.query("Do the thing")
    async for msg in client.receive_response():
        print(msg)
```

### Common Pitfalls
- Don't use `budget_tokens` on Opus 4.6 / Sonnet 4.6 — use adaptive thinking
- Don't use `output_format` — use `output_config: {format: {...}}`
- Don't reimplement SDK functionality — use `.get_final_message()`, typed exceptions, SDK types
- Don't define custom types for SDK data structures — use `Anthropic.MessageParam`, `Anthropic.Tool`, etc.
- Use streaming for anything with long I/O to prevent HTTP timeouts
- Always parse tool input JSON with `json.loads()` / `JSON.parse()`, never string-match

---

## Repo Structure

```
agent-claude/
├── CLAUDE.md                    ← This file
├── .gitignore
├── .plan/                       ← Private planning docs (gitignored)
│   ├── brief.md                 ← The assignment email
│   ├── plan.md                  ← Full implementation plan
│   ├── risks.md                 ← Risk audit
│   └── cal_call_intel.md        ← Key intel from HM screen
├── skill/
│   └── SKILL.md                 ← The /prototype skill
├── examples/
│   └── sales-research-agent/    ← Pre-generated, hand-verified example
│       ├── agent.py
│       ├── tools.py
│       ├── schemas.py
│       ├── config.py
│       ├── product_requirements.md
│       ├── requirements.txt
│       ├── .env.example
│       └── README.md
└── README.md                    ← Blog-post-style README (the main content)
```

---

## Key Intel from HM Screen (Cal Rueb)

- **Role:** Brand new. Hiring one SF + one EMEA. Sits under Applied AI (startups).
- **Mission:** "Win Day Zero founders" — every founding team's first API key should be Anthropic.
- **Claude Code is the hook, API is where scale lives.** The flywheel between them is the key insight. Cal confirmed Anthropic literally shipped a skill for this (`/claude-api`) the day before the call.
- **Discoverability is Claude Code's biggest problem.** "A lot of features are hidden away." Content should surface hidden power.
- **Cal's priorities:** Agent architecture, safety, UI/UX are the real complexity — not the API itself. APIs are simple.
- **What landed in the call:** The Claude Code → API flywheel idea ("that is a very sharp point"), the technical comms narrative, the MCP apps workshop idea.

---

## Writing Style Notes

The email and README must be in Lamis's voice:
- Plain, confident, fact-dense. State what you did, move on.
- Start sentences with "I" freely. No corporate buzzwords.
- British English. Sparing em dashes.
- Let proof points speak — don't editorialize after them.
- Builder talking to builders, not salesperson to prospects.

---

## Execution Plan

1. **Build the SKILL.md** — interview framework, PRD template, code generation rules, API guidance
2. **Test end-to-end** — run `/prototype`, verify generated PRD and code
3. **Build the example** — run the sales research agent scenario, hand-verify the output, make it standalone
4. **Write the README** — blog-post style, walkthrough-driven, under 2000 words
5. **Write the email** — under 300 words, link to repo, specific CTA
6. **Polish & submit** — test from clean clone, fresh-eyes review
