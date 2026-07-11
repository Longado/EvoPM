# Orchestration triage

The triage model does not rank architectures from basic to advanced. It selects a base control pattern, then adds independent mechanisms only when task constraints require them.

## Base control pattern

| Constraint | Recommendation |
| --- | --- |
| The path is predictable and can be encoded | `deterministic_workflow` |
| The path is not predictable or tools must be selected dynamically | `single_agent_with_tools` |
| Subtasks must be discovered and delegated at runtime | `bounded_manager_workers` |

## Additive mechanisms

| Constraint | Addition |
| --- | --- |
| Stable categories need different downstream strategies | `router` |
| Two or more known tasks are independent | `parallel_fan_out_fan_in` |
| Hard rules can be checked directly | `deterministic_validator` |
| Evaluation feedback produces measurable iteration gains | `evaluator_optimizer` |
| The task waits, pauses for approval, or must recover | `persistence_or_durable_runtime` |
| Tools and data need a standard capability boundary | `mcp_boundary` |
| Independent remote agents must interoperate | `a2a_boundary` |

## Input schema

| Field | Type | Default | Meaning |
| --- | --- | --- | --- |
| `task` | string | required | Human-readable task name |
| `predictable_path` | boolean | `true` | Steps can be predefined |
| `dynamic_tool_choice` | boolean | `false` | A model must select tools at runtime |
| `stable_categories` | boolean | `false` | Inputs fall into reliably distinct strategies |
| `known_independent_tasks` | integer >= 0 | `0` | Predefined tasks that can run concurrently |
| `runtime_discovery` | boolean | `false` | Subtasks cannot be known before execution |
| `hard_validation_rules` | boolean | `false` | Objective checks exist |
| `iterative_quality_gain` | boolean | `false` | Feedback can measurably improve the result |
| `long_wait_or_approval` | boolean | `false` | Execution pauses across time or human approval |
| `failure_recovery_required` | boolean | `false` | Restarting from zero is unacceptable |
| `standardized_tool_access` | boolean | `false` | Tools need a common access boundary |
| `independent_remote_agents` | boolean | `false` | Separately deployed agents must collaborate |

Unknown fields, ambiguous booleans, blank task names, and negative counts are rejected. The CLI does not infer missing constraints from natural language; this keeps its recommendations inspectable and testable.

## Core rule

> Minimize autonomy, but apply validation, permissions, and reliability requirements from day one. Add the smallest mechanism that solves an observed failure.

## Limits

The CLI does not:

- prove that an agent will improve business outcomes;
- choose a vendor or framework;
- execute a recommended topology;
- inspect confidential project data;
- learn from previous runs;
- replace a benchmark against the current workflow.

