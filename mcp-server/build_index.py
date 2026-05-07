#!/usr/bin/env python3
"""Build the search index that the MCP server queries.

Reads every .md file in the website root, splits each document into
sections (by markdown heading), tokenises the text, and writes a
compact JSON index to mcp-server/src/index.json. The Worker imports
this file at deploy time.

The index is keyword-based, not embeddings-based: deterministic,
free at query time, and good enough for the kind of question a
compliance officer asks an MCP-connected model.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).parent.parent
OUT = Path(__file__).parent / "src" / "index.json"
SITE = "https://zquas.ai"

# Tokens we never want to match on. These add noise to the index.
STOP_WORDS = frozenset("""
a about above after again against all am an and any are aren as at be because been before being below between
both but by could did didn do does doing don down during each few for from further had has have having he her
here hers herself him himself his how i if in into is isn it its itself just me more most my myself no nor not
now of off on once only or other our ours ourselves out over own same she should shouldn so some such t than
that the their theirs them themselves then there these they this those through to too under until up very was
wasn we were weren what when where which while who whom why will with would you your yours yourself yourselves
""".split())

# Files to skip even if they have a .md twin. These add noise more than value.
SKIP = {"404.md", "demo.md"}


def tokenise(text: str) -> list[str]:
    """Lowercase alphanumeric tokens, length >= 2, no stopwords."""
    tokens = re.findall(r"[a-zA-Z][a-zA-Z0-9-]+", text.lower())
    return [t for t in tokens if len(t) >= 2 and t not in STOP_WORDS]


def split_sections(md: str) -> list[dict]:
    """Split a markdown doc into sections by heading. Each section
    becomes its own indexed unit so search results can return
    pinpoint excerpts rather than entire 30-min articles."""
    lines = md.splitlines()
    sections: list[dict] = []
    current = {"heading": None, "level": 0, "lines": []}

    def flush():
        if current["lines"] or current["heading"]:
            text = "\n".join(current["lines"]).strip()
            if text or current["heading"]:
                sections.append({
                    "heading": current["heading"] or "",
                    "level": current["level"],
                    "text": text,
                })

    for line in lines:
        m = re.match(r"^(#{1,6})\s+(.+?)\s*$", line)
        if m:
            flush()
            current = {
                "heading": m.group(2).strip(),
                "level": len(m.group(1)),
                "lines": [],
            }
        else:
            current["lines"].append(line)
    flush()
    return sections


def slugify(s: str) -> str:
    s = re.sub(r"[^a-zA-Z0-9-]+", "-", s.lower()).strip("-")
    return s[:80]


def title_of(md: str) -> str:
    m = re.search(r"^# (.+)$", md, re.MULTILINE)
    return m.group(1).strip() if m else ""


def description_of(md: str) -> str:
    m = re.search(r"^>\s*(.+)$", md, re.MULTILINE)
    return m.group(1).strip() if m else ""


def kind_of(filename: str) -> str:
    if filename.startswith("article-") or filename == "tmnl.md":
        return "article"
    if filename in {"glossary.md", "llms.md", "facts.md"}:
        return "reference"
    return "page"


def build():
    docs: list[dict] = []
    for md_path in sorted(ROOT.glob("*.md")):
        if md_path.name in SKIP:
            continue
        # Only website .md files (skip docs added by us in the repo
        # like seo-and-distribution-playbook.md)
        html_twin = md_path.with_suffix(".html")
        if not html_twin.exists():
            continue

        md = md_path.read_text(encoding="utf-8")
        slug = md_path.stem
        title = title_of(md)
        description = description_of(md)
        sections = split_sections(md)

        for i, section in enumerate(sections):
            heading = section["heading"]
            text = section["text"]
            if not text and not heading:
                continue
            section_id = f"{slug}#{slugify(heading)}" if heading else f"{slug}#section-{i}"
            anchor = slugify(heading) if heading else f"section-{i}"
            tokens = tokenise(f"{heading} {text}")
            if not tokens:
                continue

            docs.append({
                "id": section_id,
                "doc": slug,
                "title": title,
                "description": description,
                "kind": kind_of(md_path.name),
                "heading": heading,
                "url": f"{SITE}/{slug}.html" + (f"#{anchor}" if heading else ""),
                "md_url": f"{SITE}/{slug}.md",
                "snippet": _make_snippet(text or heading),
                "tokens": tokens,
            })

    # Build a postings list: token -> list of doc indices.
    postings: dict[str, list[int]] = {}
    for i, d in enumerate(docs):
        seen = set()
        for tok in d["tokens"]:
            if tok in seen:
                continue
            seen.add(tok)
            postings.setdefault(tok, []).append(i)

    # We do not need the full token list per document at runtime, just
    # for ranking. Convert to a frequency map per doc.
    for d in docs:
        freq: dict[str, int] = {}
        for tok in d["tokens"]:
            freq[tok] = freq.get(tok, 0) + 1
        d["term_freq"] = freq
        del d["tokens"]

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps({
        "version": 1,
        "site": SITE,
        "documents": docs,
        "postings": postings,
    }), encoding="utf-8")
    print(f"Wrote {OUT.relative_to(ROOT)}: {len(docs)} sections, {len(postings)} unique terms")


def _make_snippet(text: str, max_len: int = 240) -> str:
    text = re.sub(r"\s+", " ", text).strip()
    if len(text) <= max_len:
        return text
    return text[:max_len].rsplit(" ", 1)[0] + "..."


if __name__ == "__main__":
    build()
