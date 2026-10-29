---
type: paper
source: https://arxiv.org/abs/2610.14096
authors: [Yang Yao, Haozhe Chen, Bingyi Kang, Karthik R Narasimhan, Zhuang Liu]
published: 2026-10-08
tags: [paper, llm, llm/harness-engineering, llm/evals]
---

# SWEeper-Bench — Can Agents Discover Bugs in Interactive Software (Yao et al. 2026)


Coding agents are good at fixing a bug once someone describes it, and much worse at finding it. The paper gives 15 agents a real web app and a one-sentence request such as "find and fix issues in board sharing", where a known bug appears only after several user steps. The best agent fixed the bug in 59.0% of 200 tasks, and nine agents fixed fewer than half. Given a written bug report for the same tasks, five agents passed 96.0% to 96.5%. Most failures happened before any code changed: the agent reached the right feature but never ran the steps that show the bug, or saw the bug and did not treat it as one. Agents also almost never opened the browser to test unless the prompt told them to.

## What question does the paper ask?

Coding agents now build interactive software on request: a sign-up form, a board, a dashboard. Many bugs in such software show only after a sequence of user actions. For example, a board shared with a colleague never appears in the colleague's sidebar, or a coupon accepted in the cart fails at checkout. Today the user finds these bugs and reports them, and the agent fixes them afterwards.

The paper asks whether an agent can find and fix these bugs itself, before a user meets them. The authors call this sweeping a feature for bugs, the job a colleague does before a release.

## Why was the existing answer not good enough?

Existing coding benchmarks, such as SWE-bench, start from an issue that a user already reported. They measure diagnosis and repair, but not discovery. They also grade with hidden unit tests, which check internal state, not what a user sees, and which can reject a correct fix that takes a different approach. Benchmarks for AI code review do look for unreported bugs, but they mostly read the diff. None tests the case where a bug appears only when the running app goes through a sequence of user actions.

## What did they do?

The authors built 200 tasks from 200 different open-source web apps in seven areas, such as content tools, finance apps, and online shops. The median app has 4,600 GitHub stars. Each task comes from a merged pull request that fixed a user-facing bug. The commit before the fix is the buggy app, and the merged fix is the reference repair. The authors chose bugs that are hard to find but obvious once seen, reproduced each one by hand in a browser, and confirmed that the reference fix resolved it.

Each agent gets four things:

1. The buggy source code.
2. A running copy of the app that updates as the agent edits the code.
3. A Chromium browser with Playwright, a library that lets code drive a browser.
4. A one-sentence request that names a product area and nothing else.

The agent does not see the original issue, the fix, the repository history, or the tests that grade it, and it has no internet access. The default prompt also tells it to test in the browser like a real user and to keep exploring after the first issue it can patch.

A separate agent, the verifier, grades each repair the way a user would notice it. It applies the agent's code changes to a fresh copy of the app and uses the app through the browser, without seeing the source code. Each task has two behavior tests, written as numbered user steps with explicit pass and fail rules. The target test runs the steps that expose the bug and checks that the intended behavior is back. The preservation test checks that nearby features still work. A task passes only if both pass. Because the verifier judges only what a user sees, any correct fix passes, not only one that matches the reference.

The authors checked the verifier before they used it. They ran the tests on every buggy app and every reference fix, with three verifier setups, three times each. All three setups came within one percentage point of the ideal result: fail on the bug, pass on the fix, pass the preservation test on both. The default verifier, GPT-5.6 Luna in Codex, costs $0.16 per task.

The 15 agents each pair a frontier model with its own harness, or with Codex if the model has none. Each run had an 8-hour limit.

## What did they find?

### The best agent passes 59%, and almost all failures are missed bugs

