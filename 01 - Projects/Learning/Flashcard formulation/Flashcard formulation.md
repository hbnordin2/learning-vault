---
type: moc
tags: [learning, learning/flashcard-formulation]
---

# Flashcard formulation

How to write a flashcard that tests what it intends to test. [[Spaced repetition systems]] operationalise [[The spacing effect|spacing]] and [[The testing effect|retrieval]] — but the benefit of retrieval practice applies only to what is actually retrieved ([[Pan & Rickard 2018]]), and what is retrieved is determined entirely by the question. A well-scheduled card with a badly written question teaches less than it should, and an overloaded answer corrupts the scheduler by producing unreliable self-grading. Card formulation is the discipline of making the question–answer pair match: one question, one cue, one retrievable fact.

## The central problem

The most common failure mode is not a missing card or a wrong answer — it is an **answer that carries more than the question asks for**. The learner retrieves the cued portion correctly, then flips the card and sees trailing material they did not produce. They mark the card as failed, but the failure is in the card's design, not in their memory. The trailing material was never cued, so it was never tested, so it was never strengthened by retrieval. It was re-read on a schedule — the method the literature rates lowest.

Two mechanisms explain why this fails:

- **[[Cue-dependent recall]]** — recall depends on the match between the retrieval cue (the question) and what was encoded. Uncued material in the answer is not being tested; it is being re-read.
- **[[Interference and cue overload]]** — when multiple facts are associated with a single cue, they compete at retrieval, and retrieving one actively suppresses the others (retrieval-induced forgetting).

## The principle

**[[The minimum information principle]]**: each card should encode the smallest meaningful unit of knowledge — one atomic fact per card, with the question fully specifying the answer. The principle originates in Woźniak's practitioner craft (1999) but is well-grounded in encoding specificity (Tulving & Thomson, 1973), cue overload (Watkins, 1979), and the testing-effect specificity result (Pan & Rickard, 2018): retrieval practice benefits what was retrieved, not what was merely present.

## The failure modes

**[[Card formulation anti-patterns]]** catalogues the recurring violations:

1. **The overloaded answer** — answer carries more than the question cues
2. **Enumeration and list cards** — one question, many targets, each competing
3. **Yes/no and binary cards** — 50% base rate, no recall exercise
4. **The ambiguous question** — multiple defensible answers, unstable grading
5. **The essay-answer card** — paragraph-length answer, unreliable self-grading
6. **Conceptual and judgment cards** — context-dependent answers carded as stable facts
7. **Missing context** — card assumes surrounding context not present at review

Each has a mechanism that explains the failure and points toward the structural fix.

## The practical technique

**[[Rewriting overloaded cards]]** provides the step-by-step:

1. Diagnose the overload (cover the answer, produce a response, identify what was never cued)
2. Parse the answer into atomic propositions
3. Write a question that fully specifies each answer
4. Choose the format (basic, cloze, reversed) to match the knowledge structure
5. Validate by recall test

## The evidence floor

The individual findings that ground this discipline are well-established:

| Finding | Evidence level | Key source |
|---|---|---|
| Retrieval practice strengthens memory more than restudy | Meta-analytic, g ≈ 0.50 | [[The testing effect\|Rowland 2014; Adesope et al. 2017]] |
| Retrieval benefit is specific to what was retrieved | Meta-analytic, d ≈ 0.40 for tested, ~0 for untested | [[Pan & Rickard 2018]] |
| Retrieval depends on cue–target match at encoding | Experimental, foundational | Tulving & Thomson 1973 |
| Cue overload degrades recall per item | Experimental, replicated | Watkins & Watkins 1975 |
| Retrieving one item suppresses competitors | Meta-analytic, d ≈ 0.35 | Anderson, Bjork & Bjork 1994; Murayama et al. 2014 |
| Spacing improves long-term retention | Meta-analytic, high utility | [[The spacing effect\|Cepeda et al. 2006]] |

The **minimum information principle** itself is a practitioner heuristic (Woźniak, 1999), not a controlled-experiment finding. No study has directly compared atomic vs. overloaded flashcards in an SRS context. The heuristic is well-grounded in the findings above, but the precise grain size of "atomic" is a judgment call, not an empirically determined quantity.

The **anti-patterns and rewriting guidance** are principled extrapolations from the established findings, combined with practitioner consensus. They are well-motivated but should not be cited as if they carry the same evidentiary weight as the testing effect or encoding specificity.

## Relationship to the rest of the project

This folder sits between the mechanisms ([[The testing effect]], [[The spacing effect]], [[How memory works]]) and the operating system ([[Spaced repetition systems]]). The mechanisms establish *why* retrieval, spacing, and difficulty work; the SRS operationalises the scheduling; this folder addresses the third leg — how to make the thing being scheduled actually testable.

The existing SRS note briefly states the minimum-information rules as a list. This folder is the deep treatment those rules draw on, explaining the mechanisms behind each one and providing the diagnostic and rewriting technique.

## Notes in this folder

### Concepts
- [[Cue-dependent recall]] — why the question determines what is retrievable
- [[The minimum information principle]] — Woźniak's atomicity rule, evidence assessment
- [[Interference and cue overload]] — how multi-fact answers cause competition and suppression

### Doctrine
- [[Card formulation anti-patterns]] — the catalogue of failure modes
- [[Rewriting overloaded cards]] — the practical technique for splitting and rewriting

## Sources

- Woźniak, P. (1999). *Effective learning: Twenty rules of formulating knowledge*. SuperMemo Guru.
- Tulving, E., & Thomson, D. M. (1973). Encoding specificity and retrieval processes in episodic memory. *Psychological Review, 80*(5), 352–373.
- Nielsen, M. A. (2018). *Augmenting Long-term Memory*.
- [[Pan & Rickard 2018]] — testing-effect specificity.
- Roediger & Karpicke 2006 — testing effect.
- Watkins, O. C., & Watkins, M. J. (1975). Cue overload. *JEP: Human Learning and Memory, 1*(4), 442–452.
- Anderson, M. C., Bjork, R. A., & Bjork, E. L. (1994). Retrieval-induced forgetting. *JEP: Learning, Memory, and Cognition, 20*(5), 1063–1087.
