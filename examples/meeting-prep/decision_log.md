# Decision Log

## Session 1 — 2026-03-08

### Context
First brainstorm. Founder (YC W26) has weekly investor calls and spends 30+ minutes prepping each one — googling the person, their fund, recent deals. Wants an AI tool to automate the research and produce a one-page briefing.

### Hypotheses Tested
- H1: Founders spend 30+ min prepping for investor calls → ⏳ untested (founder's own experience, need to validate with others)
- H2: Web search can surface relevant intel → ⏳ untested (need prototype)
- H3: Structured briefing > raw info dump → ⏳ untested (need user feedback)
- H4: Used before every call, not just big ones → ⏳ untested
- H5: Tool runs in under 60 seconds → ⏳ untested (need prototype)

### Key Decisions
- **Scope to CLI tool.** Founder is technical, wants speed over polish. `python briefing.py "Sarah Chen" "Sequoia"` — no web UI for v1.
- **One person + one company as input.** Not a batch tool. One call, one briefing.
- **Output is markdown.** Renders in terminal, easy to paste into notes app.
- **Sections: Overview, Recent News, Key People, Talking Points.** Four sections, not more. The talking points section is the differentiator — raw google doesn't give you that.
- **Use web search server-side tool.** No API keys to manage, no scraping. Claude searches and synthesises.
- **Sonnet 4.6 for the prototype.** Fast and cheap. Upgrade to Opus if reasoning quality on talking points isn't good enough.

### What Changed
- Initial idea was "investor CRM with AI" — scoped down to single-call briefing generator after discussing what the founder actually does manually today.

### Open Questions
- Should the tool remember previous calls with the same person? (Out of scope for v1, but worth testing if founders ask for it.)
- Is web search alone enough, or do we need LinkedIn/Crunchbase APIs? (Test with prototype first.)
