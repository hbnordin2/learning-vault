---
type: guide
---

# Flashcards and Anki, explained

Most of what you understand today will be hard to recall in a month unless you practise recalling it. Two findings from memory research do most of the work against that. Recalling something from memory strengthens it far more than reading it again ([[The testing effect]]). And recall practice spread out over days and weeks beats the same amount crammed into one sitting ([[The spacing effect]]). Flashcards put both into practice: each card asks you to recall one thing, and a scheduler shows it again just before you would forget it.

## What Anki is

Anki is a free flashcard program that does the scheduling. Each day it shows the cards that are due. You answer from memory, turn the card over, and say how it went. A card you got right comes back later, after a few days, then weeks, then months. A card you missed comes back soon. Five to fifteen minutes a day keeps hundreds of cards fresh.

Anki runs on the laptop (free), on Android as AnkiDroid (free) and on iPhone as AnkiMobile (a one-off purchase). A free AnkiWeb account keeps them all in step, so you can review on the phone cards that were made on the laptop.

## How cards get made here

The vault makes cards only for things you have shown you understand. Making a card for something you have only read locks in a sentence you cannot really use, and turns your daily review into a chore of half-understood prompts. [[Spaced repetition systems]] has the reasoning.

So cards come from a tutoring conversation:

1. You ask the agent on the laptop, "Help me really understand <topic>", or use TUTOR mode in a chat app ([[Study modes for chat apps]]).
2. You explain the idea; it asks questions until you can explain the gaps yourself.
3. It proposes a few cards, one fact each, for the facts you got right in your own words. You approve, change or drop each one.
4. On the laptop, the agent writes the approved cards at the bottom of the note they came from. From a chat app, save the session record and ask the agent to "add the flashcards from my chat session"; it shows you the cards again before writing them.

## Getting the cards into Anki

The cards sit in the note as short blocks starting with `START` and ending with `END`. To send them to Anki:

1. Open Anki on the laptop.
2. In Obsidian on the laptop, click the Obsidian_to_Anki icon in the left-hand ribbon. It sends every new or changed card to Anki.
3. Anki syncs them to AnkiWeb, and the phone picks them up the next time it syncs.

After a card has been sent, an `ID` line appears under it in the note. Leave that line alone: it is how the plugin knows which Anki card the block belongs to. If you change a card's wording in the note and click the icon again, Anki updates the card and keeps its schedule.

## Reviewing

Review wherever is easiest: Anki on the phone, or out loud with the agent on the laptop ("review my cards"). The agent shows each question, waits for your answer, grades it and records the grade in Anki. That needs Anki open on the laptop.

When a card keeps failing, the card is usually the problem, not your memory. Ask the agent to "check my flashcards on <topic>": it looks for cards that ask for too much at once or whose question does not really point to the answer, and suggests better ones. [[Card formulation anti-patterns]] lists the usual faults.
