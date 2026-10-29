---
type: concept
tags: [learning, learning/foundation]
---

# How memory works

The substrate the rest of the project rests on. Durable learning means getting information into long-term memory in a form that can be retrieved later, under cues that will not be the same ones present when it was learned. There are three sub-processes: **encoding** (forming the trace), **storage** (retaining it over time), and **retrieval** (getting it back out). Almost every effective learning technique manipulates one of these, and the counterintuitive findings all come from the gap between how *storage* and *retrieval* actually behave.

## The two-strength model

Bjork & Bjork's **New Theory of Disuse** (Bjork & Bjork, 1992) holds that every item in memory has two independent strengths:

- **Storage strength** — how deeply and durably the item is learned: how well it is interconnected with other knowledge. In the theory, storage strength is *monotonic* — it only ever increases. Storage strength is not lost; well-learned things are never truly erased.
- **Retrieval strength** — how accessible the item is *right now*, given the current cues. This fluctuates: it rises after study or a reminder, and decays with disuse.

What is experienced as "forgetting" is retrieval strength decaying, not storage strength being lost. A phone number that cannot be recalled is not gone; it is currently inaccessible. This is why a forgotten thing relearns far faster than it was first learned — the storage strength is still present.

The asymmetry that organises the project is this: the boost to storage strength from a successful retrieval is larger when retrieval strength is lower. Retrieving something that is hard to access (because time has passed, or the cues are sparse) builds more durable learning than retrieving something that is already easy. Effortful, barely-successful retrieval moves storage strength most.

This single fact unifies the high-utility techniques. [[The spacing effect|Spacing]] works because waiting lets retrieval strength decay, so the next retrieval is harder and builds more storage. [[The testing effect|Retrieval practice]] works because pulling the answer out is a harder, higher-storage-gain operation than reading it again. [[Interleaving]] works because mixing topics keeps any one of them from sitting at high retrieval strength. They are three ways of doing the same thing: forcing retrieval when retrieval strength is low. The umbrella name for the principle is [[Desirable difficulties]].

## Forgetting

Ebbinghaus (1885) plotted the first forgetting curve by relearning lists of nonsense syllables at increasing delays. The shape — a steep initial drop that decelerates — was directly replicated by Murre & Dros (2015), who reran his paradigm and recovered essentially the same curve (a roughly logarithmic/power function, *not* a clean exponential). Two caveats are worth holding:

- The smooth "50% forgotten in an hour, 70% by day two" infographic that circulates online is false precision. The *shape* is real and replicated; the specific percentages are not a constant — they depend on the material, the person, and how well it was encoded. Most online versions graft fabricated numbers onto Ebbinghaus's name.
- Each successful retrieval *flattens* the subsequent curve. Forgetting is not a fixed decay; it is the thing spaced retrieval is designed to counter. The curve gets shallower every time the item is successfully pulled back.

## The encoding bottleneck

The constraint at the front end is working memory: the small number of items that can be held and manipulated at once. New information has to pass through this bottleneck to be encoded, and when the material's [[Cognitive load and worked examples|intrinsic load]] exceeds the bottleneck, encoding fails regardless of effort. Expertise defeats this through **chunking** — storing knowledge in larger meaningful units, so that what was ten items for a novice is one item for an expert (Chase & Simon, 1973; covered in [[Expertise, schemas, and chunking]]). The novice and the expert have the same working-memory capacity; the expert's units are bigger. This is why building the schema first beats memorising the parts.

## What this rules out

The model is the reason the metacognitive cues that feel trustworthy are wrong. Because retrieval strength is what is salient in the moment — how fluently the material comes to mind while it is in front of the learner — *high retrieval strength* (easy now) is reliably mistaken for *high storage strength* (learned durably). Re-reading raises retrieval strength briefly and teaches almost nothing, yet feels like learning. The whole of [[The metacognitive trap]] follows from confusing the two strengths.

## Status

The component effects the model organises — testing, spacing, interleaving, generation — are individually robust and meta-analytically established (see each mechanism note). The two-strength model *itself* is a well-motivated, elegant theoretical framework, not a directly measured quantity: "storage strength is monotonic" is a theoretical commitment, not an observed fact. Treat it as the best available organising story — useful for intuition, not a law with an effect size.

## Where this comes up

- [[Desirable difficulties]] — the principle that follows directly from the storage/retrieval asymmetry
- [[The metacognitive trap]] — why confusing the two strengths leads to studying badly
- [[The testing effect]], [[The spacing effect]], [[Interleaving]] — the three mechanisms the model unifies
- [[Expertise, schemas, and chunking]] — how chunking defeats the encoding bottleneck
- [[Cognitive load and worked examples]] — the working-memory constraint at encoding
- [[Learning]] — project hub

## Sources

- Bjork, R. A., & Bjork, E. L. (1992). A new theory of disuse and an old theory of stimulus fluctuation. In *From Learning Processes to Cognitive Processes* (Vol. 2, pp. 35–67). Erlbaum. — the storage-strength / retrieval-strength model.
- Bjork & Bjork 2011 — *Making Things Hard on Yourself, But in a Good Way*; the accessible statement of the model and desirable difficulties.
- Ebbinghaus, H. (1885). *Über das Gedächtnis* (*Memory: A Contribution to Experimental Psychology*).
- Murre, J. M. J., & Dros, J. (2015). Replication and analysis of Ebbinghaus' forgetting curve. *PLOS ONE, 10*(7), e0120644. — direct replication; shape holds, exact percentages are not canonical.
- Chase & Simon 1973 — chunking and the working-memory bottleneck.
