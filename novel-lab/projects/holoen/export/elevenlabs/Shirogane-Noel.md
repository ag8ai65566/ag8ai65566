# ElevenLabs v4 Performance Sheet: Shirogane Noel

> Built from `bible/characters/Shirogane-Noel.md` (2026-10-02). Original designed voice matched only to register and
> energy; never clone or imitate the member's real voice (ElevenLabs Use Policy §5; COVER Derivative Works
> Guidelines). Noel is active at the 2026 baseline. She streams in Japanese; lines below are given in Japanese or romanized with
> English glosses, and the voice works for Japanese, English or Chinese dialogue. Guide:
> `novel-lab/docs/elevenlabs-v4.md`.

## 1. Voice Design prompt (original voice; provisional design choices)
"Perfect audio quality. Young woman, soft, girlish, warm voice, higher than her armor suggests; bubbly and eager in chat, flustered when she loses, with a gentler older-sister register available."
- The original voice's register is an independent design choice; mixed-recording pitch estimates are not synthesis targets.
- Laughter, shrieks, breathiness and timbre are provisional choices for the original voice, not listening observations.

## 2. Settings (starting points)
- `eleven_v4`. Stability **45%** (API `0.45`) (warm, with flustered swings; an untested starting choice).
  Similarity **75%** (API `0.75`), referring only to the selected original voice.
- Pace comes from the designed voice plus `[cheerful, warm]` or `[chatty, relaxed]`; v4 has no speed slider.

## 3. Write these habits into the script
- Calls herself "Danchou" (commander) and her viewers "danin-san"; muscle-themed greetings: the official 「こんまっする〜」 (konmassuru), and "Konbanmassuru~" as the wiki transcribes it.
- Recaps her week in old-fashioned phrasing: 「まぁ色々ありましたな」 ("well, quite a lot happened").
- Eager game recommendations.
- Mock jealousy about Flare is on-stream comedy; keep it light.

## 4. Tag palette by situation
| Situation | Tags | Line |
|---|---|---|
| Greeting | `[hearty, bright]` | "Konmassuru~" (official) |
| Recapping the week | `[chatty, relaxed]` | 「まぁ色々ありましたな」 ("Mā iroiro arimashita na") |
| Recommending something | `[eager]` | **Style demo:** "Zehi minna mo yatte mite!" ("You all should try it too!") |
| Losing a game | `[flustered, wailing]` | **Style demo:** "Danchou no kinniku ga tarinakatta…!" ("Danchou's muscles weren't enough…!") |
| The Flare bit (comedy) | `[mock-jealous, pouty]` | **Style demo:** "Furea wa danchou no da yo!?" ("Flare is mine, you know!?") |
| Older-sister mode | `[gentle, lower]` | **Style demo:** "Daijōbu, yukkuri de ii kara ne." ("It's okay, take your time.") |

With people (proposed scene directions, not observed conversational defaults): Flare `[playful, fond]`; Marine `[bickering, playful]`; Pekora `[competitive]`.

## 5. Signature sounds (provisional; tag plus a written word is a scripting convention, not a guarantee of engine behavior)
- "Konmassuru~" (spoken)
- `[laughs]` (tag only)

## 6. Pronunciation (provisional; test)
- Reading guide (untested): しろがね のえる; だんちょう; こんまっする. Listen to how the chosen voice says them and adjust.

## 7. Don't
- A gruff warrior; a cold or sultry default.

## 8. Example
```
[hearty, bright] Konmassuru~!
[chatty, relaxed] Mā, iroiro arimashita na.
[eager] Zehi minna mo yatte mite!
[flustered, wailing] Danchou no kinniku ga tarinakatta…!
```
(Line 1 is her official greeting wording; line 2 is her line, quoted only where both transcripts agree; lines 3–4 are
style demos.)
