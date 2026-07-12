# EvoPM HyperFrames Product Demo Design

## Goal

Create a 36-second English product video that explains why EvoPM exists, shows one real CLI decision as evidence, and directs developers to the repository.

## Audience and channel

- Primary audience: developers discovering EvoPM through X or GitHub.
- Format: 16:9 MP4, 1920×1080.
- Language: English.
- Audio: light background music only; no narration.

## Storyboard

### Scene 1 · The question · 0–4s

Show: `Do I need a multi-agent system?`

Purpose: establish the decision developers face before they choose frameworks or runtimes.

### Scene 2 · Complexity expands · 4–9s

Animate a simple task branching into Manager, Workers, Router, MCP, persistence, and evaluation components.

Purpose: show how architecture can expand before the need is proven.

### Scene 3 · Give EvoPM the task · 9–14s

Show the quarterly-report task and the command:

```text
evopm triage examples/quarterly-report.json
```

### Scene 4 · Evidence · 14–23s

Use a shortened segment of the existing VHS terminal recording. Keep the task and base-pattern result visible; do not make viewers read the complete CLI output.

### Scene 5 · Decision · 23–31s

Emphasize:

- Base pattern: `single_agent_with_tools`
- Add only what the task requires.
- Not needed now: Manager/Workers, MCP, A2A.

### Scene 6 · Close · 31–36s

Show:

```text
Decide before you orchestrate.
github.com/Longado/EvoPM
```

## Visual direction

- Dark neutral background with restrained violet and blue accents.
- Large editorial typography; one claim per scene.
- Diagrams are abstract responsibility blocks, not framework logos.
- Terminal footage is supporting evidence, not the main visual language.
- Motion should clarify state changes; avoid decorative particles and excessive transitions.

## Implementation boundary

- Use HyperFrames as the HTML-to-MP4 renderer.
- Reuse the verified VHS MP4 as the only recorded source asset.
- Keep the composition deterministic and version-controlled.
- Do not add narration, avatars, a product UI, analytics, or new EvoPM features.
- Use only local or permissively licensed audio; omit music if licensing cannot be verified.

## Deliverables

- HyperFrames composition source and local assets.
- One final 1920×1080 MP4.
- One representative poster frame for review and social sharing.

## Acceptance criteria

- Duration is 34–38 seconds.
- A viewer understands the problem and recommendation without audio.
- The terminal segment occupies less than one-third of the runtime.
- The repository URL is visible for at least three seconds.
- No local paths, private data, credentials, or unverified claims appear.
- Rendering is reproducible from version-controlled source.
