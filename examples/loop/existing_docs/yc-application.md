# YC Application — Loop (W26)

**Founder:** Jamie Torres
**Company:** Loop
**One-liner:** Loop keeps your product decisions grounded in user feedback — from call to code.

---

## Describe what your company does in 50 characters or less.

AI that checks if your code matches your users.

## What is your company going to make?

Loop is an AI layer that sits between user feedback and your codebase. It reads your call notes and PRDs, extracts what users actually asked for, and checks whether what your engineers shipped addressed it.

Most early-stage startups lose signal between the user call and the deployed feature. A PM hears "customers are churning because onboarding is confusing" on a call, writes a ticket, the engineer builds something, and three months later the churn rate hasn't moved. Nobody knows why. The call notes are in Notion. The ticket is closed. The PRD has drifted. The original context is gone.

Loop closes the loop. It extracts structured requirements from call notes, evaluates whether the PRD captures them, and flags when code ships without addressing the original pain.

## Why did you pick this idea to work on?

I spent four years as a PM at Stripe on the Billing team. We had 40 engineers, weekly user research, and a rigorous spec process — and we still shipped features that missed what users asked for. The drift happened slowly, across three handoffs: call notes → PRD, PRD → ticket, ticket → code. Each handoff lost context.

At smaller companies, where there's one PM (or no PM, just a technical founder), the problem is worse. You're doing user calls, writing specs, reviewing PRs, and managing roadmap simultaneously. You can't hold all the context. Something slips.

LLMs can read all of it simultaneously. That's the unlock.

## How far along are you?

No product yet. I left Stripe three months ago. I have:
- A clear thesis (validated with 12 PM interviews — see call notes)
- 4 design partners who've committed to using a prototype (two at seed-stage B2B SaaS companies, one at a Series A marketplace, one at a YC W25 company)
- A working understanding of the technical approach (structured extraction + evaluator scoring)

The biggest open question is whether LLM evaluation of PRD-to-feedback alignment is accurate enough to be trusted. That's what I'm building first.

## What's your revenue model?

SaaS. Target: PMs and technical founders at seed-to-Series A startups. Initial pricing: $49/seat/month. Design partners have said they'd pay $100+/month if it works.

## What is the biggest risk for your company?

Accuracy. If Loop misses real gaps or flags false ones, PMs will stop trusting it within a week. The core question is whether LLM evaluation is calibrated well enough that a PM would agree with its output 80%+ of the time.

The secondary risk is workflow integration — the tool only works if it's connected to where call notes and PRDs actually live (Notion, Confluence, Google Docs, Granola). MCP makes this easier than it would have been a year ago.

## Who are your competitors?

**Dovetail, Notion AI, Confluence AI** — all do generation (summarise notes, draft specs) but none do evaluation (check if spec matches notes). Generation is a feature. Evaluation is a product.

**Hex, Mixpanel** — usage analytics but no connection to qualitative feedback.

**Linear, Jira** — ticket management with some AI assist for writing. No cross-artifact consistency checking.

The gap is the eval layer: nothing today closes the loop between what users said and what shipped.

## Why now?

YC recently put out a request for an AI PM — an AI system that can handle the synthesis, prioritisation, and spec-writing work that PMs currently do manually. The bottleneck they identified is exactly what Loop addresses: the signal loss between user calls and what gets built. The tools to do this well (LLMs that can reason across documents, MCP integrations with Notion and Linear) didn't exist two years ago.

## Tell us about your team.

Jamie Torres, solo founder. PM at Stripe 2021–2025 (Billing and Revenue Recognition). Before that: product at two seed-stage startups. CS undergrad, MIT.

I've spent four years watching the call-to-code signal degrade in real time. I'm not technical enough to build this alone long-term, but I can prototype in Python and I understand the PM workflow deeply enough to spec what "good" looks like. Looking for a technical co-founder with ML or infra background.
