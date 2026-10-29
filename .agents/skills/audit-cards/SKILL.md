---
name: audit-cards
description: Check flashcards in the vault against the flashcard-formulation rubric (one fact per card, no lists behind one prompt, the question cues the whole answer) and propose fixes, which are applied only after approval. Use when the user asks to check, clean up, fix or improve their flashcards or Anki cards.
---

# /audit-cards

Review and fix flashcards in the vault, scoring each against the research-grounded rubric in `01 - Projects/Learning/Flashcard formulation/`.

## Before you start

Read these vault notes (once per session — skip if already read):
- `01 - Projects/Learning/Flashcard formulation/Flashcard formulation.md` — the hub: evidence floor and principle
- `01 - Projects/Learning/Flashcard formulation/Card formulation anti-patterns.md` — the catalogue of failure modes
- `01 - Projects/Learning/Flashcard formulation/Rewriting overloaded cards.md` — the rewriting technique

Then determine which flashcards to review. Context cues:
- If the user names a specific file, topic, or deck, find cards in those files (grep for `START`/`END` blocks in the relevant markdown).
- If invoked after writing or editing a note that has cards, review cards in that note.
- If invoked without clear context, scan for all cards in the vault: `rg -l "^START$" --type md` inside `01 - Projects/`.
- Never review the entire vault unprompted — ask the user to scope it if ambiguous.

## Rubric

Score each card against these six checks. Each is derived from the formulation corpus and maps to a specific mechanism:

1. **No un-cued payload.** Read only the front. List what it demands. Anything on the back beyond that list is trailing material — the question does not cue it, so it is not being tested. *(Cue-dependent recall: encoding specificity, transfer-appropriate processing.)*

2. **One retrieval target.** One cue → one fact to generate. Two independent facts behind one question means two cards. *(Interference and cue overload: cue overload degrades recall per item; retrieval-induced forgetting actively suppresses competitors.)*

3. **The question constrains its answer.** A person who knows the material should produce the intended answer, not a different valid one. No double-barreled questions ("what is X, and why does Y?"). *(Encoding specificity: ambiguous cues create unstable grading.)*

4. **The front forces generation, not recognition.** No yes/no questions, no "is X true?" — these allow recognition to substitute for recall. *(Testing effect: recall tests outperform recognition tests because they demand more retrieval effort.)*

5. **No enumerations or sets behind one prompt.** "What are the N things?" is worst-case cue overload — the items share a single cue and compete. Use cloze or split into discrete cards. *(Minimum information principle, cue overload.)*

6. **Citations and context off the retrieval path.** "(Reforge, 2018)", "also called NDR", "Horowitz: PMF is not permanent" — fine as context you do not expect to recall. A problem when they masquerade as part of the answer the learner should produce. If worth remembering, they get their own card. *(Testing effect: unprompted material is reread, not retrieved.)*

## Protocol

1. **Extract cards.** Parse the TARGET DECK, START/END blocks, and card content (type, front, back, tags, ID) from the file(s).

2. **Diagnose each card.** For each card:
   - Read the front. List exactly what it asks for.
   - Read the back. Identify every discrete piece of information.
   - For each piece, classify: **cued** (the front asks for it) or **trailing** (the front does not ask for it).
   - Check against all six rubric points.
   - Assign severity:
     - 🔴 **Heavy overload** — multiple independent trailing facts, or a major anti-pattern (enumeration, essay-answer, binary).
     - 🟡 **Good core + trailing payload** — correct core answer, but un-cued material hangs off the back.
     - 🟢 **Fine** — minor trim at most.

3. **Report.** Present the review as a summary table:

   | Card (front, truncated) | Issues | Severity |
   |---|---|---|

   Then for each 🔴 and 🟡 card, show:
   - The specific trailing material (quoted from the back).
   - Which rubric point(s) it violates.
   - The proposed fix: a tightened version of the existing card, plus any new cards needed from the split. Show the exact START/END block content for each.

4. **Apply fixes.** After the user approves (or edits):
   - **In-place trims** (removing trailing material from an existing card): edit the card's Back content directly in the vault markdown. Preserve the `<!--ID: -->` line so the obsidian-to-anki plugin updates the existing Anki card rather than creating a duplicate.
   - **Splits** (one card becomes multiple): keep the original card (trimmed) with its existing ID. Append the new cards as new START/END blocks adjacent to the original — they get **no** `<!--ID:-->` line (the plugin assigns one on next sync). Match the original card's TARGET DECK and Tags.
   - Never touch the `<!--ID: -->` value itself — do not fabricate, copy, or modify IDs.

5. **Summary.** Report: total cards reviewed, cards that passed (🟢), in-place trims applied, splits created, and any cross-card patterns worth noting (e.g., near-duplicate fronts that risk cue interference between cards).

## Rules

- Always show proposed changes before applying them. Wait for approval.
- Never delete a card — trim or split, do not remove. The user decided these facts matter; the fix is better structure, not deletion.
- Preserve `<!--ID: -->` lines on existing cards — fabricating or copying IDs corrupts SRS scheduling.
- New cards from splits get no ID line — the obsidian-to-anki plugin assigns them on sync.
- Tags on new cards should match the original card's tags.
- When in doubt about whether trailing material is "cued" or not, err on the side of diagnosing it — false positives (flagging something that is cued) are cheaper than missed overload.
- Flag cross-card interference: two cards with very similar fronts competing for the same cue.

## Banned

- No silent edits — always show and wait for approval.
- No fabricating Anki IDs.
- No removing cards entirely.
- No lecturing about flashcard theory — diagnose, propose, fix. The corpus is the reference if the user wants to understand why.
- No creating cards for material that was not already carded — this skill audits existing cards, it does not add new knowledge. Card creation is `/learn`.
