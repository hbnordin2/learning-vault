"""TTS provider interface + registry.

A provider knows how to turn one turn's text into one audio file using a
provider-specific voice id. Providers write native-format audio (mp3, wav,
pcm-in-wav); the audio module normalises everything to a uniform wav before
stitching, so providers don't have to agree on format.
"""

from __future__ import annotations

from pathlib import Path
from typing import Callable, Protocol

from .. import audio
from ..config import DEFAULT_PAUSE_SECONDS, HOST_A, HOST_B, SPEAKER_A, SPEAKER_PAUSE, Voice
from ..script import Turn


class TTSProvider(Protocol):
    name: str

    def synth(
        self,
        text: str,
        voice_id: str,
        out: Path,
        prev_text: str | None = None,
        next_text: str | None = None,
    ) -> Path:
        """Write audio for `text` in voice `voice_id` to `out`; return path.

        `prev_text`/`next_text` are the neighbouring turns' words; providers that
        support cross-segment prosody (ElevenLabs) use them for continuity.
        """
        ...

    def check_key(self) -> None:
        """Raise a clear error if credentials are missing."""
        ...


_REGISTRY: dict[str, Callable[[], TTSProvider]] = {}


def register(name: str) -> Callable[[Callable[[], TTSProvider]], Callable[[], TTSProvider]]:
    def deco(factory: Callable[[], TTSProvider]) -> Callable[[], TTSProvider]:
        _REGISTRY[name] = factory
        return factory

    return deco


def get_provider(name: str) -> TTSProvider:
    if name not in _REGISTRY:
        raise KeyError(f"Unknown TTS provider {name!r}. Known: {sorted(_REGISTRY)}")
    return _REGISTRY[name]()


def available_providers() -> list[str]:
    return sorted(_REGISTRY)


def synthesize_turns(
    turns: list[Turn],
    provider: TTSProvider,
    workdir: Path,
    voice_a: Voice = HOST_A,
    voice_b: Voice = HOST_B,
    progress: Callable[[int, int], None] | None = None,
) -> list[Path]:
    """Synthesize every turn to its own file. Returns segment paths in order."""
    workdir.mkdir(parents=True, exist_ok=True)
    segments: list[Path] = []
    total = len(turns)
    for i, turn in enumerate(turns):
        out = workdir / f"seg_{i:04d}"
        if turn.speaker == SPEAKER_PAUSE:
            try:
                secs = float(turn.text)
            except ValueError:
                secs = DEFAULT_PAUSE_SECONDS
            segments.append(audio.make_silence(out, secs))
            if progress:
                progress(i + 1, total)
            continue
        voice = voice_a if turn.speaker == SPEAKER_A else voice_b
        vid = voice.for_provider(provider.name)
        prev_text = turns[i - 1].text if i > 0 and turns[i - 1].speaker != SPEAKER_PAUSE else None
        next_text = (
            turns[i + 1].text if i + 1 < total and turns[i + 1].speaker != SPEAKER_PAUSE else None
        )
        segments.append(provider.synth(turn.text, vid, out, prev_text, next_text))
        if progress:
            progress(i + 1, total)
    return segments


# Import side effects register the providers.
from . import elevenlabs_tts, gemini_tts, openai_tts  # noqa: E402,F401
