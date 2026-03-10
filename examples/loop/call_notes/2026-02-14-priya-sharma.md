---
who: Priya Sharma, founder/PM at Carto (seed, B2B logistics SaaS, YC W25)
date: 2026-02-14
context: User interview, 28 min call
---

Priya is a technical founder doing PM work herself. No dedicated PM on the team (5 engineers, her, one designer).

**Opening question — hardest part of building right now:**
"Knowing whether what we're building is actually what customers want. Not in a philosophical sense — I mean literally: I talked to a customer two months ago, they told me something specific, and now I can't remember if we built that thing or something adjacent to it."

She showed me her Notion setup. Call notes folder with ~80 documents. "These are basically useless after two weeks. I can't search them effectively. I don't update them when things change."

**The specific problem she described:**
She does weekly check-ins with 6 design partners. They give feedback. She updates the roadmap mentally, sometimes in Linear, sometimes not. "My PRD for the routing feature had 12 requirements. I wrote it in January. It's now February and we've had 4 customer calls that changed my thinking on at least 3 of them. The PRD says one thing, my head says another, Linear says a third thing."

Biggest pain: "I find out we shipped something wrong when a customer tells me. That's the worst possible feedback loop. Six weeks of engineering work and then 'oh actually we meant X not Y.'"

**On checking code against requirements:**
"That would be insane. I review every PR but I'm looking for bugs, not for 'does this match what the customer asked for.' Those are completely different mental modes. I'm not doing both in a PR review."

She tried using Claude to read call notes and generate tickets. "It works okay but I don't trust it to catch things I care about. It's confident about the wrong things."

**What would change her workflow:**
1. Something that reads all her call notes and surfaces "here are the 5 things customers keep saying that aren't in your current PRD"
2. Before she writes a ticket, a check: "based on your last 3 calls with this customer, does this ticket address what they actually asked for?"
3. A weekly digest: "here's what shipped this week, here's whether it matches what customers asked for"

**On paying:**
"I'd pay for this today if it worked. What's the price? $100/month? I spend more than that in engineering time building the wrong thing."

**Interesting signal:**
She mentioned that her biggest mistakes have been PRDs that were written from a single customer's feedback and presented as universal. "I'll have one really vocal customer and I over-index on them. I need something that tells me: this requirement came from one conversation with one person, not from five."

**Quote:**
"I find out we shipped something wrong when a customer tells me. That's the worst possible feedback loop."
