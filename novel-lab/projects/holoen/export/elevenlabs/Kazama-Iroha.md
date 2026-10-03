# ElevenLabs v4 Performance Sheet: Kazama Iroha

> Built from `bible/characters/Kazama-Iroha.md` (2026-10-02). Original designed voice matched only to register and
> energy; never clone or imitate the member's real voice (ElevenLabs Use Policy §5; COVER Derivative Works
> Guidelines). Iroha is active at the 2026 baseline. She streams in Japanese; lines below are given in Japanese or romanized with
> English glosses, and the voice works for Japanese, English or Chinese dialogue. Guide:
> `novel-lab/docs/elevenlabs-v4.md`.

## 1. Voice Design prompt (original voice)
"Perfect audio quality. Young woman, clear, bright, youthful voice with a sporty edge; earnest and polite in samurai mode, quick, loud and pumped when competing, laughing easily at her own mistakes."
- The original voice's register is an independent design choice; mixed-recording pitch estimates are not synthesis targets.
- Laughter, shrieks, breathiness and timbre are provisional choices for the original voice, not listening observations.

## 2. Settings (untested audition choices; verify endpoint behavior)
- `eleven_v4`. Stability **45%** (API `0.45`) (earnest by default, pumped when competing; an untested starting choice).
  Similarity **75%** (API `0.75`), referring only to the selected original voice.
- Pace comes from the designed voice plus `[cheerful, earnest]` or `[excited, fast]`; v4 has no speed slider.

## 3. Write these habits into the script
- Calls herself "Kazama" or "Gozaru"; sentence-final "de gozaru" was uncommon in the two sampled 2026 game windows.
- 「よしよしよしよし」 ("all right, all right") when things go well.
- Talks back when chat teases her (her "oi" is a first-model observation, so lines for it are style demos).
- Laughs off her blunders (laughs are provisional choices).

## 4. Tag palette by situation
| Situation | Tags | Line |
|---|---|---|
| Introduction | `[proud, polite]` | 「holoXの用心棒、侍の風真いろはでござる」 ("holoX no yōjinbō, samurai no Kazama Iroha de gozaru"; official) |
| Going well | `[excited, fast]` | 「よしよしよしよし」 ("Yoshi yoshi yoshi yoshi") |
| Teased by chat | `[indignant, loud]` | **Style demo:** "Chotto, chat-dono!" ("Hey, chat!") |
| A blunder | `[laughs, sheepish]` | **Style demo:** "Mā, sō iu toki mo aru de gozaru." ("Well, these things happen, I daresay.") |
| Guarding holoX | `[determined]` | **Style demo:** "Koko wa Kazama ni makaseru de gozaru!" ("Leave this to Kazama, I daresay!") |

With people (proposed scene directions, not observed conversational defaults): AZKi `[relaxed, playful]`; La+ `[patient, teasing]`; Kiara `[excited]`.

Additional proposed scene directions from the card's Audio Tags (untested): `[triumphant]`, `[panicked]`.

## 5. Signature sounds (provisional; tag plus a written word is a scripting convention, not a guarantee of engine behavior)
- "de gozaru" (spoken, as a set piece)
- "yoshi yoshi yoshi yoshi" (spoken)
- `[laughs]` (tag only; a provisional choice)

## 6. Pronunciation (provisional; test)
- Reading guide (untested): かざま いろは; ござる; ようじんぼう. Listen to how the chosen voice says them and adjust.

## 7. Don't
- A gruff warrior, a grim or solemn read, or a sultry, cool voice.

## 8. Example
```
[proud, polite] holoX no yōjinbō, samurai no Kazama Iroha de gozaru!
[excited, fast] Yoshi yoshi yoshi yoshi!
[indignant, loud] Chotto, chat-dono!
[laughs, sheepish] Mā, sō iu toki mo aru de gozaru.
```
(Line 1 is her official Japanese introduction; line 2 is her line, quoted only where both transcripts agree;
lines 3–4 are style demos.)
