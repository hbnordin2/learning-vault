---
type: doctrine
tags: [learning, learning/practice]
---

# Learning with AI

How to use an LLM while checking whether learning actually occurs. AI-assisted task performance and subsequent independent capability are different outcomes. The studies below show why the instructional design and the assessment both matter; they do not establish that every AI explanation prevents learning or that every questioning tutor helps.

## The 2-sigma number, corrected

VanLehn's (2011) review reported effects around *d* = 0.79 for human tutoring and 0.76 for intelligent tutoring systems in the comparisons reviewed. These are not universal effects for tutoring, and the older systems were not current generative AI. Neither those averages nor Bloom's historical two-sigma result establishes the benefit of a particular AI tutor. [Review](https://doi.org/10.1080/00461520.2011.611369).

## The evidence is mixed, which is the point

- **Positive result in undergraduate physics:** Kestin et al. (2025) found greater learning gains with their designed AI tutor than with the active-learning class comparison. This tests that intervention and assessment, not all AI tutoring or long-term professional skill.
- **A cost of unguarded assistance in high-school mathematics:** Bastani et al. (2025) found better assisted practice performance but approximately 17% lower subsequent unassisted exam scores in the GPT Base condition than in the no-AI control. A tutor with teacher-informed safeguards largely removed that deficit; it did not establish a positive unassisted-exam benefit. GPT Base was a study interface mimicking ChatGPT, not unrestricted use of the public product.

These studies used different participants, content, systems, comparisons, and assessments. Their contrast supports inspecting how assistance is designed, but does not isolate one design feature as the sole cause. The positive physics trial is [Kestin et al. (2025)](https://doi.org/10.1038/s41598-025-97652-6); the mathematics trial is [Bastani et al. (2025)](https://doi.org/10.1073/pnas.2422633122).

## A possible mechanism of harm

One plausible risk is substitution: if assistance supplies every answer, the learner may receive less retrieval or problem-solving practice. That does not mean “nothing encodes.” [[Cognitive load and worked examples|Worked examples]] demonstrate why provided explanations can be useful, particularly to novices. The practical distinction is whether assistance supports later independent performance. A fluent interaction alone cannot establish that; see [[The metacognitive trap]].

## The rule, and how to apply it

Use the AI for the support currently needed, then check performance without it. The following prompts are applications of guidance, retrieval, and feedback findings, not individually validated AI interventions.

- **Attempt-then-check when there is sufficient prior knowledge.** Produce an answer, obtain feedback, and attempt a related question independently. Bastani's tutor was a package of design choices; that study does not establish this one prompt as the cause of its result.
- **AI as questioner.** “Quiz me on this, ask me why, and check my reasoning.” This requests retrieval and [[Elaboration and self-explanation|self-explanation]]; the prompt alone does not guarantee accurate feedback or better calibration.
- **AI as retrieval-quizzer and card-maker.** Have it generate questions or cloze cards from studied material; do the closed-book retrieval, [[Spaced repetition systems|spaced]]. The AI builds the test; the learner takes it.
- **Gap-finding.** After explaining a concept, ask "where is my explanation wrong, vague, or missing a mechanism?" — turning the AI into a metacognitive mirror.
- **Use guidance when needed.** A novice can request a worked example or an explanation before attempting a related problem. There is no requirement to struggle for an arbitrary period first. Check outputs against reliable source material; see [[Feedback, help, and learning with others]].

## The coding case

**Application to coding, not a finding from the two subject-specific trials:** if the aim is learning a stack, inspect whether a related implementation can later be produced and explained without the model. Use instruction for unfamiliar concepts and review for an attempted implementation. Shipping an AI-assisted feature is a different outcome from demonstrating the ability independently.

## Where this comes up

- [[01 - Projects/Learning/Foundations/Desirable difficulties|Desirable difficulties]] / [[How memory works]] — matching practice to what needs to be learned
- [[The metacognitive trap]] — why perceived fluency requires an independent check
- [[The testing effect]] / [[Elaboration and self-explanation]] — what to make the AI do to the learner
- [[Spaced repetition systems]] — AI as a card and question generator
- [[01 - Projects/Learning/The operating system/The operating system|The operating system]] — AI as a tool across the whole loop

## Sources

- VanLehn 2011 — comparisons involving human tutoring and earlier tutoring systems; not a universal prediction for generative AI.
- Kestin, G., et al. (2025). AI tutoring outperforms in-class active learning: An RCT introducing a novel research-based design in an authentic educational setting. *Scientific Reports, 15*, 17458.
- Bastani, H., et al. (2025). Generative AI without guardrails can harm learning: Evidence from high school mathematics. *PNAS, 122*(26), e2422633122.
- Rozenblit, L., & Keil, F. (2002). The misunderstood limits of folk science: An illusion of explanatory depth. *Cognitive Science, 26*(5), 521–562.
