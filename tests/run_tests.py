#!/usr/bin/env python3
"""Self-tests for the AI Benchmarks Explained guide.

Verifies, with zero dependencies:
  1. the expected project structure exists,
  2. the LICENSE copyright line is exact and README credits the LLC,
  3. every internal markdown/mhtml link inside docs/ and site/ resolves,
  4. all site HTML parses and has the required pages/anchors,
  5. the glossary is complete (every entry has a definition),
  6. no file looks like it contains a secret (keys, tokens).

Run:  python3 tests/run_tests.py
"""

import re
import sys
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
SITE = ROOT / "site"

REQUIRED_FILES = [
    "README.md",
    "LICENSE",
    "STATUS.md",
    "docs/00-start-here.md",
    "docs/01-what-benchmarks-measure.md",
    "docs/02-why-bigger-numbers-mislead.md",
    "docs/03-benchmark-names-decoded.md",
    "docs/04-hallucination-and-safety-scores.md",
    "docs/05-ten-minute-sanity-test.md",
    "docs/06-cloud-vs-local.md",
    "docs/07-cheat-sheet.md",
    "docs/glossary.md",
    "site/index.html",
    "site/examples.html",
    "site/glossary.html",
    "site/styles.css",
    "site/app.js",
]

COPYRIGHT_LINE = "Copyright (c) 2026 Asdale Dynamics, LLC"
REQUIRED_SITE_PAGES = {"index.html": ["AI Benchmarks Explained", "measurement, not a"],
                       "examples.html": ["Worked Examples", "fictional"],
                       "glossary.html": ["Plain-English Glossary", "Ollama"]}

failures = []
passes = []


def check(name, condition, detail=""):
    if condition:
        passes.append(name)
    else:
        failures.append(f"{name}{' — ' + detail if detail else ''}")


def md_link_targets(text):
    """Yield relative link targets from markdown link/image syntax."""
    for m in re.finditer(r"\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)", text):
        yield m.group(1)
    for m in re.finditer(r"<a [^>]*href=\"([^\"]+)\"", text):
        yield m.group(1)


def md_heading(text, level, contains=None):
    pattern = rf"^{'#' * level} " + (r".*" + re.escape(contains) + ".*" if contains else "")
    return re.search(pattern, text, flags=re.MULTILINE) is not None


def strip_anchors(target):
    return target.split("#", 1)[0]


def test_files_exist():
    for rel in REQUIRED_FILES:
        check(f"file exists: {rel}", (ROOT / rel).is_file())


def test_license_exact():
    text = (ROOT / "LICENSE").read_text(encoding="utf-8")
    check("LICENSE is MIT", "MIT License" in text.splitlines()[0]
          or "MIT License" in text)
    lines = text.splitlines()
    copyright_lines = [ln for ln in lines if ln.startswith("Copyright")]
    check("LICENSE copyright line is exact",
          copyright_lines and copyright_lines[0] == COPYRIGHT_LINE,
          detail=copyright_lines[0] if copyright_lines else "none found")


def test_readme_credits():
    text = (ROOT / "README.md").read_text(encoding="utf-8")
    check("README credits Asdale Dynamics, LLC", "Asdale Dynamics, LLC" in text)


def test_no_secrets():
    secret_re = re.compile(
        r"(sk-[A-Za-z0-9]{16,}|ghp_[A-Za-z0-9]{20,}|AKIA[0-9A-Z]{16}"
        r"|(?:api[_-]?key|secret|password|token)\s*[:=]\s*['\"][^'\"]{8,})"
        , re.IGNORECASE)
    offenders = []
    for path in ROOT.rglob("*"):
        if path.is_file() and ".git" not in path.parts:
            try:
                content = path.read_text(encoding="utf-8", errors="ignore")
            except OSError:
                continue
            if secret_re.search(content):
                offenders.append(str(path.relative_to(ROOT)))
    check("no secrets detected", not offenders, detail=", ".join(offenders))


def test_docs_links_and_content():
    for md in sorted(DOCS.glob("*.md")):
        text = md.read_text(encoding="utf-8")
        # Every chapter starts with an H1
        check(f"{md.name} has an H1 title", text.lstrip().startswith("# "))
        # Markdown word-count sanity: a chapter is a manual, not a stub
        words = len(re.findall(r"\S+", text))
        check(f"{md.name} is substantive ({words} words)", words >= 400)
        for target in md_link_targets(text):
            if target.startswith(("http://", "https://")) or target.startswith("mailto:"):
                continue
            resolved = (md.parent / strip_anchors(target)).resolve()
            check(f"{md.name} link resolves: {target}", resolved.is_file())
    # cross-references every chapter wired into the start-here page
    start = (DOCS / "00-start-here.md").read_text(encoding="utf-8")

    for chapter in ["01-what-benchmarks-measure.md", "02-why-bigger-numbers-mislead.md",
                    "03-benchmark-names-decoded.md", "05-ten-minute-sanity-test.md"]:
        check(f"00-start-here links {chapter}", chapter in start)


