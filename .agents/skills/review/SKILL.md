---
name: review
description: Run a spaced-repetition review of the user's due Anki cards through AnkiConnect: show each question, let the user answer from memory, grade the answer, and record the grade in Anki. Use when the user says “review my cards”, “do my Anki”, “what's due”, or “flashcard review”. Needs Anki desktop open with the AnkiConnect add-on.
---

# /review

Review due cards from Anki. You grade, not the user.

Anki desktop must be open with the AnkiConnect add-on (code `2055492159`) installed. If `localhost:8765` does not answer, ask the user to open Anki. On Windows, use `curl.exe` (not the PowerShell `curl` alias) or Python for the requests below.

## Before you start

Read `01 - Projects/Learning/Foundations/The metacognitive trap.md` if you haven't this session — it grounds why you grade (not the user) and why felt fluency is not trusted.

## Protocol

1. **Check what's due.** Query AnkiConnect for due cards:
   ```bash
   curl -s http://localhost:8765 -X POST -d '{"action": "findCards", "version": 6, "params": {"query": "is:due"}}'
   ```
   Report the count. If nothing is due, say so and offer to discuss a topic instead (`/learn`).

2. **Fetch card details.** For each due card, get its content:
   ```bash
   curl -s http://localhost:8765 -X POST -d '{"action": "cardsInfo", "version": 6, "params": {"cards": [CARD_ID]}}'
   ```

3. **Present the front only.** Show the question. Do not show the back. Do not hint.

4. **Wait for the attempt.** The user answers from memory — spoken or typed. Do not prompt or help.

5. **Reveal and grade.** Show the back. Compare the user's attempt against it. Grade:
   - **Good (3):** core fact(s) correct, wording may differ.
   - **Again (1):** wrong, missing the core, or "I don't know."
   - **Hard (2):** only when unambiguously hesitant but correct.
   - **Easy (4):** only when instant and complete.

6. **Explain the delta.** What they got right, what they missed or got wrong. Two sentences max. Do not re-teach the whole concept — if they need deeper work, suggest `/learn` on that topic.

7. **Rate in Anki.** Push the grade:
   ```bash
   curl -s http://localhost:8765 -X POST -d '{"action": "answerCards", "version": 6, "params": {"answers": [{"cardId": CARD_ID, "ease": GRADE}]}}'
   ```

8. **Next card.** Repeat until done or the user stops.

9. **Summary.** At the end:
   - Cards reviewed, correct count.
   - Patterns in the misses (e.g., "three misses were all from Learning::Mechanisms — might be worth a `/learn` session").
   - No streak praise. No volume praise.

## Optional: Socratic follow-up

After a correct answer, optionally probe deeper — one question max to maintain pace: "Why does that work?" / "What breaks if you remove that condition?" Never tells, only asks.

## Metacognitive mirror

If there were 5+ cards in the session, end with a calibration note: where the user was confident but wrong, where they were hesitant but right. This trains the sense of what you actually know vs what you feel you know.

## Banned

- No self-assessment — you grade, the user does not pick the rating.
- No streaks or volume praise.
- No re-teaching during review — keep deltas to two sentences; suggest `/learn` for deeper work.
- No hints before the attempt.
- No showing the back before the user has tried.
