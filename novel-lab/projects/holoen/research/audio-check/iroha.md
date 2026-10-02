# Audio check — Kazama Iroha (2026-10-02)

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
| kanji20_2026 | [【漢字でGOGO】信じられないかもですがサムネの子はかなり賢い子です。【風真いろは/ホロライブ】](https://youtu.be/fhc67kDKU94) | [0:05:00–0:25:00](https://youtu.be/fhc67kDKU94?t=300) | 11.0 | 2548 | 232.1 | 290 Hz | 129–455 Hz |
| elden20_2026 | [【ELDENRING】ラスボス目の前にして数か月ぶりだが大丈夫だろうか【風真いろは/ホロライブ】](https://youtu.be/ufbZgdek7XU) | [0:10:00–0:30:00](https://youtu.be/ufbZgdek7XU?t=600) | 10.2 | 2495 | 243.5 | 295 Hz | 177–436 Hz |

"Characters/min of speech" = transcribed kana and kanji (punctuation dropped) ÷ minutes inside whisper's speech segments; it is a rough pace index for comparing windows, not a mora count.

## Marker counts (first model)

| Marker | kanji20_2026 | elden20_2026 |
|---|---|---|
| first person 余 (yo) | 14 | 1 |
| first person 私 | 1 | 0 |
| なんか | 16 | 17 |
| まあ | 35 | 1 |
| ちょっと待って | 5 | 2 |
| やばい | 12 | 3 |
| かわいい | 2 | 0 |
| えっ/え? | 16 | 8 |
| laugh (はは/ふふ/笑) | 1 | 0 |
| こんなきり/こんにちは | 1 | 0 |

## Claims checked

| Claim in the file | Result (in the machine transcript) | Evidence (ASR, archived audio) |
|---|---|---|
| "de gozaru" as a sentence ending (wiki) | **Rare in 2026 windows**: almost no sentence-final "de gozaru" in a kanji game and an ELDEN RING stream; she does call herself 「ゴザル」 ("Gozaru") in the third person. | [0:14:30](https://youtu.be/ufbZgdek7XU?t=870), [0:17:38](https://youtu.be/ufbZgdek7XU?t=1058) |
| Laughs off her blunders | **Observed**: after mixing up 牛 and 午 she says something like "well, sometimes you're a dud like that" (the models disagree on 「ポンコツ」, so it is not quoted). | [0:05:46](https://youtu.be/fhc67kDKU94?t=346) |
| Repeats words in fours when it goes well | **Observed**: 「よしよしよしよし」. | [0:07:59](https://youtu.be/fhc67kDKU94?t=479) |
| Talks back to chat | **Observed**: a loud "oi" at chat's teasing in the kanji game. | [0:06:47](https://youtu.be/fhc67kDKU94?t=407) |
| Sticks with long games | **Observed**: returning to ELDEN RING's final area after months ("I don't remember anything"). | [0:10:11](https://youtu.be/ufbZgdek7XU?t=611) |

## Second model (whisper medium) on quoted lines

| First model (small) | At | Second model (medium), excerpt | Verdict |
|---|---|---|---|
| "まあそういうポンコツもあるよね" | [0:05:46](https://youtu.be/fhc67kDKU94?t=346) | "…なっちゃったまあそういうポコツもあるよ…" | **Not confirmed** by the second model; not quoted |
| "よしよしよしよし" | [0:07:59](https://youtu.be/fhc67kDKU94?t=479) | "…やつキター!よしよしよしよし原因…原因……" | **Shared span (computed):** whole line (kana/kanji folded) |
