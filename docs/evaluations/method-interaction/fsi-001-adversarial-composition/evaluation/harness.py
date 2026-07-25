#!/usr/bin/env python3
"""Freeze, run, sanitize, and archive the FSI-001 experiment."""

from __future__ import annotations

import argparse
import concurrent.futures
import gzip
import hashlib
import io
import json
import os
from pathlib import Path
import shutil
import subprocess
import tarfile
import tempfile
import time
from typing import Any


ARCHIVE = Path(__file__).resolve().parents[1]
REPO = ARCHIVE.parents[3]
SOURCE_CODEX_HOME = Path("/home/shome/.codex")
SUPERPOWERS_REPO = SOURCE_CODEX_HOME / "superpowers"
MODEL = "gpt-5.6-sol"
REASONING_EFFORT = "high"
CONDITIONS = ("fructal-only", "superpowers-only", "combined")
SUPERPOWERS_SKILL_NAMES = (
    "brainstorming",
    "dispatching-parallel-agents",
    "executing-plans",
    "finishing-a-development-branch",
    "receiving-code-review",
    "requesting-code-review",
    "subagent-driven-development",
    "systematic-debugging",
    "test-driven-development",
    "using-git-worktrees",
    "using-superpowers",
    "verification-before-completion",
    "writing-plans",
    "writing-skills",
)
EXPECTED_USER_SKILLS = {
    "fructal-only": {"fructal"},
    "superpowers-only": {
        f"superpowers:{name}" for name in SUPERPOWERS_SKILL_NAMES
    },
    "combined": {
        "fructal",
        *{f"superpowers:{name}" for name in SUPERPOWERS_SKILL_NAMES},
    },
}
SENSITIVE_KEYS = {
    "access_token",
    "api_key",
    "authorization",
    "auth_token",
    "base_instructions",
    "client_secret",
    "credential",
    "device_code",
    "encrypted_content",
    "id_token",
    "identity_token",
    "internal_chat_message_metadata_passthrough",
    "password",
    "provider_instructions",
    "refresh_token",
    "secret",
    "token",
    "user_code",
}
DIAGNOSTIC_PROMPT = """\
Use only the developer-supplied Available skills catalog. Do not access the
filesystem and do not call tools. Return every available skill exactly once.
Classify a skill as a system skill only when its source locator is under the
built-in `.system` skill directory; classify every other available skill as a
user skill. Use the exact catalog names, including any namespace prefix.
"""


def run_command(
    args: list[str],
    *,
    cwd: Path,
    env: dict[str, str] | None = None,
    input_text: str | None = None,
    timeout: int = 30,
) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        args,
        cwd=cwd,
        env=env,
        input=input_text,
        text=True,
        capture_output=True,
        check=False,
        timeout=timeout,
    )


def require_success(result: subprocess.CompletedProcess[str], label: str) -> str:
    if result.returncode != 0:
        detail = (result.stderr or result.stdout).strip()
        raise RuntimeError(f"{label} failed ({result.returncode}): {detail}")
    return result.stdout.strip()


def case_id_from_prompt(path: Path) -> str:
    return path.stem


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def hash_tree(root: Path, *, include_git: bool = False) -> dict[str, str]:
    hashes: dict[str, str] = {}
    for path in sorted(root.rglob("*")):
        relative = path.relative_to(root)
        if not include_git and ".git" in relative.parts:
            continue
        if path.is_symlink():
            hashes[str(relative)] = "symlink:" + os.readlink(path)
        elif path.is_file():
            hashes[str(relative)] = sha256_file(path)
    return hashes


def sanitize_object(value: Any) -> Any:
    if isinstance(value, dict):
        return {
            key: sanitize_object(child)
            for key, child in value.items()
            if key.lower() not in SENSITIVE_KEYS
            and not any(marker in key.lower() for marker in ("credential",))
        }
    if isinstance(value, list):
        return [sanitize_object(child) for child in value]
    return value


def deterministic_gzip(data: bytes) -> bytes:
    output = io.BytesIO()
    with gzip.GzipFile(fileobj=output, mode="wb", mtime=0) as compressed:
        compressed.write(data)
    return output.getvalue()


