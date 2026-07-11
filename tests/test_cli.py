import json
import os
import subprocess
import sys


def run_cli(*args: str, stdin: str | None = None) -> subprocess.CompletedProcess[str]:
    env = {**os.environ, "PYTHONPATH": "src"}
    return subprocess.run(
        [sys.executable, "-m", "evopm", *args],
        input=stdin,
        text=True,
        capture_output=True,
        env=env,
        check=False,
    )


def test_cli_renders_json(tmp_path):
    profile = tmp_path / "task.json"
    profile.write_text(
        json.dumps({"task": "Research", "dynamic_tool_choice": True}), encoding="utf-8"
    )

    completed = run_cli("triage", str(profile), "--format", "json")

    assert completed.returncode == 0
    assert json.loads(completed.stdout)["base_pattern"] == "single_agent_with_tools"


def test_cli_reads_stdin_and_renders_markdown():
    completed = run_cli(
        "triage",
        "-",
        stdin=json.dumps({"task": "Format report", "hard_validation_rules": True}),
    )

    assert completed.returncode == 0
    assert "# EvoPM orchestration recommendation" in completed.stdout
    assert "`deterministic_validator`" in completed.stdout


def test_cli_reports_invalid_profile(tmp_path):
    profile = tmp_path / "task.json"
    profile.write_text("{}", encoding="utf-8")

    completed = run_cli("triage", str(profile))

    assert completed.returncode == 2
    assert completed.stderr == "error: task is required\n"


def test_cli_reports_invalid_json(tmp_path):
    profile = tmp_path / "task.json"
    profile.write_text("{", encoding="utf-8")

    completed = run_cli("triage", str(profile))

    assert completed.returncode == 2
    assert completed.stderr.startswith("error: invalid JSON:")
