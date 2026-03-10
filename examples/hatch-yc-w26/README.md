# Hatch — Example Test Case

Fictional YC W26 application for testing the agent-claude workflow.

## What's here

| File | What it is |
|------|------------|
| `yc-application.md` | Full YC application |
| `call-notes.md` | Three user calls from after the application |

## How to use

1. Run `/onboard`
2. Paste `yc-application.md` when prompted for your YC application
3. Copy `call-notes.md` to `call_notes/` in your project
4. Run `/sprint`

## What the flow should surface

**The riskiest technical hypothesis:** Does Claude's categorization stay accurate enough across different firm contexts — different industries, different chart of accounts structures — that bookkeepers trust it without checking everything? The pilot data (3,000 transactions, ~50% time reduction) is promising but only covers 4 firms. The Janet problem (one user who checks everything anyway) is the real test.

**The obvious prototype to build:** A script that takes a QuickBooks transaction export (CSV), a sample of the firm's historical categories (also CSV), and outputs categorized transactions with confidence scores. Tests accuracy directly on real data. Priya can run it against her pilot firms' exports.

**Tensions to surface in brainstorm:**
- Solo founder looking for a co-founder — should YC app have a stronger technical narrative?
- Two segments emerging: accounting firms (B2B, target market) vs. sole traders (B2C, bigger market, different product) — which to focus?
- Client email feature is what pilots want most but hasn't been built — is that the thing to sprint on?
- Audit trail request (Marcus) is a trust/liability issue, not just a feature request

**The call notes add:**
- Segment split (business clients vs individual clients — Sarah's firm doesn't need client emails at all)
- Trust/adoption gap is behavioural not technical (Janet problem)
- Inbound demand from unexpected segment (Tom)