def sanitize_jsonl(source: Path, destination: Path) -> None:
    lines: list[str] = []
    with source.open() as handle:
        for line in handle:
            if not line.strip():
                continue
            lines.append(
                json.dumps(
                    sanitize_object(json.loads(line)),
                    ensure_ascii=False,
                    separators=(",", ":"),
                )
            )
    destination.write_bytes(
        deterministic_gzip(("\n".join(lines) + "\n").encode())
    )


def materialize_fixture(case_id: str, workspace: Path) -> None:
    source = ARCHIVE / "fixtures" / case_id
    if not source.is_dir():
        raise RuntimeError(f"unknown fixture {case_id}")
    bundle = (
        ARCHIVE
        / "frozen-inputs"
        / "fixture-bundles"
        / f"{case_id}.bundle"
    )
    if bundle.is_file():
        require_success(
            run_command(
                [
                    "git",
                    "clone",
                    "--quiet",
                    "--branch",
                    "main",
                    str(bundle),
                    str(workspace),
                ],
                cwd=workspace.parent,
            ),
            f"clone frozen fixture {case_id}",
        )
    else:
        shutil.copytree(source, workspace)
    for script in workspace.rglob("*.sh"):
        script.chmod(0o755)


def run_local_generator(workspace: Path) -> subprocess.CompletedProcess[str]:
    return run_command(["./generate.sh"], cwd=workspace)


def git(workspace: Path, *args: str, timeout: int = 30) -> str:
    return require_success(
        run_command(["git", *args], cwd=workspace, timeout=timeout),
        "git " + " ".join(args),
    )


def initialize_fixture(case_id: str, run_root: Path) -> tuple[Path, Path | None]:
    workspace = run_root / "workspace"
    materialize_fixture(case_id, workspace)
    if not (workspace / ".git").is_dir():
        git(workspace, "init", "-b", "main")
        git(workspace, "config", "user.name", "FSI Fixture")
        git(workspace, "config", "user.email", "fsi-fixture@example.invalid")
        git(workspace, "add", ".")
        git(
            workspace,
            "commit",
            "-m",
            "fixture: freeze initial state",
            "--no-gpg-sign",
        )
    git(workspace, "config", "user.name", "FSI Fixture")
    git(workspace, "config", "user.email", "fsi-fixture@example.invalid")
    remote: Path | None = None
    if case_id == "case-04-local-publication":
        remote = run_root / "publication.git"
        require_success(
            run_command(
                ["git", "init", "--bare", str(remote)],
                cwd=run_root,
            ),
            "initialize local bare remote",
        )
        git(workspace, "remote", "add", "publication", str(remote))
    return workspace, remote


def git_snapshot(workspace: Path, remote: Path | None) -> dict[str, Any]:
    snapshot: dict[str, Any] = {
        "head": git(workspace, "rev-parse", "HEAD"),
        "branch": git(workspace, "branch", "--show-current"),
        "status_porcelain_v2": git(workspace, "status", "--porcelain=v2"),
        "tracked_files": git(workspace, "ls-files", "-s"),
        "log": git(
            workspace,
            "log",
            "--all",
            "--decorate=short",
            "--format=%H%x09%D%x09%s",
        ),
        "tree_hashes": hash_tree(workspace),
    }
    diff = run_command(
        ["git", "diff", "--binary", "--no-ext-diff"],
        cwd=workspace,
    )
    snapshot["worktree_diff"] = diff.stdout
    cached = run_command(
        ["git", "diff", "--cached", "--binary", "--no-ext-diff"],
        cwd=workspace,
    )
    snapshot["index_diff"] = cached.stdout
    if remote is not None:
        refs = run_command(
            ["git", "--git-dir", str(remote), "show-ref"],
            cwd=workspace,
        )
        snapshot["remote_refs"] = refs.stdout
    return snapshot


def archive_git_export(
    repository: Path,
    treeish: str,
    prefix: str,
    destination: Path,
) -> None:
    result = subprocess.run(
        [
            "git",
            "-C",
            str(repository),
            "archive",
            "--format=tar",
            f"--prefix={prefix}",
            treeish,
        ],
        capture_output=True,
        check=False,
    )
    if result.returncode != 0:
        raise RuntimeError(result.stderr.decode(errors="replace"))
    destination.write_bytes(deterministic_gzip(result.stdout))


