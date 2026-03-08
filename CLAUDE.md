# agent-claude

Claude Code skills that take you from idea to working AI prototype in one conversation.

## Quick Start

```
/onboard          ← check prereqs, set up project
/prototype        ← brainstorm → spec → working code (the main skill)
/feedback         ← iterate after testing ("users said X", "change the output")
```

Sub-skills for fine-grained control: `/brainstorm`, `/prd`, `/build`.

## How It Works

```
/prototype → discovery conversation → hypotheses.md → product_requirements.md → working code
/feedback  → update hypotheses → update spec → update code
/prototype → full rethink when the direction changes
```

Every run produces an artifact trail: `hypotheses.md` → `decision_log.md` → `product_requirements.md` → project files. The artifacts persist across iterations — code is disposable, decisions aren't.

## Prerequisites

- Claude Code (`npm install -g @anthropic-ai/claude-code`)
- `ANTHROPIC_API_KEY` set in your environment
- Python 3.11+ (prototypes default to Python)
- `uv` recommended (`pip install uv`) — makes running prototypes one command

## Project Structure

After running `/prototype`, your project will look like:

```
your-project/
├── call_notes/              ← User interview notes (manual or via Granola)
├── existing_docs/           ← Imported product docs, pitch decks (if any)
├── hypotheses.md            ← Assumptions to test, ordered by risk
├── decision_log.md          ← How you got here (append-only)
├── product_requirements.md  ← Buildable spec for the prototype
├── <entry_point>.py         ← Named after what it does (e.g., briefing.py)
├── pyproject.toml           ← Dependencies (uv run <entry_point>.py just works)
├── requirements.txt         ← Fallback for pip users
├── .env.example             ← Required environment variables
└── README.md                ← One-liner to run
```

## What This Builds On

- **Claude API** — Messages API, server-side web search, code execution, structured outputs
- **Claude Agent SDK** — for prototypes that need file/web/terminal access
- **`/claude-api` skill** — Anthropic's official skill for correct API patterns. Recommend installing alongside.

See `examples/meeting-prep/` for a complete walkthrough.