| Agent | Harness | Pass | Mean time | Mean cost |
|---|---|---|---|---|
| Grok 4.6 | Cursor | 59.0% | 12 min | $6.41 |
| Qwen 3.8 Flash | Codex | 57.5% | 102 min | $0.76 |
| Claude Fable 5.1 | Claude Code | 56.5% | 28 min | $11.76 |
| Claude Opus 5 | Claude Code | 56.5% | 43 min | $25.01 |
| GPT-6 Astra | Codex | 56.5% | 14 min | $5.73 |
| DeepSeek V4.1 Flash | DeepSeek | 51.5% | 42 min | $0.35 |

The table shows the top six of 15. The other nine passed between 28.0% and 48.5%. Nearly all failures came from the target test. Preservation pass rates stayed between 97.5% and 100%, so agents rarely broke working features. They missed the bug they were sent to find. Agents with similar pass rates also differed greatly in time and money. Claude Opus 5 matched Claude Fable 5.1 at more than twice the cost.

### The biggest loss is at recognizing the bug

The authors split each run into five steps, where each step requires the one before it. A model (GPT-5.6 Luna) read each run, compared it with a description of the real bug, and judged how far the agent got. Averaged over 14 agents:

1. The agent reached the feature that contains the bug in 75.4% of runs.
2. It identified the buggy behavior in 50.0%. This is the largest drop.
3. It found the root cause in 43.8%.
4. It fixed the bug in 41.0%.
5. It fixed the bug and kept nearby features working in 40.8%.

So once an agent understands the bug, it almost always fixes it. The loss happens earlier. Some agents never ran the interaction that triggers the bug. For example, one agent tested accepting and reverting answers on a Q&A site, but never opened a question through its short link, which is where the bug was.

Other agents saw the bug and did not recognize it. On the Focalboard task, a shared board is missing from the recipient's sidebar. Seeing it takes nine steps across two accounts, and the fix is one function call. The authors inspected four agents, and all four reached the empty sidebar:

- Claude Fable 5.1 and GLM 5.3 treated it as a bug and fixed it.
- Claude Opus 5 decided the behavior was intended, because the existing unit tests expected no sidebar update. It called a change "a product decision, not a bug fix."
- GPT-6 Astra moved on without comment and fixed a different bug.

The authors' point is that existing tests can reinforce the wrong expectation.

### Agents rarely test in the browser unless told to

The authors removed the "test in the browser" lines from the prompt for two agents and changed nothing else. The browser was still installed. GPT-5.6 Luna then drove a browser on 2 of 200 tasks, and GLM 5.3 on 6 of 200, against 200 of 200 when told to. Both read code, ran shell commands and sent HTTP requests instead. Their pass rates fell from 42.0% to 39.5% and from 43.5% to 31.5%. The authors conclude that agents do not yet reach for interactive testing on their own.

### More browser use or more time does not mean better results

Browser actions made up 17% to 62% of agent turns, or 371 to 1,082 actions per task, and neither number tracks pass rate. Qwen 3.8 Max used 517 browser actions per task and passed 28.0%. Claude Fable 5.1 used the browser in 25% of its turns and passed 56.5%. What mattered was which scenarios an agent tested and whether it recognized a failure.

Time was similar. Grok 4.6 and GPT-6 Astra took about 13 minutes per task, while Qwen 3.8 Flash and Kimi K3 took 102 and 90 minutes for similar or lower pass rates. On three tasks, Qwen 3.8 Flash worked for nearly the full 8 hours and produced no patch. When the authors gave three agents fixed budgets of 20, 40, 60 and 80 minutes on 40 tasks, pass rates rose from 20 to 40 minutes and not after. The authors note that with 40 tasks these differences are not statistically significant.

### Finding is the hard part, not fixing

Five agents got a detailed prompt that described the bug and the expected behavior, which works like a bug report. They passed 96.0% to 96.5% of tasks, up from 35.0% to 51.5%, and the gap between agents almost disappeared. GPT-5.6 Luna also worked more directly: its median number of changed lines fell from 49 to 13. The authors' summary is that the difficulty lies in producing the bug report, not in acting on it.

### The harness matters less than the model

