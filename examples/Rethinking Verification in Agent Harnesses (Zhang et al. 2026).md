---
type: paper
source: https://arxiv.org/abs/2610.34577
authors: [Zhengxin Zhang, Erkang Zhu, Yin Lin, Claire Cardie, Bolin Ding, Jingren Zhou]
published: 2026-10-25
tags: [paper, llm, llm/harness-engineering, llm/evals]
---

# Rethinking Verification in Agent Harnesses (Zhang et al. 2026)


The paper tests 17 ways to make a coding agent check its own work, on seven models and three benchmarks. The best option is a second, cheaper model (a critic) that inspects the finished work and sends its findings back. This added 5.9 to 9.5 percentage points of accuracy on Terminal-Bench and 3.9 to 6.6 on SWE-bench Verified, at 1.00 to 1.25 times the cost of the agent with no added checks. Telling the agent to check its work, at the start or during the run, gave small gains that changed from model to model. Stopping the agent at the end and making it check again also helped, but it cost up to 1.76 times as much. The study is by authors at Cornell and Alibaba, uses about 30 tasks per coding benchmark, and reports no tests of statistical significance.

## What question does the paper ask?

A coding agent works in a loop. The model reads the task, calls a tool (edit a file, run a command), reads the result, and repeats until it stops. The software that runs this loop is the harness. The harness decides what the model is told, when, and what happens when it says it is done.

Verification here means any step where the agent's work gets checked and then fixed. The paper asks three questions about it. When should the harness step in? Who should do the checking, the agent or a separate model? How should the results of a check turn into fixes? The authors treat verification as a way to spend more computation at run time to get better results, which the field calls test-time scaling.

## Why was the existing answer not good enough?

Earlier research built the parts: trained models that score answers, methods where a model critiques and revises its own output, and checks that run code and feed the errors back. Real harnesses use these parts by rule of thumb. Claude Code offers hooks that can run checks when the agent finishes. Codex has the agent review its own work. The authors say no one has compared these choices side by side, across models, with cost measured. So a team that builds a harness cannot tell which design helps their model, or whether the gain is worth the extra spend.

## What did they do?

The authors split the agent's run into four points where a check can happen. They call these layers L0 to L3.

- **L0, initial instructions.** Before the run starts, a paragraph is added that tells the agent to run what it changes, look at the real output, and fix what breaks. The paragraph goes in either the system prompt (standing instructions from the harness) or the user's first message.
- **L1, execution-time reminders.** During the run, the harness inserts a reminder to run and check recent changes. One version sends it every third turn after the first edit. Another sends it after each turn that changes a file. Reminders stop after four.
- **L2, completion gates.** When the agent tries to finish, the harness stops it and asks for more. The versions differ in what they ask: re-read the changes, run and check the changes, or simply reject the finish with the message "An automated verification pass has determined this task is NOT complete. Keep working." That message is not true. No check ran. "Early" versions also fire when 80% of the time limit has passed.
- **L3, independent review.** A separate model, the critic, starts with a fresh context, gets the task and access to the agent's live workspace, and runs its own checks. It cannot change the work. It returns a pass, or a list of unmet requirements that goes back to the agent. The agent fixes them, and its next delivery is accepted without a second review.

The critic comes in four versions. Two choices make the four. The first choice is what the critic sees: the task and the agent's code changes (the "Changes" condition), or those plus the agent's full session of reasoning and commands (the "Trajectory" condition). The second choice is how it builds its checklist: from the task alone ("Task-first"), or also from each claim the agent made, such as "tested" or "works", which it then tries to disprove ("Claim-guided"). The critic prompt tells it to work out the expected answer on its own, to treat "I looked and saw nothing wrong" as no evidence, and to fail anything it could not show to work by running it.

Seven agent models took part: Qwen3.7-Max, Qwen3.8-Max, GLM-5.2, DeepSeek V4-Pro, DeepSeek V4-Flash, Kimi-K2.7-Code, and MiniMax-M2.5. The critic was always Qwen3.7-Plus, a cheaper model. Its output tokens cost $1.194 per million, against $5.373 for Qwen3.7-Max.

The coding benchmarks were 31 tasks from Terminal-Bench 2.1 (command-line tasks) and about 30 from SWE-bench Verified (fixes to real GitHub issues). Both grade answers automatically. Tasks were picked to mix easy, middle, and hard. Each design ran three times per model and task. Accuracy is the share of tasks solved. Cost is the dollar cost of the agent, the critic, and any fixes, priced at Alibaba Cloud rates, and reported as a multiple of the cost without added checks (the baseline).

The authors also built VisualBench, 18 tasks that ask for something a person looks at or uses: a playable game, a 3D product configurator, a sales data explorer. Raters from an internal Alibaba data team compared the output of one design against the baseline, without knowing which was which, and picked a winner on function and look. The score is net preference: the share of wins minus the share of losses, in points.

