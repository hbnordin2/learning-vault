---
name: worksheet
description: Make a practice worksheet on anything the user wants to learn (a vault folder, a note, a paper, a podcast transcript, a web page) with Quiz Block multiple-choice questions and explanations, confidence marks, recall prompts with hidden model answers, and re-tests of what earlier worksheets show was missed. Also marks a finished worksheet. Use when the user asks for a worksheet, quiz, practice questions, self-test, “test me on this”, or says they finished a worksheet.
---

# /worksheet

Make one worksheet that makes the user retrieve, apply and tell apart the ideas in a source, with feedback after every answer. The design comes from `01 - Projects/Learning/The operating system/Learning from worksheets.md`: read it once per session before writing a worksheet. It holds the evidence for every rule below, and this skill does not repeat it.

The worksheet is the test, and the user takes it. Never answer for the user, never put an answer where it is visible before the attempt, and never add Anki cards (cards come only from `/learn`).

## 1. Find the source and the goal

The user names the source in their own words: a folder, a note, a paper, a podcast, a URL, or a topic. Resolve it:

- **Vault folder or topic:** find the notes with Glob and Grep under `01 - Projects/`. Read the hub note first, then the notes the worksheet will cover. For a large folder, cover the hub's "where to start" path or ask which part.
- **Paper:** use the `/paper` note in `03 - Resources/Papers/` if one exists, and the PDF text for detail.
- **Podcast:** read the transcript note in `01 - Projects/Learning/Podcasts/`.
- **URL:** read it with the `defuddle` skill.

Read the source in full. Every question and every answer must come from it. Decide two things, and ask only when the request does not settle them:

1. **Before or after studying.** A worksheet before the user has read the source is a prequestion worksheet: fewer items, aimed at the central ideas, and a low score is expected and fine. Say so at the top. A worksheet after studying is the default.
2. **What the user needs to do with it.** Know the facts, explain the mechanism, apply it to new cases, or carry out a procedure. This sets the mix in step 4.

## 2. Read the earlier worksheets

List `01 - Projects/Learning/Worksheets/`. Read every filled-in worksheet on the same topic or source, and skim the others for related concepts. The plugin writes answers into the file:

- `[r]` is a right answer, `[w]` a wrong one, and `[c]` the correct option of a question that was answered wrongly or not at all. A block with no `[r]` or `[w]` was not answered.
- `- [x] Sure` just above a quiz block means the user was confident. `[w]` with `- [x] Sure` is a **confident error**, which is the highest-priority item to re-test.
- In recall and explain items, an unticked `- [ ] Got it` means the user marked their own answer as wrong. Read what they wrote, too.

From this, collect: missed items, low-confidence right answers, concepts the user confuses with each other, and the overall level (mostly right means move toward application and telling ideas apart; mostly wrong means add worked examples and smaller steps). Spacing needs at least a day between attempts, so items from a worksheet finished today are not re-tested yet.

## 3. Map the source before writing questions

In scratch notes (not the worksheet), list:

- The key ideas: claims, mechanisms, numbers that matter, procedures.
- **Misconceptions:** what a person who half-knows each idea would wrongly believe. These become the wrong options.
- **Confusable pairs:** ideas that are easy to mix up, in this source or between this source and earlier worksheets.
- **New situations:** cases outside the source where each idea would apply, for transfer questions.

## 4. Write the worksheet

Default size is 15 to 20 items, about 30 minutes. Use this order, and drop a section that has nothing to put in it:

1. **How to do this worksheet** (three lines): answer from memory, without the source; your first click is final, because clicking again overwrites a wrong answer; tick `Sure` before answering only if you would bet on it; write recall answers before opening the hidden answer. Quiz Block works in editing mode, not reading mode.
2. **Re-test** (only if step 2 found items): the missed and low-confidence items, each asked in new wording or in a new scenario, so the user retrieves the idea and does not recognise the old question. Confident errors first.
3. **Recall:** one or two prompts that ask the user to write the key ideas from memory, such as "Write the three main findings and why each holds." The model answer goes in a folded callout, with a short checklist to mark against.
4. **Questions:** the main multiple-choice set. At least half must be application, analysis or prediction questions, not definitions.
5. **Tell them apart:** questions that make the user choose between confusable ideas, including ideas from earlier worksheets.
6. **Apply it:** new situations that the source does not describe, as multiple choice or as short written answers with a hidden model answer. For a procedure, fade the support: a worked example to study, then one to finish, then one to do alone.

