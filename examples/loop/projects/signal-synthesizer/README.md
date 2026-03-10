# Signal Synthesizer

Cross-references usage data with qualitative feedback to evaluate whether a PRD is focused on real signal.

**Type:** Standalone experiment
**Hypothesis:** H6 — Combining usage data + qualitative feedback surfaces insights neither source provides alone
**Confirmed if:** PM finds at least one insight they wouldn't have caught from feedback alone, and agrees the "no signal" PRD items should be deprioritised

## Quick Start

```bash
export ANTHROPIC_API_KEY=your-key
uv run synthesize.py
```

No `uv`? `pip install -r requirements.txt && python synthesize.py`

Runs against the included sample data by default. To use your own:

```bash
uv run synthesize.py --events your_events.json --feedback your_notes.md --prd your_prd.md
```

## What It Does

Takes usage event data, call notes, and a PRD. Finds where data and feedback agree (build this), where they diverge (investigate), and what's in the PRD with no supporting evidence (cut this).

## What to Look For

- Does the report surface anything the PM wouldn't have caught from reading the call notes alone?
- Do the "no signal" PRD items feel right to cut, or does the PM push back?
- Are the divergence findings (data says one thing, users say another) actionable or confusing?

## How It Works

Three sequential API calls:

1. **Analyse** usage events → patterns with severity
2. **Extract** qualitative signals from call notes
3. **Synthesize** → classify signals, evaluate PRD coverage

All three use structured JSON output. The synthesis step uses adaptive thinking for cross-source reasoning.

See `../../HYPOTHESES.md` for the full Loop hypothesis set.
