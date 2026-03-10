#!/usr/bin/env python3
"""
Loop — Signal Synthesizer

Finds what's actually worth building by cross-referencing usage data with
qualitative feedback. Evaluates whether your PRD is focused on real signal.

Three steps:
1. Analyse usage events → patterns and anomalies
2. Extract pain points from call notes
3. Synthesize: where do data and feedback agree? Where do they diverge?
   Then check whether the PRD addresses the strong signals.

Usage:
    uv run synthesize.py
    uv run synthesize.py --events usage_events.json --feedback call_notes.md --prd prd.md
"""

import json
import argparse
from pathlib import Path

import anthropic

client = anthropic.Anthropic()
MODEL = "claude-sonnet-4-6"  # upgrade to claude-opus-4-6 for larger datasets


# --- Schemas ---

ANALYSE_SCHEMA = {
    "name": "event_analysis",
    "type": "object",
    "properties": {
        "patterns": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "name": {"type": "string"},
                    "description": {"type": "string"},
                    "metric": {"type": "string", "description": "The specific number or stat"},
                    "severity": {"type": "string", "enum": ["high", "medium", "low"]},
                },
                "required": ["name", "description", "metric", "severity"],
            },
        }
    },
    "required": ["patterns"],
}

FEEDBACK_SCHEMA = {
    "name": "feedback_extraction",
    "type": "object",
    "properties": {
        "pain_points": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {"type": "string"},
                    "pain": {"type": "string"},
                    "quote": {"type": "string"},
                    "mentioned_by": {"type": "string"},
                },
                "required": ["id", "pain", "quote", "mentioned_by"],
            },
        }
    },
    "required": ["pain_points"],
}

SYNTHESIS_SCHEMA = {
    "name": "signal_synthesis",
    "type": "object",
    "properties": {
        "strong_signals": {
            "type": "array",
            "description": "Where usage data AND feedback agree — these are real problems worth solving",
            "items": {
                "type": "object",
                "properties": {
                    "signal": {"type": "string"},
                    "data_evidence": {"type": "string"},
                    "feedback_evidence": {"type": "string"},
                    "prd_addressed": {"type": "boolean"},
                },
                "required": ["signal", "data_evidence", "feedback_evidence", "prd_addressed"],
            },
        },
        "data_only": {
            "type": "array",
            "description": "Patterns in usage data that nobody mentioned in calls — potential blind spots",
            "items": {
                "type": "object",
                "properties": {
                    "signal": {"type": "string"},
                    "data_evidence": {"type": "string"},
                    "prd_addressed": {"type": "boolean"},
                    "recommendation": {"type": "string"},
                },
                "required": ["signal", "data_evidence", "prd_addressed", "recommendation"],
            },
        },
        "feedback_only": {
            "type": "array",
            "description": "Things users said that aren't reflected in usage data — may be vocal minority",
            "items": {
                "type": "object",
                "properties": {
                    "signal": {"type": "string"},
                    "feedback_evidence": {"type": "string"},
                    "prd_addressed": {"type": "boolean"},
                    "recommendation": {"type": "string"},
                },
                "required": ["signal", "feedback_evidence", "prd_addressed", "recommendation"],
            },
        },
        "prd_no_signal": {
            "type": "array",
            "description": "PRD requirements with no support from either data or feedback",
            "items": {"type": "string"},
        },
        "score": {
            "type": "integer",
            "minimum": 1,
            "maximum": 10,
            "description": "How well the PRD is focused on real signal (1 = mostly noise, 10 = every item is strongly evidenced)",
        },
        "summary": {"type": "string", "description": "3-4 sentences: biggest strength, biggest gap, top recommendation"},
    },
    "required": ["strong_signals", "data_only", "feedback_only", "prd_no_signal", "score", "summary"],
}


# --- Prompts ---

ANALYSE_PROMPT = """You are a product analyst. Analyse these user event metrics and identify the most significant patterns.

Usage data:
{events}

Find patterns that matter for product decisions: drop-off points in key flows, underused features (especially those that seem prominent or intentional), unexpectedly high engagement with specific features, and anything that suggests friction or opportunity.

Be specific about numbers. "63% → 22% drop at step 3" is a pattern. "Low engagement" is not."""

FEEDBACK_PROMPT = """You are a product analyst. Read these user call notes and extract every distinct pain point or request.

Call notes:
{call_notes}

For each item, capture the underlying need (not just the surface request), the closest supporting quote, and how many users mentioned it."""

SYNTHESIS_PROMPT = """You are a product analyst synthesising two sources of evidence to evaluate a PRD.

Usage data patterns:
{patterns}

Qualitative feedback from user calls:
{pain_points}

PRD to evaluate:
{prd}

Classify all signals:
- Strong signals: where usage data AND feedback agree — high confidence, worth building
- Data only: patterns in usage nobody mentioned in calls — could be a blind spot; recommend investigating before building
- Feedback only: things users said with no data support — may be a vocal minority or unmeasured friction; flag but don't treat as confirmed
- PRD with no signal: requirements supported by neither data nor feedback — these are the most dangerous items to have in a roadmap

For each item, note whether the PRD addresses it."""


