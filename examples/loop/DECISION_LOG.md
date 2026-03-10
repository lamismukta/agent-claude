# Decision Log — Loop

## Session 1 — 2026-02-17

### Context
First sprint. Jamie has done 12 user interviews and has 4 design partners. No product built yet. Goal: identify the riskiest prototype to build first.

### Hypotheses Tested
- H1: ✅ confirmed — 4-5 hrs/week cited by multiple PMs, consistent across interviews
- H2: ✅ confirmed — call→PRD identified as primary failure point by 10/12 interviewees

### Key Decisions
- **Build H4 first (PRD-to-feedback evaluator), not H3 (call note extraction).** H3 (extraction) is table stakes — the output is just a list. H4 (evaluation) is the actual value claim: "Loop catches things you missed." That's what people will pay for. If H4 works, H3 is a prerequisite we can build after.
- **Input format: markdown files.** Don't try to integrate with Notion/Confluence yet — too much auth/API complexity for a prototype. Design partners can export their notes as markdown. This isolates the AI question from the integration question.
- **Target score threshold: 8/10.** If a PM rates 8+/10 gaps as "real and important," the evaluator is useful. Below that, it'll erode trust.
- **Named project `prd-alignment`.** Scoped to H4 only. Subsequent experiments (H5, H6, H7) get their own project folders.

### What Changed
- Created `HYPOTHESES.md` with H1–H7
- Started `projects/prd-alignment/`

### Open Questions
- What's the right sample size to validate H4? 5 PRDs feels thin. May need 10+ before drawing conclusions.
- Should the evaluator explain its reasoning or just output scores? Lean toward explanation for now — PMs need to trust the output, and scores alone won't build trust.

---

## Session 2 — 2026-02-24

### Context
Pivoted away from H4 (PRD-to-feedback alignment) after building it. The core problem: you can't build a reliable signal map from what users *say* alone. Feedback is biased toward vocal users and doesn't reflect actual behaviour. H4 was invalidated as a standalone prototype.

### Hypothesis Updates
- H4: ❌ invalidated — feedback-only alignment is insufficient. A PM could have a PRD that perfectly mirrors what users said and still be building the wrong thing.
- H6: promoted to first build — cross-referencing usage data with qualitative feedback is the real value claim.

### Key Decisions
- **Build H6 (signal synthesizer) instead of H4.** Three-step pipeline: analyse events → extract feedback → synthesize. Sample data uses Fieldwork (Marcus Chen's product) — intentional mismatches between data and feedback make the demo compelling.
- **Kept PRD evaluation as part of synthesis.** The output still checks the PRD, but against the combined signal, not just feedback.

### What Changed
- Deleted `projects/prd-alignment/`
- Created `projects/signal-synthesizer/`
- H4 marked invalidated in `HYPOTHESES.md`

### Open Questions
- Should the synthesizer also suggest what to *add* to the PRD, or just flag gaps? Lean toward flagging only for v1 — generation is easier to get wrong.
- Is JSON the right format for event data? Worth testing with a CSV input as an alternative.
