# ElevenLabs v4 Performance Sheet: Yukihana Lamy

> Source voice fields SHA-256 (Name, Dialogue Style, Catchphrases, Voice & Delivery, Audio Tags): `bdf3daf6fde4f1c39c5a453ef066cc7c7ea6e31f3e41dd8f5fa4b93a9a1f7f04` — reviewed 2026-10-04: Claude 2026-10-04: voice audits v1-v4 merged (research/qa/voice-audit-dispositions.md); attestation research/qa/voice-delivery.md; author decisions 2026-10-04 (quote inventory B; JP members speak Japanese)
> Built from `bible/characters/Yukihana-Lamy.md` (2026-10-02). Original designed voice matched only to register and
> energy; never clone or imitate the member's real voice (ElevenLabs Use Policy §5; COVER Derivative Works
> Guidelines). Lamy is active at the 2026 baseline. She streams in Japanese; her audio dialogue is Japanese
> (author decision 2026-10-04): spoken lines are Japanese script; romaji and glosses are reading aids, not spoken. Guide:
> `novel-lab/docs/elevenlabs-v4.md`.

## 1. Voice Design prompt (original voice; provisional design choices)
"Perfect audio quality. Young woman, soft, bright, gentle voice with a refined, polite surface; quick and cheerful in banter, motherly and soothing when comforting, breathy and squeaky when scared."
- The original voice's register is an independent design choice; mixed-recording pitch estimates are not synthesis targets.
- Laughter, shrieks, breathiness and timbre are provisional choices for the original voice, not listening observations.
- Design and preview this voice with Japanese text (the §8 lines). Japanese is the project's dialogue language
  for the original voice, not a claim about the member.

## 2. Settings (untested starting choices; verify endpoint behavior)
- `eleven_v4`. Stability **50%** (API `0.50`) (gentle and steady; an untested starting choice).
  Similarity **75%** (API `0.75`), referring only to the selected original voice.
- Pace comes from the designed voice plus `[gentle, cheerful]` or `[casual, quick]`; v4 has no speed slider.
- Dialogue language: **Japanese** (author decision 2026-10-04). Write her spoken turns in Japanese script;
  romaji goes on a `ROMAJI ::` line and any English on `GLOSS ::` (neither is spoken).
  `tools/scene_to_elevenlabs.py` rejects a turn of hers that has no Japanese text.

## 3. Write these habits into the script
- "Lamyoohoo!" (official) to open, said inside a Japanese turn; 「雪民」 ("Yukimin") for her fans.
- Formal thanks, then casual banter: 「今週も、皆様、お疲れ様でございました」.
- In a sampled June 2026 evening chat she invites a toast: 「とりあえず、乾杯しないと何も始まらない」 ("nothing starts until we toast first"); keep the toast light and non-specific.
- Motherly comfort and shyness are proposed scene directions.

## 4. Tag palette by situation
| Situation | Tags | Line |
|---|---|---|
| Opening | `[sweet, bright]` | "Lamyoohoo!" (official; say it inside a Japanese turn, as in §8 line 1) |
| Thanking chat | `[warm, formal]` | 「今週も、皆様、お疲れ様でございました」 ("Konshū mo, minasama, otsukaresama de gozaimashita") |
| Banter | `[casual, quick]` | 「とりあえず、乾杯しないと何も始まらない」 ("Toriaezu, kanpai shinai to nani mo hajimaranai") |
| Comforting | `[motherly, soft]` | **Style demo:** 「大丈夫、ラミィがついてるからね。」 ("Daijōbu, Ramii ga tsuiteru kara ne.", "It's all right, Lamy's here with you.") |
| Horror | `[panicked, squeaky]` | `[gasps]` (tag only) |
| Flustered | `[shy]` | **Style demo:** 「えー、そんなこと言わないでよ〜」 ("Ē, sonna koto iwanaide yo~", "Eh, don't say things like that~") |

With people (proposed scene directions, not observed conversational defaults): Botan during a frightening game `[panicked, seeking reassurance]`; Koyori `[giggly]`; Nene `[playful]`.

## 5. Signature sounds (provisional; tag plus a written word is a scripting convention, not a guarantee of engine behavior)
- 「乾杯！」 ("Kanpai!", spoken)
- `[giggles]` (tag only); `[gasps]` (tag only)

## 6. Pronunciation (provisional; test)
- Reading guide (untested): ゆきはな らみぃ; ゆきみん; かんぱい. Listen to how the chosen voice says them and adjust.

## 7. Don't
- A cold or harsh voice, or a slurred caricature.

## 8. Example
```
[sweet, bright] Lamyoohoo! ラミィだよ〜。
ROMAJI :: Lamyoohoo! Ramii da yo~.
[casual, quick] とりあえず、乾杯しないと何も始まらない。
ROMAJI :: Toriaezu, kanpai shinai to nani mo hajimaranai.
[warm, formal] 今週も、皆様、お疲れ様でございました。
ROMAJI :: Konshū mo, minasama, otsukaresama de gozaimashita.
[motherly, soft] 大丈夫、ラミィがついてるからね。
ROMAJI :: Daijōbu, Ramii ga tsuiteru kara ne.
```
(Line 1 joins her official greeting to a style-demo phrase; lines 2–3 are her lines, quoted only where both
transcripts agree (line 3 with the same reading in both); line 4 is a style demo. ROMAJI lines are reading aids and
are not spoken.)
