# MVP & PRD Canon

Reference material for the `/prd` skill. These frameworks inform how you scope and write product requirements. Internalise the principles — don't lecture the founder about them.

---

## Michael Seibel: How to Plan an MVP (YC Startup School)

### The Goal

"The first thing you can give to the very first set of users you want to target in order to see if you can deliver any value at all."

Not a product. Not a demo. The minimum thing that delivers real value to a real person.

### Lean MVP Rules

- **Build in weeks, not months.** If it takes longer, you're building too much.
- **Extremely limited scope.** Focus on one user's highest-order problem. Ignore everything else.
- **Can be non-software.** A landing page + spreadsheet is a valid MVP. So is a manual process you do by hand.
- **It's a base to iterate from** — not your vision. Don't fall in love with it.

### Scoping Framework: Hold Tightly / Hold Loosely

| Hold tightly | Hold loosely |
|-------------|-------------|
| The problem you're solving | Your solution approach |
| Your target customer | Features, architecture, tech stack |

This prevents founders from pivoting the problem when they should iterate the solution.

### Launch Timeline Hacks

1. **Time-box your spec.** Define what's buildable in your deadline (e.g., 3 weeks), then commit only to those items.
2. **Write it down.** Undocumented features creep in. A written spec prevents this.
3. **Cut ruthlessly at midpoint.** Remove non-essential features. If everything seems essential, cut "important" ones anyway.
4. **Get something out.** "Once you get anything out in the world the momentum to keep going is extremely strong."

### Iterate ≠ Pivot

- **Iterate:** Improve your solution for the same customer and problem.
- **Pivot:** Change the problem you're solving. Only do this when the problem itself is wrong — not when the first solution doesn't work.

### Common Mistakes

1. **Building for "everyone."** "If you are building for a mysterious set of users you have no idea who they are, question that slightly."
2. **Gathering feedback too late.** Waiting until "the full thing" is built wastes months. Early feedback on incomplete versions is valuable.
3. **Premature perfection.** Many founder journeys "end before a single user has actually interacted with a product they've created."
4. **Overestimating launch.** Most people don't remember when Google, Facebook, or Twitter launched. "Launches aren't that special at all."

### Real Examples of MVPs

| Company | MVP | What it lacked |
|---------|-----|---------------|
| Airbnb | Landing page with listings | No payments, no map, part-time developer |
| Twitch (Justin.tv) | One person's livestream | One channel, low resolution, no gaming |
| Stripe (/dev/payments) | Basic payment processing | No bank partnerships, founders installed it manually for each user |

All are now billion-dollar companies. The MVP didn't need to be impressive — it needed to deliver value.

---

## Paul Graham on MVPs and Prototyping

### From "Do Things That Don't Scale"

- **Do it manually first.** Understand the workflow by hand before automating. Stripe manually enrolled merchants. Viaweb built stores for merchants as a consulting service.
- **Start narrow.** Facebook was Harvard-only. Concentrated adoption in a small group beats diluted reach across many.
- **Delight early users.** "I have never once seen a startup lured down a blind alley by trying too hard to make their initial users happy."
- **Skip the big launch.** What matters is whether users are happy months later, not launch-day press.

### From "How to Get Startup Ideas"

- **The well, not the broad shallow hole.** Serve a small group intensely. A small number of people who desperately need you > a large number who kinda want you.
- **Beware sitcom ideas.** Ideas that sound plausible but nobody actually wants. Test: can you name a specific person who would use this daily?
- **Turn off the schlep filter.** Don't dismiss ideas because they involve tedious work. That's often exactly where the opportunity is.

---

## Lean PRD Best Practices

### One Page is the Goal

If the PRD is longer than one page, it's scoping too much. A prototype PRD should be readable in 2 minutes and buildable in a day.

### Priority Levels (If You Need Them)

| Priority | Meaning |
|----------|---------|
| **P0** | Required for MVP to function at all |
| **P1** | High-value additions for a "minimum delightful" product |
| **P2** | Nice-to-have. Cut these first. |

For a prototype, you should only have P0s. If you have P1s and P2s, you're scoping a product, not a prototype.

### What a Good PRD Contains

- The problem and who has it (grounded in real behaviour)
- The specific user and how they trigger the product
- What the product does (capabilities, not features)
- What it does NOT do (explicit scope boundaries)
- How you'll know it works (testable success criteria)

### What a Good PRD Does NOT Contain

- Implementation details (that's the builder's job)
- Product roadmap or future vision
- Competitive analysis or market sizing
- Design specs or wireframes (for a prototype PRD)
- Revision history or meeting notes

---

## Applying to AI Products Specifically

### Scope for AI Prototypes

Most AI prototypes fall into one of these patterns:

| Pattern | Example | Typical scope |
|---------|---------|--------------|
| **Single transform** | "Take this input, produce that output" | One API call with a good prompt |
| **Research + synthesise** | "Find information, then summarise it" | API call with web search tool |
| **Multi-step workflow** | "Do A, then B, then C based on A's output" | Tool use with fixed logic |
| **Decision-making agent** | "Figure out what to do, then do it" | Agentic loop with tools |

Start with the simplest pattern that delivers value. You can always add complexity later.

### Common AI Prototype Mistakes

- **Scoping an agent when a single API call would work.** If the workflow is fixed and predictable, you don't need an agent.
- **"AI-powered everything."** Pick the ONE thing AI does. The rest can be regular code.
- **No success criteria.** "It should give good answers" is not testable. "Given X input, it should produce Y output with Z characteristics" is.
- **Full automation when human-in-the-loop is safer.** For v1, let the human review AI output before it takes action. Build trust before building autonomy.

### The Right Question for Scoping

Ask: "What is the ONE thing this needs to do to be useful?" If the founder can't answer that, the idea isn't ready for a PRD — go back to `/brainstorm`.
