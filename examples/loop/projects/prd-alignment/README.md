# PRD Alignment Evaluator

Checks whether a PRD is grounded in user feedback. Surfaces gaps (user needs that didn't make it in) and unsupported requirements (things in the PRD nobody asked for).

## Quick Start

```bash
export ANTHROPIC_API_KEY=your-key
uv run align.py
```

No `uv`? Use `pip install -r requirements.txt && python align.py` instead.

Runs against the included sample data by default. To use your own files:

```bash
uv run align.py --feedback your_call_notes.md --prd your_prd.md
```

## What You Get

```
# PRD Alignment Report

Score: 4/10 [████░░░░░░]

The PRD captures extraction and gap analysis well but misses the most
frequently cited pain: post-ship validation (mentioned by all 3 users).
It also includes an internationalisation requirement with no user evidence.

## Feedback Coverage

✅ F1 — Requirement extraction from call notes
✅ F2 — Weekly digest of feedback themes
❌ F3 — Post-ship validation: checking if what shipped matches what was asked
   *Not addressed anywhere in the PRD*
❌ F4 — Source attribution: tagging requirements with the calls they came from
❌ F5 — Single-source warning: flagging requirements based on only one user

## Gaps — User Needs Not in the PRD

- Users mentioned post-ship validation (3/3 users) but the PRD does not address it
- Users mentioned source attribution for requirements (2/3 users) but the PRD does not address it

## Unsupported Requirements — No User Evidence

- Internationalisation (English, Spanish, French) — no user raised this
```

## How It Works

Two API calls:

1. **Extract** — reads call notes, outputs discrete feedback items as structured JSON
2. **Evaluate** — compares feedback items against the PRD, scores alignment, flags gaps

Both calls use `claude-sonnet-4-6`. The evaluate step uses structured JSON output for reliable parsing.

## What It Tests

**H4:** Can LLM evaluate PRD-to-feedback alignment and surface gaps a PM would agree are real?

Confirmed if: PM rates 8+/10 flagged gaps as real. See `../../hypotheses.md` for the full list of experiments Loop is running.
