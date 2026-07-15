# EvoPM core design

EvoPM is a lightweight project decision layer. Its purpose is to improve project judgment without becoming another workflow that the team must maintain.

## 1. PM Core

The PM Core asks:

- Why should this project exist?
- Who will use the result in a real workflow?
- What is the smallest useful scope?
- What evidence is required to continue, release, hold, or stop?
- Which decision has been made, by whom, and what changes next?

It does not replace the project owner or generate activity to fill a template.

## 2. Project Adapters

Adapters translate domain evidence into project decisions. The first adapter covers software and agent development:

- technical feasibility;
- whether an LLM or agent is needed;
- orchestration topology;
- permissions and tool boundaries;
- cost, testing, release, and recovery requirements.

The public CLI implements only the orchestration-triage portion of this adapter.

## 3. Governed Learning

The learning layer separates observations from rules:

1. record an observation with evidence, context, outcome, and counterexamples;
2. keep it as a candidate;
3. promote it only after two independent project validations or explicit owner confirmation;
4. version the rule and preserve a rollback point;
5. suspend it when a credible counterexample changes its boundary.

High-risk rules involving permissions, security, external actions, sensitive data, or irreversible operations always require explicit human approval.

## Output budget

A normal EvoPM review should contain no more than:

- one core judgment;
- three material recommendations;
- one decision-changing question, only when a loop is open;
- the evidence gap and confidence level.

If there is no material change, EvoPM should say so instead of repeating project history.

## One-question loops

A loop contains exactly one question: an unresolved owner question whose answer
can change the current judgment, approved scope, next action, or revisit
condition. The loop presents the minimum evidence needed, asks that one
question, waits for the answer, and then closes with the resulting decision and
next action.

If no decision-changing owner question exists, EvoPM does not open a loop. It
records the current judgment or says that there is no material change. It does
not invent a question to keep the process active.

See the [one-question decision loop](one-question-loop.md) for the full
protocol and synthetic example.

## Stop conditions

Reduce or disable EvoPM when:

- three consecutive reviews produce no material judgment or action;
- recommendations repeat generic advice;
- maintaining EvoPM costs more than the rework or delay it prevents;
- the output increases reading burden without changing a decision.
