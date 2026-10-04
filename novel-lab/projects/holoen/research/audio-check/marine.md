# Audio check — Houshou Marine (2026-10-02)

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
| drinkchat25_2026 | [宝鐘マリン、乱れる───【ホロライブ/宝鐘マリン】](https://youtu.be/H1Z96LzzG7k) | [0:05:00–0:30:00](https://youtu.be/H1Z96LzzG7k?t=300) | 20.9 | 7346 | 351.8 | 281 Hz | 194–450 Hz |
| drive25_2026 | [【Forza Horizon 6】船長とドライブしましょ～～～～ん♡♡♡【ホロライブ/宝鐘マリン](https://youtu.be/aHis7-TfsJY) | [0:05:00–0:30:00](https://youtu.be/aHis7-TfsJY?t=300) | 16.2 | 5085 | 314.5 | 279 Hz | 150–476 Hz |

"Characters/min of speech" = transcribed kana and kanji (punctuation dropped) ÷ minutes inside whisper's speech segments; it is a rough pace index for comparing windows, not a mora count.

## Marker counts (first model)

| Marker | drinkchat25_2026 | drive25_2026 |
|---|---|---|
| first person 私 | 0 | 3 |
| なんか | 57 | 8 |
| まあ | 8 | 2 |
| ちょっと待って | 4 | 10 |
| やばい | 3 | 11 |
| かわいい | 2 | 0 |
| えっ/え? | 5 | 12 |
| laugh (はは/ふふ/笑) | 3 | 0 |
| swear (くそ/ふざけ/殺) | 4 | 1 |
| ありがとう | 1 | 2 |
| English (Latin letters) | 2 | 16 |

## Claims checked

| Claim in the file | Result (in the machine transcript) | Evidence (ASR, archived audio) |
|---|---|---|
| Panics loudly at anything sudden | **Observed**: 「待って待って待って待って」 and 「一回落ち着こうよ」 ("let's calm down for a sec") in a 2026 racing game. | [0:05:28](https://youtu.be/aHis7-TfsJY?t=328), [0:05:41](https://youtu.be/aHis7-TfsJY?t=341) |
| Talks back at the game in a rough, comic register | **Observed**: 「馬鹿言ってるんじゃねぇや」 ("don't talk nonsense!"). | [0:06:43](https://youtu.be/aHis7-TfsJY?t=403) |
| Refers to herself as "Senchō" | **Observed**: 「船長」 in both windows. | [0:17:17](https://youtu.be/aHis7-TfsJY?t=1037) |
| Very fast commentary | **Observed**: about 315 characters a minute of speech in the racing window (a rough index; game sound mixed in). | — |

## Second model (whisper medium) on quoted lines

| First model (small) | At | Second model (medium), excerpt | Verdict |
|---|---|---|---|
| "待って待って待って待って" | [0:05:28](https://youtu.be/aHis7-TfsJY?t=328) | "…開?ちょっと待って待て説明がない…" | **Not confirmed** by the second model; not quoted |
| "一回落ち着こうよ" | [0:05:41](https://youtu.be/aHis7-TfsJY?t=341) | "…回落ち着こう一回落ち着こうよね、だいたい…" | **Shared span (computed):** whole line (kana/kanji folded) |
| "馬鹿言ってるんじゃねぇや" | [0:06:43](https://youtu.be/aHis7-TfsJY?t=403) | "…!バカ言ってんじゃねーよ!ウィン…" | **Not confirmed** by the second model; not quoted |
| "それでは行きますよー出航ー" | [3:39:54](https://youtu.be/aHis7-TfsJY?t=13194) | "…それでは行きますよー!しゅっこー!" | **Shared span (hand-checked):** whole line; 出航 and しゅっこー are the same reading (しゅっこう). Her sign-off, at the end of the stream (quotation pass, Claude, 2026-10-04) |
| "しゅっこ!" | [1:46:52](https://youtu.be/H1Z96LzzG7k?t=6412) | "…それでは行きますよ…出航!" | **Shared span (hand-checked):** the sign-off word (the first model drops the final long vowel); a second stream (quotation pass, Claude, 2026-10-04) |