## What did they find?

Before the results, one finding about the baseline sets the scene. Agents with no added checks ran a recognizable check after only 6.2% to 13.6% of the turns in which they edited files. Most edits went unchecked.

### L0: instructions at the start help a little, and only in the system prompt

The check paragraph in the system prompt raised average accuracy by 3.3 points on Terminal-Bench and 3.9 on SWE-bench. In the user message, the same paragraph gave +1.2 and −1.1. Cost stayed near baseline (0.93 to 1.08 times). The effect changed a lot by model. On SWE-bench, MiniMax-M2.5 gained 12.6 points while Qwen3.8-Max lost 2.3. On VisualBench the system-prompt version scored −3.2, which means the baseline won slightly more often.

One case shows how an instruction can hurt. On the `git-multibranch` task, the instructed Qwen3.7-Max deleted the repository to set up a test, which also deleted the deployment hook it needed, and it failed. The uninstructed run passed.

The authors recommend a short check paragraph in the system prompt, kept short so it leaves room for other harness instructions.

### L1: reminders during the run help a little and cost less

Reminders with the system role gave +3.8 (periodic) and +3.5 (after edits) on Terminal-Bench, and +3.1 and +3.6 on SWE-bench. Sending the after-edit reminder as a user message raised the Terminal-Bench gain to +5.4 but dropped SWE-bench to −0.3. Reminders cut output tokens by 14% to 25% on Terminal-Bench and 7% to 10% on SWE-bench, so cost was 0.85 to 1.12 times baseline. Higher accuracy came with less output in some cases: Qwen3.7-Max gained 14.3 points on Terminal-Bench with user reminders while using 28% fewer output tokens. On VisualBench, L1 scored −3.2.

Agents did act on reminders. After a user-role reminder, 90% to 97% of agents ran a command within two turns. But a run is not always the right check. Kimi-K2.7-Code checked that a document compiled and missed that its word swaps were invalid. DeepSeek V4-Flash checked that the output matched and missed the speed requirement.

The authors recommend reminders after each edit that ask the agent to check the result against the task, including the rendered output for visual work.

### L2: making the agent check again at the end works, but costs too much for what it gives

Gates that ask the agent to re-read its changes added almost nothing: +0.7 on Terminal-Bench and +0.5 on SWE-bench. Gates that reject the finish did better. The best was the early user-message rejection, at +6.0 and +6.2, the largest L2 gains. Rejection is expensive. It cost 1.60 to 1.76 times baseline on Terminal-Bench and 1.48 to 1.56 times on SWE-bench. After a rejection, the typical agent took 12 to 19 more steps, against 4 to 6 after a request to re-read. The early user-message recheck was the cheap middle option: +4.8 and +4.1 at 1.13 and 1.20 times cost. On VisualBench it scored +2.7.

Reopened work can also break a correct answer. On `git-multibranch`, Kimi-K2.7-Code responded to a recheck by pushing test content to the live branches and leaving it there, and failed. The baseline passed. The authors' point is that more work only helps if the agent finds the real defect and leaves a valid final state.

The authors recommend against checks at completion by the agent itself, because the gains are small for the extra cost.

### L3: a separate critic gives the most accuracy for the least extra cost

All four critic designs improved both coding benchmarks: +5.9 to +9.5 points on Terminal-Bench and +3.9 to +6.6 on SWE-bench. Total cost, including the critic and the agent's fixes, was 1.13 to 1.25 times baseline on Terminal-Bench and 1.00 to 1.04 times on SWE-bench. Against the best L2 design, the best critic gained more on Terminal-Bench (+9.5 against +6.0), about the same on SWE-bench (+6.6 against +6.2), and cost less on both.

| Critic design | Terminal-Bench | SWE-bench Verified |
|---|---|---|
| Claim-guided, changes | +5.9 | +5.1 |
| Task-first, changes | +6.9 | +6.6 |
| Claim-guided, trajectory | +8.4 | +6.1 |
| Task-first, trajectory | +9.5 | +3.9 |

The table shows that no single design wins on both coding benchmarks. The full session helped most on Terminal-Bench and least on SWE-bench, and it raised critic cost by 29% to 43%.

On VisualBench, all four critic designs beat every L0 to L2 design, at +13.2 to +23.8 net preference. Here the changes-only critic beat the full-session critic, both without a required look at the output (+21.2 against +13.2) and with one (+23.8 against +21.6). Requiring the critic to render the output and look at it helped both versions. The changes-only critics scored positive for all seven models. The full-session critics did not.

The authors recommend a separate, low-cost critic that sees the task and the code changes as the default.

