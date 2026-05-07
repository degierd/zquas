#!/usr/bin/env python3
"""Generate /.well-known/agent-skills/index.json from the resources we publish.

Run after any change to the listed files. The skills index is a
machine-readable inventory of what an AI agent can usefully fetch from
zquas.ai. Each entry has a sha256 digest so an agent can verify it
fetched the same artefact the index pointed at.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).parent
SITE = "https://zquas.ai"
OUT = ROOT / ".well-known" / "agent-skills" / "index.json"

SKILLS = [
    {
        "name": "site-summary",
        "type": "knowledge",
        "description": (
            "LLM-optimised summary of ZQUAS: what it is, who it serves, "
            "the engine's published benchmark numbers, and the regulatory "
            "frameworks it covers."
        ),
        "path": "llms.txt",
        "media_type": "text/plain",
    },
    {
        "name": "site-summary-full",
        "type": "knowledge",
        "description": (
            "Long-form companion to llms.txt with the verbatim content of "
            "the strongest pages on the site (homepage, technology, "
            "regulators, founder timeline)."
        ),
        "path": "llms-full.txt",
        "media_type": "text/plain",
    },
    {
        "name": "facts",
        "type": "knowledge",
        "description": (
            "Machine-readable fact sheet: benchmark numbers, federation "
            "protocols, regulatory engagement, founder profile, "
            "competitor positioning, locked thresholds."
        ),
        "path": "facts.json",
        "media_type": "application/json",
    },
    {
        "name": "glossary",
        "type": "knowledge",
        "description": (
            "Definitions for the cryptographic, regulatory, and "
            "architectural terms used across ZQUAS: AMLR Article 75, "
            "MPC, ECDH-PSI, Garbled Circuits, GPU-native, cryptographic "
            "proof bundle, deterministic evaluation, and more."
        ),
        "path": "glossary.html",
        "media_type": "text/html",
    },
    {
        "name": "position-paper-article-75",
        "type": "knowledge",
        "description": (
            "Position paper on AMLR Article 75: how Multi-Party "
            "Computation enables full customer base federation for AML "
            "detection without sharing personal data. Legal argument, "
            "evidence, and a path to a pilot."
        ),
        "path": "article-75.html",
        "media_type": "text/html",
    },
    {
        "name": "position-paper-edge-to-federation",
        "type": "knowledge",
        "description": (
            "Position paper on a unified architecture for real-time "
            "financial crime detection across institutional, "
            "cross-bank, and regulatory layers."
        ),
        "path": "article-edge-to-federation.html",
        "media_type": "text/html",
    },
    {
        "name": "position-paper-beyond-banking",
        "type": "knowledge",
        "description": (
            "Position paper on cross-sector federated detection across "
            "banks, telecommunications operators, and digital asset "
            "platforms."
        ),
        "path": "article-beyond-banking.html",
        "media_type": "text/html",
    },
    {
        "name": "one-pager",
        "type": "knowledge",
        "description": (
            "Single-page PDF summary of the engine, benchmarks, and "
            "regulatory traction. Suitable for buyer hand-out."
        ),
        "path": "zquas-onepager.pdf",
        "media_type": "application/pdf",
    },
    {
        "name": "articles-feed",
        "type": "knowledge",
        "description": (
            "RSS 2.0 feed of all ZQUAS analysis articles, sorted "
            "newest-first. Updated whenever a new article is published."
        ),
        "path": "feed.xml",
        "media_type": "application/rss+xml",
    },
]


def sha256(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def build():
    skills = []
    for entry in SKILLS:
        path = ROOT / entry["path"]
        if not path.exists():
            print(f"warn: missing {entry['path']}, skipping")
            continue
        skills.append({
            "name": entry["name"],
            "type": entry["type"],
            "description": entry["description"],
            "url": f"{SITE}/{entry['path']}",
            "media_type": entry["media_type"],
            "sha256": sha256(path),
        })

    doc = {
        "$schema": "https://agentskills.io/schemas/index/v0.2.0.json",
        "version": "0.2.0",
        "publisher": {
            "name": "ZQUAS",
            "url": SITE,
            "contact": "danny@zquas.ai",
        },
        "skills": skills,
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(doc, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {OUT.relative_to(ROOT)} ({len(skills)} skills)")


if __name__ == "__main__":
    build()
