# One-Question Decision Loop Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use
> superpowers:executing-plans to implement this plan task-by-task. Steps use
> checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make the public EvoPM decision protocol open a loop only when exactly
one owner question can change the decision.

**Architecture:** Keep enforcement in the public design and decision-card
template. The existing deterministic orchestration CLI remains unchanged; a
small structural check verifies that the README, core design, protocol, and
template state the same invariant.

**Tech Stack:** Markdown, Python 3.11+ structural checks, pytest, Ruff

---

## File map

- `README.md`: give users the short product rule and link to the full protocol.
- `docs/core-design.md`: make the exactly-one, decision-changing rule part of
  the PM Core output contract.
- `docs/one-question-loop.md`: remove implementation-stage wording and remain
  the canonical public protocol and synthetic example.
- `templates/decision-card.md`: guide a reviewer through the gate, one question,
  predeclared consequences, and the closed decision.
- `src/`, `tests/`: no changes; existing tests prove the orchestration CLI is
  unaffected.

### Task 1: Establish the pre-change structural failure

**Files:**
- Test: `README.md`
- Test: `docs/core-design.md`
- Test: `docs/one-question-loop.md`
- Test: `templates/decision-card.md`

- [ ] **Step 1: Run the contract check before implementation**

Run:

```bash
python3 - <<'PY'
from pathlib import Path

readme = Path("README.md").read_text()
core = Path("docs/core-design.md").read_text()
protocol = Path("docs/one-question-loop.md").read_text()
template = Path("templates/decision-card.md").read_text()

assert "[one-question decision loop](docs/one-question-loop.md)" in readme
assert "## One-question loops" in core
assert "exactly one question" in core
assert "does not open a loop" in core
assert "> Status: public protocol" in protocol
assert "## One-question loop gate" in template
assert "## Decision consequences" in template
assert "## Closed decision" in template
print("one-question contract passed")
PY
```

Expected: FAIL on the first missing assertion because the approved design has
not yet been integrated into the public entry points.

### Task 2: Integrate the invariant into the PM Core

**Files:**
- Modify: `docs/core-design.md`

- [ ] **Step 1: Add the one-question loop contract**

Insert this section after `## Output budget` and its existing list:

```markdown
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
```

- [ ] **Step 2: Tighten the output budget wording**

Change this list item:

```markdown
- one pending decision;
```

to:

```markdown
- one decision-changing question, only when a loop is open;
```

- [ ] **Step 3: Verify the core contract**

Run:

```bash
python3 - <<'PY'
from pathlib import Path

text = Path("docs/core-design.md").read_text()
assert "## One-question loops" in text
assert "A loop contains exactly one question" in text
assert "does not open a loop" in text
assert "one decision-changing question, only when a loop is open" in text
print("core contract passed")
PY
```

Expected: `core contract passed`.

### Task 3: Make the decision-card template enforce one loop question

**Files:**
- Modify: `templates/decision-card.md`

- [ ] **Step 1: Replace the pending-decision section**

Keep the existing core judgment, evidence, material recommendations, and revisit
sections. Replace `## Pending decision` and its instruction with:

```markdown
## One-question loop gate

Name the owner decision and state how different answers would change the
judgment, approved scope, next action, or revisit condition. If no answer can
change one of those outcomes, remove this section and do not open a loop.

## Question

Write exactly one question. Do not combine requests or include a follow-up
question.

## Decision consequences

- Answer or boundary: resulting decision and next action.
- Answer or boundary: resulting decision and next action.
- Ambiguous answer: close as `HOLD` and record the ambiguity.

## Closed decision

Complete this section after the owner answers. Do not add another question.

- Owner answer:
- Resulting judgment:
- Next action:
- Revisit condition:
- Did the answer change the decision: yes / no
```

- [ ] **Step 2: Verify the template structure**

Run:

```bash
python3 - <<'PY'
from pathlib import Path

text = Path("templates/decision-card.md").read_text()
required = (
    "## One-question loop gate",
    "## Question",
    "Write exactly one question",
    "## Decision consequences",
    "Ambiguous answer: close as `HOLD`",
    "## Closed decision",
    "Do not add another question",
)
for item in required:
    assert item in text, item
assert "## Pending decision" not in text
print("template contract passed")
PY
```

Expected: `template contract passed`.

### Task 4: Publish the protocol from the README

**Files:**
- Modify: `README.md`
- Modify: `docs/one-question-loop.md`

