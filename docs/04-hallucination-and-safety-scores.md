# 04 — Hallucination and Safety Scores, Read Honestly

These are the numbers people *should* look up, and often don't. If chapter 02
was about not being fooled upward, this one is about not being fooled
downward — assuming a model is trustworthy because nothing went wrong the two
times you tried it.

## What "hallucination" means (and doesn't)

> **A hallucination is a confident, fluent answer that is wrong.** Not a bug
> that strikes randomly — a natural side effect of how language models
> produce text: they generate plausible *continuations*, and plausible is not
> the same as true.

Classic species of hallucination:

- **Invented citations** — real-sounding authors, journals, years.
- **Wrong specifics on thin facts** — dates, street addresses, dosage
  details, version numbers.
- **False familiarity** — claims to remember "our last conversation" or
  agrees it wrote a book it never saw.
- **Confident arithmetic** — wrong numbers in a perfectly structured table.

## How benchmarks measure it

No test can catch every hallucination, so each benchmark probes a different
door into the same room:

- **TruthfulQA**: does the model *resist common misconceptions* when the
  folklore is the tempting answer? High score = less echo of urban legends.
- **HaluEval-style tests**: dose the model with prompts that *invite*
  making things up (fill in an unknown detail, summarize a fake paper).
  Measure how often it fabricates instead of saying "I don't know."
- **SimpleQA-style short-fact benchmarks** (a family of "answer hard
  factual questions where we know the truth" tests): measure raw accuracy on
  niche facts. Honest finding from these: factual accuracy on little-known
  specifics is *low* for many models — sometimes startlingly low.
- **Human-vote arenas (partially)**: users can downrate a confidently-wrong
  answer, but Plenty of wrong answers sound pleasant, so this only weakly
  measures truth.

## Reading hallucination numbers without despairing (or trusting)

Three rules that keep you sane:

1. **A 90% truthful score does not mean 10 lies per 100 sentences.** Different
   tests count different things (per question, per claim, per session).
   Read what unit the percent is *of*.
2. **High-truth scores transfer weakly to *new* topics.** A model can be
   careful about well-known misconceptions and still invent a citation about
   your state's licensing rules.
3. **Lower is not zero.** There is no "verified truthful" badge. There are
   only *more careful* and *less careful* models.

Practical habits that actually reduce harm, beyond caring which model you
pick:

- Ask for sources you can check, then **check them** (fake citations
  sometimes have real-sounding but non-existent titles).
- Prefer models that comfortably say "I don't know" — test this in chapter
  05's exercise 4.
- For anything with stakes (health, legal, money), treat AI output as a
  *first draft from a new intern*, verifiable by you or a trusted source.

## Safety scores, honestly

Safety benchmarks measure how a model responds to *adversarial prompts* —
attempts to make it produce harmful content in categories like violence,
self-harm content, or targeted harassment, plus bias probes:

- **BBQ (Bias Benchmark for QA)**: does the answer depend on who the person
  is (name, age, gender)?
- **ToxiGen / RealToxicityPrompts**: does the model continue a loaded prompt
  into hostile text?
- **Refusal tests**: when a clearly harmful request arrives, does the model
  decline, comply, or fumble with a half-helpful hedge?

Two honest caveats about safety numbers:

1. **"Refusal rate" is not a virtue on its own.** A model that refuses
   everything — including your harmless requests — can score great on safety
   while being useless to you. Some models too eagerly refuse ordinary
   things. Read per-category rates, not one big number.
2. **Safety benchmarks are snapshots against known attack styles.** Clever
   new prompt tricks ("jailbreaks") may work around last year's defenses.
   Scores move in both directions as the cat-and-mouse continues.

## The healthcare-worker note (education only)

If you're a nurse, therapist, or clinician with a personal interest in AI:
general-AI safety scores tell you nothing about clinical appropriateness.

- A model can pass generic safety tests and still confidently produce
  something that *sounds* like clinical guidance.
- Never use a general-purpose chat model as a clinical decision source, and
  never enter patient data into a tool that isn't approved for it.
- Treat this entire guide as background education — the kind of thing you
  already do as a professional: check sources, apply judgment, escalate when
  unsure.

## A worked example, with two fictional models

> Illustrative numbers; the *shape* of the table is what teaches.

| Measure | Storyteller-13B | Checkers-13B |
| --- | --- | --- |
| TruthfulQA (resist misconceptions) | 71% | 84% |
| Fabrication rate on unknown-detail prompts | frequent | occasional |
| Willing to say "I don't know" | rarely | often |
| Refusal rate (harmful) | high | high |
| Refusal rate (harmless requests it dislikes) | moderate | low |
| Overall "safety" banner | 93% | 91% |

Who's better here? Checkers is steadfast and honest but occasionally spills
fabrications less; Storyteller is pleasanter but overconfident. The 93 vs.
91 banner hides a real difference that *matters differently* depending on
whether you're drafting invites or answering questions about insurance law.
Banner scores compress exactly the details you'd want to keep.

Next: use what you've learned against a real, live model — in ten minutes,
[`05-ten-minute-sanity-test.md`](05-ten-minute-sanity-test.md).
