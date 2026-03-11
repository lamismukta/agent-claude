# Product Requirements: Bridge

## Problem

People learning, researching, or exploring a topic face two bad options:

1. **Manual trawling** — open tabs, bookmark articles, copy-paste into notes. Slow, scattered, full of gaps you don't know you have.
2. **AI chat** — powerful but reactive. You have to ask the right question, re-give context every session, and the output is disposable — each response regenerates rather than building on a working document. No connection to what you're actually trying to achieve.

The result: useful knowledge gets lost across tabs, chats, and docs. Nobody is proactively helping you fill gaps or connecting new information to your goals.

## Why LLM?

- **LLM is good at:** understanding what a topic list implies you care about, finding related content you wouldn't think to search for, synthesising across sources into a coherent working document, identifying gaps in your knowledge
- **LLM is NOT needed for:** storing bookmarks, rendering a UI, managing user accounts
- **What was impossible before:** proactively generating relevant suggestions from a simple topic list — inferring intent, finding connections between topics, and surfacing what you don't know you don't know

## User

- **Who:** Curious generalist — founder, student, or self-directed learner who is actively exploring 2-3 topics at once. Comfortable with a browser, not necessarily technical.
- **Trigger:** Browsing the web, finds something interesting → adds it to a Bridge list via browser extension. Or: opens Bridge directly to check suggestions and build out a project.
- **Output:** A growing, structured document per project — not a chat log. New content is appended and organised, never regenerated from scratch. Suggestions appear proactively.

## Core Capabilities

1. **Browser extension: capture to list.** User clicks the extension, picks a list (or creates one), and adds a topic/URL/snippet. Two clicks, no context switching. Lists are visible in the extension popup.
2. **Generate suggestions for a list.** Given a list of topics, generate 5-10 related items the user probably hasn't thought of. Each suggestion includes: what it is, why it's relevant to the list, and a source link. User can accept (add to list), dismiss, or save for later.
3. **Create a project from a list.** Turn a topic list into a structured research project with sections, key questions to answer, and a reading order. This becomes the working document — future content gets filed into the right section, not dumped at the bottom.
4. **Append, don't regenerate.** When new content is added or suggestions are accepted, update the working document in place. Add to the relevant section. Never blow away what's already there.
5. **Web search for depth.** When generating suggestions or building a project, search the web for recent, relevant content — articles, papers, threads, videos. Cite sources.

## Tools Required

- Web search — for finding relevant content, articles, and sources when generating suggestions
- Browser extension APIs — for the capture flow (Chrome extension manifest v3)
- Local storage or lightweight backend — for persisting lists and projects

## Architecture

- **Type:** Multi-step workflow (suggestion generation is a pipeline: list → infer intent → search → rank → format)
- **Autonomy:** Human-in-the-loop — Bridge suggests, user accepts/dismisses. Nothing is added to the working document without user action.
- **Model:** claude-opus-4-6 — suggestion quality matters more than speed here. The user isn't waiting in a chat; suggestions can generate in the background.

## Scope

### In scope (prototype)

- Browser extension that captures topics to named lists (Chrome only)
- "Generate suggestions" button per list — calls Claude API with web search to find related content
- "Create project" flow — turns a list into a structured working document (markdown)
- Suggestions UI: accept / dismiss / save for later
- Local storage (extension storage API) for lists and projects — no backend for v1

### Out of scope

- Proactive/scheduled suggestion generation (v2 — requires background workers)
- Multi-device sync (needs a backend)
- Chat interface with documents ("chat with your research")
- Voice interface for project setup
- Embedding/vector search over collected documents
- Mobile app
- Collaboration / sharing

### Constraints

- Chrome extension only (no Firefox/Safari for prototype)
- All AI calls go through Claude API — needs user's API key
- No backend — everything stored in Chrome extension storage
- Suggestions must include source URLs — no hallucinated references

## Hypothesis Under Test

- **Hypothesis:** People who are actively exploring a topic will use AI-generated suggestions to discover content they wouldn't have found on their own — and they'll prefer a growing document over disposable chat responses.
- **Confirmed if:** A test user adds 3+ items to a list, generates suggestions, accepts at least 2 they didn't already know about, and creates a project they refer back to within a week.
- **Killed if:** Users treat suggestions as a novelty but don't accept them into their project, or they prefer to just ask ChatGPT directly because the list→suggest flow feels slower.

## Success Criteria

- Browser extension installs and captures a topic to a list in under 3 seconds
- "Generate suggestions" returns 5-10 relevant items with source links in under 30 seconds
- At least 30% of suggestions are things the user hadn't already considered (self-reported)
- "Create project" produces a structured document with sections, not a flat list
- Adding a new topic to an existing project appends to the right section — never regenerates the whole document

## Demo Flow

1. Install extension → click on an article about YC startups → add "startup fundraising" to a new list called "Startup"
2. Find a language-learning article → add "spaced repetition" to a new list called "Vocab"
3. Open the "Startup" list → press "Generate suggestions" → review 5-10 suggestions (e.g., "SAFE notes", "cap table basics", "YC batch dynamics") → accept 3
4. Open the "Vocab" list → press "Create project" → get a structured document with sections like "Memory Science", "Tools & Methods", "Daily Practice", each with curated content and sources
