# ElevenLabs v4 Performance Sheet: Sakamata Chloe

> Built from `bible/characters/Sakamata-Chloe.md` (2026-10-02). Original designed voice matched only to register and
> energy; never clone or imitate the member's real voice (ElevenLabs Use Policy §5; COVER Derivative Works
> Guidelines). Chloe concluded her regular activities on 2025-01-26 and remains a hololive affiliate; the sheet covers her 2021–2025 persona. She streams in Japanese; lines below are given in Japanese or romanized with
> English glosses, and the voice works for Japanese, English or Chinese dialogue. Guide:
> `novel-lab/docs/elevenlabs-v4.md`.

## 1. Voice Design prompt (original voice)
"Perfect audio quality. Young woman, small, soft, high and slightly airy voice that chatters, giggles and teases; panicky squeaks in horror; a fuller, more mature tone when singing."
- The original voice's register is an independent design choice; mixed-recording pitch estimates are not synthesis targets.
- Laughter, shrieks, breathiness and timbre are provisional choices for the original voice, not listening observations.

## 2. Settings (untested audition choices; verify endpoint behavior)
- `eleven_v4`. Stability **45%** (API `0.45`) (quick and playful; an untested starting choice).
  Similarity **75%** (API `0.75`), referring only to the selected original voice.
- Pace comes from the designed voice plus `[soft, playful]` or `[fast, casual]`; v4 has no speed slider.

## 3. Write these habits into the script
- Opens like a meal: 「ばっくばっくばく～ん」 ("bakku bakku bakūn," official) then 「いただきます」; on stream, 「いただきまーす」 ("itadakimāsu!").
- Calls herself "Sakamata"; connected, run-on chatter that polls chat (speed and softness are provisional choices).
- Teases seniors and friends; any blame-denying line is a style demo, not a documented habit.
- Closes with 「ごちそうさまでした」 ("gochisōsama deshita," official; "Thanks for the food").

## 4. Tag palette by situation
| Situation | Tags | Line |
|---|---|---|
| Opening | `[bright, hungry]` | 「いただきまーす」 ("Itadakimāsu!") |
| Chatting | `[fast, casual]` | 「いつからおじさんなの」 ("Itsu kara ojisan na no," "since when is someone an ojisan?") |
| Teasing a member | `[mischievous, giggly]` | **Style demo:** "Ē~, sore Sakamata no sei ja nai yo?" ("Huh~, that's not Sakamata's fault, is it?") |
| Horror | `[panicked, squeaky]` | `[gasps]` (tag only) |
| Closing | `[content]` | 「ごちそうさまでした」 ("Gochisōsama deshita," official) |

With people (proposed scene directions, not observed conversational defaults): Koyori `[bickering, fond]`; Lui `[whiny, sheepish]`; Kiara `[shy, excited]`; seniors `[teasing]`.

Additional proposed scene directions from the card's Audio Tags (untested): `[curious, playful]`, `[mature, heartfelt]`.

## 5. Signature sounds (provisional; tag plus a written word is a scripting convention, not a guarantee of engine behavior)
- "Bakku bakku bakūn" (spoken, official opening)
- `[giggles]` (tag only); `[gasps]` (tag only); provisional choices

## 6. Pronunciation (provisional; test)
- Reading guide (untested): さかまた くろえ; ばっくばっくばくーん; ごちそうさまでした. Listen to how the chosen voice says them and adjust.

## 7. Don't
- A cool, mature or menacing speaking voice; slow, careful speech.

## 8. Example
```
[bright, hungry] Itadakimāsu!
[fast, casual] Itsu kara ojisan na no?
[mischievous, giggly] Ē~, sore Sakamata no sei ja nai yo?
[content] Gochisōsama deshita.
```
(Lines 1–2 are her lines, quoted only where both transcripts agree (line 2 is the shared part of a longer
line); line 3 is a style demo; line 4 is her official closing.)
