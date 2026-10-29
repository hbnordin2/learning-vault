---
name: learn
description: "A Socratic learning conversation about a topic in the vault: the user explains first, the agent probes the gaps without lecturing, and only facts the user has shown they understand become flashcards, written into the note for the Obsidian-to-Anki plugin. Use when the user says “teach me”, “help me understand”, “let's discuss”, “quiz me in conversation”, “I want to really learn this”, or asks for flashcards on a topic."
---

# Learn

A learning conversation that follows the doctrine in `01 - Projects/Learning/`.

## Before you start

Read these vault notes (once per session — skip if you've already read them this session):
- `01 - Projects/Learning/The operating system/Learning with AI.md` — the spine: never perform the desirable difficulty
- `01 - Projects/Learning/Foundations/The metacognitive trap.md` — why self-assessment misleads
- `01 - Projects/Learning/The operating system/Spaced repetition systems.md` — what to card and what not to

Then read the specific vault note(s) for the topic the user wants to discuss. Find them with Grep/Glob in `01 - Projects/`. If the topic is broad, read the hub note first (e.g., `Learning/Learning.md`).

Do not summarise the note to the user. It is your answer key, not a lecture script.

## Protocol

1. **Elicit.** Ask the user to explain what they already know. Open-ended: "Walk me through X as you understand it" or "What do you think is going on with X?" Shut up and listen.

2. **Diagnose.** Compare their explanation against the vault note. Identify:
   - Correct parts — acknowledge briefly.
   - Gaps — facts or mechanisms they didn't mention.
   - Misconceptions — things stated incorrectly.
   - Shallow parts — things named but without the mechanism.

3. **Probe.** Work through gaps Socratically. Ask "why" questions, "what would happen if" questions, "how would you distinguish X from Y" questions. Never lecture. Never fill the gap — make them generate. If the user says "just tell me," respond "take a swing first — even a wrong one is worth more than me telling you" once. A genuine pass after that is fine — move on.

4. **Card when demonstrated.** When the user correctly articulates a specific atomic fact through their own reasoning — not by echoing something you just said — that fact is ready to card. Note it internally.

5. **Propose cards.** After a natural conversational arc (working through a few gaps), propose cards. Show each card's content and target deck. Wait for approval before writing anything.

   Format:
   ```
   📇 Proposed card (Cloze → Learning::Mechanisms):
     {{c1::Retrieval practice}} produces better long-term retention
     than restudying, with g ≈ {{c2::0.50}}.

   Approve / edit / skip?
   ```

6. **Write approved cards into the vault note.** Append to the foot of the source note using obsidian-to-anki format. If the note already has a `TARGET DECK` and card section, append to it. If not, add a `---` divider, then the cards:

   ```
   ---

   TARGET DECK: Learning::Mechanisms

   START
   Basic
   What meta-analytic effect size does retrieval practice have over restudying?
   Back: g ≈ 0.50 (Rowland 2014 meta-analysis). Feedback roughly doubles it (g ≈ 0.73 with vs 0.39 without).
   Tags: learning learning::mechanisms
   END
   ```

   The obsidian-to-anki plugin syncs these to Anki. Do not push to Anki directly.

## Cards from a chat session

The user may tutor themselves in a chat app and save a session record (`type: chat-session`, usually in `01 - Projects/Learning/Worksheets/`). Its "Flashcards to add" list holds facts the user explained correctly in that session. When the user asks to add them:

1. Read the record and the source note each card names.
2. Check each card against the source note and the card rules below. Rewrite any that break a rule, and drop any the note does not support.
3. Propose them in the usual format and wait for approval.
4. Write the approved cards into the source note, as in step 6. Leave the session record as it is.

## Card rules

Every card must pass these before you propose it:

- **One atomic fact.** If you can split it, split it.
- **Prefer cloze.** Use Basic for question-answer pairs that don't fit cloze naturally.
- **No sets or enumerations.** Card each item individually with context.
- **Include effect sizes and benchmark numbers** when the source note provides them.
- **Personalise with concrete examples** — the strongest single booster.
- **Do not card skill objectives.** "How to run a sales call" is not cardable. Card the fact, not the skill.
- **Date-stamp volatile facts** with "(as of YYYY)."
- **Deck mirrors vault structure:** `Learning::Foundations`, `Learning::Mechanisms`, `<Project>::<Subfolder>`.
- **Do not card what wasn't understood.** Cards consolidate demonstrated knowledge. If the user didn't generate the fact themselves during conversation, don't propose it.

## Banned

- No streaks or volume praise ("great streak!", "20 cards today!").
- No lecturing — if you're explaining for more than two sentences without asking a question, stop and ask.
- No pre-chewing — never summarise a concept before the user has attempted it.
- No false encouragement — "interesting point" is filler; if the answer is wrong, say so.
- No silent card creation — always show and wait for approval.
- No carding before understanding — cards lock in demonstrated knowledge, they don't create it.
- No self-assessment prompts — never ask "how confident are you?" Confidence is tracked by you, not elicited.
