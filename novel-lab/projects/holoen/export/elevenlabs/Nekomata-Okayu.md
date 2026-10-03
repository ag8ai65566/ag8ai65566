# ElevenLabs v4 Performance Sheet: Nekomata Okayu

> Built from `bible/characters/Nekomata-Okayu.md` (2026-10-02). Original designed voice matched only to register
> and energy; never clone or imitate the member's real voice (ElevenLabs Use Policy §5; COVER Derivative Works
> Guidelines). Okayu is active at the 2026 baseline. She streams in Japanese; lines below are romanized with
> English glosses, and the voice works for Japanese, English or Chinese dialogue. Guide:
> `novel-lab/docs/elevenlabs-v4.md`.

## 1. Voice Design prompt (original voice; provisional design choices)
"Perfect audio quality. Young woman, soft, relaxed, boyish voice; lazy and warm, unhurried with trailing vowels,
a playful purr when teasing, a laugh that climbs high."
- The climbing laugh follows a secondary description; the purr is an original performance choice. Neither is a
  listening observation.
- This is an original voice-design choice. Mixed-recording F0 and ASR character-rate measurements are
  descriptive research data, not synthesis targets or evidence of the member's isolated vocal range.

## 2. Settings (untested audition choices; verify endpoint behavior)
- `eleven_v4`. Stability **50%** (API `0.50`) (relaxed and steady). Similarity **75%** (API `0.75`).
- Pace comes from the designed voice plus `[relaxed, warm]` or `[playful]`; v4 has no speed slider.

## 3. Write these habits into the script
- "Boku" for "I"; "Mogu mogu~ Okayu~!" to greet; "Onigiryā" for her fans.
- "Nori de" ("by vibes") appears in one sampled game opening; use it as a situational example. "Rettsura gō!" is a documented start cue; repeated "nya" is documented during play.
- Narrating her own play in long, relaxed sentences; agreeing with everyone.
- Flirty teasing kept light and non-explicit.

## 4. Tag palette by situation
| Situation | Tags | Line |
|---|---|---|
| Greeting | `[lazy, warm]` | "Mogu mogu~ Okayu~!" (official) |
| Starting a game | `[breezy]` | "Nori de aite o buttaoshitai to omoimāsu." |
| Exploring a new game | `[contented, chatty]` | "Atarashii gēmu dakara, minna to issho ni tesaguri tansaku na no tanoshii nā." |
| A move that feels good | `[pleased]` | "Nya nya nya nya." |
| Teasing a member | `[playful]` | **Style demo:** "Kawaii nē." |
| Found guilty | `[cheerful, unbothered]` | **Style demo:** "Hai, yūzai desu. Tsugunaimasu." |
| Laughing hard | `[laughs harder]` | (tag only) |

With people (proposed scene directions, not observed conversational defaults): Korone `[comfortable, fond]`;
Ina `[mellow]`; FUWAMOCO `[fond senpai, teasing]`.

Additional proposed scene directions from the card's Audio Tags (untested): `[easygoing]`, `[soft, tearful]`.

## 5. Signature sounds
- "mogu mogu" (spoken); repeated "nya" (spoken; documented); `[laughs]` (tag only).

## 6. Pronunciation (provisional; test)
- Japanese reading: ねこまた おかゆ; おにぎりゃー. No regional accent is assigned without an in-scope listening
  check. Listen to how the chosen voice says them and adjust.

## 7. Don't
- Not as default: a high, sugary voice or harsh, aggressive delivery. Stronger reactions follow the scene. Keep flirting non-explicit.

## 8. Example
```
[lazy, warm] Mogu mogu~ Okayu~!
[breezy] Nori de aite o buttaoshitai to omoimāsu.
[contented, chatty] Atarashii gēmu dakara, minna to issho ni tesaguri tansaku na no tanoshii nā.
[pleased] Nya nya nya nya.
[playful] Kawaii nē.
```
(Line 1 is her official greeting; line 5 is a style demo; lines 2–4 are her lines, quoted only where both
transcripts agree; the number of "nya" in line 4 is illustrative, not fixed.)
