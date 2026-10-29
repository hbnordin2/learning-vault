"""OpenAI text-to-speech (gpt-4o-mini-tts).

Cheap (~$0.015/min audio), good quality, expressive via `instructions`, single
API key. Voices are OpenAI presets (ash, coral, ...). Works against any
OpenAI-compatible base URL — set LEARNCAST_TTS_BASE_URL to route through a proxy that exposes /audio/speech.
"""

from __future__ import annotations

import os
from pathlib import Path

import httpx

from .base import register

MODEL = os.environ.get("OPENAI_TTS_MODEL", "gpt-4o-mini-tts")
BASE_URL = os.environ.get("LEARNCAST_TTS_BASE_URL", "https://api.openai.com/v1")
# Light steer so the explainer sounds warm and the questioner sounds curious.
INSTRUCTIONS = os.environ.get(
    "OPENAI_TTS_INSTRUCTIONS",
    "Conversational, warm, natural pacing as if chatting on a walk.",
)


class OpenAITTS:
    name = "openai"

    def check_key(self) -> None:
        if not os.environ.get("OPENAI_API_KEY"):
            raise RuntimeError(
                "OPENAI_API_KEY is not set. Add it to ~/.config/learning-vault/.env"
            )

    def synth(
        self,
        text: str,
        voice_id: str,
        out: Path,
        prev_text: str | None = None,
        next_text: str | None = None,
    ) -> Path:
        out = out.with_suffix(".mp3")
        resp = httpx.post(
            f"{BASE_URL.rstrip('/')}/audio/speech",
            headers={"Authorization": f"Bearer {os.environ['OPENAI_API_KEY']}"},
            json={
                "model": MODEL,
                "voice": voice_id,
                "input": text,
                "instructions": INSTRUCTIONS,
                "response_format": "mp3",
            },
            timeout=120,
        )
        resp.raise_for_status()
        out.write_bytes(resp.content)
        return out


@register("openai")
def _factory() -> OpenAITTS:
    return OpenAITTS()
