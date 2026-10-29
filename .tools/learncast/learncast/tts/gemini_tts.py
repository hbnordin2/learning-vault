"""Gemini text-to-speech (gemini-2.5-flash-preview-tts).

Free-tier eligible, single GEMINI_API_KEY, prebuilt voices (Charon, Kore, ...).
Returns raw PCM, which we wrap into a WAV so ffmpeg can stitch it. Per-turn
single-speaker here for parity with the other providers; Gemini's native
multi-speaker mode is a possible future enhancement.
"""

from __future__ import annotations

import base64
import os
import re
import wave
from pathlib import Path

import httpx

from .base import register

MODEL = os.environ.get("GEMINI_TTS_MODEL", "gemini-2.5-flash-preview-tts")
BASE_URL = "https://generativelanguage.googleapis.com/v1beta"


def _pcm_to_wav(pcm: bytes, out: Path, rate: int) -> Path:
    with wave.open(str(out), "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)  # 16-bit
        w.setframerate(rate)
        w.writeframes(pcm)
    return out


class GeminiTTS:
    name = "gemini"

    def check_key(self) -> None:
        if not (os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")):
            raise RuntimeError(
                "GEMINI_API_KEY is not set. Add it to ~/.config/learning-vault/.env"
            )

    def synth(
        self,
        text: str,
        voice_id: str,
        out: Path,
        prev_text: str | None = None,
        next_text: str | None = None,
    ) -> Path:
        out = out.with_suffix(".wav")
        key = os.environ.get("GEMINI_API_KEY") or os.environ["GOOGLE_API_KEY"]
        resp = httpx.post(
            f"{BASE_URL}/models/{MODEL}:generateContent",
            params={"key": key},
            json={
                "contents": [{"parts": [{"text": text}]}],
                "generationConfig": {
                    "responseModalities": ["AUDIO"],
                    "speechConfig": {
                        "voiceConfig": {
                            "prebuiltVoiceConfig": {"voiceName": voice_id}
                        }
                    },
                },
            },
            timeout=120,
        )
        resp.raise_for_status()
        part = resp.json()["candidates"][0]["content"]["parts"][0]["inlineData"]
        rate_match = re.search(r"rate=(\d+)", part.get("mimeType", ""))
        rate = int(rate_match.group(1)) if rate_match else 24000
        return _pcm_to_wav(base64.b64decode(part["data"]), out, rate)


@register("gemini")
def _factory() -> GeminiTTS:
    return GeminiTTS()
