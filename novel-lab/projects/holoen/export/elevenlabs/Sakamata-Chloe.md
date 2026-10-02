# ElevenLabs v4 Performance Sheet: Sakamata Chloe

> Built from `bible/characters/Sakamata-Chloe.md` (2026-10-02). Original designed voice matched only to register and
> energy; never clone or imitate the member's real voice (ElevenLabs Use Policy §5; COVER Derivative Works
> Guidelines). Chloe concluded her regular activities on 2025-01-26 and remains a hololive affiliate; the sheet covers her 2021–2025 persona. She streams in Japanese; lines below are given in Japanese or romanized with
> English glosses, and the voice works for Japanese, English or Chinese dialogue. Guide:
> `novel-lab/docs/elevenlabs-v4.md`.

## 1. Voice Design prompt (original voice)
"Perfect audio quality. Young woman, small, soft, high and slightly airy voice that chatters fast, giggles and teases; panicky squeaks in horror."
- The original voice's register is an independent design choice; mixed-recording pitch estimates are not synthesis targets.

## 2. Settings (starting points)
- `eleven_v4`. Stability **45%** (API `0.45`) (quick and playful; an untested starting choice).
  Similarity **75%** (API `0.75`), referring only to the selected original voice.
- Pace comes from the designed voice plus `[soft, playful]` or `[fast, casual]`; v4 has no speed slider.

## 3. Write these habits into the script
- Opens hungry: "Bakku bakku baku~" ("Chomp, chomp, chomp!") and 「いただきまーす」 ("let's eat!").
- Calls herself "Sakamata"; fast, run-on chatter that polls chat.
- Denies blame with innocent teasing.
- Closes with "Gochisōsama" ("Thanks for the food").

## 4. Tag palette by situation
| Situation | Tags | Line |
|---|---|---|
| Opening | `[bright, hungry]` | 「いただきまーす」 ("Itadakimāsu!") |
| Chatting | `[fast, casual]` | 「いつからおじさんなの」 ("Itsu kara ojisan na no," "since when is someone an ojisan?") |
| Teasing a member | `[mischievous, giggly]` | **Style demo:** "Ē~, sore Sakamata no sei ja nai yo?" ("Huh~, that's not Sakamata's fault, is it?") |
| Horror | `[panicked, squeaky]` | `[gasps]` (tag only) |
| Closing | `[content]` | "Gochisōsama." (official, "Thanks for the food") |

With people (proposed scene directions, not observed conversational defaults): Koyori `[bickering, fond]`; Lui `[whiny, sheepish]`; Kiara `[shy, excited]`; seniors `[teasing]`.

## 5. Signature sounds
- "Bakku bakku baku~" (spoken)
- `[giggles]` (tag only); `[gasps]` (tag only)

## 6. Pronunciation (provisional; test)
- Reading guide (untested): さかまた くろえ; ばっくばっくばく. Listen to how the chosen voice says them and adjust.

## 7. Don't
- A cool, mature or menacing speaking voice; slow, careful speech.

## 8. Example
```
[bright, hungry] Itadakimāsu!
[fast, casual] Itsu kara ojisan na no?
[mischievous, giggly] Ē~, sore Sakamata no sei ja nai yo?
[content] Gochisōsama.
```
(Lines 1–2 are her lines, quoted only where both transcripts agree (line 2 is the shared part of a longer
line); line 3 is a style demo; line 4 is her official closing.)
