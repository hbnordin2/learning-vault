"""Copy the vault's skills into .claude/skills/ for Claude Code.

    uv run .tools/setup/copy_skills_for_claude.py

Codex and ChatGPT read skills from .agents/skills/, which is the copy kept in
git. Claude Code reads .claude/skills/. Run this after pulling skill changes.
git ignores .claude/, so the copy never drifts into the repo.
"""

import shutil
from pathlib import Path

VAULT = Path(__file__).resolve().parents[2]
src, dst = VAULT / ".agents" / "skills", VAULT / ".claude" / "skills"
for skill in sorted(p for p in src.iterdir() if (p / "SKILL.md").exists()):
    shutil.copytree(skill, dst / skill.name, dirs_exist_ok=True)
    print(f"copied {skill.name}")
