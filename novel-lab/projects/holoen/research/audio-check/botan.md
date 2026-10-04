# Audio check — Shishiro Botan (2026-10-02)

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
| talk20_2026 | [【企画告知】そろそろみんなで稼ぎませんか💰【獅白ぼたん/ホロライブ】](https://youtu.be/9F8DKZa1L2s) | [0:03:00–0:23:00](https://youtu.be/9F8DKZa1L2s?t=180) | 16.9 | 6235 | 368.3 | 239 Hz | 178–402 Hz |
| forza20_2026 | [【Forza Horizon 6】アクセル全開が四駆の基本だ！【獅白ぼたん/ホロライブ】](https://youtu.be/MSPdwwejtXU) | [0:10:00–0:30:00](https://youtu.be/MSPdwwejtXU?t=600) | 11.2 | 3202 | 286.6 | 232 Hz | 157–385 Hz |

"Characters/min of speech" = transcribed kana and kanji (punctuation dropped) ÷ minutes inside whisper's speech segments; it is a rough pace index for comparing windows, not a mora count.

## Marker counts (first model)

| Marker | talk20_2026 | forza20_2026 |
|---|---|---|
| first person 私 | 5 | 6 |
| なんか | 0 | 7 |
| まあ | 13 | 2 |
| ちょっと待って | 3 | 3 |
| やばい | 0 | 3 |
| えっ/え? | 0 | 1 |
| laugh (はは/ふふ/笑) | 2 | 0 |
| ありがとう | 3 | 0 |
| English (Latin letters) | 4 | 10 |

## Claims checked

| Claim in the file | Result (in the machine transcript) | Evidence (ASR, archived audio) |
|---|---|---|
| Runs a server event as its game master | **Observed**: she announces "#ホロ金策サバイバル2" (June 1–5, 2026), with jobs (fighter, farmer, alchemist, gambler) and dungeons, designed so members who can join only one day can still enjoy it. | [0:06:03](https://youtu.be/9F8DKZa1L2s?t=363), [0:10:36](https://youtu.be/9F8DKZa1L2s?t=636), [0:11:54](https://youtu.be/9F8DKZa1L2s?t=714) |
| Presents in an organized, fast register | **Observed**: numbered points, "this part turns into explanation mode, bear with me"; about 368 characters a minute of speech (a rough index). | [0:07:25](https://youtu.be/9F8DKZa1L2s?t=445) |
| Looks back on last year's event | **Observed**: 「前回はですねペコちゃんが優勝しました」 ("last time, Peko-chan won") and 「あれから1年経ってるっていうのがすごいね」. | [0:09:05](https://youtu.be/9F8DKZa1L2s?t=545), [0:09:49](https://youtu.be/9F8DKZa1L2s?t=589) |
| Refers to herself as "Shishiro" | **Observed** (「シシロ」). | [0:03:26](https://youtu.be/9F8DKZa1L2s?t=206) |
| Calm through intense play | **Observed** in a 2026 racing game. | [0:15:00](https://youtu.be/MSPdwwejtXU?t=900) |

## Second model (whisper medium) on quoted lines

| First model (small) | At | Second model (medium), excerpt | Verdict |
|---|---|---|---|
| "前回はですねペコちゃんが優勝しました" | [0:09:05](https://youtu.be/9F8DKZa1L2s?t=545) | "…とではい で前回はですねぺこちゃんが優勝しましためちゃ一番稼…" | **Shared span (computed):** whole line (kana/kanji folded) |
| "あれから1年経ってるっていうのがすごいね" | [0:09:49](https://youtu.be/9F8DKZa1L2s?t=589) | "…経っ て いる って いう の が すごい ねちょっと さ…" | **Partial (computed):** shared run "るっていうのがすごいね"; only that part is quoted |
