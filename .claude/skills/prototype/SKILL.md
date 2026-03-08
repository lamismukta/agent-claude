---
name: prototype
description: "Go from idea to working AI prototype in one conversation. This is the main skill — run this. It brainstorms the idea, writes hypotheses, specs the PRD, and generates working code on Claude's API or Agent SDK. Use when a founder says 'I want to prototype something', 'help me build an AI app', 'let's build this', 'I have an idea', or anything that involves going from idea to code. Also handles iteration — 'users said X', 'update the prototype', 'I talked to users'. Sub-skills (/brainstorm, /prd, /build) exist for fine-grained control but most founders should just use /prototype."
---

# /prototype — Idea → Working Code

The main skill. Takes a founder from idea to working AI prototype in one conversation. Runs the full loop: discovery brainstorm → hypotheses → product spec → working code.

Most founders should start here. The sub-skills (`/brainstorm`, `/prd`, `/build`) exist for when you want more control over individual steps.

## How It Works

### First Run (New Idea)

1. **Brainstorm.** Run the `/brainstorm` flow — have the discovery conversation, surface the problem, user, capabilities, and scope. This produces:
   - `hypotheses.md` — the assumptions to test, tagged as 🗣️ conversation or 🛠️ prototype
   - First entry in `decision_log.md` — the reasoning trail

2. **Spec.** Run the `/prd` flow — write the product requirements doc, scoped to test the riskiest 🛠️ hypothesis. Before building, confirm with the founder: "Here's what I'm going to build to test [hypothesis]: [summary]. Ready?" Cheaper to fix the spec than rewrite code.

3. **Build.** Run the `/build` flow — read the PRD, pick the right architecture, generate a complete runnable project with `pyproject.toml`, README, and a one-liner to run (`uv run main.py`).

4. **Present.** Show the founder:
   - What was built and what hypothesis it tests
   - How to run it (the one-liner from the README)
   - Where to modify it
   - What to test next — the 🗣️ hypotheses they should take to their next user call

### Iteration (Coming Back With Feedback)

When `product_requirements.md` or `hypotheses.md` already exist, you're in iteration mode. The founder has talked to users, tested the prototype, or just changed their mind.

1. **Update hypotheses.** Run `/brainstorm` in iteration mode — pull new Granola call notes if configured, read existing hypotheses and PRD, mark what's confirmed or killed, surface new assumptions.

2. **Update spec.** Run `/prd` to update the requirements. If a hypothesis was killed, the prototype's focus may shift entirely. Mark changes with `[UPDATED]` tags. Append to `decision_log.md`.

3. **Update code.** Run `/build` to modify the existing project. Only change what the spec changed — don't regenerate from scratch.

4. **Present what's different.** Show the delta, not the whole thing.

## The Artifact Trail

Each run produces or updates these files:

| File | Written by | Purpose |
|------|-----------|---------|
| `call_notes/*.md` | Granola MCP or manual | Raw interview transcripts |
| `hypotheses.md` | Brainstorm | Current assumptions + test status |
| `decision_log.md` | Brainstorm + PRD | Append-only history of iterations |
| `product_requirements.md` | PRD | Buildable spec for the prototype |
| Project files | Build | Working code (`pyproject.toml`, `main.py`, etc.) |

## Sub-Skills (For Fine-Grained Control)

Most founders just run `/prototype`. But if you want individual steps:

- **`/brainstorm`** — Just the discovery conversation. Produces hypotheses without writing a spec or code.
- **`/prd`** — Just the spec. Use when you already have context and want to write requirements.
- **`/build`** — Just the code. Use when you already have a `product_requirements.md`.

## Tips

- **Impatient founder?** If they say "just build me a chatbot", skip the brainstorm — run `/prd` with a minimal spec from what you know, note the gaps, then `/build`. They can iterate.
- **Clear spec already?** Skip straight to `/prd` or `/build`.
- **Code is disposable, decisions aren't.** The hypotheses and PRD capture product decisions that survive across iterations. Code can always be regenerated.
- **The 🗣️ hypotheses are homework.** After building, remind the founder which assumptions need a user conversation to test — the prototype can't validate everything.
