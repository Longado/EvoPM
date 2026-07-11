from evopm.model import TaskProfile
from evopm.triage import recommend


def test_predictable_task_uses_deterministic_workflow():
    result = recommend(TaskProfile(task="Format a weekly report"))
    assert result.base_pattern == "deterministic_workflow"


def test_dynamic_tools_use_single_agent():
    result = recommend(TaskProfile(task="Open research", dynamic_tool_choice=True))
    assert result.base_pattern == "single_agent_with_tools"


def test_unpredictable_path_uses_single_agent():
    result = recommend(TaskProfile(task="Investigate an incident", predictable_path=False))
    assert result.base_pattern == "single_agent_with_tools"


def test_runtime_discovery_uses_bounded_manager_workers():
    result = recommend(TaskProfile(task="Unknown research decomposition", runtime_discovery=True))
    assert result.base_pattern == "bounded_manager_workers"


def test_known_independent_tasks_add_parallel_without_manager():
    result = recommend(TaskProfile(task="Three known sections", known_independent_tasks=3))
    assert "parallel_fan_out_fan_in" in result.additions
    assert result.base_pattern == "deterministic_workflow"


def test_cross_cutting_requirements_are_composable():
    result = recommend(
        TaskProfile(
            task="Reviewed publication",
            stable_categories=True,
            hard_validation_rules=True,
            iterative_quality_gain=True,
            long_wait_or_approval=True,
            standardized_tool_access=True,
            independent_remote_agents=True,
        )
    )
    assert result.additions == (
        "router",
        "deterministic_validator",
        "evaluator_optimizer",
        "persistence_or_durable_runtime",
        "mcp_boundary",
        "a2a_boundary",
    )


def test_failure_recovery_alone_adds_persistence():
    result = recommend(TaskProfile(task="Resume after failure", failure_recovery_required=True))
    assert "persistence_or_durable_runtime" in result.additions


def test_result_explains_what_is_not_needed():
    result = recommend(TaskProfile(task="Format a weekly report"))
    assert "bounded_manager_workers" in result.not_needed
    assert "a2a_boundary" in result.not_needed
    assert result.upgrade_trigger.startswith("Upgrade to a single agent")
