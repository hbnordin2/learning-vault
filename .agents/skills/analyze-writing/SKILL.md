---
name: analyze-writing
description: Diagnose a piece of writing against the reading-comprehension research in the vault (cognitive load, coherence, given-before-new, concreteness, assumed knowledge, signposting) and propose concrete rewrites. Use when the user asks for feedback on a draft, a paper, a grant section, a lecture handout or any prose, or asks “is this clear?” or “how can I make this easier to read?”.
---

# /analyze-writing

Analyze prose against the research-grounded comprehension principles in `01 - Projects/Learning/Writing/`.

## Before you start

Read these vault notes (once per session — skip if already read):
- `01 - Projects/Learning/Writing/Writing for comprehension.md` — the hub: Kintsch's three levels, the writer's core tradeoff
- `01 - Projects/Learning/Writing/Structure and cohesion/Coherence in text.md` — local/global coherence, the reverse coherence effect
- `01 - Projects/Learning/Writing/The reader/Cognitive load in prose.md` — extraneous load, sentence structure, given-new contract
- `01 - Projects/Learning/Writing/Style/Concrete language and seductive details.md` — concreteness advantage, the seductive details trap
- `01 - Projects/Learning/Writing/The reader/Prior knowledge and comprehension.md` — schema theory, reader knowledge dependence
- `01 - Projects/Learning/Writing/Structure and cohesion/Signaling and advance organizers.md` — headings, structural cues

Then identify the text to analyze. Context cues:
- If the user names a file or note, read that file.
- If invoked after writing or editing, analyze the recently written/edited text.
- If the user pastes text directly, analyze the pasted text.
- If ambiguous, ask.

## Analysis dimensions

Work through each dimension. For every issue found, quote the specific passage and name the research principle.

### 1. Cognitive load

Does the text impose extraneous processing demands?

- **Syntactic complexity.** Garden-path sentences, deeply nested clauses, passives that obscure the agent. Flag sentences where the reader must re-parse to understand.
- **Ambiguous reference.** Pronouns without clear antecedents, or antecedents so far back the reader must search.
- **Unnecessary jargon.** Terminology the target reader would need to stop and decode. Distinguish domain terms the reader should know from terms used for their own sake.
- **Sentence length.** Flag individual sentences above ~35 words. Note the average. The API finding: >90% comprehension at 14 words; <10% at 43. The practical range is 15-20 average.

### 2. Coherence

Are ideas connected at both levels?

- **Local.** Do adjacent sentences share referential overlap (repeated nouns, consistent subjects)? Are connectives present where causal or contrastive relationships exist? Are there jumps where the reader must infer a link the writer did not supply?
- **Global.** Is there a discernible macrostructure? Do paragraphs lead with a claim? Is the relationship between sections signaled? Can the reader reconstruct the argument's skeleton from headings and topic sentences alone?
- **Audience calibration.** If readers are high-knowledge, some coherence gaps may be appropriate — the reverse coherence effect (McNamara et al., 1996) shows that expert readers sometimes comprehend better with less coherent text because gaps force inference. State the audience assumption.

### 3. Concrete vs abstract

Is the text grounded?

- Are key claims illustrated with concrete examples?
- Are any examples vivid but structurally irrelevant to the point being made? These are **seductive details** — they divert mental-model construction toward the example rather than the target concept (Harp & Mayer, 1998).
- Is understanding at risk of binding to a single example? Multiple structurally-varied examples aid transfer; a single rich example can impair it (Fyfe et al., 2015).

### 4. Given-new ordering

Does each sentence place known ("given") information before unknown ("new") information?

- Flag sentences where the new information precedes the given, forcing the reader to construct a backward-bridging inference (Clark & Haviland, 1977). These are individually small costs that compound across a passage.

### 5. Schema assumptions

Does the text assume knowledge the reader may lack?

- Are terms defined on first use, or does the text assume the reader already holds the relevant schema?
- Is there enough scaffolding for the intended reader? (Bransford & Johnson, 1972: context must be activated *before* encoding, not after.)
- Is there over-explanation that a knowledgeable reader would find redundant? If the target audience already holds the schema, excessive scaffolding reduces engagement — the reverse coherence effect applied to explanation density.

### 6. Signaling

Is the structure visible?

- Are headings present and informative (not just decorative)?
- Do paragraphs lead with topic sentences that announce the paragraph's claim?
- Are advance organizers used where the reader is entering unfamiliar territory? (Note: the evidence for advance organizers is mixed — Luiten et al. 1980 found small effects; the confident practitioner advice overstates what the evidence supports. Flag when useful, don't prescribe universally.)

## Protocol

1. **Read the text.** Identify or infer the target audience. State the assumption: "I'm reading this as if the target reader is [X]."

2. **Analyze.** Work through each dimension. For each issue:
   - Quote the passage (short — enough to identify it).
   - Name the dimension and the mechanism (e.g., "Extraneous cognitive load — garden-path clause").
   - Propose a concrete rewrite of that passage.

3. **Report.** Organize findings by impact:
   - **Structural** — macrostructure, coherence, schema gaps. Hardest to fix, largest impact on whether the reader builds a situation model.
   - **Sentence-level** — cognitive load, given-new, ambiguous reference. Easier to fix, cumulative impact.
   - **Detail-level** — concrete language, seductive details, signaling. Polish layer.

   For each finding, show the original, the mechanism, and the proposed rewrite.

4. **Offer to apply.** If the text is a file in the vault, offer to apply the fixes. Show a diff-style summary of what would change before editing.

## Rules

- Always cite the specific research principle behind each diagnosis. The Writing corpus notes are the reference — link to them by name.
- Calibrate to the target audience. Text for domain experts should be analyzed differently from text for novices. State the assumption and adjust.
- Distinguish structural issues (reorganize, add scaffolding) from sentence-level issues (rewrite a clause). Do not flatten them into one undifferentiated list.
- Do not impose a house style. The analysis is about comprehension mechanisms, not personal preferences about sentence length, tone, or voice.
- If a passage is genuinely fine — clear, coherent, appropriately concrete — say so. Not every paragraph needs a finding.

## Banned

- No readability scores (Flesch-Kincaid, Dale-Chall) as a diagnosis — the corpus explains why these are unreliable predictors of comprehension. Do not compute or report them.
- No style-guide platitudes ("vary your sentence length," "use active voice") without grounding in the research. If the mechanism is not in the corpus, do not invoke it.
- No rewriting without quoting the original and naming the mechanism that justifies the change.
- No analysis of aesthetic, rhetorical, or literary quality — this skill is about comprehension, not taste.
- No prescribing advance organizers as a universal fix — the evidence is mixed.
