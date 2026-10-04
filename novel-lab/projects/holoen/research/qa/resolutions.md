# QA resolution ledger (holoen)

Stable IDs for every finding the QA program raises, with Claude's disposition. Statuses: **applied** (in the
bible at the commit named), **pending** (accepted, not yet done; owner task named), **deferred** (moved to a
later task), **rejected** (reason given). Each applied fix is also recorded in the affected card's Merge Record.
Source of the CONSULT-* findings: `runs/20261001-1557-check-Project-Consult/gpt-free.md` (round 1) and
`runs/20261001-2050-check-Project-Consult-R2/gpt-free.md` (round 2).

| ID | Finding | Status | Where / commit |
|---|---|---|---|
| CONSULT-P0-001 | Pre-debut private history in exported cards (Bijou, Calli, Advent Pairs) | applied | 6a9212f |
| CONSULT-P0-002 | Private-life activity outside streams (FUWAMOCO, IRyS-and-Nerissa Pairs, Kiara, Nerissa) | applied | 6a9212f |
| CONSULT-P0-003 | Ina's private-routine example (sheet, card, audio report); a language-background claim (Kiara) | applied | 6a9212f |
| CONSULT-P0-004 | Paste sheet lacked the audio Style block | applied (exporter writes it first) | 6a9212f |
| CONSULT-P1-001 | History 2023–2026: Drawn to Dawn and Serendipity rows unzoned | applied (PDT) | snapshot commit |
| CONSULT-P1-002 | Mumei / Fauna-and-Mumei: "R.E.P.O. with all of Promise" ambiguous | applied (IRyS, Kronii, Bae; archive F_EVW5Ig5QE) | snapshot commit |
| CONSULT-P1-003 | OctoClock "Bad Apple"; Kobo's "BLUE CLAPPER" with Kronii and Nerissa | applied | snapshot commit |
| CONSULT-P1-004 | Official Serendipity units missing from Groups / world aliases | applied (Last Writes, Octo'clock, Rocku Wawa, BaeRyS, Bloodraven, B.F.F; Autofister already present) | snapshot commit |
| CONSULT-P1-005 | 2026-09-07 restructuring relied on a wiki | applied (official announcement cited on "hololive") | snapshot commit |
| CONSULT-P1-006 | Kronii ASR report: "Agrees" rows that differ lexically | applied (Kronii rows rewritten by hand; all 151 other bare "Agrees" rows given computed shared spans by `tools/asr_spans.py`; 36 partial rows listed in `research/audio-check/partial-spans.md` for task 09) | this commit |
| CONSULT-P1-007 | Mococo: sparse solo evidence; speaker attribution | task 07 part applied: whole-channel archive search found no other attributable solo window (2026 "MOCOCO POV" is a multi-member role-play; 2024 candidates include her twin); attribution basis now stated separately in research/audio-check/fuwamoco.md; card and sheet say directions stay provisional. Quotation gate stays with task 09 | this commit |
| CONSULT-P1-008 | Performance sheets: settings scale; stale-sheet hashes | scale applied (UI % and API decimals); hashes pending (task 10 release builder) | snapshot commit |
| CONSULT-P2-001 | Myth sixth-anniversary live missing from shared timeline | applied and closed 2026-10-02: verified as held (hololive English channel VOD title; official posts), 2026-09-19 PDT, with the new song "THIS IS MYTH"; propagated to Myth, TakaMori, TakoTori, History 2023–2026, Concerts and the three members (task 06, research/refresh/myth-kronii-20260930.md) | this commit |
| CONSULT-P2-002 | Audio Tags boilerplate before the distinguishing cue | deferred (task 09, all 18 cards at once) | — |
| CONSULT-P2-003 | Gura sheet "pre-2025 stories" excluded her active 2025 months | applied | snapshot commit |
| CONSULT-VAL-001 | Alias "Kronster" on Kronii and Time and Death | applied (removed from Time and Death) | snapshot commit |
| CONSULT-VAL-002 | Alias "hololive English first generation" on Myth and History to 2022 | applied (removed from History to 2022) | snapshot commit |
| CONSULT-X-001 | Calli's "B(+)" listed as a recurring emoticon | applied (removed; the context-poor post dropped) | snapshot commit |
| CONSULT-R2-001 | Incoming claims must include aliases, unit names, table rows and bullets | applied (`tools/qa_packets.py`) | snapshot commit |
| CONSULT-R2-002 | Packet inventory and SHA-256 map | applied (`research/qa/manifest.json`, packet headers) | snapshot commit |
| CONSULT-R2-003 | Registry: status intervals, event precision, directional credits, reference-only people | applied (registry v2; bounded, non-exhaustive) | snapshot commit |
| CONSULT-R2-004 | Promotion provenance outside `runs/` | applied (`research/qa/promotions.md`) | snapshot commit |
| CONSULT-R2-005 | Release candidate + acceptance tied to its manifest hash; finding priority ≠ validation severity | pending (task 10–11) | — |

New audit findings are appended below with their own IDs (`{COHORT}-{TYPE}-{NNN}`, `BR-…`).
| CLAUDE-SCOPE-001 | Process notes that dated or described excluded matters (four cards and x-posts) | applied (generalized to the author's rule; no dates or reasons) | this commit |
| ADVENT-SCOPE-001 | Elizabeth: a private day-off plan in an incoming Voice Profile bullet | applied (deleted) | this commit |
| ADVENT-SCOPE-002 | Pre-debut discovery history (how a member first found hololive/VTubers): Shiori, Advent Pairs, Cross-Branch | applied; Claude propagated the same rule to Raora (Korone row and SW sentence) and Justice Pairs | this commit |
| ADVENT-SCOPE-003 | Nerissa: off-stream habits and private possessions (merch, plush, figures, cooking) | applied (Nerissa, IRyS-and-Nerissa Pairs, Cross-Branch) | this commit |
| ADVENT-SCOPE-004 | History 2023–2026: invented private backstage scene hook | applied (replaced with a public tour-stage hook) | this commit |
| ADVENT-TIE-001 | Cecilia–Mococo Chrono Trigger off-collab widened to both twins | applied (Mococo only) | this commit |
| ADVENT-TIE-002 | FUWAMOCO MORNING #167 guest hosts read as Mococo | applied (Gigi and Cecilia guest-hosted) | this commit |
| ADVENT-UNIT-001 | "kouhai to Myth and Promise from day one" used the later Promise name | applied (Myth, Project: HOPE, Council at debut) | this commit |
| ADVENT-STATUS-001 | Advent status heading used the check date instead of the 2026-09-30 baseline | applied | this commit |
| ADVENT-DATE-001 | Shiori/Bijou: unzoned debut sentence implied all five debuted 2023-07-30 | applied (JST; staggered launch) | this commit |
| ADVENT-DATE-002 | Nerissa's 3D date unzoned | applied (2024-08-09 PDT, two places) | this commit |
| ADVENT-COVERAGE-001 | Registry missed the FUWAMOCO debut (2023-07-31) | applied (generator regex fixed; registry rebuilt; both twins 2023-07-31) | this commit |
| ADVENT-QUOTE-001 | FUWAMOCO: stitched "Right! … Exactly." and a turn attributed to the other twin | applied (paraphrased; no turn attribution) | this commit |
| ADVENT-QUOTE-002 | Elizabeth: "workaholics like me" past the shared span | applied (paraphrase in three places) | this commit |
| CONSULT-P0-002 / CLAUDE-SCOPE-001 (residual) | Leftover private-life process notes (FUWAMOCO, Mococo) | applied (Advent audit) | this commit |
| CONSULT-P1-006 (residual) | Nerissa N20 and Shiori quotations crossing shared spans | applied (Advent audit; Nerissa's Voice Profile, Sample Lines and sheet also split into separate shared spans) | this commit |
| CONSULT-R2-001 (residual) | Incoming-claim retrieval was case-sensitive and missed owned world-card aliases | applied (`tools/qa_packets.py`, `re.I`, world-card names and aliases) | this commit |
| CLAUDE-SCOPE-002 | Process notes still naming the excluded details they removed (Merge Records of Kiara, Nerissa, Calli, Bijou, Ina, FUWAMOCO, Mumei, Raora; FUWAMOCO and Mumei audio reports; one X post in x-posts) | applied (generalized to "private-life material removed"; the post dropped) | this commit |
| CLAUDE-QUOTE-001 | 23 quotations ran past the span both ASR models share (Ame, Calli, Elizabeth, Gigi, Gura, Bijou, Kiara, Mumei, Nerissa, Raora; Ame, Gigi and Gura sheets) | applied (trimmed to the shared run, split into separate shared quotations, or paraphrased; one apostrophe-only difference documented). `tools/span_check.py` now checks every card and sheet against `partial-spans.md`, and V13 fails automatically on any overrun. Quotes never second-model checked remain task 09's | this commit |
| CLAUDE-SCOPE-003 | Process notes and scope headers that tied the break rule to particular members (four Myth-era cards; three Justice cards and the Justice world card) | applied (member-specific notes removed; each card keeps only the general privacy statement) | this commit |
| TASK-06 | Myth/Kronii recency refresh (done by Claude to save GPT quota) | 9 facts applied, 5 candidates held for better evidence: research/refresh/myth-kronii-20260930.md; GPT reviews the additions in the Myth cohort audits | this commit |
| CLAUDE-QUOTE-002 | span_check missed wrapped quotations and the performance sheets' example blocks; `asr_spans.py` re-runs dropped earlier partial rows | applied: both tools fixed (partial-spans.md rebuilt from every report); eight clear overruns trimmed (Calli, Gigi, IRyS, Nerissa, Raora; IRyS, Raora and Shiori sheets); the remaining hand-judged candidates listed in research/qa/span-candidates.md for task 09 | this commit |
| AUTHOR-2026-10-02 | Author order: add Hakos Baelz; do not make Tsukumo Sana | in progress: Bae's character card, "Hakos Baelz Pairs," the performance sheet and audio report (research/audio-check/bae.md) drafted; Bae ties added to 13 cast cards and to Promise, Concerts and Cross-Branch Friends; CHADCast recorded as an official unit; GPT's one xhigh claim-check review queued first (runs/20261002-0236-character-Hakos-Baelz) | this commit |
| CLAUDE-SCOPE-004 | Calli's Cross-Branch entry recorded how she came to VTubers (pre-debut history, ADVENT-SCOPE-002 rule) | applied (clause removed) | this commit |
| CLAUDE-TOOLS-001 | The roster was hard-coded in several places (18/24/18 counts, reference-only lists) | applied: `qa_packets.COHORTS` is the single roster; release counts, START-HERE and V02 derive from it, and V02 fails when the bible and the roster differ; packets skip a rostered card that is not yet promoted | this commit |
| CLAUDE-TOOLS-002 | A draft package claimed the roster counts (19/25) while its CSVs held only the promoted cards (18/24), and shipped Bae's performance sheet without her card | applied: package counts, INDEX, CHANGELOG and START-HERE count the cards actually shipped; a sheet ships only with its card; START-HERE names what is not yet included; `CAST_ORDER`/`WORLD_ORDER` must equal the COHORTS roster (assert) | this commit |
| CLAUDE-TOOLS-003 | The quote gate matched any partial ASR row by five shared words, so a wiki quote (Cecilia's "Ew! Get away from me, you FREAK!") was flagged against an unrelated FUWAMOCO stream line | applied: a report row gates only files that cite its video (a performance sheet counts its card's citations); `span_check.py --write` regenerates `span-candidates.md` (40 → 31 rows; the 9 dropped were all unrelated-video matches) | this commit |
| CLAUDE-GUIDE-001 | The author needed one place that says where to get the data and where each file goes in Sudowrite | applied: `framework/templates/start-here-zh.md` is the package's 00-START-HERE (Chinese): download, file → Sudowrite placement, smoke test, project setup, scene habits, ElevenLabs, updates, FAQ; scene-setup states the date zone rule | this commit |
| AUDIT-MYTH1 | Cohort audit myth1 (Calli, TakaMori): 38 rows | applied except MYTH-EXPORT-001 (rejected: project label); details in research/qa/audit-myth1.md | 2026-10-03 merge |
| AUDIT-MYTH3 | Cohort audit myth3 (Kiara, Other Pairs, TakoTori): 51 rows | partly applied; MYTH-QUOTE-001 and MYTH-SCOPE-005 have residuals in snapshot fa69d71; MYTH-QUOTE-004 remains open pending quotation-gate resolution. MYTH-SCOPE-002 adapted to keep the author's public-performance shorthand; MYTH-COVERAGE-001 superseded; MYTH-VOICE-001 rejected (label) | 2026-10-03 merge |
| AUDIT-JUSTICE | Cohort audit justice: 36 rows | applied; two COVERAGE rows superseded by run F; EXPORT-001 rejected (label) | 2026-10-03 merge |
| AUDIT-GLOBAL | Cohort audit global: 60 rows | applied (including the parser fixes in tools/qa_packets.py); overlaps closed by justice and myth1 | 2026-10-03 merge |
| CLAUDE-SCOPE-003 | Merge Records naming excluded topics (15 cards) | applied (genericized) | 2026-10-03 merge |
| AUDIT-MYTH4 | Cohort audit myth4 (Ina, TakoTori): 34 rows | applied in full; this also closes the myth1/myth3 residuals that myth4 flagged | 2026-10-04 merge |
| AUDIT-MYTH2 | Cohort audit myth2 (Gura, Ame, Myth, AmeSame, Bone Bros) | applied in full, including re-raised myth3 residuals | 2026-10-04 merge |
| AUDIT-PROMISE | Cohort audit promise (Kronii, IRyS, Fauna, Mumei, Bae and pair cards) | applied; PROMISE-QUOTE-001 adapted to the two-model shared span; one CONSULT-P1-006 row not applied (both models share the longer span) | 2026-10-04 merge |
| AUDIT-BRIDGE-EVENTS | Bridge audit of dates, zones and status | applied; registry rows fixed in tools/qa_packets.py (date parser) and by regeneration | 2026-10-04 merge |
| AUDIT-BRIDGE-TIES-EXTERNAL | Bridge audit of ties with external participants (rosters, credits, Groups, quotations, packet coverage) | applied in full; the TakaMori finale bullet paraphrased under MYTH-QUOTE-001; the generator now recovers each card owner in her own relationship rows | 2026-10-04 merge |
| AUDIT-JP | Cohort audit jp (Suisei, AZKi, Ayame, Okayu, JP Senpai Pairs) | applied in full; exclusion-note wording generalized across all audio reports; JP-QUOTE-001 deferred to the project-wide quotation pass (voice-delivery.md, blocks V13) | 2026-10-04 merge |
| AUDIT-JP2 | Cohort audit jp2 (Marine, Noel, Lamy, Botan, Vivi, JP Senpai Pairs 2) | applied; AZKi seniority rows keep the neutral jp label (she joined hololive in 2022), Okayu→Noel set to JP kouhai; Fauna scope redaction done by hand in the audio report | 2026-10-04 merge |
| QUOTE-INVENTORY | 93 exported spoken lines resting only on secondary transcriptions (jp:JP-QUOTE-001 and the project-wide pass) | **author decision 2026-10-04: B**, kept as an author exception; three lines upgraded by two-model checks (Shukkō, Ohamassuru, Bruh) | 2026-10-04 |
| AUDIT-HOLOX | Cohort audit holox (La+, Lui, Koyori, Chloe, Iroha, holoX) | applied; Japanese-delivery rows already satisfied by the post-v4 conversion; Mumei seniority rows by hand; Nerissa Relationships trimmed to 348 words | 2026-10-04 merge |