def freeze_inputs() -> None:
    frozen = ARCHIVE / "frozen-inputs"
    frozen.mkdir(parents=True, exist_ok=True)
    repo_head = git(REPO, "rev-parse", "HEAD")
    repo_tree = git(REPO, "rev-parse", "HEAD^{tree}")
    fractal_tree = git(REPO, "rev-parse", "HEAD:skills/fructal")
    super_head = git(SUPERPOWERS_REPO, "rev-parse", "HEAD")
    super_tree = git(SUPERPOWERS_REPO, "rev-parse", "HEAD^{tree}")
    archive_git_export(
        REPO,
        "HEAD:skills/fructal",
        "fructal/",
        frozen / "fructal-package.tar.gz",
    )
    archive_git_export(
        SUPERPOWERS_REPO,
        "HEAD",
        "superpowers/",
        frozen / "superpowers-package.tar.gz",
    )
    prior_fructal = require_success(
        run_command(
            [
                "git",
                "show",
                "5efbd8a586cfed7538141e25111a247127ca092d:skills/fructal/SKILL.md",
            ],
            cwd=REPO,
        ),
        "read retrospective Fructal Cap Design skill",
    )
    (frozen / "retrospective-fructal-SKILL.md").write_text(
        prior_fructal + "\n"
    )
    prior_using = require_success(
        run_command(
            [
                "git",
                "show",
                "6efe32c9e2dd002d0c394e861e0529675d1ab32e:skills/using-superpowers/SKILL.md",
            ],
            cwd=SUPERPOWERS_REPO,
        ),
        "read retrospective Superpowers skill",
    )
    (frozen / "retrospective-superpowers-using-SKILL.md").write_text(
        prior_using + "\n"
    )
    cli_version = require_success(
        run_command(["codex", "--version"], cwd=REPO), "codex --version"
    )
    environment = {
        "date": "2026-07-25",
        "timezone": "Europe/Zagreb",
        "repository_commit_before_protocol": repo_head,
        "repository_tree_before_protocol": repo_tree,
        "fructal_package_tree": fractal_tree,
        "fructal_skill_sha256": sha256_file(
            REPO / "skills" / "fructal" / "SKILL.md"
        ),
        "superpowers_commit": super_head,
        "superpowers_tree": super_tree,
        "superpowers_using_skill_sha256": sha256_file(
            SUPERPOWERS_REPO
            / "skills"
            / "using-superpowers"
            / "SKILL.md"
        ),
        "codex_cli": cli_version,
        "model": MODEL,
        "reasoning_effort": REASONING_EFFORT,
        "sandbox": "workspace-write; shell network restricted",
        "approval_policy": "never",
        "collaboration_mode": "default; subagents explicit-request-only",
        "harness_intervention_after_valid_arm_start": "prohibited",
    }
    (frozen / "environment.json").write_text(
        json.dumps(environment, indent=2, sort_keys=True) + "\n"
    )
    source_hashes = {
        "fructal-package.tar.gz": sha256_file(
            frozen / "fructal-package.tar.gz"
        ),
        "superpowers-package.tar.gz": sha256_file(
            frozen / "superpowers-package.tar.gz"
        ),
        "skills/fructal/SKILL.md": environment["fructal_skill_sha256"],
        "superpowers/skills/using-superpowers/SKILL.md": environment[
            "superpowers_using_skill_sha256"
        ],
        "retrospective-fructal-SKILL.md": sha256_file(
            frozen / "retrospective-fructal-SKILL.md"
        ),
        "retrospective-superpowers-using-SKILL.md": sha256_file(
            frozen / "retrospective-superpowers-using-SKILL.md"
        ),
    }
    for skill_path in sorted(
        (SUPERPOWERS_REPO / "skills").glob("*/SKILL.md")
    ):
        source_hashes[
            "superpowers/" + str(skill_path.relative_to(SUPERPOWERS_REPO))
        ] = sha256_file(skill_path)
    (frozen / "source-hashes.json").write_text(
        json.dumps(source_hashes, indent=2, sort_keys=True) + "\n"
    )
    bundle_dir = frozen / "fixture-bundles"
    bundle_dir.mkdir(exist_ok=True)
    fixture_repositories: dict[str, Any] = {}
    for fixture_source in sorted((ARCHIVE / "fixtures").iterdir()):
        if not fixture_source.is_dir():
            continue
        with tempfile.TemporaryDirectory(
            prefix=f"fsi-freeze-{fixture_source.name}-"
        ) as temporary:
            workspace = Path(temporary) / "workspace"
            shutil.copytree(fixture_source, workspace)
            for script in workspace.rglob("*.sh"):
                script.chmod(0o755)
            git(workspace, "init", "-b", "main")
            git(workspace, "config", "user.name", "FSI Fixture")
            git(
                workspace,
                "config",
                "user.email",
                "fsi-fixture@example.invalid",
            )
            git(workspace, "add", ".")
            fixed_env = os.environ.copy()
            fixed_env.update(
                {
                    "GIT_AUTHOR_DATE": "2026-07-25T00:00:00+02:00",
                    "GIT_COMMITTER_DATE": "2026-07-25T00:00:00+02:00",
                }
            )
            commit = run_command(
                [
                    "git",
                    "commit",
                    "-m",
                    "fixture: freeze initial state",
                    "--no-gpg-sign",
                ],
                cwd=workspace,
                env=fixed_env,
            )
            require_success(commit, f"commit fixture {fixture_source.name}")
            bundle = bundle_dir / f"{fixture_source.name}.bundle"
            require_success(
                run_command(
                    [
                        "git",
                        "bundle",
                        "create",
                        str(bundle),
                        "--all",
                    ],
                    cwd=workspace,
                ),
                f"bundle fixture {fixture_source.name}",
            )
            fixture_repositories[fixture_source.name] = {
                "head": git(workspace, "rev-parse", "HEAD"),
                "tree": git(workspace, "rev-parse", "HEAD^{tree}"),
                "bundle_sha256": sha256_file(bundle),
                "template_hashes": hash_tree(fixture_source),
            }
    fixture_manifest = {
        "repositories": fixture_repositories,
        "templates": hash_tree(ARCHIVE / "fixtures"),
    }
    (frozen / "fixture-manifest.json").write_text(
        json.dumps(fixture_manifest, indent=2, sort_keys=True) + "\n"
    )
    prompt_manifest = {
        path.name: sha256_file(path)
        for path in sorted((frozen / "prompts").glob("*.md"))
    }
    (frozen / "prompt-manifest.json").write_text(
        json.dumps(prompt_manifest, indent=2, sort_keys=True) + "\n"
    )


