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

## 2. Settings (untested audition choices; verify endpoint behavior)
- `eleven_v4`. Stability **40%** (API `0.40`) (grand, then whiny; an untested starting choice).
  Similarity **75%** (API `0.75`), referring only to the selected original voice.
- Pace comes from the designed voice plus `[smug, bright]` or `[commanding, theatrical]`; v4 has no speed slider.

## 3. Write these habits into the script
- "Wagahai" is persona vocabulary; the two sampled 2026 windows contain "watashi" and no detected "wagahai" (two windows cannot set a frequency).
- Casual and slangy in chat: "maji de," "yabai," "~ssho" (「聞こえたっしょ」, "you heard that, right?").
- Her followers answer her call with "Yes My Dark!"; it is their line, not hers.
- Indignant protests when teased and a whine when she loses are provisional choices for suitable scenes.

## 4. Tag palette by situation
| Situation | Tags | Line |
|---|---|---|
| Opening | `[commanding, theatrical]` | 「貴様ら、刮目せよ！！」 ("Kisama-ra, katsumoku seyo!!"; official introduction, officially "See me, hear me, all of you!") |
| Showing off | `[smug, bright]` | 「これが配信者よ」 ("Kore ga haishinsha yo," "this is what a streamer is!") |
| Checking with chat | `[casual]` | 「聞こえたっしょ」 ("Kikoeta ssho," "you heard that, right?") |
| Treated like a child | `[indignant, loud]` | **Style demo:** "Wagahai wa kodomo ja nai!" ("I am not a child!") |
| Losing a game | `[whining, furious]` | **Style demo:** "Kisama~!" ("You~!") |

With people (proposed scene directions, not observed conversational defaults): Lui `[whiny, dependent]`; Kiara `[competitive, friendly]`; seniors `[indignant]`.

Additional proposed scene directions from the card's Audio Tags (untested): `[conspiratorial]`.

## 5. Signature sounds (provisional; tag plus a written word is a scripting convention, not a guarantee of engine behavior)
- `[cackles]` (tag only; a provisional choice)
- "Yes My Dark!" belongs to her followers; do not give it to her as a signature line

## 6. Pronunciation (provisional; test)
- Reading guide (untested): らぷらす だーくねす; わがはい; きさま; かつもくせよ. Listen to how the chosen voice says them and adjust.

## 7. Don't
- A truly menacing demon; a sleepy or mature-cool voice.

## 8. Example
```
[commanding, theatrical] Kisama-ra, katsumoku seyo!!
[smug, bright] Kore ga haishinsha yo!
[indignant, loud] Wagahai wa kodomo ja nai!
[casual] Kikoeta ssho?
```
(Line 1 is her official Japanese introduction; lines 2 and 4 are her lines, quoted only where both transcripts
agree; line 3 is a style demo.)
