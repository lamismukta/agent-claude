---
name: prototype
description: "Go from idea to working AI prototype in one conversation. Runs a discovery brainstorm, writes a PRD, then generates working code on Claude's API or Agent SDK. Use when a founder says 'I want to prototype something', 'help me build an AI app', 'let's build this', or anything that combines ideation with building. Also use for iteration — 'users said X, update the prototype' or 'rebuild with these changes'. This is the full flow; use /brainstorm for just the conversation, /prd for just the spec, or /build for just the code."
---

# /prototype — Idea → Working Code

The fast path from idea to working AI prototype. Runs the discovery brainstorm, writes the PRD, then generates a complete runnable project — all in one conversation.

## How It Works

### First Run (No Existing PRD)

1. **Run `/brainstorm`.** Have the discovery conversation. Surface the problem, user, capabilities, and scope. This produces `hypotheses.md` — the assumptions to test.

2. **Run `/prd`.** Write the product requirements doc, scoped to test the riskiest hypothesis. Show the founder a summary: "Here's what I'm going to build to test [hypothesis]: [summary]. Ready?" This is the moment to catch misunderstandings — cheaper to fix the spec than rewrite code.

3. **Run `/build`.** Read the PRD, pick the right architecture, generate the project. Verify it runs.

4. **Present the result.** Show the founder what was built, how to run it, and where to modify it.

### Iteration (PRD Already Exists)

When `product_requirements.md` exists in the current directory, you're in iteration mode.

1. **Run `/brainstorm`** in iteration mode — read the existing PRD and hypotheses, update hypothesis statuses based on new evidence, ask what's changed.

2. **Run `/prd`** to update the spec. If a hypothesis was killed, the prototype's focus may shift. Mark changes with `[UPDATED]` tags.

3. **Run `/build`** to update the code. Modify only what changed.

4. **Present what's different.**

## Composability

These skills work together or independently:

- **Just the conversation:** `/brainstorm` — think through the product without writing anything
- **Just the spec:** `/prd` — write requirements from context you already have
- **Just the code:** `/build` — already have a `product_requirements.md`, just want code
- **Full loop:** `/prototype` — brainstorm → prd → build
- **Iterate:** `/prototype` again — detects existing PRD, enters iteration mode

## Tips

- If the founder is impatient and wants to skip the brainstorm ("just build me a chatbot"), run `/prd` with a minimal spec from what you know, note the gaps, then `/build`. They can iterate.
- If the founder has a clear spec already, skip `/brainstorm` and go straight to `/prd` or `/build`.
- The PRD and `hypotheses.md` are the durable artifacts. Code can be regenerated; the hypotheses and PRD capture product decisions that survive across iterations.
