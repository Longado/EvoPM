"""Output renderers for EvoPM recommendations."""

import json

from .model import Recommendation


def render_json(recommendation: Recommendation) -> str:
    """Render a stable JSON document."""

    return json.dumps(recommendation.as_dict(), indent=2, ensure_ascii=False) + "\n"


def render_markdown(recommendation: Recommendation) -> str:
    """Render a compact, reviewable decision card."""

    additions = (
        "\n".join(f"- `{item}`" for item in recommendation.additions)
        if recommendation.additions
        else "- None"
    )
    rationale = "\n".join(f"- {item}" for item in recommendation.rationale)
    not_needed = "\n".join(f"- `{item}`" for item in recommendation.not_needed)
    return (
        "# EvoPM orchestration recommendation\n\n"
        f"**Task:** {recommendation.task}\n\n"
        f"**Base pattern:** `{recommendation.base_pattern}`\n\n"
        "## Additions\n\n"
        f"{additions}\n\n"
        "## Why\n\n"
        f"{rationale}\n\n"
        "## Not needed now\n\n"
        f"{not_needed}\n\n"
        "## Upgrade trigger\n\n"
        f"{recommendation.upgrade_trigger}\n"
    )
