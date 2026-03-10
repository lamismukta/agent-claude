# Signal Synthesizer

Cross-references your usage data with user call notes to evaluate whether your PRD is focused on real signal.

**Type:** Standalone experiment
**Hypothesis:** H6 — Combining usage data + qualitative feedback surfaces insights neither source provides alone
**Confirmed if:** PM finds at least one insight they wouldn't have caught from feedback alone, and agrees the "no signal" PRD items should be deprioritised

## Quick Start

```bash
export ANTHROPIC_API_KEY=your-key
uv run synthesize.py
```

No `uv`? `pip install -r requirements.txt && python synthesize.py`

Runs against included sample data by default. Use your own data for real results:

```bash
uv run synthesize.py --events your_events.json --feedback your_notes.md --prd your_prd.md
```

### What you need

1. **Usage events** (JSON) — product analytics: signups, feature usage, drop-offs, retention. Export from Mixpanel, Amplitude, PostHog, or build a simple JSON yourself.
2. **Call notes** (Markdown) — notes from user interviews, support tickets, or sales calls. Paste from Granola, Notion, Google Docs — whatever you have.
3. **Your PRD** (Markdown) — the roadmap or spec you want to pressure-test against the evidence.

The sample data in `sample_data/` shows the expected format.

## What It Does

Takes your real usage data and user feedback, then evaluates your PRD against that evidence. Classifies every signal:

- **Strong signals** — data and feedback agree. Build this.
- **Data only** — patterns in usage nobody mentioned in calls. Investigate.
- **Feedback only** — things users said with no data support. May be vocal minority.
- **PRD with no signal** — requirements with no supporting evidence. Cut or justify.

Outputs a signal score (1-10) and a markdown report.

## What to Look For

- Does the report surface anything you wouldn't have caught from reading the call notes alone?
- Do the "no signal" PRD items feel right to cut, or do you push back?
- Are the divergence findings (data says one thing, users say another) actionable or confusing?

## How It Works

Three sequential API calls using `claude-opus-4-6`:

1. **Analyse** usage events → patterns with severity
2. **Extract** qualitative signals from call notes
3. **Synthesize** → classify signals, evaluate PRD coverage

All three use structured JSON output (`output_config`). The synthesis step uses adaptive thinking for cross-source reasoning.

See `../../HYPOTHESES.md` for the full Loop hypothesis set.
