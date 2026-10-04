# ElevenLabs v4 Performance Sheet: Kikirara Vivi

> Built from `bible/characters/Kikirara-Vivi.md` (2026-10-02). Original designed voice matched only to register and
> energy; never clone or imitate the member's real voice (ElevenLabs Use Policy §5; COVER Derivative Works
> Guidelines). Vivi is active at the 2026 baseline. She streams in Japanese; her audio dialogue is Japanese
> (author decision 2026-10-04): spoken lines are Japanese script; romaji and glosses are reading aids, not spoken. Guide:
> `novel-lab/docs/elevenlabs-v4.md`.

## 1. Voice Design prompt (original voice; provisional design choices)
"Perfect audio quality. Young woman, bright, slightly husky, girlish voice; lively, frank and fast in banter, deliberately flat for a deadpan retort, loud screams in horror, warm and sincere with her fans."
- The original voice's register is an independent design choice; mixed-recording pitch estimates are not synthesis targets.
- Laughter, shrieks, breathiness and timbre are provisional choices for the original voice, not listening observations.
- Design and preview this voice with Japanese text (the §8 lines). Japanese is the project's dialogue language
  for the original voice, not a claim about the member.

## 2. Settings (untested starting choices; verify endpoint behavior)
- `eleven_v4`. Stability **40%** (API `0.40`) (lively, with deliberate flat turns; an untested starting choice).
  Similarity **75%** (API `0.75`), referring only to the selected original voice.
- Pace comes from the designed voice plus `[lively, frank]` or `[deadpan]`; v4 has no speed slider.
- Dialogue language: **Japanese** (author decision 2026-10-04). Write her spoken turns in Japanese script;
  romaji goes on a `ROMAJI ::` line and any English on `GLOSS ::` (neither is spoken).
  `tools/scene_to_elevenlabs.py` rejects a turn of hers that has no Japanese text.

## 3. Write these habits into the script
- Opens as her archived stream titles write it, ん～～ッヴィヴィ～！！！ ("Nnn—Vivi!"); calls her fans "Vivid" and herself 「ヴィヴィ」 ("Vivi").
- Deliberately flattens her delivery for comic retorts (she has explained this on stream).
- Teases that affection costs extra: 「お金取るで」 ("I'll charge you for that").
- Casual endings (-yan, -nen, akan, honma) appear in her transcripts; no regional accent is assigned to the voice.

## 4. Tag palette by situation
| Situation | Tags | Line |
|---|---|---|
| Opening | `[theatrical, rising]` | ん～～ッヴィヴィ～！！！ (archived title wording) |
| Comic retort | `[deadpan]` | **Style demo:** 「おーい！」 ("Ōi!"; the exact word is not a verified quotation) |
| Chat asks for something sweet | `[playful, coy]` | 「お金取るで」 ("Okane toru de," "I'll charge you for that") |
| Horror | `[screams]` | (tag only) |
| Thanking her fans | `[warm, sincere]` | **Style demo:** 「みんながおらんとヴィヴィ頑張られへん。」 ("Minna ga oran to Vivi ganbararehen.", "I can't do my best without you all.") |

With people (proposed scene directions, not observed conversational defaults): Pekora `[adoring, excited]`; Marine `[playful]`; FUWAMOCO `[cheerful]`.

Additional proposed scene directions from the card's Audio Tags (untested): `[chatty, quick]`, `[flustered]`.

## 5. Signature sounds (provisional; tag plus a written word is a scripting convention, not a guarantee of engine behavior)
- `[laughs]` (tag only); `[screams]` (tag only)

## 6. Pronunciation (provisional; test)
- Reading guide (untested): ききらら ゔぃゔぃ. Listen to how the chosen voice says them and adjust.

## 7. Don't
- Prim standard speech, a breathy whisper by default, or a coolly aloof read.

## 8. Example
```
[theatrical, rising] ん～～ッヴィヴィ～！！！
ROMAJI :: Nnnnn~ Vivi!!!
[deadpan] おーい！
ROMAJI :: Ōi!
[playful, coy] お金取るで。
ROMAJI :: Okane toru de.
[warm, sincere] みんながおらんとヴィヴィ頑張られへん。
ROMAJI :: Minna ga oran to Vivi ganbararehen.
```
(Line 1 is a Style demo adapted from archived title wording; its stretching and rising delivery are provisional. Lines 2 and 4 are Style demos. Line 3 is a shared ASR span. The exact spoken opening has not been verified here. ROMAJI lines are reading aids and are not spoken.)
