---
type: concept
tags: [learning, learning/mechanism]
---

# Cognitive load and worked examples

Cognitive Load Theory (Sweller, 1988) starts from the encoding bottleneck in [[How memory works]]: learning is limited by working memory, which holds only about four chunks at once (Cowan, 2001), so instruction should be designed to spend that scarce capacity on building schemas rather than on avoidable overhead. It is one of the better-validated bodies of work in education. Its robust core is the engineering prescriptions, not the internal load-accounting, which was over-claimed and has been partly walked back.

## The three loads (now effectively two)

- **Intrinsic load** — the inherent difficulty of the material for this learner, driven by element interactivity: how many elements must be held and processed at the same time because they interact. Learning isolated vocabulary is low interactivity (one item at a time); balancing a chemical equation or reading a cap table is high (many interacting parts at once). Fixed for a given learner and task, and it falls as schemas are built, because a schema turns many interacting elements into one chunk.
- **Extraneous load** — overhead imposed by poor presentation: hunting across a page to connect a diagram to its caption, decoding clumsy wording. This is the load to minimise; it is wasted capacity.
- **Germane load** — capacity devoted to building the schema. Originally treated as a third, separate load; see the critique below.

## The worked-example effect

For a novice, studying a worked example (a fully solved problem) produces more learning than solving an equivalent problem unaided, because unguided problem-solving burns working memory on means-ends search instead of schema construction (Sweller & Cooper, 1985). The meta-analysis (Barbieri et al., 2023) puts the effect at **g ≈ 0.48** on mathematics performance. Two caveats: the meta-analysis showed publication-bias asymmetry (the true effect is plausibly smaller), and adding self-explanation prompts to the examples reduced the effect in this dataset, echoing the [[Elaboration and self-explanation|provision-vs-generation]] tension. The effect is also strongest for near problems; it does not produce far [[Transfer of learning|transfer]] on its own.

## The expertise-reversal effect

This is the main boundary, and the reason "worked examples are good" is not a universal rule. Kalyuga et al. (2003): instructional support that helps novices — worked examples, integrated diagrams, extra explanation — becomes useless or harmful as expertise grows. Once the schema is in place, the provided guidance is redundant information that must be reconciled against what is already known, which adds extraneous load. This is a genuine crossover interaction, replicated into classrooms. It motivates guidance fading: full worked example, then completion problems (finishing a partly-worked solution), then solving unaided, as competence increases. The matching prescription on the learner side is the surmountability caveat in [[Desirable difficulties]]: difficulty should track expertise.

## The falsifiability critique

The serious objection (de Jong, 2010) is that germane load was unfalsifiable: if reducing load helped, that confirmed the theory; if increasing load helped, it got relabelled "germane" — so no result could disconfirm it. And the dominant measure is a single subjective rating (the Paas mental-effort scale) that yields one global number and does not separate the three load types the theory is built on. The critique largely succeeded: Sweller (2019) abandoned the three-independent-loads model for a two-load account (intrinsic + extraneous), with germane redefined as merely the capacity allocated to intrinsic processing rather than a separate additive load. The field conceded the point.

The verdict is therefore split: the design rules (use worked examples for novices, fade guidance with expertise, avoid split-attention and redundancy) are robust and replicated; the load bookkeeping is weakly measured and was over-stated.

## How to use it

- When learning something genuinely new with high element interactivity — a new ad platform's mechanics, an unfamiliar contract structure, a new codebase pattern — start from worked examples, templates, and annotated solutions, not a blank page. Blank-page struggle is for when the schema is already in place.
- Fade the scaffolding with improvement: study a full example, then complete partial ones, then solve cold. Worked examples stop helping once the steps can be generated; past that point they slow the learner (expertise reversal).
- Cut extraneous load in materials: keep a diagram and its labels together, drop decorative detail, write plainly.

## Sources

- Sweller, J. (1988). Cognitive load during problem solving: Effects on learning. *Cognitive Science, 12*(2), 257–285.
- Sweller et al. 2011 — *Cognitive Load Theory* (the consolidated treatment). Sweller, van Merriënboer & Paas (1998; "20 years later," 2019, *Educational Psychology Review*) — the move to a two-load model.
- Sweller, J., & Cooper, G. A. (1985). The use of worked examples as a substitute for problem solving. *Cognition and Instruction, 2*(1), 59–89.
- Barbieri, C. A., et al. (2023). A meta-analysis of the worked examples effect on mathematics performance. *Educational Psychology Review, 35*, 11. — g ≈ 0.48, with publication-bias caveat.
- Kalyuga, S., Ayres, P., Chandler, P., & Sweller, J. (2003). The expertise reversal effect. *Educational Psychologist, 38*(1), 23–31.
- de Jong, T. (2010). Cognitive load theory, educational research, and instructional design: Some food for thought. *Instructional Science, 38*(2), 105–134. — the falsifiability/measurement critique.
