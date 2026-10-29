---
type: doctrine
tags: [learning, learning/practice]
---

# Spaced repetition systems

Software that schedules what to review and when, so review minutes land only on the items about to be forgotten. It operationalises the two highest-utility findings in the field — [[The spacing effect|spacing]] and [[The testing effect|retrieval]] — in a single tool. Anki is the dominant open-source implementation; this vault feeds it via the obsidian-to-anki plugin, so the cards at the foot of these notes flow straight into it.

## The algorithms

- **SM-2** (Woźniak, 1987) — the ancestor. A static heuristic: each card has an "easiness factor", intervals grow 1 day → 6 days → ×EF, and a failed recall resets the interval. Anki ran a variant of this for years.
- **FSRS** (Free Spaced Repetition Scheduler) — the modern default, shipped natively in Anki since version 23.10 (late 2023). Instead of a fixed rule, it fits a memory model to the user's own review history: the DSR model tracks, per card, **D**ifficulty (how hard the item is for that user), **S**tability (how long until recall decays — the variable SM-2 lacked), and **R**etrievability (probability of recall right now), and schedules to a target retention the user sets (default 90%). On a large benchmark it predicts recall more accurately than SM-2 for about 99.6% of users, with a claimed 20–30% fewer reviews at equal retention. That efficiency figure is model-derived, not from a controlled trial.

In practice: turn FSRS on, set desired retention to 0.90 (raise to 0.92–0.95 for material that genuinely cannot be forgotten, drop to 0.85 to cut volume on low-stakes material), and run the optimiser after a few weeks of reviews so the model fits the data.

## Writing cards: the minimum-information principle

Woźniak's "20 rules of formulating knowledge" are well-grounded craft. The most important:

- **One atomic fact per card.** A card that keeps failing is doing too much — split it. This is the same logic as managing [[Cognitive load and worked examples|element interactivity]].
- **Prefer cloze deletion** (hide one piece of a sentence) as the default format.
- **Avoid sets and enumerations.** Memory handles unordered and ordered lists badly; convert "the five stages of X" into separate cued cards or a chain, not one card with a five-item answer.
- **Build on basics** — do not card advanced material before the foundations it rests on are solid.
- **Personalise with concrete examples.** Woźniak's strongest single booster: a card tied to a specific situation or a vivid concrete instance is far stickier than a generic one.
- **Date-stamp volatile facts.** A competitor's pricing or a market statistic goes stale; note when it was true.

The deep treatment of these rules, the mechanisms behind them (encoding specificity, cue overload, interference), and the practical technique for diagnosing and rewriting cards that violate them lives in [[Flashcard formulation]].

## The limit — card facts, not skills

SRS is strong for atomic declarative facts and weak for skill, judgment, synthesis, and transfer. A card answered perfectly proves only that the card can be answered, not that the knowledge can be deployed live on a sales call ([[Transfer of learning|transfer]] is exactly what flashcards do not buy). The failure mode is the "Anki zombie": thousands of perfect cards mistaken for competence.

Card only the genuinely declarative layer of a domain: CAC/LTV/payback formulas, pricing tiers, named frameworks (MEDDIC, JTBD, the stages of a sales motion), benchmark numbers, and recurring objections paired with scripted responses. Memorising these does not produce skill; making them instant frees working memory, so during the actual rep attention is available for [[Deliberate practice in fuzzy domains|judgment]] instead of for recalling the formula. SRS handles the facts; real practice builds the skill.

## Where this comes up

- [[The spacing effect]] / [[The testing effect]] — the two mechanisms SRS fuses
- [[Learning from a book or course]] — where the durable facts come from before they are carded
- [[Deliberate practice in fuzzy domains]] — the skill layer SRS deliberately does not cover
- [[The operating system]] — the fact layer of the loop

## Sources

- Woźniak, P. (1990; 1999). The SM-2 algorithm and *Twenty rules of formulating knowledge*. SuperMemo.
- Open Spaced Repetition (Ye, J., et al.). FSRS and the DSR model; the srs-benchmark project. — efficiency figures are model-derived.
- Cepeda et al. 2006 — spacing. Roediger & Karpicke 2006 — testing. Dunlosky et al. 2013 — both rated high-utility.
