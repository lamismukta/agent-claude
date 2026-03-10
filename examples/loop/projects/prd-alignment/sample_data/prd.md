# Product Requirements: Loop MVP — Call Notes Ingestion

## Problem
PMs write PRDs from memory after user calls, losing the original evidence. Requirements drift from what users actually said.

## User
Head of Product or founder/PM at a seed-to-Series A B2B SaaS company. Running 4-8 user calls/week. Notes in Notion or Google Docs.

## Core Capabilities

1. **Call note ingestion** — paste or upload a markdown call note, Loop extracts discrete feedback items
2. **Requirement extraction** — for each call, output a structured list of user needs with supporting quotes
3. **PRD gap analysis** — given a PRD, flag requirements that have no user evidence
4. **Slack integration** — weekly digest delivered to a Slack channel summarising new feedback themes

## Out of Scope
- PR diff analysis
- Ticket generation
- Real-time alerts
- Mobile app

## Architecture
- Web app with Notion OAuth for call note import
- Claude API for extraction and analysis
- Slack webhook for weekly digest

## Success Criteria
- Extracts feedback items from a call note in under 10 seconds
- PM agrees with 80%+ of extracted items
- Weekly digest delivered on schedule

## Internationalisation
- Support for English, Spanish, and French call notes in v1
