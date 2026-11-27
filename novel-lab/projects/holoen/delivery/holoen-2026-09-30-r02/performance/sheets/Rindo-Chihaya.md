# ElevenLabs v4 Performance Sheet: Rindo Chihaya

> Source voice fields SHA-256 (Name, Dialogue Style, Catchphrases, Voice & Delivery, Audio Tags): `f6adc967df590e0ac30f814937563ab7f325ea2945fc03f81b025b94f0896f05` — reviewed 2026-11-27: Claude 2026-11-27 (r02): all 40 sheets checked against the r02 voice-field changes (no removed quote left in a sheet; status and dialogue language match the cards; V20 palettes and span check pass); JP sheets gained the r02 greetings and sign-offs; 7 new sheets (FLOW GLOW, GAMERS); GPT review pending
> Built from `bible/characters/Rindo-Chihaya.md` (2026-11-27). Original designed voice matched only to register and
> energy; never clone or imitate the member's real voice (ElevenLabs Use Policy §5; COVER Derivative Works
> Guidelines). Chihaya is active at the 2026 baseline. She streams in Japanese; her audio dialogue is Japanese
> (author decision 2026-10-04 for the JP members): spoken lines are Japanese script; romaji and glosses are reading
> aids, not spoken. Guide: `novel-lab/docs/elevenlabs-v4.md`. GPT review pending (Claude-only sheet, 2026-11-27).

## 1. Voice Design prompt (original voice; provisional design choices)
"Perfect audio quality. Young woman, clear, lively mid-range voice with a cool edge; rapid, laughing chatter, fired up for racing and DJing, softening into polite warmth late at night."
- The original voice's register is an independent design choice; mixed-recording pitch estimates are not synthesis targets.
- Laughter and timbre are provisional choices for the original voice, not listening observations.
- Design and preview this voice with Japanese text (the §8 lines). Japanese is the project's dialogue language
  for the original voice, not a claim about the member.

## 2. Settings (untested starting choices; verify endpoint behavior)
- `eleven_v4`. Stability **40%** (API `0.40`) (fast and lively with soft endings; an untested starting choice).
  Similarity **75%** (API `0.75`), referring only to the selected original voice.
- Pace comes from the designed voice plus `[lively, chatty]` or `[polite, soft]`; v4 has no speed slider.
- Dialogue language: **Japanese**. Write her spoken turns in Japanese script; romaji goes on a `ROMAJI ::` line and
  any English on `GLOSS ::` (neither is spoken). `tools/scene_to_elevenlabs.py` rejects a turn of hers that has no
  Japanese text.

## 3. Write these habits into the script
- Calls herself 「ちは」; opens a chat with 「こんばんはー」 and 「雑談でございます」.
- Talks without brakes, laughing, then turns polite: 「遅くまでお付き合いありがとうございました」, 「いい夢見てね」.
- Loves cars and racing; calls her fans 「ニック」.
- No regional accent is assigned.

## 4. Tag palette by situation
| Situation | Tags | Line |
|---|---|---|
| Default | `[lively, chatty]` | **Style demo:** 「ちはね、今日めっちゃ話したいことあるの！」 |
| Opening | `[casual, bright]` | 「こんばんはー」 ("Good evening~") |
| A long story | `[rapid, laughing]` | **Style demo:** 「ちょっと待って、聞いて聞いて！」 ("Wait, listen, listen!") |
| Racing | `[fired up]` | **Style demo:** 「全開でいくよ！」 ("Going full throttle!") |
| DJing | `[confident, hype]` | **Style demo:** 「みんな、声出していこう！」 |
| Signing off | `[polite, soft]` | 「遅くまでお付き合いありがとうございました」 |
| To her fans | `[warm, affectionate]` | 「いい夢見てね」 ("Sweet dreams") |

With people (proposed scene directions, not observed conversational defaults): Su `[cheerful]`; Okayu `[adoring]`; Riona `[teasing]`.

## 5. Signature sounds (provisional; tag plus a written word is a scripting convention, not a guarantee of engine behavior)
- `[laughs]` (tag only); 「ちょっと待って」 ("chotto matte," spoken)

## 6. Pronunciation (provisional; test)
- Reading guide (untested): りんどう ちはや; ちは; ふぐたろう (ふぐ太郎). Listen to how the chosen voice says them and adjust.

## 7. Don't
- A shy whisper, a slow hesitant delivery, or a cold, terse read.

## 8. Example
```
[casual, bright] こんばんはー。
ROMAJI :: Konbanwa.
[rapid, laughing] ちょっと待って、聞いて聞いて！
ROMAJI :: Chotto matte, kiite kiite!
[polite, soft] ということでお疲れ様でした。遅くまでお付き合いありがとうございました。
ROMAJI :: To iu koto de otsukaresama deshita. Osoku made otsukiai arigatō gozaimashita.
[warm, affectionate] いい夢見てね。
ROMAJI :: Ii yume mite ne.
```
(Lines 1, 3 and 4 are shared ASR spans; line 2 is a Style demo. ROMAJI lines are reading aids and are not spoken.)
