# agent-claude

Claude Code skills for going from idea to working AI prototype. Runs a discovery conversation, writes hypotheses, specs a PRD, and generates a complete runnable project. Iterates with you.

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
| `/sprint` | Any time — new idea, just tested something, talked to users, want to iterate. Reads your context and figures out the right questions. |
| `/status` | Read-only snapshot — confirmed hypotheses, what still needs validating |
| `/onboard` | First-time setup |

That's it. `/sprint` handles first builds and iteration alike. Run it whenever you have something new to work through.

## How it works

`/sprint` reads your project context — `decision_log.md`, `hypotheses.md`, `call_notes/` — and routes based on where you are:

- **Empty context** → runs a discovery conversation, writes hypotheses, specs a PRD, generates code
- **Existing project** → synthesises what's changed, asks what happened, updates hypotheses + spec + code

Every run produces:

| File | Location | What it captures |
|------|----------|-----------------|
| `hypotheses.md` | root | Assumptions ordered by risk, tagged 🗣️ (talk to users) or 🛠️ (build to test) |
| `decision_log.md` | root | Append-only record of what changed and why |
| `product_requirements.md` | `projects/<name>/` | Spec scoped to test the riskiest hypothesis |
| Project files | `projects/<name>/` | `pyproject.toml`, entry point, README — runs with one command |

Generated prototypes use the Claude API or Agent SDK, picking the simplest approach that fits the spec. If you have the [`/claude-api` skill](https://www.anthropic.com/engineering/claude-code-best-practices) installed, it ensures correct API patterns and model selection.

## Model

Designed for **Claude Sonnet 4.6** — the skills, prompts, and generated code are all tuned for it. Sonnet is the right default: fast enough to iterate in a conversation, capable enough to handle discovery, spec writing, and code generation in one session. Upgrade individual prototypes to Opus 4.6 if reasoning quality on a specific task isn't good enough.

Web search in generated prototypes requires Sonnet 4.6 or Opus 4.6 — Haiku doesn't support it.

## Resources

- [Claude API docs](https://platform.claude.com/docs/en/home)
- [Claude Agent SDK](https://github.com/anthropics/claude-agent-sdk-python)
- [Claude Code docs](https://docs.anthropic.com/en/docs/claude-code)
- [`/claude-api` skill](https://www.anthropic.com/engineering/claude-code-best-practices) — Anthropic's official skill for correct API patterns
