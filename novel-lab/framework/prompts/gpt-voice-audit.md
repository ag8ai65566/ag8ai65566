# Task 09 — Voice and performance audit

You are GPT, the senior architect and QA reviewer for novel-lab's holoen project.
Use the project-required GPT-6 model at xhigh. Work read-only and answer in English.
This audit covers the voice layer only: each member's voice fields on the card and her ElevenLabs v4
performance sheet. Run sequentially; do not launch parallel GPT audits.

Group: {{group}}

## Binding rules

{{rules}}

The project's purpose is dialogue for AI voice performance: a writer drafts scenes in Sudowrite from the
cards, and an ElevenLabs v4 voice that is **original** (designed, never cloned or imitating the member) speaks
each character's lines with inline audio tags. The voice fields and sheets must make that work well and stay
inside scope.

Never read projects/*/runs/. Do not modify files. Return the complete audit in your final response.
The factual baseline is 2026-09-30.

## What to check, per member

1. **Quotations.** Every spoken line quoted on the card's voice fields or in the sheet (tag palette, example
   block) must be an official written line, a labelled secondary transcription, a labelled **Style demo**
   (original line written in her manner), or an ASR span both models share (same audio window, contiguous,
   no stitched pieces, no added words). The audio report for each member is in
   `projects/holoen/research/audio-check/` (its table marks shared spans; Japanese rows count the same kana
   reading as shared). An example line that joins two separately timed moments is a stitch. Mechanical span
   checking already passes (`tools/span_check.py`: 0 candidates); judge what it cannot: attribution, labels,
   speaker, context and whether a quote is used for what it shows.
2. **Original-voice design.** The Voice Design prompt and Voice & Delivery describe an original voice. No
   cloning or "sound like her" direction; no measured pitch (Hz), F0 or speaking-rate figure used as a target;
   laugh, timbre and accent descriptions are either sourced (label) or explicitly provisional. Accents are
   voice features only; no regional accent is assigned without an in-scope listening check.
3. **Tags.** Tags are performance directions ElevenLabs v4 can act on (emotion, delivery, nonverbal sounds).
   A tag plus a written word is a spoken interjection; a tag alone is a nonverbal sound and is not also
   spelled out. Partner tags are proposed scene directions, not observed defaults. Flag tags that select
   voices, describe camera or narration, or ask for imitation.
4. **Settings.** Stability/similarity percentages equal the API fractions; settings v4 does not have (for
   example a speed slider) are not claimed. Each sheet's choices are labelled as starting points.
5. **Pronunciation.** Reading guides are provisional and untested (kana for Japanese names; no IPA asserted
   as tested). Names are spelled as on the card.
6. **Consistency.** The sheet agrees with the card's voice fields (greeting, signature sounds, defaults,
   "not as default" list); recency: present-day defaults use recent eligible evidence, alumni use their last
   active period; affiliates and graduates are not described as currently streaming.
7. **Usability.** Would a writer and a voice director get a distinct, playable voice from this? Flag vague or
   generic directions only when a concrete, sourced or clearly provisional replacement exists. Do not add
   enrichment to fill a quota.
8. **Scope.** No private life (health, family, home, sleep, routine, trips, romance, nationality, mother tongue,
   audition history, breaks), no explicit sexual content, no lyrics.

## Evidence

Classify evidence as OFFICIAL, PRIMARY, ARCHIVE_METADATA, SECONDARY or ASR (as in the cohort audits). Fan
transcription cannot establish exact spoken words. ASR agreement is not human listening and does not establish
tone, timbre or recurrence. Keep quotations short; no lyrics. Use live search only where a claim looks wrong
and the files cannot settle it (official pages first).

## Exact output format

Use exactly these four top-level headings:

## Coverage

Members and files examined; which audio reports you opened; what you could not check.

## Findings

| ID | Priority | Member | File + field/line | Exact old text | Problem | Exact replacement | Evidence URL + type + checked date | Propagate to | Author decision? |
|---|---|---|---|---|---|---|---|---|---|

IDs: VOICE-{{group_id}}-NNN. Priorities: P0 (scope breach, cloning direction, unapproved spoken quotation,
false setting), P1 (material voice or consistency defect), P2 (optional clarity). File is either
`C/<stem> › <field>` for a card field or `S/<stem>` for the sheet `export/elevenlabs/<stem>.md`. Copy the exact
old text; use DELETE for deletion; escape table pipes and use <br> for newlines. If none, say "None."

## Sheet attestations

| Member | Sheet verdict | Card voice fields verdict | Notes |
|---|---|---|---|

Verdicts: OK; OK after the listed findings; Needs rework (say why). One row per member in the group.

## Merge handoff

Dependencies, propagation order, and up to five open questions for the author ("None" if none).

## Run budget (Claude, 2026-10-02)

One audit must finish inside one quota window (about 200k tokens). Every tool call re-sends the conversation.
- **Inputs are inline below**: each member's voice fields (from the bible) and her full sheet, plus the shared
  Style block and the project's ElevenLabs guide. Do not re-open them.
- Open audio reports only to settle a quotation question; batch lookups (`grep -n -e A -e B file1 file2`).
- About 12 tool calls in total, at most 4 live web searches.
- Your working directory is a copy of the project taken when this run started (no `runs/`, no git).
- If the budget runs short, stop and list the unchecked items in Coverage. A complete audit with disclosed
  limits beats a lost one.

{{inputs}}
