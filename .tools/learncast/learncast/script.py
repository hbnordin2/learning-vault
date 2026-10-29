"""The dialogue script: the bridge between content and audio.

A transcript is a list of (speaker, text) turns where speaker is HOST_A or
HOST_B. Two ways to get one:

1. PROVIDED — Claude (in the loop) writes the transcript directly and the tool
   just synthesizes it. This is the primary path: best context, no per-call
   LLM cost, no longform/Gemini lock. See `parse_transcript`.

2. GENERATED — for standalone/batch runs, call an OpenAI-compatible LLM
   (OpenRouter, OpenAI, ...) to write the transcript from source
   text. See `generate_transcript`.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

from .config import DEFAULT_PAUSE_SECONDS, SPEAKER_A, SPEAKER_B, SPEAKER_PAUSE, Settings
from .content import Source

_SPEAKER_LINE = re.compile(r"^\s*(HOST_A|HOST_B)\s*:\s*(.*)$", re.I)
_PAUSE_LINE = re.compile(r"^\s*\[\s*pause(?:\s+([0-9]*\.?[0-9]+))?\s*\]\s*$", re.I)
_CANON = {"host_a": SPEAKER_A, "host_b": SPEAKER_B}


@dataclass
class Turn:
    speaker: str  # SPEAKER_A | SPEAKER_B | SPEAKER_PAUSE
    text: str  # spoken words, or (for a pause) the duration in seconds


def parse_transcript(raw: str) -> list[Turn]:
    """Parse `HOST_A:`/`HOST_B:` line format into turns.

    Lines without a speaker prefix are appended to the current turn, so a
    speaker can span multiple lines. Blank lines and `#` comments are ignored.
    """
    turns: list[Turn] = []
    for line in raw.splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        p = _PAUSE_LINE.match(line)
        if p:
            turns.append(Turn(speaker=SPEAKER_PAUSE, text=p.group(1) or str(DEFAULT_PAUSE_SECONDS)))
            continue
        m = _SPEAKER_LINE.match(line)
        if m:
            speaker = _CANON[m.group(1).lower()]
            turns.append(Turn(speaker=speaker, text=m.group(2).strip()))
        elif turns and turns[-1].speaker != SPEAKER_PAUSE:
            turns[-1].text = f"{turns[-1].text} {line.strip()}".strip()
    if not turns:
        raise ValueError(
            "No HOST_A:/HOST_B: turns found. Transcript must use that line format."
        )
    return turns


def transcript_to_text(turns: list[Turn]) -> str:
    lines = []
    for t in turns:
        if t.speaker == SPEAKER_PAUSE:
            lines.append(f"[PAUSE {t.text}]")
        else:
            lines.append(f"{t.speaker}: {t.text}")
    return "\n".join(lines)


def word_count(turns: list[Turn]) -> int:
    return sum(len(t.text.split()) for t in turns if t.speaker != SPEAKER_PAUSE)


# --- optional LLM generation (standalone path) -------------------------------


def build_prompt(source: Source, minutes: int, preset: str) -> list[dict]:
    target_words = minutes * 150  # ~150 spoken words/min
    system = (
        "You write two-host educational podcast scripts designed for second-screen "
        "listening — the listener is cooking, walking, or otherwise occupied and "
        "WILL zone out for stretches. HOST_A is the explainer; HOST_B is the curious "
        "questioner who asks for examples, probes assumptions, and requests "
        "re-explanation. Pick ONE core insight from the source material and explore "
        "it from multiple angles — do not try to cover the whole topic. Return to "
        "the central idea every 90–120 seconds so a listener who tunes back in can "
        "re-enter without backtracking. Each 2-minute stretch should be self-contained. "
        "Repetition across angles IS the structure — restate the idea in different "
        "words, through different examples, from different domains. Natural spoken "
        "rhythm, contractions, the occasional 'right,' or 'so—'. No stage directions, "
        "no markdown. Output ONLY lines of the form 'HOST_A: ...' and 'HOST_B: ...', "
        "alternating naturally. " + preset
    )
    if source.text.strip():
        user = (
            f"Source material to teach (~{minutes} min, ~{target_words} words):\n\n"
            f"{source.text[:24000]}"
        )
    else:
        user = (
            f"Topic to teach (~{minutes} min, ~{target_words} words): "
            f"{source.title}\nUse your own knowledge; be accurate and concrete."
        )
    return [
        {"role": "system", "content": system},
        {"role": "user", "content": user},
    ]


def generate_transcript(source: Source, minutes: int, preset: str, s: Settings) -> str:
    """Call an OpenAI-compatible chat endpoint. Works with OpenRouter, OpenAI
    or any compatible gateway — only the base URL, key, and model name change."""
    import os

    import httpx

    key = (
        os.environ.get("LEARNCAST_LLM_API_KEY")
        or os.environ.get("OPENROUTER_API_KEY")
        or os.environ.get("OPENAI_API_KEY")
    )
    if not key:
        raise RuntimeError(
            "No LLM key for standalone script-gen. Set LEARNCAST_LLM_API_KEY "
            "(or OPENROUTER_API_KEY). Or let Claude write the transcript and "
            "pass it with --transcript."
        )
    resp = httpx.post(
        f"{s.llm_base_url.rstrip('/')}/chat/completions",
        headers={"Authorization": f"Bearer {key}"},
        json={
            "model": s.llm_model,
            "messages": build_prompt(source, minutes, preset),
            "temperature": 0.8,
        },
        timeout=180,
    )
    resp.raise_for_status()
    return resp.json()["choices"][0]["message"]["content"]


def read_transcript_file(path_str: str) -> list[Turn]:
    return parse_transcript(Path(path_str).expanduser().read_text())
