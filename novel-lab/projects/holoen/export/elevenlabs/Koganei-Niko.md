# ElevenLabs v4 Performance Sheet: Koganei Niko

> Source voice fields SHA-256 (Name, Dialogue Style, Catchphrases, Voice & Delivery, Audio Tags): `pending` — reviewed: pending
> Built from `bible/characters/Koganei-Niko.md` (2026-11-27). Original designed voice matched only to register and
> energy; never clone or imitate the member's real voice (ElevenLabs Use Policy §5; COVER Derivative Works
> Guidelines). Niko is active at the 2026 baseline. She streams in Japanese; her audio dialogue is Japanese
> (author decision 2026-10-04 for the JP members): spoken lines are Japanese script; romaji and glosses are reading
> aids, not spoken. Guide: `novel-lab/docs/elevenlabs-v4.md`. GPT review pending (Claude-only sheet, 2026-11-27).

## 1. Voice Design prompt (original voice; provisional design choices)
"Perfect audio quality. Young woman, relaxed, slightly husky mid-range voice built for comedy; swings from pompous mock-formality to blunt, quick banter; loud and panicky when scared; warm with her fans."
- The original voice's register is an independent design choice; mixed-recording pitch estimates are not synthesis targets.
- Laughter, wails and timbre are provisional choices for the original voice, not listening observations.
- Design and preview this voice with Japanese text (the §8 lines). Japanese is the project's dialogue language
  for the original voice, not a claim about the member.

## 2. Settings (untested starting choices; verify endpoint behavior)
- `eleven_v4`. Stability **35%** (API `0.35`) (comic swings between registers; an untested starting choice).
  Similarity **75%** (API `0.75`), referring only to the selected original voice.
- Pace comes from the designed voice plus `[playful, casual]` or `[mock-formal, theatrical]`; v4 has no speed slider.
- Dialogue language: **Japanese**. Write her spoken turns in Japanese script; romaji goes on a `ROMAJI ::` line and
  any English on `GLOSS ::` (neither is spoken). `tools/scene_to_elevenlabs.py` rejects a turn of hers that has no
  Japanese text.

## 3. Write these habits into the script
- Calls herself 「ニコたん」; her fans are 「ニコ担」 (said the same way).
- Swings from exaggerated formal apologies to blunt casual speech (「ほんまにごめん」).
- Signs off with a chant: 「ニコたんが〜、帰宅〜！」 then 「バイバ〜イ」.
- No regional accent is assigned.

## 4. Tag palette by situation
| Situation | Tags | Line |
|---|---|---|
| Default | `[playful, casual]` | **Style demo:** 「ニコたんだよ〜」 ("It's Nikotan~") |
| A bit gone wrong | `[mock-formal, theatrical]` | **Style demo:** 「誠に申し訳ございませんでした。」 ("I most humbly apologize.") |
| Banter | `[deadpan]` | 「ほんまにごめん」 ("Really sorry") |
| Signing off | `[chanting, cheerful]` | 「ニコたんが〜、帰宅〜！」 ("Nikotan is going ho~me!") |
| Horror | `[panicked]` | **Style demo:** 「ちょっ、待って待って！」 ("Wait, wait!") |
| Thanking her fans | `[warm]` | **Style demo:** 「ニコ担、いつもありがとね。」 |
| A morning show | `[groggy, upbeat]` | **Style demo:** 「おはよ〜、朝ガオの時間だよ」 |

With people (proposed scene directions, not observed conversational defaults): Riona `[teasing]`; Lui `[whiny, pleading]`; Su `[goofy]`.

## 5. Signature sounds (provisional; tag plus a written word is a scripting convention, not a guarantee of engine behavior)
- `[laughs]` (tag only); `[wails]` (tag only)

## 6. Pronunciation (provisional; test)
- Reading guide (untested): こがねい にこ; にこたん; きたく (帰宅). Listen to how the chosen voice says them and adjust.

## 7. Don't
- A delicate, breathy voice, prim formality held for a whole scene, or a coldly aloof read.

## 8. Example
```
[mock-formal, theatrical] 誠に申し訳ございませんでした。
ROMAJI :: Makoto ni mōshiwake gozaimasen deshita.
[deadpan] ほんまにごめん。
ROMAJI :: Honma ni gomen.
[chanting, cheerful] ニコたんが〜、帰宅〜！
ROMAJI :: Nikotan ga, kitaku!
```
(Line 1 is a Style demo; line 2 is a shared ASR span; line 3 follows the sign-off both models heard, with 帰宅 as our reading. ROMAJI lines are reading aids and are not spoken.)
