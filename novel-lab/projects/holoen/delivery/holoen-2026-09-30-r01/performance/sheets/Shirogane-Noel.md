# ElevenLabs v4 Performance Sheet: Shirogane Noel

> Source voice fields SHA-256 (Name, Dialogue Style, Catchphrases, Voice & Delivery, Audio Tags): `2dbf6c08a3dbdf8b5e83f74327bdf1907d3ae020f86055a54bb19ddc04a70851` — reviewed 2026-10-04: Claude 2026-10-04: voice audits v1-v4 merged (research/qa/voice-audit-dispositions.md); attestation research/qa/voice-delivery.md; author decisions 2026-10-04 (quote inventory B; JP members speak Japanese)
> Built from `bible/characters/Shirogane-Noel.md` (2026-10-02). Original designed voice matched only to register and
> energy; never clone or imitate the member's real voice (ElevenLabs Use Policy §5; COVER Derivative Works
> Guidelines). Noel is active at the 2026 baseline. She streams in Japanese; her audio dialogue is Japanese
> (author decision 2026-10-04): spoken lines are Japanese script; romaji and glosses are reading aids, not spoken. Guide:
> `novel-lab/docs/elevenlabs-v4.md`.

## 1. Voice Design prompt (original voice; provisional design choices)
"Perfect audio quality. Young woman, soft, girlish, warm voice, higher than her armor suggests; bubbly and eager in chat, flustered when she loses, with a gentler older-sister register available."
- The original voice's register is an independent design choice; mixed-recording pitch estimates are not synthesis targets.
- Laughter, shrieks, breathiness and timbre are provisional choices for the original voice, not listening observations.
- Design and preview this voice with Japanese text (the §8 lines). Japanese is the project's dialogue language
  for the original voice, not a claim about the member.

## 2. Settings (untested starting choices; verify endpoint behavior)
- `eleven_v4`. Stability **45%** (API `0.45`) (warm, with flustered swings; an untested starting choice).
  Similarity **75%** (API `0.75`), referring only to the selected original voice.
- Pace comes from the designed voice plus `[cheerful, warm]` or `[chatty, relaxed]`; v4 has no speed slider.
- Dialogue language: **Japanese** (author decision 2026-10-04). Write her spoken turns in Japanese script;
  romaji goes on a `ROMAJI ::` line and any English on `GLOSS ::` (neither is spoken).
  `tools/scene_to_elevenlabs.py` rejects a turn of hers that has no Japanese text.

## 3. Write these habits into the script
- Calls herself 「団長」 ("Danchou," commander) and her viewers 「団員さん」 ("danin-san"); muscle-themed greetings: the official 「こんまっする〜」 (konmassuru), 「おはまっする」 (ohamassuru, mornings; both ASR models) and 「こんばんまっする〜」 (konbanmassuru~, as the wiki transcribes it).
- Recaps her week in old-fashioned phrasing: 「まぁ色々ありましたな」 ("well, quite a lot happened").
- Eager game recommendations.
- Mock jealousy about Flare is on-stream comedy; keep it light.

## 4. Tag palette by situation
| Situation | Tags | Line |
|---|---|---|
| Greeting | `[hearty, bright]` | 「こんまっする〜」 ("Konmassuru~", official) |
| Recapping the week | `[chatty, relaxed]` | 「まぁ色々ありましたな」 ("Mā iroiro arimashita na") |
| Recommending something | `[eager]` | **Style demo:** 「みんなもぜひ遊んでみて！」 ("Minna mo zehi asonde mite!", "You all should try it too!") |
| Losing a game | `[flustered, wailing]` | **Style demo:** 「団長の筋肉が足りなかった…！」 ("Danchou no kinniku ga tarinakatta…!", "Danchou's muscles weren't enough…!") |
| The Flare bit (comedy) | `[mock-jealous, pouty]` | **Style demo:** 「フレアは団長のだよ！？」 ("Furea wa danchou no da yo!?", "Flare is mine, you know!?") |
| Older-sister mode | `[gentle, lower]` | **Style demo:** 「大丈夫、ゆっくりでいいからね。」 ("Daijōbu, yukkuri de ii kara ne.", "It's okay, take your time.") |

With people (proposed scene directions, not observed conversational defaults): Flare `[playful, fond]`; Marine `[bickering, playful]`; Pekora `[competitive]`.

## 5. Signature sounds (provisional; tag plus a written word is a scripting convention, not a guarantee of engine behavior)
- 「こんまっする〜」 ("Konmassuru~", spoken)
- `[laughs]` (tag only)

## 6. Pronunciation (provisional; test)
- Reading guide (untested): しろがね のえる; だんちょう; こんまっする. Listen to how the chosen voice says them and adjust.

## 7. Don't
- A gruff warrior; a cold or sultry default.

## 8. Example
```
[hearty, bright] こんまっする〜！
ROMAJI :: Konmassuru~!
[chatty, relaxed] まぁ、色々ありましたな。
ROMAJI :: Mā, iroiro arimashita na.
[eager] みんなもぜひ遊んでみて！
ROMAJI :: Minna mo zehi asonde mite!
[flustered, wailing] 団長の筋肉が足りなかった…！
ROMAJI :: Danchou no kinniku ga tarinakatta…!
```
(Line 1 is her official greeting wording; line 2 is her line, quoted only where both transcripts agree; lines 3–4 are
style demos. ROMAJI lines are reading aids and are not spoken.)
