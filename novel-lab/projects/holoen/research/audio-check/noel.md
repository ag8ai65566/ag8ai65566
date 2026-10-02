# Audio check — Shirogane Noel (2026-10-02)

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
(family, childhood, health, trips, daily life) are not quoted or summarized here.

## Windows measured

| Window | Stream | Segment | Speech (min) | Characters | Characters/min of speech | F0 median | F0 p10–p90 |
|---|---|---|---|---|---|---|---|
| chat25_2026 | [【朝活雑談】6月といえばジューンブライド...だんちょを貰ってください(圧)【白銀ノエル/ホロラ](https://youtu.be/99f7sLRAHHM) | [0:05:00–0:30:00](https://youtu.be/99f7sLRAHHM?t=300) | 20.4 | 5446 | 266.9 | 283 Hz | 213–462 Hz |
| dq20_2026 | [#9【ドラゴンクエストVII Reimagined】DQ7完全初見！ずっとプレイしてみたかった7](https://youtu.be/TrrD5iQGCGA) | [0:10:00–0:30:00](https://youtu.be/TrrD5iQGCGA?t=600) | 14.8 | 4667 | 314.3 | 260 Hz | 119–448 Hz |

"Characters/min of speech" = transcribed kana and kanji (punctuation dropped) ÷ minutes inside whisper's speech segments; it is a rough pace index for comparing windows, not a mora count.

## Marker counts (first model)

| Marker | chat25_2026 | dq20_2026 |
|---|---|---|
| first person 余 (yo) | 0 | 2 |
| first person 僕 (boku) | 0 | 2 |
| first person 私 | 0 | 10 |
| なんか | 36 | 12 |
| まあ | 13 | 6 |
| ちょっと待って | 0 | 1 |
| やばい | 1 | 2 |
| かわいい | 1 | 2 |
| えっ/え? | 1 | 5 |
| laugh (はは/ふふ/笑) | 0 | 1 |
| ありがとう | 4 | 1 |
| English (Latin letters) | 0 | 1 |

## Claims checked

| Claim in the file | Result (in the machine transcript) | Evidence (ASR, archived audio) |
|---|---|---|
| Recaps her week on the Sunday-morning chat | **Observed**: 「今週ね、何があったかと言いますと、まぁ色々ありましたな」, then "as much as I can share." | [0:05:28](https://youtu.be/99f7sLRAHHM?t=328) |
| Calls herself "Danchou" | **Observed** (the first model writes 「男帳」/「男長」, so no line with it is quoted). | [0:06:23](https://youtu.be/99f7sLRAHHM?t=383) |
| Recommends games eagerly | **Observed**: 「いやぜひみなさんもやってみて欲しい」 ("really, I want you all to try it too"). | [0:08:52](https://youtu.be/99f7sLRAHHM?t=532) |
| First playthrough of Dragon Quest VII Reimagined | **Observed** (2026). | [0:11:00](https://youtu.be/TrrD5iQGCGA?t=660) |

## Second model (whisper medium) on quoted lines

| First model (small) | At | Second model (medium), excerpt | Verdict |
|---|---|---|---|
| "まぁ色々ありましたな" | [0:05:28](https://youtu.be/99f7sLRAHHM?t=328) | "…と言いますとまぁ色々ありましたなまぁ色々あり…" | **Shared span (computed):** whole line (kana/kanji folded) |
| "いやぜひみなさんもやってみて欲しい" | [0:08:52](https://youtu.be/99f7sLRAHHM?t=532) | "…しかったからいや ぜひ みなさんもね やってみ…" | **Partial (computed):** shared run "いやぜひみなさんも"; only that part is quoted |
| "今週ね、何があったかと言いますと、まぁ色々ありましたな" | [0:05:28](https://youtu.be/99f7sLRAHHM?t=328) | "…ぁ今週ねまぁ何があったかと言いますとまぁ色々ありましたなまぁ色々あり…" | **Partial (computed):** shared run "何があったかと言いますとまあ色々ありましたな"; only that part is quoted |
