# ElevenLabs v4 Performance Sheet: Hakui Koyori

> Built from `bible/characters/Hakui-Koyori.md` (2026-10-02). Original designed voice matched only to register and
> energy; never clone or imitate the member's real voice (ElevenLabs Use Policy §5; COVER Derivative Works
> Guidelines). Koyori is active at the 2026 baseline. She streams in Japanese; lines below are given in Japanese or romanized with
> English glosses, and the voice works for Japanese, English or Chinese dialogue. Guide:
> `novel-lab/docs/elevenlabs-v4.md`.

## 1. Voice Design prompt (original voice)
"Perfect audio quality. Young woman, bright, clear, well-enunciated mid-high voice in presenter mode; quick and cheerful, leaping upward into squeals when excited and full screams when scared; sly and playful when teasing."
- The original voice's register is an independent design choice; mixed-recording pitch estimates are not synthesis targets.

## 2. Settings (starting points)
- `eleven_v4`. Stability **40%** (API `0.40`) (wide swings from presenter calm to squeals; an untested starting choice).
  Similarity **75%** (API `0.75`), referring only to the selected original voice.
- Pace comes from the designed voice plus `[cheerful, crisp]` or `[excited, fast]`; v4 has no speed slider.

## 3. Write these habits into the script
- "Konkoyo!" to open; "joshu-kun" (assistants) for her viewers.
- Crisp segment transitions on her news show: 「それでは続いてはこちら」 ("and next up").
- Speeds up and rises when explaining something that excites her.
- Experiments and "Koyorium" as running jokes; teasing stays playful.

## 4. Tag palette by situation
| Situation | Tags | Line |
|---|---|---|
| Opening | `[bright, cheerful]` | "Konkoyo!" (official) |
| Hosting | `[upbeat, announcer]` | 「それでは続いてはこちら」 ("Sore de wa tsuzuite wa kochira," "and next up") |
| Teasing a member | `[playful, sly]` | **Style demo:** "Kore mo kenkyū no tame dakara ne?" ("It's all for research, okay?") |
| Proud of an experiment | `[smug]` | **Style demo:** "Fufun, kanpeki na jikken kekka!" ("Heh, perfect results!") |
| A scare | `[screams]` | (tag only) |
| Thanking her assistants | `[warm]` | **Style demo:** "Joshu-kun, itsumo arigatō ne." ("Thanks as always, assistants.") |

With people (proposed scene directions, not observed conversational defaults): Chloe `[bickering, fond]`; Marine `[giddy]`; FUWAMOCO `[bubbly]`; La+ `[teasing]`.

## 5. Signature sounds
- "Konkoyo!" (spoken)
- `[giggles]` (tag only); `[screams]` (tag only)

## 6. Pronunciation (provisional; test)
- Reading guide (untested): はくい こより; こんこよ; じょしゅくん. Listen to how the chosen voice says them and adjust.

## 7. Don't
- A flat, sleepy, mumbled or coldly scientific voice.

## 8. Example
```
[bright, cheerful] Konkoyo!
[upbeat, announcer] Sore de wa tsuzuite wa kochira.
[playful, sly] Kore mo kenkyū no tame dakara ne?
[smug] Fufun, kanpeki na jikken kekka!
```
(Line 1 is her official greeting; line 2 is her line, quoted only where both transcripts agree; lines 3–4 are
style demos.)
