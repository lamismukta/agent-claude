---
name: sprint
description: "The main skill. Use any time — starting a new idea, testing a prototype, talking to users, or iterating on what exists. Reads the project context (decision log, hypotheses, call notes) and figures out the right questions to ask. Use when a founder says 'I want to build something', 'I have an idea', 'let's sprint', 'I tested it', 'users said X', 'I had some calls', 'what should I do next', or anything else. Sprint handles it."
---

# /sprint

The only skill you need to run. Works for first builds, iteration, and major rethinks. Reads your project context — decision log, hypotheses, call notes — and figures out where you are and what to do next.

**The founder drives.** Present what you've got at each checkpoint and wait for confirmation before moving on.

---

## Step 0: Read context first

Before saying anything, read:
- `DECISION_LOG.md` — the most important signal. Does it exist? What's the latest entry? What was being built and tested?
- `HYPOTHESES.md` — current status of all assumptions
- `call_notes/` — any user interviews. Read frontmatter first (who, date, context) to prioritise — focus on the most recent and most relevant. Note anything new since the last decision log entry.
- `projects/` — list any existing project folders. For each, read `PRODUCT_REQUIREMENTS.md`.
- `existing_docs/yc-application.md` — foundation context

**If Granola MCP is configured:** Run `list_meetings` and check for meetings since the last saved note. Fetch and save any new ones to `call_notes/` with this frontmatter:
```markdown
---
who: [Name, Role at Company]
date: [YYYY-MM-DD]
context: [User interview / Demo / Intro call, N min]
source: granola
---
```

Then route based on what you find:

---

### No decision log, no hypotheses, no projects

