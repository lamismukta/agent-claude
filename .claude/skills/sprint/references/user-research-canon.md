# User Research & Prototyping Canon

Reference material for the `/brainstorm` skill. This distills the startup canon on asking the right questions and building the right thing. Read this to inform your discovery conversation — don't quote it verbatim to the founder.

---

## The Mom Test (Rob Fitzpatrick)

The core insight: people will lie to you to be polite. Your job is to ask questions they can't lie about.

### Three Rules

1. **Talk about their life, not your idea.** The moment you pitch, you've lost — they'll tell you what you want to hear.
2. **Ask for specifics in the past, not generics about the future.** "Would you use X?" is worthless. "When did you last have this problem?" is gold.
3. **Talk less, listen more.** If you're talking more than 30% of the time, you're doing it wrong.

### Three Types of Bad Data

1. **Compliments.** "That sounds amazing!" — means nothing. Deflect and ask about their life instead.
2. **Hypothetical fluff.** "I would definitely use that." — future-tense promises are worthless. Ask what they do *now*.
3. **Wishlists.** "It would be cool if it could also do X." — features disguised as validation. Dig into the underlying need.

### Fluff Detectors

When you hear generic claims ("I always...", "I usually...", "I never..."), hypothetical maybes ("I might...", "I could..."), or future-tense promises ("I would...", "I will...") — redirect:

- "When did that last happen? Walk me through it."
- "How did you solve it last time? What else did you try?"
- "Why do you want that? What would it let you do?"
- "How are you managing without it?"

### The Killer Question

Before every conversation, identify the question that could destroy your idea. If you're not asking questions that could prove you wrong, you're just seeking validation.

### Applied to AI Product Interviews

- Don't ask "Would you use an AI that does X?" — ask "How do you do X today? Walk me through the last time."
- Don't accept "AI could help with that" — ask "What specifically took the longest? What was the most annoying part?"
- When they describe a workflow, listen for the manual, repetitive, error-prone steps. That's where AI adds value.

---

## Eric Migicovsky's 5 Questions (YC "How to Talk to Users")

These five questions work at every stage. They're ordered — start with #1 and follow the thread.

1. **"What's the hardest part about [doing this thing]?"**
   Opens the conversation around pain, not solutions. Let them define the problem space.

2. **"Tell me about the last time you encountered that problem."**
   Forces specifics. Past tense. Real events, not hypotheticals. This is where you learn what actually happens.

3. **"Why was that hard?"**
   Digs into root cause. The first answer is usually surface-level. Keep asking why.

4. **"What, if anything, have you done to try to solve this?"**
   If they haven't tried to solve it, the problem might not be painful enough. If they have, their existing solutions tell you what to beat.

5. **"What don't you love about the solutions you've tried?"**
   Reveals the gap between what exists and what they need. This is your opportunity space.

### Supplementary Questions

- **Frequency:** "How often does this come up?" (hourly problems > yearly problems)
- **Cost:** "How much time/money does this waste?"
- **Budget:** "What would you pay to make this go away?"

### Three Interview Stages

| Stage | Goal | Who to talk to |
|-------|------|---------------|
| **Idea** | Validate the problem exists | People who might have this problem |
| **Prototype** | Find your first customers | People actively trying to solve this problem |
| **Post-launch** | Iterate to product-market fit | Your actual users |

### Applied to AI Product Interviews

- "What's the hardest part about [their workflow]?" surfaces where AI could help — without leading them.
- "Tell me about the last time..." reveals the actual data, tools, and steps involved — which tells you what tools the AI needs.
- "What have you tried?" might reveal they're already using ChatGPT/Claude manually — meaning automation has clear value.

---

## Paul Graham: Key Essays

### "How to Get Startup Ideas"

**Core framework:** Don't think up ideas. Notice them.

- **Live in the future, build what's missing.** The best ideas come from personally experiencing a gap. Microsoft, Dropbox, Airbnb — none were "thought up." They were noticed.
- **The well, not the broad shallow hole.** Serve a small group intensely rather than many people weakly. Facebook started with Harvard. Stripe started with developers.
- **Turn off your filters.** Two mental blocks kill ideas:
  - **The schlep filter:** Dismissing ideas because they involve tedious work (Stripe won because others avoided payments)
  - **The unsexy filter:** Dismissing ideas because they're boring (enterprise software, plumbing, logistics)
