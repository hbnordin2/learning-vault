---
type: guide
---

# Talking to your notes in ChatGPT or Claude

ChatGPT and the Claude app can read your notes and discuss them with you, by text or out loud. They do it through a **project**: a workspace in the app that holds a set of files and a standing set of instructions. Every conversation started inside the project can see those files and follows those instructions. You set it up once, and then you open the project whenever you want to talk to your notes.

The apps change their menus often. The steps below were right in October 2026. If a menu has moved, ask the app itself where it went ("how do I add files to a project?").

## What a project gives you

- **Your notes as background.** The app answers from your notes and can say which note an answer came from, instead of answering from general knowledge.
- **Study modes.** The instructions in [[Study modes for chat apps]] turn the project into a tutor, a quiz partner or a paper-reading partner on request.
- **Voice.** Start a voice conversation from inside the project and it uses the same notes and instructions.

A chat app can only **read** the vault. It cannot change notes, make podcasts or send flashcards to Anki. At the end of a tutoring or quiz session it gives you a short record to save into Obsidian, so the agent on the laptop can use it later (see "Saving what you did" below).

## ChatGPT

1. Open ChatGPT (on the website or the desktop app is easiest for setup) and create a project: **Projects → New project**. Call it "Vault".
2. Open the project's settings and paste the instructions from [[Study modes for chat apps]] into **Instructions**.
3. Add your notes. There are two ways, and you can use both:
   - **Upload files.** Projects take a limited number of files, so ask the agent on the laptop: "Make chat upload files for the Learning folder" (or any folder). It joins the notes into one or a few large files in `build/chat-upload/`. Upload those files into the project. Do this again when the notes have changed a lot.
   - **Connect GitHub.** In ChatGPT's settings, under apps or connectors, connect GitHub and allow it to see your vault repository. ChatGPT then reads the current notes directly when you ask about them. This is not available on every plan or in every part of ChatGPT, so if you cannot find it, use uploads.
4. **Voice.** On the phone, open the project, then tap the voice button. As of August 2026, voice conversations started inside a project use its files and instructions. OpenAI is rolling this out gradually, so on some accounts voice may not see the files yet. If voice does not seem to know your notes, ask it "which files can you see?"

## Claude

1. Open Claude (claude.ai or the app) and create a project: **Projects → New project**. Call it "Vault".
2. Paste the instructions from [[Study modes for chat apps]] into the project's **instructions**.
3. Add your notes: in the project's knowledge section, choose **+ → GitHub**, pick the vault repository, and choose the folders to include (for example `01 - Projects/Learning` and `03 - Resources/Papers`). A private repository may first need you to install the Claude GitHub app and allow it to see that repository; Claude shows a link when this is needed. The project keeps the files in step with GitHub. The upload files from step 3 above also work here.
4. **Voice.** In the Claude app on the phone, open the project and tap the voice button.

## Saving what you did

When a tutoring or quiz session ends (or when you say "wrap up"), the app gives you a **session record**: what you got wrong, what you were sure of but got wrong, what you got right, and any flashcards it suggests. To keep it:

1. Copy the record. On the phone, long-press the message and choose Copy.
2. In Obsidian, make a new note in `01 - Projects/Learning/Worksheets/` called something like "Testing effect — chat quiz 2026-11-02", and paste.

The next time you ask the agent on the laptop for a worksheet on that topic, it reads these records and asks again about what you missed, in new words. To send the suggested flashcards to Anki, tell the agent: "add the flashcards from my chat quiz on the testing effect". [[Flashcards and Anki, explained]] explains what happens next.

## Which app to use when

Use the chat apps for talking: a tutoring session on the sofa, a spoken quiz while walking, or going through a paper out loud. Use the agent on the laptop for making things: paper notes, podcasts, worksheets, flashcards. Use Obsidian for reading, writing your own notes, and clickable worksheets.
