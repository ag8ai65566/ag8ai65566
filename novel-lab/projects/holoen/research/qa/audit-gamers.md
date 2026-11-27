# Cohort audit: gamers (Fubuki, Mio, Korone, hololive GAMERS; Claude self-check 2026-11-27; GPT review pending)

**What this file is.** The other cohort audits are GPT cross-card audits merged by Claude. This one is not: the
GAMERS cards were added on the author's order of 2026-11-27 ("追加人物, 把gamers補完"), and the Codex login that the
framework uses for GPT was blocked in this session, so Claude researched, wrote and checked them alone. The file
records the checks Claude ran and what they found, so that V11, V12, V14 and V15 have a written review to point to.
It does not replace the GPT audit; run `lab.py` cohort audit "gamers" with GPT when the login is available, and merge
its findings here. Nekomata Okayu stays in the "jp" cohort, where her card was first audited.

Scope: `bible/characters/Shirakami-Fubuki.md`, `Ookami-Mio.md`, `Inugami-Korone.md`, `bible/world/hololive-GAMERS.md`,
their performance sheets, `research/audio-check/gamers.md`, and the GAMERS lines added to existing cards (Okayu, Ayame,
Marine, AZKi, Lui, Lamy, Koyori, Calli, Fuwawa, Mococo, Riona, Niko, Chihaya, Vivi, Botan, Suisei, La+, Noel, Iroha,
Bae; Groups on Okayu and Marine).

## Checks run

| Check | How | Result |
|---|---|---|
| Dates and status (V10-type) | Each date traced to the official profile (debut, birthday, height, unit), the official music catalog (release dates read from each entry), archived titles, or a named news report | All three active. Debuts 2018-06-01, 2018-12-07, 2019-04-13 (official). Albums: FBKINGDOM "Blessing" 2025-01-15, "Night walk" 2023-12-07, "My Sparkle" 2025-08-20 (official music pages). Fubuki's first solo live 2025-02-13 at Pia Arena MM (official announcement plus a Famitsu report; the archive titles agree). Mio's "Our Sparkle" 2025-09-10 (official news headline on her profile). Korone's originals dated from the official catalog. |
| Participants and direction (V11) | Each tie checked against full archive titles (member lists in the title brackets) on the channel that hosted it; `tools/web_check.py` for coverage | Twenty existing cards now name the GAMERS members they share collabs with. Title keyword matches that were false positives (ルイージ for Lui, ビビリ / ビビッド for Vivi, ジジイ for Gigi, ニコラ for Niko, 優しい彗星 for Suisei, ホロぐら for Gura) were discarded. Three new one-way ties were closed (Riona→Mio rephrased, Lamy↔Fubuki added, Fubuki→Ina rephrased; the English-lesson tie stays in Fubuki's map with its sources); the five remaining one-way ties are the FLOW GLOW coverage notes recorded in audit-flowglow.md. |
| Evidence records (V12) | Each [SW] claim matched to a dossier line with a source ID | Every claim has an official page, an archive ID, a row in the audio report or a named secondary source. Fubuki's stream vocabulary, cat joke, Kurokami Fubuki, Vice-Manager Unicorn and mascots come from her official Q&A (English and Japanese). Units added to `tools/qa_packets.py` carry their evidence (hololive GAMERS, AyaFubuMi, NYANGUCORN and RosaMiA from official profiles or music credits; FAMS and OKFAMS from Fubuki's official Q&A). |
| Quotations and ASR (V13) | `tools/span_check.py holoen` | 0 quotations outside a shared span. Lines heard as near-matches by both models (Mio's 「おはみぉーん」 and "otsu-mion," Fubuki's "Hi, Friends!" and "otsukon") are given in the members' own written spellings (titles, official profile) or in romaji, labelled as such. Mio's 「うちうち、うちだよ」 is labelled as written (a 2021 title) wherever it appears. A Fubuki sample line that joined 「ではでは」 to 「今日もありがとうございました」 across an intervening sign-off was split. |
| Scope screening (V14) | The release PRIVACY pattern plus a manual scan of the new files for family, pets, health, sleep, breaks, travel, home and routine words | 0 automated candidates. Removed: "at Mio's" (a home location from a title) on the world card. Not used: personal remarks from the transcribed chats, personal items in some stream titles, the official profile's snack and drink lines. Stream labels in the audio report are neutral. |
| Usability and fidelity (V15) | Field lengths against `framework/sudowrite-fields.json`; Japanese dialogue rule; palettes | All new fields inside the soft limits; Relationships on edited cards at or under 350 (Calli trimmed by three short phrases to stay at 350). Spoken lines are Japanese with romaji and an English gloss; Audio Tags declare Japanese dialogue; the V20 palette check passes. |

## Dispositions (self-review findings)

- **Outfit dates.** Dated only where a reveal title, hashtag, thumbnail or silhouette ties the gallery image to a
  date: Fubuki 2019-12-22 (thumbnail), 2024-08-09 (silhouette), the "TEK" outfit's 2024-08-05 return and the royal
  outfit's 2025 solo live (thumbnails), the Western-style outfit by 2020-10-06 (thumbnail); Mio 2022-12-06
  (silhouette) and her room wear's 2022-01-09 "2.0" (title and thumbnail art); Korone 2022-06-24 (title and ©SEGA),
  2023-07-07 and 2024-10-01 (silhouettes). The rest are undated.
- **Kurokami Fubuki** is described from the official Q&A as a separate persona; she has no card and her rough register
  is excluded from Fubuki's voice direction.
- **Groups alignment.** "holoWitches" follows the Marine card's spelling for the official artist "Magical Girl
  holoWitches!"; BABACORN was added to Marine's Groups and NYANGUCORN to Okayu's, each with an evidence note.

## Open items

1. GPT cohort audit (blocked login).
2. A spoken check of Fubuki's 「こんこんきーつね」 and of Korone's greeting outside her morning show (both are covered by
   music or game audio in the checked windows; the cards rely on the official profiles).
3. Reveal dates for the undated gallery outfits; what Korone's 2022 "ambassador" title refers to.