# --- Pipeline ---

def read_file(path: str) -> str:
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"File not found: {path}")
    return p.read_text()


def analyse_events(events: str) -> list[dict]:
    response = client.messages.create(
        model=MODEL,
        max_tokens=2048,
        messages=[{"role": "user", "content": ANALYSE_PROMPT.format(events=events)}],
        output_config={"format": {"type": "json_schema", "schema": ANALYSE_SCHEMA}},
    )
    return json.loads(response.content[0].text)["patterns"]


def extract_feedback(call_notes: str) -> list[dict]:
    response = client.messages.create(
        model=MODEL,
        max_tokens=2048,
        messages=[{"role": "user", "content": FEEDBACK_PROMPT.format(call_notes=call_notes)}],
        output_config={"format": {"type": "json_schema", "schema": FEEDBACK_SCHEMA}},
    )
    return json.loads(response.content[0].text)["pain_points"]


def synthesize(patterns: list[dict], pain_points: list[dict], prd: str) -> dict:
    response = client.messages.create(
        model=MODEL,
        max_tokens=4000,
        thinking={"type": "adaptive"},  # cross-source reasoning benefits from extended thinking
        messages=[
            {
                "role": "user",
                "content": SYNTHESIS_PROMPT.format(
                    patterns=json.dumps(patterns, indent=2),
                    pain_points=json.dumps(pain_points, indent=2),
                    prd=prd,
                ),
            }
        ],
        output_config={"format": {"type": "json_schema", "schema": SYNTHESIS_SCHEMA}},
    )
    for block in reversed(response.content):
        if block.type == "text":
            return json.loads(block.text)
    raise ValueError("No text block in response")


# --- Formatting ---

def format_report(result: dict) -> str:
    score = result["score"]
    bar = "█" * score + "░" * (10 - score)

    lines = [
        "# Signal Report\n",
        f"**PRD signal score: {score}/10** {bar}\n",
        f"{result['summary']}\n",
        "---\n",
    ]

    if result["strong_signals"]:
        lines.append("## Strong Signals — Data + Feedback Agree\n")
        for s in result["strong_signals"]:
            status = "✅ in PRD" if s["prd_addressed"] else "❌ missing from PRD"
            lines.append(f"**{s['signal']}** [{status}]")
            lines.append(f"  Data: {s['data_evidence']}")
            lines.append(f"  Feedback: {s['feedback_evidence']}")
            lines.append("")

    if result["data_only"]:
        lines.append("## Data Only — Not Mentioned in Calls\n")
        for s in result["data_only"]:
            status = "✅ in PRD" if s["prd_addressed"] else "❌ missing from PRD"
            lines.append(f"**{s['signal']}** [{status}]")
            lines.append(f"  Data: {s['data_evidence']}")
            lines.append(f"  → {s['recommendation']}")
            lines.append("")

    if result["feedback_only"]:
        lines.append("## Feedback Only — Not Reflected in Usage Data\n")
        for s in result["feedback_only"]:
            status = "✅ in PRD" if s["prd_addressed"] else "❌ missing from PRD"
            lines.append(f"**{s['signal']}** [{status}]")
            lines.append(f"  Feedback: {s['feedback_evidence']}")
            lines.append(f"  → {s['recommendation']}")
            lines.append("")

    if result["prd_no_signal"]:
        lines.append("## No Signal — Reconsider These PRD Items\n")
        for item in result["prd_no_signal"]:
            lines.append(f"- {item}")
        lines.append("")

    return "\n".join(lines)


# --- Entry point ---

def main():
    parser = argparse.ArgumentParser(description="Synthesise usage data + feedback to evaluate a PRD")
    parser.add_argument("--events", default="sample_data/usage_events.json", help="Usage event metrics (JSON)")
    parser.add_argument("--feedback", default="sample_data/call_notes.md", help="User call notes (markdown)")
    parser.add_argument("--prd", default="sample_data/prd.md", help="Product requirements doc (markdown)")
    args = parser.parse_args()

    try:
        events = read_file(args.events)
        call_notes = read_file(args.feedback)
        prd = read_file(args.prd)
    except FileNotFoundError as e:
        print(f"Error: {e}")
        raise SystemExit(1)

    print("Analysing usage data...")
    patterns = analyse_events(events)
    print(f"Found {len(patterns)} patterns\n")

    print("Extracting feedback signals...")
    pain_points = extract_feedback(call_notes)
    print(f"Found {len(pain_points)} feedback signals\n")

    print("Synthesising...\n")
    result = synthesize(patterns, pain_points, prd)

    report = format_report(result)
    print(report)

    output = Path("signal_report.md")
    output.write_text(report)
    print(f"Saved to {output}")


if __name__ == "__main__":
    main()
