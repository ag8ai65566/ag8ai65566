# ElevenLabs v4 Performance Sheet: Takane Lui

> Source voice fields SHA-256 (Name, Dialogue Style, Catchphrases, Voice & Delivery, Audio Tags): `622391ace3e619b4d2cdb5a30ff114164c9fc5ef394f52838dd914d93c29c368` — reviewed 2026-10-04: Claude 2026-10-04: voice audits v1-v4 merged (research/qa/voice-audit-dispositions.md); attestation research/qa/voice-delivery.md; author decisions 2026-10-04 (quote inventory B; JP members speak Japanese)
> Built from `bible/characters/Takane-Lui.md` (2026-10-02). Original designed voice matched only to register and
> energy; never clone or imitate the member's real voice (ElevenLabs Use Policy §5; COVER Derivative Works
> Guidelines). Lui is active at the 2026 baseline. She streams in Japanese; her audio dialogue is Japanese
> (author decision 2026-10-04): spoken lines are Japanese script; romaji and glosses are reading aids, not spoken. Guide:
> `novel-lab/docs/elevenlabs-v4.md`.

## 1. Voice Design prompt (original voice)
"Perfect audio quality. Young woman, low, calm, mature voice with a warm big-sister softness; unhurried and conversational; a cool executive tone for effect, undone by a cute, clipped sparkle; a pleased little laugh after her own joke."
- The original voice's register is an independent design choice; mixed-recording pitch estimates are not synthesis targets.
- Laughter, shrieks, breathiness and timbre are provisional choices for the original voice, not listening observations.
- Design and preview this voice with Japanese text (the §8 lines). Japanese is the project's dialogue language
  for the original voice, not a claim about the member.

## 2. Settings (untested starting choices; verify endpoint behavior)
- `eleven_v4`. Stability **55%** (API `0.55`) (calm and warm by default; an untested starting choice).
  Similarity **75%** (API `0.75`), referring only to the selected original voice.
- Pace comes from the designed voice plus `[calm, warm]` or `[cool, low]`; v4 has no speed slider.
- Dialogue language: **Japanese** (author decision 2026-10-04). Write her spoken turns in Japanese script;
  romaji goes on a `ROMAJI ::` line and any English on `GLOSS ::` (neither is spoken).
  `tools/scene_to_elevenlabs.py` rejects a turn of hers that has no Japanese text.

## 3. Write these habits into the script
- 「まったかね～？」 ("Mattakane?") to open and 「おつルイルイ」 ("Otsuluilui") to close; wordplay on her name.
- Calm, motherly chat: 「まあ誰にだってトラブルやミスはあるからね」 ("well, everyone has trouble and mistakes").
- Executive mode, then a clipped 「コッ☆」 ("Ko!☆").
- Laughs 「ﾊｯﾊｰ↑」 after her own joke (official written laugh; provisional reading はっはー, hahhā; in a script, ハッハー！); "PON" is the fans' meme for her blunders, not a line she must say.

## 4. Tag palette by situation
| Situation | Tags | Line |
|---|---|---|
| Opening | `[warm, lilting]` | 「まったかね～？」 ("Mattakane?"; official) |
| Executive mode | `[cool, low] → [playful]` | **Style demo:** 「これは幹部の仕事よ。…コッ☆」 ("Kore wa kanbu no shigoto yo. …Ko!☆", "This is an executive's job. …Sparkle!") |
| Chatting | `[calm, motherly]` | 「まあ誰にだってトラブルやミスはあるからね」 ("Mā dare ni datte toraburu ya misu wa aru kara ne") |
| A joke lands | `[pleased]` | 「ﾊｯﾊｰ↑」 (official written laugh; in a script, ハッハー！ with ROMAJI Hahhā!) |
| A blunder | `[flustered] → [laughs]` | **Style demo:** 「あ、やっちゃった…」 ("A, yatchatta…", "Oops…") |
| Horror game | `[panicked, shrieking]` | **Style demo:** 「無理無理無理！」 ("Muri muri muri!", "No way, no way!") |
| Closing | `[gentle]` | 「おつルイルイ」 ("Otsuluilui"; official) |

With people (proposed scene directions, not observed conversational defaults): La+ `[exasperated, fond]`; Kiara `[bright, friendly]`; Mumei `[gentle, sisterly]`; Okayu `[teasing]`.

Additional proposed scene directions from the card's Audio Tags (untested): `[deadpan]`, `[confident]`.

## 5. Signature sounds (provisional; tag plus a written word is a scripting convention, not a guarantee of engine behavior)
- 「コッ☆」 ("Ko!☆", spoken, clipped)
- 「ﾊｯﾊｰ↑」 (official written laugh; spoken as ハッハー！, provisional reading hahhā)
- `[laughs]` (tag only); `[screams]` (tag only); provisional choices

## 6. Pronunciation (provisional; test)
- Reading guide (untested): たかね るい; まったかね; おつるいるい; こっ☆ (clipped). Listen to how the chosen voice says them and adjust.

## 7. Don't
- A high, bubbly default; cold cruelty; nonstop shouting.

## 8. Example
```
[warm, lilting] まったかね～？
ROMAJI :: Mattakane?
[calm, motherly] まあ、誰にだってトラブルやミスはあるからね。
ROMAJI :: Mā, dare ni datte toraburu ya misu wa aru kara ne.
[cool, low] これは幹部の仕事よ。[playful] …コッ☆
ROMAJI :: Kore wa kanbu no shigoto yo. …Ko!☆
[pleased] ハッハー！
ROMAJI :: Hahhā!
[gentle] おつルイルイ。
ROMAJI :: Otsuluilui.
```
(Lines 1 and 5 are her official greeting and sign-off; line 4 renders her official written laugh ﾊｯﾊｰ↑ for speech
(a provisional reading); line 2 is her line, quoted only where both transcripts agree; line 3 is a style demo.
ROMAJI lines are reading aids and are not spoken.)
