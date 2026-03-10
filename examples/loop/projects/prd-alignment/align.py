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
MODEL = "claude-sonnet-4-6"  # upgrade to claude-opus-4-6 if evaluation accuracy is insufficient

EXTRACT_SCHEMA = {
    "name": "feedback_extraction",
    "type": "object",
    "properties": {
        "feedback_items": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {"type": "string"},
                    "need": {"type": "string", "description": "The underlying need in one plain sentence"},
                    "quote": {"type": "string", "description": "Closest verbatim quote or paraphrase"},
                    "mentioned_by": {"type": "string", "description": "Number of users who raised this, or 'unclear'"},
                },
                "required": ["id", "need", "quote", "mentioned_by"],
            },
        }
    },
    "required": ["feedback_items"],
}

EVALUATE_SCHEMA = {
    "name": "alignment_evaluation",
    "type": "object",
    "properties": {
        "coverage": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {"type": "string"},
                    "need": {"type": "string"},
                    "addressed": {"type": "boolean"},
                    "prd_section": {"type": ["string", "null"]},
                    "note": {"type": "string", "description": "Nuance — partially addressed, addressed differently, etc."},
                },
                "required": ["id", "need", "addressed", "prd_section", "note"],
            },
        },
        "gaps": {
            "type": "array",
            "items": {"type": "string"},
            "description": "User needs not addressed in the PRD, stated as 'Users mentioned X (N users) but the PRD does not address it'",
        },
        "unsupported_requirements": {
            "type": "array",
            "items": {"type": "string"},
            "description": "PRD requirements with no grounding in user feedback",
        },
        "score": {"type": "integer", "minimum": 1, "maximum": 10},
        "summary": {"type": "string", "description": "2-3 sentences: overall quality, most important gap, recommendation"},
    },
    "required": ["coverage", "gaps", "unsupported_requirements", "score", "summary"],
}

EXTRACT_PROMPT = """You are a product analyst. Read these user call notes and extract every distinct user need, pain point, or request.

Call notes:
{call_notes}

Extract each distinct piece of feedback as a structured item. Capture the underlying need (not just the surface request), the closest supporting quote, and how many users mentioned it if that's clear from the notes."""

EVALUATE_PROMPT = """You are a product analyst checking whether a PRD is grounded in user research.

User feedback items extracted from call notes (including how many users raised each need):
{feedback_items}

PRD to evaluate:
{prd}

For each feedback item, check whether the PRD addresses it. Then check for PRD requirements that have no grounding in any of the feedback items. Weight gaps by how many users mentioned them — a need raised by 3/3 users that's missing is more serious than one raised by 1 user."""


def read_file(path: str) -> str:
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"File not found: {path}")
    return p.read_text()


def extract_feedback(call_notes: str) -> list[dict]:
    response = client.messages.create(
        model=MODEL,
        max_tokens=2048,
        messages=[{"role": "user", "content": EXTRACT_PROMPT.format(call_notes=call_notes)}],
        output_config={"format": {"type": "json_schema", "json_schema": EXTRACT_SCHEMA}},
    )
    return json.loads(response.content[0].text)["feedback_items"]


def evaluate_alignment(feedback_items: list[dict], prd: str) -> dict:
    response = client.messages.create(
        model=MODEL,
        max_tokens=4000,
        thinking={"type": "adaptive"},  # cross-document reasoning benefits from extended thinking
        messages=[
            {
                "role": "user",
                "content": EVALUATE_PROMPT.format(
                    feedback_items=json.dumps(feedback_items, indent=2),
                    prd=prd,
                ),
            }
        ],
        output_config={"format": {"type": "json_schema", "json_schema": EVALUATE_SCHEMA}},
    )
    # structured output is always the last content block
    for block in reversed(response.content):
        if block.type == "text":
            return json.loads(block.text)
    raise ValueError("No text block in response")


def format_report(evaluation: dict) -> str:
    score = evaluation["score"]
    score_bar = "█" * score + "░" * (10 - score)

    lines = [
        "# PRD Alignment Report\n",
        f"**Score: {score}/10** {score_bar}\n",
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

    try:
        print("Reading files...")
        call_notes = read_file(args.feedback)
        prd = read_file(args.prd)
    except FileNotFoundError as e:
        print(f"Error: {e}")
        raise SystemExit(1)

    print("Extracting feedback items from call notes...")
    feedback_items = extract_feedback(call_notes)
    print(f"Found {len(feedback_items)} feedback items\n")

    print("Evaluating PRD alignment...\n")
    evaluation = evaluate_alignment(feedback_items, prd)

    report = format_report(evaluation)
    print(report)

    output_path = Path("alignment_report.md")
    output_path.write_text(report)
    print(f"Saved to {output_path}")


if __name__ == "__main__":
    main()
