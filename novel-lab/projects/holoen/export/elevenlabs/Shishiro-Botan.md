# ElevenLabs v4 Performance Sheet: Shishiro Botan

> Built from `bible/characters/Shishiro-Botan.md` (2026-10-02). Original designed voice matched only to register and
> energy; never clone or imitate the member's real voice (ElevenLabs Use Policy §5; COVER Derivative Works
> Guidelines). Botan is active at the 2026 baseline. She streams in Japanese; her audio dialogue is Japanese
> (author decision 2026-10-04): spoken lines are Japanese script; romaji and glosses are reading aids, not spoken. Guide:
> `novel-lab/docs/elevenlabs-v4.md`.

## 1. Voice Design prompt (original voice; provisional design choices)
"Perfect audio quality. Young woman, clear, cool-toned but cheerful voice; relaxed and amused in play, brisk and orderly when presenting, with an easy, frequent laugh."
- The original voice's register is an independent design choice; mixed-recording pitch estimates are not synthesis targets.
- Laughter, shrieks, breathiness and timbre are provisional choices for the original voice, not listening observations.
- Design and preview this voice with Japanese text (the §8 lines). Japanese is the project's dialogue language
  for the original voice, not a claim about the member.

## 2. Settings (untested starting choices; verify endpoint behavior)
- `eleven_v4`. Stability **55%** (API `0.55`) (relaxed and steady; an untested starting choice).
  Similarity **75%** (API `0.75`), referring only to the selected original voice.
- Pace comes from the designed voice plus `[relaxed, cheerful]` or `[brisk, organized]`; v4 has no speed slider.
- Dialogue language: **Japanese** (author decision 2026-10-04). Write her spoken turns in Japanese script;
  romaji goes on a `ROMAJI ::` line and any English on `GLOSS ::` (neither is spoken).
  `tools/scene_to_elevenlabs.py` rejects a turn of hers that has no Japanese text.

## 3. Write these habits into the script
- "La-lion♪" to open and "Well then, cya~" to close (official profile wording), each said inside a Japanese turn.
- A brisk explanatory register when presenting a project: 「前回はですねペコちゃんが優勝しました」 ("last time, Peko-chan won").
- An offhand 「ぽい」 (poi; secondary transcription) as she lobs a grenade.
- Proposed horror-scene direction, informed by secondary descriptions: begin with calm amusement or teasing when appropriate, and allow surprise when the scene warrants it.

## 4. Tag palette by situation
| Situation | Tags | Line |
|---|---|---|
| Opening | `[breezy]` | "La-lion♪" (official; say it inside a Japanese turn, as in §8 line 1) |
| Presenting a project | `[brisk, organized]` | 「前回はですねペコちゃんが優勝しました」 ("Zenkai wa desu ne, Peko-chan ga yūshō shimashita") |
| FPS play | `[calm, focused]` | **Style demo:** 「左、一人削った。」 ("Hidari, hitori kezutta.", "Left, one's weakened.") |
| Throwing a grenade | `[offhand]` | 「ぽい」 ("Poi!", secondary transcription) |
| Lamy in a horror scene (fictional direction) | `[amused, reassuring]` | **Style demo:** 「大丈夫大丈夫、まだ何も出てないよ。」 ("Daijōbu daijōbu, mada nani mo dete nai yo.", "It's fine, it's fine, nothing's even come out yet.") |
| Closing | `[easy]` | "Well then, cya~" (official English; inside a Japanese turn) |

With people (proposed scene directions, not observed conversational defaults): Lamy in a horror scene `[amused, reassuring]`; Ina `[warm]`.

Additional proposed scene directions from the card's Audio Tags (untested): `[amused, teasing]`, `[surprised, laughing]`.

## 5. Signature sounds (provisional; tag plus a written word is a scripting convention, not a guarantee of engine behavior)
- 「ぽい！」 ("Poi!", spoken)
- `[laughs]` (tag only)

## 6. Pronunciation (provisional; test)
- Reading guide (untested): ししろ ぼたん; ししろん; ぽいっ. Listen to how the chosen voice says them and adjust.

## 7. Don't
- A gruff, deep "tough girl" voice; a sleepy drawl.

## 8. Example
```
[breezy] La-lion♪ 獅白ぼたんです。
ROMAJI :: La-lion♪ Shishiro Botan desu.
[brisk, organized] 前回はですね、ペコちゃんが優勝しました。
ROMAJI :: Zenkai wa desu ne, Peko-chan ga yūshō shimashita.
[offhand] ぽい！
ROMAJI :: Poi!
[amused, teasing] 大丈夫大丈夫、まだ何も出てないよ。
ROMAJI :: Daijōbu daijōbu, mada nani mo dete nai yo.
```
(Line 1 joins her official greeting to a style-demo self-introduction; line 2 is her line, quoted only where both
transcripts agree; line 3 is her grenade call as a secondary transcription; line 4 is a style demo. ROMAJI lines are
reading aids and are not spoken.)
