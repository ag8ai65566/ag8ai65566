# Audio check — Kikirara Vivi (2026-10-02)

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
| mario20_2026 | [【 スーパーマリオワールド 】真最終回！完全初見！初めてのマリオワールドに挑戦！【#綺々羅々ヴィ](https://youtu.be/p10HUmvmrfc) | [0:10:00–0:30:00](https://youtu.be/p10HUmvmrfc?t=600) | 11.6 | 1873 | 162.0 | 351 Hz | 158–509 Hz |
| call20_2026 | [ヴィヴィから着信📞Vivi Ch. 綺々羅々ヴィヴィ - FLOW GLOW がライブ配信中！](https://youtu.be/zEmPFayNEFo) | [0:05:00–0:25:00](https://youtu.be/zEmPFayNEFo?t=300) | 14.0 | 3592 | 257.1 | 275 Hz | 222–406 Hz |

"Characters/min of speech" = transcribed kana and kanji (punctuation dropped) ÷ minutes inside whisper's speech segments; it is a rough pace index for comparing windows, not a mora count.

## Marker counts (first model)

| Marker | mario20_2026 | call20_2026 |
|---|---|---|
| first person 余 (yo) | 1 | 0 |
| first person 僕 (boku) | 0 | 2 |
| なんか | 3 | 18 |
| まあ | 3 | 0 |
| ちょっと待って | 1 | 1 |
| やばい | 1 | 0 |
| かわいい | 0 | 1 |
| えっ/え? | 2 | 1 |
| ありがとう | 1 | 6 |
| English (Latin letters) | 1 | 3 |

## Claims checked

| Claim in the file | Result (in the machine transcript) | Evidence (ASR, archived audio) |
|---|---|---|
| Third-person "Vivi" | **Observed** constantly (dozens of times in the late-night window). | [0:06:25](https://youtu.be/zEmPFayNEFo?t=385) |
| Deadpan "Ōi!" on purpose | **Observed**: she explains that when she retorts "ōi" she deliberately strips the emotion out, then performs an "emotional version." The models disagree on the exact words, so the explanation is paraphrased. | [0:18:22](https://youtu.be/zEmPFayNEFo?t=1102), [0:19:13](https://youtu.be/zEmPFayNEFo?t=1153) |
| "I'll charge you for that" joke | **Observed**: 「お金取るで」 when chat asks for something sweet (second model writes 「とる」; same reading). | [0:07:04](https://youtu.be/zEmPFayNEFo?t=424) |
| Kansai-style speech | **Observed**: "~yan," "~nen," "akan," "honma," "~hen" throughout. | [0:05:00](https://youtu.be/zEmPFayNEFo?t=300) |
| A game beginner on Mario | **Observed** in her 2026 Super Mario World finale. | [0:10:20](https://youtu.be/p10HUmvmrfc?t=620) |

## Second model (whisper medium) on quoted lines

| First model (small) | At | Second model (medium), excerpt | Verdict |
|---|---|---|---|
| "お金取るで" | [0:07:04](https://youtu.be/zEmPFayNEFo?t=424) | "…いもちもちはお金とるでもちも…" | **Shared span (computed):** whole line (same reading; the models spell a word differently) |
| "誰がぼう読みや" | [0:18:06](https://youtu.be/zEmPFayNEFo?t=1086) | "…ーえ?暴読?誰が暴読や誰が暴…" | **Not confirmed** by the second model; not quoted |
| "感情抜いてます" | [0:18:22](https://youtu.be/zEmPFayNEFo?t=1102) | "…とさあ感情を抜いてますこれわかる?…" | **Partial (computed):** shared run "抜いてます"; only that part is quoted |
