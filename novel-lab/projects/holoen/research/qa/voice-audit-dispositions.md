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

## v3: the JP nine (runs/20261002-1657-check-QA-voice-v3)

GPT attested the Noel and Lamy cards and sheets as OK. The other seven were OK after the listed findings.

| IDs | Disposition |
|---|---|
| V3-001 (Suisei) | Applied. The two "warukunai" remarks are separate ASR excerpts with their own timestamps, in §3 and §4. |
| V3-002, V3-003 (Suisei) | Applied. The English introduction is official profile wording. "Hi, honey!" keeps its secondary label in the exported Audio Tags. |
| V3-004 – V3-006 (AZKi) | Applied. Her self-naming comes from the April Fools 2026 debut parody, not habitual third-person speech; the dossier note is aligned. The §8 note restores the parody context, and the palette rows are labelled "debut parody". The giggle after a flourish is optional and provisional (§3, §4, §5). |
| V3-007, V3-008 (Ayame) | Applied. "Urusai!" and "Komatta hitotachi." are separate excerpts in §3, §4, §8, the card's Dialogue Style and its palette table. The §8 note is renumbered. "Yo da yo!" carries its secondary label in §3 and §4. |
| V3-009, V3-010 (Ayame, Okayu) | Applied. "Kawayo" is documented viewer vocabulary, not her required filler. Both cards' reading guides are marked provisional and untested. |
| V3-011, V3-012 (Okayu) | Applied. "Nori de" is one sampled occurrence. §7 lists defaults to avoid, not absolute bans. |
| V3-013 (Marine) | Applied. §7 lists defaults to avoid. Pace and volume follow the scene. |
| V3-014 (Botan) | Applied to the sheet and the card's Voice & Delivery: a proposed horror-scene direction informed by secondary descriptions. |
| V3-015 (Vivi) | Applied. Line 1 is a Style demo adapted from archived title wording. |
| Merge handoff 3 (shared guide) | Already satisfied by the v1 revision of `docs/elevenlabs-v4.md`: measurements are research context, not synthesis targets, and nonverbal sounds are tag-only. |
| Harmonization (Claude) | The VOICE-V2-001 Audio Tags opening and sheet §1 heading were applied to all nine, so the 2026 JP cards use the same provisional wording as the EN cast. |

## v4: holoX (runs/20261003-2322-check-QA-voice-v4)

GPT attested all five holoX cards and sheets as OK after the listed findings. Its prompt carried both of the author's
decisions of 2026-10-04: Japanese dialogue and quote-inventory option B.

| IDs | Disposition |
|---|---|
| VOICE-V4-001 (La+) | Applied by hand. The card's Dialogue Style keeps only the two shared spans, 「聞こえたっしょ」 and 「これが配信者よ」. The unchecked fillers ("watashi", "maji de", "yabai") are no longer exported. The sheet's §3 rewords the first-person note as GPT proposed. |
| VOICE-V4-002 (La+) | Applied. Option B labels: "Yes My Dark!" is a secondary transcription and the followers' line. 「吾輩」 and 「貴様」 are secondary vocabulary records. The labels were carried into Dialogue Style, Audio Tags and the sheet's §3 and §5. |
| VOICE-V4-003, 006, 007, 011, 013 | Already satisfied. The palette lines were added by WF-015/016 ("Additional proposed scene directions…" in §4), which the converter reads. V20 passes. GPT saw the sheets as they stood on 10-03. |
| VOICE-V4-004 (Lui) | Applied. Dialogue Style keeps 「まあ」 and 「ね」 only as they occur in the shared line. The calm delivery is a provisional choice. |
| VOICE-V4-005 (Lui) | Applied, and normalized across Dialogue Style, Catchphrases, Voice & Delivery, Audio Tags and sheet §§3–5 and 8. The official written laugh 「ﾊｯﾊｰ↑」 has the provisional reading はっはー (hahhā). In a script it is `[pleased] ハッハー！` with a ROMAJI line. The ROMAJI line that the tool had put inside Audio Tags was folded into one line. |
| VOICE-V4-008 – 010 (Chloe) | Applied. Dialogue Style drops the unchecked "~sā" filler. The sheet introduction is in the past tense ("Her archived performances used Japanese"). Giggles and the singing register are provisional choices. |
| VOICE-V4-012 (Iroha) | Applied. 「よしよしよしよし」 is one documented example, not a fixed repetition count. The same wording is on the sheet's §3. |
| VOICE-V4-014 (all five) | Applied in the format used for the nine JP sheets. §2 says "Dialogue language: **Japanese**", and Audio Tags opens with the dialogue-language sentence. Lines in §§3–5 and 8 are in Japanese script with ROMAJI lines. A holoX scene lints against the real sheets. Two Style demos that matched lines only one ASR model heard were replaced (Iroha; Marine's in the earlier JP pass). |

