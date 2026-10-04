# Audio check — Takane Lui (2026-10-02)

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
| mother20_2026 | [【 MOTHER2 】完全初見！砂漠を進んでフォーサイドへ・・・！【鷹嶺ルイ/ホロライブ】](https://youtu.be/gN91npViT-k) | [0:10:00–0:30:00](https://youtu.be/gN91npViT-k?t=600) | 9.8 | 1657 | 168.6 | 213 Hz | 132–502 Hz |
| hirukatsu25_2026 | [2026 public chat — Takane Lui](https://youtu.be/wOHSGHgT5Aw) | [0:05:00–0:30:00](https://youtu.be/wOHSGHgT5Aw?t=300) | 13.7 | 3232 | 236.7 | 190 Hz | 137–293 Hz |

"Characters/min of speech" = transcribed kana and kanji (punctuation dropped) ÷ minutes inside whisper's speech segments; it is a rough pace index for comparing windows, not a mora count.

## Marker counts (first model)

| Marker | mother20_2026 | hirukatsu25_2026 |
|---|---|---|
| first person 僕 (boku) | 2 | 1 |
| first person 私 | 3 | 6 |
| なんか | 8 | 10 |
| まあ | 3 | 16 |
| ちょっと待って | 0 | 5 |
| かわいい | 1 | 0 |
| laugh (はは/ふふ/笑) | 2 | 0 |
| swear (くそ/ふざけ/殺) | 1 | 0 |
| ありがとう | 0 | 2 |

## Claims checked

| Claim in the file | Result (in the machine transcript) | Evidence (ASR, archived audio) |
|---|---|---|
| Calm, reassuring with chat | **Observed**: 「まあ誰にだってトラブルやミスはあるからね」 ("well, everyone has trouble and mistakes"). | [0:05:39](https://youtu.be/wOHSGHgT5Aw?t=339) |
| Possible address term in the Nintendo Direct discussion | **Unverified**: the first-model rendering does not establish who addresses whom; no approved two-model quotation span is available for this term. | [0:09:15](https://youtu.be/wOHSGHgT5Aw?t=555) |
| Answers chat one comment at a time | **Observed** in the 2026 midday chat. | [0:10:27](https://youtu.be/wOHSGHgT5Aw?t=627) |
| Saturday RPG streams (MOTHER 2, 2026) | **Observed**: a first playthrough, reacting to each new area. | [0:10:26](https://youtu.be/gN91npViT-k?t=626) |
| Easy laughter, rare profanity | **Undetermined**: one automatic swear-pattern match occurred in the game window and its meaning was not validated; overall profanity habits remain undetermined; laughter is not reliably transcribed (run E review, 2026-10-03). | — |

## Second model (whisper medium) on quoted lines

| First model (small) | At | Second model (medium), excerpt | Verdict |
|---|---|---|---|
| "まあ誰にだってトラブルやミスはあるからね" | [0:05:39](https://youtu.be/wOHSGHgT5Aw?t=339) | "まあ 誰にだってトラブルやミスはあるからね対応力が上が…" | **Shared span (computed):** whole line (kana/kanji folded) |
| "ニワカでやるのありだな" | [0:18:44](https://youtu.be/wOHSGHgT5Aw?t=1124) | "…があるやニアカでやるのありだなうんまずニア…" | **Partial (computed):** shared run "かでやるのありだな"; only that part is quoted |
