---
type: doctrine
tags: [learning, learning/flashcard-formulation]
---

# Rewriting overloaded cards

The practical technique for taking a card whose answer carries more than its question asks for and converting it into a set of atomic cards that each test one retrievable fact. This is the applied form of [[The minimum information principle]], grounded in [[Cue-dependent recall]] and [[Interference and cue overload]].

## Step 1: Diagnose the overload

Read the question. Cover the answer. Produce a response from memory. Then reveal the answer and compare. Everything in the answer that the response did not cover falls into one of two categories:

- **Genuinely forgotten** — the question did ask for it and memory failed. This is a normal retrieval failure; the card is working as intended.
- **Never cued** — the question did not ask for it. The material is present in the answer but the question does not prompt it. This is the overload. No amount of review will fix it, because the question will never cue it.

The diagnostic question: *could a person who fully understands this topic produce the entire answer from the question alone, with nothing extra and nothing missing?* If not, the card is overloaded.

## Step 2: Identify the atomic facts

Parse the answer into its constituent claims. Each independent proposition is a candidate for its own card. A proposition is atomic when it answers exactly one question and does not depend on another proposition to be meaningful (or, if it does depend, the dependency is in the question's context, not hidden in the answer).

Example — the original card:
> Q: What is a business model?
> A: How a company creates, delivers, and captures value. Create = what problem you solve and for whom. Deliver = how you get the solution to the customer. Capture = how you turn delivered value into money. A business plan executes a known model; a startup is a hypothesis about whether a model can exist.

The atomic facts:
1. A business model is how a company creates, delivers, and captures value.
2. "Create" means what problem is solved and for whom.
3. "Deliver" means how the solution reaches the customer.
4. "Capture" means how delivered value becomes revenue.
5. A business plan executes a known model; a startup is a hypothesis about whether a model can exist.

Five facts, five potential cards. The original card had one question and five facts — a cue-to-target ratio of 1:5.

## Step 3: Write a question that fully specifies each answer

Each atomic fact needs a question precise enough that the answer is the only correct response. The question must:

- **Contain enough context to be standalone.** A card encountered in a mixed-deck review, weeks from now, with no surrounding notes visible, must be self-interpretable. "What does 'create' mean?" is ambiguous; "In the create-deliver-capture model, what does 'create' refer to?" is specific.

- **Cue exactly what the answer contains.** If the answer is "what problem is solved and for whom," the question must specifically ask for that scope — not more, not less.

- **Admit exactly one correct answer.** If the question could be answered in multiple defensible ways, it is under-specified. Add constraints until only the intended answer survives.

## Step 4: Choose the format

Three formats, matched to the structure of the knowledge:

**Basic (front/back)** — for self-contained facts where the question and answer are independent of any surrounding text. "What does NRR stand for?" → "Net revenue retention." Clean, fast to review, and unambiguous.

**Cloze deletion** — for facts that are meaningful only in context. When a fact is one piece of a larger structure (e.g., one component of a three-part framework), cloze preserves the structure while testing one piece:

> In Rachleff's value hypothesis, the three things to prove are what you're building, {{c1::who is desperate for it}}, and what business model delivers it.

Cloze is Woźniak's recommended default (Rule 5) because it decomposes multi-fact material naturally: one cloze per fact, context stays visible.

**Reversed cards** — for bidirectional associations. If the learner needs to go from term to definition AND from definition to term (or from metric to meaning and from meaning to metric), two cards are needed. "What is NRR?" and "Which metric measures whether the installed customer base grows on its own?" test the same knowledge from opposite directions and should both exist.

## Step 5: Validate by recall test

After rewriting, run each new card through the diagnostic from Step 1: read the question, cover the answer, produce a response. If the response matches the answer with nothing extra and nothing missing, the card is well-formed. If there is still trailing material, the card is not yet atomic — split again.

## What to do with relational knowledge

Some knowledge is inherently relational — the point is the connection between two concepts, not a fact about either one in isolation. Examples: "How does venture selection relate to product-market fit?" or "Why can't SEO drive a growth loop during category creation?"

The relational fact is the causal or structural link between them. Card it as the relationship, not as a property of either concept:

> Q: In category creation, why can't SEO drive a growth loop?
> A: SEO captures existing search demand. In category creation, no one is searching for the thing yet.

The answer is the causal link (no existing demand → nothing to capture). The two concepts (SEO loops, category creation) appear in the question as context. If additional facts about SEO loops or category creation are worth knowing, they get their own cards — they do not trail onto this one.

## What to do with examples and citations

Concrete examples and source attributions are valuable context but are often the trailing material that inflates answers. Two options:

- **If the example is the point** (the card is testing whether the learner can produce the example), put it in the answer and ask for it: "What example did Vohra use to demonstrate segment-first PMF strategy?" → "Superhuman: went from 22% to 32% Ellis score by finding the right user segment, not by changing the product."

- **If the example is illustration, not the tested fact**, move it to the question side as context, or drop it from the card entirely. The example is not being tested; including it in the answer just inflates it. The learner will encounter the example in the source note; the card is not the note.

Citations and attributions (e.g., "Reforge, 2018" or "Rachleff's version") follow the same logic. If the attribution is what is being tested ("Who coined the value hypothesis?"), it belongs in the answer. If it is decorative provenance, it does not belong on the card at all — it belongs in the source note.

## Where this comes up

- [[The minimum information principle]] — the principle this technique implements
- [[Cue-dependent recall]] — why the question must fully specify the answer
- [[Interference and cue overload]] — why multi-fact answers degrade recall
- [[Card formulation anti-patterns]] — the failure modes this fixes
- [[Spaced repetition systems]] — the system these cards feed into
- [[Flashcard formulation]] — the hub note

## Sources

- Woźniak, P. (1999). *Effective learning: Twenty rules of formulating knowledge*. SuperMemo Guru. — the source of the atomicity principle and cloze-as-default recommendation.
- Nielsen, M. A. (2018). *Augmenting Long-term Memory*. — extended practical treatment of card writing, including the one-question-one-answer principle and the "what would a thoughtful answer look like" test.
