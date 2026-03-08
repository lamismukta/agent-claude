---
name: onboard
description: "Set up a new project for prototyping with Claude. Use when someone clones the repo, says 'get started', 'set up', 'onboard', or is clearly new and hasn't run any skills yet. Checks prerequisites, creates the directory structure, imports any existing context the founder already has, and gets them ready to run /brainstorm or /prototype."
---

# /onboard — Get Set Up

Get a founder from clone to ready in under 2 minutes. Check prerequisites, create the project structure, import any existing context they already have, and point them at the right next step.

Most YC founders aren't starting from zero — they have call recordings, product docs, pitch decks, maybe working code. Onboard is where all of that gets pulled into the project so `/brainstorm` and `/prototype` can build on it.

## How It Works

1. **Check prerequisites.**
   - Verify `ANTHROPIC_API_KEY` is set. If not, walk them through getting one from [console.anthropic.com](https://console.anthropic.com).
   - Check Python is available (`python3 --version`). The prototypes `/build` generates are Python by default.
   - Check `uv` is available (`uv --version`). Recommend it for running prototypes without dependency headaches — `pip install uv` or `curl -LsSf https://astral.sh/uv/install.sh | sh`. Not required, but makes `/build` output easier to run.

2. **Create the project structure.**
   Create a working directory for the founder's project (or use the current directory if they already have one). Set up:
   ```
   call_notes/        ← User interview notes (manual or Granola)
   existing_docs/     ← Imported product docs, pitch decks, research (only created if they have docs to import)
   ```
   Don't create `hypotheses.md` or `product_requirements.md` — those are outputs of `/brainstorm` and `/prd`.

3. **Granola setup (optional).**
   Ask: "Do you record user calls with Granola? If so, I can wire it up to pull transcripts automatically."
   - If yes: write `.claude/mcp_servers.json` directly with the Granola config:
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
     Then tell them: "Granola is configured. Restart Claude Code (Ctrl+C, then `claude`) to pick it up. After that, `/brainstorm` will automatically pull your latest call transcripts."
   - If yes + they want historical calls: use `list_meetings` to show their recent calls and let them pick which ones to import. Save them to `call_notes/` with frontmatter. This seeds the brainstorm with real user data from day one.
   - If no: skip. They can paste notes into `call_notes/` manually, or just talk through the brainstorm without notes.
   - If `.claude/mcp_servers.json` already exists (e.g., they have other MCP servers), read it and add the `granola` entry to the existing `mcpServers` object rather than overwriting.

4. **Import existing context.**
   Ask: "Do you have any existing material I should know about? Things like:"
   - Product docs, PRDs, or pitch decks
   - User research notes or interview transcripts
   - Existing code or a working prototype
   - Notion exports, Google Docs, or markdown files

   **How to handle each type:**

   | What they have | What to do |
   |---------------|------------|
   | **Product docs / PRD / pitch deck** | Save to `existing_docs/`. Read and summarise the key points — problem, user, current scope. Note gaps that `/brainstorm` should fill. |
   | **User research / interview notes** | Save to `call_notes/` with frontmatter (who, date, context). These feed directly into `/brainstorm`. |
   | **Existing code** | Ask where it lives. Read the codebase — entry point, dependencies, what it does. Summarise for context. Don't move or copy the code; just note the path. `/build` can work from it later. |
   | **Notion / Google Docs** | Ask them to paste the content or export as markdown. Save to `existing_docs/`. |
   | **Nothing yet** | That's fine — skip this step entirely. |

   If they import docs, summarise what you learned: "From your docs, I can see you're building X for Y. Your main open question seems to be Z. Does that sound right?" This bridges into `/brainstorm` with context already loaded.

5. **Quick context.**
   Ask one question: "What are you building, in one sentence?" Don't run the full brainstorm — just capture enough to make the next step feel warm. Save their answer as a note for context.

   If they already imported docs in step 4, skip this — you already have context.

6. **Point to the next step.**
   Tailor the recommendation based on what they imported:

   **If they have existing code:**
   ```
   You're set up. You have existing code at [path] — I've read through it.

   /prototype  — Rethink from scratch (brainstorm → new spec → new code)
   /prd        — Write a spec from your existing code (document what you have)
   /feedback   — Iterate on what you've got (update spec + code together)
   /brainstorm — Step back and test your assumptions before building more

   If your code works but needs direction: /brainstorm
   If your code works and you want to iterate: /feedback
   ```

   **If they have docs but no code:**
   ```
   You're set up. I've read your docs — here's what I understand: [1-line summary].

   /prototype   — Go from your existing context to working code
   /brainstorm  — Pressure-test your assumptions first (recommended)

   Start with: /brainstorm
   ```

   **If they're starting fresh:**
   ```
   You're set up. Here's what you can do:

   /prototype   — Go straight from idea to working code
   /brainstorm  — Think through your idea first (recommended)

   Start with: /brainstorm
   ```

## What Not to Do

- Don't run the brainstorm. Just set up, import, and hand off.
- Don't install heavy dependencies. The prototype is local Python — `uv` is the only nice-to-have.
- Don't require Granola. It's an enhancement, not a prerequisite.
- Don't require existing docs. Many founders are genuinely starting from scratch — that's fine.
- Don't rewrite or restructure their existing docs. Save them as-is — `/brainstorm` will read them.
- Don't over-explain. The founder is technical — check the boxes and get out of the way.
