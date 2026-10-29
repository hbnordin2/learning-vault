# Learning vault

A starter kit for an Obsidian vault that an AI agent can work in. It turns research papers into plain-English notes, turns notes into two-host podcasts for the phone, makes practice worksheets that remember what you got wrong, and writes flashcards only for what you have shown you understand. Underneath sits a corpus of about 70 notes on the research into how people learn and remember, which the agent uses as its reference for designing all of these.

It runs on free or low-cost pieces. GitHub syncs the notes between laptops and phone, so there is no Obsidian Sync subscription. The agent is whichever one you already use: Codex, ChatGPT or Claude Code. The only paid parts are optional: a voice service for podcasts (ElevenLabs or OpenAI) and a few cents of storage to get the podcasts onto the phone.

## Set it up

1. Install Codex (the ChatGPT desktop app or the `codex` command) and sign in.
2. Start Codex in your Documents folder, or any folder you like.
3. Paste this prompt:

```text
Set up my learning vault. Download the instructions from
https://raw.githubusercontent.com/hbnordin2/learning-vault/main/SETUP.md
and follow them step by step. I am not a programmer: run the commands
yourself, ask me one question at a time, tell me in plain words what each
step is for, and never ask me to paste a password or API key into the chat.
```

When Codex asks for permission to run a command or reach the internet, approve it: setup needs to download programs and talk to GitHub. The agent asks what kind of phone you have, whether you want podcasts and flashcards, and walks you through the accounts it cannot create for you. It makes your own copy of this repository as a **private** repository, so your notes stay yours. This template stays public; your copy does not.

For a second laptop, paste the same prompt there and say the vault already exists.

## What you can ask for

Ask in plain words, in Codex started inside the vault folder. You do not need to know the skill names.

| Ask for | What happens |
|---|---|
| "Write up this paper" (with a PDF, DOI or link) | A plain-English rewrite in `03 - Resources/Papers/` that keeps every finding at its original strength, in a fixed order: what they asked, what they did, what they found, how strong the evidence is |
| "Make me a podcast about the spacing effect" | A 45 to 60 minute two-host episode built for listening while doing something else. It circles one idea from several angles, so drifting off for a few minutes costs nothing. It appears in the phone's podcast app |
| "Make a podcast of this paper" | A 15 to 20 minute episode that walks through every finding |
| "Give me a worksheet on this" | Clickable multiple-choice questions with explanations, recall prompts with hidden answers, and re-tests of what earlier worksheets show you missed |
| "Help me really understand this" | A conversation where you explain first and the agent asks questions. Flashcards are written only for what you got right yourself |
| "Review my cards" | The agent shows each due Anki card, you answer, and it grades and records the result |
| "Is this draft clear?" | Feedback on a draft, grounded in reading-comprehension research, with proposed rewrites |
| "Tidy these notes" | Suggestions to split, retitle and link notes, applied only after you agree |

## How the pieces fit together

```
          laptop (macOS / Windows)                         phone
 ┌────────────────────────────────────┐          ┌─────────────────────┐
 │ Obsidian  ── Git plugin ──┐        │          │ Obsidian            │
 │ Codex / Claude Code       ├─ git ──┼── GitHub ┼── GitSync           │
 │   reads AGENTS.md + skills│        │ (private)│                     │
 │   runs .tools/learncast ──┼─ ElevenLabs       │ Podcast app ◄─ feed │
 │   runs .tools/media-feed ─┼────────────────────────────── S3 / R2   │
 │ Anki ◄─ Obsidian_to_Anki  ├─ AnkiWeb ─────────┼── AnkiDroid / Mobile│
 └────────────────────────────────────┘          └─────────────────────┘
```

- **Notes** are Markdown files. Every device keeps a full copy and syncs it through your private GitHub repository. Every change is a commit, so any earlier version of any note can be recovered.
- **Skills** (`.agents/skills/`) are instruction files the agent loads when a request matches. Each one holds a method (how to rewrite a paper, how to structure a podcast) and points at the notes in `01 - Projects/Learning/` that justify it.
- **The learning corpus** (`01 - Projects/Learning/`) covers memory, retrieval practice, spacing, worked examples, feedback, motivation, note-making, flashcard design and writing for comprehension, with the evidence and its limits for each. Start at `Learning.md`, or read `How to learn.md` as one continuous essay.
- **Tools** (`.tools/`): `learncast` voices podcast transcripts, `media-feed` publishes audio and video to a private podcast feed, `worksheets/check.py` checks quiz syntax, and `setup/` installs the Obsidian plugins.
- **Media** never goes in git. It goes to a storage bucket under a long random folder name, which a podcast app subscribes to.
- **Keys** live in `~/.config/learning-vault/.env` on each computer, never in the vault.

## Rules the agent follows

`AGENTS.md` holds them. The ones that matter most to you: file names avoid `: * ? " < > | \` because Windows and phones cannot store them; every change is committed and pushed so the phone sees it; the agent asks before spending money or deleting anything; and flashcards are made only in a `learn` conversation, never as a side effect of writing notes.

## Costs

| Part | Cost |
|---|---|
| GitHub, Obsidian, GitSync, Anki on computers, AnkiDroid | Free |
| AnkiMobile (iPhone) | One-off purchase |
| ElevenLabs voices | A monthly plan. A 60-minute episode uses about 26,000 credits. See elevenlabs.io/pricing |
| OpenAI voices (alternative) | Pay per use, through an OpenAI API account |
| Podcast storage | Amazon S3: well under US$1 a month. Cloudflare R2: free up to 10 GB |
| Codex | Included in ChatGPT plans that include Codex |

## Using it with other agents

Codex and ChatGPT read skills from `.agents/skills/` and instructions from `AGENTS.md`. Claude Code reads `CLAUDE.md`, which points at `AGENTS.md`; run `uv run .tools/setup/copy_skills_for_claude.py` to give it the skills. Any other agent that reads `AGENTS.md` can follow the same files.

## Credits

`simple-english` is by AminBlg, and `defuddle`, `obsidian-markdown`, `obsidian-bases` and `json-canvas` are from Steph Ango's obsidian-skills, all under the MIT licence (see the licence files in `.agents/skills/`). The Obsidian plugins are by their authors: Git by Vinzent03, Quiz Block by olliecheng, Obsidian_to_Anki by Pseudonium.
