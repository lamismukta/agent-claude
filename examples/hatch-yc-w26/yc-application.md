# Hatch — YC W26 Application

> Fictional example company for testing the agent-claude workflow.
> Paste this when `/onboard` asks for your YC application.

---

## Founders

**Priya Anand** — sole founder
Previously PM at QuickBooks for 3 years (SMB accounting product). Before that, operations at a 6-person accounting firm while finishing her degree — she did the books herself. Writes Python; not a software engineer but can build.

No co-founder yet. Looking for a technical co-founder who's worked in fintech or accounting software.

Technical work: all code written by Priya. No outside contractors.

---

## Company

**Company name:** Hatch

**One-liner:** AI bookkeeper for small accounting firms

**What are you making?**
Accounting firms with 1–5 staff spend 60–70% of their time on transaction categorization — pulling bank feeds, deciding which category each transaction belongs to, flagging anomalies for client review. It's the most time-consuming part of bookkeeping and the most automatable.

Hatch connects to QuickBooks and Xero, pulls uncategorized transactions, and uses Claude to categorize them with high confidence — learning from how each firm has categorized similar transactions before. Anything Claude isn't confident about gets flagged for human review with a suggested category and a one-line explanation. Firms review the flagged items (usually 5–15% of transactions) rather than all of them.

The second feature, not yet built: drafting the monthly client email. Accountants spend 2–3 hours per client writing "here's what happened with your money this month." Hatch will generate a first draft from the categorized transactions.

**Location:** London, UK. Would move to SF for YC.

---

## Progress

**How far along are you?**
Working CLI tool in Python. Connects to QuickBooks API, pulls transactions, sends batches to Claude with firm-specific context, returns categories + confidence scores + flags. 6 pilot users across 4 accounting firms. Processing real transactions in production — ~3,000 transactions categorized in the last 6 weeks.

**How long working on this?**
4 months. Full-time for the last 2.

**Tech stack:**
Python, Claude API (claude-sonnet-4-6 for categorization, claude-haiku-4-5 for the confidence scoring pass), QuickBooks API, SQLite for storing firm-specific category patterns. Built largely with Claude Code — roughly 60% of the codebase was written or substantially revised through Claude Code sessions.

**Are people using your product?**
Yes — 6 users across 4 firms. All pilots, no payment yet.

**Revenue:**
No. 3 LOIs at £150/user/month. One firm (Steadman & Co, 3 users) has committed verbally to paying when we add the client email feature.

---

## Idea

**Why this idea?**
I watched bookkeepers at the firm I worked at spend entire Tuesdays on transaction categorization. They called it "the slog." When I joined QuickBooks I assumed we'd automate it — we never did, because the categorization accuracy wasn't good enough to trust. Claude is the first model I've tried where the accuracy is high enough that a bookkeeper would rather review the exceptions than do it all manually.

**Domain expertise?**
3 years as a PM on the SMB product at QuickBooks. I've seen the data on where firms spend time. I was also a bookkeeper myself — I know what "wrong category" feels like from the firm side and the client side.

**How do you know people need it?**
Talked to 23 bookkeepers and firm owners before building. 19 of them said categorization was their biggest time sink. 4 of the 6 pilots came from those conversations. Two of the pilot firms reduced their categorization time by ~50% in the first month (self-reported).

**Competitors:**
Botkeeper, Pilot.com (both target larger firms, higher price point, full outsourcing). QuickBooks and Xero have basic auto-categorization (rule-based, low accuracy, doesn't learn). None of them have tackled the client communication piece.

What we understand that they don't: small firms don't want full outsourcing, they want a tool that makes their existing staff faster. The relationship with the client is the product — they're not going to hand that to a faceless service.

**How will you make money?**
SaaS, per-user pricing. £150/user/month. A 3-person firm is £450/month — cheaper than hiring a part-time admin. Upsell: client email drafting at higher tier.

Target: 50 firms × 3 users average = 150 users × £150 = £22,500 MRR within 12 months of launch.

**Category:** B2B SaaS / AI

**Other ideas considered:**
- AI for VAT return preparation (UK-specific, smaller market)
- AI that monitors client bank accounts for fraud signals and alerts the accountant
- Automated payroll reconciliation

---

## Equity

Legal entity: No, not yet incorporated.
Investment: No.
Fundraising: No.

---

## Other

**What convinced you to apply to YC?**
Two portfolio founders I know (both B2B SaaS) said YC was the only accelerator that genuinely helped with go-to-market in the US. The accounting software market is dominated by US companies even in the UK — I need to understand that market and YC is the fastest path.
