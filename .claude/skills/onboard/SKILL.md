---
name: onboard
description: "Set up a new project for prototyping with Claude. Use when someone clones the repo, says 'get started', 'set up', 'onboard', or is clearly new and hasn't run any skills yet. Checks prerequisites, creates the directory structure, and gets the founder ready to run /brainstorm or /prototype."
---

# /onboard — Get Set Up

Get a founder from clone to ready in under 2 minutes. Check prerequisites, create the project structure, optionally wire up Granola for call notes, and point them at the right next step.

## How It Works

1. **Check prerequisites.**
   - Verify `ANTHROPIC_API_KEY` is set. If not, walk them through getting one from [console.anthropic.com](https://console.anthropic.com).
   - Check Python is available (`python3 --version`). The prototypes `/build` generates are Python by default.
   - Check `uv` is available (`uv --version`). Recommend it for running prototypes without dependency headaches — `pip install uv` or `curl -LsSf https://astral.sh/uv/install.sh | sh`. Not required, but makes `/build` output easier to run.

2. **Create the project structure.**
   Create a working directory for the founder's project (or use the current directory if they already have one). Set up:
   ```
   call_notes/        ← User interview notes (manual or Granola)
   ```
   Don't create `hypotheses.md` or `product_requirements.md` — those are outputs of `/brainstorm` and `/prd`.

3. **Granola setup (optional).**
   Ask: "Do you record user calls with Granola? If so, I can wire it up to pull transcripts automatically."
   - If yes: copy `.claude/mcp_servers.json.example` to `.claude/mcp_servers.json`, remove the `_comment` line, and tell them to restart Claude Code.
   - If no: skip. They can paste notes into `call_notes/` manually, or just talk through the brainstorm without notes.

4. **Quick context.**
   Ask one question: "What are you building, in one sentence?" Don't run the full brainstorm — just capture enough to make the next step feel warm. Save their answer as a note for context.

5. **Point to the next step.**
   Print a clear summary:
   ```
   You're set up. Here's what you can do:

   /brainstorm  — Think through your idea (recommended first step)
   /prototype   — Go straight from idea to working code
   /prd         — Write a spec if you already know what to build
   /build       — Generate code from an existing spec

   Start with: /brainstorm
   ```

## What Not to Do

- Don't run the brainstorm. Just set up and hand off.
- Don't install heavy dependencies. The prototype is local Python — `uv` is the only nice-to-have.
- Don't require Granola. It's an enhancement, not a prerequisite.
- Don't over-explain. The founder is technical — check the boxes and get out of the way.
