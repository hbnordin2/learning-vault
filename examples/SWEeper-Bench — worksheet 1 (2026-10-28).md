---
type: worksheet
topic: SWEeper-Bench
sources: ["SWEeper-Bench — Can Agents Discover Bugs in Interactive Software (Yao et al. 2026)", "Rethinking Verification in Agent Harnesses (Zhang et al. 2026)"]
created: 2026-10-28
kind: after-study
retests: 0
---

# SWEeper-Bench — worksheet 1

How to do this worksheet. Answer from memory, with the paper note closed. Your first click on each question is final, because clicking again overwrites a wrong answer. Tick `Sure` before answering only if you would bet on your answer. Write recall answers before you open the hidden answer. Quiz Block works in editing mode, not reading mode.

## Recall

**Write the three most important findings of SWEeper-Bench**, each with the number or comparison that supports it.

Answer:

> [!success]- Model answer
> 1. Agents find and fix far fewer bugs without a bug report: the best of 15 agents passed 59% with a one-sentence request, while five agents given a written bug report passed about 96%.
> 2. The loss happens at recognising the bug: agents reached the right feature in about three quarters of runs but identified the buggy behaviour in only half.
> 3. Agents rarely test in the browser unless told to: with the instruction removed, two agents opened the browser on 2 and 6 of 200 tasks, and their scores fell.
>
> - [ ] Had the report-versus-no-report gap
> - [ ] Placed the loss at recognising the bug, not fixing it
> - [ ] Had the browser finding, or that more time and clicking did not help
>
> Source: SWEeper-Bench — Can Agents Discover Bugs in Interactive Software (Yao et al. 2026)

- [ ] Got it

## Questions

- [ ] Sure

```quiz
How did SWEeper-Bench decide whether an agent's repair worked?
[ ] It ran the project's hidden unit tests that came with the original fix
[c] A second agent used the repaired app in a browser, following written user steps, without seeing the code
[ ] It compared the agent's code changes line by line with the original developer's fix

**Right:** a verifier agent applied the changes to a fresh copy of the app and ran two behaviour tests through the browser, judging only what a user would see.
**Why not the others:** the authors avoided hidden unit tests because they can reject a correct fix written a different way. Comparing against the original fix would fail any correct alternative for the same reason.
Source: SWEeper-Bench — Can Agents Discover Bugs in Interactive Software (Yao et al. 2026)
```

- [ ] Sure

```quiz
A benchmark grades bug fixes with the unit tests from the original developer's fix. An agent fixes the bug correctly but restructures the code. What is the risk the SWEeper-Bench authors point to?
[ ] The unit tests run too slowly to finish inside the time limit
[c] The tests can reject the correct fix because it differs from the reference implementation
[ ] The agent can read the hidden tests and write code that passes them

**Right:** hidden unit tests check internal details of one implementation, so a correct fix that takes a different approach can fail them.
**Why not the others:** speed is not the problem the paper names. The agent in this setup cannot see the hidden tests, so it cannot game them.
Source: SWEeper-Bench — Can Agents Discover Bugs in Interactive Software (Yao et al. 2026)
```

- [ ] Sure

```quiz
The authors split each run into stages: reach the feature, identify the buggy behaviour, find the cause, fix it, keep nearby features working. Where did the share of runs fall the most?
[ ] Between reaching the feature and the start of the run
[c] Between reaching the feature and identifying the buggy behaviour
[ ] Between finding the cause and fixing the bug

**Right:** about three quarters of runs reached the feature, and only half identified the buggy behaviour. That is the largest drop.
**Why not the others:** reaching the feature was the most common success, at about 75%. Once an agent found the cause, it almost always fixed it: about 44% found the cause and 41% fixed the bug.
Source: SWEeper-Bench — Can Agents Discover Bugs in Interactive Software (Yao et al. 2026)
```

- [ ] Sure

```quiz
An agent logs in as the second user, sees that the shared board is missing from the sidebar, and then reads the existing unit tests, which do not expect the sidebar to change. Based on the paper's Focalboard case, what is the most likely outcome?
[c] It decides the empty sidebar is intended behaviour and does not fix it
[ ] It fixes the sidebar but breaks a nearby feature, failing the preservation test
[ ] It keeps exploring until the time limit and produces no patch

**Right:** this is what Claude Opus 5 did. It concluded that changing the sidebar would be "a product decision, not a bug fix", because the tests did not expect a change.
**Why not the others:** agents broke nearby features rarely (97.5% to 100% preservation pass rates). Running out of time without a patch happened on only a few tasks, for one agent.
Source: SWEeper-Bench — Can Agents Discover Bugs in Interactive Software (Yao et al. 2026)
```