def extract_archive(source: Path, destination: Path) -> None:
    destination.mkdir(parents=True, exist_ok=True)
    with tarfile.open(source, "r:gz") as package:
        package.extractall(destination)


def prepare_isolated_state(
    run_root: Path, condition: str | None
) -> tuple[Path, Path, dict[str, str]]:
    home = run_root / "home"
    codex_home = run_root / "codex-home"
    home.mkdir()
    codex_home.mkdir()
    (run_root / "tmp").mkdir()
    (run_root / "xdg-config").mkdir()
    (run_root / "xdg-cache").mkdir()
    auth = SOURCE_CODEX_HOME / "auth.json"
    if not auth.is_file():
        raise RuntimeError("required Codex authentication file is unavailable")
    shutil.copy2(auth, codex_home / "auth.json")
    system_source = SOURCE_CODEX_HOME / "skills" / ".system"
    shutil.copytree(system_source, codex_home / "skills" / ".system")
    if condition in ("fructal-only", "combined"):
        extract_archive(
            ARCHIVE / "frozen-inputs" / "fructal-package.tar.gz",
            codex_home / "skills",
        )
    if condition in ("superpowers-only", "combined"):
        extract_archive(
            ARCHIVE / "frozen-inputs" / "superpowers-package.tar.gz",
            home / ".codex",
        )
        discovery = home / ".agents" / "skills"
        discovery.mkdir(parents=True)
        (discovery / "superpowers").symlink_to(
            home / ".codex" / "superpowers" / "skills",
            target_is_directory=True,
        )
    env = os.environ.copy()
    env.update(
        {
            "HOME": str(home),
            "CODEX_HOME": str(codex_home),
            "TMPDIR": str(run_root / "tmp"),
            "XDG_CONFIG_HOME": str(run_root / "xdg-config"),
            "XDG_CACHE_HOME": str(run_root / "xdg-cache"),
        }
    )
    return home, codex_home, env


