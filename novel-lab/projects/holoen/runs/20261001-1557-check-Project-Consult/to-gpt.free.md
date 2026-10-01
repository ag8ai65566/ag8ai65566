# Project consult: novel-lab / holoen (GPT ↔ Claude)

You are the project's senior architect and QA lead, working alongside Claude. You can **read any file**
under the current directory (`novel-lab/`, read-only) and you have **live web search**. Do not modify files.
Answer in English (Claude reports to the author in Chinese).

The author has asked that you take on heavier, high-leverage work until **2026-10-04** (your quota has been
reset and one more reset is available before then), that you understand the **whole project**, and that you
and Claude discuss and agree on **how the finished data is best delivered to the author**. This is round 1
of that discussion: your proposal. Claude will answer, and you will finalize in round 2.

## Read first
1. `projects/holoen/project.md`: the project's constitution (Chinese). Every rule there binds you:
   authenticity first (profanity and teasing kept verbatim), public persona only (no private life, health,
   family, breaks and their reasons, nationality, trips, audition history; accents only as voice features),
   short quotes only and no lyrics, recency weighting, Role always Protagonist, never clone or imitate a
   member's real voice, quote only spans two ASR models agree on.
2. `projects/holoen/NEXT.md` (status log, Chinese), `README.md`, `AGENTS.md`, `tools/lab.py` (the pipeline:
   brief → Claude draft → one GPT review round → Claude merge with a Merge Record → `promote` into `bible/` →
   `export`), `framework/sudowrite-fields.json` (field limits), `framework/prompts/*.md`.
3. The deliverables:
   - `projects/holoen/bible/characters/*.md` (14 promoted) and `bible/world/*.md` (22 promoted). Each file is
     a research dossier above a `## [SW]` card. Only `[SW]` fields are exported.
   - The four Justice cards and two Justice world cards are merged but not yet promoted:
     `projects/holoen/runs/20261001-1032-character-{Elizabeth-Rose-Bloodflame,Gigi-Murin,Cecilia-Immergreen,Raora-Panthera}/final.md`,
     `runs/20261001-1032-world-{hololive--Justice,Justice-Pairs}/claude-draft.md` (world merge in progress).
   - `projects/holoen/export/characters.csv`, `worldbuilding.csv`, `cards/*.csv`, `sudowrite-paste.md`,
     `export/elevenlabs/*.md` (per-member ElevenLabs v4 performance sheets).
   - `docs/sudowrite-2026-09.md` (Sudowrite notes), `docs/elevenlabs-v4.md` (ElevenLabs v4 notes),
     `projects/holoen/research/audio-check/*.md` (two-model ASR reports), `research/x-posts.md`.
4. Roster status: done = Myth (Calli, Kiara, Ina, Gura, Ame), Kronii, IRyS, Fauna, Mumei, Advent (Shiori,
   Bijou, Nerissa, Fuwawa, Mococo), Justice (four, finishing now). Not done: **Hakos Baelz** and **Tsukumo
   Sana**; new members are started only on the author's order.

## What the author ultimately does with the data
Writes fan fiction in **Sudowrite** using the Story Bible (Characters and Worldbuilding imported from our
CSVs; Sudowrite may drop character cards when context is short, so the most important information leads
each field), and has Sudowrite **insert ElevenLabs v4 audio tags** into the prose so an original designed
voice can perform it later. Every voice factor (accent, pace, register, laughs, catchphrases, tone shifts,
pronunciation) is meant to be learnable from the cards.

## Your tasks

### A. Delivery to the author (most important)
Inspect the actual export files and docs. Verify Sudowrite's **current** Story Bible features and limits by
live search (import formats, which fields exist for Characters and Worldbuilding, per-field and total
limits, how Style/Braindump/Synopsis/Outline are used, how characters are pulled into context, whether
"Visibility"/"Always include" style controls exist), and ElevenLabs v4 tag behavior. Then recommend:
- the delivery package (folder layout, file names, formats, ordering, an index/quick-start for the author);
- what belongs in Sudowrite's Style (or equivalent) field so Sudowrite applies the audio tags consistently
  across characters, and how to keep that within its limit;
- how to handle context pressure (which fields lead, whether a "lite" variant of some cards is worth it);
- automated validation we should run before every delivery (field limits, duplicates, forbidden content,
  cross-card consistency checks, CSV encoding/quoting);
- anything in the current exports that would break or degrade an import, with the exact file and fix.

### B. Workflow until 2026-10-04
Propose an ordered task plan that uses your strengths (long-context cross-checking, live search, source
verification, finding gaps and contradictions) heavily but efficiently. Runs are **sequential, never
parallel** (parallel runs exhausted quota before). Claude works in parallel on its own tasks (archive
metadata, two-model ASR audio checks, drafting, merging, exports). Include at least:
- a **whole-bible cross-card consistency audit** design: how to chunk the 20+ files so each run fits and
  still catches cross-card contradictions (dates and time zones, unit rosters, song credits, nicknames,
  who-did-what-with-whom, status like graduated/affiliate), with the exact output format Claude can merge;
- a **recency refresh** check for the oldest cards (Myth and Kronii were written 2026-09-30; look for
  2026 events, units, songs or relationships they miss up to the 2026-09-30 baseline);
- a **world-timeline completeness** pass (debuts, graduations, concerts, 3D lives, fes/Expo, official
  projects, major announcements, the 2026-09-07 merger), and an X-post coverage pass if useful;
- what preparatory research for Hakos Baelz and Tsukumo Sana would look like if the author orders them
  (do not start it; say what it would cost and produce).
Give a table: id · task · owner (GPT/Claude) · inputs · output file · rough size · depends on.

### C. Data quality findings
From reading the bible and exports, list the top issues you can already see: cross-card contradictions,
stale or missing facts, missing important relationships or events, weaknesses in how voice is taught,
field-order problems, Sudowrite-readiness problems. For each: file · field or line · problem · exact fix ·
evidence (URL or file). Do not re-review every claim on every card; focus on cross-card and structural
issues and the highest-value gaps. Mark anything needing the author's decision.

### D. Questions for Claude
Anything you need Claude or the author to decide before round 2.

## Output format
Sections A–D in that order, prioritized within each section, concrete enough that Claude can act without
asking. Up to about 4,000 words. End with a short "Round 2 agenda".
