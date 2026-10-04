# Audio check — Hakui Koyori (2026-10-02)

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
| goemon20_2026 | [【がんばれゴエモン大集合！】SFC「がんばれゴエモン3 獅子重禄兵衛のからくり卍固め」完全初見！](https://youtu.be/PN2i1U-MDIE) | [0:10:00–0:30:00](https://youtu.be/PN2i1U-MDIE?t=600) | 14.6 | 3593 | 245.9 | 304 Hz | 204–506 Hz |
| asakoyo20_2026 | [【 #朝こよ 】あと10回で300回！？火曜日の朝は朝こよ！☀ #290 【博衣こより/holo](https://youtu.be/ogC6DbQJpJQ) | [0:03:00–0:23:00](https://youtu.be/ogC6DbQJpJQ?t=180) | 15.6 | 3895 | 250.3 | 263 Hz | 202–433 Hz |

"Characters/min of speech" = transcribed kana and kanji (punctuation dropped) ÷ minutes inside whisper's speech segments; it is a rough pace index for comparing windows, not a mora count.

## Marker counts (first model)

| Marker | goemon20_2026 | asakoyo20_2026 |
|---|---|---|
| なんか | 4 | 7 |
| まあ | 2 | 3 |
| ちょっと待って | 1 | 0 |
| やばい | 2 | 0 |
| えっ/え? | 6 | 0 |
| laugh (はは/ふふ/笑) | 3 | 2 |
| swear (くそ/ふざけ/殺) | 1 | 0 |
| ありがとう | 2 | 2 |
| こんなきり/こんにちは | 1 | 0 |

## Claims checked

| Claim in the file | Result (in the machine transcript) | Evidence (ASR, archived audio) |
|---|---|---|
| AsaKoyo is a news show built on corners | **Observed**: news items, a "hololive quote of the month" corner and viewer questions, introduced with 「それでは続いてはこちら」 ("and next up"). | [0:07:18](https://youtu.be/ogC6DbQJpJQ?t=438), [0:19:41](https://youtu.be/ogC6DbQJpJQ?t=1181) |
| Refers to herself as "Koyori-chan" | **Observed**: 「こよりちゃんでございます」 in the opening. | [0:05:24](https://youtu.be/ogC6DbQJpJQ?t=324) |
| Calls viewers "joshu-kun" (Assistants) | **Observed**; the first model writes it 「女子君」. Not quoted. | [0:07:49](https://youtu.be/ogC6DbQJpJQ?t=469) |
| Writes a monthly game column for Weekly Famitsu (first anniversary in July 2026) | **Her account** on the show; the column title is garbled by the model and not confirmed. | [0:14:55](https://youtu.be/ogC6DbQJpJQ?t=895) |
| Voices the fan-born mascot Mofukoyo and promotes its shorts | **Observed**: a new Mofukoyo short introduced on the show. | [0:17:06](https://youtu.be/ogC6DbQJpJQ?t=1026) |
| Bubbly giggle | **Observed** once as 「うふふふふふ」; transcription does not capture laughter reliably. | [0:05:01](https://youtu.be/ogC6DbQJpJQ?t=301) |

## Second model (whisper medium) on quoted lines

| First model (small) | At | Second model (medium), excerpt | Verdict |
|---|---|---|---|
| "それでは続いてはこちら" | [0:07:18](https://youtu.be/ogC6DbQJpJQ?t=438) | "…ておりますよそれでは続いてはこちらホロドリーコ…" | **Shared span (computed):** whole line (kana/kanji folded) |
| "こよりちゃんでございます" | [0:05:24](https://youtu.be/ogC6DbQJpJQ?t=324) | "…コヨリちゃんでございますはいほな今日…" | **Shared span (computed):** whole line (kana/kanji folded) |
| "ぜひぜひ見てみてください" | [0:19:15](https://youtu.be/ogC6DbQJpJQ?t=1155) | "…きますので ぜひぜひ見てみてくださいあーまあスマ…" | **Shared span (computed):** whole line (kana/kanji folded) |
