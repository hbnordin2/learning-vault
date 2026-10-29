# learncast

learncast turns a transcript into a two-host podcast episode. The agent (Codex, Claude Code or another coding agent) writes the transcript from the vault's notes. learncast sends each line to a text-to-speech service, joins the pieces with ffmpeg, and saves the MP3 and a transcript note in the vault.

The transcript design lives in the `podcast` skill (`.agents/skills/podcast/SKILL.md`), and the evidence behind it in `01 - Projects/Learning/The operating system/Learning from passive audio.md`. learncast only does the voicing.

## Setup

Install [uv](https://docs.astral.sh/uv/) and ffmpeg (`brew install uv ffmpeg` on macOS, `winget install astral-sh.uv Gyan.FFmpeg` on Windows). Then, from this folder:

```bash
uv sync
uv run learncast providers
```

`providers` shows which voice keys it can see. Keys go in `~/.config/learning-vault/.env`, outside the vault, so they never reach git. `.env.example` lists every setting.

## Use

```bash
uv run learncast synth build/my-episode.txt --title "Spacing effect"
```

This writes `99 - Attachments/Podcasts/<slug>-<date>.mp3` and a note in `01 - Projects/Learning/Podcasts/` that embeds the audio and the transcript. `--no-vault` keeps the MP3 in `build/` only. `-p openai` or `-p gemini` picks another voice provider for one run.

`uv run learncast generate --note "Spacing effect" --length 15` writes the script with an LLM API instead of the agent. It needs the `LEARNCAST_LLM_*` settings. The agent-written path gives better episodes, because the agent follows the podcast skill.

## Transcript format

Each line starts with a speaker, `HOST_A` (explains) or `HOST_B` (asks, guesses, restates). `[PAUSE 0.5]` on its own line adds half a second of silence.

```
HOST_A: So here is the strange thing about cramming.
HOST_B: It works, though. I crammed my way through second-year stats.
HOST_A: It works for Friday's exam. Now guess how much of it was left a month later.
```

`examples/net-revenue-retention.txt` is a full example.

## Voices

`uv run learncast voices` shows the voice for each host and provider. The IDs are in `learncast/config.py`. To change an ElevenLabs voice, copy a voice ID from the ElevenLabs voice library and replace the one in `HOST_A` or `HOST_B`.
