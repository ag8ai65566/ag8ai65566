# ElevenLabs v4 Performance Sheet: Kikirara Vivi

> Built from `bible/characters/Kikirara-Vivi.md` (2026-10-02). Original designed voice matched only to register and
> energy; never clone or imitate the member's real voice (ElevenLabs Use Policy §5; COVER Derivative Works
> Guidelines). Vivi is active at the 2026 baseline. She streams in Japanese; lines below are given in Japanese or romanized with
> English glosses, and the voice works for Japanese, English or Chinese dialogue. Guide:
> `novel-lab/docs/elevenlabs-v4.md`.

## 1. Voice Design prompt (original voice)
"Perfect audio quality. Young woman, bright, slightly husky, girlish voice; lively, frank and fast in banter, deliberately flat for a deadpan retort, loud screams in horror, warm and sincere with her fans."
- The original voice's register is an independent design choice; mixed-recording pitch estimates are not synthesis targets.
- Laughter, shrieks, breathiness and timbre are provisional choices for the original voice, not listening observations.

## 2. Settings (starting points)
- `eleven_v4`. Stability **40%** (API `0.40`) (lively, with deliberate flat turns; an untested starting choice).
  Similarity **75%** (API `0.75`), referring only to the selected original voice.
- Pace comes from the designed voice plus `[lively, frank]` or `[deadpan]`; v4 has no speed slider.

## 3. Write these habits into the script
- Opens with a rising "Nnnnnn~ Vivi!!!"; calls her fans "Vivid."
- Retorts with a deliberately flat, emotionless "Ōi!"
- Teases that affection costs extra: 「お金取るで」 ("I'll charge you for that").
- Regional dialect endings live in the words ("-de," "-hen," "honma"); no accent is assigned to the voice itself.

## 4. Tag palette by situation
| Situation | Tags | Line |
|---|---|---|
| Opening | `[theatrical, rising]` | "Nnnnnn~ Vivi!!!" (secondary transcription) |
| Retort | `[deadpan]` | "Ōi!" |
| Chat asks for something sweet | `[playful, coy]` | 「お金取るで」 ("Okane toru de," "I'll charge you for that") |
| Horror | `[screams]` | (tag only) |
| Thanking her fans | `[warm, sincere]` | **Style demo:** "Minna ga oran to Vivi ganbararehen." ("I can't do my best without you all.") |

With people (proposed scene directions, not observed conversational defaults): Pekora `[adoring, excited]`; Marine `[playful]`; FUWAMOCO `[cheerful]`.

## 5. Signature sounds (provisional; tag plus a written word is a scripting convention, not a guarantee of engine behavior)
- "Ōi!" (spoken, deadpan)
- `[laughs]` (tag only); `[screams]` (tag only)

## 6. Pronunciation (provisional; test)
- Reading guide (untested): ききらら ゔぃゔぃ; おーい. Listen to how the chosen voice says them and adjust.

## 7. Don't
- Prim standard speech, a breathy whisper by default, or a coolly aloof read.

## 8. Example
```
[theatrical, rising] Nnnnnn~ Vivi!!!
[deadpan] Ōi!
[playful, coy] Okane toru de.
[warm, sincere] Minna ga oran to Vivi ganbararehen.
```
(Line 1 is her opening as a secondary transcription; lines 2–3 are her lines from the sampled audio (line 3
quoted only where both transcripts agree); line 4 is a style demo.)
