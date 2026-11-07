# 06 — Cloud vs. Local: Choosing Without Math Anxiety

Two ways to use a chat model:

- **Cloud**: you send your question to someone else's computer (OpenAI,
  Anthropic, Google, or whichever service) and get an answer back. Usually a
  subscription or metered fee.
- **Local**: the model runs on *your* computer, powered by tools like
  [Ollama](glossary.md#ollama) or LM Studio. No per-message fee, no
  internet needed after download.

Both are legitimate. The trick is matching the choice to *your* situation —
and the good news is that the deciding questions are mostly not math ones.

## The four questions that actually decide it

### 1. How private does this need to be?

- **Local** wins when the stakes are "I don't want this text leaving my
  machine": journals, drafts, family finances, anything sensitive.
  ACTUAL private = the file stays on your disk; no literal incremental
  privacy leak from asking questions.
- **Cloud** is fine for generic questions, brainstorming, learning. Read any
  cloud service's data policy once; the one-sentence version of those
  policies is usually "we may store/train on it unless you opt out or use a
  business tier."

A rough and honest rule: if you'd blush to see the prompt printed in a
neighbor's newsletter, prefer local.

### 2. What's your hardware?

For local models, everything lives and dies by **RAM** and **disk**. Here's
the non-scary version, tuned to the "small model" sizes that actually fit
regular laptops:

| Typical modern laptop/desktop | What it can comfortably run |
| --- | --- |
| 8 GB RAM | Small models (~1–4B parameters, including most "tiny" GGUF builds) — quick tasks, drafting, searching files |
| 16 GB RAM | Mid-small models (~7–8B) — the sweet spot for everyday local use |
| 32 GB+ RAM | Lower-mid models (13–14B) and roomier quantizations of 7–8B; noticeably better quality |
| Mac with M-series chip | Best-case scenario for laptops overall — unified memory handles models better than the raw RAM number suggests |

"GGUF" is just the current popular file format that lets a big model be
dented — **quantized** — down to a compressed size that fits consumer
hardware, at some small quality cost. Most Ollama model pages list file sizes
right up front; that's your disk bill.

> These are rules of thumb, not guarantees. A slow laptop can still run a
> mid-small model faithfully — just *slower* — and speed depends on your CPU,
> and if you have one, your GPU.

### 3. Which tasks are yours?

Rough mapping (and this is where most people talk themselves into the wrong
tier of cloud, so breathe):

| Your use | Local small model is... | Cloud big model is... |
| --- | --- | --- |
| Drafting, rewriting, summarizing your own notes | usually enough | fine too, costs money |
| Brainstorming, tone-checking, "explain this like a friend" | usually enough | overkill |
| Multi-step reasoning over hard material | hit-or-miss; test with ch. 05 | likely better |
| Long-document analysis, big-context coding | limited by context window | likely better |
| Niche factual accuracy | weak — verify anyway | better but *still* verify |

The pattern: **local covers most everyday text work; cloud pulls ahead for
the hardest reasoning tasks.** "Better," combined with chapter 02's five
caveats, of course.

### 4. Is "always available" important?

Local: no network, no subscription expiring, no rate limits, no one
deprecating your favorite tool — only two real failure modes, power and
disk space. Cloud: it's someone else's uptime, someone else's pricing, and
a model you loved can be retired. Local-first is also the friendlier-habit
choice if you're privacy-tired of everything uploading by default.

## What "Ollama-friendly" means (and how to check honestly)

A model is *Ollama-friendly* when:

1. It has a downloadable, quantized build (usually **GGUF**).
2. It's small enough to fit your RAM (see the table above) — the model
   *page* tells you the size; start with the smallest tagged version if
   unsure.
3. It's a *chat/instruct* model — the plain-English label for "tuned to talk
   with people" — not a raw base model (which just babbles continuations).

Honest extra checks that cost you one browser tab each:

- **License**: is it an open-weights license that permits your intended use?
  (Some "open" models still restrict commercial use.)
- **Context window**: how much text it can consider at once. Small models
  often have small context; long documents (a 60-page PDF) may exceed it.
- **"Best at" claims on the model card**: beta-tested by the same skeptic's
  checklist as chapter 02 — per-category, run procedure, recency.

## A worked decision (fictional, but you'll recognize yourself)

> **Priya**: 16 GB laptop, nurse, wants a private journaling helper and
> occasional week-by-week meal planners, is curiously skeptical about
> health-clinic questions.
>
> Choice: **local, mid-small model via Ollama.** Her uses are ordinary text
> tasks, privacy matters (journals), and her hardware is the "sweet spot"
> row. She keeps one free cloud account for the occasional hard multi-step
> question — hybrid approaches are completely fine, and common.
>
> **Marcus**: writes training content as a side business, analyzes long
> PDFs, has an 8 GB laptop. Choice: **cloud, middle-tier plan** for now,
> with the note that a hardware upgrade would open the local option later
> — or a hybrid where drafting happens locally on a *tiny* model and
> analysis stays in the cloud.

Neither chose the "best model on the leaderboard" — they chose the best
*fit*. That's the point.

## The two-minute flowchart (plain English)

1. Do you need maximum privacy? → lean **local**.
2. Is your computer 16 GB+ RAM (or an M-series Mac)? → local is *feasible*
   (still test with ch. 05).
3. Do your tasks include heavy multi-step reasoning over big documents? →
   lean **cloud**, or hybrid.
4. Still unsure? → try both: run exercise 2 and 4 from
   [`05-ten-minute-sanity-test.md`](05-ten-minute-sanity-test.md) against a
   local candidate and your current cloud choice. Your own ten minutes beat
   anyone's billboard.

On to the one-page recap, [`07-cheat-sheet.md`](07-cheat-sheet.md).
