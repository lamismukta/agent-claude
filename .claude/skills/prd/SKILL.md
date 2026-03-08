---
name: prd
description: "Write a structured product requirements doc (PRD) for an AI product. Use after a discovery conversation (e.g. /brainstorm), when the user says 'write the PRD', 'create a spec', 'document the requirements', or when enough context exists to define what to build. Also use when updating an existing PRD after user feedback. Outputs product_requirements.md that /build can turn into working code."
---

# /prd — Write the Product Requirements Doc

Take everything learned from the discovery conversation and produce a `product_requirements.md` — a concise, buildable spec that `/build` can turn into working code.

Before writing, read `references/mvp-canon.md` — it contains the YC and Paul Graham frameworks on scoping MVPs and writing specs. The core insight: scope a prototype buildable in a day that tests the riskiest assumption, not a product that does everything.

## How It Works

1. **Gather context.** Read the conversation so far. If `/brainstorm` was run, the key decisions are already surfaced. If not, work with whatever the founder has described — ask clarifying questions only if critical information is missing.

2. **Read `hypotheses.md`** if it exists. The prototype should test the riskiest assumption tagged 🛠️. This drives what you put in Core Capabilities and Success Criteria — the prototype's job is to confirm or kill that hypothesis.

3. **Check for existing PRD.** If `product_requirements.md` exists, you're in update mode — read it, apply changes, mark updates.

4. **Write the PRD.** One page. Buildable in a day. Every section earns its place.

## Writing Principles

The PRD is a handoff document — it needs to be clear enough that `/build` (or a developer) can generate working code without asking follow-up questions. But it's a prototype spec, not a product bible.

- **Specific over vague.** "Summarise the document" is useless. "Extract the 5 key findings and output a markdown list with one sentence each" is buildable.
- **Scope to a prototype.** If it can't be built in a day, cut features until it can. The goal is to test the riskiest assumption, not to ship a product.
- **Name the user.** Not "users" — one specific persona with a role, context, and trigger.
- **Architecture is a recommendation, not a decree.** Suggest the right surface (API call, workflow, agent) and model, but `/build` makes the final call based on what the code needs.
- **State what's out of scope.** This prevents scope creep during build. Be explicit about what the prototype does NOT do.

## PRD Template

Write `product_requirements.md` using this structure:

```markdown
# Product Requirements: [Product Name]

## Problem
[1-2 sentences. What problem, for whom. Ground it in real behaviour — what do they do today and why is it broken?]

## Why LLM?
[Why does this need AI — not just a script, a database query, or a spreadsheet? Be specific about what the LLM adds.]
- **LLM is good at:** [e.g., "interpreting unstructured text", "generating natural language summaries", "making judgment calls on ambiguous input"]
- **LLM is NOT needed for:** [e.g., "storing data", "sending emails", "CRUD operations" — use tools for these]
- **What was impossible before:** [the capability that only exists because of LLMs — this is the core value]

## User
- **Who:** [specific persona — role, technical ability, context]
- **Trigger:** [how they start using it — CLI command, web form, API call, Slack message, cron job]
- **Output:** [what they get back — text, structured data, file, email, action taken]

## Core Capabilities
[Numbered list of what the AI needs to do. Each capability should be specific enough to implement.]

1. [e.g., "Accept a company name and person name as input"]
2. [e.g., "Search the web for recent news, funding rounds, and key people"]
3. [e.g., "Generate a one-page briefing doc in markdown with sections: Company Overview, Recent News, Key People, Talking Points"]

## Tools Required
[Which external tools/APIs the AI needs. Only list what's necessary for the capabilities above.]

- Web search — for [what specifically]
- File system — for [reading/writing what]
- [External API] — for [what specifically]

## Architecture
- **Type:** [Single API call / Multi-step workflow / Autonomous agent]
- **Autonomy:** [Fully autonomous / Human-in-the-loop / Suggestions only]
- **Model:** [Recommended model and why — e.g., "Sonnet 4.6 — fast and cheap enough for a prototype. Upgrade to Opus if reasoning quality matters."]

## Scope
- **In scope:** [what the prototype will do — be specific]
- **Out of scope:** [what it won't do — be explicit, prevents scope creep]
- **Constraints:** [privacy, compliance, rate limits, budget, etc.]

## Hypothesis Under Test
[Which hypothesis from hypotheses.md this prototype is built to test. Copy it here so it's visible in the PRD. If no hypotheses.md exists, state the riskiest assumption in one sentence.]

- **Hypothesis:** [e.g., "H2: Claude can extract structured deal terms from unformatted PDF term sheets with >90% accuracy"]
- **Confirmed if:** [what outcome proves it]
- **Killed if:** [what outcome disproves it]

## Success Criteria
[How you know the prototype works. Concrete, testable. These should directly test the hypothesis above.]

- [e.g., "Given a company name, produces a briefing doc in under 30 seconds"]
- [e.g., "Briefing contains at least 3 recent news items from the past 6 months"]
- [e.g., "Output is markdown that renders cleanly"]
```

## Update Mode

When `product_requirements.md` already exists and the founder has new feedback:

1. Read the existing PRD.
2. Apply changes. Mark updated sections with `[UPDATED]` so the diff is visible.
3. If the feedback changes the architecture (e.g., "actually this needs to be an agent, not a single call"), flag it clearly — `/build` needs to know.
4. Don't bloat the PRD with revision history. One clean document, with `[UPDATED]` tags on changed sections.
5. Append to `decision_log.md` — log what changed in the spec and why. Use this format:

```markdown
## PRD Update — [date]

### Changes
- [Section]: [what changed and why]

### Hypothesis Impact
- Now testing: [which hypothesis the updated prototype targets]
```

## What Not to Do

- Don't pad the PRD with sections that don't inform the build. If there's nothing to say about constraints, leave it out.
- Don't write implementation details — that's `/build`'s job. The PRD says *what*, not *how*.
- Don't scope a product. Scope a prototype. One day of build time. One core workflow.
- Don't invent requirements the founder didn't express. If you think something's missing, ask — don't assume.
