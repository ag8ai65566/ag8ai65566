# Audio check — Sakamata Chloe (2026-10-02)

Method: windows from the public stream archive archive.ragtag.moe (YouTube blocks this environment),
transcribed in Japanese with faster-whisper small (multilingual), pitch measured with Praat (100–600 Hz, speech
segments only). Tools and limits: `novel-lab/tools/audiocheck/README.md`. **This is not a listening check**: the
audio was machine-transcribed and acoustically measured, and the transcripts were reviewed in context. Lines used
on the character card were re-transcribed by a second model (whisper medium, multilingual) and compared after
folding katakana to hiragana and dropping punctuation (see the end of this file). Transcription does not write
laughs reliably, and Japanese ASR often picks different kanji or kana for the same word; only spans both models
render identically are quoted. Measurements describe the sampled recording and ASR segmentation; game audio,
music and other voices prevent treating them as isolated vocal measurements.

All windows are from 2024, her last full year of regular activities (she concluded them on 2025-01-26). Only in-scope public performance material is used: personal remarks in the chats
are not quoted or summarized here.

## Windows measured

| Window | Stream | Segment | Speech (min) | Characters | Characters/min of speech | F0 median | F0 p10–p90 |
|---|---|---|---|---|---|---|---|
| chat25_2024 | [【 雑談 】ねぇねぇおはなししよ【ホロライブ/沙花叉クロヱ】](https://youtu.be/Myw1OMa2wvQ) | [0:05:00–0:30:00](https://youtu.be/Myw1OMa2wvQ?t=300) | 19.3 | 5972 | 309.4 | 301 Hz | 217–482 Hz |
| sandtrix20_2024 | [【 Sandtrix+ 】最近流行りの砂テトリス！いっしょに20万点めざそ！【ホロライブ/沙花叉](https://youtu.be/p-5eLuQw6C0) | [0:10:00–0:30:00](https://youtu.be/p-5eLuQw6C0?t=600) | 15.2 | 4152 | 273.9 | 302 Hz | 124–478 Hz |

"Characters/min of speech" = transcribed kana and kanji (punctuation dropped) ÷ minutes inside whisper's speech segments; it is a rough pace index for comparing windows, not a mora count.

## Marker counts (first model)

| Marker | chat25_2024 | sandtrix20_2024 |
|---|---|---|
| first person 私 | 1 | 0 |
| なんか | 81 | 52 |
| まあ | 10 | 5 |
| ちょっと待って | 0 | 1 |
| やばい | 2 | 15 |
| かわいい | 4 | 0 |
| えっ/え? | 3 | 1 |
| laugh (はは/ふふ/笑) | 5 | 1 |
| swear (くそ/ふざけ/殺) | 1 | 0 |
| English (Latin letters) | 7 | 10 |

## Claims checked

| Claim in the file | Result (in the machine transcript) | Evidence (ASR, archived audio) |
|---|---|---|
| Opens a stream like a meal | **Observed**: 「いただきまーす」 ("itadakimāsu") near the start of the 2024 chat. | [0:05:49](https://youtu.be/Myw1OMa2wvQ?t=349) |
| Refers to herself as "Sakamata" | **Observed**; the first model renders it in several ways (e.g. 「坂本」), so no line with it is quoted. | [0:10:08](https://youtu.be/Myw1OMa2wvQ?t=608) |
| Turns a stray question into a poll of chat | **Observed**: asks chat when an "ojisan" becomes an "ojisan" and runs a show of hands. | [0:07:32](https://youtu.be/Myw1OMa2wvQ?t=452) |
| Drawn-out "~sā" sentence endings | **Observed**: 「ずっとさー」 … 「めっちゃ緊張してさー」 in the opening. | [0:05:59](https://youtu.be/Myw1OMa2wvQ?t=359) |
| Fast, soft chatter | **Not established**: ASR records connected chatter; the character-rate measurement (about 309 characters a minute, a rough index) does not establish perceived speed, softness or timbre, which stay provisional (run F review, 2026-10-03). | — |

## Second model (whisper medium) on quoted lines

| First model (small) | At | Second model (medium), excerpt | Verdict |
|---|---|---|---|
| "おじさんっていつからおじさんなの" | [0:07:33](https://youtu.be/Myw1OMa2wvQ?t=453) | "…じさんってさいつからおじさんなの?自分でさあ…" | **Partial (computed):** shared run "いつからおじさんなの"; only that part is quoted |
| "いただきまーす" | [0:05:49](https://youtu.be/Myw1OMa2wvQ?t=349) | "…はこれです!いただきまーす!キノコ生え…" | **Shared span (computed):** whole line (kana/kanji folded) |
