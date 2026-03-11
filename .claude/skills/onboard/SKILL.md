---
name: onboard
description: "Set up a new project for prototyping with Claude. Use when someone clones the repo, says 'get started', 'set up', 'onboard', or is clearly new and hasn't run any skills yet. Reads their YC application, asks where they are now, understands their codebase, sets up integrations, and gets them ready to run /sprint."
---

# /onboard — Get Set Up

Onboard a YC founder in under 5 minutes. Read their YC application, understand where they are now, get their codebase, set up integrations, and point them at the right next step.

This is not a cold-start flow. Every YC founder has a YC application — that document contains everything needed to understand the company. Start there.

---

## How It Works

Ask questions **one at a time**. Wait for each answer before moving on. The goal: get to `/sprint` as fast as possible.

**While the founder is answering questions, run prerequisites silently in the background** (Step 5). Don't wait for the end — check API key, Python, and uv as soon as the conversation starts.

### 1. Welcome + YC application

> "Welcome — I'm going to help you build and test your ideas. Let's get set up.
>
> First thing I need: your YC application. It has the context I need to understand what you're building. Paste it here or drop the file path."

Don't ask any other questions yet. Wait for the YC application.

If they don't have it handy, or want to try with a sample, point them to:
> "No worries — there's a sample in `examples/loop/existing_docs/yc-application.md` you can use to try the flow."

**While reading their application**, silently create the project structure and save the YC app:
- `mkdir -p call_notes existing_docs existing_code`
- Save to `existing_docs/yc-application.md`

Don't create `HYPOTHESES.md` or `PRODUCT_REQUIREMENTS.md` — those are outputs of `/sprint`.

---

### 2. Synthesise and ask what's changed

Read the application carefully. Extract:
- **Problem** — what pain are they solving, for whom
- **Solution** — what they've built or are building
- **Traction** — what they've validated, who's using it, revenue
- **Team** — backgrounds, why this team for this problem
- **What they've already built** — working code, prototype, manual process
- **Open bets** — what assumptions they haven't validated yet

Then synthesise and ask one question:

> "Here's what I'm taking from your application: [problem in one line]. You're building [solution] for [user]. You've got [traction/what exists]. The big open question seems to be [what they haven't figured out yet].
>
> **What's changed since then? What's your traction, where is your product, and what are your biggest risks?**"

This is the only discovery question. Wait for the answer — it tells you where they are and what to focus on.

Also ask: **"Do you have any user data — analytics, usage logs, CSV exports — that we could look at?"** Even rough data (Mixpanel exports, database queries, spreadsheets) can inform what to build. Note what they have for later.

---

### 3. Codebase

Ask: "Do you have a codebase? Share a GitHub URL or local path — or skip if you're starting fresh."

**If they skip:** Note it. `/sprint` will build from scratch. Move on.

**If GitHub URL:**
- Try to clone it: `gh repo clone <url>` (if `gh` CLI is available)
- Or read the key files via WebFetch on the raw GitHub URLs: README, main entry point, package.json/pyproject.toml

**If local path:**
- **Try hard to find it.** If the path doesn't exist exactly as given, try variations: expand `~`, check common locations (`~/Projects/`, `~/Code/`, `~/repos/`, `~/Documents/`), try with and without trailing slashes, check case sensitivity. Use `ls` on parent directories to find close matches. Don't give up after one failed path — the founder knows their repo exists, so find it.
- Once found, do a thorough read. Don't skim — actually explore:
  - `ls` the root directory
  - Read README, main entry point, config files (package.json, pyproject.toml, Cargo.toml, etc.)
  - `ls` key subdirectories (src/, lib/, app/, components/, etc.)
  - Read 2-3 core files beyond the entry point

**Create `existing_code/codebase-notes.md`** with a structured summary:

```markdown
# Codebase Notes — [repo name]

**Repo:** [path or URL]
**Language:** [Python/TypeScript/etc.]
**Framework:** [if applicable]

## Structure
[Key directories and what they contain]

## What's Built
[What functionality exists and works]

## Architecture
[How it's structured — monolith, microservices, CLI, web app, etc.]

## Entry Points
[Main files, how to run it]

## Dependencies
[Key packages/libraries]

## What's Missing or Incomplete
[Gaps, TODOs, rough edges]

## Notes for /sprint
[Anything relevant for building on top of this — conventions to follow, patterns in use, where new code should go]
```

This persists across sessions so `/sprint` doesn't have to re-read the whole codebase every time.

Note the repo path. `/sprint` will ask whether each experiment should extend this codebase or run standalone — that decision happens per-project, not upfront.

---

### 4. Integrations

Ask: "Do you use Granola to record user calls? Skip if not."

