# Instructions for the agent

This folder is an Obsidian vault kept in a private GitHub repository. It holds the owner's notes, a research-based corpus on how people learn, and tools that turn notes and papers into podcasts, worksheets and flashcards. Codex, Cursor and Claude Code all read this file.

The owner is a researcher, not a programmer. Run commands yourself instead of asking the owner to run them. Explain what you did in plain words, and say what it cost when a paid service was used. Ask before anything that spends money, deletes files, or sends something outside the vault.

## What the owner can ask for

The skills in `.agents/skills/` do the work. Pick the skill from what the owner asks for. The owner does not need to name it.

The guides for the owner are in `00 - Start here/`. When the owner asks how to use the vault from ChatGPT or the Claude app, by voice, or with Anki, point them to the right guide there and help them through it.

| When the owner asks to… | Use |
|---|---|
| read, write up, or explain a research paper | `paper` |
| get a podcast or "something to listen to" about a topic, note or paper | `podcast` (and `paper` for a paper) |
| get a worksheet, quiz or practice questions, or says a worksheet is finished | `worksheet` |
| really understand a topic, discuss it, make flashcards, or add the flashcards from a saved chat session | `learn` |
| review Anki cards that are due | `review` |
| check or fix existing flashcards | `audit-cards` |
| tidy or restructure notes | `audit-notes` |
| get feedback on the clarity of a draft | `analyze-writing` |
| write or rewrite text in plain English | `simple-english` |
| read a web page | `defuddle` |
| write Obsidian syntax (callouts, embeds, properties, Bases, Canvas) | `obsidian-markdown`, `obsidian-bases`, `json-canvas` |
| make files to upload to a ChatGPT or Claude project | run `uv run .tools/setup/bundle_for_chat.py "<folder>"` and tell the owner to upload everything in `build/chat-upload/` |

When the owner asks what the vault can do, answer from this table in plain sentences, with one example request for each.

## Folders

| Folder | What goes there |
|---|---|
| `00 - Start here/` | Plain guides for the owner: using the vault, chat apps and voice, study modes, Anki |
| `00 - Inbox/` | Quick captures and daily notes, not organised yet |
| `01 - Projects/` | Long-running topics. Each project folder has a hub note with the same name as the folder |
| `01 - Projects/Learning/` | The learning-science corpus. The skills read it as their reference. Start from `Learning.md` |
| `01 - Projects/Learning/Podcasts/` | Transcript notes of generated podcast episodes |
| `01 - Projects/Learning/Worksheets/` | Worksheets, including the filled-in ones that record what the owner got right and wrong |
| `02 - Areas/` | Ongoing responsibilities (teaching, supervision, committees) |
| `03 - Resources/Papers/` | Plain-English rewrites of research papers made by the `paper` skill |
| `04 - Archive/` | Finished or dormant material |
| `99 - Attachments/` | Images, and media files that git ignores |
| `.claude/skills/` | A copy of `.agents/skills/` for Claude Code. Never edit it directly |
| `examples/` | Sample outputs (two paper notes and a worksheet) showing what the skills produce |
| `.tools/` | `learncast` (voices podcasts), `media-feed` (publishes media to the phone), `worksheets` (checks quiz syntax), `setup` (installs plugins) |

## Rules

1. **Note and folder names must not contain `: * ? " < > | \`.** Windows and phones cannot store those characters, so a note with one in its name breaks syncing. Use an em dash (`—`) where a colon would go, and curly quotes (`“ ”`) instead of straight ones. Note titles must be specific enough to be unique across the whole vault, because Obsidian links notes by title.
2. **Commit and push every change.** GitHub is how notes reach the phone and the other laptops. Pull before starting work (`git pull --rebase`), then `git add`, `git commit`, `git push` when done. If a push is rejected, pull and try again. Never force-push.
3. **Audio and video never go in git.** Publish them with `.tools/media-feed/publish.py` (see `.tools/media-feed/README.md`) and link the episode URL from the note.
4. **Secrets never go in the vault.** API keys and the feed settings live in `~/.config/learning-vault/.env` on each computer. Never print a key back to the owner, and never write the feed URL or `MEDIA_PREFIX` into a note other than as the episode links the publish script prints.
5. **Flashcards come only from the `learn` skill.** Do not add `TARGET DECK` or `START`/`END` card blocks while writing other notes. Never write, copy or change a `<!--ID:-->` line: the Obsidian_to_Anki plugin owns them, and a wrong ID corrupts the Anki schedule.
6. **Notes use a neutral voice.** A note is reference prose: no "I", no "you", and no trace of the conversation that produced it. The guides in `00 - Start here/` are the exception: they speak to the owner directly.
7. **Write plainly.** Full sentences, the real term for each thing, defined at first use, with a concrete example. No bullet-point fragments in place of reasoning.
8. **Stay faithful to sources.** Keep each claim at the strength its source gives it. Check numbers, quotes and citations against the source itself, never from memory. When the owner's own field is involved, the owner's expertise outranks yours: ask.

## Editing skills

Edit skills only in `.agents/skills/`. Codex and Cursor read that folder. Claude Code reads `.claude/skills/`, which is a copy. After any change to a skill, run `uv run .tools/setup/sync_skills.py` and commit both folders together. `uv run .tools/setup/sync_skills.py --check` says whether they match.

## Running the tools

Python tools run with [uv](https://docs.astral.sh/uv/), which installs what each one needs:

- Podcasts: `cd .tools/learncast && uv run learncast synth build/<slug>.txt --title "<Title>"`
- Media feed: `uv run .tools/media-feed/publish.py "<file>" --title "<Title>" --about "<one line>"`
- Worksheet check: `uv run .tools/worksheets/check.py "<worksheet>.md"`

These commands need network access (ElevenLabs, the storage bucket, GitHub). If the sandbox blocks them, ask the owner to approve the command, or see "Network access" in `SETUP.md`.

If setup has not been done on this computer (no `~/.config/learning-vault/.env`, or `uv` is missing), follow `SETUP.md`.
