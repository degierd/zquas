#!/usr/bin/env python3
"""Generate Markdown versions of every HTML page for agent consumption.

Output: <slug>.md alongside each .html file. Stripped of nav, footer,
and styling. Preserves headings, paragraphs, lists, tables (as text),
and links.

This complements Cloudflare's Markdown for Agents (Accept: text/markdown
content negotiation) by giving agents a stable, fetchable URL even when
they cannot or do not negotiate.
"""

from __future__ import annotations

import re
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).parent
SITE = "https://zquas.ai"

# HTML pages that should NOT get a Markdown twin
SKIP = {"404.html", "demo.html"}


class Md(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.out: list[str] = []
        self.in_skip = 0          # depth inside <nav>/<footer>/<script>/<style>
        self.in_main = False      # we only collect inside <main>
        self.tag_stack: list[str] = []
        self.list_stack: list[str] = []  # 'ul' or 'ol'
        self.list_counter: list[int] = []
        self.pending_link: str | None = None
        self.in_table_cell = False
        self.last_text_kind: str = ""  # for spacing

    def _push_skip_if_needed(self, tag: str) -> bool:
        if tag in {"nav", "footer", "script", "style", "noscript", "svg"}:
            self.in_skip += 1
            return True
        return False

    def _pop_skip_if_needed(self, tag: str) -> bool:
        if tag in {"nav", "footer", "script", "style", "noscript", "svg"}:
            self.in_skip = max(0, self.in_skip - 1)
            return True
        return False

    def handle_starttag(self, tag, attrs) -> None:
        attrs_d = dict(attrs)
        if tag == "main":
            self.in_main = True
            return
        if self._push_skip_if_needed(tag):
            return
        if not self.in_main or self.in_skip:
            return

        self.tag_stack.append(tag)
        if tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
            level = int(tag[1])
            self._newline_block()
            self.out.append("#" * level + " ")
        elif tag == "p":
            self._newline_block()
        elif tag == "br":
            self.out.append("\n")
        elif tag == "hr":
            self._newline_block()
            self.out.append("---\n\n")
        elif tag == "ul":
            self.list_stack.append("ul")
            self.list_counter.append(0)
            self._newline_block()
        elif tag == "ol":
            self.list_stack.append("ol")
            self.list_counter.append(0)
            self._newline_block()
        elif tag == "li":
            depth = max(0, len(self.list_stack) - 1)
            indent = "  " * depth
            if self.list_stack and self.list_stack[-1] == "ol":
                self.list_counter[-1] += 1
                self.out.append(f"\n{indent}{self.list_counter[-1]}. ")
            else:
                self.out.append(f"\n{indent}- ")
        elif tag in ("strong", "b"):
            self.out.append("**")
        elif tag in ("em", "i"):
            self.out.append("*")
        elif tag == "code":
            self.out.append("`")
        elif tag == "pre":
            self._newline_block()
            self.out.append("```\n")
        elif tag == "blockquote":
            self._newline_block()
            self.out.append("> ")
        elif tag == "a":
            href = attrs_d.get("href", "")
            if href:
                self.pending_link = href
                self.out.append("[")
            else:
                self.pending_link = None
        elif tag == "table":
            self._newline_block()
        elif tag == "tr":
            self.out.append("\n| ")
        elif tag in ("td", "th"):
            self.in_table_cell = True
        elif tag == "img":
            alt = attrs_d.get("alt", "")
            src = attrs_d.get("src", "")
            if src:
                self.out.append(f"![{alt}]({src}) ")

    def handle_endtag(self, tag) -> None:
        if tag == "main":
            self.in_main = False
            return
        if self._pop_skip_if_needed(tag):
            return
        if not self.in_main or self.in_skip:
            return
        if self.tag_stack and self.tag_stack[-1] == tag:
            self.tag_stack.pop()

        if tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
            self.out.append("\n\n")
        elif tag == "p":
            self.out.append("\n\n")
        elif tag in ("ul", "ol"):
            if self.list_stack and self.list_stack[-1] == tag:
                self.list_stack.pop()
                self.list_counter.pop()
            self.out.append("\n\n")
        elif tag == "li":
            pass
        elif tag in ("strong", "b"):
            self.out.append("**")
        elif tag in ("em", "i"):
            self.out.append("*")
        elif tag == "code":
            self.out.append("`")
        elif tag == "pre":
            self.out.append("\n```\n\n")
        elif tag == "blockquote":
            self.out.append("\n\n")
        elif tag == "a":
            if self.pending_link is not None:
                self.out.append(f"]({self.pending_link})")
                self.pending_link = None
        elif tag == "table":
            self.out.append("\n\n")
        elif tag == "tr":
            self.out.append(" |")
        elif tag in ("td", "th"):
            self.in_table_cell = False
            self.out.append(" | ")

    def handle_data(self, data) -> None:
        if not self.in_main or self.in_skip:
            return
        if not data.strip() and not self.out:
            return
        self.out.append(data)

    def _newline_block(self) -> None:
        if self.out and not self.out[-1].endswith("\n\n"):
            if self.out[-1].endswith("\n"):
                self.out.append("\n")
            else:
                self.out.append("\n\n")

    def render(self) -> str:
        text = "".join(self.out)
        # Tighten triple+ newlines to a max of two
        text = re.sub(r"\n{3,}", "\n\n", text)
        # Strip trailing pipe-table cruft on lines that became empty
        text = re.sub(r"\|\s*\|\s*$", "", text, flags=re.MULTILINE)
        # Strip leading whitespace on otherwise-blank lines
        text = re.sub(r"^[ \t]+$", "", text, flags=re.MULTILINE)
        return text.strip() + "\n"


def title_of(html: str) -> str:
    m = re.search(r"<title>([^<]+)</title>", html)
    if m:
        return re.sub(r"\s+[—–-]\s*ZQUAS.*$", "", m.group(1)).strip()
    return ""


def description_of(html: str) -> str:
    m = re.search(r'<meta name="description" content="([^"]+)"', html)
    return m.group(1) if m else ""


def canonical_of(html: str, fallback: str) -> str:
    m = re.search(r'<link rel="canonical" href="([^"]+)"', html)
    return m.group(1) if m else fallback


def convert(path: Path) -> str:
    html = path.read_text(encoding="utf-8")
    title = title_of(html)
    desc = description_of(html)
    canonical = canonical_of(html, f"{SITE}/{path.name}")

    parser = Md()
    parser.feed(html)
    body = parser.render()

    head = []
    if title:
        head.append(f"# {title}")
        head.append("")
    if desc:
        head.append(f"> {desc}")
        head.append("")
    head.append(f"Source: {canonical}")
    head.append(f"Site: {SITE}")
    head.append("")
    head.append("---")
    head.append("")
    return "\n".join(head) + body


def main() -> None:
    written = 0
    for html_path in sorted(ROOT.glob("*.html")):
        if html_path.name in SKIP:
            continue
        md_path = html_path.with_suffix(".md")
        md_path.write_text(convert(html_path), encoding="utf-8")
        written += 1
    print(f"Wrote {written} Markdown files")


if __name__ == "__main__":
    main()
