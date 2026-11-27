# Cohort audit: flowglow (Riona, Niko, Su, Chihaya, FLOW GLOW; Claude self-check 2026-11-27; Gemini Neon review pending)

**What this file is.** The other cohort audits are GPT cross-card audits merged by Claude. This one is not: the
FLOW GLOW cards were added on the author's order of 2026-11-27, and the Codex login that the framework uses for GPT
was blocked in this session, so Claude researched, wrote and checked them alone. The file records the checks Claude
ran and what they found, so that V11, V12, V14 and V15 have a written review to point to. On 2026-11-27 the
author decided not to use the Codex/GPT audit and to have Gemini Neon (desktop) re-review the work instead; the
packets are in `research/qa/external-review/`, and Gemini's findings will be merged here.

Scope: `bible/characters/Isaki-Riona.md`, `Koganei-Niko.md`, `Mizumiya-Su.md`, `Rindo-Chihaya.md`,
`bible/world/FLOW-GLOW.md`, their performance sheets, `research/audio-check/flowglow.md`, and the FLOW GLOW lines
added to ten existing cards (Calli, Nerissa, Marine, Lamy, AZKi, Koyori, Okayu, Lui, Chloe, Vivi).

## Checks run

| Check | How | Result |
|---|---|---|
| Dates and status (V10-type) | Each date traced to the official debut announcement, the official music catalog (release dates read from each entry), archived titles, or a named news report | All five members active; debut 2024-11-09 (PST relay start noted); 3D debut live 2025-11-23 (news report plus official #FG3Dライブ videos); festival debut 2026-03-07 (news report plus official listing). Vivi's dossier dates for "good enough" (09-20 → 2025-09-21) and "magic summer" (08-18 → 2026-08-19) corrected to the official release dates. |
| Participants and direction (V11) | Every tie checked from both channels where the archive has both; `tools/web_check.py` for coverage | Ten existing cards now name the FLOW GLOW members they share collabs with. Five ties stay one-way and are coverage notes, not errors: Riona → IRyS, Bijou, Nerissa (dance shorts of her song); Chihaya → Suisei (covers of Suisei's songs), Calli (a watch-along). Covers are credited per song; a dance short on a channel does not establish who performed the motion. |
| Evidence records (V12) | Each [SW] claim matched to a dossier line with a source ID | Every claim has an official page, an archive ID, a row in the audio report or a named secondary source. Secondary-only items are labelled (the unit fan name FLOMIE stays off the cards; Su's height history is marked secondary). A song the earlier research note listed for 2025-02-05 is not in the official catalog and is not used. |
| Quotations and ASR (V13) | `tools/span_check.py holoen` | 0 quotations outside a shared span. Two quotes were tightened during this check: Chihaya's opening is quoted only in the parts both models share; a joined Riona quote was split into its two shared spans. Coined words heard as near-matches ("otsu-Riona," the word after Su's group "otsu") are not quoted as verified lines. |
| Scope screening (V14) | The release PRIVACY pattern plus a manual scan of the new files for family, pets, health, sleep, breaks and routine words | 0 automated candidates. Private details were deliberately excluded from the cards, the dossiers and the audio report (neutral stream labels; personal remarks neither quoted nor summarized). |
| Usability and fidelity (V15) | Field lengths against `framework/sudowrite-fields.json`; Japanese dialogue rule; palettes | All new fields inside the soft limits; Relationships edits on existing cards kept inside 350 words (Calli and Nerissa trimmed). Spoken lines are Japanese with romaji and an English gloss; Audio Tags declare Japanese dialogue; V20 palette check passes. |

## Dispositions (self-review findings)

- **Unverified items removed or confirmed.** "逆様" (Riona × Niko) and "クリームで会いにいけますか" (Su × Vivi) were
  confirmed from the official video listings on their profiles (undated here). The 7th fes. appearance was confirmed
  with a news photo report. The unit fan name stays secondary and off the cards.
- **Scope.** Routine details from stream titles and the official profile's household line were kept off the cards;
  scope notes use the project's generic wording.
- **Outfits.** Each member's three outfits are Claude's reading of the official gallery images; Riona's New Year
  outfit is matched to its reveal silhouette. The other members' Japanese-style outfits are not dated.

## Open items

1. Gemini Neon re-review (author decision 2026-11-27; packets A and B in `research/qa/external-review/`).
2. A 2026 chat window for Su and for Chihaya (their checked windows are from August 2025).
3. Release dates for "逆様" and "クリームで会いにいけますか"; reveal dates for the Japanese-style outfits.