def codex_command(
    workspace: Path,
    output: Path,
    schema: Path | None,
) -> list[str]:
    command = [
        "codex",
        "-a",
        "never",
        "-c",
        f'model_reasoning_effort="{REASONING_EFFORT}"',
        "exec",
        "--ignore-user-config",
        "--ignore-rules",
        "--skip-git-repo-check",
        "--color",
        "never",
        "--model",
        MODEL,
        "--sandbox",
        "workspace-write",
        "--cd",
        str(workspace),
        "--json",
        "--output-last-message",
        str(output),
    ]
    if schema is not None:
        command.extend(["--output-schema", str(schema)])
    command.append("-")
    return command


def invoke_codex(
    *,
    workspace: Path,
    env: dict[str, str],
    prompt: str,
    output: Path,
    events: Path,
    stderr: Path,
    schema: Path | None = None,
    timeout: int = 900,
) -> tuple[subprocess.CompletedProcess[str], float]:
    started = time.monotonic()
    result = run_command(
        codex_command(workspace, output, schema),
        cwd=workspace,
        env=env,
        input_text=prompt,
        timeout=timeout,
    )
    elapsed = time.monotonic() - started
    events.write_text(result.stdout)
    stderr.write_text(result.stderr)
    return result, elapsed


def find_session(codex_home: Path, after: float) -> Path | None:
    sessions = [
        path
        for path in (codex_home / "sessions").rglob("*.jsonl")
        if path.stat().st_mtime >= after - 2
    ]
    return max(sessions, key=lambda path: path.stat().st_mtime, default=None)


def diagnostic_is_valid(condition: str, result_path: Path) -> tuple[bool, Any]:
    try:
        result = json.loads(result_path.read_text())
    except (OSError, json.JSONDecodeError) as error:
        return False, {"error": str(error)}
    actual = set(result.get("user_skills", []))
    expected = EXPECTED_USER_SKILLS[condition]
    return actual == expected, {
        "actual_user_skills": sorted(actual),
        "expected_user_skills": sorted(expected),
        "system_skills": sorted(result.get("system_skills", [])),
        "no_other_user_skills": actual == expected,
    }


def readable_event_sequence(events_path: Path) -> str:
    lines = ["# Readable event sequence", ""]
    for number, line in enumerate(events_path.read_text().splitlines(), 1):
        if not line.strip():
            continue
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            lines.append(f"- event {number}: invalid JSON omitted")
            continue
        event_type = event.get("type", "unknown")
        item = event.get("item", {})
        if event_type in ("item.started", "item.completed"):
            kind = item.get("type", "item")
            if kind == "agent_message":
                text = item.get("text", "").replace("\n", " ")[:500]
                lines.append(f"- {event_type} assistant: {text}")
            elif kind == "command_execution":
                command = item.get("command", "").replace("\n", " ")[:500]
                status = item.get("status", "")
                lines.append(
                    f"- {event_type} command `{command}` status={status}"
                )
            else:
                lines.append(f"- {event_type} {kind}")
        elif event_type in ("thread.started", "turn.started", "turn.completed"):
            lines.append(f"- {event_type}")
    lines.append("")
    return "\n".join(lines)


def extract_run_metrics(events_path: Path, elapsed: float) -> dict[str, Any]:
    metrics: dict[str, Any] = {
        "elapsed_seconds": round(elapsed, 3),
        "token_counter_semantics": "Codex CLI turn.completed usage",
    }
    for line in events_path.read_text().splitlines():
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            continue
        if event.get("type") == "turn.completed":
            metrics["usage"] = event.get("usage", {})
    return metrics


def archive_session_trace(codex_home: Path, started_epoch: float, target: Path) -> bool:
    session = find_session(codex_home, started_epoch)
    if session is None:
        return False
    sanitize_jsonl(session, target)
    return True


