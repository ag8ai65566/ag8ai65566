#!/usr/bin/env python3
"""Run the GPT queue (.gpt-quota.json "pending") unattended, one command at a time, across quota resets.

    setsid nohup python3 novel-lab/tools/gpt_autorun.py >> <log> 2>&1 &

- Waits while another `lab.py gpt` process is running (never two GPT runs at once).
- Runs the first pending command; lab.py removes it from the list on success and records the reset time on a
  quota stop (exit 75). On a quota stop it sleeps until the reset (plus two minutes) and continues.
- After each successful run it commits the run directory (and any packet files the QA prepare step rebuilt)
  and pushes to the current branch. A failed command is logged and skipped, not retried.
- Stops when the list is empty or only failed commands remain. Merging results is Claude's job, on the
  author's word (author order 2026-10-02).
"""
import datetime as dt
import json
import shlex
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent  # novel-lab/
REPO = ROOT.parent
QUOTA = ROOT / ".gpt-quota.json"
QUOTA_EXIT = 75


def log(msg):
    print(f"[{dt.datetime.now(dt.timezone.utc):%Y-%m-%d %H:%M} UTC] {msg}", flush=True)


def other_gpt_running():
    r = subprocess.run(["pgrep", "-f", "lab.py gpt "], capture_output=True, text=True)
    return bool(r.stdout.strip())


def git(*args, check=False):
    return subprocess.run(["git", *args], cwd=REPO, capture_output=True, text=True, check=check)


def commit_push(label):
    git("add", "-A", "novel-lab/projects")
    if not git("diff", "--cached", "--quiet").returncode:
        return
    msg = (f"holoen: GPT output {label} (unattended queue, merge pending author order)\n\n"
           "Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>\n"
           "Claude-Session: https://claude.ai/code/session_01TBvQi5t1Wnzf7Q3KQhgH2h")
    if git("commit", "-q", "-m", msg).returncode:
        log(f"commit failed for {label}")
        return
    branch = git("rev-parse", "--abbrev-ref", "HEAD").stdout.strip()
    for wait in (0, 2, 4, 8, 16):
        time.sleep(wait)
        if not git("push", "-q", "-u", "origin", branch).returncode:
            log(f"pushed {label}")
            return
    log(f"push failed for {label} (committed locally)")


def main():
    failed = set()
    while True:
        while other_gpt_running():
            time.sleep(60)
        commit_push("from an earlier process")
        if not QUOTA.exists():
            log("queue empty; done")
            return
        data = json.loads(QUOTA.read_text(encoding="utf-8"))
        todo = [c for c in data.get("pending", []) if c not in failed]
        if not todo:
            log(f"nothing left but {len(failed)} failed command(s); done")
            return
        reset = data.get("reset_utc")
        now = dt.datetime.now(dt.timezone.utc)
        if reset and dt.datetime.fromisoformat(reset) > now:
            secs = (dt.datetime.fromisoformat(reset) - now).total_seconds() + 120
            log(f"quota resets {reset}; sleeping {secs / 60:.0f} min")
            time.sleep(secs)
            continue
        cmd = todo[0]
        label = Path(shlex.split(cmd)[4]).name if len(shlex.split(cmd)) > 4 else cmd
        log(f"▶ {label}")
        r = subprocess.run(shlex.split(cmd), cwd=REPO)
        if r.returncode == QUOTA_EXIT:
            after = json.loads(QUOTA.read_text(encoding="utf-8")) if QUOTA.exists() else {}
            if not after.get("reset_utc"):
                log("quota stop without a reset time; sleeping 30 min")
                time.sleep(1800)
            continue
        if r.returncode:
            failed.add(cmd)
            log(f"✗ exit {r.returncode}: {label} (skipped)")
            continue
        log(f"✓ {label}")
        commit_push(label)


if __name__ == "__main__":
    sys.exit(main())
