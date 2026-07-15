# One-question decision loop

> Status: public protocol

The one-question decision loop keeps EvoPM focused on decisions that require the
project owner. It is a review protocol, not an interactive runtime or workflow
engine.

## Problem

A review can create reading burden without improving a decision. Multiple
questions make the owner reconstruct priorities, while questions whose answers
cannot change the outcome are process noise.

EvoPM therefore opens a loop only around one unresolved decision that matters
now.

## Decision invariant

A valid loop contains exactly one question, and the answer to that question
must be capable of changing at least one of:

- the current `CONTINUE`, `HOLD`, or `STOP` judgment;
- the approved scope;
- the next action;
- the revisit condition.

If no such question exists, EvoPM does not open a loop. It records the current
judgment or says that there is no material change.

## Loop contract

### 1. Gate

Before opening a loop, identify the unresolved owner decision and describe how
different answers would change the outcome. Evidence collection, technical
verification, and reversible implementation details are not owner questions
unless they cross a product, public-commitment, authority, or irreversible-risk
boundary.

### 2. Open

The open loop contains:

1. the current judgment;
2. only the evidence needed to answer;
3. exactly one question;
4. the decision consequence of each materially different answer.

The context may contain statements and evidence gaps, but it must not hide
additional requests or interrogative prompts. A compound question counts as
multiple questions and is invalid.

### 3. Wait

After asking the question, EvoPM waits for the owner's answer. It does not add a
second question to improve, clarify, or confirm the same loop.

If the answer is ambiguous, the loop closes as `HOLD` with the ambiguity
recorded. Resolving that ambiguity requires a new loop with its own single
decision-changing question.

### 4. Close

The closed loop records:

- the owner's answer;
- the resulting judgment;
- the next action;
- the revisit condition;
- whether the answer actually changed the decision.

No follow-up question is included in the closed record.

## Synthetic example

**Current judgment:** `HOLD` the next product feature until one priority is
chosen.

**Evidence:** First-run completion is below the agreed threshold. Two users have
also requested CSV export, but repeat demand is not yet established. The team
has capacity for one change in the next iteration.

**Question:** Should the next iteration prioritize CSV export over improving
first-run completion?

**Decision consequences:**

- `Yes` changes the next action to a bounded CSV-export experiment.
- `No` keeps first-run completion as the next action.
- An ambiguous answer closes the loop as `HOLD`.

This is one question even though it has multiple possible answers. Each answer
has a predeclared effect on the decision.

## Public scope

This protocol is implemented through:

- the PM Core output rule in `docs/core-design.md`;
- the public decision-card template;
- concise README guidance and a link to this protocol;
- one public, explicitly synthetic example.

It does not add a state machine, database, natural-language question generator,
interactive CLI command, or change to `evopm triage`.

## Acceptance checks

The implementation is acceptable when:

1. the public design states the exactly-one, decision-changing invariant;
2. the template provides space for one question and predeclared answer effects;
3. the template cannot be read as inviting follow-up questions in the same loop;
4. the README explains when a loop should not start;
5. the example contains exactly one question and shows how answers change the
   next action;
6. existing CLI behavior and tests remain unchanged;
7. public-content and link checks pass.

## Revisit condition

Consider deterministic validation only after real use produces repeated loops
with zero questions, multiple questions, or questions that do not change a
decision. Until then, keep enforcement in the protocol and review template.
