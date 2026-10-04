# Audio check — Yukihana Lamy (2026-10-02)

Method: windows from the public stream archive archive.ragtag.moe (YouTube blocks this environment),
transcribed in Japanese with faster-whisper small (multilingual), pitch measured with Praat (100–600 Hz, speech
segments only). Tools and limits: `novel-lab/tools/audiocheck/README.md`. **This is not a listening check**: the
audio was machine-transcribed and acoustically measured, and the transcripts were reviewed in context. Lines used
on the character card were re-transcribed by a second model (whisper medium, multilingual) and compared after
folding katakana to hiragana and dropping punctuation (see the end of this file). Transcription does not write
laughs reliably, and Japanese ASR often picks different kanji or kana for the same word; only spans both models
render identically are quoted. Measurements describe the sampled recording and ASR segmentation; game audio,
music and other voices prevent treating them as isolated vocal measurements.

All windows are from 2026. Only in-scope public performance material is used: personal remarks in the chats
are not quoted or summarized here.

## Windows measured

| Window | Stream | Segment | Speech (min) | Characters | Characters/min of speech | F0 median | F0 p10–p90 |
|---|---|---|---|---|---|---|---|
| banshaku25_2026 | [【晩酌】雪夜月で晩酌、しちゃう…？♡【雪花ラミィ /ホロライブ】](https://youtu.be/bquezhdXu2E) | [0:05:00–0:30:00](https://youtu.be/bquezhdXu2E?t=300) | 17.8 | 5905 | 332.1 | 303 Hz | 132–472 Hz |
| village20_2026 | [【ぷちホロの村 - 剣とお店と田舎暮らし】魔法使いラミィの、のんびり田舎暮らし！！【雪花ラミィ ](https://youtu.be/d2u2FOBGhy4) | [0:10:00–0:30:00](https://youtu.be/d2u2FOBGhy4?t=600) | 14.2 | 2359 | 166.5 | 261 Hz | 110–497 Hz |

"Characters/min of speech" = transcribed kana and kanji (punctuation dropped) ÷ minutes inside whisper's speech segments; it is a rough pace index for comparing windows, not a mora count.

## Marker counts (first model)

| Marker | banshaku25_2026 | village20_2026 |
|---|---|---|
| first person 余 (yo) | 0 | 1 |
| first person 私 | 1 | 0 |
| なんか | 20 | 7 |
| まあ | 7 | 3 |
| ちょっと待って | 1 | 4 |
| やばい | 0 | 1 |
| かわいい | 5 | 0 |
| えっ/え? | 0 | 2 |
| swear (くそ/ふざけ/殺) | 3 | 0 |
| ありがとう | 2 | 0 |
| English (Latin letters) | 8 | 0 |

## Claims checked

| Claim in the file | Result (in the machine transcript) | Evidence (ASR, archived audio) |
|---|---|---|
| Evening-drink chat format with a toast | **Observed**: 「とりあえず、乾杯しないと何も始まらない」 ("nothing starts until we toast first"), then 「今週も、皆様、お疲れ様でございました」. | [0:06:04](https://youtu.be/bquezhdXu2E?t=364), [0:06:35](https://youtu.be/bquezhdXu2E?t=395) |
| Third-person "Lamy" | **Observed** (two dozen times in the evening window; the first model spells it variously). | [0:05:45](https://youtu.be/bquezhdXu2E?t=345) |
| Polite set phrases sliding into casual slang | **Observed**: formal "o-tsukaresama de gozaimashita" alongside "hona," "chū koto de," "umē." | [0:06:28](https://youtu.be/bquezhdXu2E?t=388) |
| Cozy slow-life games | **Observed**: a village-life game in which she plays a wizard. | [0:11:40](https://youtu.be/d2u2FOBGhy4?t=700) |

## Second model (whisper medium) on quoted lines

| First model (small) | At | Second model (medium), excerpt | Verdict |
|---|---|---|---|
| "乾杯しないと何も始まらない" | [0:06:04](https://youtu.be/bquezhdXu2E?t=364) | "…なとりあえず乾杯しないと何も始まらないということで…" | **Shared span (computed):** whole line (kana/kanji folded) |
| "今週も、皆様、お疲れ様でございました" | [0:06:35](https://youtu.be/bquezhdXu2E?t=395) | "…おつかれさまでございましたほな、乾杯で…" | **Shared span (computed):** whole line (same reading; the models spell a word differently) |
| "とりあえず、乾杯しないと何も始まらない" | [0:06:04](https://youtu.be/bquezhdXu2E?t=364) | "…ようぜみんなとりあえず乾杯しないと何も始まらないということで…" | **Shared span (computed):** whole line (kana/kanji folded) |
