# ElevenLabs v4 Performance Sheet: Isaki Riona

> Source voice fields SHA-256 (Name, Dialogue Style, Catchphrases, Voice & Delivery, Audio Tags): `pending` — reviewed: pending
> Built from `bible/characters/Isaki-Riona.md` (2026-11-27). Original designed voice matched only to register and
> energy; never clone or imitate the member's real voice (ElevenLabs Use Policy §5; COVER Derivative Works
> Guidelines). Riona is active at the 2026 baseline. She streams in Japanese; her audio dialogue is Japanese
> (author decision 2026-10-04 for the JP members): spoken lines are Japanese script; romaji and glosses are reading
> aids, not spoken. Guide: `novel-lab/docs/elevenlabs-v4.md`. GPT review pending (Claude-only sheet, 2026-11-27).

## 1. Voice Design prompt (original voice; provisional design choices)
"Perfect audio quality. Young woman, clear, bright mid-high voice with a confident, slightly cool edge; brisk and polite in set phrases, bursting into gleeful shouts when something goes her way, fiery when she loses, warm when she cheers people on."
- The original voice's register is an independent design choice; mixed-recording pitch estimates are not synthesis targets.
- Laughter, squeals and timbre are provisional choices for the original voice, not listening observations.
- Design and preview this voice with Japanese text (the §8 lines). Japanese is the project's dialogue language
  for the original voice, not a claim about the member.

## 2. Settings (untested starting choices; verify endpoint behavior)
- `eleven_v4`. Stability **40%** (API `0.40`) (bright with big emotional swings; an untested starting choice).
  Similarity **75%** (API `0.75`), referring only to the selected original voice.
- Pace comes from the designed voice plus `[bright, energetic]` or `[formal, upbeat]`; v4 has no speed slider.
- Dialogue language: **Japanese**. Write her spoken turns in Japanese script; romaji goes on a `ROMAJI ::` line and
  any English on `GLOSS ::` (neither is spoken). `tools/scene_to_elevenlabs.py` rejects a turn of hers that has no
  Japanese text.

## 3. Write these habits into the script
- Welcomes viewers home: 「おかえりおな〜！」 (okaeri-ona); opens formally with 「それでは挨拶をさせてください」.
- Celebrates lucky moments at full volume; hates losing.
- Cheers people on before she leaves: 「みんなも今日一日頑張ってね」「応援してるよ」.
- Softens a sharp remark with 「好きだよ」 ("I love you"); calls Calli 「大好きなカリオペ先輩」.
- No regional accent is assigned.

## 4. Tag palette by situation
| Situation | Tags | Line |
|---|---|---|
| Default | `[bright, energetic]` | **Style demo:** 「よし、今日もいくよ！」 ("Okay, here we go today too!") |
| Opening | `[formal, upbeat]` | 「それでは挨拶をさせてください」 ("Allow me to greet you") |
| A lucky pull | `[ecstatic, shouting]` | **Style demo:** 「きたきたきた！やったぁぁ！」 |
| Losing | `[frustrated]` | **Style demo:** 「悔しい！もう一回！」 ("So frustrating! One more!") |
| Horror | `[scared]` | **Style demo:** 「無理無理無理！」 ("No no no!") |
| Cheering viewers | `[warm, encouraging]` | 「みんなも今日一日頑張ってね」 ("You all do your best today too") |
| Leading the unit | `[confident]` | **Style demo:** 「FLOW GLOW、いくよ！」 |

With people (proposed scene directions, not observed conversational defaults): Calli `[adoring, excited]`; Niko `[playful]`; Chihaya `[teasing]`.

## 5. Signature sounds (provisional; tag plus a written word is a scripting convention, not a guarantee of engine behavior)
- `[squeals]` (tag only); `[laughs]` (tag only)

## 6. Pronunciation (provisional; test)
- Reading guide (untested): いさき りおな; おかえりおな; いさきれんごう (響咲連合). Listen to how the chosen voice says them and adjust.

## 7. Don't
- A timid, breathy whisper, a drowsy delivery or a flat, cold read.

## 8. Example
```
[formal, upbeat] それでは挨拶をさせてください。
ROMAJI :: Soredewa aisatsu o sasete kudasai.
[ecstatic, shouting] きたきたきた！やったぁぁ！
ROMAJI :: Kita kita kita! Yattaa!
[warm, encouraging] みんなも今日一日頑張ってね。
ROMAJI :: Minna mo kyō ichinichi ganbatte ne.
```
(Lines 1 and 3 are shared ASR spans; line 2 is a Style demo. ROMAJI lines are reading aids and are not spoken.)
