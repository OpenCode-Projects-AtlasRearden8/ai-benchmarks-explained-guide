# AI Benchmarks Explained — a plain-English guide to reading AI model rankings

*Explain AI "like a friend would" — plain English, step by step, never condescending.*

Most AI leaderboards look like alphabet soup: MMLU, GPQA, HellaSwag, scores like
`86.3%` and `#1 on Arena`. This guide teaches you what those numbers actually
measure, why **bigger numbers mislead**, and how to sanity-test a model yourself
in ten minutes — no math degree required.

**This is an education project. It is never an endorsement of hype, and it is
never medical, legal, or financial advice.**

## What's inside

| Path | What it is |
| --- | --- |
| `docs/00-start-here.md` | How to use this guide, in one sitting or in pieces |
| `docs/01-what-benchmarks-measure.md` | What a benchmark actually is (and isn't) |
| `docs/02-why-bigger-numbers-mislead.md` | The five big reasons a "better score" can fool you |
| `docs/03-benchmark-names-decoded.md` | MMLU-style names decoded, plain-English glossary of famous benchmarks |
| `docs/04-hallucination-and-safety-scores.md` | Reading truthfulness, hallucination, and safety numbers honestly |
| `docs/05-ten-minute-sanity-test.md` | A hands-on checklist to test any model yourself, today |
| `docs/06-cloud-vs-local.md` | Choosing between cloud models and Ollama-friendly local ones, without math anxiety |
| `docs/07-cheat-sheet.md` | One-page recap: the questions to ask any leaderboard |
| `site/` | A static website version with a live soft-glossary and worked examples |

## Run the website

No build step, no dependencies, no network calls. The site is plain HTML/CSS/JS.

```sh
python3 -m http.server 8000 --directory site
# then open http://localhost:8000
```

(You can just double-click `site/index.html` too — everything is local.)

## Run the self-tests

```sh
python3 tests/run_tests.py
```

The tests verify the docs are complete, internal links resolve, the site's
HTML is well-formed, every glossary term is defined, and the LICENSE line is
exact.

## Who made this

Built and maintained by **Asdale Dynamics, LLC** — the company behind
Registered Nurse turned AI author Dylan Asdale, his book *The Massive AI
Manual*, and the hub site `dylanasdale.github.io`. Part of a family of
beginner-first AI education projects:

- `ai-model-picker-cli` — an interactive tool that helps you *pick* a model.
  This project is different: it teaches you to *read the numbers yourself*.
- `mini-model-bench-cli` — a runnable script that *tests* models.
  This project is the manual behind why its results make sense.

## License

MIT — see [LICENSE](LICENSE). `Copyright (c) 2026 Asdale Dynamics, LLC`

## Editorial promise

Numbers go out of date fast; judgment doesn't. Nothing here tells you which
model is "best" — it teaches you how to ask better questions, run your own
quick checks, and stay skeptical of anyone selling you a leaderboard. Use AI
to assist your thinking, especially for anything involving health, money, or
law — and always confirm important things with your own trusted sources.
