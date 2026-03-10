# Product Requirements: Signal Synthesizer

## Problem
PMs make roadmap decisions based on what users say in calls, but what users say and what they do are often different. A user who asks for "better export" may rarely export. A feature used by 47% of users may never come up in interviews. Building from feedback alone produces roadmaps full of vocal-minority requests and blind spots.

## Why LLM?
- **LLM is good at:** reading two different-format evidence sources simultaneously and reasoning about what they imply together — something a spreadsheet or keyword search can't do
- **LLM is NOT needed for:** storing event data, scheduling calls, creating tickets
- **What was impossible before:** cross-source semantic reasoning at this level — identifying that "users complain about confusing onboarding" maps to "63% → 22% drop at step 3," or that 47% mobile usage is conspicuously absent from three user interviews

## User
- **Who:** Jamie Torres — solo PM/founder, running user calls weekly, has basic product analytics, writing PRD in Notion
- **Trigger:** Before writing or updating a roadmap — `uv run synthesize.py --events metrics.json --feedback notes.md --prd roadmap.md`
- **Output:** Signal report showing strong signals (build), data-only signals (investigate), feedback-only signals (validate), and PRD items with no evidence (cut)

## Core Capabilities
1. Analyse a JSON event log and extract significant patterns with severity ratings
2. Extract discrete pain points from call notes with supporting quotes and frequency
3. Cross-reference both sources: classify signals as confirmed (both), data-only, feedback-only
4. Evaluate PRD coverage against the synthesized signal map
5. Flag PRD items with no support from either source
6. Output a structured signal report in markdown

## Architecture
- **Type:** Three-step sequential pipeline
- **Autonomy:** Fully automated
- **Model:** claude-sonnet-4-6 with adaptive thinking on the synthesis step

## Scope
- **In scope:** JSON event log + markdown call notes + markdown PRD → signal report
- **Out of scope:** Live analytics integrations, Mixpanel/Amplitude connectors, automated PRD rewriting, ticket generation
- **Constraints:** Event log must be JSON; call notes and PRD must be markdown

## Hypothesis Under Test
- **Hypothesis:** H6 — combining usage data + qualitative feedback surfaces insights neither source provides alone, and produces a more reliable signal for prioritisation
- **Confirmed if:** PM reviews the report and identifies at least one finding they wouldn't have caught from feedback alone, and agrees the "no signal" PRD items should be deprioritised
- **Killed if:** The synthesis produces obvious findings only, or the cross-referencing adds no value over reading the two sources separately
