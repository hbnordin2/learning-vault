---
type: doctrine
tags: [learning, learning/flashcard-formulation]
---

# Card formulation anti-patterns

A catalogue of recurring failure modes in flashcard design. Each anti-pattern is described with the mechanism that makes it fail, so the diagnosis points toward a fix rather than just a label. Most of these are instances of violating [[The minimum information principle]], [[Cue-dependent recall|cue specificity]], or [[Interference and cue overload|cue overload]], or of producing cards that train recognition rather than recall.

## 1. The overloaded answer

The answer contains more information than the question asks for. The cued portion is retrieved; the trailing material is re-read after flipping the card.

**Example:**
> Q: What are the two leading indicators of product-market fit?
> A: Retention (does the cohort retention curve of the key action at its natural frequency flatten?) and the Sean Ellis survey (do 40%+ of users say they'd be "very disappointed" to lose the product?). Lagging indicators — organic growth, word-of-mouth — come later.

The question asks for two names. The answer gives them, then defines each in parenthetical detail, then appends a bonus clause about lagging indicators. The learner who answers "retention and the Sean Ellis survey" has fully answered the question but will see a wall of text they did not produce, creating a false sense of failure.

**Mechanism:** [[Cue-dependent recall]] — material the question does not cue is not being tested. [[Interference and cue overload]] — the trailing facts compete with and are suppressed by the cued facts. The SRS scheduling is corrupted because self-grading incorporates uncued material.

**Fix:** Split. The question "What are the two leading indicators of PMF?" gets an answer of two names and nothing else. Each indicator's definition, threshold, and mechanism become separate cards with their own questions.

## 2. Enumeration and list cards

A question that asks the learner to produce an unordered set of items: "What are the five components of X?"

**Problem:** Memory handles unordered sets badly. Each item is an independent recall target, but they share a single cue. [[Interference and cue overload|Cue overload]] means recall of each degrades with set size. The learner consistently recalls the same 3 of 5, marks the card as failed, and the two forgotten items never get individually spaced. Woźniak (1999) identifies this as the most common card-writing error.

There is a related but distinct problem: **ordered sequences** ("list the stages of X in order"). These are less susceptible to cue overload because the ordinal position provides an additional retrieval cue, but they are still prone to the "chain-break" problem — forgetting one element breaks access to all elements that follow.

**Fix:** Convert each element into a separate card. For ordered sequences, use chained cloze cards: "The stages of X are: _1_, 2, 3, 4, 5" / "The stages of X are: 1, _2_, 3, 4, 5" / etc. For unordered sets, give each element its own question that cues it independently (e.g., "Which component of X addresses [specific function]?").

## 3. Yes/no and binary cards

A question with a binary answer: "Is X true?" / "Does Y cause Z?"

**Problem:** The answer has a 50% base rate by guessing, so "correct" retrieval often reflects a coin flip or a vague association, not durable knowledge. Even when the learner genuinely knows, producing "yes" or "no" exercises almost no retrieval — there is no content to reconstruct ([[Retrieval is reconstruction]]). Recognition of the direction of the fact replaces recall of the fact itself.

**Fix:** Reframe as a recall question. "Is NRR above 100% good?" → "What does NRR above 100% indicate?" The learner must now produce the content rather than evaluate a proposition.

## 4. The ambiguous question

A question with multiple defensible answers depending on interpretation, or a question so general that the learner cannot determine what the card "wants."

**Example:**
> Q: What is important about retention?
> A: [Any of a dozen possible answers depending on the domain]

**Problem:** Ambiguity defeats encoding specificity. The learner encodes one interpretation; the card expects another. Repeated failures that feel arbitrary erode trust in the SRS system and produce "learned helplessness" around that card — the learner stops genuinely trying to retrieve and starts guessing what the card-maker intended.

**Fix:** Make the question specific enough that there is exactly one correct answer. "What does retention indicate when measured as the key-action retention curve?" or "In PLG, why is retention the centre of the growth engine rather than acquisition?" The constraint should be in the question, not silently held in the answer.

## 5. The essay-answer card

A question so broad that the only valid answer is a paragraph of exposition. The learner cannot reproduce a paragraph from a cue, so they retrieve fragments, flip the card, and grade on a vague impression of how close they got.

**Example:**
> Q: Explain the relationship between venture selection and product-market fit.
> A: [a 50-word paragraph]

**Problem:** Self-grading is unreliable because there is no crisp success criterion. The same answer might be graded "Good" on a confident day and "Again" on a self-doubting day. The SRS model requires a stable signal; unstable self-grading produces scheduling noise. Additionally, paragraph-length answers bundle multiple facts behind one cue — the overloaded-answer problem at scale.

**Fix:** Decompose the essay into its constituent claims. Each claim becomes a card with a specific question. The relationship between venture selection and PMF is not one fact — it is a claim about what venture selection does (searches), a claim about what PMF does (validates), and a claim about the sequencing between them. Three cards, three questions, three stable grading targets.

## 6. Conceptual and judgment cards

A card that asks for a contextual judgment or a "best" answer as if it were a stable fact.

**Example:**
> Q: What is the best go-to-market strategy for a startup?

**Problem:** The answer depends on context (stage, market, product type) and has no single correct retrieval target. The learner is being asked to memorise a recommendation rather than a fact, but recommendations change with context. The card either locks in a context-free platitude or requires the learner to reconstruct a nuanced argument — which is the essay-answer problem.

**Fix:** Card the underlying facts that inform the judgment, not the judgment itself. "What does Rachleff argue must be proven before testing the growth hypothesis?" has a stable answer. The judgment about which strategy is "best" is a skill exercise, not a flashcard target — that belongs to [[Deliberate practice in fuzzy domains]], not the SRS.

## 7. Missing context

A card that assumes knowledge of the surrounding note, conversation, or source that produced it. The card makes sense during the first review session — when the context is still in working memory — but becomes opaque when encountered weeks later in a mixed-deck review.

**Example:**
> Q: What is the key action?
> A: The one user behaviour that best represents the product's core value, measured at its natural frequency.

"The key action" assumes the learner remembers this is a retention-measurement concept from the PMF literature. Encountered out of context, it could be about product analytics, user research, or game design.

**Problem:** The retrieval cue is underspecified. It works as a within-context prompt but not as a standalone item. The card violates a basic requirement: it must be self-contained.

**Fix:** Embed enough context to make the card standalone: "In retention measurement, what is the key action?" The context word ("In retention measurement") narrows the cue to a single interpretation without giving away the answer.

## Where this comes up

- [[Cue-dependent recall]] — the mechanism behind anti-patterns 1, 4, 5, and 7
- [[Interference and cue overload]] — the mechanism behind anti-patterns 1 and 2
- [[The minimum information principle]] — the principle violated by most of these
- [[Rewriting overloaded cards]] — the practical technique for fixing them
- [[Flashcard formulation]] — the hub note

## Sources

- Woźniak, P. (1999). *Effective learning: Twenty rules of formulating knowledge*. SuperMemo Guru. — identifies enumeration as the most common error; the source of minimum-information guidance.
- Dunlosky, J., Rawson, K. A., Marsh, E. J., Nathan, M. J., & Willingham, D. T. (2013). Improving students' learning with effective learning techniques. *Psychological Science in the Public Interest, 14*(1), 4–58. — self-testing practice, including the conditions that make it effective.
- [[Pan & Rickard 2018]] — transfer specificity; the testing effect does not spread to untested material.
