# Task 11 — Sudowrite + ElevenLabs workflow: verify, plan, integrate

You are GPT, the senior researcher and QA reviewer for novel-lab's holoen project. Use the project-required
GPT-6 model at xhigh with live web search. Work read-only and answer in English. This is one task in a sequential
queue; do not launch parallel GPT work. Never read projects/*/runs/. Do not modify files; return the complete
result in your final response. The factual baseline is 2026-09-30 (today is 2026-10-02).

## Binding rules

- Public persona only. Never record or infer private life: health, family, home, sleep or daily routine,
  trips and travel, romantic life or orientation, nationality or mother tongue, audition history, breaks or
  their reasons (announced breaks are not written at all). Accents appear only as voice features.
- Authenticity first: profanity, teasing and crude jokes stay verbatim; never sanitize.
- Short quotes only; no lyrics. A spoken quote must be a span both ASR models share (see the audio reports).
- Never clone or imitate a member's real voice; performance directions are for original designed voices.
- Baseline 2026-09-30; recency weighting for "current" defaults; every character's Role is Protagonist.
- Promotions are author decisions, not GPT approval; the author's rules in project.md bind.
- Never propose (even when an official profile or wiki lists it): body measurements, drinking amounts, family,
  home or home region, pets, health, sleep or daily routine, trips, romance, audition history, breaks or their
  reasons, pre-debut history or the performer behind the persona. A Merge Record that says "private details
  deliberately excluded" means a topic was left out on purpose: do not re-propose it.
- No explicit sexual content, no lyrics, no long quotes. Spoken quotations are not accepted from you: list them
  as candidates for Claude's two-model audio check (video, timestamp, approximate words). Official written
  lines (profiles, post text, titles) may be quoted short with their source.
- No member rankings or comparisons. Partner tags and voice directions are proposed scene directions for
  original designed voices, never imitation; no pitch, F0 or speaking-rate targets.
- Evidence classes: OFFICIAL (hololive/COVER pages, official accounts), PRIMARY (the member's own stream title,
  description or post), ARCHIVE_METADATA, SECONDARY (wiki, fan sites; label it), ASR (Claude's audio reports).
  Fan transcription cannot establish exact spoken words.

## Goal

The project's product is dialogue for AI voice performance. A writer drafts scenes in Sudowrite from the Story
Bible cards (Characters, Worldbuilding, Style); an ElevenLabs v4 voice that is original (designed, never cloned
or imitating the member) performs each character's lines with inline audio tags. The author wants the whole
Sudowrite + ElevenLabs workflow planned and integrated: what the writer and the voice director do, step by step,
with which files, and exactly what our package must change to support it.

## Read first (in your working copy; do not re-open them repeatedly)
- novel-lab/docs/sudowrite-2026-09.md and novel-lab/docs/elevenlabs-v4.md (our platform notes)
- novel-lab/projects/holoen/project.md (the author's rules) and novel-lab/framework/sudowrite-fields.json
- novel-lab/projects/holoen/export/sudowrite-paste.md, export/characters.csv, export/worldbuilding.csv (what
  the writer pastes or imports), export/elevenlabs/sudowrite-style.md (the Style block) and one sheet, e.g.
  export/elevenlabs/Mori-Calliope.md and export/elevenlabs/AZKi.md
- novel-lab/tools/release.py (delivery package layout, START-HERE text, checks V01–V25)

## Verify live (official documentation first, as of 2026-10)
- Sudowrite: Story Bible structure and fields (Characters, Worldbuilding, Style, Synopsis, Outline, Braindump,
  Genre), field limits, visibility toggles, import paths (paste, CSV, others), Write/Draft/Rewrite/Describe and
  scene or chapter tools, Plugins, Muse or current model choices, export formats, any API.
- ElevenLabs: the current v4 model name and ID, the audio-tag set and how tags are written, Text to Dialogue
  (multi-speaker) in the app and API (request shape, limits), Voice Design (text-to-voice), voice settings and
  their API ranges, pronunciation dictionaries, Studio/projects for long-form assembly, output formats, and the
  terms on voices of real people (consent, impersonation, voice library rules).
- COVER's fan-work and derivative-work guidelines that bear on fan fiction and synthetic voice of its talents
  (official URLs).

## Exact output format (these headings, in this order)

## Verified platform facts
| Platform | Feature | What it does now | Source URL | Checked | What our docs say | Agree? |
|---|---|---|---|---|---|---|

## End-to-end workflow
Numbered stages: 0 setup; 1 load the bible into Sudowrite; 2 plan a scene; 3 draft dialogue with tags;
4 lint the script; 5 design the original voices; 6 generate in ElevenLabs; 7 listen and fix; 8 assemble and
deliver; 9 version and archive. For each: inputs, actions, outputs with file names, who does it, checks, common
failures and their fixes.

## Script format spec
The scene format Sudowrite should be prompted to output and the converter reads: speaker labels, where tags go,
narration and stage directions (excluded from audio or sent to a narrator voice), line length, pauses and SFX,
multi-speaker turns, language mixing (Japanese lines with romanization). Include a short example using only
labelled Style demo lines (no real quotations).

## Converter
Full Python 3 standard-library code for `novel-lab/tools/scene_to_elevenlabs.py`: parse a script file in the
spec's format; validate speakers against a voice map (JSON: speaker → voice_id, set by the voice director) and
tags against each character's allowed tags (parsed from export/elevenlabs/<stem>.md); flag nonverbal tags that
are also spelled out; split over-long turns; emit the Text to Dialogue request body as JSON (one file per scene)
plus a plain-text listening sheet. No network calls, no keys. Then a minimal test (sample script in, expected
JSON out) as a second code block.

## Package gap analysis
| ID | Priority | File + section | Exact old text | Problem | Exact replacement | Evidence |
|---|---|---|---|---|---|---|
IDs WF-NNN; P0 (blocks the workflow or breaks platform terms), P1 (material), P2 (clarity). Copy old text
exactly; DELETE for deletions; escape pipes; <br> for newlines.

## Writer's quick-start
One page in English for the delivery package's START-HERE: the workflow in ten lines or fewer per role.

## Risks and policy
Voice cloning and impersonation, disclosure of synthetic voice, platform terms, COVER guidelines, explicit
content (never written; the project marks such scenes 【Sudowrite 處理】 without content).

## Open questions for the author
Up to five, each answerable with a short choice.

## Run budget
One task must finish inside one quota window (about 200k tokens); every tool call re-sends the conversation.
Batch local lookups (`rg -n -e A -e B files`), prefer official pages, and stop at about 30 tool calls.
Your working directory is a copy of the project taken when this run started (no `runs/`, no git). If the
budget runs short, stop and list what you could not check under Coverage; a complete answer with disclosed
limits beats a lost one.
