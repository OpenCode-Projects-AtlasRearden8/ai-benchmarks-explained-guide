# 07 — The Cheat Sheet

One page. Print it, screenshot it, or read it before every launch post.

## The five questions to ask any big score

1. **What exactly was measured?** (One benchmark = one test, one domain,
   one moment in time.)
2. **Was the test fresh or famous?** (Old public benchmarks can be
   memorized — *contamination*. Look for "held-out," "fresh," "Live.")
3. **Is everyone near the ceiling?** (Top models clustered 90%+ means the
   test stopped separating good from very good.)
4. **What's in each slice?** (Overall averages hide exactly the
   weaknesses you'd care about — check per-category scores.)
5. **Who ran it, and how?** (Prompt phrasing and setup change numbers;
   scores are estimates, not laws of nature.)

## The name-decoder, condensed

| You see | It usually means |
| --- | --- |
| **-Pro, -Hard, -XXL, -8K** | Harder/bigger edition of a base test |
| **-Verified** | Humans filtered item quality |
| **Multi-, M(M)** | Many subjects / includes images |
| **Live / Fresh / Held-out** | Anti-memorization; created after training |
| **Arena / Elo** | Human votes, not percent-correct |
| **Grade-school vs. graduate-level** | Difficulty flavor, not audience |

## Trust and honesty, in one breath

- A **hallucination** = confident, fluent, wrong. Normal behavior, not a
  glitch.
- Truthfulness benchmarks measure *resistance to known falsehoods* — they
  don't certify a model as truthful.
- "Refusal rate" high isn't automatically good: over-refusing harmless
  requests is a usability bug.
- For anything with stakes, treat AI output as a *draft from a new intern*
  — verify with sources you trust. **Education, never medical/legal/financial
  advice.**

## Your ten-minute sanity test (compact)

1. Greeting — does it hedge or boast?
2. Rephrase test — *"How many days in February 2100?"* then *"Is 2100 a
   leap year?"* (28 days; not a leap year — the two answers must agree.)
3. Arithmetic with process — schedule "every 6 hours from 7 a.m." →
   7 a.m., 1 p.m., 7 p.m., 1 a.m. = 4 doses.
4. Honesty probe — ask a deliberately unknowable fact. Invent? Or "I don't
   know"?
5. Constraint test — "three sentences, no commas, numbered." Count all
   three constraints.
6. Niche fact **you** know cold — right, wrong, or honest-unknown?
7. Safety + pushback — will it flag a fake citation; will it refuse a
   harmless request it doesn't like?

Score each 0/1/2 → out of 14. 11+ worth a bigger trial; under 7 probably
exhausting; ties → favor the honesty probes.

## Cloud vs. local, in one breath

- **Privacy → local.** ("If you'd blush seeing it in a newsletter, keep it
  local.")
- **8 GB → tiny models. 16 GB → mid-small (7–8B). 32 GB+ → lower-mid
  (13–14B).** M-series Macs punch above the line. Rules of thumb, not laws.
- **Everyday drafting/summarizing → local small models usually suffice.**
  Hard multi-step reasoning, huge documents → cloud (or hybrid).
- Ollama-friendly = has a GGUF build, fits your RAM, is a *chat/instruct*
  model, comes with a license you can live with.

## The standing rule

Benchmarks shortlist. **You** decide — with the same skepticism, against
your own ten minutes, for your own tasks. When a number impresses you,
that's the moment to run the checklist, not to buy anything.

*Built by Asdale Dynamics, LLC — plain-English AI education.* Further
reading: everything under `docs/` and the interactive site under `site/`.
