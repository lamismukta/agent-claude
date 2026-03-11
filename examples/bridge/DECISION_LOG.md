# Decision Log — Bridge

## Session 1 — 2026-03-10

### Context
First sprint. Founder has a clear problem (knowledge gets lost across browsing sessions) and a demo flow in mind (browser extension → lists → suggestions → projects).

### Hypotheses Tested
- H1: Knowledge loss across tabs/chats → ⏳ untested
- H2: AI suggestions surface novel content → ⏳ untested
- H3: Growing doc > disposable chat → ⏳ untested
- H4: Browser extension is the right surface → ⏳ untested
- H5: Two-click capture is fast enough → ⏳ untested

### Key Decisions
- Prototype as Chrome extension (not standalone app or CLI) — matches where the capture happens
- Local storage only for v1 — no backend, no sync, keeps scope tight
- Append-only document model — the core differentiator vs ChatGPT/Claude projects
- Human-in-the-loop: suggestions are proposed, never auto-added
- Claude Opus 4.6 for suggestion quality — this runs in the background, latency isn't critical

### What Changed
- Wrote HYPOTHESES.md with 5 hypotheses, 3 testable with prototype
- Wrote PRODUCT_REQUIREMENTS.md scoped to test H2 (suggestion quality) as the riskiest assumption
- Deferred: proactive/scheduled generation, multi-device sync, embedding search, voice interface

### Open Questions
- How to handle API key management in a browser extension? (security concern)
- Should suggestions be generated on-demand or pre-cached when the list changes?
- What's the right number of suggestions per generation? (started with 5-10, may need tuning)

---
