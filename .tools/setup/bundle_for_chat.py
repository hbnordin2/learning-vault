"""Join a vault folder's notes into a few files to upload to a ChatGPT or Claude project.

    uv run .tools/setup/bundle_for_chat.py "01 - Projects/Learning"
    uv run .tools/setup/bundle_for_chat.py "03 - Resources/Papers" --max-kb 400

Chat projects accept a limited number of files, so one file per note does not
fit a large folder. This writes build/chat-upload/<folder> (part N).md, each
holding many notes, each opened by a line with its vault path so the
chat app can say which note an answer came from. Upload every part.
"""

import argparse
import re
from pathlib import Path

VAULT = Path(__file__).resolve().parents[2]
SKIP = {".git", ".obsidian", ".agents", ".claude", ".tools", "build", "99 - Attachments"}


def notes(folder: Path) -> list[Path]:
    return sorted(
        p for p in folder.rglob("*.md")
        if not any(part in SKIP for part in p.relative_to(VAULT).parts)
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("folders", nargs="+")
    parser.add_argument("--max-kb", type=int, default=800, help="size of each part (default 800 KB)")
    args = parser.parse_args()

    out_dir = VAULT / "build" / "chat-upload"
    out_dir.mkdir(parents=True, exist_ok=True)
    for name in args.folders:
        folder = (VAULT / name).resolve()
        found = notes(folder)
        if not found:
            raise SystemExit(f"no notes in {name}")
        parts, current = [], []
        size = 0
        for note in found:
            text = note.read_text(encoding="utf-8")
            text = re.sub(r"^---\n.*?\n---\n", "", text, count=1, flags=re.S)
            block = f"\n\n---\n\nNote: {note.relative_to(VAULT).as_posix()}\n\n{text.strip()}\n"
            if current and size + len(block.encode()) > args.max_kb * 1024:
                parts.append(current)
                current, size = [], 0
            current.append(block)
            size += len(block.encode())
        parts.append(current)
        label = folder.name
        for i, blocks in enumerate(parts, 1):
            dest = out_dir / f"{label} (part {i}).md"
            dest.write_text(f"# {label} — notes from the vault, part {i} of {len(parts)}" + "".join(blocks), encoding="utf-8")
            print(dest.relative_to(VAULT).as_posix())
        print(f"{len(found)} notes from {name} in {len(parts)} file(s)")


if __name__ == "__main__":
    main()