- [ ] **Step 1: Add concise README guidance**

In the `## Design` section, extend the final paragraph so it reads:

```markdown
Only the deterministic orchestration triage CLI is implemented in this release.
See [core design](docs/core-design.md) for the intended boundary, the
[one-question decision loop](docs/one-question-loop.md) for the rule that a loop
opens only around one decision-changing owner question, and the
[first-use closed-loop case](docs/first-use-closed-loop.md) for onboarding
evidence.
```

- [ ] **Step 2: Add the loop rule to the public principles**

Add this bullet after `Keep recommendations short, explainable, rejectable, and
reversible.`:

```markdown
- Open a loop only for exactly one owner question whose answer can change the decision.
```

- [ ] **Step 3: Mark the approved design as the public protocol**

In `docs/one-question-loop.md`, replace:

```markdown
> Design status: approved for implementation on 2026-07-15
```

with:

```markdown
> Status: public protocol
```

Change the heading `## Public implementation scope` to:

```markdown
## Public scope
```

Change its opening sentence from `The first implementation changes only:` to:

```markdown
This protocol is implemented through:
```

- [ ] **Step 4: Verify the public entry points and example**

Run:

```bash
python3 - <<'PY'
from pathlib import Path

readme = Path("README.md").read_text()
protocol = Path("docs/one-question-loop.md").read_text()
assert "[one-question decision loop](docs/one-question-loop.md)" in readme
assert "Open a loop only for exactly one owner question" in readme
assert "> Status: public protocol" in protocol
assert "## Public scope" in protocol
assert "## Synthetic example" in protocol
assert protocol.count("?") == 1
print("public protocol passed")
PY
```

Expected: `public protocol passed`.

### Task 5: Run complete verification

**Files:**
- Verify: `README.md`
- Verify: `docs/core-design.md`
- Verify: `docs/one-question-loop.md`
- Verify: `templates/decision-card.md`
- Verify unchanged: `src/`
- Verify unchanged: `tests/`

- [ ] **Step 1: Run the full one-question contract check**

Run:

```bash
python3 - <<'PY'
from pathlib import Path

readme = Path("README.md").read_text()
core = Path("docs/core-design.md").read_text()
protocol = Path("docs/one-question-loop.md").read_text()
template = Path("templates/decision-card.md").read_text()

assert "[one-question decision loop](docs/one-question-loop.md)" in readme
assert "## One-question loops" in core
assert "exactly one question" in core
assert "does not open a loop" in core
assert "> Status: public protocol" in protocol
assert protocol.count("?") == 1
assert "## One-question loop gate" in template
assert "## Decision consequences" in template
assert "## Closed decision" in template
assert "## Pending decision" not in template
print("one-question contract passed")
PY
```

Expected: `one-question contract passed`.

- [ ] **Step 2: Run the existing project checks**

Run:

```bash
PYTHONPATH=src ../../.venv/bin/python -m pytest -q
../../.venv/bin/python -m ruff check .
git diff --check
```

Expected: 17 tests pass, Ruff reports `All checks passed!`, and
`git diff --check` prints nothing.

- [ ] **Step 3: Verify Markdown links**

Run:

```bash
python3 - <<'PY'
import re
from pathlib import Path

for source in (Path("README.md"), Path("docs/core-design.md")):
    for target in re.findall(r"\[[^]]+\]\(([^)]+\.md)\)", source.read_text()):
        path = source.parent / target
        assert path.exists(), f"broken link: {source} -> {target}"
print("markdown links passed")
PY
```

Expected: `markdown links passed`.

- [ ] **Step 4: Scan the public diff for private or unsupported content**

Run:

```bash
git diff -- README.md docs/core-design.md docs/one-question-loop.md templates/decision-card.md |
  rg -n '/Users/|Eddie|customer|client|contract|password|secret|token|api[_-]?key' &&
  exit 1 || true
```

Expected: no matches.

- [ ] **Step 5: Review the final scope**

Run:

```bash
git status --short
git diff --stat
git diff -- README.md docs/core-design.md docs/one-question-loop.md templates/decision-card.md
```

Expected: only the four approved public files are modified; `src/` and
`tests/` are unchanged.

- [ ] **Step 6: Commit the implementation**

Run:

```bash
git add README.md docs/core-design.md docs/one-question-loop.md templates/decision-card.md
git commit -m "docs: enforce one-question decision loops"
```

Expected: one focused implementation commit after the design and plan commits.
