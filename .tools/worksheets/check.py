"""Check a worksheet's quiz blocks against the Quiz Block plugin's syntax.

Usage: python3 .tools/worksheets/check.py "<worksheet>.md" [...]
Exits non-zero and lists problems if any block is malformed.
"""
import re
import sys

OPTION = re.compile(r"^\[([ crw])\] (.*)$")


def check(path):
    problems = []
    lines = open(path, encoding="utf-8").read().split("\n")
    blocks, current, start = [], None, 0
    for n, line in enumerate(lines, 1):
        if current is None and re.match(r"^```quiz\s*$", line):
            current, start = [], n
        elif current is not None and re.match(r"^```\s*$", line):
            blocks.append((start, current))
            current = None
        elif current is not None:
            current.append(line)
    if current is not None:
        problems.append(f"line {start}: quiz block never closed")

    for start, body in blocks:
        options = [OPTION.match(l) for l in body]
        idx = [i for i, m in enumerate(options) if m]
        where = f"block at line {start}"
        if not idx:
            problems.append(f"{where}: no options")
            continue
        question = "\n".join(body[: idx[0]]).strip()
        details = "\n".join(body[idx[-1] + 1 :]).strip()
        states = [options[i].group(1) for i in idx]
        texts = [options[i].group(2).strip().lower() for i in idx]
        if not question:
            problems.append(f"{where}: no question")
        if any(not OPTION.match(body[i]) for i in range(idx[0], idx[-1] + 1)):
            problems.append(f"{where}: a non-option line sits between options")
        if states.count("c") + states.count("r") != 1:
            problems.append(f"{where}: needs exactly one correct option ([c])")
        if len(idx) != 3:
            problems.append(f"{where}: has {len(idx)} options; worksheets use 3")
        if len(set(texts)) != len(texts):
            problems.append(f"{where}: duplicate options (the plugin drops them)")
        if not details:
            problems.append(f"{where}: no explanation after the options")
    return blocks, problems


status = 0
for path in sys.argv[1:]:
    blocks, problems = check(path)
    print(f"{path}: {len(blocks)} quiz blocks, {len(problems)} problems")
    for p in problems:
        print("  -", p)
    status |= bool(problems)
sys.exit(status)
