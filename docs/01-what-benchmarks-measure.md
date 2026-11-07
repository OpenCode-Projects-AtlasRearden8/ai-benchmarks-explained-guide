# 01 — What Benchmarks Actually Measure

Let's start with the plainest possible definition.

> **A benchmark is a fixed set of questions — with known answers — that a
> model takes like an exam.** The score is simply the share it gets right
> (or how well judges rate its answers).

That's it. Everything else in this chapter is consequences of that one idea.

## The anatomy of a benchmark

Every benchmark you'll meet has the same four parts:

1. **Item set** — the questions or tasks. Could be 300 items, could be 15,000.
2. **Answer key or judge** — either fixed right answers, or a grading method
   (sometimes a human, sometimes another AI playing judge).
3. **Run procedure** — the exact way the model is asked (the phrasing of the
   prompt, how many tries, temperature setting — all of it is chosen by
   someone).
4. **A scoring rule** — percent correct, per-task average, or a rating like
   the Elo-style scores used by human-vote arenas.

So a benchmark is best imagined as a standardized test — even the good ones
only sample the subject.

## What the scores are really measuring

Here's the crucial nuance: **a benchmark measures performance on a proxy.**
Nobody can test "is this model actually good" — good at *what*, for *whom*?
So benchmark builders pick a stand-in:

| Benchmark measures... | As a stand-in for... |
| --- | --- |
| Multiple-choice questions across school subjects | Broad knowledge |
| Word-association puzzles | Common sense |
| Grade-school math problems | Everyday reasoning |
| Real editing tasks from file-change records | Practical coding |
| Human votes on two anonymous answers | "Do people like the reply?" |

The stand-ins are chosen thoughtfully, but they're still stand-ins. A model
can be better in real life than its "reasoning" score — or worse.

## Scores are relative, mostly

One underappreciated fact: a score means the most **relative to other models
on the same benchmark, run the same way**. "Checkers-7B scored 62%" doesn't
mean 62% of anything you care about. "Checkers-7B scored 62% vs. Neighbor-8B
at 61% on the same test, same run procedure" is a (weak but real) signal about
which one to try first.

Scores become misleading the moment someone compares a number from one
benchmark to a number from another — or to the same benchmark run a different
way. You'll see exactly how that goes wrong in chapter 02.

## What benchmarks measure well (and don't)

**They're good at catching:**

- Big gaps between similar-size models (one clearly lagging).
- Whether a model has trouble with a specific *skill type* — say, math with
  multiple steps.
- Obvious regressions: a new release scoring much worse than the old one.

**They're bad at telling you:**

- Whether the model will be pleasant, clear, or patient with *your* phrasing.
- Whether it *freshly learned* something (a benchmark is frozen in the past).
- Whether it fits on your computer (nothing about memory here).
- Whether it hedges, rambles, or takes forever to answer.

That last family of qualities — tone, speed, fit, feel — is exactly why
chapter 05 gives you a do-it-yourself sanity test. The benchmark gets you a
short-list; your ten minutes picks the winner for you.

## A friendly example

Imagine two fictional models on a fictional school-quiz benchmark:

- **Storyteller-13B: 88%** (answers quickly, warm tone, occasionally invents
  city council dates)
- **Checkers-13B: 90%** (drier tone, twice as slow, rarely invents anything)

The leaderboard says Checkers wins. Real life - for a nurse drafting a plain-
English patient handout — could easily favor Storyteller *unless* accuracy on
small facts matters more than warmth. The benchmark doesn't know your tradeoff;
*you* do, and that's the whole theme of this guide.
