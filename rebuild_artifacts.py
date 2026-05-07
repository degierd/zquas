#!/usr/bin/env python3
"""Rebuild all derived artefacts after a content change.

Run this whenever you edit articles, the homepage, or any page that
appears in the feeds, the agent skills index, or the markdown twins.

Outputs:
  - feed.xml, atom.xml             (via generate_feed.py)
  - .well-known/agent-skills/index.json (via generate_agent_skills.py)
  - <page>.md for every HTML page  (via generate_markdown.py)
  - zquas-onepager.pdf             (via generate_onepager.py)

Usage:
  python rebuild_artifacts.py
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).parent
SCRIPTS = [
    "generate_feed.py",
    "generate_markdown.py",
    "generate_agent_skills.py",
    "generate_onepager.py",
]


def run(script: str) -> bool:
    print(f"--- {script} ---")
    result = subprocess.run(
        [sys.executable, script],
        cwd=ROOT,
    )
    return result.returncode == 0


def main() -> None:
    failures = []
    for s in SCRIPTS:
        if not (ROOT / s).exists():
            print(f"skip: {s} not found")
            continue
        if not run(s):
            failures.append(s)
    if failures:
        print(f"\nFAILED: {', '.join(failures)}")
        sys.exit(1)
    print("\nAll artefacts rebuilt.")


if __name__ == "__main__":
    main()
