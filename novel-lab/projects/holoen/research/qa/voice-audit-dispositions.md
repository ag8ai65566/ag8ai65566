# Task-09 voice audits: dispositions (working ledger)

The voice audits are one GPT xhigh round per cohort: v1 Myth + Promise, v2 Advent + Justice, v3 the JP nine and
v4 holoX. Claude merged them on the author's order of 2026-10-03 ("你現在可以開始做你(CLAUDE)應該做的任務了").
Each card's Merge Record lists the IDs applied to it. Sheets are edited in place under `export/elevenlabs/`.
`research/qa/voice-delivery.md` is the V13/V19 attestation. It is written only after all four audits are merged.

Tools: `tools/voice_apply.py <run>/gpt-free.md` handles exact replacements. Rows it could not pair were applied by
hand, with the same old → new text. The span check (`tools/span_check.py holoen`) reports 0 quotes outside a
shared ASR span after each merge.

## v1: Myth + Promise (runs/20261002-0755-check-QA-voice-v1)

| IDs | Disposition |
|---|---|
| V1-001, V1-002 | Applied to all nine cards and sheets except Baelz, whose card already used the newer wording. The cards got the provisional-direction boilerplate. A note after each sheet's §1 heading says the timbre and laughter are design choices. |
| V1-003, V1-004 | Applied. "American English" and "American accent" were removed from the eight cards and the sheet prompts. They now read "English (no regional accent assigned)" and "English speech with no prescribed regional accent". |
| V1-005, V1-006 | Applied. The Register and With-people prefixes now say these are provisional scene directions. Secondary labels survive into the exported fields. |
| V1-007 – V1-012 (Calli) | Applied. The kana guide is marked untested. The palette examples are split into separately attributed ASR excerpts. |
| V1-013 – V1-016 (Kiara) | Applied. "Subdued scene" situation. A Style demo replaces the unsourced tired line. Kana guide. |
| V1-017 – V1-020 (Ina) | Applied. Secondary labels. A Style demo replaces the tangent quote. The sign-off is quoted only within its shared span. |
| V1-021 – V1-025 (Gura) | Applied. "Hello? Hello? Hello?" is placed as a microphone check (ASR excerpt), not as her default opening. |
| V1-026 – V1-030 (Ame) | Applied. A health complaint line was deleted (out of scope). Hiccups are marked as an optional sparse scene effect. Name order is fixed. |
| V1-031 – V1-034 (Kronii) | Applied. The imitation framing is removed. The opening is now a Style demo. §8 is reframed as an assembled performance exercise. |
| V1-035 – V1-039 (IRyS) | Applied. "Outfit speculation" situation. `[slight smirk]` becomes `[sly, lightly amused]`. |
| V1-040 – V1-043 (Fauna) | Applied. `[theatrical, clearly enunciated]` for game text. The alum note now covers the period through her 2025-01-03 graduation. |
| V1-044 – V1-048 (Mumei) | Applied. "don don" is labelled secondary. "Opening self-correction" situation. Alum note through her 2025-04-27 graduation. Kana guide. |
| V1-049 (Baelz) | Applied. The Australian accent is unassigned pending an in-scope listening check. The secondary description is kept. |
| V1-050 | Applied. Kana guides (Calli, Kiara, Ina, Mumei) are marked provisional and untested. |

Shared guide (`docs/elevenlabs-v4.md`), revised per v1:
- It is retitled around an original voice performing her lines, with no imitation framing.
- Cross-language rows no longer imply a native accent.
- Measured pitch and rate are research context, not synthesis targets.
- Spoken signature words take tag + word; nonverbal sounds are tag-only.
- Japanese names get kana guides marked untested.

## v2: Advent + Justice (runs/20261002-0755-check-QA-voice-v2)

| IDs | Disposition |
|---|---|
| V2-001 | Applied to all nine cards (the Audio Tags boilerplate) and all nine sheets (the §1 heading "original voice; provisional design choices"). |
| V2-002 – V2-010 | Applied. Regional accents were removed from cards and sheet prompts for Shiori, Bijou, Nerissa, Fuwawa, Mococo, Elizabeth, Gigi, Cecilia and Raora. The text now reads "English; regional accent unassigned pending an in-scope listening check" in cards and "English-speaking" in prompts. Standalone Voice & Delivery text is marked "Provisional original-voice direction". Gigi's research note was aligned too. |
| V2-011 – V2-014 (Shiori) | Applied. The apology is conditional. The horror row is relabelled "Horror-trailer commentary" and loses its inserted scream. The §8 note is rewritten. Two comfort/dismay lines are labelled as secondary transcriptions. |
| V2-015 – V2-019 (Nerissa) | Applied. The official introduction keeps the group possessive. The caveman story is cut to one contiguous shared span. "Ope?!" is a proposed spoken use of a written post, delivery unverified. Partner tags with romantic intent are replaced by "scripted public-persona joke" directions, on both Nerissa's and Shiori's sides. "I need to stop swearing so much" is a sampled self-comment, not a routine. |
| V2-020 – V2-021 (Fuwawa) | Applied. The sneeze signature is removed from Fuwawa (it is Mococo's). The §8 greeting is separated from the wiki line. |
| V2-022 – V2-024 (Mococo) | Applied. The break wording is removed from the sheet. Palette respellings are labelled Style demo. "Bau bau!" is dropped from the wiki line. Line 5 is a Style demo. The card uses the plain "Nooo!" spelling. |
| V2-025 – V2-028 (Elizabeth) | Applied. "Fictional character bit" situation. "Workaholic? Me? Never." is a Style demo. The sign-off and "Huzzah!" are separate ASR excerpts. The §8 note says line 4 is in-game commentary. |
| V2-029 – V2-030 (Gigi) | Applied. The §8 note is rewritten. `[vocal percussion]` replaces `[sound effects]` on the card and the sheet. |
| V2-031 – V2-033 (Cecilia) | Applied. The sign-off is one shared excerpt under `[warm]`. "Spin to win!" is dropped from line 1. `[mock-dramatic] dun dun dun` is a Style demo. |
| V2-034 – V2-036 (Raora) | Applied. The joined mock-stern line is cut to one span. The sign-off is one shared excerpt. "I'm a hater now" is no longer used as the observed example for game frustration. |
| V2-037 | Applied. The kana guides for Shiori, Bijou, Fuwawa and Mococo are provisional and untested. |
| V2-038 | Applied. Wiki-only catchphrases are labelled "SECONDARY transcription, wiki; not audio-verified" on the twins' cards. The repeated instances in Dialogue Style are labelled as wiki transcriptions. |

## v3: the JP nine; v4: holoX

Pending. v3 has landed. v4 is queued in GPT and runs after the 2026-10-04 quota reset.