- [ ] Sure

```quiz
The authors deleted the "test in the browser like a real user" lines from the prompt for two agents and left the browser installed. What happened?
[ ] The agents opened the browser anyway, and their scores did not change
[c] The agents almost never opened the browser, and their scores fell
[ ] The agents used the browser more, because they had less guidance on how to test

**Right:** one agent drove a browser on 2 of 200 tasks and the other on 6. Their pass rates fell from 42.0% to 39.5% and from 43.5% to 31.5%.
**Why not the others:** the browser was available in both cases, yet use collapsed without the instruction, so it was not used "anyway". Less guidance led to reading code and sending HTTP requests, not more browser testing.
Source: SWEeper-Bench — Can Agents Discover Bugs in Interactive Software (Yao et al. 2026)
```

- [ ] Sure

```quiz
Your agent builds a small sign-up app for a team, and bugs keep reaching users. Which single change does the paper's evidence support most?
[c] Add an instruction to test the app in the browser like a real user
[ ] Give the agent twice as long before it has to stop
[ ] Move the agent to a different harness with the same model

**Right:** without the instruction, agents almost never test in the browser, and that is where interaction bugs show.
**Why not the others:** more time helped only from 20 to 40 minutes and then flattened. Changing harness moved one model by a few points, and the authors found the model mattered more than the harness.
Source: SWEeper-Bench — Can Agents Discover Bugs in Interactive Software (Yao et al. 2026)
```

- [ ] Sure

```quiz
Three agents were given time budgets of 20, 40, 60 and 80 minutes on the same 40 tasks. What happened to their pass rates?
[ ] They rose steadily from 20 to 80 minutes
[c] They rose from 20 to 40 minutes and then stopped rising
[ ] They did not change at any budget

**Right:** pass rates rose from 20 to 40 minutes and not beyond. The authors note that with 40 tasks these differences are not statistically significant.
**Why not the others:** there was no steady rise past 40 minutes. There was some change at the low end, so "no change" is too strong.
Source: SWEeper-Bench — Can Agents Discover Bugs in Interactive Software (Yao et al. 2026)
```

- [ ] Sure

```quiz
Preservation tests passed 97.5% to 100% of the time, but overall pass rates were 28% to 59%. What does that combination tell you?
[c] Agents rarely broke working features; they failed because they missed the bug they were sent to find
[ ] The verifier was too lenient on preservation tests, so those results are unreliable
[ ] Agents mostly made no code changes at all, so nothing could break

**Right:** a task passes only if both tests pass. With preservation near 100%, almost all failures come from the target test, the one that checks the bug.
**Why not the others:** the verifier was checked against buggy apps and real fixes and came within one point of ideal. The prompt required at least one real code change, so empty diffs were not the explanation.
Source: SWEeper-Bench — Can Agents Discover Bugs in Interactive Software (Yao et al. 2026)
```

- [ ] Sure

```quiz
Why should the top five agents (59.0% down to 56.5%) not be ranked against each other?
[ ] Each agent was tested on a different set of apps
[c] The gap is about five tasks out of 200, and the scores appear to come from single runs with no confidence intervals
[ ] The verifier disagreed with itself too often to separate them

**Right:** one task is 0.5 points, so 2.5 points is five tasks, and there is no measure of run-to-run variation for the pass rates.
**Why not the others:** all agents ran the same 200 tasks. The verifier's runs varied by at most 0.8 points.
Source: SWEeper-Bench — Can Agents Discover Bugs in Interactive Software (Yao et al. 2026)
```

- [ ] Sure

```quiz
One model, GPT-5.6 Luna, was run in five harnesses with everything else fixed. What did the authors conclude?
[ ] The harness explains most of the difference between agents
[c] A matched harness helps, but the model explains most of the difference between agents
[ ] The harness makes no difference to the pass rate

**Right:** Luna passed 35.0% to 42.5% across harnesses and did best in Codex, its own harness. The authors still judged the model to account for most of the variation.
**Why not the others:** a spread of about 7 points rules out "no difference", and the authors did not say the harness explains most of it.
Source: SWEeper-Bench — Can Agents Discover Bugs in Interactive Software (Yao et al. 2026)
```

