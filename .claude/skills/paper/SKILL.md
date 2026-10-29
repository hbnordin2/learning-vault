---
name: paper
description: "Rewrite a research paper (PDF, arXiv link, DOI or journal URL) into a plain-English vault note that keeps every claim at its original strength: a full rewrite in a fixed reading order, not a summary. Optionally also make a podcast episode covering the whole paper and a narrated slide video. Use when the user shares a paper, says “read this paper”, “write up this paper”, “explain this article”, “add this paper to my vault”, or asks for a podcast or video of a paper."
---

# Paper

Turn a research paper into a note a returning reader can skim in five minutes and trust. The output is a **rewrite, not a summary**: every finding, number, condition, and caveat that matters in the main body survives. What changes is the order and the sentences.

The sentence rules come from the `simple-english` skill (Plain mode, never Strict: Strict's word list strips the precision a paper needs). The structure below fixes the larger problem, which is that an abstract packs five jobs into one paragraph and the reader has to work out which sentence does which.

## 1. Get the paper

Work in `build/papers/<slug>/` at the vault root. Git ignores `build/`, so PDFs and scratch files never reach the repo.

- **A PDF the user gives you:** copy it into the work folder.
- **arXiv:** download `https://arxiv.org/pdf/<id>` and fetch metadata from `http://export.arxiv.org/api/query?id_list=<id>` (title, authors, date, abstract, page count).
- **A DOI or journal page:** look up the metadata at `https://api.crossref.org/works/<doi>`. Download the PDF only if it is open access (try `https://api.unpaywall.org/v2/<doi>?email=<the user's email>`). If it is paywalled, ask the user to download it through their library and give you the file. Never write from the abstract alone.
- **Extract the text.** Use `pdftotext paper.pdf plain.txt` if poppler is installed (non-layout mode reads tables best). Otherwise: `uv run --with pypdf python -c "import sys,pypdf; print('\n'.join(p.extract_text() or '' for p in pypdf.PdfReader(sys.argv[1]).pages))" paper.pdf > plain.txt`. Find section headings with grep, then read the **whole main body**, the methods section or appendix, and any appendix that holds the materials, definitions, or protocol the results depend on.
- Render pages with figures if a video is wanted: `pdftoppm -r 150 -png -f N -l N paper.pdf page` (poppler), or screenshot the PDF page.

The structure below fits empirical papers from any field. For a qualitative, theoretical or review paper, keep the same questions and answer "What did they do?" with the method the paper actually uses (interviews, a model, a proof, a corpus, a systematic search).

## 2. Write the note

Before drafting, read the writing canon in `01 - Projects/Learning/Writing/` (once per session): start with `Writing for comprehension.md`, then the notes under `The reader/`, `The sentence/` and `Structure and cohesion/`. Apply it as you draft. In practice: open each section with its point, start sentences with what the reader already knows and end with what is new, make people and systems the subjects and their actions the verbs, and write for a reader who does not share the authors' background (the curse of knowledge).

Save to `03 - Resources/Papers/<Paper title> (<First author> et al. <year>).md`. Strip any `: * ? " < > | \` from the title (use `—` for a colon). Frontmatter: `type: paper`, `source:` (abs URL), `authors:`, `published:`, `tags:` (topic tags matching the vault cluster it relates to).

Sections, always in this order, each heading a plain question:

1. **One paragraph up top, no heading:** what the paper found, in three or four sentences, with the headline numbers. A reader who stops here must have the right answer, at the right strength.
2. **What question does the paper ask?** The question in the reader's words, and the setting it lives in.
3. **Why was the existing answer not good enough?** The gap the authors name, stated plainly. Note it when the gap is thin.
4. **What did they do?** Setup: what was compared, on what, measured how, how many runs. Define every term at first use. Concrete details over category names ("31 Terminal-Bench tasks, three runs each", not "a diverse benchmark suite").
5. **What did they find?** Result by result, each with its number, its comparison point, and its cost. Keep every result the authors make a recommendation from. A small table is fine when the paper compares many conditions on the same axes, but every row needs a sentence of reasoning around it.
6. **How strong is the evidence?** The limits: sample sizes, missing statistics, who ran it, what was not tested, where results flip between models or benchmarks. Separate the authors' stated limits from ones the reader should notice anyway, and say which is which.
7. **What changes in practice?** The authors' recommendations, attributed to them, then (marked as the note's reading, not the paper's) how it connects to existing vault notes via `[[wikilinks]]`.
8. **Terms** — a short glossary of every defined term, one line each.
9. **Sources** — the arXiv link, and page or section pointers for each key number so it can be checked.

## Faithfulness rules (non-negotiable)

- **Keep claim strength.** "We show" stays a demonstration; "suggests", "can", "may" stay hedged. Never upgrade a hedged finding or a single-benchmark result into a general one.
- **Keep the comparison.** A number without its baseline is meaningless: "+9.5 points over the same model without review", never "+9.5 points".
- **Keep the cost.** If the paper reports what a gain costs, the cost travels with the gain.
- **Numbers come from the text, checked twice.** Copy each figure from the extracted text, then re-grep for it before saving. Never compute a new statistic and present it as the paper's.
- **Quote sparingly** — the paper's own wording only where the exact words matter (a prompt, a definition).
- **No invented framing.** Use the paper's own names for its methods and layers; do not coin labels.
- **Neutral voice.** The note is reference prose: no "you", no "I", no trace of the conversation. Where the note adds its own reading (a limit the authors did not state, a link to a vault note), say so in the sentence ("This note's reading:").

## Check before saving

Run the `simple-english` skill's document self-check on the note: split sentences over 25 words (20 for steps), and search for `;`, `—` in prose, `has been`, `should`, `may`, `might`, `could`, `would`, `, making`, and contractions. Fix each hit, with one exception: a `may`, `could` or `might` that carries the paper's own hedge stays, because the faithfulness rules outrank the style rules. Then re-grep every number in the note against the extracted paper text.

## 3. Podcast (optional)

Write it the way the `podcast` skill says, with one change: the episode covers **every finding in the note**, not one core insight. Use the note's order (setup, how it was graded, results one by one, limits, what to do), one segment per finding. Keep every other `podcast` technique in each segment: open by restating in one line where the episode is so far (so a listener who drifted can rejoin), give a concrete example before the principle, have one host pose a question to the listener and the other guess (often wrong) before the answer, ask deep questions, round the numbers, and avoid lists. End with the whole paper restated in a few sentences.

Default length is 15–20 minutes (2,800–3,500 words, about 8,000–10,000 ElevenLabs credits; 2,400 words voice to about 13 minutes). State the credit estimate before voicing. Publish with `.tools/media-feed/publish.py` and link it from the note.

## 4. Video (optional)

A narrated slide video, about 5 minutes:

1. Write a slide script in the work folder: 8–12 slides, each with one claim on screen and 40–90 words of narration (HOST_A only). Use real paper figures where they carry the result.
2. Build each slide as HTML (1920×1080, large type, one idea), screenshot it with headless Chrome or Edge: `<browser> --headless=new --hide-scrollbars --allow-file-access-from-files --screenshot="<abs path>/s01.png" --window-size=1920,1080 "file:///<abs path>/s01.html"`. The browser is at `/Applications/Google Chrome.app/Contents/MacOS/Google Chrome` on macOS and usually `C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe` on Windows. Images inside a slide need absolute `file://` paths. Look at every screenshot before voicing; give flex children `flex-shrink:0` or bar charts squash.
3. Voice each slide's narration separately with `uv run --project .tools/learncast learncast synth s01.txt --title x -p elevenlabs --no-vault -o s01.mp3`, so each slide's length matches its audio.
4. Join with ffmpeg: one clip per slide (`-loop 1 -i s01.png -i s01.mp3 -af apad=pad_dur=0.8 -c:v libx264 -tune stillimage -pix_fmt yuv420p -r 30 -c:a aac -ar 44100 -shortest`; the pad leaves a short gap between slides), then join with `ffmpeg -f concat -safe 0 -i list.txt -c copy`. Save to `99 - Attachments/Videos/` (git ignores media files), publish with `.tools/media-feed/publish.py`, and link it from the note.

## 5. Finish

Commit and push the note (media never goes in git). Report the note path, the media links, the credits spent, and anything in the paper that the note could not resolve.

Then offer a `learn` session on the note. Reading a clear rewrite feels like understanding but builds little memory (see `01 - Projects/Learning/Foundations/The metacognitive trap.md`). Recall is what makes it stick, so the `learn` skill asks the user to explain the paper first, probes the gaps, and writes flashcards only after they show they understand it. Do not add flashcards to the note as part of this skill.
