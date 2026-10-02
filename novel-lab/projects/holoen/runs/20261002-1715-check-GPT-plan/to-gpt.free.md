# Task 12 — Review program: audit Claude's plan and design the post-merge verification

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

## Context

The author ordered (2026-10-02) that GPT plan and carry out all later reviews, find new material, and plan the
Sudowrite + ElevenLabs workflow. Claude wrote the queue in `novel-lab/projects/holoen/GPT-PROGRAM.md` (read it
first) and merges results only when the author says so. Read also: projects/holoen/NEXT.md (top status block
only), research/qa/validation-spec.md, research/qa/validation.json, research/qa/resolutions.md (headings and
open items), novel-lab/framework/prompts/rubric.md, tools/release.py (checks V01–V25), tools/qa_runs.py and
tools/qa_packets.py (how the cohort audits are built).

## Deliverables (exact headings)

## Gaps in the queue
Reviews the release needs that the queue does not cover (for example world cards, performance sheets after the
voice fixes, the Sudowrite paste file and CSVs, cross-card consistency after merges, holoX cohort and voice
audits after runs E and F, recency drift), each with why it matters.

## Post-merge verification plan
Rounds that should run after Claude merges the queue's results, in order: what each round checks, its inputs,
its output format, its budget (one quota window each), and exit criteria. The author's rule is one GPT round per
card; promotions are author decisions; say where a second look is a spot check of a merge rather than a re-review.

## Release criteria
Map each blocking check (V01–V25) to the run or round that clears it and what "done" means for release r01.

## Recommended changes to the queue
Order changes, splits or merges of runs, prompts to tighten (cite the file and line), with reasons.

## Risks
Budget, staleness, merge conflicts between runs that touch the same cards, scope risks.

## Run budget
One task must finish inside one quota window (about 200k tokens); every tool call re-sends the conversation.
Batch local lookups (`rg -n -e A -e B files`), prefer official pages, and stop at about 15 tool calls.
Your working directory is a copy of the project taken when this run started (no `runs/`, no git). If the
budget runs short, stop and list what you could not check under Coverage; a complete answer with disclosed
limits beats a lost one.
