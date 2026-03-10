# agent-claude

Claude Code skills for stress testing your ideas and getting you a working AI prototype. Runs a discovery conversation, writes hypotheses, specs a PRD, and generates a complete runnable project. Iterates with you.

## Prerequisites

- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) installed (`npm install -g @anthropic-ai/claude-code`)
- `ANTHROPIC_API_KEY` set in your environment ([get one here](https://console.anthropic.com))
- Python 3.11+
- [`uv`](https://docs.astral.sh/uv/) recommended — `curl -LsSf https://astral.sh/uv/install.sh | sh`

## Setup

```bash
git clone https://github.com/lamismukta/agent-claude.git
cd agent-claude
claude
```

Then run `/onboard` — checks prerequisites, optionally connects [Granola](https://granola.ai) or [Notion](https://notion.so) for call notes, and imports any existing docs or code.

## Skills

| Skill | When to use |
|-------|-------------|
| `/sprint` | Any time — new idea, just tested something, talked to users, want to iterate. Reads your context and figures out the right questions. Translates learnings into PRDs and builds working code. |
| `/status` | Read-only snapshot of the latest — confirmed hypotheses, what still needs validating |
| `/onboard` | First-time setup |

That's it. `/sprint` handles first builds and iteration alike. Run it whenever you have something new to work through - either iterating an exiting project or starting a new test.

## How it works

`/sprint` reads your project context — `DECISION_LOG.md`, `HYPOTHESES.md`, `call_notes/` — and routes based on where you are:

- **Empty context** → runs a discovery conversation, writes hypotheses, specs a PRD, generates code
- **Existing project** → synthesises what's changed, asks what happened, updates hypotheses + spec + code

There are core msater files which each run may update:

| File | Location | What it captures |
|------|----------|-----------------|
| `HYPOTHESES.md` | root | Assumptions ordered by risk, tagged 🗣️ (talk to users) or 🛠️ (build to test) |
| `DECISION_LOG.md` | root | Append-only record of what changed and why |
| `PRODUCT_REQUIREMENTS.md` | `projects/<name>/` | Spec scoped to test the riskiest hypothesis |
| Project files | `projects/<name>/` | `pyproject.toml`, entry point, README — runs with one command |

Generated prototypes use the Claude API or Agent SDK, picking the simplest approach that fits the spec. The `/claude-api` skill (built into Claude Code) ensures correct API patterns.

## Going further

This framework is easy to extend — ask Claude to add:

**More integrations:** email, calendar, CRM, Slack

**Skills:** research competitors and investors, automate sales outreach, draft weekly progress report

## Model

Works best in **Claude Code with Sonnet 4.6**. Generated prototypes pick the right model for the task — Claude decides based on the spec.

## Resources

- [Claude API docs](https://platform.claude.com/docs/en/home)
- [Claude Agent SDK](https://github.com/anthropics/claude-agent-sdk-python)
- [Claude Code docs](https://docs.anthropic.com/en/docs/claude-code)
- `/claude-api` skill — built into Claude Code, handles correct API patterns when generating prototypes
