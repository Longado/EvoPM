# First-use closed-loop case

> Status: design review pending; implementation has not started  
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

## Revisit trigger

Revisit the next product direction when either:

- an external user reports that the quick start still fails or is unclear;
- two independent users complete the first-use path and provide evidence about recommendation usefulness;
- a real project is ready for a controlled baseline-versus-EvoPM comparison.

Until then, do not expand the CLI based only on internal architectural ideas.
