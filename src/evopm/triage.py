"""Deterministic orchestration recommendation rules."""

from .model import Recommendation, TaskProfile


_ALL_PATTERNS = (
    "deterministic_workflow",
    "single_agent_with_tools",
    "bounded_manager_workers",
    "router",
    "parallel_fan_out_fan_in",
    "deterministic_validator",
    "evaluator_optimizer",
    "persistence_or_durable_runtime",
    "mcp_boundary",
    "a2a_boundary",
)

_RATIONALE = {
    "deterministic_workflow": "The execution path can be predefined, so model autonomy is unnecessary.",
    "single_agent_with_tools": "The task needs model-driven decisions or dynamic tool choice.",
    "bounded_manager_workers": "Subtasks must be discovered and delegated at runtime.",
    "router": "Stable task categories require different downstream strategies.",
    "parallel_fan_out_fan_in": "Known independent tasks can run concurrently and be aggregated.",
    "deterministic_validator": "Hard validation rules should be enforced by deterministic checks.",
    "evaluator_optimizer": "Evaluation feedback is expected to produce measurable iterative gains.",
    "persistence_or_durable_runtime": "Waiting, approval, or recovery requires resumable state.",
    "mcp_boundary": "Tool and data access needs a standardized capability boundary.",
    "a2a_boundary": "Independent remote agents need an explicit interoperability boundary.",
}


def recommend(profile: TaskProfile) -> Recommendation:
    """Recommend the least-autonomous architecture that satisfies explicit constraints."""

    if profile.runtime_discovery:
        base = "bounded_manager_workers"
        upgrade_trigger = (
            "Keep workers bounded; add autonomy only when evaluation evidence shows a specific gap."
        )
    elif profile.dynamic_tool_choice or not profile.predictable_path:
        base = "single_agent_with_tools"
        upgrade_trigger = (
            "Add manager/workers only when subtasks must be discovered at runtime and the "
            "decomposition benefit is measurable."
        )
    else:
        base = "deterministic_workflow"
        upgrade_trigger = (
            "Upgrade to a single agent only when the path cannot be predefined and "
            "model-driven decisions are required."
        )

    additions: list[str] = []
    if profile.stable_categories:
        additions.append("router")
    if profile.known_independent_tasks >= 2:
        additions.append("parallel_fan_out_fan_in")
    if profile.hard_validation_rules:
        additions.append("deterministic_validator")
    if profile.iterative_quality_gain:
        additions.append("evaluator_optimizer")
    if profile.long_wait_or_approval or profile.failure_recovery_required:
        additions.append("persistence_or_durable_runtime")
    if profile.standardized_tool_access:
        additions.append("mcp_boundary")
    if profile.independent_remote_agents:
        additions.append("a2a_boundary")

    selected = {base, *additions}
    return Recommendation(
        task=profile.task,
        base_pattern=base,
        additions=tuple(additions),
        rationale=tuple(_RATIONALE[item] for item in (base, *additions)),
        not_needed=tuple(item for item in _ALL_PATTERNS if item not in selected),
        upgrade_trigger=upgrade_trigger,
    )
