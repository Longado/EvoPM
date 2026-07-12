# EvoPM VHS Demo Implementation Plan

> **For agentic workers:** Execute this plan inline and verify each checkpoint before continuing. No subagents are required.

**Goal:** Generate a reproducible English terminal demo that shows EvoPM selecting the simplest justified orchestration pattern for a quarterly-report task.

**Architecture:** A single VHS tape is the source of truth for both GIF and MP4 outputs. The tape runs the existing deterministic CLI from the repository root; the README embeds the GIF and points to the existing quick start.

**Tech Stack:** VHS, Python 3, EvoPM CLI, ffmpeg/ffprobe, Markdown

---

## File map

- Create `docs/demo/evopm-triage.tape`: reproducible terminal narrative.
- Generate `docs/demo/evopm-triage.gif`: GitHub README asset.
- Generate `docs/demo/evopm-triage.mp4`: X-ready video asset.
- Modify `README.md`: add the demo immediately before Quick start.

### Task 1: Create and validate the VHS tape

- [ ] Create `docs/demo/evopm-triage.tape` with exactly this content:

```text
Output docs/demo/evopm-triage.gif
Output docs/demo/evopm-triage.mp4

Require python

Set Shell "bash"
Set FontSize 18
Set Width 1200
Set Height 900
Set Padding 24
Set Theme "Catppuccin Mocha"
Set TypingSpeed 28ms
Set Framerate 30

Type "clear" Enter
Sleep 1s

Type "echo 'Do I need a multi-agent system for this task?'" Enter
Sleep 2s

Type "PYTHONPATH=src python -m evopm triage examples/quarterly-report.json" Enter
Sleep 8s

Type "echo 'Make the architecture decision before building the architecture.'" Enter
Sleep 4s
```

- [ ] Run `vhs validate docs/demo/evopm-triage.tape`.

Expected: the command exits with status 0 and reports no parse error.

- [ ] Run `PYTHONPATH=src python -m evopm triage examples/quarterly-report.json`.

Expected: output includes `Base pattern: single_agent_with_tools`, `Not needed now`, and `bounded_manager_workers`.

### Task 2: Generate and verify both assets

- [ ] Run `vhs docs/demo/evopm-triage.tape` from the repository root.

Expected: both `docs/demo/evopm-triage.gif` and `docs/demo/evopm-triage.mp4` exist and are non-empty.

- [ ] Run:

```bash
ffprobe -v error -show_entries format=duration,size \
  -of default=noprint_wrappers=1 docs/demo/evopm-triage.mp4
```

Expected: duration is between 15 and 60 seconds and size is greater than zero.

- [ ] Render one representative MP4 frame to a temporary PNG and visually inspect it:

```bash
ffmpeg -y -ss 8 -i docs/demo/evopm-triage.mp4 -frames:v 1 /tmp/evopm-demo-frame.png
```

Expected: the task question and/or EvoPM recommendation is legible, with no local path, credential, or private data visible.

### Task 3: Add the README entry and run repository verification

- [ ] Insert this section immediately before `## Quick start` in `README.md`:

```markdown
## See it decide

![EvoPM choosing an orchestration pattern](docs/demo/evopm-triage.gif)

The example starts with a quarterly-report task, recommends the simplest justified control pattern, and makes the unnecessary complexity explicit. Reproduce it with the [quick start](#quick-start) below.
```

- [ ] Run `python -m pytest -q`.

Expected: all existing tests pass.

- [ ] Run `python -m ruff check .`.

Expected: no lint errors.

- [ ] Run `git diff --check`.

Expected: no whitespace errors.

- [ ] Inspect `git diff -- README.md docs/demo/evopm-triage.tape` and verify that only the approved demo scope changed.

### Task 4: Commit the verified demo

- [ ] Commit only the tape, generated assets, and README integration:

```bash
git add README.md \
  docs/demo/evopm-triage.tape \
  docs/demo/evopm-triage.gif \
  docs/demo/evopm-triage.mp4
git commit -m "docs: add reproducible EvoPM demo"
```

Expected: one focused commit. Do not tag, push, or publish `v0.1.0` in this task.
