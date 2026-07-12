# EvoPM HyperFrames Demo Implementation Plan

**Goal:** Render a silent 36-second English product introduction that explains EvoPM without showing a terminal.

**Architecture:** One self-contained HyperFrames HTML composition owns the six-scene timeline, typography, diagrams, and motion. HyperFrames 0.7.54 renders the MP4; FFmpeg extracts the poster frame. The separate VHS recording remains a README technical demo.

**Tech Stack:** HyperFrames 0.7.54, HTML/CSS, GSAP 3, FFmpeg

## File map

- `docs/demo/hyperframes/index.html`: six-scene product composition.
- `docs/demo/evopm-product-demo.mp4`: final 1920×1080 video.
- `docs/demo/evopm-product-demo-poster.png`: representative closing frame.

## Build and review

- [x] Frame the problem: complexity often arrives before proof.
- [x] Show a representative task and its constraints as a product card.
- [x] Explain the decision flow: read constraints, choose the base pattern, name the upgrade trigger.
- [x] Show the resulting recommendation and unnecessary complexity.
- [x] Close with the product promise and public repository URL.
- [x] Keep terminal footage out of the product video.
- [x] Run HyperFrames lint and validation.
- [x] Inspect representative frames for readability and visual continuity.
- [x] Render the final MP4 and extract its poster.
- [x] Run repository tests, style checks, and media metadata checks.

## Acceptance

- Silent H.264 MP4, 1920×1080, approximately 36 seconds.
- No terminal, local path, private name, credential, or unsupported product claim appears.
- The three-step decision logic is readable without narration.
- `single_agent_with_tools` is the strongest visual element in the recommendation scene.
- The closing repository URL is legible.