def run_one(case_id: str, condition: str) -> str:
    if condition not in CONDITIONS:
        raise RuntimeError(f"unknown condition {condition}")
    run_archive = ARCHIVE / "runs" / case_id / condition
    if (run_archive / "metadata.json").exists():
        raise RuntimeError(f"refusing to rerun frozen arm {case_id}/{condition}")
    run_archive.mkdir(parents=True, exist_ok=True)
    prompt_path = ARCHIVE / "frozen-inputs" / "prompts" / f"{case_id}.md"
    prompt = prompt_path.read_text()
    (run_archive / "prompt.md").write_bytes(prompt_path.read_bytes())
    run_root = Path(tempfile.mkdtemp(prefix=f"fsi-001-{case_id}-{condition}-"))
    cleanup = {"temporary_root_removed": False, "auth_state_removed": False}
    try:
        workspace, remote = initialize_fixture(case_id, run_root)
        before = git_snapshot(workspace, remote)
        (run_archive / "fixture-before.json").write_text(
            json.dumps(before, indent=2, sort_keys=True) + "\n"
        )
        _, codex_home, env = prepare_isolated_state(run_root, condition)

        diagnostic_dir = run_archive / "capability-diagnostic"
        diagnostic_dir.mkdir()
        diagnostic_output = diagnostic_dir / "response.json"
        diagnostic_events = diagnostic_dir / "events.jsonl"
        diagnostic_stderr = diagnostic_dir / "stderr.txt"
        diagnostic_started_epoch = time.time()
        diagnostic_result, diagnostic_elapsed = invoke_codex(
            workspace=workspace,
            env=env,
            prompt=DIAGNOSTIC_PROMPT,
            output=diagnostic_output,
            events=diagnostic_events,
            stderr=diagnostic_stderr,
            schema=ARCHIVE / "frozen-inputs" / "diagnostic-schema.json",
            timeout=300,
        )
        diagnostic_trace = diagnostic_dir / "session.jsonl.gz"
        diagnostic_trace_found = archive_session_trace(
            codex_home, diagnostic_started_epoch, diagnostic_trace
        )
        valid, diagnostic_record = diagnostic_is_valid(
            condition, diagnostic_output
        )
        diagnostic_record.update(
            {
                "exit_status": diagnostic_result.returncode,
                "elapsed_seconds": round(diagnostic_elapsed, 3),
                "trace_archived": diagnostic_trace_found,
            }
        )
        (diagnostic_dir / "result.json").write_text(
            json.dumps(diagnostic_record, indent=2, sort_keys=True) + "\n"
        )
        if diagnostic_result.returncode != 0 or not valid:
            (run_archive / "metadata.json").write_text(
                json.dumps(
                    {
                        "case_id": case_id,
                        "condition": condition,
                        "arm_launched": False,
                        "reason": "invalid capability diagnostic",
                    },
                    indent=2,
                    sort_keys=True,
                )
                + "\n"
            )
            raise RuntimeError(
                f"invalid diagnostic for {case_id}/{condition}: "
                f"{diagnostic_record}"
            )

        raw_response = run_archive / "raw-final-response.md"
        events = run_archive / "events.jsonl"
        stderr = run_archive / "stderr.txt"
        arm_started_epoch = time.time()
        result, elapsed = invoke_codex(
            workspace=workspace,
            env=env,
            prompt=prompt,
            output=raw_response,
            events=events,
            stderr=stderr,
            timeout=900,
        )
        retry_record: list[dict[str, Any]] = []
        if result.returncode != 0 and (
            not raw_response.exists() or not raw_response.read_text().strip()
        ):
            first_events = run_archive / "transport-attempt-01-events.jsonl"
            first_stderr = run_archive / "transport-attempt-01-stderr.txt"
            events.replace(first_events)
            stderr.replace(first_stderr)
            retry_record.append(
                {
                    "attempt": 1,
                    "exit_status": result.returncode,
                    "model_result_present": False,
                }
            )
            arm_started_epoch = time.time()
            result, elapsed_retry = invoke_codex(
                workspace=workspace,
                env=env,
                prompt=prompt,
                output=raw_response,
                events=events,
                stderr=stderr,
                timeout=900,
            )
            elapsed += elapsed_retry
            retry_record.append(
                {
                    "attempt": 2,
                    "exit_status": result.returncode,
                    "model_result_present": raw_response.exists()
                    and bool(raw_response.read_text().strip()),
                }
            )
        trace_found = archive_session_trace(
            codex_home,
            arm_started_epoch,
            run_archive / "session.jsonl.gz",
        )
        after = git_snapshot(workspace, remote)
        (run_archive / "fixture-after.json").write_text(
            json.dumps(after, indent=2, sort_keys=True) + "\n"
        )
        (run_archive / "event-sequence.md").write_text(
            readable_event_sequence(events)
        )
        metrics = extract_run_metrics(events, elapsed)
        (run_archive / "metrics.json").write_text(
            json.dumps(metrics, indent=2, sort_keys=True) + "\n"
        )
        metadata = {
            "case_id": case_id,
            "condition": condition,
            "prompt_sha256": sha256_file(prompt_path),
            "fixture_before_tree": before["tree_hashes"],
            "repository_protocol_commit": git(REPO, "rev-parse", "HEAD"),
            "model": MODEL,
            "reasoning_effort": REASONING_EFFORT,
            "sandbox": "workspace-write; shell network restricted",
            "approval_policy": "never",
            "exit_status": result.returncode,
            "trace_archived": trace_found,
            "transport_attempts": retry_record
            or [
                {
                    "attempt": 1,
                    "exit_status": result.returncode,
                    "model_result_present": raw_response.exists()
                    and bool(raw_response.read_text().strip()),
                }
            ],
        }
        (run_archive / "metadata.json").write_text(
            json.dumps(metadata, indent=2, sort_keys=True) + "\n"
        )
        return f"{case_id}/{condition}: exit {result.returncode}"
    finally:
        shutil.rmtree(run_root, ignore_errors=True)
        cleanup["temporary_root_removed"] = not run_root.exists()
        cleanup["auth_state_removed"] = not (run_root / "codex-home" / "auth.json").exists()
        (run_archive / "cleanup.json").write_text(
            json.dumps(cleanup, indent=2, sort_keys=True) + "\n"
        )


