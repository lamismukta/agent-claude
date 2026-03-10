---
name: status
description: "Show where you are on the current product. Reads hypotheses.md, decision_log.md, and product_requirements.md and gives a clean summary: what's been confirmed, what's still untested, and what to validate with users next. Use when a founder says 'where are we', 'what's left to validate', 'catch me up', or 'what should I be doing'."
---

# /status — Where You Are

Give the founder a fast, honest read on where the product stands. Read the artifacts, synthesise the state, surface what matters next. No fluff.

## How It Works

1. **Read everything.**
   - `hypotheses.md` — current status of each hypothesis
   - `decision_log.md` — what's changed and why across sessions
   - `product_requirements.md` — what's been specced and built
   - Any source files — what's actually in the codebase

2. **Output a clean status summary.** Use this format:

---

## Status — [product name] — [date]

**What you're building**
[One sentence — the core bet, in plain language.]

**What's been confirmed**
- ✅ H2: [assumption] — [one line of evidence]
- ✅ H4: [assumption] — [one line of evidence]

**What's still untested**
- ⏳ H1: [assumption] — [why it matters if wrong]
- ⏳ H3: [assumption] — [why it matters if wrong]

**What to validate with users**
Conversations to have before the next sprint:
- Ask [who]: [specific question] — tests H1
- Show [who] the output and ask: [specific question] — tests H3

**What to build next**
[One sentence — the most valuable next prototype or feature, based on what's untested.]

---

3. **Write it to `status.md`** in the working directory so it's easy to reference later. Tell the founder: "I've written this to `status.md`."

4. **If nothing has been built yet** (no hypotheses.md): tell the founder what's missing and point them at `/sprint`.

## What Not to Do

- Don't re-run the brainstorm. Just read and report.
- Don't pad the output. If two hypotheses are confirmed and three are untested, say that clearly.
- Don't hedge. "It's hard to say" is not useful. Read the artifacts and make a call.
