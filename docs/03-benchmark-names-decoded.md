# 03 — Decoding MMLU-Style Benchmark Names

AI benchmark names are proud, slightly silly acronyms — a naming style
inherited from academic papers. Once you know the pattern, you can decode a
name you've never seen and make a decent guess at what it measures. Then we
turn to the famous ones individually.

## The acronym pattern, in three moves

Almost every benchmark name is built like this:

1. **Pick the domain** (math, questions, common sense, honesty).
2. **Add scope words** — *Massive, Multi-, Grade-School, Graduate-Level* —
   to describe quantity or difficulty flavor.
3. **Compress to a pronounceable acronym**, ideally cute enough to remember.

Example: **MMLU = Massive Multitask Language Understanding.** Massive
(thousands of items), Multitask (many subjects mixed), Language Understanding
(the aspiration, not the proof). That's the whole decoding engine. Let's run
it on the classics.

## The famous names, decoded

> Scores and SOTA values below are examples for illustration; what matters is
> *what each test measures*, not whether the numbers are current.

### Knowledge and school-style tests

- **MMLU — Massive Multitask Language Understanding.** Thousands of
  multiple-choice questions across subjects: history, law, medicine,
  math... Good old general-knowledge survey. Caveat: it's been public for
  years, so treat very high scores with the chapter-02 squint.
- **MMLU-Pro — "MMLU, but harder."** Fewer nonsense distractor answers,
  more reasoning-heavy items. The name is the pitch.
- **GPQA — Graduate-level, Google-Proof Q&A.** Written by domain PhDs, in
  theory hard to answer even with search open ("Google-proof"). Small set,
  hard questions.
- **ARC — AI2 Reasoning Challenge.** Grade-school science questions that
  trip up pattern-matching. Multiple-choice reasoning flavor.
- **MMMU — Massive Multi-discipline Multimodal Understanding.** MMLU's
  sibling that includes *images* (charts, diagrams). *Multimodal* = more
  than one mode of input.

### Commonsense and word-puzzle tests

- **HellaSwag.** Sentence completion: pick the most plausible continuation
  of a scenario. Yes, really named after a college survey (SWAG) with
  "Hella" = "a lot of" slapped on. Adversarially filtered so naive
  pattern-guessing fails.
- **WinoGrande.** A large version of the Winograd Challenge: sentences
  where a pronoun's meaning depends on *real-world logic*
  ("The trophy didn't fit in the suitcase because it was too big — what is
  *it*?").
- **PIQA — Physical Interaction Question Answering.** Everyday physical
  common sense: how do you actually separate an egg yolk?
- **BigBench / BIG-Bench — Beyond the Imitation Game Benchmark.** A grab
  bag of hundreds of odd tasks; the "hard" subset is **BBH (BigBench-Hard)**.

### Reasoning and math

- **GSM8K — Grade School Math, 8K (8,000) problems.** Word problems a
  careful 4th–8th grader could do, multi-step. Saturation zone for big
  models; still useful for small ones.
- **MATH — literally the dataset named MATH.** Competition-style problems
  (algebra, geometry, proofs), much harder than GSM8K.
- **AIME** — American Invitational Mathematics Examination problems, used to
  probe top-end reasoning. If a model scores well here, it's genuinely
  capable at hard math *as measured by hard math*.

### Honesty, truthfulness, and safety

- **TruthfulQA.** Questions where a *common misconception* is the tempting
  wrong answer ("Do we only use 10% of our brains?"). A model that echoes
  folklore gets punished. Note the subtlety: it tests *resistance to
  falsehood*, not breadth of fact.
- **BBQ — Bias Benchmark for QA.** Social-bias probes: does the answer
  change based on a person's name, gender, age, etc.?
- **RealToxicityPrompts / ToxiGen.** Continuation and generation tests that
  score whether outputs turn hostile or offensive from loaded prompt
  starts.
- **HaluEval and friends.** Tests built to measure **hallucination rate** —
  does the model invent details (fake citations, wrong dates) when the
  prompt invites it to?

### Coding and real-world tools

- **HumanEval.** Small classic set: write a Python function to match a doc
  comment; graded by *running* the code against hidden tests. Old enough
  that very high scores are expected now, not impressive.
- **SWE-bench (Verified).** Real GitHub issues from real repositories: can
  the model produce a change that fixes the failing test suite? "Verified"
  = humans filtered item quality. One of the best stand-ins for
  *practical* coding because the grading is automated and concrete.
- **LiveCodeBench — a contamination-aware coding test.** Uses problems
  *published after* a model's training cutoff, exactly to dodge Reason 1
  (memorization) from chapter 02.

### Chat quality and instruction following

- **MT-Bench — Multi-Turn Benchmark.** Two-turn conversation judged (often
  by a strong model acting as judge) on helpfulness.
- **IFEval — Instruction-Following Evaluation.** Petty (on purpose!) rules:
  "answer in exactly three sentences," "no commas," "write in all-caps."
  Tests whether a model obeys *constraints*, which many models are
  surprisingly bad at. Very predictive of real-life annoyance level.
- **Chatbot Arena (LMSYS/LMSYS-Elo family).** Humans vote between two
  anonymous answers; models get Elo-style ratings. Honest strengths:
  reflects real people voting on real questions. Honest weaknesses: votes
  favor confident-sounding, nicely formatted answers; the crowd isn't every
  audience.

## Reader's mini-dictionary of name suffixes

| Suffix/word in a name | Usual meaning |
| --- | --- |
| **-8K, -Hard, -XXL, -Pro** | Harder or expanded edition of the base test |
| **-Verified** | Humans quality-filtered the items |
| **Multi-** | Several subjects or input types mixed |
| **Multimodal / M(M)** | Includes images (sometimes audio) |
| **Grade-school / elementary** | Easy for adults, useful to spot small-model weakness |
| **Graduate-level / PhD** | Expert difficulty; separates top models |
| **Live / Fresh / Held-out** | Items created after training, anti-memorization |
| **Elo / Arena** | Human-vote rating, not a percent-correct test |

## Practice round, on me

Try decoding a fictional one: **"NurseQA-Hard-Multi: 90%."** You can now
guess the shape before looking anything up: a question-answer item set
(*QA*), probably domain-flavored, harder edition (*Hard*), several topics
mixed (*Multi*), and a very high score that — per chapter 02 — means "everyone
likely passed." See? You already read it like a nutrition label.

Continue to [`04-hallucination-and-safety-scores.md`](04-hallucination-and-safety-scores.md)
to read the scores that matter most for trust.
