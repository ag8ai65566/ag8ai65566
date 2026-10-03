# ElevenLabs v4 Performance Sheet: Houshou Marine

> Built from `bible/characters/Houshou-Marine.md` (2026-10-02). Original designed voice matched only to register and
> energy; never clone or imitate the member's real voice (ElevenLabs Use Policy §5; COVER Derivative Works
> Guidelines). Marine is active at the 2026 baseline. She streams in Japanese; lines below are given in Japanese or romanized with
> English glosses, and the voice works for Japanese, English or Chinese dialogue. Guide:
> `novel-lab/docs/elevenlabs-v4.md`.

## 1. Voice Design prompt (original voice; provisional design choices)
"Perfect audio quality. Young woman, bright, brassy, mature-sounding mid-high voice; rapid-fire and comic, jumping into shrieks when startled and loud cackles; switches on demand to a cutesy idol voice."
- The original voice's register is an independent design choice; mixed-recording pitch estimates are not synthesis targets.
- Laughter, shrieks, breathiness and timbre are provisional choices for the original voice, not listening observations.

## 2. Settings (untested audition choices; verify endpoint behavior)
- `eleven_v4`. Stability **35%** (API `0.35`) (big comic swings; an untested starting choice).
  Similarity **75%** (API `0.75`), referring only to the selected original voice.
- Pace comes from the designed voice plus `[energetic, brassy]` or `[panicked, rapid]`; v4 has no speed slider.

## 3. Write these habits into the script
- "Ahoy!" to open; calls herself "Senchō" (Captain); official 「ヨーソロー」 (yōsorō); the wiki transcribes her sign-off as "Shukkō!" (set sail).
- Rapid, emphatic delivery for game reactions; pace and volume follow the scene.
- Regroups out loud: 「一回落ち着こうよ」 ("let's calm down for a sec").
- Flips into a cutesy idol voice for a bit, then straight back. Crude jokes keep their teasing register; nothing explicit.

## 4. Tag palette by situation
| Situation | Tags | Line |
|---|---|---|
| Opening | `[bright, theatrical]` | "Ahoy!" (official) |
| Startled | `[panicked, rapid]` | **Style demo:** "Matte matte matte!" ("Wait wait wait!") |
| Regrouping | `[comic, self-scolding]` | 「一回落ち着こうよ」 ("Ikkai ochitsukō yo," "let's calm down for a sec") |
| Arguing with a game | `[rough, comic]` | **Style demo:** "Baka iu na!" ("Don't be stupid!") |
| Idol mode | `[cutesy, sweet]` | **Style demo:** "Senchō no koto, suki ni naccha dame da yo♡" ("You mustn't fall for the Captain♡") |
| Closing | `[bright]` | "Shukkō!" (secondary transcription) |

With people (proposed scene directions, not observed conversational defaults): Pekora `[bickering, fond]`; Suisei `[playful]`; Kiara `[playful, teasing]`; FUWAMOCO `[doting]`.

Additional proposed scene directions from the card's Audio Tags (untested): `[mischievous]`, `[warm]`.

## 5. Signature sounds (provisional; tag plus a written word is a scripting convention, not a guarantee of engine behavior)
- "Ahoy!" (spoken)
- `[cackles]` (tag only); `[shrieks]` (tag only)

## 6. Pronunciation (provisional; test)
- Reading guide (untested): ほうしょう まりん; せんちょう; ようそろー; しゅっこう. Listen to how the chosen voice says them and adjust.

## 7. Don't
- Not as default: quiet, shy, slow or sleepy delivery. Pace and volume follow the scene. Keep humor non-explicit.

## 8. Example
```
[bright, theatrical] Ahoy!
[panicked, rapid] Matte matte matte!
[comic, self-scolding] Ikkai ochitsukō yo.
[cutesy, sweet] Senchō no koto, suki ni naccha dame da yo♡
[bright] Shukkō!
```
(Line 1 is her official greeting; line 3 is her line, quoted only where both transcripts agree; line 5 is her
sign-off as a secondary transcription; lines 2 and 4 are style demos.)
