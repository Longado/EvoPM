import pytest

from evopm.model import TaskProfile


def test_profile_requires_task():
    with pytest.raises(ValueError, match="task is required"):
        TaskProfile.from_dict({})


def test_profile_requires_non_empty_task():
    with pytest.raises(ValueError, match="task must not be empty"):
        TaskProfile.from_dict({"task": "   "})


def test_profile_rejects_negative_independent_task_count():
    with pytest.raises(ValueError, match="known_independent_tasks"):
        TaskProfile.from_dict({"task": "Research", "known_independent_tasks": -1})


def test_profile_rejects_non_boolean_flags():
    with pytest.raises(ValueError, match="predictable_path must be a boolean"):
        TaskProfile.from_dict({"task": "Research", "predictable_path": "yes"})


def test_profile_rejects_unknown_fields():
    with pytest.raises(ValueError, match="unknown fields: magic"):
        TaskProfile.from_dict({"task": "Research", "magic": True})
