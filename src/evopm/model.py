"""Validated data types for orchestration triage."""

from dataclasses import dataclass, fields
from typing import Any, Mapping


@dataclass(frozen=True)
class TaskProfile:
    """Explicit task constraints used by the deterministic decision engine."""

    task: str
    predictable_path: bool = True
    dynamic_tool_choice: bool = False
    stable_categories: bool = False
    known_independent_tasks: int = 0
    runtime_discovery: bool = False
    hard_validation_rules: bool = False
    iterative_quality_gain: bool = False
    long_wait_or_approval: bool = False
    failure_recovery_required: bool = False
    standardized_tool_access: bool = False
    independent_remote_agents: bool = False

    @classmethod
    def from_dict(cls, data: Mapping[str, Any]) -> "TaskProfile":
        """Build a profile from a mapping and reject ambiguous input."""

        allowed = {field.name for field in fields(cls)}
        unknown = sorted(set(data) - allowed)
        if unknown:
            raise ValueError(f"unknown fields: {', '.join(unknown)}")

        if "task" not in data:
            raise ValueError("task is required")
        task = data["task"]
        if not isinstance(task, str):
            raise ValueError("task must be a string")
        if not task.strip():
            raise ValueError("task must not be empty")

        bool_fields = allowed - {"task", "known_independent_tasks"}
        for name in sorted(bool_fields):
            if name in data and not isinstance(data[name], bool):
                raise ValueError(f"{name} must be a boolean")

        count = data.get("known_independent_tasks", 0)
        if isinstance(count, bool) or not isinstance(count, int) or count < 0:
            raise ValueError("known_independent_tasks must be a non-negative integer")

        normalized = dict(data)
        normalized["task"] = task.strip()
        return cls(**normalized)


@dataclass(frozen=True)
class Recommendation:
    """Explainable output from the deterministic decision engine."""

    task: str
    base_pattern: str
    additions: tuple[str, ...]
    rationale: tuple[str, ...]
    not_needed: tuple[str, ...]
    upgrade_trigger: str

    def as_dict(self) -> dict[str, object]:
        """Return a JSON-serializable representation."""

        return {
            "task": self.task,
            "base_pattern": self.base_pattern,
            "additions": list(self.additions),
            "rationale": list(self.rationale),
            "not_needed": list(self.not_needed),
            "upgrade_trigger": self.upgrade_trigger,
        }
