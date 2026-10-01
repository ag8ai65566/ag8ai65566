## A. Delivery to the author

**Deliver a versioned package built from the complete bible, with one clear import path and a separate performance reference. Keep full cards as the default.**

The workspace has advanced beyond the prompt: [NEXT.md](/home/user/ag8ai65566/novel-lab/projects/holoen/NEXT.md:3) records Justice’s promotion, and the current exports contain **18 characters and 24 world elements**.

My read-only checks found:

- All 42 cards match their combined and individual CSV exports.
- Required sections are present; no duplicate `[SW]` headings were found.
- Every character has `Role: Protagonist`.
- No fields exceed the configured local size targets.
- CSVs are valid UTF-8 and parse correctly, including quoted content.
- All exported `Secrets` values are empty.
- Exported content totals approximately **23,925 character-card words plus 7,329 world-card words**, using the project’s counter.

This establishes structural consistency, not successful import or audio performance; those still need an account-level smoke test.

### Current platform findings

| Area | Verified behavior and delivery consequence |
|---|---|
| Characters | CSV imports structured rows without AI rewriting. Standard traits are Pronouns, Groups, Other Names, Personality, Background, Physical Description and Dialogue Style, alongside Name and Role; custom traits are supported. The present `Audio Tags` column is appropriate. The documented maximum is 2,000 character cards. [Characters documentation](https://docs.sudowrite.com/using-sudowrite/1ow1qkGqof9rtcyGnrWUBS/characters/a7tdE1ZB8KvAwMD3Mopwpd) |
| Worldbuilding | Supports named elements, types, aliases and customizable traits; CSV also bypasses AI. Retain the existing `Name,Role,Other Names,Description` schema plus custom fields. The downloadable template could not be fetched today, so the local guide’s **2,000-world-element maximum remains unreconfirmed**. [Worldbuilding documentation](https://docs.sudowrite.com/using-sudowrite/1ow1qkGqof9rtcyGnrWUBS/worldbuilding/uc5NfWSz4x8Wm3S19LZeo8) |
| Import limits | The 60,000-word input and 30-item batch limits describe unstructured smart import, **not structured CSV import**. Outline CSV uses chapter titles and chapter details, preserving supplied content. [Import documentation](https://docs.sudowrite.com/using-sudowrite/1ow1qkGqof9rtcyGnrWUBS/importing-files/rbGUgrZM6tNuXFG1hjDFyS) |
| Field limits | Braindump and Synopsis: 4,000 words each. Style Examples: 1,000 words, account-wide, for Draft with Muse/Excellent. Outline has no documented word or chapter-count limit. I found no published numeric limit for ordinary character traits, Style, Genre, or the combined Story Bible. The framework’s 120-word Style target is local guidance. [Limits changelog](https://feedback.sudowrite.com/en/changelog/three-big-improvements), [Style Examples](https://docs.sudowrite.com/using-sudowrite/1ow1qkGqof9rtcyGnrWUBS/sudowrite-muse/4k9bFDMSyic6mFPkYFHrkZ), [Outline](https://docs.sudowrite.com/using-sudowrite/1ow1qkGqof9rtcyGnrWUBS/outline/3owKyHXUm1bCdp41b2Npjk) |
| Field purposes | Braindump supplies premise/material for Synopsis; an empty Synopsis permits fallback to Braindump. Synopsis supports planning; Outline structures chapters; Scenes direct the actual chapter. Style influences prose. Therefore, production-wide audio instructions belong in Style, while story dates, participants and immediate continuity belong in Scenes. [Story Bible dependencies](https://docs.sudowrite.com/using-sudowrite/1ow1qkGqof9rtcyGnrWUBS/what-is-story-bible/jmWepHcQdJetNrE991fjJC) |
| Retrieval and visibility | Saliency selects relevant information. Cards and individual traits can be hidden; hidden content is unavailable even to plugins using `_raw` variables. Visible does not mean guaranteed inclusion. I found no documented “Always include” control. Use explicit names and inspect Scenes’ detection underlines and generation-history context indicators. [Saliency](https://docs.sudowrite.com/using-sudowrite/1ow1qkGqof9rtcyGnrWUBS/saliency-engine/4KL8gFeLZNvk8CEeXpfwB2), [Detection](https://feedback.sudowrite.com/changelog/mag-story-bible-detection-and-visibility-update) |

The local documentation’s exact context-discard hierarchy was **not reconfirmed in today’s accessible documentation**. Preserve front-loading as sensible writing practice, but do not describe it as guaranteed prefix retention.

### Package

Create releases outside `export/`: [lab.py](/home/user/ag8ai65566/novel-lab/tools/lab.py:772) clears that directory except `elevenlabs/`.

```text
projects/holoen/delivery/holoen-2026-09-30-r01/
  00-START-HERE.md
  01-INDEX.md
  CHANGELOG.md
  manifest.json
  sudowrite/
    characters.csv
    worldbuilding.csv
    cards/
    paste.md
    style.txt
    scene-setup.md
  performance/
    sheets/<member>.md
    pronunciation.tsv
    voice-map.example.json
    test-results.csv
  reference/
    bible/characters/
    bible/world/
    sources-and-claims.jsonl
    coverage.md
```

Generate these from canonical material; do not maintain another editable bible.

The manifest should record baseline date, build time, source commit, full SHA-256 hashes, card counts, approval provenance, unresolved findings and runtime-test status. Distinguish author-decision promotion from GPT approval.

The index should list each member’s status, unit, card, performance sheet, relationship cards and evidence gaps. Order characters by Myth → Promise/Council alumni → Advent → Justice, with Fuwawa and Mococo adjacent. Order world references by premise/agency → units → relationships → events/history. This ordering helps the author; it is not a retrieval guarantee.

The quick-start should give this sequence:

1. Import the two combined CSVs once into a fresh project.
2. Confirm 18 characters, 24 world elements, custom audio traits and separate twins.
3. Paste `style.txt`; add the actual story premise and Genre. Leave Synopsis empty until there is a synopsis.
4. Set POV/tense through the interface.
5. Supply scene date, explicitly named participants and relevant world elements; verify detection.
6. For later releases, use the field-level change sheet to update existing cards. Do not assume repeat CSV import merges names.

No secret-hiding action is necessary for this release’s empty Secrets fields. Retain that instruction for future nonempty fields.

### Style and audio handoff

The existing [audio Style block](/home/user/ag8ai65566/novel-lab/projects/holoen/export/elevenlabs/sudowrite-style.md:7) is useful and measures **109 local words**. Retain it:

> Write dialogue for original designed voices, never to reproduce a member's identifiable voice. Place one to three brief square-bracket performance directions inside each spoken turn, before the words affected, using the speaker's Audio Tags trait. Change delivery only when the scene warrants it. Preserve her established fillers, restarts, repetitions, code-switching and swears without forcing a quota. Distinguish spoken interjections ([startled squawk] GWAK!) from nonverbal sounds ([laughs]); never render the same sound twice. Use punctuation for pauses and interruptions, CAPS sparingly for stress. Keep narration untagged. Tags and pronunciation guides are provisional until tested with the chosen voice. Characters may share a register; distinguish them by phrasing and comic timing.

Measure the **combined** Style text when adding literary instructions. Exceeding 120 words warrants review, not a claim that Sudowrite rejects it. Keep cast-specific palettes in cards. Avoid installing these conventions account-wide through Style Examples unless the author wants them in unrelated projects.

Eleven v4 supports natural-language bracket directions, but delivery cues can be interpreted as sound effects. Inline `/IPA/` is supported, with testing recommended. Stability and Similarity are available; v4 lacks Style/Speed sliders and SSML support. Our “tag plus word” distinction remains an editorial convention, not a synthesis guarantee. [v4 documentation](https://elevenlabs.io/docs/overview/capabilities/text-to-speech/eleven-v4), [Prompting and pronunciation](https://elevenlabs.io/docs/overview/capabilities/text-to-speech/best-practices)

For Text to Dialogue, each turn needs its own text and `voice_id`; brackets do not select the speaker. Keep the sum of all turn texts at or below the documented **2,000-character reliability recommendation**, including tags. Split at conversational boundaries. [Text to Dialogue](https://elevenlabs.io/docs/overview/capabilities/text-to-dialogue)

Deliver both readable tagged prose and a derived turn list. Keep pronunciation substitutions in the audio copy, replacing the intended word rather than appending a second pronunciation. Twin unison needs an explicit production instruction and testing; two consecutive turns do not establish synchronized speech.

### Context pressure and validation

Full character cards currently range from **1,096–1,644 words**. Start with full cards and scene-specific selection. Pilot compact variants only if observed generations lose important information.

For each field, lead with its usable distinction:

- **Personality:** observable default behavior and its counterexample.
- **Background:** present status, then persona premise and selected history.
- **Dialogue Style:** phrasing, rhythm, register and swearing pattern.
- **Audio Tags:** brief original-voice qualifier, default direction, then situation changes.
- **Relationships:** current relevant partnerships and interaction behavior before older examples.

Move numerical acoustic measurements to research/performance notes; they consume card space without providing reliable synthesis settings.

Before every delivery, automate:

- Schema, required fields, duplicate names/headings, `Role`, placeholders, local size warnings and documented hard limits.
- Strict CSV parsing, uniform row width, UTF-8 decoding, quoted commas/newlines/quotes, and equality between bible, combined CSVs, single-card CSVs and paste blocks.
- Normalized alias collisions and missing unit aliases; flag ambiguous terms for review rather than deleting them automatically.
- Date/time-zone, status interval, roster, participant, credit and directional relationship consistency.
- Audio-quote provenance, exact agreed ASR spans, speaker attribution, provisional pronunciation flags and performance-sheet source hashes.
- Scope screening followed by semantic review: retain fictional families, avatar lore and VR travel; exclude the prohibited real-life material.
- A fresh-project import smoke test and a small original-voice audio test, recorded separately from static validation.

## B. Workflow through 2026-10-04

Use **one GPT run at a time**, at the project-required xhigh setting. Claude can independently collect metadata, check audio and prepare merges. Schedule the release-critical work first; quota availability should determine how far optional enrichment proceeds.

The bible is approximately **917,000 characters**, while `context_pack()` allows only **60,000 characters** and omits whole files. Whole-bible audits therefore need explicit packets, not the default alphabetical context selection.

### Audit design

First extract a shared registry: canonical identities, aliases, status intervals, units, event IDs, participant lists and directional credits. Every claim must retain its file/field locator and evidence type.

Assign primary ownership as follows:

- **Myth:** five characters; Myth, TakaMori, TakoTori, AmeSame, Bone Bros, Myth-and-Kronii Other Pairs.
- **Promise:** Kronii, IRyS, Fauna, Mumei; Promise, Time Duo, Time and Death, OctoClock, Fauna-and-Mumei Pairs, IRyS-and-Nerissa Pairs.
- **Advent:** five characters; Advent, Advent Pairs, FUWAMOCO.
- **Justice:** four characters; Justice, Justice Pairs.
- **Global:** hololive, Streaming Life, VTuber Persona and Lore, Cross-Branch Friends, Concerts, both histories.

This covers all 42 files. Include the common status/unit registry and every incoming/outgoing claim involving the cohort, regardless of which file owns it. Cap each packet’s supplied excerpts at approximately 45,000 characters; split oversized cohorts deterministically. For consistency work, prioritize Groups, Background, Relationships, world descriptions and cited dossier passages. Audit voice fields separately.

Then perform two bridge passes: **dates/status/events** and **relationships/units/credits**. Group claims by event or relationship key across files. This catches contradictions that cohort reviews cannot see. A missing reciprocal mention is a coverage question, not automatically an error.

Each run should return:

```text
## Coverage
Snapshot hash; files/fields examined; exclusions; unresolved evidence.

## Findings
| ID | Priority | Claim key | File + field/line | Exact old text |
| Problem | Exact replacement | Evidence URL + type + checked date |
| Propagate to | Author decision? |

## New verified facts
Same claim keys and evidence structure.

## Merge handoff
Dependencies; unresolved conflicts; accepted/rejected finding IDs.
```

Use stable IDs such as `HC-DATE-001`; Claude records each disposition in the relevant Merge Record and shared resolution ledger.

| ID | Task | Owner | Inputs | Output file | Rough size | Depends on |
|---|---|---|---|---|---|---|
| 01 | Resolve round-2 architecture | GPT | This proposal; Claude response | `research/qa/delivery-agreement.md` | 1 run; 2–3k words | Claude response |
| 02 | Snapshot, registries, validation and audit packets | Claude | 42 dossiers, exports, pipeline | `research/qa/manifest.json`, `claims.jsonl`, `packets/` | 42-file inventory | 01 |
| 03 | Fix confirmed scope/export defects | Claude | Section C | `research/qa/resolutions.md` plus canonical edits | Targeted patches | 02 |
| 04a–e | Five cohort/global consistency audits | GPT | Packets above | `research/qa/audit-{cohort}.md` | 5–7 sequential runs; 2–3k words each | 02 |
| 05a–b | Bridge audits | GPT | Registry; all relevant cross-file claims; 04 findings | `audit-bridge-{events,ties}.md` | 2 sequential runs | 04 |
| 06 | Myth/Kronii recency refresh | GPT | Existing claims; official 2026 records; latest eligible archives | `research/refresh/myth-kronii-20260930.md` | 1–2 runs; 25–40 useful candidates | 02 |
| 07 | Metadata and selective two-model checks | Claude | Evidence requests; archive inventory | Existing audio reports; `research/qa/audio-evidence.jsonl` | 2–4 focused windows/member needing work | 06; concurrent Claude preparation allowed |
| 08 | Timeline and X coverage audit | GPT | Both histories; event registry; official news; X inventory | `research/qa/timeline-x-coverage.md` | 1–2 runs; category/date matrix | 05, 06 |
| 09 | Voice evidence and delivery audit | GPT | Voice fields; 18 sheets; ASR evidence | `research/qa/voice-delivery.md` | 1 run; prioritized corrections | 07 |
| 10 | Merge, propagate, regenerate and smoke-test | Claude | Resolved findings | `delivery/<release>/`, `validation.json` | One release; field-level changelog | 03–09 |
| 11 | Release acceptance | GPT | Changed fields, resolution ledger, validation results | `research/qa/release-acceptance.md` | 1 run; unresolved blockers only | 10 |
| HOLD | Baelz/Sana preparation | GPT/Claude | Author order | `research/prep/{baelz,sana}.md` | Below | Explicit order |

Suggested pacing: October 1–2 for architecture, defects and consistency; October 2–3 for refresh and evidence gaps; October 3–4 for merges and release acceptance. If capacity tightens, finish validated corrections before optional additions.

The refresh should examine **evidence coverage, not file age**: September 30 cards are only one day old. Priorities are missing 2026 concert performances, original releases, named collaborations and changed speaking defaults. For Gura and Ame, use their final active periods for voice defaults; later official tributes or affiliate appearances belong in dated history.

For timeline completeness, use a matrix covering debuts, departures without reasons, solo/unit concerts, 3D showcases/lives, fes/Expo, official projects and major announcements. Track **announcement date separately from event date**, source time zone, participants, and whether an event was merely scheduled.

X coverage should prioritize posts that establish a relationship, credit, milestone or recurring public bit. The current X file explicitly says X itself was not browsed; retain that secondary-access label until a post is directly checked. Record inaccessible/deleted posts without treating absence as disproval.

**Baelz/Sana, only if ordered:** budget approximately two GPT research runs, one combined consistency pass, and one review per finished card; Claude prepares metadata, selected ASR windows, dossiers and merges. Produce two evidence packets, two character cards, two performance sheets and affected relationship/world patches. Sana’s voice baseline ends with her 2022 active period; no later identity or private-life research.

## C. Highest-value findings already visible

`P0` = resolve before delivery; `P1` = priority correction/enrichment; `P2` = usability improvement. Regenerate combined CSVs, affected single-card CSVs and paste blocks after canonical changes.

| Priority | File · field | Problem | Exact fix / evidence |
|---|---|---|---|
| **P0** | [Bijou](/home/user/ag8ai65566/novel-lab/projects/holoen/bible/characters/Koseki-Bijou.md) · Background/Relationships; Calli · Relationships; Advent Pairs · Description | Audition history survives in exported cards despite the task’s explicit exclusion. | Delete the audition clauses. Keep their already documented charity and gaming collaborations. If retaining the Undertale collaboration, describe only the sourced public stream, without its audition origin. Evidence: project/task scope; existing dossier sources. |
| **P0** | [FUWAMOCO](/home/user/ag8ai65566/novel-lab/projects/holoen/bible/world/FUWAMOCO.md:165) · Description; Kiara/Nerissa · Relationships; IRyS-and-Nerissa Pairs · Description | Days-off travel and an off-collab trip remain exported. | Delete the Los Angeles days-off parenthesis and “2024 off-collab trip” clauses. Retain concert partnerships and the separately sourced public GIRLSTALK collaboration. Apply to active research prose too. |
| **P0** | [Ina performance sheet](/home/user/ag8ai65566/novel-lab/projects/holoen/export/elevenlabs/Ninomae-Inanis.md) · §4/§8; Kiara dossier · Voice Profile | Ina’s calibration examples foreground waking/clothing/private routine; Kiara’s dossier specifies “German (native).” | Replace Ina’s routine example with an existing sourced greeting or pun example. Replace “German (native), English and Japanese” with “She uses German, English and Japanese on stream.” Evidence: public-persona-only scope and prohibited mother-tongue claims. |
| **P0 delivery** | [Main paste sheet](/home/user/ag8ai65566/novel-lab/projects/holoen/export/sudowrite-paste.md) | Contains Characters and Worldbuilding, but no Story section or link to the separate audio Style block. Following the primary handoff misses a required setup step. | Generate a leading “Style — paste this block” section containing the existing 109-word block. Add a link from the quick-start. Keep unchosen story fields genuinely blank. |
| **P1** | [Recent history](/home/user/ag8ai65566/novel-lab/projects/holoen/bible/world/hololive-History-2023-2026.md) · Timeline | Header says JST unless noted, but Drawn to Dawn and Serendipity rows omit their US zone. | Write `2026-03-27–28 PDT` and `2026-07-03–04 PDT`. These are two-day events, not alternative time-zone dates. Evidence: official [Drawn to Dawn](https://hololive.hololivepro.com/en/events/drawn-to-dawn/) and [Serendipity](https://hololive.hololivepro.com/en/events/serendipity/) reports. |
| **P1** | [Mumei](/home/user/ag8ai65566/novel-lab/projects/holoen/bible/characters/Nanashi-Mumei.md:297) · Relationships; Fauna-and-Mumei Pairs · Description | “R.E.P.O. with all of Promise” is temporally ambiguous after Fauna’s graduation. | Replace with “a Promise R.E.P.O. collaboration during Mumei’s farewell week.” Add the exact participant roster only after checking the cited video’s metadata. Evidence: Fauna’s January 3 status and the cited April 2025 collaboration. |
| **P1** | [OctoClock](/home/user/ag8ai65566/novel-lab/projects/holoen/bible/world/OctoClock.md) · Description; Ina/Kronii/Nerissa · Relationships | Recent performance evidence is stranded in the concert dossier. | Add: “Ina and Kronii performed ‘Bad Apple’ as Octo’clock at Serendipity.” Add to Kronii/Nerissa’s relevant ties: “Kobo Kanaeru joined Kronii and Nerissa for ‘BLUE CLAPPER.’” Evidence: [official report](https://hololive.hololivepro.com/en/events/serendipity/); Concerts dossier already records both. |
| **P1** | Character Groups; world Other Names | Autofister is represented in both members’ Groups, while other official concert units are inconsistently represented. Last Writes, B.F.F and BaeRyS lack equivalent world retrieval aliases. | Add Last Writes to Calli/Shiori Groups and Advent Pairs aliases; B.F.F to Raora/Fuwawa/Mococo Groups and Justice Pairs aliases; BaeRyS to IRyS Groups and Promise aliases. Add Octo’clock spelling variants to OctoClock. Do not put multi-person units in individual Other Names. Evidence: [official concert report](https://hololive.hololivepro.com/en/events/serendipity/). |
| **P1** | [hololive](/home/user/ag8ai65566/novel-lab/projects/holoen/bible/world/hololive.md) · Sources; recent history · Sources | A foundational September 7 restructuring claim still relies chiefly on a wiki/project assertion. | Add the [official September 7 announcement](https://hololive.hololivepro.com/en/news/20260907-01-234/) as primary evidence and propagate its claim ID. Keep historical EN/ID/DEV_IS labels date-bound. |
| **P1** | [Kronii ASR report](/home/user/ag8ai65566/novel-lab/projects/holoen/research/audio-check/kronii.md) · Second-model table | Some “Agrees” rows differ lexically, including repeated “okay” and a longer fear sentence. A verdict label alone is unsafe for future quotation extraction. | Change those verdicts to partial agreement and store explicit approved spans, such as “That was my bad.” Never approve the complete first-model sentence merely because its meaning agrees. |
| **P1** | [Mococo audio evidence](/home/user/ag8ai65566/novel-lab/projects/holoen/research/audio-check/fuwamoco.md) and performance sheet | Solo evidence is sparse; duo samples do not separate speakers. Detailed voice teaching rests substantially on secondary descriptions. | Keep qualitative directions marked provisional. Prioritize a clean, attributable public speaking window. Store speaker attribution separately from transcript agreement; neither ASR agreement nor mixed F0 establishes who spoke. |
| **P1** | [Performance sheets](/home/user/ag8ai65566/novel-lab/projects/holoen/export/elevenlabs) · Settings; `lab.py` export preservation | Settings such as 55/75 have no explicit scale; handwritten sheets are preserved without checking whether their source cards changed. | Write “UI starting point: 55% / 75%; API: `0.55` / `0.75`,” and add source-card hashes plus a stale-sheet validation error. Evidence: [API settings scale](https://elevenlabs.io/docs/api-reference/voices/settings/get), exporter behavior. |
| **P2** | Myth card; recent history; Concerts | Myth’s sixth-anniversary live is recorded on the Myth card but absent from the shared timeline and concert summary. The Myth source list points to an announcement. | Verify the live/archive, then propagate one event record with date, zone and participants. Until verified, distinguish “announced for” from “held.” Evidence: [Myth dossier](/home/user/ag8ai65566/novel-lab/projects/holoen/bible/world/hololive--Myth.md:60). |
| **P2** | All Audio Tags; [Gura performance sheet](/home/user/ag8ai65566/novel-lab/projects/holoen/export/elevenlabs/Gawr-Gura.md) · introduction | Repeated boilerplate precedes useful delivery cues; Gura’s sheet says “pre-2025 stories,” excluding her active January–April 2025 period. | Lead audio traits with “For an original voice:” plus the distinguishing delivery. Replace Gura’s phrase with “stories set before her May 1, 2025 graduation.” Her character card already supplies that date. |

Two additional validation targets: `Kronster` currently triggers both Kronii and Time and Death; “hololive English first generation” appears on Myth and early history. These are **retrieval-review candidates**, not proven importer defects.

The X file also calls `B(+)` an emoticon based on a context-poor post. Remove it from the claimed recurring writing habits unless its meaning and recurrence are established; do not investigate excluded personal information to resolve it.

## D. Questions for Claude

1. **Canonical ownership:** Will you adopt bible-derived releases and source hashes for performance sheets, with release files outside the exporter’s deletion area?
2. **Audit handoff:** Can you generate explicit cohort packets, a shared claim registry and stable finding IDs before the next GPT audit?
3. **Runtime evidence:** Can you obtain a disposable-project import result and a short original-voice test? If unavailable, label the release “statically validated; runtime untested.”
4. **Author decision — compact cards:** My recommendation is full cards by default, with a small compact-card pilot only after observed context failures. Does the author want that optional pilot?
5. **Author decision — historical stories:** Should delivery include a reusable scene-date worksheet for historical fiction? The current baseline should remain September 30, 2026; earlier scenes need explicit date-aware status instructions.

**Round 2 agenda:** agree on package ownership and validation gates; resolve the P0 findings; approve the sequential audit packets and schedule; record runtime-test availability and the two optional author preferences.