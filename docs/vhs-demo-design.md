# EvoPM VHS Demo Design

## Goal

Show an unfamiliar developer, in under 60 seconds, how EvoPM turns one concrete task into an explainable orchestration decision and helps avoid unnecessary architecture.

## Audience and channel

- Primary audience: developers discovering EvoPM through GitHub or X.
- Language: English.
- Primary surface: GitHub README GIF.
- Secondary surface: an MP4 suitable for X.

## Story

1. Ask: `Do I need a multi-agent system for this task?`
2. Run `evopm triage examples/quarterly-report.json`.
3. Show the recommended base control pattern and the constraints that triggered additional mechanisms.
4. Make the avoided complexity explicit.
5. End with: `Make the architecture decision before building the architecture.`
6. Point to the repository quick start.

## Implementation boundary

- Use a single VHS tape as the reproducible source.
- Generate one GIF and one MP4 from the same tape.
- Do not add product features, a web UI, voice-over, analytics, or a hosted demo service.
- Do not expose local paths, credentials, private data, or internal project context.

## Deliverables

- `docs/demo/evopm-triage.tape`
- `docs/demo/evopm-triage.gif`
- `docs/demo/evopm-triage.mp4`
- One README section embedding the GIF and linking to the quick start.

## Acceptance criteria

- The complete demo is 45–60 seconds.
- The tape runs from a clean checkout using documented project commands.
- A stranger can identify the problem, recommendation, and avoided complexity within 10 seconds.
- A stranger can reproduce the demonstrated command within 5 minutes.
- The generated assets contain no machine-specific or sensitive information.
- Re-running the tape produces the same narrative without manual editing.

## Release boundary

The demo may accompany `v0.1.0`, but creating the release is a separate publish action. This task only prepares and verifies the demo assets and README integration.
