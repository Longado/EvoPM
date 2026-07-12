# EvoPM

> **Status: design-stage / alpha.** EvoPM is a decision framework with a small deterministic CLI. It is **not** an agent runtime, autonomous PM, or production governance platform.

EvoPM helps AI and software projects make fewer expensive decisions by defaulting to the least-complex approach that fits the task.

It focuses on three recurring failure modes:

1. scope expands without an explicit trade-off;
2. development continues without real user evidence;
3. discussions repeat without a recorded decision.

The first runnable component is `evopm triage`: a deterministic rule engine that maps explicit task constraints to an explainable orchestration recommendation.

## Product overview

[![Watch the 36-second EvoPM product overview](docs/demo/evopm-product-demo-poster.png)](docs/demo/evopm-product-demo.mp4)

In 36 seconds: why architecture should follow task constraints, how EvoPM selects the smallest justified pattern, and when complexity is allowed to increase.

## See it decide

![EvoPM choosing an orchestration pattern](docs/demo/evopm-triage.gif)

The example starts with a quarterly-report task, recommends the simplest justified control pattern, and makes the unnecessary complexity explicit. Reproduce it with the [quick start](#quick-start) below.

## Quick start

EvoPM requires Python 3.11 or newer. Check your interpreter before creating the
environment:

```bash
python3 -c 'import sys; assert sys.version_info >= (3, 11), "EvoPM requires Python 3.11+"'
```

If that check fails, replace `python3` below with an installed Python 3.11+
command, such as `python3.11`.

```bash
git clone https://github.com/Longado/EvoPM.git
cd EvoPM
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e .
evopm triage examples/quarterly-report.json
```

The same command works without installation:

```bash
PYTHONPATH=src python3 -m evopm triage examples/quarterly-report.json
```

Use JSON output for automation:

```bash
evopm triage examples/quarterly-report.json --format json
```

## What the CLI decides

It chooses one base control pattern:

- `deterministic_workflow`
- `single_agent_with_tools`
- `bounded_manager_workers`

It can then add only the mechanisms required by explicit constraints:

- router;
- fixed parallel fan-out/fan-in;
- deterministic validator;
- evaluator-optimizer;
- persistence or durable runtime;
- MCP tool boundary;
- A2A independent-agent boundary.

These mechanisms are composable. They are not a maturity ladder. A fixed approval workflow may need persistence on day one, while a short multi-agent research task may not need it at all.

## Input

`evopm triage` reads a JSON object. The `task` field is required; all other fields have conservative defaults.

```json
{
  "task": "Prepare a reviewed quarterly report",
  "predictable_path": false,
  "dynamic_tool_choice": true,
  "stable_categories": true,
  "known_independent_tasks": 3,
  "hard_validation_rules": true,
  "iterative_quality_gain": true,
  "long_wait_or_approval": true
}
```

See [orchestration triage](docs/orchestration-triage.md) for every field and decision rule.

## Design

The broader EvoPM design has three independent parts:

- **PM Core:** problem definition, scope, priority, user evidence, stage gates, and retrospectives;
- **Project Adapters:** domain-specific judgment, starting with software and agent development;
- **Governed Learning:** observations become cross-project rules only after two independent validations or explicit owner confirmation.

Only the deterministic orchestration triage CLI is implemented in this release. See [core design](docs/core-design.md) for the intended boundary.

## Development

```bash
python -m pip install pytest ruff build
python -m pytest -q
python -m ruff check .
python -m build
```

## Principles

- Minimize autonomy; add only the mechanism that solves an observed failure.
- Prefer deterministic validation for hard rules.
- Keep recommendations short, explainable, rejectable, and reversible.
- Do not promote one-off experience into permanent policy.
- Measure reduced rework and decision time, not document volume.

## License

MIT
