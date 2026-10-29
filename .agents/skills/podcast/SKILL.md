---
name: podcast
description: "Make a 45–60 minute two-host learning podcast from vault notes: the agent writes the transcript, learncast voices it with ElevenLabs (or OpenAI or Gemini), and the episode is published to the private podcast feed for the phone. Built for listening while cooking, walking or relaxing: one core idea per episode, approached from several angles so a listener who drifts off can rejoin. Use when the user asks for a podcast, an episode, an audio version, or “something to listen to” about a topic or note."
---

# Podcast

Turn a vault topic into a 45–60 minute two-host episode designed for **second-screen listening** — the listener is cooking, walking, or otherwise occupied and *will* zone out for stretches. The design is grounded in `01 - Projects/Learning/The operating system/Learning from passive audio.md` — that note holds the evidence; this skill operationalises it.

**The engine:** *you* write the transcript — you are the LLM, no script API is called. The `learncast` tool at `.tools/learncast` (inside the vault) voices it with ElevenLabs and drops the MP3 + a transcript note into the vault. The whole value is in the transcript obeying the design below; a two-voice reading of a summary is the failure mode, not the goal.

**The core constraint:** one insight per episode, not one topic. The listener will miss 30–50% of any given stretch. The episode must work anyway — through circular structure, re-anchoring, and redundancy across angles, not through progressive argument that requires continuous attention.

## Before you start

Read once per session:
- `01 - Projects/Learning/The operating system/Learning from passive audio.md` — the 10 design implications this skill enforces, and why each holds.
- The vault note(s) for the topic. Find them with Grep/Glob in `01 - Projects/`; read the hub note first if the topic is broad; follow `[[wikilinks]]` one level for context. The notes are your source of truth — be faithful to their claims, tiering, and caveats (do not flatten a hedged claim into a confident one).

Then confirm with the user: **the one core insight** (not just the topic — the specific claim or mechanism the episode will orbit), **length** (45 or 60 min), and **whether to pull in linked notes**. If the source material has several key ideas, propose which single one to build the episode around and why. Tell them the **credit estimate** before generating (see Cost).

## The shape of an episode

One insight, explored circularly. Not a linear argument that builds — a single idea the listener keeps encountering from new angles, so any 2-minute window is self-contained and a zoned-out listener can re-enter without backtracking.

- **Anchor** (~2–3 min, ~350–450 words): a concrete scene or puzzle, then the core insight stated plainly in one sentence. This is the thesis the entire episode orbits. No map of "where we're going" — the listener doesn't need to track a sequence.
- **Passes** (45 min → 4 passes; 60 min → 6), each ~6–9 min / ~900–1,300 words: **the same core insight, approached from a different angle each time** — a new example, a different domain, a misconception, an edge case. Each pass is self-contained: comprehensible even if the listener missed everything before it. Per-pass template below.
- **Final re-anchor** (~3–4 min, ~500–600 words): the insight one last time, in the simplest words yet. Not a summary of the journey (there was no journey) — just the idea, landed cleanly, with one open question worth chasing.

Word budget: aim ~145 words/min of target runtime — **45 min ≈ 6,500 words, 60 min ≈ 8,700 words** — minus what the pauses absorb. Length is approximate; don't pad to hit it.

## Per-pass template

Each pass is a self-contained orbit around the core insight — comprehensible on its own:

1. **Re-anchor** (~60–90s). HOST_B pulls back to the core idea: "OK so the thing we keep coming back to is…" — restating it in fresh words. This is the re-entry ramp for the listener who just tuned back in. Every pass opens this way. (The first pass uses the anchor from the cold open instead.)
2. **New angle.** HOST_A approaches the same insight from a different direction — a new example, a different domain, a historical case, a misconception, an edge case. This is not a new idea; it is the same idea wearing different clothes.
3. **Concrete first.** A worked instance in this pass's domain, *then* fade to how it connects back to the core insight. Never abstraction-first.
4. **Deep question.** HOST_B asks one deep question about this angle (why must it be so / how / what breaks if we change X) and visibly *constructs* — predicts, gets it half-wrong, self-corrects. The construction is the mechanism, not decoration.
5. **A retrieval beat — filled, not silent.** A host hands a question to *the listener* ("you've got the setup — what do you reckon happens when…?"), and then, instead of dead air, the **co-host fills the gap by venturing a quick guess** — often the tempting-but-wrong one — which HOST_A then confirms or corrects. The listener is still cued to answer first; the guess keeps sound flowing and gives them something to check their own answer against. The one rule: the co-host's guess must *not* be the immediate, correct, confident answer — that collapses the effect.
6. **Connect back.** HOST_A explicitly ties this angle back to the core insight — "and that's the same thing as…" — showing it's the same idea, not a new one. If this is pass 3+, connect to an earlier pass too ("same move as the fish-market thing from before").
7. **Micro-recap**: HOST_B restates the core insight — not this pass's angle, the *core insight itself* — in their own words. This is both the spaced restatement and the close of this self-contained window.

**The re-anchor at the top of each pass is non-negotiable.** It is the mechanism that makes the episode work under divided attention. A listener who zoned out for 5 minutes and tunes back in hits a re-anchor within 90 seconds and knows exactly what the episode is about.

## Transcript format

Plain lines. Speakers are `HOST_A` (explainer) and `HOST_B` (questioner/learner-advocate/re-anchorer). Default to no silence — the retrieval beat is filled by a guess. `[PAUSE n]` on its own line gives *n* seconds of real silence and is available, but use it at most as a tiny ~0.5s breath; do not drop seconds of dead air into the episode.

