---
type: concept
tags: [learning, learning/flashcard-formulation]
---

# The minimum information principle

The principle that a flashcard should encode the smallest possible unit of knowledge — one atomic fact per card, with no extraneous material in the answer. It is Rule 4 of Woźniak's "Twenty rules of formulating knowledge" (1999), and the single most-cited piece of card-writing advice in the spaced-repetition community. The claim: simpler items are easier to remember, easier to schedule, and more resistant to interference than complex ones.

## What Woźniak actually claims

The "20 rules" are informal craft wisdom from two decades of building SuperMemo and coaching users, published as an article on supermemo.guru (originally 1999, updated periodically). They are not a research paper and do not cite controlled experiments in support. Woźniak's argument is empirical in the practitioner sense — based on patterns observed across thousands of users and millions of card reviews — but not experimentally validated.

The core claims:

1. **Complex items are hard to schedule.** A card that bundles multiple facts will fail whenever any sub-fact is forgotten, even if the others are solid. The scheduler treats the card as one unit; it cannot space one sub-fact differently from another. The result is wasted reviews on the parts already known and insufficient reviews on the part that keeps failing.

2. **Complex items are harder to retrieve.** An answer with five elements creates five opportunities for partial recall, and partial recall creates ambiguous self-grading. The learner does not know whether to mark the card as known or failed, which corrupts the scheduler's model.

3. **Decomposition forces understanding.** Splitting a complex item into atomic cards forces the learner to identify what the distinct facts actually are, which is itself a form of [[Elaboration and self-explanation|elaborative processing]].

## Evidence assessment

The minimum information principle is a **practitioner heuristic**, not a controlled-experiment finding. No study has directly compared "one-fact cards" with "multi-fact cards" in a spaced-repetition system and measured long-term retention. However, the principle is consistent with and well-motivated by several established findings:

- **Cue overload and interference.** When multiple facts are associated with a single retrieval cue (the question), recall of each individual fact is impaired because the associations compete at retrieval (Watkins, 1979; Anderson, 2003). This is the mechanism explored in [[Interference and cue overload]]. The more facts behind one question, the less reliably any one of them is recalled.

- **Encoding specificity.** Material in the answer that the question does not cue is not being tested — it is being re-read. [[Cue-dependent recall]] predicts that only the cued portion benefits from retrieval practice.

- **Cognitive load.** An answer with high element interactivity — where the components interact and must be processed simultaneously — taxes working memory at encoding ([[Cognitive load and worked examples]]). Reducing element count reduces load.

- **Testing-effect specificity.** The benefit of retrieval practice is specific to what was retrieved; related-but-untested material shows near-zero transfer benefit ([[Pan & Rickard 2018]]). Each fact that should be learned must be individually tested.

The alignment is strong enough that the principle is well-grounded even without direct validation. The gap is the obvious one: the ideal grain size of "atomic" is undefined. Woźniak's examples suggest one proposition per card, but what counts as one proposition in a complex domain is a judgment call, not a measurement.

## Relationship to cloze deletion

Woźniak recommends cloze deletion as the default card format (Rule 5), because it decomposes naturally: a passage with three facts becomes three cloze cards, each testing one fact in context. This is a practical implementation of the minimum information principle — the context stays visible, and only one piece is hidden per card. Whether cloze outperforms basic (front/back) format for a given item depends on whether the surrounding context is necessary for the fact to be meaningful. If the fact is self-contained ("NRR stands for net revenue retention"), basic suffices. If the fact depends on its frame ("In Rachleff's value hypothesis, the three components are what you're building, ___, and what business model delivers it"), cloze preserves the frame.

## Where this comes up

- [[Cue-dependent recall]] — the mechanism: only cued material is tested
- [[Interference and cue overload]] — the mechanism: more items per cue = worse recall per item
- [[Spaced repetition systems]] — the brief statement of this principle in the operating system
- [[Rewriting overloaded cards]] — the practical technique for applying it
- [[Card formulation anti-patterns]] — what happens when it is violated
- [[Flashcard formulation]] — the hub note

## Sources

- Woźniak, P. (1999; updated periodically). *Effective learning: Twenty rules of formulating knowledge*. SuperMemo Guru. — the source of the principle; practitioner heuristic, not experimental.
- Watkins, O. C., & Watkins, M. J. (1975). Buildup of proactive inhibition as a cue-overload effect. *JEP: Human Learning and Memory, 1*(4), 442–452. — cue overload.
- Anderson, M. C. (2003). Rethinking interference theory: Executive control and the mechanisms of forgetting. *Journal of Memory and Language, 49*(4), 415–445. — interference at retrieval.
- [[Pan & Rickard 2018]] — testing-effect specificity.
- [[Cognitive load and worked examples]] — element interactivity and working-memory limits.
