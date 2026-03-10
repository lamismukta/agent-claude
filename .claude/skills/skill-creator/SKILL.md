---
name: skill-creator
description: "Create new skills, modify and improve existing skills. Use when a founder says 'turn this into a skill', 'I want a skill that does X', 'help me build a custom skill', 'make this repeatable', or wants to create or edit a SKILL.md file."
---

# /skill-creator — Create and Improve Skills

Help the founder create a new Claude Code skill or improve an existing one. A skill is a SKILL.md file that teaches Claude how to do something on command.

## How It Works

1. **Understand the intent.** Figure out what they want the skill to do. If they say "turn this into a skill", extract the workflow from the conversation — tools used, sequence of steps, corrections made, input/output formats. If they're starting fresh, ask:
   - What should this skill enable Claude to do?
   - When should it trigger? (what phrases or contexts)
   - What does a good output look like?

2. **Write the SKILL.md.** See structure below.

3. **Test it.** Come up with 2-3 realistic test prompts and run them. Share the results with the founder before revising.

4. **Iterate.** Improve based on feedback. Repeat until the skill does what they want.

5. **Optionally optimise the description** for better triggering — see the section below.

---

## Anatomy of a Skill

```
.claude/skills/skill-name/
├── SKILL.md          ← required: frontmatter + instructions
└── references/       ← optional: docs or frameworks loaded as needed
```

**SKILL.md structure:**

```markdown
---
name: skill-name
description: "When to trigger and what it does. Be specific about trigger phrases."
---

# Skill Name

[Instructions for Claude when this skill is active]
```

**Three-level loading:**
1. **Frontmatter** (name + description) — always in context
2. **SKILL.md body** — in context when skill triggers. Keep under 500 lines.
3. **References** — loaded on demand. Put large docs, frameworks, or reference material here.

If SKILL.md is getting long, move detailed content into `references/` files and point to them from the main file.

---

## Writing Good Skills

**Description is the trigger.** Claude decides whether to use a skill based on its description. Include both what the skill does and specific phrases that should activate it. Err on the side of being explicit — Claude tends to under-trigger skills.

**Explain the why.** Skills work better when Claude understands the reasoning, not just the rules. Instead of "ALWAYS use this format", explain why the format matters. Today's models respond well to intent.

**Prefer imperative instructions.** "Read HYPOTHESES.md before writing the spec" is clearer than "HYPOTHESES.md should be read".

**Keep it lean.** Remove anything that isn't earning its place. If a section doesn't change the output, cut it.

**Use examples sparingly.** One concrete example is worth ten abstract rules. Include examples for the non-obvious parts, not everything.

---

## Testing

After writing the skill draft, create 2-3 realistic test prompts — the kind of thing a real user would actually type. Run them and share the results with the founder.

Good test prompts are specific and concrete. Bad: "test the skill". Good: "I just got off a call with my first potential customer at a Series A fintech. They said the manual reconciliation process takes their team 3 hours every Friday. Draft outreach to two similar fintechs."

For each test, note:
- Did the skill produce the right output?
- Did it trigger correctly?
- What would a founder think if they saw this?

Revise and retest until the output is consistently good.

---

## Description Optimisation

The description field determines when Claude uses the skill. After the skill is working well, offer to optimise it.

To test triggering manually: think of 5-10 prompts that should trigger the skill and 5-10 that shouldn't. The tricky cases are near-misses — prompts that share keywords but need something different. Run through them and check whether Claude would pick up the skill. Revise the description based on what's missing or misfiring.

**What makes a good description:**
- Includes specific trigger phrases ("when a founder says 'I want to build X'...")
- Covers the main use cases without being so broad it triggers on unrelated things
- Mentions the output so Claude knows what the skill produces

---

## Installing the Skill

Skills in `.claude/skills/` are auto-discovered by Claude Code when you open a session in that directory. No additional installation needed — write the SKILL.md and it's available immediately.

To share a skill, copy the skill directory (e.g., `.claude/skills/my-skill/`) to another repo's `.claude/skills/`.
