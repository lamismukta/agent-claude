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
- `call_notes/` — any user interviews. Note anything new since the last decision log entry.
- `projects/` — list any existing project folders. For each, read `PRODUCT_REQUIREMENTS.md`.
- `existing_docs/yc-application.md` — foundation context

**If Granola MCP is configured:** Run `list_meetings` and check for meetings since the last saved note. Fetch and save any new ones to `call_notes/` with this frontmatter:
```markdown
---
who: [Name, Role at Company]
date: [YYYY-MM-DD]
context: [User interview / Demo / Intro call, N min]
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

### Read everything first

Before the discovery conversation, read all existing context:
- `existing_docs/yc-application.md` — problem, user, solution, traction, team
- `existing_docs/` — any other imported docs
- `call_notes/` — extract pain points, workarounds, surprises, verbatim quotes
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
- **Model:** [e.g., "claude-sonnet-4-6 — fast and cheap. Upgrade to Opus if reasoning quality matters."]

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

---

## Phase 3: Build

### Pick the architecture

Start with a single API call. Only add complexity when genuinely required:
- **Single API call** — one prompt in, one response out. Solves more than expected.
- **Tool use / multi-step** — when the model needs to take actions (web search, file reads)
- **Agentic loop** — when it needs decisions across multiple steps
- **Agent SDK** — only when it needs file, web, or terminal access as a full agent

### Generate the project

Create a complete project in `projects/<name>/`:

```
projects/<name>/
├── README.md              ← see template below
├── pyproject.toml         ← dependencies (uv installs automatically)
├── requirements.txt       ← fallback for pip users
├── .env.example           ← ANTHROPIC_API_KEY=your-key-here
├── <entry_point>.py       ← named after what it does (briefing.py, categorizer.py)
└── PRODUCT_REQUIREMENTS.md
```

**README.md template:**
```markdown
# <Project Name>

<One sentence: what it does and what it tests.>

**Type:** Standalone experiment / Extension of <repo> ([branch](link))
**Hypothesis:** H<N> — <assumption in plain language>
**Confirmed if:** <what outcome proves it>

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

## How It Works

<Brief explanation of architecture — single call / pipeline / agent.>
```

For branch mode, the branch link should point to the actual branch in the founder's repo. For standalone, omit the link.


**pyproject.toml:**
```toml
[project]
name = "project-name"
version = "0.1.0"
requires-python = ">=3.11"
dependencies = ["anthropic"]
```

### Code guidelines

**Defaults:**
- Model: `claude-sonnet-4-6`. Note in a comment where to upgrade to `claude-opus-4-6`.
- Adaptive thinking for reasoning: `thinking={"type": "adaptive"}`
- Stream long responses: `.stream()` with `.get_final_message()`

**Tool use — Tool Runner pattern:**
```python
from anthropic import Anthropic, beta_tool

@beta_tool
def search_web(query: str) -> str:
    """Search the web for information."""
    return results

response = client.beta.messages.tool_runner(
    model="claude-sonnet-4-6",
    max_tokens=4096,
    tools=[search_web],
    messages=[{"role": "user", "content": prompt}],
)
```

**Server-side tools (free with the API):**
```python
tools = [
    {"type": "web_search_20260209", "name": "web_search"},
    {"type": "code_execution_20260120", "name": "code_execution"},
]
```
Note: web search requires Sonnet 4.6 or Opus 4.6 — Haiku doesn't support it.

**Structured output:**
```python
response = client.messages.create(
    model="claude-sonnet-4-6",
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

### Self-test before handing off

Run the prototype after generating. This is not optional.

Create synthetic test data first — don't wait for the founder. Generate realistic sample inputs and run against those.

```bash
uv run <entry_point>.py [test args]
# or if uv unavailable:
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
.venv/bin/python <entry_point>.py [test args]
```

Fix errors before presenting. Report what the output looked like — "I ran it against 5 sample transactions, categorized 4 correctly, flagged 1 for review" is useful. "It runs" is not.

---

## Phase 4: Hand Off

```
## Your prototype is ready.

### Run it
export ANTHROPIC_API_KEY=your-key
uv run <entry_point>.py [args]

No uv? pip install -r requirements.txt && python <entry_point>.py [args]

### What it does
[1-2 sentences — input, output, what happens in between]

### What it tests
[Which hypothesis this confirms or kills]

### What to look for
- [Specific thing to evaluate]
- [Another thing]

### Validate with users
These hypotheses need a conversation, not code:
- 🗣️ H1: [assumption] — ask [who] about [what]

### Files generated
[List every file with a one-line description]
```

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
