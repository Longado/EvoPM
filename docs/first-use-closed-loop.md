# First-use closed-loop case

> Status: onboarding loop closed on 2026-07-12; core product validation remains open
> Scope: public, reproducible onboarding evidence only

## Decision

The next EvoPM change will improve and verify the five-minute first-use path instead of adding product functionality.

This is the smallest useful self-dogfood case for the three mechanisms EvoPM has studied:

- ADR: record the decision, accepted downside, and revisit trigger;
- evidence binding: keep raw observations separate from the acceptance judgment;
- controlled comparison: compare the current and candidate quick starts under the same user scenario.

## Evidence that triggered the decision

The public README uses `python3` in its quick start, while the package requires Python 3.11 or newer. On the macOS audit machine, the default `python3` is Python 3.9.6. The no-install README path fails during import with that interpreter, while the same command succeeds with Python 3.11.

The repository's 17 tests and Ruff checks pass under the existing Python 3.12 development environment. This means implementation quality is currently verified, but the documented first-use path is not.

## Options considered

1. **Verify first use now — selected.** Fix the observed onboarding boundary without expanding EvoPM.
2. Build a baseline-versus-candidate architecture case. This tests the core proposition more directly but requires a larger task, shared scorers, and real workflow evidence.
3. Add CI and reconcile local branch history first. This improves maintenance but does not prove user value.

## Candidate change

The implementation is limited to:

1. state the Python 3.11+ prerequisite before the quick-start commands;
2. add a version preflight that prevents users from silently continuing with an unsupported interpreter;
3. keep both installed and no-install paths short;
4. append raw baseline and candidate observations, the evaluation result, and the revisit decision to this document.

No CLI behavior, task schema, runtime, database, automatic learning, or new architectural rule will be added.

## Comparison contract

### Frozen case

A first-time macOS user has checked out the public repository and follows the README without prior EvoPM knowledge. External network download time is recorded separately because EvoPM cannot control it.

### Baseline

Follow the current public README using the default `python3` available on the audit machine.

### Candidate

Follow the revised README on the same machine, including its interpreter preflight, then use an available Python 3.11+ interpreter.

### Raw evidence

Record without interpretation:

- interpreter and version;
- commands executed;
- exit status;
- elapsed time after checkout;
- first recommendation output;
- test and lint output.

### Evaluation rules

The candidate passes only when:

1. the Python 3.11+ requirement is visible before environment creation;
2. an unsupported default interpreter is detected before installation or CLI execution;
3. the installed path and the no-install path both return exit status 0 with Python 3.11+;
4. a first recommendation is produced within five minutes after checkout, excluding external clone latency;
5. the full existing test suite and Ruff checks still pass;
6. public-content review finds no local paths, private names, credentials, internal records, or unsupported claims.

## Accepted downside

This case validates onboarding, not whether EvoPM recommendations reduce project rework. Core product validation remains open and must use a real baseline-versus-candidate project case later.

## Observed evidence

The comparison used one macOS machine after checkout. Clone latency was excluded.
The default `python3` was Python 3.9.6; the supported comparison interpreter
was Python 3.11.15.

### Baseline observations

| Path | Command boundary | Exit | Elapsed | Observed result |
| --- | --- | ---: | ---: | --- |
| No install | `PYTHONPATH=src python3 -m evopm triage examples/quarterly-report.json` | 1 | 0.253 s | Import stopped with `TypeError: unsupported operand type(s) for \|` before the CLI could explain the version requirement. |
| Editable install | `python3 -m venv .venv`, then `python -m pip install -e .` | 1 | 7.255 s | The Python 3.9 environment used pip 21.2.4, which rejected the editable install from the `pyproject.toml` build. |

No recommendation was produced by either baseline path.

### Candidate observations

| Path | Command boundary | Exit | Elapsed | Observed result |
| --- | --- | ---: | ---: | --- |
| Unsupported-interpreter preflight | README version check with default Python 3.9.6 | 1 | 0.168 s | Stopped before environment creation with `AssertionError: EvoPM requires Python 3.11+`. |
| Editable install | Revised path using Python 3.11.15 | 0 | 27.083 s | Installation completed and the CLI produced a recommendation. |
| No install | Revised path using Python 3.11.15 | 0 | 0.135 s | The CLI produced the same recommendation. |

The first successful recommendation was:

```text
Base pattern: single_agent_with_tools
Additions: router, parallel_fan_out_fan_in, deterministic_validator,
           evaluator_optimizer, persistence_or_durable_runtime
Upgrade trigger: Add manager/workers only when subtasks must be discovered at
                 runtime and the decomposition benefit is measurable.
```

### Evaluation

| Rule | Result | Evidence |
| --- | --- | --- |
| Python 3.11+ is visible before environment creation | Pass | The prerequisite and executable check precede the setup commands. |
| Unsupported default interpreter is detected early | Pass | Python 3.9.6 stopped at the preflight in 0.168 seconds. |
| Installed and no-install paths return exit status 0 | Pass | Both Python 3.11.15 paths completed successfully. |
| First recommendation appears within five minutes | Pass | The slower full install path completed in 27.083 seconds after checkout. |
| Existing tests and Ruff checks pass | Pass | 17 tests passed; Ruff reported all checks passed. |
| Public-content review passes | Pass | Manual review and path/name/secret scans found no private material or unsupported conclusion. |

## Outcome

Keep the README change. The same case changed from an unexplained failure to an
early, actionable version boundary and two successful paths. This closes only
the onboarding evidence loop. It does not support a claim that EvoPM improves
project decisions or reduces rework.

## Revisit trigger

Revisit the next product direction when either:

- an external user reports that the quick start still fails or is unclear;
- two independent users complete the first-use path and provide evidence about recommendation usefulness;
- a real project is ready for a controlled baseline-versus-EvoPM comparison.

Until then, do not expand the CLI based only on internal architectural ideas.
