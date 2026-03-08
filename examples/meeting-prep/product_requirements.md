# Product Requirements: Meeting Prep Briefing

## Problem
YC founders spend 30+ minutes before each investor call manually googling the person, their fund, and recent deals. The research is repetitive, scattered across tabs, and never saved — they start from scratch every time.

## User
- **Who:** Technical YC founder (2-4 person team), has 3-5 investor calls per week.
- **Trigger:** CLI command: `python briefing.py "Sarah Chen" "Sequoia Capital"`
- **Output:** A one-page markdown briefing printed to stdout and saved to `briefings/`.

## Core Capabilities
1. Accept a person name and company/fund name as input.
2. Search the web for: the person's background, the fund's recent investments, recent news about both, and any mutual connections or shared interests.
3. Generate a structured one-page briefing with four sections:
   - **Person Overview** — role, background, investment focus, notable takes.
   - **Fund/Company Overview** — stage, sector focus, recent deals, fund size.
   - **Recent News** — last 6 months, 3-5 items max.
   - **Talking Points** — 3 conversation starters grounded in the research (not generic).
4. Save the briefing as `briefings/{person_name}_{date}.md`.

## Tools Required
- Web search (server-side) — for researching the person and fund.
- File system — for saving the briefing to `briefings/`.

## Architecture
- **Type:** Single API call with server-side web search tool.
- **Autonomy:** Fully autonomous — no human-in-the-loop needed. It's a research task, not a decision task.
- **Model:** Sonnet 4.6 — fast and cheap for a prototype. The talking points section may need Opus if quality isn't high enough.

## Hypothesis Under Test
- **Hypothesis:** H2 — Web search can surface relevant, recent intel about a person and their fund.
- **Confirmed if:** 8 out of 10 test runs produce briefings with at least 3 accurate, recent facts about the person/fund.
- **Killed if:** Most briefings contain stale, generic, or hallucinated information that a founder wouldn't trust.

## Scope
- **In scope:** Single person + company lookup, markdown output, saved to file.
- **Out of scope:** Batch processing, memory of previous calls, CRM integration, web UI, LinkedIn/Crunchbase API integration.
- **Constraints:** No paid APIs beyond Anthropic. Web search only. Must run in under 60 seconds.

## Success Criteria
- Given a real investor name and fund, produces a briefing in under 60 seconds.
- Briefing contains at least 3 recent, verifiable facts (not hallucinated).
- Talking points are specific to the person — not generic "ask about their portfolio" filler.
- Output is clean markdown that renders in a terminal and a notes app.
