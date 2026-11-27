# ElevenLabs v4 Performance Sheet: Inugami Korone

> Source voice fields SHA-256 (Name, Dialogue Style, Catchphrases, Voice & Delivery, Audio Tags): `cf8f32d96cf5bd7d4f5005175b3fe6cba398dec1ad43a89cb53af625471901c5` — reviewed 2026-11-27: Claude 2026-11-27 (r02): all 40 sheets checked against the r02 voice-field changes (no removed quote left in a sheet; status and dialogue language match the cards; V20 palettes and span check pass); JP sheets gained the r02 greetings and sign-offs; 7 new sheets (FLOW GLOW, GAMERS); Gemini Neon review pending
> Built from `bible/characters/Inugami-Korone.md` (2026-11-27). Original designed voice matched only to register and
> energy; never clone or imitate the member's real voice (ElevenLabs Use Policy §5; COVER Derivative Works
> Guidelines). Korone is active at the 2026 baseline. She streams in Japanese; her audio dialogue is Japanese
> (author decision 2026-10-04 for the JP members): spoken lines are Japanese script; romaji and glosses are reading
> aids, not spoken. Guide: `novel-lab/docs/elevenlabs-v4.md`. Gemini Neon review pending (Claude-only sheet, 2026-11-27; the author dropped the GPT review).

## 1. Voice Design prompt (original voice; provisional design choices)
"Perfect audio quality. Young woman, high, bright, bouncy voice; drowsy and drawling in the morning; quick, playful and repetitive when tension builds; loud and triumphant when she wins; screaming and laughing through horror; warm and content when she wraps up."
- The original voice's register is an independent design choice; mixed-recording pitch estimates are not synthesis targets.
- Laughter, screams and timbre are provisional choices for the original voice, not listening observations.
- Design and preview this voice with Japanese text (the §8 lines). Japanese is the project's dialogue language
  for the original voice, not a claim about the member.

## 2. Settings (untested starting choices; verify endpoint behavior)
- `eleven_v4`. Stability **40%** (API `0.40`) (playful with big swings; an untested starting choice).
  Similarity **75%** (API `0.75`), referring only to the selected original voice.
- Pace comes from the designed voice plus `[playful, energetic]` or `[sleepy, cheerful]`; v4 has no speed slider.
- Dialogue language: **Japanese**. Write her spoken turns in Japanese script; romaji goes on a `ROMAJI ::` line and
  any English on `GLOSS ::` (neither is spoken). `tools/scene_to_elevenlabs.py` rejects a turn of hers that has no
  Japanese text.

## 3. Write these habits into the script
- Greets by asking for fingers: 「ぉぁょ~！ゆびゆび～」 (official).
- On her morning show: a drowsy 「はい、おはよー」.
- Repeats herself when tension builds (「待てよ待てよ」) and plays a game to the very end.
- Can wrap up by narrating herself in the third person: 「…ころねなのであった」.
- No regional accent is assigned.

## 4. Tag palette by situation
| Situation | Tags | Line |
|---|---|---|
| Default | `[playful, energetic]` | **Style demo:** 「よーし、今日もやるぞ～！」 ("Alright, let's do this today too!") |
| Morning show | `[sleepy, cheerful]` | 「はい、おはよー」 ("OK, mornin'") |
| Waiting on a game | `[suspicious]` | **Style demo:** 「待てよ待てよ、まだ油断できない」 ("Wait, wait, can't let my guard down yet") |
| A clear | `[triumphant, shouting]` | **Style demo:** 「クリアしたああああ！」 ("I cleared it!") |
| Horror | `[screaming]` | **Style demo:** 「無理無理無理！」 ("No no no!") |
| Asking for fingers | `[mischievous]` | 「ぉぁょ~！ゆびゆび～」 (official) |
| Wrapping up | `[content, warm]` | 「なんか朝枠もいいなって思うころねなのであった」 ("And so Korone thought a morning slot is kind of nice, too") |

With people (proposed scene directions, not observed conversational defaults): Okayu `[playful, affectionate]`; Mio `[teasing]`; Marine `[rowdy]`.

## 5. Signature sounds (provisional; tag plus a written word is a scripting convention, not a guarantee of engine behavior)
- `[laughs]` (tag only); `[screams]` (tag only)

## 6. Pronunciation (provisional; test)
- Reading guide (untested): いぬがみ ころね; ゆび; ころねすきー (Koronesky); ぉぁょ (oayo, a stylized おはよう). Listen to how the chosen voice says them and adjust.

## 7. Don't
- A cool, low deadpan, a breathy whisper or slow solemnity.

## 8. Example
```
[mischievous] ぉぁょ~！ゆびゆび～！
ROMAJI :: Oayo~! Yubi yubi~!
[sleepy, cheerful] はい、おはよー。
ROMAJI :: Hai, ohayō.
[content, warm] なんか朝枠もいいなって思う、ころねなのであった。
ROMAJI :: Nanka asawaku mo ii natte omou, Korone na no de atta.
```
(Line 1 is her official greeting; lines 2 and 3 are lines both ASR models heard. ROMAJI lines are reading aids and are not spoken.)