## Tell them apart

- [ ] Sure

```quiz
Both this paper and *Rethinking Verification in Agent Harnesses* find that agents miss cases they did not think of. A separate critic model that tests the finished work addresses which moment?
[c] After the agent says it is done, checking work it already produced
[ ] Before any edit, discovering a bug that no one has reported
[ ] After the bug is described, writing the code that fixes it

**Right:** the verification paper's critic inspects the delivered work and returns failures for the agent to fix.
**Why not the others:** discovering an unreported bug is SWEeper-Bench's problem, and no critic was tested there. Writing the fix once the bug is described is the step agents already do well (about 96%).
Source: Rethinking Verification in Agent Harnesses (Zhang et al. 2026)
```

- [ ] Sure

```quiz
Which statement fits the findings of both papers on telling an agent to test its work?
[ ] An instruction alone has no measurable effect on what the agent does
[c] An instruction changes what the agent does, but the size of the gain varies by model and task
[ ] An instruction alone closes most of the gap to the best design

**Right:** in the verification paper, a check instruction in the system prompt added a few points that varied by model. In SWEeper-Bench, removing the browser instruction collapsed browser use, and scores fell by 2.5 points for one agent and 12 for the other.
**Why not the others:** both papers show measurable effects, so "no effect" is wrong. In the verification paper the separate critic beat any instruction, so an instruction does not close most of the gap.
Source: Rethinking Verification in Agent Harnesses (Zhang et al. 2026)
```

## Apply it

**Explain why** existing unit tests can stop an agent from fixing a real bug, using the Focalboard case.

Answer:

> [!success]- Model answer
> The tests were written by the same developers who wrote the bug, so they encode the developers' expectation, including the mistake. Claude Opus 5 saw the empty sidebar, found that the tests expected no sidebar change, and concluded the behaviour was intended. The authors' lesson is to judge an app by what it is meant to do for a user, not only by what its tests expect.
> - [ ] Said the tests encode the same mistaken expectation as the code
> - [ ] Gave the remedy: judge by intended user behaviour
>
> Source: SWEeper-Bench — Can Agents Discover Bugs in Interactive Software (Yao et al. 2026)

- [ ] Got it

**Write a behaviour test** in the paper's format for this bug: a coupon is accepted in the cart but rejected at checkout. Five to eight steps is enough.

Answer:

> [!success]- Model answer
> 1. Open the shop's home page and wait until the product list is visible.
> 2. Add one product to the cart. If the product cannot be added, stop and report a setup problem.
> 3. Open the cart, type exactly `SAVE10` in the coupon field, and apply it. Confirm the cart shows the discount.
> 4. Click Checkout and fill the shipping form with the given test details.
> 5. On the payment step, read the order summary.
> 6. PASS only if the summary still shows the `SAVE10` discount. FAIL if the coupon is gone or shows as invalid. Do not use the API, the network panel or the database to decide.
>
> - [ ] Numbered user steps with the exact text to type
> - [ ] Setup problems kept separate from product failures
> - [ ] Explicit pass and fail rules
> - [ ] Judged only on what a user sees
>
> Source: SWEeper-Bench — Can Agents Discover Bugs in Interactive Software (Yao et al. 2026)

- [ ] Got it

- [ ] Sure

```quiz
A teammate's agent reports: "The shared board is missing from the member's sidebar, but the unit tests expect that, so I left it." What is the best next step, given this paper?
[c] Tell the agent what the feature should do for a user, and ask it to fix the behaviour and update the tests
[ ] Accept the result, because the existing tests define correct behaviour
[ ] Re-run the agent with a longer time limit so it explores more

**Right:** the agent saw the bug and talked itself out of it. Stating the intended user behaviour removes the ambiguity that the tests created.
**Why not the others:** in the paper, deferring to the tests is exactly how Claude Opus 5 missed this bug. More time does not help an agent that has already seen the bug and dismissed it.
Source: SWEeper-Bench — Can Agents Discover Bugs in Interactive Software (Yao et al. 2026)
```
