"""Configuration: env loading, paths, voice presets.

All knobs live here so the rest of the code stays declarative. Secrets come
from ~/.config/learning-vault/.env (outside the vault, so never in git) or the real
environment, which is how Claude Code cloud sessions supply them.
"""

from __future__ import annotations

import os
from dataclasses import dataclass, field
from pathlib import Path

# --- paths -------------------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent

# The Obsidian vault: learncast lives at <vault>/.tools/learncast, so the vault
# is two levels up. Override with LEARNCAST_VAULT.
VAULT = Path(
    os.environ.get("LEARNCAST_VAULT", str(PROJECT_ROOT.parent.parent))
).expanduser()

# Where finished audio + transcript notes land inside the vault.
VAULT_AUDIO_DIR = VAULT / "99 - Attachments" / "Podcasts"
VAULT_NOTE_DIR = VAULT / "01 - Projects" / "Learning" / "Podcasts"


def load_dotenv(path: Path | None = None) -> None:
    """Minimal .env loader (no dependency). Existing env vars win."""
    path = path or Path.home() / ".config" / "learning-vault" / ".env"
    if not path.exists():
        return
    for line in path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        os.environ.setdefault(key, value)


# --- voices ------------------------------------------------------------------


@dataclass
class Voice:
    """A single host's voice, named per provider.

    `ids` maps a provider name -> the provider-specific voice identifier.
    """

    role: str  # "explainer" | "questioner"
    ids: dict[str, str] = field(default_factory=dict)

    def for_provider(self, provider: str) -> str:
        try:
            return self.ids[provider]
        except KeyError as exc:  # pragma: no cover - guard rail
            raise KeyError(
                f"No voice id for provider '{provider}' on role '{self.role}'. "
                f"Known: {list(self.ids)}"
            ) from exc


# Two hosts. HOST_A explains; HOST_B probes, asks for examples, pushes back.
# Voice ids are sensible defaults per provider; tune freely.
HOST_A = Voice(
    role="explainer",
    ids={
        # OpenAI gpt-4o-mini-tts preset voices
        "openai": "ash",
        # ElevenLabs (Chris) — replace with your own cloned/chosen voice id
        "elevenlabs": "iP95p4xoKVk53GoZ742B",
        # Gemini multi-speaker prebuilt voice names
        "gemini": "Charon",
    },
)
HOST_B = Voice(
    role="questioner",
    ids={
        "openai": "coral",
        # ElevenLabs (Jessica)
        "elevenlabs": "cgSgspJ2msm6clMCkdW9",
        "gemini": "Kore",
    },
)

# Speaker labels used in transcripts. Stable contract between script + TTS.
SPEAKER_A = "HOST_A"
SPEAKER_B = "HOST_B"
# A silent beat. `[PAUSE]` or `[PAUSE 2.5]` on its own line becomes real silence
# in the audio, so a host can pose a question and leave the listener room to
# answer in their head before the reveal (covert retrieval).
SPEAKER_PAUSE = "PAUSE"
DEFAULT_PAUSE_SECONDS = 2.0


@dataclass
class Settings:
    provider: str = field(default_factory=lambda: os.environ.get("LEARNCAST_TTS_PROVIDER", "openai"))
    # Optional LLM path for standalone script-gen (Claude-out-of-the-loop).
    # OpenAI-compatible: works with OpenRouter, OpenAI, etc.
    llm_base_url: str = field(default_factory=lambda: os.environ.get("LEARNCAST_LLM_BASE_URL", "https://openrouter.ai/api/v1"))
    llm_model: str = field(default_factory=lambda: os.environ.get("LEARNCAST_LLM_MODEL", "anthropic/claude-sonnet-4"))
    default_minutes: int = field(default_factory=lambda: int(os.environ.get("LEARNCAST_DEFAULT_MINUTES", "15")))



def settings() -> Settings:
    load_dotenv()
    return Settings()
