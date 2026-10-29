---
name: audit-notes
description: Check vault notes against the note-making research (one idea per note, titles that name the idea, notes that stand alone, useful links) and propose restructuring, applied only after approval. Use when the user asks to tidy, review, restructure, split or improve their notes.
---

# /audit-notes

Review vault notes against the research-grounded principles in `01 - Projects/Learning/Note-making/`.

## Before you start

Read these vault notes (once per session — skip if already read):
- `01 - Projects/Learning/Note-making/Note-making.md` — the hub: atomicity, concept-orientation, linking
- `01 - Projects/Learning/Note-making/The Zettelkasten.md` — what "atomic" means, source separation
- `01 - Projects/Learning/Note-making/Evergreen notes.md` — concept-oriented titles, developmental trajectory, titles as APIs
- `01 - Projects/Learning/Note-making/The evidence base for structured note-making.md` — what is supported, what is not

Then determine which notes to review. Context cues:
- If the user names a specific file, folder, or topic, review those notes.
- If invoked after writing or editing a note, review that note.
- If ambiguous, ask.

## Rubric

Score each note against these five checks. Each is derived from the note-making corpus.

1. **Atomicity.** Does the note address one concept or claim? A note is atomic when it is self-contained and irreducible — not merely short. Signs of non-atomicity: multiple H2 sections that could each stand alone as independent notes; a title that joins two ideas with "and"; content that covers distinct concepts with no structural dependency between them. *(Zettelkasten: one idea per card. Matuschak: each note focuses on a single idea.)*

   **Exception:** Hub notes (type: moc) are intentionally non-atomic — they serve as navigation and orientation. Do not flag hubs for atomicity.

2. **Concept-orientation.** Is the note organized around an idea, not a source? A concept-oriented note accumulates findings from multiple sources under one claim; a source-oriented note summarizes one paper or book. Signs: title names an author or paper rather than an idea; content reads as a book summary rather than a claim with evidence. *(Matuschak: "Organizing by source means your new thoughts on the concept don't combine with the old ones to form a stronger whole.")*

3. **Title as API.** Does the title name a concept or claim that is findable and linkable? Good: "Cue overload degrades recall." Bad: "Notes on Watkins & Watkins 1975." Borderline: single-word titles ("Retention") that are too vague to distinguish from other notes on similar topics. The title should be a complete phrase that communicates what the note is about without opening it. *(Matuschak: "Evergreen note titles are like APIs.")*

4. **Self-containment.** Can the note be understood without reading other notes? Are key terms defined or linked on first use? Does the note have enough context to stand alone when encountered months later? Signs of non-self-containment: "as discussed above," references to "the framework" without specifying which, terms used without definition or link. *(Zettelkasten: cards designed to be independently understandable. Atomicity means self-contained, not short.)*

5. **Linking.** Are there explicit cross-references to related notes in the vault? Are the links substantive — connecting ideas — rather than decorative? Are there obvious connections to existing vault notes that are missing? *(Both traditions: dense linking forces thinking about how ideas relate and creates navigable structure.)*

## Protocol

1. **Read the note(s).** Identify the note type (concept, doctrine, moc, etc.) from frontmatter if present.

2. **Diagnose each note.** For each note:
   - State the note's apparent scope: what concept or claim does it address?
   - Check against all five rubric points.
   - Assign severity:
     - 🔴 **Structural** — the note is not atomic (covers multiple independent concepts), or is source-oriented rather than concept-oriented. Requires splitting or reframing.
     - 🟡 **Moderate** — title could be sharper, self-containment gaps, or missing links. Fixable in place.
     - 🟢 **Fine** — minor improvements at most.

3. **Report.** Present the review as a summary table:

   | Note (title) | Issues | Severity |
   |---|---|---|

   Then for each 🔴 and 🟡 note, show:
   - The specific issue (quoted from the note where relevant).
   - Which rubric point(s) it violates.
   - The proposed fix: retitle, split, add context, add links. For splits, name the proposed new notes and outline their content.

4. **Apply fixes.** After the user approves (or edits):
   - **In-place edits** (retitles, added links, added context): edit the note directly. If retitling, rename the file and update any `[[links]]` to the old title in other vault files.
   - **Splits** (one note becomes multiple): create new note files in the same folder. Move the relevant content from the original into each new note. Preserve frontmatter conventions (type, tags). Add cross-links between the new notes. If the original had flashcards (TARGET DECK / START-END blocks), move each card to the note whose content it tests — preserve `<!--ID:-->` lines.
   - Never delete a note — split or restructure, but the content must be preserved somewhere.

5. **Summary.** Report: total notes reviewed, notes that passed (🟢), in-place edits applied, splits created, and any vault-level patterns worth noting (e.g., a cluster of source-oriented notes that should be refactored into concept-oriented ones).

## Rules

- Always show proposed changes before applying them. Wait for approval.
- Never delete a note — restructure, split, or refactor. Content must be preserved.
- Hub/MOC notes are intentionally non-atomic. Do not flag them for atomicity.
- When splitting, preserve frontmatter conventions from the original note (type, tags).
- When retitling, check for and update `[[links]]` to the old title in other vault files.
- If a note has flashcards, move each card to the note whose content it tests during splits. Preserve `<!--ID:-->` lines.
- Distinguish structural issues (splitting, reframing) from polish issues (sharpening titles, adding links). Do not flatten them into one list.
- When proposing links, only link to notes that actually exist in the vault. Use Grep/Glob to verify before suggesting.

## Banned

- No silent edits — always show and wait for approval.
- No deleting notes.
- No creating flashcards — that is `/learn`.
- No analyzing writing quality — that is `/analyze-writing`. This skill checks note structure, not prose.
- No imposing a single "correct" note length — atomicity is about self-containment and irreducibility, not brevity.
- No prescribing linking density targets — the corpus does not specify a number; the principle is that obvious connections should be explicit.
- No treating Ahrens' fleeting/literature/permanent taxonomy as canonical — the corpus is clear that this is one interpretation, not Luhmann's vocabulary.
