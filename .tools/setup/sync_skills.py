"""Mirror .agents/skills/ into .claude/skills/, so every agent sees the same skills.

    uv run .tools/setup/sync_skills.py           # copy any changes across
    uv run .tools/setup/sync_skills.py --check   # only report whether they differ

.agents/skills/ is the one place to edit a skill. Codex and Cursor read it
directly. Claude Code reads only .claude/skills/, so this
script keeps a copy there, and both copies are committed so a fresh clone works
in every tool. A copy is used instead of a link because links break when the
repository is checked out on Windows.
"""

import filecmp
import shutil
import sys
from pathlib import Path

VAULT = Path(__file__).resolve().parents[2]
SRC, DST = VAULT / ".agents" / "skills", VAULT / ".claude" / "skills"


def differences() -> list[str]:
    found = []

    def walk(cmp: filecmp.dircmp, rel: Path) -> None:
        found.extend(str(rel / n) for n in cmp.left_only + cmp.right_only + cmp.diff_files)
        for name, sub in cmp.subdirs.items():
            walk(sub, rel / name)

    if not DST.exists():
        return [str(DST)]
    walk(filecmp.dircmp(SRC, DST, ignore=[".DS_Store", "__pycache__"]), Path())
    return found


if "--check" in sys.argv:
    diff = differences()
    print("\n".join(diff) if diff else "skills are in sync")
    sys.exit(1 if diff else 0)

if DST.exists():
    shutil.rmtree(DST)
shutil.copytree(SRC, DST, ignore=shutil.ignore_patterns(".DS_Store", "__pycache__"))
print(f"copied {sum(1 for p in DST.iterdir() if p.is_dir())} skills to .claude/skills/")
