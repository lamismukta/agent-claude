# agent-claude

Claude Code skills that take you from idea to working AI prototype in one conversation.

You describe the problem. Claude runs a discovery conversation, writes hypotheses, specs a PRD scoped to test the riskiest assumption, and generates a complete runnable project on Claude's API. The whole loop — brainstorm to working code — happens in a single session. When you talk to users and come back with feedback, it updates the hypotheses, the spec, and the code together.

## Demo: meeting prep tool in one session

Here's what a full `/prototype` run looks like. The founder says: "I spend 30 minutes before every investor call googling the person. Can AI do that for me?"

Claude runs the brainstorm, surfaces 5 hypotheses, writes a PRD scoped to test the riskiest one ("can web search surface useful intel?"), and generates a working CLI tool:

```bash
export ANTHROPIC_API_KEY=your-key
uv run briefing.py "Sarah Chen" "Sequoia Capital"
```

30 seconds later:

```
# Briefing: Sarah Chen — Sequoia Capital

## Person Overview
Role, background, investment focus, notable public takes.

## Fund/Company Overview
Stage focus, recent deals, fund size.

## Recent News
3-5 bullet points from the last 6 months.

## Talking Points
3 specific conversation starters grounded in the research.
```

The full example — hypotheses, decision log, PRD, and working code — is in [`examples/meeting-prep/`](examples/meeting-prep/).

## How it works

### The artifact trail

Every `/prototype` run produces files that persist across iterations:

| Artifact | What it captures |
|----------|-----------------|
| `hypotheses.md` | Assumptions to test, tagged 🗣️ (ask users) or 🛠️ (build software) |
| `decision_log.md` | Append-only history — why you built it this way |
| `product_requirements.md` | Buildable spec, scoped to test the riskiest hypothesis |
| Project files | Working code — `pyproject.toml`, entry point, README |

Code is disposable. The hypotheses and decisions survive across iterations.

### The iteration loop

```
/prototype  → first build (brainstorm → spec → code)
/feedback   → quick iterations (update spec → update code)
/prototype  → major rethink (full brainstorm again)
```

`/feedback` is for when the direction is right but something needs tweaking — "users said the output format is wrong" or "it crashes on edge cases." `/prototype` is for when the direction itself needs rethinking.

### What Claude decides

Based on the PRD, `/build` picks the simplest architecture that works:

| What the PRD describes | What gets built |
|------------------------|----------------|
| Single task (classify, summarise, extract) | Claude API — one call |
| Multi-step pipeline with fixed logic | Claude API + tool use |
| Open-ended agent that makes decisions | Claude API + agentic loop |
| Agent that needs file/web/terminal access | Agent SDK |

It defaults to Sonnet 4.6 for prototypes (fast, cheap), generates a `pyproject.toml` so `uv run main.py` just works, and includes a `requirements.txt` fallback for pip users.

## Setup

```bash
git clone https://github.com/lamismukta/agent-claude.git
cd agent-claude
claude
```

Then:

```
/onboard
```

This checks your prerequisites (API key, Python, uv), imports any existing context you have (product docs, user research, call recordings, existing code), and optionally wires up [Granola](https://granola.ai) for pulling user call transcripts directly.

### Prerequisites

- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) installed
- `ANTHROPIC_API_KEY` set in your environment ([get one here](https://console.anthropic.com))
- Python 3.11+
- [`uv`](https://docs.astral.sh/uv/) recommended — `pip install uv`

## Skills

| Skill | What it does |
|-------|-------------|
| `/prototype` | **Start here.** Full loop: brainstorm → spec → working code |
| `/feedback` | Quick iteration after testing — updates hypotheses, spec, and code |
| `/brainstorm` | Just the discovery conversation — produces hypotheses without building |
| `/prd` | Just the spec — use when you already know what to build |
| `/build` | Just the code — use when you already have a `product_requirements.md` |
| `/onboard` | First-time setup — checks env, imports existing docs/code, optional Granola config |

Most people use `/prototype` to start and `/feedback` to iterate. The sub-skills exist for when you want more control.

## What this adds over "just ask Claude to build it"

Two things.

**Product thinking first.** `/brainstorm` makes you articulate the problem, user, and riskiest assumption before writing code. The hypotheses file forces you to name what could kill the idea. The PRD becomes the persistent artifact across iterations — not throwaway chat context.

**Structured iteration.** When you come back with "users said X", the update flows through hypotheses → spec → code. The decision log tracks why you built it this way. Three iterations in, you can trace every change back to evidence.

Everything else — which model, streaming vs sync, tool use patterns, structured outputs — Claude Code handles that with the right docs in context. The skills don't over-specify what the API already does well.

## What it builds on

- [Claude API](https://platform.claude.com/docs/en/home) — Messages API, server-side web search, code execution, structured outputs
- [Claude Agent SDK](https://github.com/anthropics/claude-agent-sdk-python) — for prototypes that need file, web, or terminal access
- [`/claude-api` skill](https://www.anthropic.com/engineering/claude-code-best-practices) — Anthropic's official skill for correct API patterns. Recommend installing alongside.

## Project structure

```
agent-claude/
├── CLAUDE.md                       ← Project context for Claude Code
├── .claude/skills/                 ← Auto-discovered by Claude Code on clone
│   ├── prototype/SKILL.md          ← /prototype — the main skill
│   ├── feedback/SKILL.md           ← /feedback — quick iteration
│   ├── brainstorm/SKILL.md         ← /brainstorm — discovery conversation
│   ├── prd/SKILL.md                ← /prd — writes the spec
│   ├── build/SKILL.md              ← /build — generates code
│   └── onboard/SKILL.md            ← /onboard — first-time setup
├── examples/meeting-prep/          ← Complete walkthrough
└── call_notes/                     ← User interview notes
```

Skills live in `.claude/skills/` — Claude Code auto-discovers them when you open a session. Clone the repo, run `claude`, and the skills are available immediately.
