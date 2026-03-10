# Test Flow — Hatch

Use this to test `/onboard` end-to-end, including Notion integration. Simulates a founder who's used Notion for user research and has Granola for call recordings.

---

## What this tests

- `/onboard` cold start (no HYPOTHESES.md, no DECISION_LOG.md)
- YC application read + synthesis
- Notion MCP setup
- Granola MCP setup
- Prereq checks (API key, uv, Python)
- Handoff to `/sprint`

---

## Step 1 — Start fresh

Run from the `examples/hatch/` directory (or point Claude at it):

```bash
cd examples/hatch
claude
```

Or from the repo root, just start `claude` and tell it you're working on the Hatch example.

---

## Step 2 — Run /onboard

```
/onboard
```

Expected: Claude asks for your YC application first. Don't give it anything else yet.

**Paste or reference the YC application:**
> `existing_docs/yc-application.md`

Claude should read it and synthesise back something like:
> "Here's what I'm taking from your application: PMs spend too much time integrating feedback into PRDs. You're building Loop — an AI layer for product managers. You've got 12 user interviews and 4 design partners. The big open question seems to be whether the AI evaluation is accurate enough to trust. Does that capture it?"

*(It should recognise Sofia + Daniel, the hiring platform angle, the supply problem.)*

---

## Step 3 — Answer the three questions

**Q1: Where are you now?**
> "We've placed 3 engineers in 6 weeks. 7 founders with active pipelines, 22 engineers listed. Daniel built the whole thing solo — match flow, dashboards, referral mechanic. We're live but still free."

**Q2: What's changed since you wrote the app?**
> "The referral mechanic is working better than expected — 64% of signups come through referral, not cold. But engineer reactivation is a real problem. Someone signs up, gets listed, and then just disappears. We don't know how to keep supply warm."

**Q3: What's your biggest concern?**
> "Engineer ghosting after the intro call. Arjun at Vesper called it out — he set up 2 intros, both went well, then silence. He has no visibility into whether the engineer is still active. I think we need to show some kind of activity signal, but I don't want to make engineers feel tracked."

---

## Step 4 — Share the codebase

When Claude asks for the codebase:
> "It's not public yet — Daniel's still cleaning it up. But I can share the call notes folder: `call_notes/`"

Claude should read the Arjun Mehta call notes and summarise key themes.

---

## Step 5 — Notion integration

When Claude asks about Granola:
> "Yes, I use Granola for all my user calls."

Expected: Claude writes `.claude/mcp_servers.json` with `granola-mcp`.

Then: "Do you use Notion for your research notes?"
> "Yes — I have a Notion workspace with all my user research. My token is `ntn_TEST_TOKEN_REPLACE_ME`."

Expected: Claude adds Notion to the same `mcp_servers.json` file (merges, doesn't overwrite). Should prompt you to restart Claude Code at the end, not mid-conversation.

---

## Step 6 — Prereqs

Claude should silently check:
- `ANTHROPIC_API_KEY` — if not set, it'll ask you to share it
- `uv` — if not installed, it installs it directly
- `python3` — if missing, points to python.org

---

## Step 7 — Handoff

Expected output at the end:

> "You're set up. I've read through the Arjun call and your YC app.
>
> You have a working match flow with 3 placed hires. Your biggest concern is engineer ghosting — you need activity signals without making engineers feel tracked.
>
> Run `/sprint` — I'll work from what you have, not from scratch."

Followed by the skills table and the Granola/Notion restart reminder.

---

## Step 8 — Sprint

After `/onboard`, run:

```
/sprint
```

Expected: Claude reads the call notes, synthesises hypotheses, asks 2–3 targeted questions about what to build, then scopes a prototype. The riskiest thing to test is H_: "Activity signals increase founder trust without reducing engineer willingness to be listed."

---

## What to watch for

| Check | What good looks like |
|-------|---------------------|
| YC app synthesis | Accurate 3–4 sentence summary, names Sofia and Daniel, identifies supply problem as the open question |
| Questions | Targeted, not generic. Q3 answer should visibly shape the handoff. |
| Notion config | MCP file created with both granola + notion. Token is placeholder, not echoed back in chat. |
| Prereq check | Silent — no fanfare if everything is installed |
| Handoff | Specific to what you told it, not generic "run /sprint" boilerplate |
| /sprint | Reads call_notes/ directory, references Arjun's feedback by name |