The examples show why a critic catches what self-checks miss. On `regex-log`, MiniMax-M2.5 tested its regular expression and declared it done. The critic tried a log line with the date before the IP address, the match failed, and the agent fixed it and passed. On `cobol-modernization`, Qwen3.7-Max's Python rewrite passed its own checks. The critic tested an underflow and found that Python wrote a minus sign where the COBOL field had none, which broke the record format. The agent fixed the formatting and passed. In both cases the critic tested a case the agent did not think of, and it handed back a failure the agent could run. The critic does not always rescue the run. On `cancel-async-tasks`, GLM-5.2's critic found the bug, but the run hit its 45-minute limit before the fix.

### Scaling the critic: more rounds or more critics add a few points

On Terminal-Bench, with the claim-guided changes critic, one critic and one round reached 62.7% accuracy using 38,200 critic tokens on average. Two rounds reached 65.6% at 79,500 tokens. Two critics side by side reached 64.4% at 69,700. Four rounds reached 66.1% and four critics 65.8%. Four critics added 3.1 points over one, at 1.33 times total cost. Four critics came close to four rounds at 19% lower total cost, because the agent fixes once against all the critics' findings, not four times in a row.

## How strong is the evidence?

The authors do not state limits beyond the results themselves. The points below are this note's reading of the setup.

The samples are small. Each coding benchmark has about 30 tasks and three runs, so one model on one design rests on about 90 graded attempts. On Terminal-Bench, the per-model numbers move in steps of about 1.2 points, which is one attempt flipping. The paper gives no confidence intervals or significance tests. The averages across seven models are steadier than any single model's number, and the single-model swings (often 10 points or more in either direction) are best read as noise plus real model differences that the study cannot separate.

The models are all from Chinese labs and were reached through Alibaba Cloud. No Claude, GPT, or Gemini model was tested as the agent, so the results may not hold for those. The critic was one model, Qwen3.7-Plus, for every agent. The authors work at Alibaba, which makes the Qwen models. VisualBench is internal and was rated by an internal company team, so it cannot be rerun from outside.

The study tests one set of prompts per design. A better-written gate or reminder could do better. The L2 rejection gate also tells the agent something false (that an automated check failed), which a real harness may not want to do.

The headline is stable across both coding benchmarks and VisualBench: a separate critic beats asking the agent to check itself, at lower cost than reopening the agent's work. The finer choices, such as what context the critic sees, flip between benchmarks and are not settled.

## What changes in practice?

The authors give four recommendations. Keep a short check instruction in the system prompt. Send a reminder to check after edits, and include the rendered output for visual work. Do not rely on making the agent re-check itself when it finishes. Use a separate, cheap critic that sees the task and the changes, and add rounds or critics when the task is worth more spend.

The critic prompt in Appendix E.4 is the most reusable part of the paper. It makes the critic write a weighted checklist from the task, name the one property where a passing-looking answer could still be wrong, prove each item by running the real output, and never change the work.

This note's reading: the result fits the generator/evaluator split in Designing the generator-evaluator harness, where the agent that does the work is never the agent that judges it, and the case in Verification and self-repair for an independent checker over self-checking. This paper adds a cost-measured comparison across models that those sources did not have. In the terms of Guides and sensors, L0 and L1 are guides and L3 is a sensor.

## Terms

- **Harness:** the software that runs the model's loop of reasoning, tool calls, and results, and decides what the model is told and when.
- **Verification:** any step where the agent's work is checked and then fixed.
- **Test-time scaling:** spending more computation at run time, not training time, to get better results.
- **Baseline:** the same model and harness with no added checks.
- **Critic:** a separate model that inspects the agent's finished work and reports problems, without changing it.
- **Changes / Trajectory:** what the critic sees: the code changes only, or the changes plus the agent's full session.
- **Task-first / Claim-guided:** how the critic builds its checklist: from the task only, or also from the agent's own claims of success.
- **Completion gate:** a step that stops the agent when it tries to finish and asks for more work.
- **Net preference:** the share of rater wins minus the share of losses against the baseline, in points.
- **Percentage points (pp):** the plain difference between two percentages. 60% to 66% is +6 points.

## Sources

- Zhang, Zhu, Lin, Cardie, Ding, Zhou. "Rethinking Verification in Agent Harnesses." arXiv:2610.34577, 25 October 2026. https://arxiv.org/abs/2610.34577
- Design layers and variants: Section 3, Figure 1, Table 1.
- Models, benchmarks, metrics: Section 4. Task selection: Appendix A.1. Prices: Appendix A.2, Table 4.
- Per-model accuracy changes: Table 2 (Terminal-Bench), Table 3 (SWE-bench Verified). Cost: Figure 2.
- Baseline check rate (6.2% to 13.6%): Section 3 and Appendix Table 7. Reminder follow-through: Appendix Table 8.
- VisualBench results: Figure 3 and Appendix Table 12.
- Scaling rounds and critics: Section 5.4, Figure 4, Appendix Figure 23.
- Exact prompts for every design, including the critic: Appendix E.