- **Beware "sitcom ideas."** Ideas that sound plausible to a TV audience but nobody actually wants. "A social network for pet owners" — sounds reasonable, no one cares.

### "Do Things That Don't Scale"

**Core insight:** Startups take off because founders make them take off.

- **Recruit users manually.** Don't wait for organic growth. The Collison brothers would say "give me your laptop" and install Stripe on the spot ("Collison installation").
- **Delight early users obsessively.** Wufoo sent handwritten thank-you notes. "I have never once seen a startup lured down a blind alley by trying too hard to make their initial users happy."
- **Start narrow.** Facebook was Harvard-only. Concentrated adoption beats diluted reach.
- **Do it manually first, automate later.** Understand the workflow by hand before building software for it. Stripe manually enrolled merchants behind the scenes.
- **Consulting is learning.** Acting as a consultant for early B2B customers teaches you what to build. It feels "lame" but it's strategically optimal.
- **Skip the big launch.** It doesn't matter. What matters is whether users are still happy months later.

### Applied to AI Product Interviews

- Push founders to narrow their user. "Who is the ONE person who needs this most?" not "who might use it?"
- Ask about manual workarounds — that's where the AI replaces human effort.
- If they can't describe a specific person with a specific problem, the idea is probably a "sitcom idea."

---

## YC MVP Principles (Michael Seibel)

- **An MVP is "ridiculously simple."** It's the first thing you can give to the first set of users to see if you deliver any value at all.
- **Launch in weeks, not months.** If it takes more than a few weeks, you're building too much.
- **Core functionality only.** Airbnb's MVP had no payments and no map. It was a landing page.
- **The goal is learning, not impressing.** An MVP collects "the maximum amount of validated learning with the least effort."
- **Talk to users within 90 days.** If you haven't talked to real users in 90 days, you're building in the dark.

### Applied to AI Product Interviews

- The PRD should scope a prototype that can be built in a day, not a product that takes months.
- Push founders to cut scope aggressively. "What's the ONE thing this needs to do to be useful?"
- The prototype should test the riskiest assumption, not demonstrate all features.

---

## YC AI Startup School 2025 Insights

- **Don't clone ChatGPT** (Sam Altman). Build what's uniquely yours.
- **Product overhang exists.** Current model capabilities vastly exceed what most apps use — there's untapped potential.
- **Start with one narrow hypothesis** (Andrew Ng). Define tight scope, move through validation cycles quickly.
- **Partial autonomy over full automation** (Andrej Karpathy). Let users control how much they delegate. Build fast generation-verification loops with human oversight.
- **Focus where AI is transformative, not marginal** (Aaron Levie). Don't use AI to make something 10% better — use it where it creates entirely new capabilities.

### Applied to AI Product Interviews

- Ask "What can you do with AI that was literally impossible before?" — not just "What can AI speed up?"
- Push founders toward agent architectures when the task is open-ended, but simple API calls when it's structured.
- Human-in-the-loop is usually the right default for v1. Ask about trust and error tolerance.

---

## Summary: What Makes a Good Interview Question

| Good question | Why it works |
|--------------|-------------|
| "What's the hardest part about X?" | Opens with pain, not solutions |
| "Walk me through the last time..." | Forces past-tense specifics |
| "How do you solve this today?" | Reveals existing behaviour and workarounds |
| "What have you tried?" | Tests if the pain is real (did they bother?) |
| "What don't you love about that?" | Reveals the gap to fill |
| "Who is the ONE person who needs this most?" | Forces narrow focus |
| "What would make you stop using this after the first try?" | Surfaces deal-breakers early |

| Bad question | Why it fails |
|-------------|-------------|
| "Would you use this?" | Hypothetical, invites polite lies |
| "Do you think this is a good idea?" | Fishing for validation |
| "How much would you pay?" (asked too early) | Hypothetical without context |
| "Don't you think AI could help with...?" | Leading question |
| "What features would you want?" | Invites wishlists, not needs |
