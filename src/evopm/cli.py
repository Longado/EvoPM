"""Command-line interface for EvoPM."""

import argparse
import json
import sys
from pathlib import Path
from typing import Sequence

from .model import TaskProfile
from .render import render_json, render_markdown
from .triage import recommend


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="evopm",
        description="Recommend the least-complex orchestration pattern for a task.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)
    triage = subparsers.add_parser("triage", help="Evaluate a JSON task profile")
    triage.add_argument("path", help="JSON file path, or - to read stdin")
    triage.add_argument("--format", choices=("markdown", "json"), default="markdown")
    return parser


def _load_profile(path: str) -> TaskProfile:
    raw = sys.stdin.read() if path == "-" else Path(path).read_text(encoding="utf-8")
    try:
        data = json.loads(raw)
    except json.JSONDecodeError as error:
        raise ValueError(f"invalid JSON: {error.msg} at line {error.lineno} column {error.colno}") from error
    if not isinstance(data, dict):
        raise ValueError("task profile must be a JSON object")
    return TaskProfile.from_dict(data)


def main(argv: Sequence[str] | None = None) -> int:
    """Run the CLI and return a process status."""

    args = _parser().parse_args(argv)
    try:
        profile = _load_profile(args.path)
        result = recommend(profile)
    except (OSError, ValueError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 2

    output = render_json(result) if args.format == "json" else render_markdown(result)
    sys.stdout.write(output)
    return 0
