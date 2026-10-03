# ElevenLabs v4 Performance Sheet: Takane Lui

> Built from `bible/characters/Takane-Lui.md` (2026-10-02). Original designed voice matched only to register and
> energy; never clone or imitate the member's real voice (ElevenLabs Use Policy §5; COVER Derivative Works
> Guidelines). Lui is active at the 2026 baseline. She streams in Japanese; lines below are given in Japanese or romanized with
> English glosses, and the voice works for Japanese, English or Chinese dialogue. Guide:
> `novel-lab/docs/elevenlabs-v4.md`.

## 1. Voice Design prompt (original voice)
"Perfect audio quality. Young woman, low, calm, mature voice with a warm big-sister softness; unhurried and conversational; a cool executive tone for effect, undone by a cute, clipped sparkle; a pleased little laugh after her own joke."
- The original voice's register is an independent design choice; mixed-recording pitch estimates are not synthesis targets.
- Laughter, shrieks, breathiness and timbre are provisional choices for the original voice, not listening observations.

## 2. Settings (untested audition choices; verify endpoint behavior)
- `eleven_v4`. Stability **55%** (API `0.55`) (calm and warm by default; an untested starting choice).
  Similarity **75%** (API `0.75`), referring only to the selected original voice.
- Pace comes from the designed voice plus `[calm, warm]` or `[cool, low]`; v4 has no speed slider.

## 3. Write these habits into the script
- 「まったかね～？」 ("Mattakane?") to open and 「おつルイルイ」 ("Otsuluilui") to close; wordplay on her name.
- Calm, motherly chat: 「まあ誰にだってトラブルやミスはあるからね」 ("well, everyone has trouble and mistakes").
- Executive mode, then a clipped 「コッ☆」 ("Ko!☆").
- Laughs ﾊｯﾊｰ↑ ("Haha↑") after her own joke (official phrase); "PON" is the fans' meme for her blunders, not a line she must say.

## 4. Tag palette by situation
| Situation | Tags | Line |
|---|---|---|
| Opening | `[warm, lilting]` | 「まったかね～？」 ("Mattakane?"; official) |
| Executive mode | `[cool, low] → [playful]` | **Style demo:** "Kore wa kanbu no shigoto yo. …Ko!☆" ("This is an executive's job. …Sparkle!") |
| Chatting | `[calm, motherly]` | 「まあ誰にだってトラブルやミスはあるからね」 ("Mā dare ni datte toraburu ya misu wa aru kara ne") |
| A joke lands | `[pleased]` | ﾊｯﾊｰ↑ ("Haha↑," official phrase) |
| A blunder | `[flustered] → [laughs]` | **Style demo:** "A, yatchatta…" ("Oops…") |
| Horror game | `[panicked, shrieking]` | **Style demo:** "Muri muri muri!" ("No way, no way!") |
| Closing | `[gentle]` | 「おつルイルイ」 ("Otsuluilui"; official) |

With people (proposed scene directions, not observed conversational defaults): La+ `[exasperated, fond]`; Kiara `[bright, friendly]`; Mumei `[gentle, sisterly]`; Okayu `[teasing]`.

Additional proposed scene directions from the card's Audio Tags (untested): `[deadpan]`, `[confident]`.

## 5. Signature sounds (provisional; tag plus a written word is a scripting convention, not a guarantee of engine behavior)
- "Ko!☆" (spoken, clipped)
- "Haha↑" (spoken, official phrase)
- `[laughs]` (tag only); `[screams]` (tag only); provisional choices

## 6. Pronunciation (provisional; test)
- Reading guide (untested): たかね るい; まったかね; おつるいるい; こっ☆ (clipped). Listen to how the chosen voice says them and adjust.

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
