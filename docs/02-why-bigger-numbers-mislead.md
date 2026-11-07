# 02 — Why Bigger Numbers Mislead

A higher score on a leaderboard **usually** means "did better on that test."
But there are at least five honest ways the story goes sideways. Once you can
name them, you can't un-see them — you'll start noticing them in every launch
post you read.

## Reason 1: The benchmark gets memorized (contamination)

Benchmark questions end up on the internet — in study guides, GitHub repos,
blog posts — and models trained on the internet can have seen the exact
questions before. That's called **contamination**. It's like grading a
someone's math test after handing them the answer key in study hall.

- You can't easily prove a model *didn't* see the questions, so treat
  suspiciously huge jumps on old benchmark names with care.
- Counter-move many builders use: keep held-out sets, refresh items, or test
  on questions created after the training data ends. When a leaderboard
  mentions "fresh" or "held-out" questions, that's a good sign.

## Reason 2: Near the ceiling, differences shrink to nothing

When a benchmark is mature and popular, top models cluster in the high 80s
and 90s. A jump from `91.2%` to `91.8%` looks like progress but is usually
noise — a handful of questions either way, prompt phrasing, luck.

> **Rule of thumb: when everyone scores above 90%, the test has stopped
> separating the good from the very good. Read it as "everyone passed."**

## Reason 3: Prompting and setup change the number

The same model, asked the same questions, can score noticeably differently
depending on:

- the exact wording of the instructions ("answer with the letter A–D" vs.
  "answer with the full text of the choice"),
- whether it's allowed to "think out loud" first,
- how many attempts are made and how scoring picks the best one.

So "Checkers-7B scored 70%" really means "a particular team ran Checkers-7B
under a particular setup and got 70%." Re-run scores are estimates, not laws
of nature.

## Reason 4: The average hides the shape

An overall score is an average — and averages flatten out what you'd care
about most. A model can earn a great overall number while being terrible at
exactly the thing you need.

Fictional worked example — **Widget-9B**, overall score **78%**:

| Skill slice | Score |
| --- | --- |
| Word puzzles | 95% |
| Multi-step math | 41% |
| Following multi-part instructions | 52% |
| Refusing harmful requests politely | 88% |

78% overall looks solid. If you need the model to reliably do three-step
*safety-critical* instructions, the 52% slice is the one that matters, and it
is hidden. **Whenever possible, read the per-category scores, not the banner
number.**

A related trick: averaging can mask a lopsided model, just like a restaurant
with average "4 stars" can be terrible at breakfast and great at dinner.

## Reason 5: Marketing picks the flattering test

Every model has a strongest benchmark, and promotional posts lead with that
one. This isn't usually lying — it's *emphasis*, which is quieter and harder
to notice.

- A coding-strong model leads with its coding score.
- A chat-focused model leads with its human-vote arena rating.
- A small model leads with "best 7B!" — a category created by slicing the
  field however convenient.

**Counter-move:** before believing "best," ask *best at chosen what, compared
to whom, per what* to your actual use case? A model that is "best 3B in
class" can still be worse for your task than last year's 13B.

## Bonus: tie-breaking on different tests

Sometimes two different benchmarks produce *different winners*, both honestly
run. That's not a scandal; that's testing different skills. Treat any
conflict between leaderboards as a prompt to run your own ten-minute check
(chapter 05), not as a reason to trust the loudest source.

## Quick scoring-hygiene checklist

When you see a big number, ask:

1. Was the test fresh/held-out, or old and famous (memorization risk)?
2. Is everyone near the ceiling (top-90s cluster)?
3. Whose run procedure produced it — and would mine match?
4. What does each per-skill slice look like?
5. Which test did the marketing choose to show me — and which did they skip?

If even one of those is missing from the page you're reading, lower your
confidence one notch. That's the whole game: confidence in *notches*, not
certainty in neon digits.