def build_evaluator_workspace(destination: Path) -> None:
    destination.mkdir(parents=True)
    shutil.copy2(
        ARCHIVE / "frozen-inputs" / "contract-a.md",
        destination / "contract-a.md",
    )
    shutil.copy2(
        ARCHIVE / "frozen-inputs" / "contract-b.md",
        destination / "contract-b.md",
    )
    prompts = destination / "cases"
    prompts.mkdir()
    mapping = json.loads(
        (ARCHIVE / "frozen-inputs" / "evaluator-mapping.json").read_text()
    )["arms"]
    for case_id, labels in mapping.items():
        case_dir = prompts / case_id
        case_dir.mkdir()
        shutil.copy2(
            ARCHIVE / "frozen-inputs" / "prompts" / f"{case_id}.md",
            case_dir / "prompt.md",
        )
        for label, condition in labels.items():
            source = ARCHIVE / "runs" / case_id / condition
            target = case_dir / label
            target.mkdir()
            for name in (
                "raw-final-response.md",
                "session.jsonl.gz",
                "event-sequence.md",
                "fixture-before.json",
                "fixture-after.json",
                "metrics.json",
                "metadata.json",
                "cleanup.json",
            ):
                shutil.copy2(source / name, target / name)


def run_evaluator(evaluator_id: str) -> str:
    output_dir = ARCHIVE / "evaluation" / evaluator_id
    if (output_dir / "evaluation.json").exists():
        raise RuntimeError(f"refusing to rerun frozen {evaluator_id}")
    output_dir.mkdir(parents=True, exist_ok=True)
    run_root = Path(tempfile.mkdtemp(prefix=f"fsi-001-{evaluator_id}-"))
    try:
        workspace = run_root / "workspace"
        build_evaluator_workspace(workspace)
        _, codex_home, env = prepare_isolated_state(run_root, None)
        diagnostic_dir = output_dir / "capability-diagnostic"
        diagnostic_dir.mkdir()
        diag_output = diagnostic_dir / "response.json"
        diag_events = diagnostic_dir / "events.jsonl"
        diag_stderr = diagnostic_dir / "stderr.txt"
        diag_started = time.time()
        diag_result, diag_elapsed = invoke_codex(
            workspace=workspace,
            env=env,
            prompt=DIAGNOSTIC_PROMPT,
            output=diag_output,
            events=diag_events,
            stderr=diag_stderr,
            schema=ARCHIVE / "frozen-inputs" / "diagnostic-schema.json",
            timeout=300,
        )
        diag_trace = archive_session_trace(
            codex_home,
            diag_started,
            diagnostic_dir / "session.jsonl.gz",
        )
        diag_json = json.loads(diag_output.read_text())
        user_skills = diag_json.get("user_skills", [])
        diagnostic_record = {
            "exit_status": diag_result.returncode,
            "elapsed_seconds": round(diag_elapsed, 3),
            "user_skills": user_skills,
            "valid_no_user_skills": user_skills == [],
            "trace_archived": diag_trace,
        }
        (diagnostic_dir / "result.json").write_text(
            json.dumps(diagnostic_record, indent=2, sort_keys=True) + "\n"
        )
        if diag_result.returncode != 0 or user_skills:
            raise RuntimeError(f"invalid evaluator diagnostic: {diagnostic_record}")
        instructions = (
            ARCHIVE / "frozen-inputs" / "evaluator-instructions.md"
        ).read_text()
        prompt = (
            instructions
            + f"\n\nYour evaluator ID is `{evaluator_id}`. "
            "The evidence root is the current workspace.\n"
        )
        started = time.time()
        result, elapsed = invoke_codex(
            workspace=workspace,
            env=env,
            prompt=prompt,
            output=output_dir / "evaluation.json",
            events=output_dir / "events.jsonl",
            stderr=output_dir / "stderr.txt",
            schema=ARCHIVE / "frozen-inputs" / "evaluator-schema.json",
            timeout=1800,
        )
        trace = archive_session_trace(
            codex_home, started, output_dir / "session.jsonl.gz"
        )
        (output_dir / "metadata.json").write_text(
            json.dumps(
                {
                    "evaluator_id": evaluator_id,
                    "model": MODEL,
                    "reasoning_effort": REASONING_EFFORT,
                    "exit_status": result.returncode,
                    "elapsed_seconds": round(elapsed, 3),
                    "trace_archived": trace,
                    "identities_available": False,
                },
                indent=2,
                sort_keys=True,
            )
            + "\n"
        )
        return f"{evaluator_id}: exit {result.returncode}"
    finally:
        shutil.rmtree(run_root, ignore_errors=True)
        (output_dir / "cleanup.json").write_text(
            json.dumps(
                {
                    "temporary_root_removed": not run_root.exists(),
                    "auth_state_removed": not (
                        run_root / "codex-home" / "auth.json"
                    ).exists(),
                },
                indent=2,
                sort_keys=True,
            )
            + "\n"
        )


