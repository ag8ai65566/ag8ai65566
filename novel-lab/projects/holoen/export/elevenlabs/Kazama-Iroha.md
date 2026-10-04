# ElevenLabs v4 Performance Sheet: Kazama Iroha

> Source voice fields SHA-256 (Name, Dialogue Style, Catchphrases, Voice & Delivery, Audio Tags): `b3ead757c391fac9233c6571807a27f0812b50d44321726cc8d57bc75d2a49bc` — reviewed 2026-10-04: Claude 2026-10-04: voice audits v1-v4 merged (research/qa/voice-audit-dispositions.md); attestation research/qa/voice-delivery.md; author decisions 2026-10-04 (quote inventory B; JP members speak Japanese)
> Built from `bible/characters/Kazama-Iroha.md` (2026-10-02). Original designed voice matched only to register and
> energy; never clone or imitate the member's real voice (ElevenLabs Use Policy §5; COVER Derivative Works
> Guidelines). Iroha is active at the 2026 baseline. She streams in Japanese; her audio dialogue is Japanese
> (author decision 2026-10-04): spoken lines are Japanese script; romaji and glosses are reading aids, not spoken. Guide:
> `novel-lab/docs/elevenlabs-v4.md`.

## 1. Voice Design prompt (original voice)
"Perfect audio quality. Young woman, clear, bright, youthful voice with a sporty edge; earnest and polite in samurai mode, quick, loud and pumped when competing, laughing easily at her own mistakes."
- The original voice's register is an independent design choice; mixed-recording pitch estimates are not synthesis targets.
- Laughter, shrieks, breathiness and timbre are provisional choices for the original voice, not listening observations.
- Design and preview this voice with Japanese text (the §8 lines). Japanese is the project's dialogue language
  for the original voice, not a claim about the member.

## 2. Settings (untested starting choices; verify endpoint behavior)
- `eleven_v4`. Stability **45%** (API `0.45`) (earnest by default, pumped when competing; an untested starting choice).
  Similarity **75%** (API `0.75`), referring only to the selected original voice.
- Pace comes from the designed voice plus `[cheerful, earnest]` or `[excited, fast]`; v4 has no speed slider.
- Dialogue language: **Japanese** (author decision 2026-10-04). Write her spoken turns in Japanese script;
  romaji goes on a `ROMAJI ::` line and any English on `GLOSS ::` (neither is spoken).
  `tools/scene_to_elevenlabs.py` rejects a turn of hers that has no Japanese text.

## 3. Write these habits into the script
- Calls herself 「風真」 ("Kazama") or 「ござる」 ("Gozaru"); sentence-final 「でござる」 ("de gozaru") was uncommon in the two sampled 2026 game windows.
- 「よしよしよしよし」 ("all right, all right") after a success; one documented example, not a fixed repetition count.
- Talks back when chat teases her (her 「おい」 ("oi") is a first-model observation, so lines for it are style demos).
- Laughs off her blunders (laughs are provisional choices).

## 4. Tag palette by situation
| Situation | Tags | Line |
|---|---|---|
| Introduction | `[proud, polite]` | 「holoXの用心棒、侍の風真いろはでござる」 ("holoX no yōjinbō, samurai no Kazama Iroha de gozaru"; official) |
| Going well | `[excited, fast]` | 「よしよしよしよし」 ("Yoshi yoshi yoshi yoshi") |
| Teased by chat | `[indignant, loud]` | **Style demo:** 「ちょっと、チャット殿！」 ("Chotto, chatto-dono!", "Hey, chat!") |
| A blunder | `[laughs, sheepish]` | **Style demo:** 「失敗は成功のもとでござる！」 ("Shippai wa seikō no moto de gozaru!", "Failure is where success starts, I daresay!") |
| Guarding holoX | `[determined]` | **Style demo:** 「ここは風真に任せるでござる！」 ("Koko wa Kazama ni makaseru de gozaru!", "Leave this to Kazama, I daresay!") |

With people (proposed scene directions, not observed conversational defaults): AZKi `[relaxed, playful]`; La+ `[patient, teasing]`; Kiara `[excited]`.

Additional proposed scene directions from the card's Audio Tags (untested): `[triumphant]`, `[panicked]`.

## 5. Signature sounds (provisional; tag plus a written word is a scripting convention, not a guarantee of engine behavior)
- 「でござる」 ("de gozaru", spoken, as a set piece)
- 「よしよしよしよし」 ("yoshi yoshi yoshi yoshi", spoken)
- `[laughs]` (tag only; a provisional choice)

## 6. Pronunciation (provisional; test)
- Reading guide (untested): かざま いろは; ござる; ようじんぼう. Listen to how the chosen voice says them and adjust.

## 7. Don't
- A gruff warrior, a grim or solemn read, or a sultry, cool voice.

## 8. Example
```
[proud, polite] holoXの用心棒、侍の風真いろはでござる！
ROMAJI :: holoX no yōjinbō, samurai no Kazama Iroha de gozaru!
[excited, fast] よしよしよしよし！
ROMAJI :: Yoshi yoshi yoshi yoshi!
[indignant, loud] ちょっと、チャット殿！
ROMAJI :: Chotto, chatto-dono!
[laughs, sheepish] 失敗は成功のもとでござる！
ROMAJI :: Shippai wa seikō no moto de gozaru!
```
(Line 1 is her official Japanese introduction; line 2 is her line, quoted only where both transcripts agree;
lines 3–4 are style demos. ROMAJI lines are reading aids and are not spoken.)