### Multiple-choice items

```quiz
A team's coding agent fixes 96% of bugs when given a written bug report but about half when told only "find and fix issues in checkout". What does that gap say the agent lacks?
[ ] The skill to change code correctly once the cause is known
[c] The ability to find and recognise the bug without a report
[ ] Enough time to explore the codebase before stopping

**Right:** the bug report supplies the discovery step. With it, the fix rate is near-perfect, so the fix itself is not the limit.
**Why not the others:** fixing ability is what the 96% shows is present. Time is ruled out because longer runs did not score higher.
Source: [[SWEeper-Bench — Can Agents Discover Bugs in Interactive Software (Yao et al. 2026)#Finding is the hard part, not fixing]]
```

Put `- [ ] Sure` on its own line directly above each quiz block. Rules for every item:

- **Three options, one correct (`[c]`).** Each wrong option is a real misconception from step 3, plausible to someone who half-knows the idea. Never "all of the above", "none of the above", or a joke option.
- **The question stands alone:** it states the full problem, so it could be answered before the options are read. One idea per question.
- **No give-aways:** options of similar length, grammar and detail; no word in the question that repeats only in the right option; no negative questions ("which is NOT") unless unavoidable, with NOT in bold.
- **Each option on one line**, starting `[ ] ` or `[c] `. The question above the options may be several lines of markdown. The plugin shuffles the options, so their order does not matter.
- **The explanation goes after the options** and appears only once the user answers. It says why the right answer is right, why each wrong option is wrong, and links the source section. This is the feedback, and it is never optional.

### Recall and written-answer items

```markdown
**Explain why** a critic model that sees only the code changes can beat one that reads the agent's whole session.

Answer:

> [!success]- Model answer
> The session is the agent's own account of its work, so reading it pulls the critic toward the agent's view and its blind spots. On visual tasks, the changes-only critic won by about 8 points of net preference without required visual checks.
> - [ ] Named the agent's account as the source of bias
> - [ ] Gave the direction of the result
>
> Source: [[Rethinking Verification in Agent Harnesses (Zhang et al. 2026)#L3 a separate critic gives the most accuracy for the least extra cost]]

- [ ] Got it
```

The folded callout (`> [!success]-`) hides the answer until it is clicked. The user writes their answer under "Answer:", then opens the callout, ticks the checklist, and ticks `Got it` only if their answer was right.

### Check every answer

Before saving, check each correct option and each model answer against the source text. If the source does not settle a question, cut the question. Each explanation's link must point at a heading that exists.

## 5. Save and check

Save to `01 - Projects/Learning/Worksheets/<Topic> — worksheet <N> (<YYYY-MM-DD>).md`, where N counts worksheets on that topic. Strip `: * ? " < > | \` from the topic. Frontmatter:

```yaml
---
type: worksheet
topic: <topic>
sources: ["[[<note>]]"]
created: <YYYY-MM-DD>
kind: after-study    # or before-study
retests: <number of re-test items>
---
```

Run the syntax check, and fix every problem it lists:

```bash
uv run .tools/worksheets/check.py "01 - Projects/Learning/Worksheets/<file>.md"
```

Commit and push the worksheet. Tell the user the path, how many items of each kind it has, and which earlier misses it re-tests.

## 6. When the user says they finished

Read the filled-in worksheet. Report in plain sentences: what they got right, each miss with the idea behind it, any confident errors, and how their `Sure` marks matched their results. Do not re-teach at length: the explanations are already in the worksheet. Suggest the next worksheet on the topic no sooner than the next day, and offer `/learn` for any idea they missed twice. Commit and push the filled-in file.
