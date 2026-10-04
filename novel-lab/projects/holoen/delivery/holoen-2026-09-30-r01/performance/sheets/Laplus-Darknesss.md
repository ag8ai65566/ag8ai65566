# ElevenLabs v4 Performance Sheet: La+ Darknesss

> Source voice fields SHA-256 (Name, Dialogue Style, Catchphrases, Voice & Delivery, Audio Tags): `66fddfbed30b3f0245f7af91b4a7783bdfdf348edd723dfee7182bcaff00b74b` — reviewed 2026-10-04: Claude 2026-10-04: voice audits v1-v4 merged (research/qa/voice-audit-dispositions.md); attestation research/qa/voice-delivery.md; author decisions 2026-10-04 (quote inventory B; JP members speak Japanese)
> Built from `bible/characters/Laplus-Darknesss.md` (2026-10-02). Original designed voice matched only to register and
> energy; never clone or imitate the member's real voice (ElevenLabs Use Policy §5; COVER Derivative Works
> Guidelines). La+ is active at the 2026 baseline. She streams in Japanese; her audio dialogue is Japanese
> (author decision 2026-10-04): spoken lines are Japanese script; romaji and glosses are reading aids, not spoken. Guide:
> `novel-lab/docs/elevenlabs-v4.md`.

## 1. Voice Design prompt (original voice)
"Perfect audio quality. Young woman, small, bright, bratty voice that puffs itself up into a grand villain register and cracks into a loud whine when teased or beaten; quick and cocky when winning, with a smug cackle."
- The original voice's register is an independent design choice; mixed-recording pitch estimates are not synthesis targets.
- Laughter, shrieks, breathiness and timbre are provisional choices for the original voice, not listening observations.
- Design and preview this voice with Japanese text (the §8 lines). Japanese is the project's dialogue language
  for the original voice, not a claim about the member.

## 2. Settings (untested starting choices; verify endpoint behavior)
- `eleven_v4`. Stability **40%** (API `0.40`) (grand, then whiny; an untested starting choice).
  Similarity **75%** (API `0.75`), referring only to the selected original voice.
- Pace comes from the designed voice plus `[smug, bright]` or `[commanding, theatrical]`; v4 has no speed slider.
- Dialogue language: **Japanese** (author decision 2026-10-04). Write her spoken turns in Japanese script;
  romaji goes on a `ROMAJI ::` line and any English on `GLOSS ::` (neither is spoken).
  `tools/scene_to_elevenlabs.py` rejects a turn of hers that has no Japanese text.

## 3. Write these habits into the script
- 「吾輩」 (wagahai; secondary vocabulary record) is persona vocabulary; the first-model notes suggest ordinary first-person usage and do not detect the persona pronoun in these two windows; this cannot establish an overall frequency.
- Casual checking phrase: 「聞こえたっしょ」 (kikoeta ssho, "you heard it, right?"; shared ASR span).
- Her followers answer her call with "Yes My Dark!" (secondary transcription); it is their line, not hers.
- Indignant protests when teased and a whine when she loses are provisional choices for suitable scenes.

## 4. Tag palette by situation
| Situation | Tags | Line |
|---|---|---|
| Opening | `[commanding, theatrical]` | 「貴様ら、刮目せよ！！」 ("Kisama-ra, katsumoku seyo!!"; official introduction, officially "See me, hear me, all of you!") |
| Showing off | `[smug, bright]` | 「これが配信者よ」 ("Kore ga haishinsha yo," "this is what a streamer is!") |
| Checking with chat | `[casual]` | 「聞こえたっしょ」 ("Kikoeta ssho," "you heard that, right?") |
| Treated like a child | `[indignant, loud]` | **Style demo:** 「吾輩は子供じゃない！」 ("Wagahai wa kodomo ja nai!", "I am not a child!") |
| Losing a game | `[whining, furious]` | **Style demo:** 「貴様〜！」 ("Kisama~!", "You~!") |

With people (proposed scene directions, not observed conversational defaults): Lui `[whiny, dependent]`; Kiara `[competitive, friendly]`; seniors `[indignant]`.

Additional proposed scene directions from the card's Audio Tags (untested): `[conspiratorial]`.

## 5. Signature sounds (provisional; tag plus a written word is a scripting convention, not a guarantee of engine behavior)
- `[cackles]` (tag only; a provisional choice)
- "Yes My Dark!" (secondary transcription) belongs to her followers; do not give it to her as a signature line

## 6. Pronunciation (provisional; test)
- Reading guide (untested): らぷらす だーくねす; わがはい; きさま; かつもくせよ. Listen to how the chosen voice says them and adjust.

## 7. Don't
- A truly menacing demon; a sleepy or mature-cool voice.

## 8. Example
```
[commanding, theatrical] 貴様ら、刮目せよ！！
ROMAJI :: Kisama-ra, katsumoku seyo!!
[smug, bright] これが配信者よ！
ROMAJI :: Kore ga haishinsha yo!
[indignant, loud] 吾輩は子供じゃない！
ROMAJI :: Wagahai wa kodomo ja nai!
[casual] 聞こえたっしょ？
ROMAJI :: Kikoeta ssho?
```
(Line 1 is her official Japanese introduction; lines 2 and 4 are her lines, quoted only where both transcripts
agree; line 3 is a style demo. ROMAJI lines are reading aids and are not spoken.)
