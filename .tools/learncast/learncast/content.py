"""Assemble source material from vault notes, files, URLs, or a topic.

The goal is a single clean text blob plus a short human title, which the
script stage turns into dialogue. Wikilinks inside vault notes are resolved
one level deep so a note that links out still carries its context.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

import frontmatter

from .config import VAULT

WIKILINK = re.compile(r"\[\[([^\]|#]+)(?:[#|][^\]]*)?\]\]")


@dataclass
class Source:
    title: str
    text: str
    origin: str  # short provenance string for the transcript header


def _read_markdown(path: Path) -> str:
    post = frontmatter.load(path)
    return post.content


def _resolve_vault_note(name_or_path: str) -> Path:
    """Accept a path, a vault-relative path, or a bare note name."""
    p = Path(name_or_path).expanduser()
    if p.exists():
        return p
    candidate = VAULT / name_or_path
    if candidate.exists():
        return candidate
    if not name_or_path.endswith(".md"):
        candidate = VAULT / f"{name_or_path}.md"
        if candidate.exists():
            return candidate
    # last resort: search by stem anywhere in the vault
    matches = [m for m in VAULT.rglob(f"{Path(name_or_path).stem}.md")]
    if matches:
        return matches[0]
    raise FileNotFoundError(f"Could not find note: {name_or_path!r}")


def from_note(name_or_path: str, follow_links: bool = True) -> Source:
    path = _resolve_vault_note(name_or_path)
    body = _read_markdown(path)
    parts = [f"# {path.stem}\n\n{body}"]

    if follow_links:
        seen: set[str] = {path.stem}
        for link in WIKILINK.findall(body):
            link = link.strip()
            if link in seen:
                continue
            seen.add(link)
            try:
                linked = _resolve_vault_note(link)
                parts.append(f"\n\n# (linked) {linked.stem}\n\n{_read_markdown(linked)}")
            except FileNotFoundError:
                continue

    return Source(
        title=path.stem,
        text="\n".join(parts),
        origin=f"vault note: {path.relative_to(VAULT) if VAULT in path.parents else path}",
    )


def from_file(path_str: str) -> Source:
    path = Path(path_str).expanduser()
    if not path.exists():
        raise FileNotFoundError(path)
    if path.suffix.lower() == ".pdf":
        from pypdf import PdfReader

        reader = PdfReader(str(path))
        text = "\n\n".join(page.extract_text() or "" for page in reader.pages)
    elif path.suffix.lower() in {".md", ".markdown"}:
        text = _read_markdown(path)
    else:
        text = path.read_text(errors="replace")
    return Source(title=path.stem, text=text, origin=f"file: {path.name}")


def from_url(url: str) -> Source:
    import httpx

    resp = httpx.get(url, follow_redirects=True, timeout=30)
    resp.raise_for_status()
    html = resp.text
    # crude tag strip; good enough to feed an LLM, not for rendering
    text = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", html, flags=re.S | re.I)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    title_match = re.search(r"<title[^>]*>(.*?)</title>", html, flags=re.S | re.I)
    title = (title_match.group(1).strip() if title_match else url)[:80]
    return Source(title=title, text=text, origin=f"url: {url}")


def from_topic(topic: str) -> Source:
    """A bare topic carries no source text; the script stage researches it."""
    return Source(title=topic, text="", origin=f"topic: {topic}")
