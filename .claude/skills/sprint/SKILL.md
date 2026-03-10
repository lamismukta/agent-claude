---
name: sprint
description: "Go from idea to working AI prototype in one conversation. This is the main skill — run this. It brainstorms the idea, writes hypotheses, specs the PRD, and generates working code on Claude's API or Agent SDK. Use when a founder says 'I want to run a sprint', 'help me build an AI app', 'let's build this', 'I have an idea', or anything that involves going from idea to code. Also handles iteration — 'users said X', 'update the sprint', 'I talked to users'. Sub-skills (/brainstorm, /prd, /build) exist for fine-grained control but most founders should just use /sprint."
---

# /sprint — Idea → Working Code

The main skill. Takes a founder from idea to working AI prototype in one conversation. Runs the full loop: discovery brainstorm → hypotheses → product spec → working code.

Most founders should start here. The sub-skills (`/brainstorm`, `/prd`, `/build`) exist for when you want more control over individual steps.

**The founder drives.** You are the co-pilot. At every stage, present what you've got and wait for confirmation before moving on. Don't run the whole pipeline silently — the checkpoints are where the best product decisions happen.

## How It Works

### First Run (New Idea)

1. **Brainstorm.** Run the `/brainstorm` flow — have the discovery conversation, surface the problem, user, capabilities, and scope. Ask **one question at a time**. Check for any context already captured by `/onboard` (existing docs, notes, or anything the founder mentioned during setup) and build on it — don't re-ask what's already known. This produces:
   - `hypotheses.md` — the assumptions to test, tagged as 🗣️ conversation or 🛠️ prototype
   - First entry in `decision_log.md` — the reasoning trail

   **Checkpoint:** Present the hypotheses. "Here are the 5 assumptions I think could kill this idea. The riskiest one we can test with software is [H2]. Does this feel right, or am I missing something?"

2. **Spec.** Run the `/prd` flow — write the product requirements doc, scoped to test the riskiest 🛠️ hypothesis.

   **Checkpoint:** Present the PRD summary before building. "Here's what I'm going to build: [one-paragraph summary]. It tests [hypothesis] by [how]. The architecture is [single call / workflow / agent] using [model]. Ready to build, or should we change anything?" Cheaper to fix the spec than rewrite code.

3. **Build.** Run the `/build` flow — read the PRD, pick the right architecture, generate a complete runnable project.

4. **Hand off.** Give the founder everything they need to run and test it:

   ```
   ## Your prototype is ready.

   ### Run it
   [exact command, e.g.: export ANTHROPIC_API_KEY=your-key && uv run briefing.py "Sarah Chen" "Sequoia Capital"]

   No uv? [fallback command with pip]

   ### What it does
   [1-2 sentences — what input it takes, what output it produces]

   ### What it tests
   [Which hypothesis this prototype is built to confirm or kill]

   ### What to look for
   - [Specific thing to check, e.g., "Are the talking points specific to the person, or generic?"]
   - [Another thing, e.g., "Does it find recent news, or hallucinate?"]

   ### Validate with users
   These hypotheses need a conversation, not code:
   - 🗣️ H1: [assumption] — ask [who] about [what]
   - 🗣️ H3: [assumption] — show [who] the output and ask [what]

   ### Files generated
   [List of files with one-line descriptions]
   ```

   This is the most important step. A prototype that the founder can't run or doesn't know how to evaluate is worthless.

### Iteration (Coming Back With Feedback)

When `product_requirements.md` or `hypotheses.md` already exist, you're in iteration mode. The founder has talked to users, tested the prototype, or just changed their mind.

1. **Update hypotheses.** Run `/brainstorm` in iteration mode — pull new Granola call notes if configured, read existing hypotheses and PRD, mark what's confirmed or killed, surface new assumptions.

2. **Update spec.** Run `/prd` to update the requirements. If a hypothesis was killed, the prototype's focus may shift entirely. Mark changes with `[UPDATED]` tags. Append to `decision_log.md`.

   **Checkpoint:** "Here's what changed in the spec: [summary]. The prototype now tests [new hypothesis] instead of [old one]. Should I rebuild?"

3. **Update code.** Run `/build` to modify the existing project. Only change what the spec changed — don't regenerate from scratch.

4. **Hand off again.** Same format as first run — exact run command, what changed, what to test.

## The Artifact Trail

Each run produces or updates these files:

| File | Written by | Purpose |
|------|-----------|---------|
| `call_notes/*.md` | Granola MCP or manual | Raw interview transcripts |
| `hypotheses.md` | Brainstorm | Current assumptions + test status |
| `decision_log.md` | Brainstorm + PRD + Feedback | Append-only history of iterations |
| `product_requirements.md` | PRD | Buildable spec for the prototype |
| Project files | Build | Working code (`pyproject.toml`, entry point, etc.) |

## Quick Feedback Loop

After the first build, most iteration happens through `/feedback` — not `/sprint` again:

```
/sprint  → first build (brainstorm → spec → code)
/feedback   → quick iterations (feedback → update spec → update code)
/sprint  → major rethink (full brainstorm again)
```

Use `/feedback` when the direction is right but something needs tweaking. Use `/sprint` again when the direction itself needs rethinking.

## Sub-Skills (For Fine-Grained Control)

Most founders use `/sprint` + `/feedback`. But individual steps are available:

- **`/brainstorm`** — Just the discovery conversation. Produces hypotheses without writing a spec or code.
- **`/prd`** — Just the spec. Use when you already have context and want to write requirements.
- **`/build`** — Just the code. Use when you already have a `product_requirements.md`.
- **`/feedback`** — Quick iteration. Takes feedback, updates hypotheses + spec + code without a full brainstorm.

## Tips

- **Impatient founder?** If they say "just build me a chatbot", skip the brainstorm — run `/prd` with a minimal spec from what you know, note the gaps, then `/build`. They can iterate.
- **Clear spec already?** Skip straight to `/prd` or `/build`.
- **Code is disposable, decisions aren't.** The hypotheses and PRD capture product decisions that survive across iterations. Code can always be regenerated.
- **The 🗣️ hypotheses are homework.** After building, remind the founder which assumptions need a user conversation to test — the prototype can't validate everything.
