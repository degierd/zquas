#!/usr/bin/env python3
"""Ping IndexNow with the URLs that changed in the most recent commit.

Bing, Yandex, Naver, Seznam, and Yep accept IndexNow submissions. Google
does not (use Search Console for Google).

Run after pushing to production. Requires only the standard library.
"""

from __future__ import annotations

import json
import subprocess
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).parent
HOST = "zquas.ai"
KEY = "16593f2e833f7ba12ad896062da4fbb8"
KEY_LOCATION = f"https://{HOST}/{KEY}.txt"
ENDPOINT = "https://api.indexnow.org/IndexNow"


def changed_urls() -> list[str]:
    """Return canonical URLs for HTML files changed in the last commit."""
    out = subprocess.check_output(
        ["git", "diff", "--name-only", "HEAD~1", "HEAD"],
        cwd=ROOT,
        text=True,
    )
    urls: list[str] = []
    for line in out.splitlines():
        line = line.strip()
        if not line:
            continue
        if line == "index.html":
            urls.append(f"https://{HOST}/")
        elif line.endswith(".html") and "/" not in line:
            urls.append(f"https://{HOST}/{line}")
        elif line in {"sitemap.xml", "feed.xml", "atom.xml", "llms.txt", "facts.json"}:
            urls.append(f"https://{HOST}/{line}")
    return urls


def submit(urls: list[str]) -> None:
    if not urls:
        print("No URLs changed in last commit. Nothing to submit.")
        return
    payload = {
        "host": HOST,
        "key": KEY,
        "keyLocation": KEY_LOCATION,
        "urlList": urls,
    }
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        ENDPOINT,
        data=data,
        headers={"Content-Type": "application/json; charset=utf-8"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            print(f"IndexNow: HTTP {resp.status} for {len(urls)} URLs")
            for u in urls:
                print(f"  - {u}")
    except urllib.error.HTTPError as e:
        print(f"IndexNow: HTTP {e.code} -- {e.reason}")
        sys.exit(1)


def main() -> None:
    urls = changed_urls()
    submit(urls)


if __name__ == "__main__":
    main()
