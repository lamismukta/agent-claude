# Signal Synthesizer

Cross-references usage data with user feedback to evaluate whether a PRD is focused on real signal. Finds where data and calls agree (build this), where they diverge (investigate), and what's in the PRD with no evidence at all (cut this).

## Quick Start

```bash
export ANTHROPIC_API_KEY=your-key
uv run synthesize.py
```

No `uv`? Use `pip install -r requirements.txt && python synthesize.py` instead.

Runs against the included sample data by default. To use your own:

```bash
uv run synthesize.py --events your_events.json --feedback your_notes.md --prd your_prd.md
```

## What You Get

```
# Signal Report

PRD signal score: 5/10 ████░░░░░░

The PRD correctly prioritises onboarding — the strongest confirmed signal.
But Priority 2 (team collaboration) has no support from either data or calls,
and the mobile app (47% of users) isn't addressed at all.

## Strong Signals — Data + Feedback Agree

**Data import failure at onboarding step 3** [✅ in PRD]
  Data: 63% → 22% drop between step 2 and step 3
  Feedback: Mentioned by 3/3 users — "I tried three times and gave up"

## Data Only — Not Mentioned in Calls

**Mobile app has significant usage** [❌ missing from PRD]
  Data: 47% of users open the mobile app — the second most-used surface
  → High usage with no feedback suggests users are adapted to its limitations.
     Worth a dedicated call to understand if this is friction or satisfaction.

## Feedback Only — Not Reflected in Usage Data

**Better reporting and export** [✅ in PRD]
  Feedback: Mentioned by 3/3 users — "I need to show my boss a weekly summary"
  → Only 6% of users actually use export. May be a real need that's
     currently unmet (so no usage), or a vocal minority. Run one focused
     session before building.

## No Signal — Reconsider These PRD Items

- Team collaboration features: 8% usage, not mentioned in any call
- API integrations: 2% usage, not mentioned in any call
```

## How It Works

Three sequential API calls:

1. **Analyse** usage events → patterns with severity (what does the data tell us?)
2. **Extract** qualitative signals from call notes (what do users say?)
3. **Synthesize** → classify signals, evaluate PRD coverage

All three calls use structured JSON output. The synthesis step uses adaptive thinking for cross-source reasoning.

## What It Tests

**H6:** Does combining usage data + qualitative feedback surface insights that neither source provides alone?

See `../../HYPOTHESES.md` for the full Loop hypothesis set.