**If yes:**
Write `.mcp.json` in the project root (this is gitignored — each user creates their own):
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

If `.mcp.json` already exists, read it and add to the existing `mcpServers` object — don't overwrite.

**Then pull existing notes.** After configuring Granola, immediately pull recent meeting notes into `call_notes/`. Run `list_meetings` and fetch any that look like user interviews, demos, or relevant calls. Save each as `call_notes/YYYY-MM-DD-<short-description>.md` with frontmatter:
```markdown
---
who: [Name, Role at Company]
date: [YYYY-MM-DD]
context: [User interview / Demo / Intro call, N min]
source: granola
---
```

Tell the founder what you pulled:
> "I pulled [N] meeting notes from Granola — [brief list]. They're in `call_notes/` and `/sprint` will use them."

Do NOT tell them to restart yet — defer to the end.

If they also use Notion for user research, ask:
> "Do you also use Notion for user research? I can connect that too — skip if not."

If yes, they'll need an internal integration token:
> "Go to https://www.notion.so/my-integrations — create an internal integration, copy the token, and share it here."

Then add to `.mcp.json` (merge with existing `mcpServers` if the file already exists):
```json
{
  "notion": {
    "command": "npx",
    "args": ["-y", "@notionhq/notion-mcp-server"],
    "env": {
      "OPENAPI_MCP_HEADERS": "{\"Authorization\":\"Bearer ntn_THEIR_TOKEN\",\"Notion-Version\":\"2022-06-28\"}"
    }
  }
}
```

After configuring, remind them:
> "One more thing — in Notion, go to each page you want me to access → **...** → **Connections** → add your integration. I can only see pages that are explicitly shared with the integration."

**If no Granola / skip:**
> "No problem. If you have any user interview notes, drop them in `call_notes/` — txt, md, or paste them in. `/sprint` will pick them up."

Move on.

---

### 5. Prerequisites (silent — run in background)

**Start these checks as soon as the conversation begins.** Don't wait for a dedicated step — run them in the background while asking questions. Only surface issues when they're relevant or at the end.

Check silently:
- `echo ${ANTHROPIC_API_KEY:+set}` — API key set?
- `python3 --version` — Python available?
- `uv --version` — uv available?

**If API key not set:**
> "You'll need an ANTHROPIC_API_KEY to run prototypes. Get one at console.anthropic.com → API Keys. Once you have it, share it here and I'll add it to your `~/.zshrc` so it persists."
If they share it: run both commands so the key is live immediately:
```bash
echo 'export ANTHROPIC_API_KEY=<key>' >> ~/.zshrc
export ANTHROPIC_API_KEY=<key>
```
Confirm it's set. Don't echo the key back into conversation.

**If uv not installed:**
Install it directly: `curl -LsSf https://astral.sh/uv/install.sh | sh`. Tell them what you're doing. Don't ask.

**If Python missing:** Tell them to install Python 3.11+ from python.org.

---

### 6. Save what you learned

Create `DECISION_LOG.md` with the first entry — this is how `/sprint` picks up where onboard left off:

```markdown
## Onboard — [date]

### Context
[One line: who they are, what they're building]

### Where they are now
[What the founder said in response to the one question — traction, product status, concerns. Use their words.]

### Codebase
[Repo path/URL and one-line summary, or "No codebase yet"]

### User data available
[What data they mentioned — analytics, usage logs, exports — or "None yet"]

### Integrations
[What was configured — Granola, Notion — or "None"]

### What to focus on
[Your read on the most important thing to build or test, based on everything above]
```

This is the bridge between onboard and sprint. Without it, `/sprint` re-asks questions the founder already answered.

---

### 7. Ready — point to `/sprint`

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

Always end with a skills overview:

> | Skill | What it does |
> |-------|-------------|
> | `/sprint` | Run this any time — first build, feedback, iteration, rethink. Reads your context and figures out the right questions. |
> | `/latest` | Where you are — confirmed hypotheses, what still needs validating |

**If integrations were configured:**
> One last thing: restart Claude Code to pick up the [Granola/Notion] integration. Press Ctrl+C, then run `claude` again.

**If prereqs had issues**, report them here concisely — don't make the founder solve problems before they know what they're building.

---

## What Not to Do

- Don't start with prerequisites. Start with the YC application.
- Don't ask "what are you building." You'll know after reading their YC app.
- Don't run the brainstorm or write hypotheses. That's `/sprint`.
- Don't ask the founder to restart Claude Code mid-conversation. Always defer to the end.
- Don't over-explain. They're busy. Check the boxes and get out of the way.
- Never ask for API keys in chat for testing purposes. Always use environment variables.
