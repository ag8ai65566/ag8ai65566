# Voice delivery attestation: V13 (quotations and ASR) and V19 (voice and pronunciation claims)

Written by Claude on 2026-10-04, after all four task-09 voice audits were merged on the author's order of 2026-10-03.
- Voice audits v1–v4 (GPT xhigh): dispositions in `research/qa/voice-audit-dispositions.md`.
- Quotation pass: `research/qa/quote-inventory.md`.

Promotions remain author decisions (`research/qa/promotions.md`). This file attests the exported voice layer:
- the cards' Dialogue Style, Catchphrases, Voice & Delivery and Audio Tags;
- the 33 performance sheets under `export/elevenlabs/`.

It does not attest listening tests: the runtime evidence is V24 (`test-results.csv` in the package).

## Author decisions this attestation applies (2026-10-04)

1. **Quote inventory, option B.** 93 exported spoken lines rest only on secondary transcriptions (fan wiki and similar). They are listed in `research/qa/quote-inventory.md` and stay in the exports as an **author exception**. Their provenance stays in each card's dossier.
2. **Dialogue language.** The 14 hololive JP members (the JP nine, holoX and DEV_IS's Vivi) speak Japanese in audio scripts:
   - Their spoken turns are written in Japanese script.
   - Romaji and English go only on `ROMAJI ::` / `GLOSS ::` lines, which are not spoken.
   - Each of their sheets says `Dialogue language: Japanese` in §2, and each card's Audio Tags opens with the same rule.
   - `tools/scene_to_elevenlabs.py` rejects a turn of theirs that has no Japanese text.
   - EN members keep English.

## V13: quotations and ASR

| Check | Result |
|---|---|
| Two-model gate | Every ASR-derived spoken quotation in the cards and sheets lies inside a span both models share (small/medium, or small.en/medium.en), from the same window, as recorded in the audio reports' second-model tables. `tools/span_check.py holoen`: **0 quotes outside a shared span**. The two flagged lines are Bae's wiki self-introduction, listed as **author exceptions** (inventory, option B). |
| Stitching | No stitched spans. Ellipses split quotations; each piece must be shared on its own. Excerpts separated in time are labelled as separate excerpts (v1–v4 dispositions). |
| Speaker attribution | Quotations come from the member's own solo streams. Two-speaker windows (the TakaMori Split Fiction co-op; Gigi/Cecilia's CCGG) and game voices (AZKi's Paranormasight narrator) are not quoted. They are paraphrased or recorded as "not confirmed as hers". |
| Upgrades in the quotation pass | Two-model checks run for this pass confirmed three lines, and their labels were upgraded: Marine's 「出航！」 sign-off (two streams), Noel's 「おはまっする」 and Bae's "Bruh.". Rejected candidates are recorded in the reports with their reasons. |
| Written quotations | Official profile wording, X posts and stream titles are labelled as written text and are not used as speech evidence. Lui's 「ﾊｯﾊｰ↑」 is an official written laugh; its spoken rendering ハッハー is a provisional reading. |
| Secondary transcriptions | Under option B they are kept with their labels where exported. The inventory (93 lines, 25 cards) is the author exception. voice-v4:VOICE-V4-002 added the missing labels for La+. |
| Style demos | Invented example lines are labelled "Style demo" in the sheets. Two Style demos that matched a line only one model heard were replaced (Marine, Iroha). |
| Lyrics | No lyrics are quoted. Song titles are named only. |

## V19: voice and pronunciation claims

| Check | Result |
|---|---|
| No cloning or imitation | Every sheet's §1 Voice Design prompt describes an original designed voice. Every sheet header says never to clone or imitate the member's real voice (ElevenLabs Use Policy §5; COVER Derivative Works Guidelines). Every card's Audio Tags says the same. A scan for non-negated "clone/imitate" finds none. |
| Measured pitch and pace | The ten EN sheets and cards that give Hz or words-per-minute figures label them "sample observations from the audio check, not synthesis targets" or "research context only, never synthesis targets". `docs/elevenlabs-v4.md` keeps measurements out of Voice Design. |
| Regional accents | None assigned. EN cards read "English (no regional accent assigned)", and sheets say a regional accent needs an in-scope listening check. Kiara's prompt says "neutral English accent", which assigns none. JP sheets assign no dialect. Vivi's transcript endings (-yan, -nen) are wording, with "no regional accent assigned to the voice". |
| Model controls | v4 settings are Stability and Similarity only, with UI percentages equal to API fractions (V18 checks the numbers). No sheet uses Style, Speed or Speaker Boost. Pace comes from the designed voice plus tags. |
| Pronunciation | All reading guides (kana, IPA, `pronunciation.tsv`) are marked provisional and untested. In the Japanese examples, kanji a voice could misread are written in kana (AZKi's 「ゆか」). |
| Timbre and laughter | Laughter, giggles, screams and timbre are provisional performance choices, not listening findings (v1–v4). |
| Dialogue language | Japanese for the 14 hololive JP members, as above. Voice Design for those voices is previewed with Japanese text (each sheet's §1 note). |

## Limits

No member audio was listened to for this attestation. ASR agreement verifies wording only: it says nothing about vocal quality, and it attributes speakers only through the solo-stream rule. The designed voices, settings, tag readings and Japanese pronunciation still need the listening tests recorded under V24 (`elevenlabs-3-line`, `elevenlabs-japanese`, `sudowrite-import`, `sudowrite-generation`).
