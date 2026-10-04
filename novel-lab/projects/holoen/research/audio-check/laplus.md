# Audio check — La+ Darknesss (2026-10-02)

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
| chat25_2026 | [【雑談】本当にいろいろあったから話そうぜ～～～～～＾＾【ラプラス・ダークネス/ホロライブ】](https://youtu.be/dBzPcy1DqzU) | [0:05:00–0:30:00](https://youtu.be/dBzPcy1DqzU?t=300) | 16.8 | 4141 | 246.6 | 276 Hz | 196–543 Hz |
| cheki20_2026 | [【新年】太客贔屓チェキ会配信【ラプラス・ダークネス/ホロライブ】](https://youtu.be/ebnfDlxLZug) | [0:10:00–0:30:00](https://youtu.be/ebnfDlxLZug?t=600) | 11.5 | 2708 | 235.2 | 287 Hz | 207–508 Hz |

"Characters/min of speech" = transcribed kana and kanji (punctuation dropped) ÷ minutes inside whisper's speech segments; it is a rough pace index for comparing windows, not a mora count.

## Marker counts (first model)

| Marker | chat25_2026 | cheki20_2026 |
|---|---|---|
| first person 私 | 9 | 1 |
| なんか | 25 | 18 |
| まあ | 6 | 2 |
| ちょっと待って | 4 | 2 |
| やばい | 7 | 4 |
| えっ/え? | 4 | 0 |
| laugh (はは/ふふ/笑) | 2 | 2 |
| swear (くそ/ふざけ/殺) | 2 | 1 |
| ありがとう | 1 | 5 |
| English (Latin letters) | 8 | 4 |
| こんなきり/こんにちは | 1 | 0 |

## Claims checked

| Claim in the file | Result (in the machine transcript) | Evidence (ASR, archived audio) |
|---|---|---|
| Speaks as a villain, "wagahai" for "I" (wiki) | **Not observed in 2026 windows**: in a May 2026 chat and a January 2026 fan-greeting stream she says 「私」 (watashi) in plain talk; "wagahai" is kept as her persona line from the wiki. | [0:06:08](https://youtu.be/dBzPcy1DqzU?t=368) |
| Casual, quick chat with chat | **Observed**: 「聞こえたっしょ?」 ("you heard it, right?") checking her audio; slangy "maji de," "yabai." | [0:06:55](https://youtu.be/dBzPcy1DqzU?t=415) |
| Turns her own setup into a bit | **Observed**: showing off her new streaming setup, 「これが配信者よ」 ("this is what a streamer is!"). | [0:19:15](https://youtu.be/dBzPcy1DqzU?t=1155) |
| Plays up being bad at sums | **Observed** (January 2026): she jokes she "really can't do arithmetic." | [0:12:48](https://youtu.be/ebnfDlxLZug?t=768) |

## Second model (whisper medium) on quoted lines

| First model (small) | At | Second model (medium), excerpt | Verdict |
|---|---|---|---|
| "聞こえたっしょ" | [0:06:55](https://youtu.be/dBzPcy1DqzU?t=415) | "…ん?これか?聞こえたっしょ聞こえたっし…" | **Shared span (computed):** whole line (kana/kanji folded) |
| "これが配信者よ" | [0:19:15](https://youtu.be/dBzPcy1DqzU?t=1155) | "どう?これが配信者よこれが配信者…" | **Shared span (computed):** whole line (kana/kanji folded) |
