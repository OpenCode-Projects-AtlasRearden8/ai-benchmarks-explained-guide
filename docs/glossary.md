# Soft Glossary

Plain-English definitions, one or two sentences each, alphabetical. The
interactive version lives at `site/glossary.html`.

- **Arena (Chatbot Arena / Elo-style rating)** — A leaderboard built from
  real people voting between two anonymous answers. Measures *preference*,
  not correctness — polished, confident answers tend to win votes.
- **Benchmark** — A fixed set of tasks with known answers (or a judging
  method), used to score models. A measurement, not a promise.
- **Benchmark saturation** — When top models cluster near the maximum score
  and small differences become noise.
- **Chat / instruct model** — A model tuned to converse and follow
  instructions. What you want for everyday use; contrast with a raw base
  model, which just continues text.
- **Contamination** — Benchmark questions leaking into training data so a
  model can score from memory rather than skill.
- **Cloud model** — A model running on a provider's servers; you pay a fee
  and send prompts over the network.
- **Context window** — How much text a model can consider at once.
  Exceeding it means the model genuinely can't "see" the extra material.
- **Elo rating** — A relative score from pairwise comparisons (chess
  heritage). Meaningful only against models rated in the *same* pool.
- **GGUF** — The common file format for compressed ("quantized") local
  model files; standard for Ollama and friends.
- **Hallucination** — A confident, fluent answer that is wrong. A natural
  side effect of generating plausible text, not a random glitch.
- **Held-out / fresh items** — Benchmark questions kept out of training
  (or created after training ends) to resist memorization.
- **IFEval-style constraint test** — Checking whether a model obeys
  explicit rules ("exactly three sentences, no commas"). Predictive of
  real-life annoyance level.
- **Inference** — Running a model to get answers (as opposed to training
  one).
- **Jailbreak** — A prompt trick attempting to bypass a model's safety
  behavior; safety scores only cover the known tricks.
- **LLM (large language model)** — The model type behind chat assistants;
  trained on enormous amounts of text to predict plausible continuations.
- **Local model** — A model running on your own hardware via tools like
  Ollama or LM Studio. Private by default; limited by your machine.
- **MMLU (Massive Multitask Language Understanding)** — A many-subject
  multiple-choice knowledge test; the classic "school survey" benchmark.
- **Multimodal** — Handles more than one input type (text plus images,
  sometimes audio).
- **Ollama** — A popular free tool for downloading and running local
  models with simple commands.
- **Over-refusal** — Declining harmless requests out of caution; a
  usability cost, not a safety achievement.
- **Parameters (B = billion)** — Roughly, the model's size — more
  parameters means more capability headroom *and* more RAM needed.
- **Per-category / per-slice scores** — The sub-scores behind an overall
  average; usually more informative than the banner number.
- **Prompt** — The text you send the model; its phrasing measurably
  changes scores.
- **Quantization** — Compressing a model's numbers to fit consumer
  hardware, trading a little quality for a lot of feasibility.
- **RAM** — Your computer's working memory; the main limit on which local
  models fit (8 GB tiny, 16 GB mid-small, 32 GB+ lower-mid is the rough
  ladder).
- **Refusal rate** — How often a model declines requests; read it
  per-category (harmful vs. harmless).
- **Safety benchmark** — A test of how a model responds to adversarial
  prompts (bias, toxicity, harmful requests). A snapshot against known
  attacks, not a guarantee.
- **SOTA (state of the art)** — "Best publicly known score right now" —
  which quietly expires every few weeks.
- **TruthfulQA-style benchmark** — Tests whether a model resists common
  misconceptions instead of echoing them.
