"""Stitch per-turn audio segments into one MP3 via ffmpeg.

Every segment is first normalised to a uniform WAV (mono, 24 kHz) so segments
from any provider concatenate cleanly. A short silence between turns gives the
conversation natural breathing room.
"""

from __future__ import annotations

import shutil
import subprocess
from pathlib import Path

SAMPLE_RATE = 24000
GAP_MS = 350  # pause between turns


def _ffmpeg() -> str:
    exe = shutil.which("ffmpeg")
    if not exe:
        raise RuntimeError("ffmpeg not found on PATH. Install it: brew install ffmpeg (macOS) or winget install ffmpeg (Windows)")
    return exe


def _run(args: list[str]) -> None:
    proc = subprocess.run(args, capture_output=True, text=True)
    if proc.returncode != 0:
        raise RuntimeError(f"ffmpeg failed:\n{proc.stderr[-2000:]}")


def _normalise(src: Path, dst: Path) -> Path:
    _run([_ffmpeg(), "-y", "-i", str(src), "-ac", "1", "-ar", str(SAMPLE_RATE), str(dst)])
    return dst


def _silence(dst: Path, ms: int) -> Path:
    _run([
        _ffmpeg(), "-y", "-f", "lavfi",
        "-i", f"anullsrc=channel_layout=mono:sample_rate={SAMPLE_RATE}",
        "-t", f"{ms / 1000:.3f}", str(dst),
    ])
    return dst


def make_silence(dst: Path, seconds: float) -> Path:
    """Public: write `seconds` of silence as a wav (used for [PAUSE] beats)."""
    return _silence(dst.with_suffix(".wav"), int(round(seconds * 1000)))


def stitch(segments: list[Path], out_mp3: Path, gap_ms: int = GAP_MS) -> Path:
    """Normalise, interleave with silence, and encode a single MP3."""
    workdir = out_mp3.parent / "_stitch"
    workdir.mkdir(parents=True, exist_ok=True)
    gap = _silence(workdir / "gap.wav", gap_ms)

    norm: list[Path] = []
    for i, seg in enumerate(segments):
        norm.append(_normalise(seg, workdir / f"n_{i:04d}.wav"))
        if i < len(segments) - 1:
            norm.append(gap)

    listfile = workdir / "concat.txt"
    listfile.write_text("".join(f"file '{p.resolve()}'\n" for p in norm))

    out_mp3.parent.mkdir(parents=True, exist_ok=True)
    _run([
        _ffmpeg(), "-y", "-f", "concat", "-safe", "0", "-i", str(listfile),
        "-c:a", "libmp3lame", "-q:a", "2", str(out_mp3),
    ])

    shutil.rmtree(workdir, ignore_errors=True)
    return out_mp3


def duration_seconds(mp3: Path) -> float:
    exe = shutil.which("ffprobe")
    if not exe:
        return 0.0
    proc = subprocess.run(
        [exe, "-v", "error", "-show_entries", "format=duration",
         "-of", "default=noprint_wrappers=1:nokey=1", str(mp3)],
        capture_output=True, text=True,
    )
    try:
        return float(proc.stdout.strip())
    except ValueError:
        return 0.0
