---
name: add-capability
description: "Add a new capability to your Claude setup — connect tools, build new skills, or extend what Claude can do for you. Use when a founder says 'I want Claude to also do X', 'can you add email', 'I want a competitor research skill', 'help me set up calendar integration', 'write a weekly roundup', or anything about extending beyond the core sprint workflow."
---

# /add-capability — Extend Your Setup

Help the founder add a new capability to their Claude setup. This might mean configuring an MCP integration, building a new skill, or both.

## How It Works

1. **Find out what they want.** If they haven't specified, present the common options:

   ```
   What would you like to add?

   Integrations (connect tools Claude can use):
   a) Email and calendar — read/draft emails, create events (Gmail + Google Calendar)
   b) Notion — read and write to your workspace (if not already set up)
   c) Granola — pull user call transcripts (if not already set up)

   New skills (things Claude learns to do on command):
   d) Competitor research — deep-dive on a competitor on demand
   e) Weekly roundup — summarise progress, decisions, and learnings from the week
   f) Investor research — profile an investor before a meeting
   g) Customer outreach — draft personalised outreach emails
   h) Something else — describe what you want
   ```

2. **Handle the selection.** Each capability has a different setup path — see below.

3. **Test it.** After setup, run a quick test so the founder sees it working before they close the session.

---

## Integrations

### Email and Calendar (Gmail + Google Calendar)

Gmail and Google Calendar connect through Claude.ai's Google Workspace integration — not via `mcp_servers.json`. Once connected in Claude.ai settings, they're automatically available in Claude Code under Anthropic's managed `claude.ai` MCP namespace (no extra config needed).

**Setup:**
1. Go to [Claude settings](https://claude.ai/settings) → Integrations
2. Connect Gmail and/or Google Calendar under Google Workspace
3. Restart Claude Code — the tools will be available immediately
4. See [Anthropic's connector guide](https://support.claude.com/en/articles/10166901-use-google-workspace-connectors) if you hit issues (Team/Enterprise plans require an admin to enable first)

**Quick test:** Ask "what's on my calendar tomorrow?" or "show me my last 3 unread emails."

### Notion

See the Notion setup in `/onboard` — same config. If it's already in `.claude/mcp_servers.json`, say so.

### Granola

See the Granola setup in `/onboard`. If it's already configured, say so.

---

## New Skills

For each new skill, use `/skill-creator` to build it properly — write a SKILL.md, test it with a real example, and iterate. Below are starting briefs for the common ones.

### Competitor Research

**What it does:** Takes a competitor name, runs structured web research across their product, pricing, reviews, and recent news, and produces a one-page summary with a strengths/weaknesses table and talking points.

**Trigger:** "Research [competitor]", "what does [competitor] do", "how does [competitor] compare to us"

**Key outputs:** Product overview, pricing, what customers say they love/hate (from reviews), recent news, and 3 competitive angles.

**Start with:** Ask the founder which competitors matter most, then run `/skill-creator` to build `competitor-research/SKILL.md`. The skill should use Claude's web search tool.

---

### Weekly Roundup

**What it does:** Every week, synthesises what happened — decisions made (from `DECISION_LOG.md`), hypotheses updated (from `HYPOTHESES.md`), sprint changes, and user calls. Produces a short markdown summary suitable for a team update or personal log.

**Trigger:** "Write my weekly roundup", "what did we ship this week", "summarise the week"

**Key outputs:** What shipped, what changed in the hypotheses, what users said, what's next.

**Start with:** Run `/skill-creator` to build `weekly-roundup/SKILL.md`. The skill reads `DECISION_LOG.md`, `HYPOTHESES.md`, and `call_notes/` for the current week, then synthesises.

---

### Investor Research

**What it does:** Takes an investor name and fund, searches for their thesis, recent investments, public takes, and portfolio. Produces a pre-meeting briefing with talking points tailored to what they care about.

**Trigger:** "Research [investor]", "prep me for my meeting with [investor]", "who is [investor]"

**Key outputs:** Background, investment thesis, recent deals, public takes, 3 tailored talking points.

**Start with:** This is similar to the `examples/meeting-prep/` example. Run `/skill-creator` to build `investor-research/SKILL.md`, or adapt the meeting-prep example directly.

---

### Customer Outreach

**What it does:** Drafts a personalised cold outreach email to a potential customer. Takes the person's name, company, and role, researches them if web search is available, and writes a short email grounded in their specific context — not a template.

**Trigger:** "Draft an outreach email to [person]", "write to [company] about [thing]", "help me reach out to [person]"

**Key outputs:** Subject line + email body. Optionally drafts directly to Gmail if the integration is configured.

**Start with:** Run `/skill-creator` to build `customer-outreach/SKILL.md`. If Gmail MCP is configured, the skill can draft the email directly rather than just generating text.

---

### Something Else

If the founder describes a custom capability:

1. Listen to what they want to do.
2. Check if an existing MCP server covers it (search at [modelcontextprotocol.io](https://modelcontextprotocol.io) if needed).
3. If it's an integration: add the MCP config.
4. If it's a new behaviour: run `/skill-creator` to build a SKILL.md for it.

---

## After Setup

Always end with:
1. A quick test showing the capability working.
2. One sentence on how to use it going forward ("Say `/competitor-research [name]` any time you want a deep-dive on a competitor.").
3. An offer to add another capability or return to `/sprint`.
