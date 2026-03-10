# User Call Notes — Loop Research (Feb 2026)

## Marcus Chen, Head of Product, Fieldwork — Feb 10

Core pain: discovering features were built wrong only when customers complain, weeks after shipping.

"The problem isn't writing the ticket. The problem is six weeks later when I'm looking at what shipped and thinking — wait, is this actually what they asked for?"

Described a specific miss: customers complained about confusing onboarding. Wrote ticket for onboarding checklist. Engineers shipped it. Churn didn't improve. Six months later discovered users actually wanted to import existing data on day 1 — the checklist was irrelevant. "The call notes said that. I just missed it when I wrote the ticket."

Wants:
- Something that reads call notes and tells him: here's what users actually asked for
- Reads PRD and tells him: here's what you forgot to include
- Reads the PR and tells him: this doesn't address what users said
- A weekly digest showing what shipped vs what was asked for

Spends 4-5 hrs/week on translation work (call notes → tickets → PRD updates).
Would pay $200-500/month.

Key quote: "The three handoffs are where everything dies. Call to PRD. PRD to ticket. Ticket to code. Each one loses something."

---

## Priya Sharma, founder/PM, Carto (YC W25) — Feb 14

Solo PM/founder, 5 engineers. Biggest pain: finding out something was built wrong when a customer tells her.

"I find out we shipped something wrong when a customer tells me. That's the worst possible feedback loop."

Her PRD for the routing feature had 12 requirements written in January. By February, 4 customer calls had changed her thinking on 3 of them. PRD, Linear tickets, and her mental model were all saying different things.

Biggest source of frustration: over-indexing on one vocal customer. "I'll have one really vocal customer and I write a requirement that I present as universal. I need something that tells me: this came from one conversation, not five."

Also flagged: she does PR reviews for bugs, not for "does this match what the customer asked for." Those are different mental modes and she can't do both.

Wants:
- Surface things customers keep saying that aren't in the current PRD
- Before writing a ticket: check if it addresses what the customer actually asked for
- Weekly digest: what shipped, does it match what customers asked for
- Indication of how many customers a requirement is based on (single source vs multiple)

Would pay $100/month today.

---

## Sofia Reyes, PM, Harbour (seed, B2B compliance SaaS) — Feb 12

Similar pattern. Key additional feedback:

Wants to know source/frequency for each requirement: "when I'm writing a PRD I want to say this requirement came from 3 calls not 1, so I can push back when engineering wants to descope it."

Currently copies-pastes quotes from Notion into PRD comments as evidence. Very manual. "It takes me an extra hour per PRD just to attach the evidence."

Flagged that she often can't find the original call note when engineers push back on a requirement. "I know I heard this somewhere but I can't prove it."

Would want: every PRD requirement tagged with the source calls it came from, with the specific quote.