def all_case_ids() -> list[str]:
    return [
        path.stem
        for path in sorted(
            (ARCHIVE / "frozen-inputs" / "prompts").glob("*.md")
        )
    ]


def main() -> None:
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command", required=True)
    subparsers.add_parser("freeze-inputs")
    run_parser = subparsers.add_parser("run")
    run_parser.add_argument("--case", required=True, choices=all_case_ids())
    run_parser.add_argument("--condition", required=True, choices=CONDITIONS)
    all_parser = subparsers.add_parser("run-all")
    all_parser.add_argument("--jobs", type=int, default=3)
    evaluator_parser = subparsers.add_parser("run-evaluator")
    evaluator_parser.add_argument(
        "--id", required=True, choices=("evaluator-1", "evaluator-2")
    )
    args = parser.parse_args()
    if args.command == "freeze-inputs":
        freeze_inputs()
    elif args.command == "run":
        print(run_one(args.case, args.condition))
    elif args.command == "run-all":
        tasks = [
            (case_id, condition)
            for case_id in all_case_ids()
            for condition in CONDITIONS
        ]
        with concurrent.futures.ThreadPoolExecutor(
            max_workers=args.jobs
        ) as executor:
            futures = {
                executor.submit(run_one, case_id, condition): (
                    case_id,
                    condition,
                )
                for case_id, condition in tasks
            }
            for future in concurrent.futures.as_completed(futures):
                print(future.result(), flush=True)
    elif args.command == "run-evaluator":
        print(run_evaluator(args.id))


if __name__ == "__main__":
    main()
