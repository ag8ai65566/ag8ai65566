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

## 2. Settings (starting points)
- `eleven_v4`. Stability **45%** (API `0.45`) (earnest by default, pumped when competing; an untested starting choice).
  Similarity **75%** (API `0.75`), referring only to the selected original voice.
- Pace comes from the designed voice plus `[cheerful, earnest]` or `[excited, fast]`; v4 has no speed slider.

## 3. Write these habits into the script
- Calls herself "Kazama" or "Gozaru"; the samurai "de gozaru" is a set piece more than a 2026 habit.
- 「よしよしよしよし」 ("all right, all right") when things go well.
- A loud "Oi!" when chat teases her.
- Laughs off her blunders.

## 4. Tag palette by situation
| Situation | Tags | Line |
|---|---|---|
| Introduction | `[proud, polite]` | "Kazama Iroha here, I daresay!" (official English) |
| Going well | `[excited, fast]` | 「よしよしよしよし」 ("Yoshi yoshi yoshi yoshi") |
| Teased by chat | `[indignant, loud]` | "Oi!" (observed interjection) |
| A blunder | `[laughs, sheepish]` | **Style demo:** "Mā, sō iu toki mo aru de gozaru." ("Well, these things happen, I daresay.") |
| Guarding holoX | `[determined]` | **Style demo:** "Koko wa Kazama ni makaseru de gozaru!" ("Leave this to Kazama, I daresay!") |

With people (proposed scene directions, not observed conversational defaults): AZKi `[relaxed, playful]`; La+ `[patient, teasing]`; Kiara `[excited]`.

## 5. Signature sounds (provisional; tag plus a written word is a scripting convention, not a guarantee of engine behavior)
- "de gozaru" (spoken, as a set piece); "Oi!" (spoken)
- `[laughs]` (tag only)

## 6. Pronunciation (provisional; test)
- Reading guide (untested): かざま いろは; ござる. Listen to how the chosen voice says them and adjust.

## 7. Don't
- A gruff warrior, a grim or solemn read, or a sultry, cool voice.

## 8. Example
```
[proud, polite] Kazama Iroha here, I daresay!
[excited, fast] Yoshi yoshi yoshi yoshi!
[indignant, loud] Oi!
[laughs, sheepish] Mā, sō iu toki mo aru de gozaru.
```
(Line 1 is her official English introduction; line 2 is her line, quoted only where both transcripts agree;
line 3 is an observed interjection; line 4 is a style demo.)
