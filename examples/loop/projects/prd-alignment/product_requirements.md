# Product Requirements: PRD Alignment Evaluator

## Problem
PMs write PRDs after user calls, but the PRD often fails to capture everything users said — and adds requirements nobody asked for. By the time engineers ship, nobody can trace the original user evidence. Loop needs to prove it can catch this drift reliably.

## Why LLM?
- **LLM is good at:** reading two documents simultaneously and identifying semantic gaps — what's in A that's missing from B, and what's in B with no grounding in A
- **LLM is NOT needed for:** storing or retrieving documents, ticket creation, sending alerts
- **What was impossible before:** cross-document semantic comparison at this level of nuance. Keyword search can't catch "customer said 'confusing onboarding'" mapping to (or not mapping to) a PRD requirement about "streamlined first-run experience"

## User
- **Who:** Jamie Torres — solo PM/founder, running 6-8 user calls/week, writing PRDs in Notion, no PM tooling budget
- **Trigger:** CLI command after writing a PRD — `uv run align.py --feedback call_notes.md --prd prd.md`
- **Output:** Alignment report printed to stdout + saved as `alignment_report.md`. Shows: which feedback items are covered, which are missing, which PRD requirements have no user evidence, overall score.

## Core Capabilities

1. Extract discrete feedback items from call notes — each user need, pain point, or request as a structured object with the underlying need and (where available) frequency
2. For each feedback item, evaluate whether the PRD addresses it — with the specific PRD section if yes, or a concrete gap description if no
3. Flag PRD requirements that have no grounding in user evidence — things that were added without user validation
4. Produce an overall alignment score (1-10) with a 2-3 sentence summary
5. Format output as readable markdown report

## Architecture
- **Type:** Multi-step pipeline (two sequential API calls)
- **Autonomy:** Fully automated — no human-in-the-loop for this prototype
- **Model:** claude-sonnet-4-6 — reasoning quality matters here, but Sonnet is sufficient. Upgrade to Opus if evaluation accuracy on complex PRDs is insufficient.

## Scope
- **In scope:** call notes (markdown) + PRD (markdown) → alignment report
- **Out of scope:** Notion/Confluence integration, ticket generation, PR diff analysis, multi-user PRDs, real-time alerts
- **Constraints:** Both input files must be markdown. No auth, no external APIs beyond Anthropic.

## Hypothesis Under Test
- **Hypothesis:** H4 — LLM can evaluate PRD-to-feedback alignment and surface gaps a PM would agree are real
- **Confirmed if:** PM rates 8+ out of 10 flagged gaps as "real and worth fixing", and evaluator catches 8+ out of 10 gaps the PM identifies independently
- **Killed if:** More than 3/10 flagged gaps are false positives, or PM finds obvious gaps the evaluator missed

## Success Criteria
- Given call_notes.md + prd.md, produces a report in under 30 seconds
- Report identifies all major user needs from the call notes as discrete items
- Flags at least one gap that a PM would say "yes, that's a real miss"
- Flags at least one unsupported requirement if one exists
- Score correlates with PM's intuition about PRD quality
