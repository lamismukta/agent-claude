# agent-claude

Claude Code skills for going from idea to working AI prototype. Runs a discovery conversation, writes hypotheses, specs a PRD, and generates a complete runnable project. Iterates with you.

## Model

Designed for **Claude Sonnet 4.6** — the skills, prompts, and `/build` output are all tuned for it. Sonnet is the right default: fast enough to iterate in a conversation, capable enough to handle discovery, spec writing, and code generation in one session. Upgrade individual prototypes to Opus 4.6 if reasoning quality on a specific task isn't good enough.

Web search in generated prototypes requires Sonnet 4.6 or Opus 4.6 — Haiku doesn't support it.

## Prerequisites

- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) installed (`npm install -g @anthropic-ai/claude-code`)
- `ANTHROPIC_API_KEY` set in your environment ([get one here](https://console.anthropic.com))
- Python 3.11+
- [`uv`](https://docs.astral.sh/uv/) recommended — `curl -LsSf https://astral.sh/uv/install.sh | sh`

## Setup

**1. Clone the repo**

```bash
git clone https://github.com/lamismukta/agent-claude.git
cd agent-claude
claude
```

**2. Run `/onboard`**

Checks prerequisites, optionally connects [Granola](https://granola.ai) or [Notion](https://notion.so) for call notes, and imports any existing docs or code you have.

## Skills

| Skill | What it does |
|-------|-------------|
| `/sprint` | Full loop: brainstorm → spec → working code. Start here. |
| `/brainstorm` | Discovery conversation — produces `hypotheses.md` |
| `/prd` | Write the spec from an existing brainstorm |
| `/build` | Generate code from an existing `product_requirements.md` |
| `/feedback` | Iterate after testing — updates hypotheses, spec, and code together |
| `/onboard` | First-time setup |

## How it works

`/sprint` produces these files in your working directory:

| File | What it captures |
|------|-----------------|
| `hypotheses.md` | Assumptions to test, tagged 🗣️ (talk to users) or 🛠️ (build to test) |
| `decision_log.md` | Append-only record of what changed and why |
| `product_requirements.md` | Spec scoped to test the riskiest hypothesis |
| Project files | `pyproject.toml`, entry point, README |

```
/sprint  → first build (brainstorm → spec → code)
/feedback   → iterate (update spec → update code)
/sprint  → major rethink (full brainstorm again)
```

`/build` generates working code using the Claude API, Agent SDK, or both — picking the simplest approach that fits the spec. Outputs a project you can run with a single command. If you have the [`/claude-api` skill](https://www.anthropic.com/engineering/claude-code-best-practices) installed, `/build` will use it to ensure correct API patterns, model selection, and tool use — it's Anthropic's official skill for building on the Claude API.

## Extending this

Run `/add-capability` to add new skills to your setup. Common starting points:

- Connect email and calendar (Gmail, Google Calendar via MCP)
- Add a competitor research skill
- Write a weekly progress and learnings roundup
- Research investors
- Customer outreach drafts

Or use `/skill-creator` to build any custom skill from scratch.

## Resources

- [Claude API docs](https://platform.claude.com/docs/en/home)
- [Claude Agent SDK](https://github.com/anthropics/claude-agent-sdk-python)
- [Claude Code docs](https://docs.anthropic.com/en/docs/claude-code)
- [`/claude-api` skill](https://www.anthropic.com/engineering/claude-code-best-practices) — Anthropic's official skill for correct API patterns
