# ElevenLabs v4 Performance Sheet: Nakiri Ayame

> Source voice fields SHA-256 (Name, Dialogue Style, Catchphrases, Voice & Delivery, Audio Tags): `9487b1e2dcc63cf88ba6b960a5235a928a5956c45b6eaab69ea779bd9f7f7c46` — reviewed 2026-10-04: Claude 2026-10-04: voice audits v1-v4 merged (research/qa/voice-audit-dispositions.md); attestation research/qa/voice-delivery.md; author decisions 2026-10-04 (quote inventory B; JP members speak Japanese)
> Built from `bible/characters/Nakiri-Ayame.md` (2026-10-02). Original designed voice matched only to register
> and energy; never clone or imitate the member's real voice (ElevenLabs Use Policy §5; COVER Derivative Works
> Guidelines). Ayame is active at the 2026 baseline. She streams in Japanese; her audio dialogue is Japanese
> (author decision 2026-10-04): spoken lines are Japanese script; romaji and glosses are reading aids, not spoken. Guide:
> `novel-lab/docs/elevenlabs-v4.md`.

## 1. Voice Design prompt (original voice; provisional design choices)
"Perfect audio quality. Young woman, soft and cute mid-high voice with a playful, mock-haughty edge; chatty and
unhurried, dissolving into quick giggles; shaky and breathless when frightened."
- Giggles are a provisional performance choice (secondary description), not a listening observation.
- This is an original voice-design choice. Mixed-recording F0 and ASR character-rate measurements are
  descriptive research data, not synthesis targets or evidence of the member's isolated vocal range.
- Design and preview this voice with Japanese text (the §8 lines). Japanese is the project's dialogue language
  for the original voice, not a claim about the member.

## 2. Settings (untested starting choices; verify endpoint behavior)
- `eleven_v4`. Stability **40%** (API `0.40`) (giggles and mood swings). Similarity **75%** (API `0.75`).
- Pace comes from the designed voice plus `[playful, warm]` or `[scared, shaky]`; v4 has no speed slider.
- Dialogue language: **Japanese** (author decision 2026-10-04). Write her spoken turns in Japanese script;
  romaji goes on a `ROMAJI ::` line and any English on `GLOSS ::` (neither is spoken).
  `tools/scene_to_elevenlabs.py` rejects a turn of hers that has no Japanese text.

## 3. Write these habits into the script
- 「余」 ("Yo") for "I" and 「人間様」 ("ningen-sama") for her viewers; 「こんなきり！」 ("Konnakiri!", her official greeting, also heard in use by both ASR models) and 「余だよ！」 ("Yo da yo!", secondary transcription; not audio-verified).
- Polite at first (「聞こえておりますでしょうか？」, "Kikoete orimasu deshō ka?"), casual within minutes (「マジで」「めっちゃ」).
- Pouting scolds: 「うるさい！」 ("Urusai!"); separately, 「困った人たち」 ("Komatta hitotachi") (two ASR excerpts, not one spoken turn).
- In horror: 「声が震えちゃう」 ("Koe ga furuechau"), 「落ち着いて落ち着いて」 ("Ochitsuite, ochitsuite").

## 4. Tag palette by situation
| Situation | Tags | Line |
|---|---|---|
| Greeting | `[bright, playful]` | 「こんなきり！」 ("Konnakiri!", official greeting; both ASR models hear it in use) |
| The oni act | `[mock-haughty]` | 「余だよ！」 ("Yo da yo!", secondary transcription; not verified by the two-model audio check) |
| Opening a stream | `[polite, careful]` | 「聞こえておりますでしょうか？」 ("Kikoete orimasu deshō ka?") |
| Teasing chat | `[pouting]` | 「うるさい！」 (ASR); separately, 「困った人たち」 (ASR) |
| Horror game | `[scared, shaky]` | 「今驚かされたら本当に心臓が止まりそう」 ("Ima odorokasaretara hontō ni shinzō ga tomarisō") |
| FPS clutch | `[focused, quick]` | **Style demo:** 「味方、いけるよ！」 ("Mikata, ikeru yo!", "Team, we can do this!") |
| A bad pun | `[giggles]` → `[laughs harder]` | (tag only) |

With people (proposed scene directions, not observed conversational defaults): Fubuki and Mio `[comfortable, giggly]`;
Okayu `[teasing]`; Kiara `[polite, excited]`.

Additional proposed scene directions from the card's Audio Tags (untested): `[shy, careful]`.

## 5. Signature sounds
- `[giggles]` (tag only); **Style demo:** 「もう〜」 ("Mō~", spoken).

## 6. Pronunciation (provisional; test)
- Japanese reading: なきり あやめ; こんなきり; 余＝よ. Regional accent and pitch-accent patterns are unverified.
  Listen to how the chosen voice says them and adjust.

## 7. Don't
- A cruel or menacing oni; a cold, superior read; a monotone.

## 8. Example
```
[polite, careful] 聞こえておりますでしょうか？
ROMAJI :: Kikoete orimasu deshō ka?
[bright, playful] こんなきり！
ROMAJI :: Konnakiri!
[pouting] うるさい！
ROMAJI :: Urusai!
[pouting] 困った人たち。
ROMAJI :: Komatta hitotachi.
[scared, shaky] 声が震えちゃう。
ROMAJI :: Koe ga furuechau.
[scared, shaky] 今驚かされたら本当に心臓が止まりそう。
ROMAJI :: Ima odorokasaretara hontō ni shinzō ga tomarisō.
```
(Line 2 is her official greeting, which both ASR models also hear in use. Lines 1 and 3–6 are separate shared ASR
excerpts, not one conversation. Their delivery tags are proposed performance directions, not listening findings.
ROMAJI lines are reading aids and are not spoken.)
