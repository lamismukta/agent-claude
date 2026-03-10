#!/usr/bin/env python3
"""
Loop — PRD Alignment Evaluator

Checks whether a PRD is grounded in user feedback.
Surfaces gaps (feedback that didn't make it in) and unsupported requirements
(things in the PRD nobody asked for).

Usage:
    uv run align.py
    uv run align.py --feedback path/to/notes.md --prd path/to/prd.md
"""

import json
import argparse
from pathlib import Path

import anthropic

client = anthropic.Anthropic()
MODEL = "claude-sonnet-4-6"


EXTRACT_PROMPT = """You are a product analyst. Read these user call notes and extract every distinct user need, pain point, or request.

Call notes:
{call_notes}

Extract each distinct piece of feedback as a structured item. Capture the underlying need (not just the surface request), the closest supporting quote, and how many users mentioned it if that's clear from the notes.

Respond in JSON only:
{{
  "feedback_items": [
    {{
      "id": "F1",
      "need": "<the underlying need in one plain sentence>",
      "quote": "<closest verbatim quote or paraphrase from the notes>",
      "mentioned_by": "<number of users who raised this, or 'unclear'>"
    }}
  ]
}}"""


EVALUATE_PROMPT = """You are a product analyst checking whether a PRD is grounded in user research.

User feedback items extracted from call notes:
{feedback_items}

PRD to evaluate:
{prd}

For each feedback item, check whether the PRD addresses it. Then check for PRD requirements that have no grounding in any of the feedback items.

Respond in JSON only:
{{
  "coverage": [
    {{
      "id": "F1",
      "need": "<the need>",
      "addressed": true or false,
      "prd_section": "<which PRD section addresses it, or null if not addressed>",
      "note": "<any nuance — partially addressed, addressed differently than asked, etc.>"
    }}
  ],
  "gaps": [
    "<specific gap stated as: 'Users mentioned X (N users) but the PRD does not address it'>"
  ],
  "unsupported_requirements": [
    "<PRD requirement or section that has no grounding in any user feedback>"
  ],
  "score": <integer 1-10>,
  "summary": "<2-3 sentences: overall alignment quality, most important gap, recommendation>"
}}"""


def read_file(path: str) -> str:
    return Path(path).read_text()


def extract_feedback(call_notes: str) -> list[dict]:
    response = client.messages.create(
        model=MODEL,
        max_tokens=2048,
        messages=[{"role": "user", "content": EXTRACT_PROMPT.format(call_notes=call_notes)}],
    )
    text = response.content[0].text
    data = json.loads(text[text.find("{") : text.rfind("}") + 1])
    return data["feedback_items"]


def evaluate_alignment(feedback_items: list[dict], prd: str) -> dict:
    response = client.messages.create(
        model=MODEL,
        max_tokens=3000,
        messages=[
            {
                "role": "user",
                "content": EVALUATE_PROMPT.format(
                    feedback_items=json.dumps(feedback_items, indent=2),
                    prd=prd,
                ),
            }
        ],
    )
    text = response.content[0].text
    return json.loads(text[text.find("{") : text.rfind("}") + 1])


def format_report(feedback_items: list[dict], evaluation: dict) -> str:
    score = evaluation["score"]
    score_bar = "█" * score + "░" * (10 - score)

    lines = [
        "# PRD Alignment Report\n",
        f"**Score: {score}/10** [{score_bar}]\n",
        f"{evaluation['summary']}\n",
        "---\n",
        "## Feedback Coverage\n",
    ]

    for item in evaluation["coverage"]:
        icon = "✅" if item["addressed"] else "❌"
        lines.append(f"{icon} **{item['id']}** — {item['need']}")
        if item.get("note"):
            lines.append(f"   *{item['note']}*")
    lines.append("")

    if evaluation["gaps"]:
        lines.append("## Gaps — User Needs Not in the PRD\n")
        for gap in evaluation["gaps"]:
            lines.append(f"- {gap}")
        lines.append("")

    if evaluation["unsupported_requirements"]:
        lines.append("## Unsupported Requirements — No User Evidence\n")
        for req in evaluation["unsupported_requirements"]:
            lines.append(f"- {req}")
        lines.append("")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Check PRD alignment with user feedback")
    parser.add_argument(
        "--feedback",
        default="sample_data/call_notes.md",
        help="Path to call notes or user feedback (markdown)",
    )
    parser.add_argument(
        "--prd",
        default="sample_data/prd.md",
        help="Path to product requirements doc (markdown)",
    )
    args = parser.parse_args()

    print("Reading files...")
    call_notes = read_file(args.feedback)
    prd = read_file(args.prd)

    print("Extracting feedback items from call notes...")
    feedback_items = extract_feedback(call_notes)
    print(f"Found {len(feedback_items)} feedback items\n")

    print("Evaluating PRD alignment...\n")
    evaluation = evaluate_alignment(feedback_items, prd)

    report = format_report(feedback_items, evaluation)
    print(report)

    output_path = Path("alignment_report.md")
    output_path.write_text(report)
    print(f"Saved to {output_path}")


if __name__ == "__main__":
    main()
