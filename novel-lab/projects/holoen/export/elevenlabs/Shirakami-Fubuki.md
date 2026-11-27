# ElevenLabs v4 Performance Sheet: Shirakami Fubuki

> Source voice fields SHA-256 (Name, Dialogue Style, Catchphrases, Voice & Delivery, Audio Tags): `a56948f6a420ca7fb1720a2467720b41aaefa4911b9adc54f556f9d843863d23` — reviewed 2026-11-27: Claude 2026-11-27 (r02): all 40 sheets checked against the r02 voice-field changes (no removed quote left in a sheet; status and dialogue language match the cards; V20 palettes and span check pass); JP sheets gained the r02 greetings and sign-offs; 7 new sheets (FLOW GLOW, GAMERS); Gemini Neon review pending
> Built from `bible/characters/Shirakami-Fubuki.md` (2026-11-27). Original designed voice matched only to register
> and energy; never clone or imitate the member's real voice (ElevenLabs Use Policy §5; COVER Derivative Works
> Guidelines). Fubuki is active at the 2026 baseline. She streams in Japanese; her audio dialogue is Japanese
> (author decision 2026-10-04 for the JP members): spoken lines are Japanese script; romaji and glosses are reading
> aids, not spoken. Guide: `novel-lab/docs/elevenlabs-v4.md`. Gemini Neon review pending (Claude-only sheet, 2026-11-27; the author dropped the GPT review).

## 1. Voice Design prompt (original voice; provisional design choices)
"Perfect audio quality. Young woman, bright, clear, high voice; quick, lively and well organized like a cheerful MC; dropping into a gruff, comic register for a joke; warm and sincere when she gives advice; deadpan for a game over, then laughing."
- The original voice's register is an independent design choice; mixed-recording pitch estimates are not synthesis targets.
- Laughter and timbre are provisional choices for the original voice, not listening observations.
- Kurokami Fubuki, her alter ego, is a separate character with a rough register; do not use it for Fubuki's lines.
- Design and preview this voice with Japanese text (the §8 lines). Japanese is the project's dialogue language
  for the original voice, not a claim about the member.

## 2. Settings (untested starting choices; verify endpoint behavior)
- `eleven_v4`. Stability **45%** (API `0.45`) (lively but orderly; an untested starting choice).
  Similarity **75%** (API `0.75`), referring only to the selected original voice.
- Pace comes from the designed voice plus `[cheerful, energetic]` or `[warm, orderly]`; v4 has no speed slider.
- Dialogue language: **Japanese**. Write her spoken turns in Japanese script; romaji goes on a `ROMAJI ::` line and
  any English on `GLOSS ::` (neither is spoken; her English bits such as "Hi, Friends!" may be written in katakana,
  ハイ、フレンズ！). `tools/scene_to_elevenlabs.py` rejects a turn of hers that has no Japanese text.

## 3. Write these habits into the script
- Calls herself 「白上」 (Shirakami); greets 「こんこんきーつね！白上フブキです！」 (official) or "Hi, Friends!".
- Her own words for each moment (official Q&A): 「はじまんぼう」 to start, 「おはこん」/「よるこん」 as greetings, "F" at a game over, 「おつこーん」 to end.
- Comic indignation in gruff 「～じゃい！」 / 「～やんけ！」 endings; 「キツネです！」 ("I'm a fox!") if called a cat.
- Closes in order: 「ということで、今日はこの辺りで終わっていこうと思います」, then 「ではでは」 and 「おつこーん」.
- No regional accent is assigned.

## 4. Tag palette by situation
| Situation | Tags | Line |
|---|---|---|
| Default | `[cheerful, energetic]` | **Style demo:** 「はい、今日もやっていきましょー！」 ("OK, let's get going today too!") |
| Opening | `[bright, upbeat]` | 「こんこんきーつね！白上フブキです！」 (official) |
| Called a cat | `[indignant, comic]` | 「キツネです！」 (official Q&A) |
| Game over | `[deadpan]` | **Style demo:** 「はい、F。」 ("Yep. F.") |
| Advising kouhai | `[warm, sincere]` | 「このキツネの先輩の言葉に流されず、ぜひ自分らしく配信をしてほしいです」 |
| Closing | `[warm, orderly]` | 「ということで、今日はこの辺りで終わっていこうと思います」 |
| FBKINGDOM stage | `[regal, playful]` | **Style demo:** 「フブキングダムへようこそ！」 ("Welcome to FBKINGDOM!") |

With people (proposed scene directions, not observed conversational defaults): Mio `[playful, affectionate]`; Okayu `[teasing]`; Marine `[rowdy]`; kouhai `[encouraging]`.

## 5. Signature sounds (provisional; tag plus a written word is a scripting convention, not a guarantee of engine behavior)
- `[laughs]` (tag only)

## 6. Pronunciation (provisional; test)
- Reading guide (untested): しらかみ ふぶき; こんこんきーつね; すこんぶ (すこん部); おつこーん; はじまんぼう. Listen to how the chosen voice says them and adjust.

## 7. Don't
- A slow, sleepy drawl, a cold, aloof read or Kurokami Fubuki's rough voice.

## 8. Example
```
[bright, upbeat] こんこんきーつね！白上フブキです！
ROMAJI :: Konkon kītsune! Shirakami Fubuki desu!
[warm, sincere] このキツネの先輩の言葉に流されず、ぜひ自分らしく配信をしてほしいです。
ROMAJI :: Kono kitsune no senpai no kotoba ni nagasarezu, zehi jibunrashiku haishin o shite hoshii desu.
[warm, orderly] ということで、今日はこの辺りで終わっていこうと思います。
ROMAJI :: To iu koto de, kyō wa kono atari de owatte ikō to omoimasu.
```
(Line 1 is her official greeting; lines 2 and 3 are lines both ASR models heard. ROMAJI lines are reading aids and are not spoken.)
