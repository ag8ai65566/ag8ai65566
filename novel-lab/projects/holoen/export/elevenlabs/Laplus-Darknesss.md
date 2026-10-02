# ElevenLabs v4 Performance Sheet: La+ Darknesss

> Built from `bible/characters/Laplus-Darknesss.md` (2026-10-02). Original designed voice matched only to register and
> energy; never clone or imitate the member's real voice (ElevenLabs Use Policy §5; COVER Derivative Works
> Guidelines). La+ is active at the 2026 baseline. She streams in Japanese; lines below are given in Japanese or romanized with
> English glosses, and the voice works for Japanese, English or Chinese dialogue. Guide:
> `novel-lab/docs/elevenlabs-v4.md`.

## 1. Voice Design prompt (original voice)
"Perfect audio quality. Young woman, small, bright, bratty voice that puffs itself up into a grand villain register and cracks into a loud whine when teased or beaten; quick and cocky when winning, with a smug cackle."
- The original voice's register is an independent design choice; mixed-recording pitch estimates are not synthesis targets.
- Laughter, shrieks, breathiness and timbre are provisional choices for the original voice, not listening observations.

## 2. Settings (starting points)
- `eleven_v4`. Stability **40%** (API `0.40`) (grand, then whiny; an untested starting choice).
  Similarity **75%** (API `0.75`), referring only to the selected original voice.
- Pace comes from the designed voice plus `[smug, bright]` or `[commanding, theatrical]`; v4 has no speed slider.

## 3. Write these habits into the script
- "Wagahai" is her persona set piece; in 2026 chats she mostly says "watashi."
- Casual and slangy in chat: "maji de," "yabai," "~ssho" (「聞こえたっしょ?」, "you heard that, right?").
- Rallies her followers with "Yes My Dark!"
- Insists she is not a child; whines and fumes when she loses.

## 4. Tag palette by situation
| Situation | Tags | Line |
|---|---|---|
| Opening | `[commanding, theatrical]` | "See me, hear me, all of you!" (official English) |
| Showing off | `[smug, bright]` | 「これが配信者よ」 ("Kore ga haishinsha yo," "this is what a streamer is!") |
| Checking with chat | `[casual]` | 「聞こえたっしょ?」 ("Kikoeta ssho?", "you heard that, right?") |
| Treated like a child | `[indignant, loud]` | **Style demo:** "Wagahai wa kodomo ja nai!" ("I am not a child!") |
| Losing a game | `[whining, furious]` | **Style demo:** "Kisama~!" ("You~!") |
| Rallying followers | `[triumphant]` | "Yes My Dark!" (secondary transcription) |

With people (proposed scene directions, not observed conversational defaults): Lui `[whiny, dependent]`; Kiara `[competitive, friendly]`; seniors `[indignant]`.

## 5. Signature sounds (provisional; tag plus a written word is a scripting convention, not a guarantee of engine behavior)
- "Yes My Dark!" (spoken)
- `[cackles]` (tag only)

## 6. Pronunciation (provisional; test)
- Reading guide (untested): らぷらす だーくねす; わがはい; きさま. Listen to how the chosen voice says them and adjust.

## 7. Don't
- A truly menacing demon; a sleepy or mature-cool voice.

## 8. Example
```
[commanding, theatrical] See me, hear me, all of you!
[smug, bright] Kore ga haishinsha yo!
[indignant, loud] Wagahai wa kodomo ja nai!
[triumphant] Yes My Dark!
```
(Line 1 is her official English introduction; line 2 is her line, quoted only where both transcripts agree;
line 3 is a style demo; line 4 is her followers' call as a secondary transcription.)
