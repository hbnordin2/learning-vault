"""Install the vault's Obsidian community plugins and turn them on.

    uv run .tools/setup/install_obsidian_plugins.py            # all plugins below
    uv run .tools/setup/install_obsidian_plugins.py quizblock  # only some

Each plugin's GitHub repo is looked up in Obsidian's official plugin list (or
KNOWN_REPOS below), and
the files of its latest release go into .obsidian/plugins/<id>/. Obsidian must
be closed while this runs, or restarted afterwards. The first time, Obsidian
also asks to turn on community plugins (Settings → Community plugins).

.obsidian/ is not in git: each device keeps its own plugins and layout, so run
this once on each laptop. On a phone, install the plugins from inside Obsidian.
"""

from __future__ import annotations

import json
import sys
import urllib.request
from pathlib import Path

VAULT = Path(__file__).resolve().parents[2]
PLUGINS = {
    "obsidian-git": "Git: pulls and pushes the vault so every device stays in sync",
    "quizblock": "Quiz Block: makes the multiple-choice questions in worksheets clickable",
    "obsidian-to-anki-plugin": "Obsidian_to_Anki: sends flashcards written in notes to Anki",
}
# Plugins that have left Obsidian's list but still publish releases on GitHub.
KNOWN_REPOS = {"obsidian-to-anki-plugin": "Pseudonium/Obsidian_to_Anki"}
REGISTRY = "https://raw.githubusercontent.com/obsidianmd/obsidian-releases/master/community-plugins.json"

# Desktop git settings: pull on open and every 10 minutes, commit and push every 10.
GIT_SETTINGS = {
    "commitMessage": "vault backup: {{date}}",
    "autoCommitMessage": "vault backup: {{date}}",
    "autoSaveInterval": 10,
    "autoPushInterval": 0,
    "autoPullInterval": 10,
    "autoPullOnBoot": True,
    "pullBeforePush": True,
    "disablePush": False,
    "syncMethod": "merge",
    "differentIntervalCommitAndPush": False,
    "autoBackupAfterFileChange": False,
}


def get(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": "learning-vault-setup"})
    with urllib.request.urlopen(req, timeout=60) as resp:
        return resp.read()


def main() -> None:
    wanted = sys.argv[1:] or list(PLUGINS)
    registry = KNOWN_REPOS | {p["id"]: p["repo"] for p in json.loads(get(REGISTRY))}
    plugins_dir = VAULT / ".obsidian" / "plugins"

    for plugin_id in wanted:
        repo = registry.get(plugin_id)
        if not repo:
            sys.exit(f"{plugin_id} is not in Obsidian's plugin list")
        release = json.loads(get(f"https://api.github.com/repos/{repo}/releases/latest"))
        assets = {a["name"]: a["browser_download_url"] for a in release.get("assets", [])}
        dest = plugins_dir / plugin_id
        dest.mkdir(parents=True, exist_ok=True)
        for name in ("main.js", "manifest.json", "styles.css"):
            if name in assets:
                (dest / name).write_bytes(get(assets[name]))
            elif name != "styles.css":
                sys.exit(f"{plugin_id} {release.get('tag_name')}: release has no {name}")
        if plugin_id == "obsidian-git" and not (dest / "data.json").exists():
            (dest / "data.json").write_text(json.dumps(GIT_SETTINGS, indent=2))
        print(f"installed {plugin_id} {release.get('tag_name')} from {repo}")

    enabled_file = VAULT / ".obsidian" / "community-plugins.json"
    enabled = json.loads(enabled_file.read_text()) if enabled_file.exists() else []
    enabled += [p for p in wanted if p not in enabled]
    enabled_file.write_text(json.dumps(enabled, indent=2))
    print("Restart Obsidian, then allow community plugins if it asks.")


if __name__ == "__main__":
    main()
