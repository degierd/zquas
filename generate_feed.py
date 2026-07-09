#!/usr/bin/env python3
"""Generate RSS 2.0 and Atom feeds from articles.html.

Run after editing the articles index. Output:
  - feed.xml (RSS 2.0)
  - atom.xml (Atom 1.0)

The script parses the articles list, extracts publication month/year from
the .article-meta line, and emits a feed sorted newest-first.
"""

from __future__ import annotations

import re
from datetime import datetime, timezone, date
from html import escape
from pathlib import Path

ROOT = Path(__file__).parent
ARTICLES_HTML = ROOT / "articles.html"
SITE = "https://zquas.ai"

MONTHS = {
    "january": 1, "february": 2, "march": 3, "april": 4,
    "may": 5, "june": 6, "july": 7, "august": 8,
    "september": 9, "october": 10, "november": 11, "december": 12,
}

# Fallback pubDate for an entry whose .article-meta carries no month and year.
# This used to be date.today(), which re-stamped undated entries on every
# rebuild. Feed readers sort by pubDate, not document order, so those entries
# resurfaced as brand new to every subscriber each time the feeds were built.
# A fixed sentinel older than the archive keeps them stable and at the bottom.
UNDATED_SENTINEL = date(2020, 1, 1)

ARTICLE_RE = re.compile(
    r'<a href="(article-[^"]+\.html|tmnl\.html)"[^>]*class="article-item[^"]*"[^>]*>'
    r'\s*<div class="article-meta">([^<]+)</div>'
    r'\s*<h2>([^<]+)</h2>'
    r'\s*<p>([\s\S]*?)</p>',
    re.MULTILINE,
)


def parse_articles():
    html = ARTICLES_HTML.read_text(encoding="utf-8")
    items = []
    for m in ARTICLE_RE.finditer(html):
        href, meta_raw, title, desc = m.groups()
        meta = re.sub(r"&[a-z]+;", " ", meta_raw)
        month_match = re.search(
            r"(january|february|march|april|may|june|july|"
            r"august|september|october|november|december)\s+(\d{4})",
            meta,
            re.IGNORECASE,
        )
        if month_match:
            mname = month_match.group(1).lower()
            year = int(month_match.group(2))
            pub_date = date(year, MONTHS[mname], 15)
        else:
            pub_date = None
        items.append({
            "url": f"{SITE}/{href}",
            "title": _clean(title),
            "description": _clean(desc),
            "pub_date": pub_date,
        })
    # Sort: dated entries first (newest first), then undated at the bottom.
    dated = sorted(
        (x for x in items if x["pub_date"] is not None),
        key=lambda x: x["pub_date"],
        reverse=True,
    )
    undated = [x for x in items if x["pub_date"] is None]
    return dated + undated


def _clean(s: str) -> str:
    s = re.sub(r"&euro;", "EUR ", s)
    s = re.sub(r"&middot;", "*", s)
    s = re.sub(r"&[a-zA-Z]+;", "", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s


def rfc822(d: date | None) -> str:
    if d is None:
        d = UNDATED_SENTINEL
    dt = datetime(d.year, d.month, d.day, 9, 0, 0, tzinfo=timezone.utc)
    return dt.strftime("%a, %d %b %Y %H:%M:%S +0000")


def iso(d: date | None) -> str:
    if d is None:
        d = UNDATED_SENTINEL
    return f"{d.isoformat()}T09:00:00+00:00"


def build_rss(items):
    last_build = rfc822(date.today())
    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom" xmlns:dc="http://purl.org/dc/elements/1.1/">',
        '<channel>',
        f'<title>{escape("ZQUAS Articles")}</title>',
        f'<link>{SITE}/articles.html</link>',
        f'<atom:link href="{SITE}/feed.xml" rel="self" type="application/rss+xml" />',
        f'<description>{escape("Analysis and perspective on compliance technology, regulatory architecture, and the future of cross-institutional financial crime detection.")}</description>',
        '<language>en-GB</language>',
        f'<lastBuildDate>{last_build}</lastBuildDate>',
        f'<pubDate>{rfc822(items[0]["pub_date"]) if items else last_build}</pubDate>',
        f'<image><url>{SITE}/og-image.png</url><title>ZQUAS</title><link>{SITE}/</link></image>',
        '<copyright>(c) ZQUAS. Bounded Compliance on an Unbounded Platform.</copyright>',
        '<managingEditor>danny@zquas.ai (Danny de Gier)</managingEditor>',
        '<webMaster>danny@zquas.ai (Danny de Gier)</webMaster>',
        '<generator>generate_feed.py</generator>',
        '<docs>https://www.rssboard.org/rss-specification</docs>',
    ]
    for it in items:
        lines.append('<item>')
        lines.append(f'<title>{escape(it["title"])}</title>')
        lines.append(f'<link>{it["url"]}</link>')
        lines.append(f'<guid isPermaLink="true">{it["url"]}</guid>')
        lines.append(f'<description>{escape(it["description"])}</description>')
        lines.append(f'<pubDate>{rfc822(it["pub_date"])}</pubDate>')
        lines.append('<dc:creator>Danny de Gier</dc:creator>')
        lines.append('</item>')
    lines.append('</channel>')
    lines.append('</rss>')
    return "\n".join(lines) + "\n"


def build_atom(items):
    updated = iso(items[0]["pub_date"] if items else date.today())
    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<feed xmlns="http://www.w3.org/2005/Atom" xml:lang="en-GB">',
        f'<title>ZQUAS Articles</title>',
        f'<subtitle>Analysis and perspective on compliance technology, regulatory architecture, and the future of cross-institutional financial crime detection.</subtitle>',
        f'<link href="{SITE}/atom.xml" rel="self" type="application/atom+xml" />',
        f'<link href="{SITE}/articles.html" rel="alternate" type="text/html" />',
        f'<id>{SITE}/atom.xml</id>',
        f'<updated>{updated}</updated>',
        '<author><name>Danny de Gier</name><email>danny@zquas.ai</email><uri>https://www.linkedin.com/in/danny-de-gier-prof-pgdip-fcc/</uri></author>',
        '<rights>(c) ZQUAS</rights>',
        '<generator uri="https://zquas.ai/">generate_feed.py</generator>',
    ]
    for it in items:
        lines.append('<entry>')
        lines.append(f'<title>{escape(it["title"])}</title>')
        lines.append(f'<link href="{it["url"]}" rel="alternate" type="text/html" />')
        lines.append(f'<id>{it["url"]}</id>')
        lines.append(f'<published>{iso(it["pub_date"])}</published>')
        lines.append(f'<updated>{iso(it["pub_date"])}</updated>')
        lines.append(f'<summary type="text">{escape(it["description"])}</summary>')
        lines.append('</entry>')
    lines.append('</feed>')
    return "\n".join(lines) + "\n"


def main():
    items = parse_articles()
    if not items:
        raise SystemExit("No articles parsed from articles.html")
    undated = [i for i in items if i["pub_date"] is None]
    if undated:
        print(
            f"warning: {len(undated)} entry(s) have no month and year in their "
            f".article-meta line. Falling back to {UNDATED_SENTINEL.isoformat()} "
            f"so the feed stays stable. Add a date to sort them properly:"
        )
        for u in undated:
            print(f"  - {u['url']}")
    rss = build_rss(items)
    atom = build_atom(items)
    (ROOT / "feed.xml").write_text(rss, encoding="utf-8")
    (ROOT / "atom.xml").write_text(atom, encoding="utf-8")
    print(f"Wrote feed.xml and atom.xml ({len(items)} entries)")


if __name__ == "__main__":
    main()
