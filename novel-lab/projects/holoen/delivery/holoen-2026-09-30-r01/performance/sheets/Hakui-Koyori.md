# ElevenLabs v4 Performance Sheet: Hakui Koyori

> Source voice fields SHA-256 (Name, Dialogue Style, Catchphrases, Voice & Delivery, Audio Tags): `31ccc30aa7a83fa4da6bc4bf8e450d48dc7926dbf448697536d5b7d9f7e9c03d` — reviewed 2026-10-04: Claude 2026-10-04: voice audits v1-v4 merged (research/qa/voice-audit-dispositions.md); attestation research/qa/voice-delivery.md; author decisions 2026-10-04 (quote inventory B; JP members speak Japanese)
> Built from `bible/characters/Hakui-Koyori.md` (2026-10-02). Original designed voice matched only to register and
> energy; never clone or imitate the member's real voice (ElevenLabs Use Policy §5; COVER Derivative Works
> Guidelines). Koyori is active at the 2026 baseline. She streams in Japanese; her audio dialogue is Japanese
> (author decision 2026-10-04): spoken lines are Japanese script; romaji and glosses are reading aids, not spoken. Guide:
> `novel-lab/docs/elevenlabs-v4.md`.

## 1. Voice Design prompt (original voice)
"Perfect audio quality. Young woman, bright, clear, well-enunciated mid-high voice in presenter mode; quick and cheerful, leaping upward into squeals when excited and full screams when scared; sly and playful when teasing."
- The original voice's register is an independent design choice; mixed-recording pitch estimates are not synthesis targets.
- Laughter, shrieks, breathiness and timbre are provisional choices for the original voice, not listening observations.
- Design and preview this voice with Japanese text (the §8 lines). Japanese is the project's dialogue language
  for the original voice, not a claim about the member.

## 2. Settings (untested starting choices; verify endpoint behavior)
- `eleven_v4`. Stability **40%** (API `0.40`) (wide swings from presenter calm to squeals; an untested starting choice).
  Similarity **75%** (API `0.75`), referring only to the selected original voice.
- Pace comes from the designed voice plus `[cheerful, crisp]` or `[excited, fast]`; v4 has no speed slider.
- Dialogue language: **Japanese** (author decision 2026-10-04). Write her spoken turns in Japanese script;
  romaji goes on a `ROMAJI ::` line and any English on `GLOSS ::` (neither is spoken).
  `tools/scene_to_elevenlabs.py` rejects a turn of hers that has no Japanese text.

## 3. Write these habits into the script
- 「こんこよ～！」 ("Konkoyo~!") to open; 「助手くん」 ("joshu-kun," assistants) for her viewers; 「こよりちゃん」 for herself.
- Crisp segment transitions on her news show: 「それでは続いてはこちら」 ("and next up").
- Invites viewers warmly: 「ぜひぜひ見てみてください」 ("please do take a look").
- Excited explanations may speed up and rise (a provisional direction); experiments and 「コヨリニウム」 ("koyoriniumu") are running jokes.

## 4. Tag palette by situation
| Situation | Tags | Line |
|---|---|---|
| Opening | `[bright, cheerful]` | 「こんこよ～！」 ("Konkoyo~!"; official) |
| Hosting | `[upbeat, announcer]` | 「それでは続いてはこちら」 ("Sore de wa tsuzuite wa kochira," "and next up") |
| Inviting viewers | `[warm, upbeat]` | 「ぜひぜひ見てみてください」 ("Zehi zehi mite mite kudasai," "please do take a look") |
| Teasing a member | `[playful, sly]` | **Style demo:** 「これも研究のためだからね？」 ("Kore mo kenkyū no tame dakara ne?", "It's all for research, okay?") |
| Proud of an experiment | `[smug]` | **Style demo:** 「ふふん、完璧な実験結果！」 ("Fufun, kanpeki na jikken kekka!", "Heh, perfect results!") |
| A scare | `[screams]` | (tag only) |

With people (proposed scene directions, not observed conversational defaults): Chloe `[bickering, fond]`; Marine `[giddy]`; FUWAMOCO `[bubbly]`; La+ `[teasing]`.

Additional proposed scene directions from the card's Audio Tags (untested): `[warm]`.

## 5. Signature sounds (provisional; tag plus a written word is a scripting convention, not a guarantee of engine behavior)
- 「こんこよ～！」 ("Konkoyo!", spoken)
- `[giggles]` (tag only; the recorded giggle is a first-model observation, so this is a provisional choice); `[screams]` (tag only)

## 6. Pronunciation (provisional; test)
- Reading guide (untested): はくい こより; こんこよ; じょしゅくん; こよりにうむ. Listen to how the chosen voice says them and adjust.

## 7. Don't
- A flat, sleepy, mumbled or coldly scientific voice.

## 8. Example
```
[bright, cheerful] こんこよ～！
ROMAJI :: Konkoyo~!
[upbeat, announcer] それでは続いてはこちら。
ROMAJI :: Sore de wa tsuzuite wa kochira.
[warm, upbeat] ぜひぜひ見てみてください！
ROMAJI :: Zehi zehi mite mite kudasai!
[playful, sly] これも研究のためだからね？
ROMAJI :: Kore mo kenkyū no tame dakara ne?
```
(Line 1 is her official greeting; lines 2 and 3 are her lines, quoted only where both transcripts agree; line 4 is a
style demo. ROMAJI lines are reading aids and are not spoken.)