def test_glossary_covers_html_anchors():
    """Every glossary anchor linked from anywhere must have a real target."""
    link_anchors = set()
    for base in (DOCS, SITE):
        for path in sorted(base.rglob("*")):
            if not path.is_file() or path.suffix not in {".md", ".html"}:
                continue
            text = path.read_text(encoding="utf-8", errors="ignore")
            for m in re.finditer(r"\((glossary\.md#([\w-]+))\)", text):
                link_anchors.add(m.group(2))
    glossary_md = (DOCS / "glossary.md").read_text(encoding="utf-8")
    dt_lines = [ln.strip().lstrip("- ") for ln in glossary_md.splitlines()
                if ln.startswith("- **")]
    dt_terms = [re.sub(r"\*\*", "", ln).split(" — ")[0].split(" (")[0]
                .lower() for ln in dt_lines]
    # Markdown glossary has no explicit anchors now; the HTML one does.
    check("glossary.md has entries", len(dt_terms) >= 20)
    gloss_html = (SITE / "glossary.html").read_text(encoding="utf-8")
    html_anchors = set(re.findall(r'<div id="([\w-]+)"', gloss_html))
    for anchor in link_anchors:
        check(f"glossary anchor target exists: {anchor}", anchor in html_anchors)


class StructureParser(HTMLParser):
    """Crude structural check: track open/close pairing of key container tags."""

    VOID = {"meta", "link", "br", "img", "input", "hr", "source", "wbr"}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []
        self.errors = []
        self.ids = set()

    def handle_starttag(self, tag, attrs):
        if tag in self.VOID:
            return
        self.stack.append(tag)
        for k, v in attrs:
            if k == "id" and v:
                self.ids.add(v)

    def handle_endtag(self, tag):
        if tag in self.VOID:
            return
        if not self.stack:
            self.errors.append(f"</{tag}> with empty stack")
            return
        if self.stack[-1] == tag:
            self.stack.pop()
        else:
            self.errors.append(f"</{tag}> but open is <{self.stack[-1]}>")


def test_site_html_structure_and_targets():
    for name in REQUIRED_SITE_PAGES:
        page = SITE / name
        parser = StructureParser()
        parser.feed(page.read_text(encoding="utf-8"))
        check(f"{name} parses with balanced structure", not parser.errors and not parser.stack,
              detail="; ".join(parser.errors) or f"unclosed {parser.stack[:3]}")
        for must in REQUIRED_SITE_PAGES[name]:
            check(f"{name} contains '{must}'", must in page.read_text(encoding="utf-8"))
        text = page.read_text(encoding="utf-8")
        for m in re.finditer(r'(?:href|src)="([^"]+)"', text):
            url = m.group(1)
            if url.startswith(("http://", "https://", "mailto:", "#")) or url == "":
                continue
            resolved = (SITE / strip_anchors(url)).resolve()
            check(f"{name} asset/link resolves: {url}", resolved.is_file())
        # Asset links never point at CDNs — fully local site
        external_assets = [u for u in re.findall(r'(?:href|src)="([^"]+)"', text)
                           if u.startswith(("http://", "https://"))]
        check(f"{name} has no external asset links", not external_assets,
              detail=", ".join(external_assets))

    entries = re.findall(r'<div id="([\w-]+)">\s*<dt>(.*?)</dt>\s*<dd>(.*?)</dd>',
                         (SITE / "glossary.html").read_text(encoding="utf-8"), flags=re.DOTALL)
    for anchor, term, definition in entries:
        check(f"glossary entry '{anchor}' defined", bool(term.strip()) and len(definition.strip()) > 30)
    check("glossary.html has 20+ entries", len(entries) >= 20)
    check("glossary.html no empty anchor divs",
          not re.search(r'<div id="([\w-]+)">\s*</div>',
                        (SITE / "glossary.html").read_text(encoding="utf-8")))


def test_site_scripts_nonempty():
    for name in ("styles.css", "app.js"):
        body = (SITE / name).read_text(encoding="utf-8")
        check(f"{name} is non-trivial", len(body) >= 1000)
    js = (SITE / "app.js").read_text(encoding="utf-8")
    pages = (SITE / "examples.html").read_text(encoding="utf-8") + \
            (SITE / "glossary.html").read_text(encoding="utf-8")
    for hook in ("glossary-search", "show-slices", "score-total", "score-verdict"):
        check(f"interactivity wired: {hook}", hook in js and hook in pages)


def main():
    test_files_exist()
    test_license_exact()
    test_readme_credits()
    test_no_secrets()
    test_docs_links_and_content()
    test_glossary_covers_html_anchors()
    test_site_html_structure_and_targets()
    test_site_scripts_nonempty()

    print(f"PASS {len(passes)} checks")
    for p in passes:
        print(f"  ok: {p}")
    if failures:
        print(f"\nFAIL {len(failures)} checks")
        for f in failures:
            print(f"  FAIL: {f}")
        return 1
    print("\nAll checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
