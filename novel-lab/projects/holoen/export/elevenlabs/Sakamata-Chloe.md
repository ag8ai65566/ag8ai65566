# ElevenLabs v4 Performance Sheet: Sakamata Chloe

> Source voice fields SHA-256 (Name, Dialogue Style, Catchphrases, Voice & Delivery, Audio Tags): `bec1029dd257bf13fa4de59c2cef4ef06d0c4286dac6d28a7a9717d5b4b5ed8f` — reviewed 2026-11-27: Claude 2026-11-27 (r02): all 40 sheets checked against the r02 voice-field changes (no removed quote left in a sheet; status and dialogue language match the cards; V20 palettes and span check pass); JP sheets gained the r02 greetings and sign-offs; 7 new sheets (FLOW GLOW, GAMERS); Gemini Neon review pending
> Built from `bible/characters/Sakamata-Chloe.md` (2026-10-02). Original designed voice matched only to register and
> energy; never clone or imitate the member's real voice (ElevenLabs Use Policy §5; COVER Derivative Works
> Guidelines). Chloe concluded her regular activities on 2025-01-26 and remains a hololive affiliate; the sheet covers her 2021–2025 persona. Her archived performances used Japanese; her audio dialogue is Japanese
> (author decision 2026-10-04): spoken lines are Japanese script; romaji and glosses are reading aids, not spoken. Guide:
> `novel-lab/docs/elevenlabs-v4.md`.

## 1. Voice Design prompt (original voice)
"Perfect audio quality. Young woman, small, soft, high and slightly airy voice that chatters, giggles and teases; panicky squeaks in horror; a fuller, more mature tone when singing."
- The original voice's register is an independent design choice; mixed-recording pitch estimates are not synthesis targets.
- Laughter, shrieks, breathiness and timbre are provisional choices for the original voice, not listening observations.
- Design and preview this voice with Japanese text (the §8 lines). Japanese is the project's dialogue language
  for the original voice, not a claim about the member.

## 2. Settings (untested starting choices; verify endpoint behavior)
- `eleven_v4`. Stability **45%** (API `0.45`) (quick and playful; an untested starting choice).
  Similarity **75%** (API `0.75`), referring only to the selected original voice.
- Pace comes from the designed voice plus `[soft, playful]` or `[fast, casual]`; v4 has no speed slider.
- Dialogue language: **Japanese** (author decision 2026-10-04). Write her spoken turns in Japanese script;
  romaji goes on a `ROMAJI ::` line and any English on `GLOSS ::` (neither is spoken).
  `tools/scene_to_elevenlabs.py` rejects a turn of hers that has no Japanese text.

## 3. Write these habits into the script
- Opens like a meal: 「ばっくばっくばく～ん」 ("bakku bakku bakūn," official) then 「いただきます」; on stream, 「いただきまーす」 ("itadakimāsu!").
- Calls herself 「沙花叉」 ("Sakamata"); connected, run-on phrasing that polls chat (speed and softness are provisional choices).
- Teases seniors and friends; any blame-denying line is a style demo, not a documented habit.
- Closes with 「ごちそうさまでした」 ("gochisōsama deshita," official; "Thanks for the food").
- Also on the card (r02): a quick 「ではな〜」 after her closing; 「飼育員」 (Handlers) is her name for the viewers, not a line.

## 4. Tag palette by situation
| Situation | Tags | Line |
|---|---|---|
| Opening | `[bright, hungry]` | 「いただきまーす」 ("Itadakimāsu!") |
| Chatting | `[fast, casual]` | 「いつからおじさんなの」 ("Itsu kara ojisan na no," "since when is someone an ojisan?") |
| Teasing a member | `[mischievous, giggly]` | **Style demo:** 「えぇ～、それ沙花叉のせいじゃないよ？」 ("Ē~, sore Sakamata no sei ja nai yo?", "Huh~, that's not Sakamata's fault, is it?") |
| Horror | `[panicked, squeaky]` | `[gasps]` (tag only) |
| Closing | `[content]` | 「ごちそうさまでした」 ("Gochisōsama deshita," official) |

With people (proposed scene directions, not observed conversational defaults): Koyori `[bickering, fond]`; Lui `[whiny, sheepish]`; Kiara `[shy, excited]`; seniors `[teasing]`.

Additional proposed scene directions from the card's Audio Tags (untested): `[curious, playful]`, `[mature, heartfelt]`.

## 5. Signature sounds (provisional; tag plus a written word is a scripting convention, not a guarantee of engine behavior)
- 「ばっくばっくばく～ん」 ("Bakku bakku bakūn", spoken, official opening)
- `[giggles]` (tag only); `[gasps]` (tag only); provisional choices

## 6. Pronunciation (provisional; test)
- Reading guide (untested): さかまた くろえ; ばっくばっくばくーん; ごちそうさまでした. Listen to how the chosen voice says them and adjust.

## 7. Don't
- A cool, mature or menacing speaking voice; slow, careful speech.

## 8. Example
```
[bright, hungry] いただきまーす！
ROMAJI :: Itadakimāsu!
[fast, casual] いつからおじさんなの？
ROMAJI :: Itsu kara ojisan na no?
[mischievous, giggly] えぇ～、それ沙花叉のせいじゃないよ？
ROMAJI :: Ē~, sore Sakamata no sei ja nai yo?
[content] ごちそうさまでした。
ROMAJI :: Gochisōsama deshita.
```
(Lines 1–2 are her lines, quoted only where both transcripts agree (line 2 is the shared part of a longer
line); line 3 is a style demo; line 4 is her official closing. ROMAJI lines are reading aids and are not spoken.)
