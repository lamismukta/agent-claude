# agent-claude

Claude Code skills for stress testing your ideas and getting you a working AI prototype. Runs a discovery conversation, writes hypotheses, specs a PRD, and generates a complete runnable project. Iterates with you.

## Prerequisites

- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) installed (`npm install -g @anthropic-ai/claude-code`)
- `ANTHROPIC_API_KEY` set in your environment ([get one here](https://console.anthropic.com))
- Python 3.11+
- [`uv`](https://docs.astral.sh/uv/) recommended — `curl -LsSf https://astral.sh/uv/install.sh | sh`

## Setup

```bash
git clone https://github.com/lamismukta/agent-claude.git
cd agent-claude
claude
```

Then run `/onboard`.

## Skills

### `/onboard` — get set up

Run once when you start. Gets Claude up to speed on your company and sets up the tools it needs.

- **Reads your YC application** — understands your problem, solution, traction, and open questions without you having to explain from scratch
- **Asks what's changed** — three targeted questions to capture what's happened since you wrote the app: what you've shipped, what surprised you, what you're most worried about
- **Reads your codebase** — give it a GitHub URL or local path; it summarises what's built, what's missing, and what to work from
- **Sets up integrations** — connects [Granola](https://granola.ai) for call recordings and [Notion](https://notion.so) for research notes via MCP; easy to extend with other tools
- **Checks prerequisites** — API key, Python, uv; installs what's missing

---

### `/sprint` — build and iterate

The main skill. Run it any time — new idea, just talked to users, just tested something, want to rethink direction. It reads your context and figures out the right questions.

**First run (no existing project):**
- Interviews you using YC-style questions to surface your riskiest assumptions
- Analyses any call notes or user data you have — finds patterns, surfaces what users are actually saying
- Writes `HYPOTHESES.md` — a prioritised list of your assumptions, each tagged with how to test it: 🗣️ talk to users, or 🛠️ build to test
- Scopes the riskiest hypothesis into a buildable experiment in `projects/<name>/`
- Generates a complete runnable prototype — Python, one command to run
- Logs everything in `DECISION_LOG.md` — what you decided and why

**Subsequent runs (existing project):**
- Asks what happened since last time — feedback, surprises, what broke
- Updates hypotheses (confirmed ✅, invalidated ❌, or refined)
- Scopes the next experiment based on what's still untested
- Appends to the decision log — never overwrites, always accumulates

---

### `/status` — where you are

Read-only snapshot. Useful before a call or when you've been heads-down and want to resurface.

- Which hypotheses are confirmed, which are still untested, which were invalidated
- What to validate with users before the next sprint
- What to build next

---

## Artifact trail

Every sprint produces or updates:

| File | What it is |
|------|-----------|
| `HYPOTHESES.md` | Your assumptions, ordered by risk. Each one is tagged 🗣️ (validate in conversation) or 🛠️ (build an experiment). Updated every sprint. |
| `DECISION_LOG.md` | Append-only record of what changed and why. Captures pivots, invalidated bets, and what you learned. Never overwritten. |
| `projects/<name>/PRODUCT_REQUIREMENTS.md` | Spec for one experiment — scoped to test a single hypothesis. |
| `projects/<name>/` | Runnable code: entry point, `pyproject.toml`, README. `uv run <entrypoint>.py` and it works. |

Code is disposable. The artifact trail isn't — it's your decision history.

## Going further

Easy to extend — ask Claude to add:

**More integrations:** email, calendar, CRM, Slack

**Skills:** research competitors and investors, automate sales outreach, draft weekly progress report

## Model

Works best in **Claude Code with Sonnet 4.6**. Generated prototypes pick the right model for the task — Claude decides based on the spec.

## Resources

- [Claude API docs](https://platform.claude.com/docs/en/home)
- [Claude Agent SDK](https://github.com/anthropics/claude-agent-sdk-python)
- [Claude Code docs](https://docs.anthropic.com/en/docs/claude-code)
