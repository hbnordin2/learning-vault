"""Deliver the finished episode into the Obsidian vault.

Writes the MP3 into the attachments folder and a companion markdown note that
embeds the audio (Obsidian plays `![[file.mp3]]` inline) and carries the full
transcript for reference and linking.
"""

from __future__ import annotations

import re
import shutil
from datetime import date
from pathlib import Path

from .config import VAULT, VAULT_AUDIO_DIR, VAULT_NOTE_DIR
from .script import Turn


def _slug(title: str) -> str:
    s = re.sub(r"[^\w\s-]", "", title).strip().lower()
    return re.sub(r"[\s_-]+", "-", s)[:60] or "episode"


def deliver(
    mp3: Path,
    title: str,
    turns: list[Turn],
    origin: str,
    minutes: float,
    on_date: date,
) -> tuple[Path, Path]:
    """Copy audio + write note into the vault. Returns (audio_path, note_path)."""
    VAULT_AUDIO_DIR.mkdir(parents=True, exist_ok=True)
    VAULT_NOTE_DIR.mkdir(parents=True, exist_ok=True)

    stamp = on_date.isoformat()
    base = f"{_slug(title)}-{stamp}"
    audio_dest = VAULT_AUDIO_DIR / f"{base}.mp3"
    shutil.copy2(mp3, audio_dest)

    transcript = "\n\n".join(f"**{t.speaker}:** {t.text}" for t in turns)
    note = f"""---
type: podcast
status: generated
date: {stamp}
tags: [learning, podcast]
---

# 🎧 {title}

> [!info] {minutes:.0f} min · generated {stamp}
> Source — {origin}

![[{audio_dest.name}]]

## Transcript

{transcript}
"""
    note_dest = VAULT_NOTE_DIR / f"{base}.md"
    note_dest.write_text(note)
    return audio_dest, note_dest


def rel_to_vault(path: Path) -> str:
    try:
        return str(path.relative_to(VAULT))
    except ValueError:
        return str(path)
