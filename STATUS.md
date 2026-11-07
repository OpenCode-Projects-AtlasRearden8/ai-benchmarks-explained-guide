# STATUS — AI Benchmarks Explained

A plain-English educational manual for reading AI model rankings — what
benchmarks actually measure, why bigger numbers mislead, how to decode
MMLU-style names, how to read hallucination/safety scores honestly, how to
sanity-test a model yourself in ten minutes, and how to choose between cloud
and Ollama-friendly local models without math anxiety.

Education only. It never endorses hype, never tells you which model to buy,
and is never medical/legal/financial advice. All example models and numbers
("Checkers-7B", "Widget-9B", etc.) are fictional teaching aids.

Maintained by **Asdale Dynamics, LLC** (Dylan Asdale, *The Massive AI
Manual*, dylanasdale.github.io). MIT licensed — `LICENSE` begins with
`Copyright (c) 2026 Asdale Dynamics, LLC`, and the README credits the LLC.

## What was built

### `docs/` — the manual (markdown, 9 files, ~6,900 words)

- `00-start-here.md` — how to use the guide, the one core idea, what it won't do
- `01-what-benchmarks-measure.md` — benchmark anatomy; scores as proxies; relative vs. absolute meaning
- `02-why-bigger-numbers-mislead.md` — the five honest failure modes: contamination, ceiling clumping, run-procedure variance, averages hiding slices, cherry-picked emphasis; plus a scoring-hygiene checklist
- `03-benchmark-names-decoded.md` — the three-move acronym decoder; ~20 famous benchmarks (MMLU, GPQA, HellaSwag, GSM8K, TruthfulQA, BBQ, SWE-bench, LiveCodeBench, IFEval, Arena, etc.) decoded; suffix mini-dictionary
- `04-hallucination-and-safety-scores.md` — what hallucination is, how truth benchmarks count, misinformation-resistant reading rules; safety/refusal rates incl. the over-refusal caveat; a healthcare-worker note (education only)
- `05-ten-minute-sanity-test.md` — seven concrete exercises with exact prompts, expected answers, a 0–14 rubric, and a worked scorecard
- `06-cloud-vs-local.md` — privacy/hardware/tasks/availability decision flow; RAM rules of thumb; "Ollama-friendly" defined; two worked personas
- `07-cheat-sheet.md` — one-page recap of everything
- `glossary.md` — soft glossary, one-line plain-English definitions

### `site/` — static site (dependency-free HTML/CSS/JS, no build step)

- `index.html` — overview + the "five questions to ask any big score"
- `examples.html` — worked examples: a fictional leaderboard you flip to reveal hidden per-category slices; an interactive 0–14 sanity-test scorecard with verdicts; name-decoding practice; cloud-vs-local flow
- `glossary.html` — live-searchable soft glossary (30 terms, anchor-linked)
- `styles.css`, `app.js` — single stylesheet/script; no trackers, no external fonts, no network calls

### `tests/run_tests.py` — self-tests (stdlib only)

## How to run it

```sh
# Read the manual
#   open docs/00-start-here.md and go chapter by chapter

# Browse the site (no build step; fully local)
python3 -m http.server 8000 --directory site
#   → http://localhost:8000   (or just double-click site/index.html)

# Run the self-tests
python3 tests/run_tests.py
```

## Verification results (actual, from this workspace)

- `python3 tests/run_tests.py` — **PASS, 123 checks, 0 failures**.
  Verifies: project structure, exact LICENSE copyright line, README
  credit, no secrets pattern-matched across all files, every internal
  markdown/HTML link resolves, all site pages parse with balanced
  structure, all 30 glossary entries defined, glossary anchor targets
  exist, interactivity hooks wired, no external asset links.
- Server smoke test — `python3 -m http.server 8321 --directory site`; all
  five site files returned HTTP 200; index served content as expected.
- `node --check site/app.js` — JS parses cleanly.
- One test failure was found and fixed during development (a required
  phrase was split across HTML lines); suite then fully green.

## Known gaps

- Benchmark examples use classic, stable benchmark names; specific score
  values are illustrative by design (this guide deliberately tracks *how
  to read*, not what's current). SOTA claims expire — the guide teaches
  skepticism toward them rather than listing them.
- The "sanity-test scoring helper" only adds integers — deliberately; the
  guide's premise is minimal math.
- No automated browser test of the site's JavaScript at runtime (syntax
  checked via `node --check`, hooks verified statically). A future
  Playwright-style check would tighten this.
- Real benchmark-per-model data tables (e.g., importing live leaderboard
  data) are intentionally out of scope to avoid stale numbers and vendor
  endorsement.
- No RSS/newsletters/social anything; this is a local-first folder, not a
  publishing pipeline.
