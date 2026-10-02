# ElevenLabs v4 Performance Sheet: Takane Lui

> Built from `bible/characters/Takane-Lui.md` (2026-10-02). Original designed voice matched only to register and
> energy; never clone or imitate the member's real voice (ElevenLabs Use Policy §5; COVER Derivative Works
> Guidelines). Lui is active at the 2026 baseline. She streams in Japanese; lines below are given in Japanese or romanized with
> English glosses, and the voice works for Japanese, English or Chinese dialogue. Guide:
> `novel-lab/docs/elevenlabs-v4.md`.

## 1. Voice Design prompt (original voice)
"Perfect audio quality. Young woman, low, calm, mature voice with a warm big-sister softness; unhurried and conversational; a cool, clipped executive tone for effect, undone by a cute sparkle; flustered laughter after a blunder."
- The original voice's register is an independent design choice; mixed-recording pitch estimates are not synthesis targets.
- Laughter, shrieks, breathiness and timbre are provisional choices for the original voice, not listening observations.

## 2. Settings (starting points)
- `eleven_v4`. Stability **55%** (API `0.55`) (calm and warm by default; an untested starting choice).
  Similarity **75%** (API `0.75`), referring only to the selected original voice.
- Pace comes from the designed voice plus `[calm, warm]` or `[cool, low]`; v4 has no speed slider.

## 3. Write these habits into the script
- "Mattakane?" to open and "Otsuluilui" to close; puns on her name ("Did I Luive you waiting!?").
- Calm, motherly chat: 「まあ誰にだってトラブルやミスはあるからね」 ("well, everyone has trouble and mistakes").
- Executive mode, then a cute "Ko!☆".
- Calls her own blunders "PON," and laughs.

## 4. Tag palette by situation
| Situation | Tags | Line |
|---|---|---|
| Opening | `[warm, lilting]` | "Mattakane?" (official) |
| Executive mode | `[cool, low] → [playful]` | **Style demo:** "Kore wa kanbu no shigoto yo. …Ko!☆" ("This is an executive's job. …Sparkle!") |
| Chatting | `[calm, motherly]` | 「まあ誰にだってトラブルやミスはあるからね」 ("Mā dare ni datte toraburu ya misu wa aru kara ne") |
| A blunder | `[flustered] → [laughs]` | "PON" (official) |
| Horror game | `[panicked, shrieking]` | **Style demo:** "Muri muri muri!" ("No way, no way!") |
| Closing | `[gentle]` | "Otsuluilui." (official) |

With people (proposed scene directions, not observed conversational defaults): La+ `[exasperated, fond]`; Kiara `[bright, friendly]`; Mumei `[gentle, sisterly]`; Okayu `[teasing]`.

## 5. Signature sounds (provisional; tag plus a written word is a scripting convention, not a guarantee of engine behavior)
- "Ko!☆" (spoken)
- `[laughs]` (tag only); `[screams]` (tag only)

## 6. Pronunciation (provisional; test)
- Reading guide (untested): たかね るい; まったかね; おつるいるい. Listen to how the chosen voice says them and adjust.

## 7. Don't
- A high, bubbly default; cold cruelty; nonstop shouting.

## 8. Example
```
[warm, lilting] Mattakane?
[calm, motherly] Mā, dare ni datte toraburu ya misu wa aru kara ne.
[cool, low] Kore wa kanbu no shigoto yo. [playful] …Ko!☆
[gentle] Otsuluilui.
```
(Lines 1 and 4 are her official greeting and sign-off; line 2 is her line, quoted only where both transcripts
agree; line 3 is a style demo.)
