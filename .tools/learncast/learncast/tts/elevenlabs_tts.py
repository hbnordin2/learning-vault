"""ElevenLabs text-to-speech.

Top-tier quality — the NotebookLM benchmark. Per-character cost (~$5/mo
Starter). Each host is a distinct ElevenLabs voice id (see config.HOST_A/B).
Defaults to the Flash model, which bills at half credits.
"""

from __future__ import annotations

import os
from pathlib import Path

import httpx

from .base import register

MODEL = os.environ.get("ELEVENLABS_MODEL", "eleven_flash_v2_5")
BASE_URL = "https://api.elevenlabs.io/v1"


class ElevenLabsTTS:
    name = "elevenlabs"

    def check_key(self) -> None:
        if not os.environ.get("ELEVENLABS_API_KEY"):
            raise RuntimeError(
                "ELEVENLABS_API_KEY is not set. Add it to "
                "~/.config/learning-vault/.env"
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
        body = {
            "text": text,
            "model_id": MODEL,
            "voice_settings": {"stability": 0.5, "similarity_boost": 0.75},
        }
        # Cross-turn context lets ElevenLabs keep prosody continuous across the
        # many small segments a conversation is cut into.
        if prev_text:
            body["previous_text"] = prev_text
        if next_text:
            body["next_text"] = next_text
        resp = httpx.post(
            f"{BASE_URL}/text-to-speech/{voice_id}",
            headers={
                "xi-api-key": os.environ["ELEVENLABS_API_KEY"],
                "accept": "audio/mpeg",
            },
            json=body,
            timeout=120,
        )
        resp.raise_for_status()
        out.write_bytes(resp.content)
        return out


@register("elevenlabs")
def _factory() -> ElevenLabsTTS:
    return ElevenLabsTTS()
