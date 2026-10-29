"""learncast CLI.

Two ways in:

  Agent-in-the-loop (primary) — the agent writes a transcript, the tool voices it:
      learncast synth transcript.txt --title "Net revenue retention" --provider openai

  Standalone — the tool also writes the script via an OpenAI-compatible LLM:
      learncast generate --note "Net revenue retention" --length 15
      learncast generate --topic "mechanism design" --length 20 --transcript-only
"""

from __future__ import annotations

from datetime import date
from pathlib import Path
from typing import Optional

import typer
import yaml
from rich.console import Console

from . import content as content_mod
from . import script as script_mod
from . import audio as audio_mod
from . import vault as vault_mod
from .config import HOST_A, HOST_B, PROJECT_ROOT, Settings, settings
from .tts import available_providers, get_provider, synthesize_turns

app = typer.Typer(add_completion=False, help=__doc__, no_args_is_help=True)
console = Console()


def _load_preset(name: str) -> str:
    path = PROJECT_ROOT / "presets" / f"{name}.yaml"
    if not path.exists():
        return ""
    data = yaml.safe_load(path.read_text()) or {}
    return str(data.get("user_instructions", "")).strip()


def _resolve_source(
    note: Optional[str], file: Optional[str], url: Optional[str], topic: Optional[str]
) -> content_mod.Source:
    provided = [x for x in (note, file, url, topic) if x]
    if len(provided) != 1:
        raise typer.BadParameter("Pass exactly one of --note / --file / --url / --topic.")
    if note:
        return content_mod.from_note(note)
    if file:
        return content_mod.from_file(file)
    if url:
        return content_mod.from_url(url)
    return content_mod.from_topic(topic)  # type: ignore[arg-type]


def _synthesize_and_deliver(
    turns: list[script_mod.Turn],
    title: str,
    origin: str,
    provider_name: str,
    out: Optional[Path],
    to_vault: bool,
) -> None:
    provider = get_provider(provider_name)
    provider.check_key()

    workdir = (out.parent if out else PROJECT_ROOT / "build") / "segments"
    n = len(turns)
    console.print(f"[bold]Synthesizing[/] {n} turns via [cyan]{provider_name}[/] …")
    with console.status("Voicing turns…") as status:
        def _progress(done: int, total: int) -> None:
            status.update(f"Voicing turns… {done}/{total}")

        segments = synthesize_turns(turns, provider, workdir, HOST_A, HOST_B, _progress)

    slug = vault_mod._slug(title)
    out_mp3 = out or (PROJECT_ROOT / "build" / f"{slug}.mp3")
    console.print("Stitching audio…")
    audio_mod.stitch(segments, out_mp3)
    secs = audio_mod.duration_seconds(out_mp3)
    console.print(f"[green]✓[/] {out_mp3}  ([bold]{secs/60:.1f} min[/])")

    if to_vault:
        audio_dest, note_dest = vault_mod.deliver(
            out_mp3, title, turns, origin, secs / 60, date.today()
        )
        console.print(f"[green]✓ vault[/] audio → {vault_mod.rel_to_vault(audio_dest)}")
        console.print(f"[green]✓ vault[/] note  → {vault_mod.rel_to_vault(note_dest)}")


@app.command()
def synth(
    transcript: Path = typer.Argument(..., help="Transcript file (HOST_A:/HOST_B: lines)."),
    title: str = typer.Option(..., "--title", "-t", help="Episode title."),
    provider: Optional[str] = typer.Option(None, "--provider", "-p"),
    origin: str = typer.Option("agent-written transcript", "--origin"),
    out: Optional[Path] = typer.Option(None, "--out", "-o", help="MP3 path (else build/)."),
    no_vault: bool = typer.Option(False, "--no-vault", help="Skip vault delivery."),
) -> None:
    """Voice a transcript the agent (or you) already wrote, and drop it in the vault."""
    s = settings()
    turns = script_mod.read_transcript_file(str(transcript))
    _synthesize_and_deliver(
        turns, title, origin, provider or s.provider, out, not no_vault
    )


@app.command()
def generate(
    note: Optional[str] = typer.Option(None, "--note", "-n", help="Vault note name/path."),
    file: Optional[str] = typer.Option(None, "--file", "-f"),
    url: Optional[str] = typer.Option(None, "--url", "-u"),
    topic: Optional[str] = typer.Option(None, "--topic"),
    length: int = typer.Option(0, "--length", "-l", help="Target minutes (0 = default)."),
    preset: str = typer.Option("learning", "--preset"),
    provider: Optional[str] = typer.Option(None, "--provider", "-p"),
    out: Optional[Path] = typer.Option(None, "--out", "-o"),
    transcript_only: bool = typer.Option(False, "--transcript-only"),
    no_vault: bool = typer.Option(False, "--no-vault"),
) -> None:
    """Write the script with an OpenAI-compatible LLM, then voice it (standalone)."""
    s: Settings = settings()
    minutes = length or s.default_minutes
    source = _resolve_source(note, file, url, topic)

    console.print(
        f"[bold]Generating script[/] (~{minutes} min) via "
        f"[cyan]{s.llm_model}[/] @ {s.llm_base_url}"
    )
    raw = script_mod.generate_transcript(source, minutes, _load_preset(preset), s)
    turns = script_mod.parse_transcript(raw)
    console.print(f"[green]✓[/] script: {len(turns)} turns, ~{script_mod.word_count(turns)} words")

    if transcript_only:
        dest = (out or PROJECT_ROOT / "build" / f"{vault_mod._slug(source.title)}.txt")
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(script_mod.transcript_to_text(turns))
        console.print(f"[green]✓[/] transcript written → {dest}")
        raise typer.Exit()

    _synthesize_and_deliver(
        turns, source.title, source.origin, provider or s.provider, out, not no_vault
    )


@app.command()
def providers() -> None:
    """List TTS providers and whether their keys are present."""
    import os

    settings()  # load .env
    key_for = {
        "openai": "OPENAI_API_KEY",
        "elevenlabs": "ELEVENLABS_API_KEY",
        "gemini": "GEMINI_API_KEY",
    }
    for name in available_providers():
        env = key_for.get(name, "")
        ok = bool(os.environ.get(env)) or (name == "gemini" and bool(os.environ.get("GOOGLE_API_KEY")))
        mark = "[green]●[/] key set" if ok else "[red]○[/] no key"
        console.print(f"  {name:12} {mark}   ({env})")


@app.command()
def voices() -> None:
    """Show the two-host voice mapping per provider."""
    for label, v in (("HOST_A (explainer)", HOST_A), ("HOST_B (questioner)", HOST_B)):
        console.print(f"[bold]{label}[/]")
        for prov, vid in v.ids.items():
            console.print(f"    {prov:12} {vid}")


if __name__ == "__main__":
    app()
