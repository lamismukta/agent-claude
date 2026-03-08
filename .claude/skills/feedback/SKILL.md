---
name: feedback
description: "Process feedback on a prototype and update the project. Use when a founder says 'users said X', 'this didn't work', 'I tested it and...', 'change this', 'the output was wrong', or gives any feedback on a built prototype. Skips the full brainstorm — goes straight from feedback to updated hypotheses, PRD, and code. For quick iterations, not deep rethinks. Use /prototype if the direction is changing fundamentally."
---

# /feedback — Quick Iteration Loop

The fast path for incorporating feedback without a full brainstorm. The founder tested the prototype or talked to users — now they want changes. Update the hypotheses, update the spec, update the code.

Use this for incremental feedback. If the whole direction is changing, use `/prototype` instead — it runs the full brainstorm.

## How It Works

1. **Read current state.** Read `hypotheses.md`, `product_requirements.md`, and the existing code. Understand what was built and what it was testing.

2. **Take the feedback.** Listen to what the founder says. Categorise it:
   - **Hypothesis result** — "users actually don't care about X" or "the AI output was wrong" → update hypothesis status
   - **Feature tweak** — "add a section for Y" or "change the output format" → update PRD
   - **Bug or quality issue** — "it crashes when..." or "the talking points are generic" → fix code directly
   - **Direction shift** — "actually we should build something different" → suggest `/prototype` instead

3. **Update artifacts.** Based on the feedback type:

   **If hypotheses changed:**
   - Update `hypotheses.md` — mark tested ones as ✅ confirmed or ❌ invalidated with evidence
   - Add new hypotheses if the feedback reveals new assumptions
   - Re-order by risk

   **If the spec needs updating:**
   - Update `product_requirements.md` — mark changed sections with `[UPDATED]`
   - Update the "Hypothesis Under Test" if the riskiest assumption shifted

   **Always:**
   - Append to `decision_log.md`:
   ```markdown
   ## Feedback — [date]

   ### What was tested
   - [What the founder tested and how]

   ### Results
   - [What they learned — be specific]

   ### Hypothesis Updates
   - H1: [status change + evidence]

   ### Changes Made
   - [What was updated in PRD/code and why]
   ```

4. **Update the code.** If the feedback requires code changes:
   - Read the existing project code
   - Make targeted changes — don't regenerate from scratch
   - If the architecture needs to change (e.g., adding a new tool), explain before doing it
   - Verify the code still runs after changes

5. **Present what changed.** Show the founder:
   - Which hypotheses moved
   - What changed in the spec (if anything)
   - What changed in the code
   - What to test next

## When to Use /feedback vs /prototype

| Situation | Use |
|-----------|-----|
| "The output quality is bad" | `/feedback` — fix the code |
| "Users said they want X instead" | `/feedback` — update spec + code |
| "Actually I want to build something completely different" | `/prototype` — full brainstorm |
| "I talked to 5 users and everything we assumed is wrong" | `/prototype` — rethink from scratch |
| "Add a flag to change the output format" | `/feedback` — tweak code directly |
| "I haven't built anything yet" | `/prototype` — start from the beginning |

## What Not to Do

- Don't run the full brainstorm. If the founder just wants a tweak, don't ask them 20 discovery questions.
- Don't regenerate the whole project. Modify what changed.
- Don't skip the decision log. Even small changes should be tracked — "why did we change the output format?" matters later.
- Don't accept vague feedback. If they say "it's not good", ask: "What specifically wasn't useful? Walk me through when you tried it."
