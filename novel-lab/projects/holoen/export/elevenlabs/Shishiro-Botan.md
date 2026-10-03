# ElevenLabs v4 Performance Sheet: Shishiro Botan

> Built from `bible/characters/Shishiro-Botan.md` (2026-10-02). Original designed voice matched only to register and
> energy; never clone or imitate the member's real voice (ElevenLabs Use Policy §5; COVER Derivative Works
> Guidelines). Botan is active at the 2026 baseline. She streams in Japanese; lines below are given in Japanese or romanized with
> English glosses, and the voice works for Japanese, English or Chinese dialogue. Guide:
> `novel-lab/docs/elevenlabs-v4.md`.

## 1. Voice Design prompt (original voice; provisional design choices)
"Perfect audio quality. Young woman, clear, cool-toned but cheerful voice; relaxed and amused in play, brisk and orderly when presenting, with an easy, frequent laugh."
- The original voice's register is an independent design choice; mixed-recording pitch estimates are not synthesis targets.
- Laughter, shrieks, breathiness and timbre are provisional choices for the original voice, not listening observations.

## 2. Settings (untested starting choices; verify endpoint behavior)
- `eleven_v4`. Stability **55%** (API `0.55`) (relaxed and steady; an untested starting choice).
  Similarity **75%** (API `0.75`), referring only to the selected original voice.
- Pace comes from the designed voice plus `[relaxed, cheerful]` or `[brisk, organized]`; v4 has no speed slider.

## 3. Write these habits into the script
- "La-lion♪" to open; "Well then, cya~" to close (official profile wording).
- A brisk explanatory register when presenting a project: 「前回はですねペコちゃんが優勝しました」 ("last time, Peko-chan won").
- An offhand 「ぽい」 (poi; secondary transcription) as she lobs a grenade.
- Proposed horror-scene direction, informed by secondary descriptions: begin with calm amusement or teasing when appropriate, and allow surprise when the scene warrants it.

## 4. Tag palette by situation
| Situation | Tags | Line |
|---|---|---|
| Opening | `[breezy]` | "La-lion♪" (official) |
| Presenting a project | `[brisk, organized]` | 「前回はですねペコちゃんが優勝しました」 ("Zenkai wa desu ne, Peko-chan ga yūshō shimashita") |
| FPS play | `[calm, focused]` | **Style demo:** "Hidari, hitori kezutta." ("Left, one's weakened.") |
| Throwing a grenade | `[offhand]` | 「ぽい」 ("Poi!", secondary transcription) |
| Lamy in a horror scene (fictional direction) | `[amused, reassuring]` | **Style demo:** "Daijōbu daijōbu, mada nani mo dete nai yo." ("It's fine, it's fine, nothing's even come out yet.") |
| Closing | `[easy]` | "Well then, cya~" (official English) |

With people (proposed scene directions, not observed conversational defaults): Lamy in a horror scene `[amused, reassuring]`; Ina `[warm]`.

Additional proposed scene directions from the card's Audio Tags (untested): `[amused, teasing]`, `[surprised, laughing]`.

## 5. Signature sounds (provisional; tag plus a written word is a scripting convention, not a guarantee of engine behavior)
- "Poi!" (spoken)
- `[laughs]` (tag only)

## 6. Pronunciation (provisional; test)
- Reading guide (untested): ししろ ぼたん; ししろん; ぽいっ. Listen to how the chosen voice says them and adjust.

## 7. Don't
- A gruff, deep "tough girl" voice; a sleepy drawl.

## 8. Example
```
[breezy] La-lion♪
[brisk, organized] Zenkai wa desu ne, Peko-chan ga yūshō shimashita.
[offhand] Poi!
[amused, teasing] Daijōbu daijōbu, mada nani mo dete nai yo.
```
(Line 1 is her official greeting; line 2 is her line, quoted only where both transcripts agree; line 3 is her
grenade call as a secondary transcription; line 4 is a style demo.)
