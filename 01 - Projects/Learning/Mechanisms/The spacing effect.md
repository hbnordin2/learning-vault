---
type: concept
tags: [learning, learning/mechanism]
---

# The spacing effect

Distributing study across time produces far better long-term retention than massing the same amount of study together (cramming), for equal total time. It is the second of the two *high-utility* techniques in Dunlosky et al. (2013), and one of the oldest findings in psychology — Ebbinghaus noted it in 1885. The mechanism is the storage/retrieval asymmetry: a gap lets retrieval strength decay, so the next retrieval is more effortful and builds more storage strength ([[How memory works]], [[Desirable difficulties]]).

## Effect size, and the optimal-gap function

The meta-analytic base is large — Cepeda et al. (2006) synthesised 317 experiments — and spaced practice reliably outperforms massed, with effect sizes commonly around **d ≈ 0.4–0.5**. The more actionable result is not the flat effect but the **function relating the optimal gap to how long the material needs to be retained** (Cepeda et al., 2008):

- The gap between study sessions that maximises retention *grows* as the target retention interval grows.
- As a *proportion* of the retention interval, the optimal gap *shrinks* — roughly **10–20%** of the delay for short horizons, falling to **~5–10%** for a one-year horizon.

In practice: to still know something in a month, review it across several days; to still know it in a year, review at roughly three-to-four-week intervals. The function is broad and forgiving — any substantial spacing outperforms massing, and erring towards longer gaps is low-cost. There is no single optimal interval.

## Expanding vs. equal intervals

A widespread belief (the intuition behind Leitner-box and older flashcard schemes) holds that *expanding* intervals — each gap longer than the last — are optimal. The evidence does not support the strong version. **Karpicke & Roediger (2007)** found expanding schedules win only on *immediate* tests; on *delayed* tests, **equal-interval spacing matches or beats expanding.** What matters is that the **first retrieval is sufficiently delayed** to be effortful, not the expansion pattern. Modern spaced-repetition algorithms do expand intervals, but for a different and valid reason: to *minimise total reviews* at a target retention, not because expansion itself improves memory over equal spacing.

## Why cramming feels effective and is not

Massed study raises performance on a test taken minutes later, which is why it feels productive — the fluency is real and immediate. But that performance is retrieval strength, not durable learning, and it collapses over days. This is the [[The metacognitive trap|metacognitive trap]] in a clear form: the strategy that feels most efficient in the moment is among the worst for retention.

## Lab vs. real world

Field support is strong: spacing improves retention in real classrooms and applied training, though field effects are smaller and noisier than tightly-controlled lab ones (Kang 2016 reviews the educational evidence). The effect also interacts with sleep — gaps that span a night gain consolidation for free (see [[Sleep and consolidation]]).

## How to use it

- Spread any topic across multiple days with at least one night's sleep between exposures, rather than one long session.
- Let a [[Spaced repetition systems|spaced-repetition system]] (Anki with FSRS) schedule the gaps — it is the spacing effect, automated, for the atomic-fact layer.
- The exact interval does not need to be precise; the function is forgiving. A reasonable default is expanding-ish gaps of roughly a day, a few days, a week, a few weeks.


## Sources

- Cepeda et al. 2006 — meta-analysis, 317 experiments; spaced beats massed.
- Cepeda, N. J., Vul, E., Rohrer, D., Wixted, J. T., & Pashler, H. (2008). Spacing effects in learning: A temporal ridgeline of optimal retention. *Psychological Science, 19*(11), 1095–1102. — the optimal-gap function.
- Karpicke, J. D., & Roediger, H. L. (2007). Expanding retrieval practice promotes short-term retention, but equally spaced retrieval enhances long-term retention. *JEP: LMC, 33*(4), 704–719.
- Kang 2016 — spacing in educational settings. Dunlosky et al. 2013 — high-utility rating.