GPT-5.6 Luna ran in five harnesses with everything else fixed. It passed 35.0% to 42.5%, and did best in Codex, its own harness. The authors conclude that a matched harness helps, but the model accounts for most of the variation between agents.

## How strong is the evidence?

The authors state four limits. The benchmark covers only web apps. Each task scores one known bug, so it measures how many real bugs agents catch, not how many of their changes are needed. Fixes to other real issues earn no credit, and needless changes cost nothing unless they break the preservation test. The tests check function only, not visual design, ease of use or speed.

The points below are this note's reading. The main pass rates appear to come from one run per agent, with no confidence intervals. With 200 tasks, one task is 0.5 points, so the top five agents (59.0% to 56.5%) are five tasks apart and cannot be ranked against each other with confidence. The five-step analysis uses a model as judge, and the paper does not report a check of that judge against human labels, as it does for the verifier. Agents also ran at different reasoning settings, from "none" to "max", so the table compares setups, not models alone. The behavior tests were written by the authors. The Focalboard comparison is four agents on one task, which shows how agents can fail, not how often each one does.

The two large effects are robust to all of this: about 96% with a bug report against at most 59% without one, and the drop in browser use when the prompt does not ask for it.

## What changes in practice?

The authors draw two conclusions. Agents need to use the app the way a user would and judge its behavior by what it is meant to do, not only by what its tests expect. And verifiers that check what a user sees could reward this kind of testing during training.

This note's reading, for a team that uses agents to build UI:

- Tell the agent to test in the browser, every time. Without the instruction, agents almost never do it, even with a browser installed.
- The expensive step is the bug report. An agent that gets an exact reproduction fixes the bug about 96% of the time. Effort spent on precise, step-by-step reproductions pays more than effort spent on the fix.
- Existing tests can mislead. When the code, its tests and the product intent disagree, an agent may side with the tests, as Claude Opus 5 did. State the intended behavior in the task.
- The paper's behavior-test format (Appendix B) is reusable for agent-run UI tests. Each test gives numbered user steps with exact text to type, separates setup failures from product failures, states pass and fail rules, and forbids checking the API or database, so the verdict rests only on what a user sees.

The finding fits Rethinking Verification in Agent Harnesses (Zhang et al. 2026). There, a separate critic helped because it tested cases the coding agent never thought of. Here, the same gap appears before any code changes: the agent does not think of the user steps that show the bug. In both papers, checks that use the running app helped, and agents did few of them unless the harness asked. See also Verification and self-repair.

## Terms

- **Sweep:** look through a product area for bugs before release, without a bug report.
- **Behavior test:** numbered user steps with explicit pass and fail rules, run in a browser.
- **Target test:** the behavior test that runs the steps that expose the bug and checks the fix.
- **Preservation test:** the behavior test that checks that nearby features still work.
- **Verifier:** a separate agent that runs the behavior tests on the repaired app, without seeing the source code.
- **Agent:** in this paper, a model paired with a harness, such as Claude Opus 5 in Claude Code.
- **Playwright:** a library that lets code drive a browser: open pages, click, type, and read the screen.
- **Recall:** the share of real bugs that a method catches.

## Sources

- Yao, Chen, Kang, Narasimhan, Liu. "SWEeper-Bench: Can Agents Discover Bugs in Interactive Software?" arXiv:2610.14096, 8 October 2026. Princeton University. https://arxiv.org/abs/2610.14096
- Task construction and prompt: Sections 2.1 and 2.2, Figure 4. Full prompt: Appendix A.
- Verifier design and accuracy: Section 2.3, Table 1. Example behavior test: Appendix B, Table 6.
- Main results: Section 3.1, Figure 2, Table 2.
- Five-step analysis and Focalboard case: Section 3.2, Figures 5 to 7.
- Browser use and time: Section 3.3, Figures 8 and 9.
- Browser instruction removed: Section 4.1, Table 3. Detailed prompt: Section 4.2, Table 4. Harnesses: Section 4.3, Table 5. Time budgets: Section 4.4, Figure 10.
- Limits: Section 6.
