# agent-claude

Claude Code skills that take you from idea to working AI prototype in one conversation.

## Quick Start

```
/onboard   ← first time setup
/sprint    ← everything else
```

`/sprint` reads your project context and figures out where you are. Run it when you have a new idea, want to build something, have talked to users, tested a prototype, or just want to know what to do next. It handles first builds and iteration alike.

## How It Works

```
/sprint  → reads decision_log, hypotheses, call notes
         → if empty: runs discovery conversation
         → if existing: synthesises what's changed, asks what happened, updates and rebuilds
```

Every run produces an artifact trail: `HYPOTHESES.md` → `DECISION_LOG.md` → `PRODUCT_REQUIREMENTS.md` → project files. Code is disposable, decisions aren't.

## Prerequisites

- Claude Code (`npm install -g @anthropic-ai/claude-code`)
- `ANTHROPIC_API_KEY` set in your environment
- Python 3.11+ (prototypes default to Python)
- `uv` recommended (`curl -LsSf https://astral.sh/uv/install.sh | sh`) — makes running prototypes one command

## Project Structure

```
your-project/
├── call_notes/              ← User interview notes (manual or via Granola)
├── existing_docs/           ← YC app, pitch decks, imported docs
├── HYPOTHESES.md            ← Assumptions to test, ordered by risk
├── DECISION_LOG.md          ← How you got here (append-only)
└── projects/
    └── transaction-categorizer/
        ├── PRODUCT_REQUIREMENTS.md
        ├── categorizer.py
        ├── pyproject.toml
        └── README.md
```

## What This Builds On

- **Claude API** — Messages API, server-side web search, code execution, structured outputs
- **Claude Agent SDK** — for prototypes that need file/web/terminal access

See `examples/` for complete walkthroughs.
