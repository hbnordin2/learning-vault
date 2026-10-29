---
type: concept
tags: [learning, learning/flashcard-formulation]
---

# Interference and cue overload

When multiple items are associated with the same retrieval cue, recall of any one item is impaired. The items compete at retrieval, and more competitors means lower recall probability for each. In flashcard terms: the more facts packed behind a single question, the less reliably any individual fact is recalled. This is the second mechanism (alongside [[Cue-dependent recall|cue-dependent recall]]) that explains why overloaded cards fail.

## Cue overload

Watkins (1979) formalised the **cue-overload principle**: a retrieval cue becomes less effective as more items are associated with it. This is not a function of memory capacity — the items are stored — but of discrimination at retrieval. When the cue activates many candidates, the system must select among them, and selection is noisy. Watkins and Watkins (1975) demonstrated the effect as a buildup of proactive inhibition: as more items were paired with the same cue, recall of the most recent item declined systematically.

For a flashcard whose answer contains five facts, the question is one cue mapped to five targets. Each review strengthens the association between the question and whichever facts the learner happens to retrieve first, but the others are left competing. Over repeated reviews, the first-retrieved facts become dominant, and the remaining facts become harder to access — an instance of the rich-get-richer dynamic in cue-target associations.

## Retrieval-induced forgetting

Anderson, Bjork and Bjork (1994) showed that successfully retrieving one item associated with a cue can **actively suppress** recall of the other items sharing that cue. This is retrieval-induced forgetting (RIF). The mechanism is inhibitory: the memory system suppresses competitors to resolve the competition, and that suppression persists.

Applied to an overloaded flashcard: the learner retrieves the primary fact the question asks for, which actively inhibits retrieval of the trailing facts. The trailing material does not merely sit passively uncued — it is suppressed by the act of retrieving the thing the question did cue. This is worse than "not tested"; it is actively disadvantaged by the card's own structure.

The effect is moderate in size (d ≈ 0.35 in meta-analyses — Murayama et al., 2014) but reliable, and it is largest when retrieval of the practised item is successful, which is exactly when a learner would mark the card "Good" and move on — unaware that the trailing facts have been suppressed.

## Proactive and retroactive interference

The classical interference framework (see Anderson, 2003, for review) describes two directions:

- **Proactive interference**: earlier-learned associations to a cue impair recall of later-learned associations. A learner who has already memorised facts 1–3 attached to a question will have more difficulty encoding fact 4 on the same card, because the existing associations pre-empt it.
- **Retroactive interference**: newly learned associations impair recall of older ones. Adding a new fact to a card's answer can degrade recall of facts previously learned from the same card.

Both operate on the same mechanism — competition at retrieval — and both predict that adding more material to a single card's answer is not just wasteful but actively destructive to the existing memories attached to that question.

## What this means for card design

The interference findings converge on a single prescription: one cue should map to one target. When a question maps to multiple facts:

- The facts compete, lowering recall of each ([[The minimum information principle|minimum information principle]]).
- The first-retrieved fact suppresses the others (retrieval-induced forgetting).
- Adding facts later degrades recall of facts already learned (retroactive interference).
- Facts learned early resist displacement by new facts (proactive interference).

The fix is structural: each fact gets its own question, so each retrieval cue has exactly one target. This eliminates cue overload, removes the conditions for retrieval-induced forgetting within a card, and prevents inter-fact interference. See [[Rewriting overloaded cards]] for the practical technique.

## Evidence tier

- **Cue overload**: established by experiment, replicated across paradigms (Watkins, 1979; Watkins & Watkins, 1975). Solid.
- **Retrieval-induced forgetting**: meta-analytically confirmed, d ≈ 0.35, with identified boundary conditions (Murayama et al., 2014; Storm & Levy, 2012). Robust but debated at the mechanism level (inhibition vs. competition).
- **Proactive/retroactive interference**: among the oldest findings in memory research (Underwood, 1957; Postman, 1961), replicated extensively. Not controversial.
- **Application to flashcard answer overloading**: principled extrapolation. The interference effects are established in paired-associate and list-learning paradigms that structurally resemble flashcards. No study has directly tested "overloaded vs. atomic flashcards" in an SRS context, but the structural match between paired-associate tasks and flashcard review is close enough that the extrapolation is well-motivated.

## Where this comes up

- [[Cue-dependent recall]] — the complementary mechanism: the question determines what is cued, and only cued material is tested
- [[The minimum information principle]] — the practitioner rule these findings ground
- [[Card formulation anti-patterns]] — enumeration cards and overloaded answers as specific instances
- [[How memory works]] — retrieval-strength competition under the two-strength model
- [[Flashcard formulation]] — the hub note

## Sources

- Watkins, O. C., & Watkins, M. J. (1975). Buildup of proactive inhibition as a cue-overload effect. *JEP: Human Learning and Memory, 1*(4), 442–452.
- Watkins, M. J. (1979). Engrams as cuegrams and forgetting as cue overload: A cueing approach to the structure of memory. In C. R. Puff (Ed.), *Memory Organization and Structure* (pp. 347–372). Academic Press.
- Anderson, M. C., Bjork, R. A., & Bjork, E. L. (1994). Remembering can cause forgetting: Retrieval dynamics in long-term memory. *JEP: Learning, Memory, and Cognition, 20*(5), 1063–1087. — retrieval-induced forgetting.
- Anderson, M. C. (2003). Rethinking interference theory: Executive control and the mechanisms of forgetting. *Journal of Memory and Language, 49*(4), 415–445.
- Murayama, K., Miyatsu, T., Buchli, D., & Storm, B. C. (2014). Forgetting as a consequence of retrieval: A meta-analytic review of retrieval-induced forgetting. *Psychological Bulletin, 140*(5), 1383–1409. — meta-analysis, d ≈ 0.35.
- Underwood, B. J. (1957). Interference and forgetting. *Psychological Review, 64*(1), 49–60.