```
HOST_B: OK so — the thing we keep coming back to. Prices aren't set by anyone. They're discovered. Right?
HOST_A: That's it. And here's a completely different place that same thing shows up. Forget the fish market — think about how Uber prices a ride on New Year's Eve.
HOST_A: Nobody at Uber HQ is typing in a number. The algorithm watches demand spike, watches drivers log off, and the fare climbs until enough drivers come back online. The price finds itself.
HOST_B: So it's the same thing as the fish market — just automated.
HOST_A: Exactly the same mechanism. Now here's one to sit with — if the algorithm can see all the data, why does it ever overshoot? Why does surge pricing sometimes hit 9x and then crash back to 2x?
HOST_B: You listening — what's your guess on that? Mine is that there's a lag... the drivers see the high price, they all rush back, and now there's too many.
HOST_A: That's it. The information isn't instant. There's a delay, and the delay causes the overshoot. Same thing happens on the fish-market floor when bids come in faster than the auctioneer can relay them.
HOST_B: So the core idea — prices discover themselves — that's true, but only as fast as information travels. The speed of the information IS the quality of the price.
```

Note the moves: re-anchor to the core insight → new domain (ride-sharing) → concrete example → connect back to earlier pass (fish market) → retrieval beat with wrong guess → reveal → HOST_B restates the core insight, not this example. The listener who just tuned in catches the re-anchor and can follow this pass without having heard the fish-market one.

## Generate

1. **Draft pass by pass** — an 8,700-word transcript can't be written well in one pass. Build each pass to the template. Each pass should be self-contained (a listener starting here should be able to follow), while using different angles/domains/examples from earlier passes.
2. **Assemble into one `.txt`** at `.tools/learncast/build/<slug>.txt` using the format above.
3. **Voice it:**
   ```bash
   cd .tools/learncast && uv run learncast synth build/<slug>.txt --title "<Title>" -p elevenlabs
   ```
   It drops `99 - Attachments/Podcasts/<slug>-<date>.mp3` and a note in `01 - Projects/Learning/Podcasts/` that embeds the audio + transcript.
4. **Publish it to the phone** (from the vault root) — this is how the user actually listens; Obsidian is a poor player and git can't hold the MP3:
   ```bash
   uv run .tools/media-feed/publish.py "99 - Attachments/Podcasts/<slug>-<date>.mp3" --title "<Title>" --about "<one-line hook>"
   ```
   Then add a `[▶ Listen](<episode url>)` line near the top of the podcast note, and commit and push the note. The episode appears in the podcast app on the phone, in the "Vault" feed. If the feed is not set up yet (no `MEDIA_BUCKET` in `~/.config/learning-vault/.env`), skip this step and tell the user the MP3 is in `99 - Attachments/Podcasts/`. Same for any other audio or video made in a session (see `.tools/media-feed/README.md`).
5. **Report** the vault paths, the duration, the credits spent, and that it is in the feed. Synthesis voices each turn separately, so a full episode takes a few minutes — say so before you start.

## Cost & length

ElevenLabs Flash bills ~0.5 credits/char. A 60-min episode ≈ ~52,000 chars ≈ **~26,000 credits**; 45 min ≈ ~20,000.
- **Starter (30k/mo):** ~1 hour-long episode per month — too tight for a habit.
- **Creator (~100k/mo):** ~4–5 per month — the realistic plan for regular episodes.

Always state the estimate before generating. If the user is near their cap, offer a 30-min cut or `--no-vault` for a local draft.

## Banned

- **No progressive structure that requires continuous attention.** The episode must not build a linear argument where missing minute 12 makes minute 18 incomprehensible. Each pass stands alone. If a listener can't tune in at minute 25 and follow what's happening within 90 seconds, the structure is wrong.
- **No breadth.** Do not cover "the topic" — pick the one insight from the source material that is most worth internalising and stay on it. Multiple ideas per episode is the single most common failure mode. If the source material has five key claims, the episode is about one of them.
- **No chat-washing.** Two voices alternating narration is a lecture in stereo. Every exchange must change the explanation's state — a probe answered, a model corrected, a prediction tested.
- **Retrieval questions go to the listener, then get a *guess* — not the answer.** Hand the question to the listener and have the co-host venture a quick (often wrong) guess before the reveal. Never have the co-host immediately answer its own question correctly and confidently — that collapses the effect.
- **No skipping re-anchors.** Every pass opens with a re-anchor to the core insight. This is the mechanism that makes the format work — it is never optional, never "implied," never skipped because "we just said it." The listener may not have heard it.
- **No long dead-air silences.** Engagement is the precondition for any comprehension benefit; keep voices flowing. A guess fills the gap, not seconds of silence.
- **No shallow questioner.** "Interesting!" / "what is X?" is filler. Deep questions only (why/how/what-breaks).
- **No lists or exact numbers read aloud.** Convert to a sequence or one example; round figures ("about a third," not "31.7%").
- **No novice scaffolding for an expert listener** — no slow on-ramps, no over-defining known vocabulary. Compress and go deeper (expertise reversal).
- **No decorative tangents.** Interest must be intrinsic to the idea; a fun-but-irrelevant aside lowers retention.
- **No abstraction-first, no single analogy** for a hard idea.
- **No summary read aloud.** If the transcript would teach as well sitting still and reading it silently, it isn't using the medium — rewrite it around questions, gaps, and a causal spine.
