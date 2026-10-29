@AGENTS.md

Claude Code reads skills from `.claude/skills/`, not `.agents/skills/`. If `.claude/skills/` is missing or older than `.agents/skills/`, run `uv run .tools/setup/copy_skills_for_claude.py` first.
