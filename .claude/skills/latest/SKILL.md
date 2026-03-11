---
name: latest
description: "Show where you are on the current product. Reads HYPOTHESES.md, DECISION_LOG.md, and PRODUCT_REQUIREMENTS.md and gives a clean summary: what's been confirmed, what's still untested, and what to validate with users next. Use when a founder says 'where are we', 'what's left to validate', 'catch me up', 'what should I be doing', or 'what's the latest'."
---

# /latest — Where You Are

Give the founder a fast, honest read on where the product stands. Read the artifacts, synthesise the state, surface what matters next. No fluff.

## How It Works

1. **Read everything.**
   - `HYPOTHESES.md` — current status of each hypothesis (root level)
   - `DECISION_LOG.md` — what's changed and why across sessions (root level)
   - `projects/*/PRODUCT_REQUIREMENTS.md` — what's been specced and built, for each project
   - Key source files in `projects/*/` — what's actually in the codebase

2. **Output a clean status summary.** Use this format:

---

## [product name] — [date]

**Where you are**
[2-3 sentences. The core bet, what exists, what the evidence says so far. Write like you're catching up a friend — honest, not formal.]

**What you know**
- ✅ [assumption] — [one line of evidence]

**What you don't know yet**
- ⏳ [assumption] — [why this matters]

**Ideas for next**
[Suggestions, not assignments. "You could...", "It might be worth...", "The quickest way to find out would be...". Frame as options, not tasks. If there's an obvious highest-value move, say so — but the founder decides.]

---

3. **If nothing has been built yet** (no HYPOTHESES.md): tell the founder what's missing and point them at `/sprint`.

## Tone

- Catch them up like a sharp friend, not a project manager.
- Suggest, don't assign. "You could try X" not "Do X next."
- Be honest about uncertainty. "The prototype looked good on synthetic data, but that's not the same as real users" is more useful than "H1: untested."
- Keep it short. If two things are confirmed and three aren't, say that — don't pad it.
- Don't hedge. "It's hard to say" is not useful. Read the artifacts and make a call — just frame it as your read, not an order.
