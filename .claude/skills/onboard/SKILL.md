---
name: onboard
description: "Set up a new project for prototyping with Claude. Use when someone clones the repo, says 'get started', 'set up', 'onboard', or is clearly new and hasn't run any skills yet. Reads their YC application, asks where they are now, understands their codebase, sets up integrations, and gets them ready to run /sprint."
---

# /onboard — Get Set Up

Onboard a YC founder in under 5 minutes. Read their YC application, understand where they are now, get their codebase, set up integrations, and point them at the right next step.

This is not a cold-start flow. Every YC founder has a YC application — that document contains everything needed to understand the company. Start there.

---

## How It Works

Ask questions **one at a time**. Wait for each answer before moving on.

### 1. Warm welcome

Greet the founder and tell them what's about to happen:

> "Welcome — I'm going to help you move faster with AI. Let's get set up.
>
> First thing I need: your YC application. It has the context I need to understand what you're building. Paste it here or drop the file path."

Don't ask any other questions yet. Wait for the YC application.

If they don't have it handy, or want to try with a sample, point them to:
> "No worries — there's a sample in `examples/yc-application.md` you can use to try the flow."

---

### 2. Read the YC application

Read it carefully. Extract:
- **Problem** — what pain are they solving, for whom
- **Solution** — what they've built or are building
- **Traction** — what they've validated, who's using it, revenue
- **Team** — backgrounds, why this team for this problem
- **What they've already built** — working code, prototype, manual process
- **Open bets** — what assumptions they haven't validated yet

Then synthesise back in 3–4 sentences:
> "Here's what I'm taking from your application: [problem in one line]. You're building [solution] for [user]. You've got [traction/what exists]. The big open question seems to be [what they haven't figured out yet]. Does that capture it?"

Wait for confirmation or correction before moving on.

---

### 3. Three questions (one at a time)

These questions update the YC app context with what's happened since it was written.

**Q1:** "Where are you now — what have you shipped and who's using it?"

Wait for answer. Probe if vague: "Walk me through what exists today."

**Q2:** "What's changed since you wrote the application? Any pivots, surprises, things you thought were true that turned out not to be?"

Wait for answer.

**Q3:** "What's your biggest concern right now — the thing you most need to figure out?"

Wait for answer. This is the most important question. The answer usually points directly at what to build or validate next.

---

### 4. Existing codebase

Ask: "Do you have a codebase? Share a GitHub URL or local path."

**If GitHub URL:**
- Try to clone it: `gh repo clone <url>` (if `gh` CLI is available)
- Or read the key files via WebFetch on the raw GitHub URLs: README, main entry point, package.json/pyproject.toml
- Summarise: what's built, what architecture, what's missing or incomplete

**If local path:**
- Read the directory structure, entry point, dependencies
- Summarise: what it does, what's working, what's rough

**If no codebase yet:**
- Note it. `/sprint` will build from scratch.

Go deeper than a surface summary. If there's a codebase, read the main entry point. Note: "You have [X] built. It looks like [Y] is the next thing to build. Does that feel right?"

---

### 5. Integrations (optional)

Ask: "Do you use Granola to record user calls?"

**If yes:**
Write `.claude/mcp_servers.json`:
```json
{
  "mcpServers": {
    "granola": {
      "command": "npx",
      "args": ["-y", "granola-mcp"]
    }
  }
}
```
Confirm it's written. Do NOT tell them to restart yet — defer to the end.

If they also use Notion for user research, add:
```json
{
  "mcpServers": {
    "granola": { "command": "npx", "args": ["-y", "granola-mcp"] },
    "notion": {
      "command": "npx",
      "args": ["-y", "@notionhq/notion-mcp-server"],
      "env": {
        "OPENAPI_MCP_HEADERS": "{\"Authorization\": \"Bearer ntn_YOUR_TOKEN\", \"Notion-Version\": \"2022-06-28\"}"
      }
    }
  }
}
```

If `.claude/mcp_servers.json` already exists, read it and add to the existing `mcpServers` object — don't overwrite.

**If no:** Skip. Move on.

---

### 6. Prerequisites (silent check)

Run silently, report results concisely:

- `echo ${ANTHROPIC_API_KEY:+set}` — check if API key is set
- `python3 --version` — check Python
- `uv --version` — check uv

**If API key not set:**
> "You'll need an ANTHROPIC_API_KEY to run prototypes. Get one at console.anthropic.com → API Keys. Once you have it, share it here and I'll add it to your `~/.zshrc` so it persists."
If they share it: run both commands so the key is live immediately without needing a restart:
```bash
echo 'export ANTHROPIC_API_KEY=<key>' >> ~/.zshrc
export ANTHROPIC_API_KEY=<key>
```
Confirm it's set. Don't echo the key back into conversation.

**If uv not installed:**
Install it directly: `curl -LsSf https://astral.sh/uv/install.sh | sh`. Tell them what you're doing. Don't ask.

**If Python missing:** Tell them to install Python 3.11+ from python.org.

---

### 7. Create project structure

```
call_notes/        ← User interview notes
existing_docs/     ← YC app + any other docs (save the YC app here)
```

Save the YC application to `existing_docs/yc-application.md` so it's available for future sessions.

Don't create `hypotheses.md` or `product_requirements.md` — those are outputs of `/sprint`.

---

### 8. Point to the next step

Tailor based on what you learned:

**If they have a codebase and a clear concern:**
> "You're set up. I've read through your code and your YC app.
>
> You have [X] built. Your biggest concern is [Y].
>
> Run `/sprint` — I'll work from what you have, not from scratch."

**If they have a codebase but unclear direction:**
> "You're set up. You have [X] built.
>
> Run `/sprint` — it'll read what you have and help you figure out what to build next."

**If no codebase:**
> "You're set up. No code yet — that's fine.
>
> Run `/sprint` — we'll go from your YC application to working code."

Always end with a skills overview so the founder knows what they're working with:

> Here's what you can run:
>
> | Skill | What it does |
> |-------|-------------|
> | `/sprint` | Run this any time — first build, feedback, iteration, rethink. Reads your context and figures out the right questions. |
> | `/status` | Where you are — confirmed hypotheses, what still needs validating |

**If integrations were configured:** Add after the table:
> One last thing: restart Claude Code to pick up the [Granola/Notion] integration. Press Ctrl+C, then run `claude` again.

---

## What Not to Do

- Don't start with prerequisites. Start with the YC application.
- Don't ask "what are you building." You'll know after reading their YC app.
- Don't run the brainstorm or write hypotheses. That's `/sprint`.
- Don't ask the founder to restart Claude Code mid-conversation. Always defer to the end.
- Don't over-explain. They're busy. Check the boxes and get out of the way.
- Never ask for API keys in chat for testing purposes. Always use environment variables.