This is a first sprint. Run [Phase 1: Discovery](#phase-1-discovery) from scratch.

Open with:
> "Let's build something. What are you working on?"

Then run the full discovery conversation below.

---

### Decision log exists

Read the latest entry. Understand what was last built and what hypothesis it was testing. Then open with a synthesis — not a question:

> "Last time we [built X / tested H2 / talked to users about Y]. [One sentence on what the evidence showed or what changed.] What's happened since?"

Listen to the answer. Route based on what they say:

- **"I tested it / users said X / it didn't work"** → ask "What mattered most — what worked, what didn't?" then → [Iteration: incorporate feedback](#iteration-incorporate-feedback)
- **"I want to build something new / try a different direction"** → ask if this is a new project or a full rethink, then run [Phase 1: Discovery](#phase-1-discovery)
- **"Nothing, just continuing"** → summarise hypothesis status and ask what they want to tackle next

If new call notes were pulled, surface key insights before asking anything:
> "I also pulled [N] new meeting notes. Here's what stood out: [2-3 key insights]. Does that change anything?"

---

## Phase 1: Discovery

### Read reference material

Before your first discovery conversation, read the reference docs in `references/`:
- `references/user-research-canon.md` — Mom Test, Eric Migicovsky's 5 Questions, Paul Graham's essays on startup ideas. Internalise the principles — don't quote them at the founder.
- `references/mvp-canon.md` — YC MVP frameworks, scoping heuristics, "Hold tightly / Hold loosely" framework. Informs how you scope the prototype in Phase 2.

### Read everything first

Before the discovery conversation, read all existing context:
- `existing_docs/yc-application.md` — problem, user, solution, traction, team
- `existing_docs/` — any other imported docs
- `call_notes/` — read all notes. Extract: **pain points** (what problems?), **workarounds** (how do they solve it today?), **requests** (what did they ask for — dig into the *why*), **surprises** (anything that contradicts assumptions?), **quotes** (verbatim quotes are gold — surface the best ones)
- `HYPOTHESES.md` — if it exists, where do things stand?

### Open with a critique, not a question

Synthesise what you've read, then push back on what's shaky:

> "Here's what I think you're betting on: [problem + core hypothesis in 2-3 sentences]. Here's what I'd push back on: [1-2 things that seem underspecified, risky, or contradicted by call notes]. What resonates? What's wrong?"

This is a critique, not a summary. The founder doesn't need you to reflect what they wrote — they need you to identify what's shaky.

### Discovery conversation

Ask **one question at a time**. Wait for the answer. Never dump a list. Follow threads that reveal risk. The goal: surface the assumption most likely to kill the idea if wrong.

The founder is the **builder**, not always the user. Ask about their users — what they've observed, what users say, what they've seen break. Don't ask the founder how they feel about the product; ask what they've seen their users do.

**Understand the user's pain (past tense beats future tense):**
- "Walk me through a specific user. What does their day look like when this problem hits?"
- "What do your users say is the hardest part?" — what have you actually heard, not what you assume
- "Tell me about the last time a user got stuck or complained. What happened?" — forces real events

Watch for **fluff**: generic claims ("users always..."), hypotheticals ("they might..."), future-tense promises ("they would..."). Redirect: "Tell me about a specific user. When did that last happen?"

**Test if the pain is real:**
- "How are your users solving this today?" — manual, spreadsheet, another tool, not at all?
- "What's broken about that?" — listen for repetitive, error-prone, slow, or embarrassing steps
- "Have any users asked for something like this unprompted?" — strongest signal

If users are already doing this manually with ChatGPT, that's a strong signal — they just need it automated properly.

**Define the user and scope:**
- "Who is the ONE person who needs this most?" — role, technical ability, context
- "How do they trigger this?" — CLI, web form, Slack bot, API call, cron job?
- "What does the output look like?" — text, structured data, file, action taken?
- "What's the simplest version that would actually be useful? What can you cut?" — push for a scope buildable in a day

**Architecture and success:**
- "What should the AI actually *do*?" — list specific capabilities
- "Does it need to make decisions, or just run a fixed pipeline?" — API call vs. workflow vs. agent
- "How much autonomy?" — human-in-the-loop is usually right for v1
- "How will you know this works?" — concrete success criteria from the user's perspective
- "What would make a user stop using this after the first try?" — surfaces deal-breakers early

### Write HYPOTHESES.md

Distil the key assumptions into `HYPOTHESES.md`. Each hypothesis is something that could kill the idea if wrong. Order by risk.

```markdown
# Hypotheses

## H1: [Assumption in plain language]
- **Risk:** [What goes wrong if this is false]
- **Test:** 🗣️ conversation / 🛠️ prototype
- **How:** [Specific test — who to ask, what to build, what result confirms or kills it]
- **Status:** untested

## H2: ...
```

Tag each hypothesis:
- **🗣️ conversation** — validated by talking to users. Good for "do people have this problem?" and "would they switch?"
- **🛠️ prototype** — needs working software to test. Good for "can the AI do this reliably?" and "is the output good enough?"

**Checkpoint:** "Here are the assumptions I think could kill this idea. The riskiest one we can test with software is [H2]. Does this feel right?"

### Write the first decision log entry

Create or append to `DECISION_LOG.md`:

```markdown
## Session — [date]

### Context
[What triggered this session. 1-2 sentences.]

### Hypotheses Tested
- H1: [assumption] → ⏳ untested

### Key Decisions
- [Decision and why]

### What Changed
- [What was written or decided]

### Open Questions
- [Anything unresolved]

---
```

---

## Phase 2: Spec

### Name the project and choose where to build

Ask:
> "Is this a standalone experiment, or an extension of your existing product?"

- **Standalone** — builds in `projects/<name>/`, self-contained, disposable.
- **Extension** — ask for the repo path if not already known. Creates a branch (`experiment/<project-name>`) in that repo and builds there.

**Important:** For extension mode, never write a single line of code in the founder's repo until the PRD is approved. Present the spec, wait for explicit sign-off, then create the branch and build. Nothing touches main at any point — the founder reviews the diff and decides whether to merge or delete.

Suggest a project name:
> "I'll call this `transaction-categorizer`. Good?"

Keep it kebab-case, descriptive of what it does. Wait for confirmation. Then append to `DECISION_LOG.md`:
```
## [date] — Started projects/[name]
Testing [hypothesis] — [one line on what this build does and why]
```

### Write the PRD

Write `projects/<name>/PRODUCT_REQUIREMENTS.md`. Scope it to test the riskiest 🛠️ hypothesis. One page. Buildable in a day.

**Writing principles:**
- Specific over vague. "Extract the 5 key findings and output a markdown list" is buildable. "Summarise the document" is not.
- Name the user. Not "users" — one persona with a role, context, and trigger.
- State what's out of scope. Prevents scope creep during build.

```markdown
# Product Requirements: [Product Name]

## Problem
[1-2 sentences. What problem, for whom. Ground in real behaviour — what do they do today and why is it broken?]

## Why LLM?
- **LLM is good at:** [e.g., "interpreting unstructured text", "making judgment calls on ambiguous input"]
- **LLM is NOT needed for:** [e.g., "storing data", "CRUD operations"]
- **What was impossible before:** [the capability that only exists because of LLMs]

## User
- **Who:** [specific persona — role, technical ability, context]
- **Trigger:** [how they start — CLI, web form, API call, cron job]
- **Output:** [what they get back — text, structured data, file, action taken]

## Core Capabilities
1. [specific enough to implement]
2. ...

## Tools Required
- [Tool] — for [what specifically]

## Architecture
- **Type:** [Single API call / Multi-step workflow / Autonomous agent]
- **Autonomy:** [Fully autonomous / Human-in-the-loop / Suggestions only]
- **Model:** [e.g., "claude-opus-4-6 — default. Downgrade to Sonnet if speed or cost becomes a constraint."]

## Scope
- **In scope:** [what the prototype will do]
- **Out of scope:** [what it won't do]
- **Constraints:** [privacy, rate limits, budget, etc.]

## Hypothesis Under Test
- **Hypothesis:** [copy from HYPOTHESES.md]
- **Confirmed if:** [what outcome proves it]
- **Killed if:** [what outcome disproves it]

## Success Criteria
- [concrete, testable]
```

**Checkpoint:** "Here's what I'm going to build: [one-paragraph summary]. It tests [hypothesis] by [how]. Architecture is [single call / workflow / agent] using [model]. Ready, or should we change anything?"

If they say no: ask what they'd like to change, or whether they want to test something else entirely. Adjust the PRD and re-confirm. Don't build until they're happy with the scope.

---

## Phase 3: Build

**Before writing any code, invoke the `/claude-api` skill.** It provides current API patterns, correct model IDs, and schema requirements. Code written without it will have wrong patterns.

### Step 1: Read the existing codebase (if one exists)

If the founder gave a repo path or the PRD says "extension mode", read their code before writing anything. This is not optional — you cannot integrate with code you haven't read.

**What to read:**
- Entry points — `main.py`, `app.py`, `index.ts`, whatever starts the app
- Package config — `pyproject.toml`, `package.json` — dependencies already available, project structure conventions
- Patterns — how they structure imports, handle errors, name things, configure the app
- Adjacent code — the module or area you're extending. Read the actual files, not just the directory listing.
- Tests — do they exist? What framework? What patterns?

**What to extract:**
- Language and framework (FastAPI? Express? Plain script?)
- How config/env vars are handled (dotenv? pydantic-settings? raw os.environ?)
- Import style (relative? absolute? barrel files?)
- Naming conventions (snake_case functions? camelCase? Classes for everything or plain functions?)
- Where new code should live — which directory, which module

**Then confirm:**
> "I've read through your codebase. You're using [framework] with [pattern]. I'll add [what] in [where], matching your existing style. Sound right?"

If it's a **standalone experiment** with no existing codebase, skip this step entirely — go straight to Step 2.

### Step 2: Detect language and pick architecture

**Language:**
- If there's an existing codebase → match it
- `*.py`, `requirements.txt`, `pyproject.toml` → Python
- `*.ts`, `package.json`, `tsconfig.json` → TypeScript
- No existing files → default to Python, mention TypeScript is also supported

**Architecture — start simple, only add complexity when genuinely required:**
- **Single API call** — one prompt in, one response out. Solves more than expected.
- **Tool use / multi-step** — when the model needs to take actions (web search, file reads)
- **Agentic loop** — when it needs decisions across multiple steps
- **Agent SDK** — only when it needs file, web, or terminal access as a full agent

### Step 3: Write the code

**Standalone mode** — create a complete project in `projects/<name>/`:

```
projects/<name>/
├── README.md              ← see template below
├── pyproject.toml         ← dependencies (uv installs automatically)
├── .env.example           ← ANTHROPIC_API_KEY=your-key-here
├── <entry_point>.py       ← named after what it does (briefing.py, categorizer.py)
└── PRODUCT_REQUIREMENTS.md
```

For TypeScript: `package.json` + `tsconfig.json` instead. README shows: `npx tsx <entry_point>.ts [args]`

**Extension mode** — build into their codebase:
1. Create a branch: `experiment/<project-name>`
2. Add files where they belong in the existing structure — not in a `projects/` folder
3. Match their patterns: same import style, same naming, same error handling
4. Add dependencies to their existing `pyproject.toml` / `package.json` — don't create a separate one
5. If they have tests, write tests in their test framework

**pyproject.toml (standalone only):**
```toml
[project]
name = "project-name"
version = "0.1.0"
requires-python = ">=3.11"
dependencies = ["anthropic"]
```

**README.md template (standalone):**
```markdown
# <Project Name>

<One sentence: what it does and what it tests.>

## Quick Start

​```bash
export ANTHROPIC_API_KEY=your-key
uv run <entry_point>.py
​```

No `uv`? `pip install -r requirements.txt && python <entry_point>.py`

## What It Does

<2-3 sentences on input → process → output.>

## What to Look For

- <Specific thing to evaluate when testing>
- <Another signal to watch>

## Test Results

_Updated after build run._

- **Data used:** [real data from founder / synthetic — describe what]
- **Output:** [quote or summarise what the AI actually produced]
- **Quality:** [honest assessment — what looked right, what was off]
- **Issues fixed during build:** [any errors hit and resolved, or "none"]
```

### Code guidelines

**Defaults:**
- Model: `claude-opus-4-6`. Downgrade to `claude-sonnet-4-6` only if the founder explicitly asks for speed or lower cost.
- Adaptive thinking for reasoning: `thinking={"type": "adaptive"}`
- Stream long responses: `.stream()` with `.get_final_message()`

**Tool use — Tool Runner pattern (Python):**
```python
from anthropic import Anthropic, beta_tool

@beta_tool
def search_web(query: str) -> str:
    """Search the web for information."""
    return results

response = client.beta.messages.tool_runner(
    model="claude-opus-4-6",
    max_tokens=4096,
    tools=[search_web],
    messages=[{"role": "user", "content": prompt}],
)
```

**Tool use — Tool Runner pattern (TypeScript):**
```typescript
import Anthropic from "@anthropic-ai/sdk";
import { betaZodTool } from "@anthropic-ai/sdk/helpers/beta/zod";
import { z } from "zod";

const client = new Anthropic();

const searchWeb = betaZodTool({
  name: "search_web",
  description: "Search the web for information.",
  inputSchema: z.object({ query: z.string() }),
  run: async ({ query }) => {
    // implementation
    return results;
  },
});

const response = await client.beta.messages.toolRunner({
  model: "claude-opus-4-6",
  max_tokens: 4096,
  tools: [searchWeb],
  messages: [{ role: "user", content: prompt }],
});
```

**Server-side tools (free with the API):**
```python
tools = [
    {"type": "web_search_20260209", "name": "web_search"},
    {"type": "code_execution_20260120", "name": "code_execution"},
]
```
Note: web search requires Sonnet 4.6 or Opus 4.6 — Haiku doesn't support it. Structured output (`output_config`) works alongside web search — the schema constraint applies to the final response after all search rounds complete.

**Structured output:**
```python
response = client.messages.create(
    model="claude-opus-4-6",
    max_tokens=4096,
    messages=[{"role": "user", "content": prompt}],
    output_config={"format": {"type": "json_schema", "schema": your_schema}},
    # Schema must have "additionalProperties": False on every object type
)
```

**Agent SDK:**
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

**Pitfalls to avoid:**
- Don't use `budget_tokens` on Opus/Sonnet 4.6 — use adaptive thinking
- Don't use `output_format` — deprecated, use `output_config: {format: {...}}`
- Don't build a manual tool-use loop — Tool Runner exists
- Never hardcode API keys. Never ask the founder to paste a key into chat — say: "Run `export ANTHROPIC_API_KEY=sk-ant-...` in your terminal."

### Step 4: Run it and show the output

This is not optional. Never hand off code you haven't run. The founder should see results, not instructions.

**Get the best test data you can.** What to use depends on what the prototype does:

- **Prototype processes input** (categoriser, analyser, summariser) — ask for real data: "Do you have any real data we can test against? Even a small sample: a few call notes, a CSV export, a real document." Real data catches problems synthetic data won't, and gives the founder a result they can actually evaluate.
- **Prototype generates output** (suggestion engine, content generator, research tool) — generate realistic synthetic input that mirrors what real users would provide. Still ask: "I'll test with sample data — do you have anything real I should use instead?"
- **Check the decision log for user data.** If onboard noted analytics, usage logs, or exports, use those — they're the best signal available.

If no real data is available, generate realistic synthetic data that mirrors the expected structure — not placeholder lorem ipsum.

**Run it:**
```bash
uv run <entry_point>.py [test args]
# or if uv unavailable:
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
.venv/bin/python <entry_point>.py [test args]
```

**Fix every error before moving on.** Common failures:
- `400 invalid_request_error` — schema issue. Check: `additionalProperties: false` on every object, no `minimum`/`maximum` on integers.
- `401` — API key not set. Remind the founder: `export ANTHROPIC_API_KEY=your-key`.
- `ImportError` — missing dependency. Add to `pyproject.toml` and re-run.
- Output looks wrong — adjust the prompt, not the schema.

**Once it runs successfully, show the actual output.** Quote it or paste it. The founder needs to see what the AI produced, not hear "it works."

---

## Phase 4: Hand Off — THIS IS WHAT I BUILT

Present the handoff in exactly this format. This is the most important output of the entire sprint — make it unmissable.

```
---

## ✅ Prototype complete.

### What I built
[2-3 sentences. What it does, what input it takes, what output it produces.]

### What I tested
- Ran against: [real data they gave you / synthetic data you generated]
- Result: [what the output actually looked like — quote or summarise the key parts]
- Issues found and fixed: [any errors you hit and resolved, or "none"]

### What you should check
- [ ] [Does the output quality match what you'd expect?]
- [ ] [Does it handle edge case X correctly?]
- [ ] [Is the tone/format of the output right for your users?]

### How to run it yourself
​```bash
export ANTHROPIC_API_KEY=your-key
uv run <entry_point>.py [args]
​```
No `uv`? `pip install -r requirements.txt && python <entry_point>.py [args]`

### Next steps to test
- [ ] **Try it on real data** — [specific suggestion: "run it on your actual user's captured topics" / "feed in a real call transcript" / etc.]
- [ ] **Show it to a user** — [who specifically, and what to watch for]
- 🗣️ [Hypothesis that needs a conversation, not code] — ask [who] about [what]

### Files
| File | What it does |
|------|-------------|
| `<entry_point>.py` | [one line] |
| `pyproject.toml` | Dependencies |
| ... | ... |

---
```

For **extension mode**, replace "Files" with a diff summary:
```
### Changes to your repo
Branch: `experiment/<name>`

| File | Change |
|------|--------|
| `src/analyzers/categorizer.py` | New — transaction categorization module |
| `src/config.py` | Modified — added ANTHROPIC_API_KEY |
| `pyproject.toml` | Modified — added `anthropic` dependency |
| `tests/test_categorizer.py` | New — 3 tests covering core categorization |

To review: `git diff main...experiment/<name>`
To merge: `git merge experiment/<name>` (or raise a PR)
To discard: `git branch -D experiment/<name>`
```

### Log the build

After presenting the handoff, update the project's `README.md` with the "Test Results" section — what data you used, what the output looked like, quality assessment, and any issues fixed. This is scoped to the project and gives the founder context when they go to run or evaluate it.

Don't write findings to `DECISION_LOG.md` unilaterally — that's a shared record. The decision log gets updated in the iteration phase, after the founder has tested it and you both agree on what happened.

---

## Iteration: Incorporate Feedback

When the founder has tested the prototype or talked to users:

1. **Surface the evidence.** If new call notes exist, open with what stood out. "From your recent calls: [2-3 insights]. This seems to [confirm / challenge] H2."

2. **Update hypotheses.** Mark tested ones as `✅ confirmed` or `❌ invalidated` with one line of evidence. Add new assumptions. Re-order by risk.

3. **Update spec.** Edit `projects/<name>/PRODUCT_REQUIREMENTS.md`. Mark changed sections `[UPDATED]`. Update "Hypothesis Under Test" if the riskiest assumption shifted.

4. **Checkpoint.** "Here's what changed: [summary]. The prototype now tests [new hypothesis]. Should I rebuild?"

5. **Update code.** Modify `projects/<name>/` — only what the spec changed. Don't regenerate from scratch. Verify it still runs.

6. **Append to `DECISION_LOG.md`:**
```markdown
## Update — [date]

### What was tested
[What the founder tested and how]

### Results
[What they learned]

### Hypothesis Updates
- H2: ❌ invalidated — [one line of evidence]

### Changes Made
[What was updated in hypotheses / spec / code]
```

7. **Hand off again** — same format, with what changed and what to test next.

---

## Artifact Trail

| File | Location | Purpose |
|------|----------|---------|
| `call_notes/*.md` | root | Raw interview transcripts |
| `existing_docs/` | root | YC app, pitch deck, imported docs |
| `HYPOTHESES.md` | root | Company-level assumptions + test status |
| `DECISION_LOG.md` | root | Append-only history — all projects, all iterations |
| `PRODUCT_REQUIREMENTS.md` | `projects/<name>/` | Spec for this specific build |
| Code + `pyproject.toml` | `projects/<name>/` | Working prototype |

---

## Tips

- **Impatient founder?** If they say "just build something", skip discovery — write a minimal PRD from what you know, note the gaps, build. Iterate from there.
- **Code is disposable, decisions aren't.** Hypotheses and the PRD survive across iterations. Code can always be regenerated.
- **Don't clone ChatGPT.** Push for what's literally impossible without AI.
- **The 🗣️ hypotheses are homework.** After building, remind the founder which assumptions need a user conversation — the prototype can't validate everything.
