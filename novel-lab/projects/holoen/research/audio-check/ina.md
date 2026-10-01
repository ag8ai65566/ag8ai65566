# Audio check — Ninomae Ina'nis (2026-09-30)

Method: short windows from the public stream archive archive.ragtag.moe (YouTube blocks this
environment), transcribed with faster-whisper small.en, pitch measured with Praat (100–600 Hz, word
intervals only). Tools and limits: `novel-lab/tools/audiocheck/README.md`. **This is not a listening check**: the audio was
machine-transcribed and acoustically measured, and the transcripts were reviewed in context. Lines used on
the character card were re-transcribed by a second model (whisper medium.en) and compared (see the end of
this file). Machine transcription, read
in context; it drops some fillers and does not write "WAH" reliably or non-speech sounds. The 2026 chat
stream (we8TkYC7__0) is the same stream Claude's earlier caption study (I3) used, so this is an audio
cross-check of those caption quotes.

## Windows measured

| Window | Stream | Segment | Speech (min) | Words | Words/min of speech | F0 median | F0 p10–p90 |
|---|---|---|---|---|---|---|---|
| el3_close | [【Ender Lilies】 Thrice Upon a Tako 【#3】](https://youtu.be/4k_oLA5zeaI) | [4:01:05–4:41:05](https://youtu.be/4k_oLA5zeaI?t=14465) | 28.3 | 1920 | 67.9 | 214 Hz | 112–343 Hz |
| el3_open | [【Ender Lilies】 Thrice Upon a Tako 【#3】](https://youtu.be/4k_oLA5zeaI) | [0:00:00–0:30:00](https://youtu.be/4k_oLA5zeaI?t=0) | 20.1 | 2330 | 115.9 | 210 Hz | 113–344 Hz |
| tomorrow | [Nintendo Direct Feb 2022 Watchalong! ※Not a Mirr](https://youtu.be/EHpxi7khHb0) | [0:49:00–0:51:30](https://youtu.be/EHpxi7khHb0?t=2940) | 1.5 | 68 | 45.7 | 244 Hz | 179–397 Hz |
| chat30 | [【CHAT】Chill Chatting......Eepy....](https://youtu.be/we8TkYC7__0) | [0:30:00–1:00:00](https://youtu.be/we8TkYC7__0?t=1800) | 24.7 | 1999 | 81.0 | 230 Hz | 143–363 Hz |
| close | [【CHAT】Chill Chatting......Eepy....](https://youtu.be/we8TkYC7__0) | [1:26:14–1:38:14](https://youtu.be/we8TkYC7__0?t=5174) | 9.2 | 766 | 82.9 | 232 Hz | 139–365 Hz |
| open | [【CHAT】Chill Chatting......Eepy....](https://youtu.be/we8TkYC7__0) | [0:00:00–0:15:00](https://youtu.be/we8TkYC7__0?t=0) | 10.4 | 990 | 95.0 | 223 Hz | 149–363 Hz |

## Claims checked

| Claim in the file | Result (in the machine transcript) | Evidence (ASR, archived audio) |
|---|---|---|
| Opening: "Good morning, afternoon, evening, everyone." → "Could this be Tako time?" → "It is indeed Tako time." | **Confirmed** (whisper spells it "taco time"). The caption quote was right. | [0:02:43](https://youtu.be/we8TkYC7__0?t=163), "it is indeed taco time" [0:03:03](https://youtu.be/we8TkYC7__0?t=183) |
| Sign-off: "have a wonderful rest of the morning, afternoon, evening… until next time" with "We'll see." | **Confirmed.** | "Anyways, I do have to start getting ready soon." [1:35:17](https://youtu.be/we8TkYC7__0?t=5717); "have a wonderful rest of the morning afternoon evening" [1:36:42](https://youtu.be/we8TkYC7__0?t=5802); "we'll see… anyway thank you until next time" [1:37:06](https://youtu.be/we8TkYC7__0?t=5826) |
| [a private-routine line; redacted 2026-10-01 and not used on the card] | **Confirmed verbatim.** | [1:35:26](https://youtu.be/we8TkYC7__0?t=5726) |
| "like" as a constant hedge (about 1 in 33 words from captions) | **Consistent.** 103 hits in about 3,700 transcribed words (1 in 36); whisper tends to drop fillers, so this is a floor. "I think" about 20 times an hour. | chat windows |
| "TOMORROW?!" at the 2022 Nintendo Direct (locator 50:05) | **Confirmed as a moment**: an "Oh" at 50:09, an outburst whisper does not transcribe, then her apology. | "Sorry, I got a little excited there" [0:50:27](https://youtu.be/EHpxi7khHb0?t=3027) |
| Silly epithets on her own name ("Hell Flame Ninomae Ina'nis") | **Confirmed in context** (playing with a chat suggestion). | "Can I also be hell flame nino-…" [0:40:00](https://youtu.be/we8TkYC7__0?t=2400); "I should call this outfit the hell flame outfit" [0:40:12](https://youtu.be/we8TkYC7__0?t=2412) |
| Forbidden WAH (wiki I2 §WAH; *Ender Lilies* #3, 2021) | **Confirmed as a bit.** Going through the WAH acronyms chat made ("We're happy… We're hype, we're here"), she says someone added "a fourth… with a different caption, and… that's the forbidden wah. We don't say that in public." The first model hears "the forbidden wah", the second "the forbidden one"; "We don't say that in public" agrees in both. | [0:04:50](https://youtu.be/4k_oLA5zeaI?t=290) |
| Profanity near zero | **Consistent.** No swearing in her own words in these windows, including the 2021 game stream (the only "hell" hits are "Hell Flame"). | — |
| Soft, unhurried voice | **Confirmed, relative.** In the 2026 chat windows the slowest speaker of the six (81–95 words per minute of speech); a 2021 game stream measures 68–116 (its opening chat 116, close to Kronii and Ame). Median F0 223–232 Hz in the chat windows and 210–214 Hz in the 2021 game stream (game narration mixes in), in the middle of the group (Kronii 177–188, Gura and Ame about 250–270). "Mid-to-low" is therefore too low; "mid" fits. | table above |

## New material (ASR-transcribed short lines)

Lines not listed in the second-model check at the end of this file are first-model transcriptions only.

- "Anyways, I do have to start getting ready soon." [1:35:17](https://youtu.be/we8TkYC7__0?t=5717)
- "Sorry, I got a little excited there" (after the Nintendo Direct outburst) [0:50:27](https://youtu.be/EHpxi7khHb0?t=3027)

## Second-model check (whisper medium.en)

Each line below was cut from the archived audio (a window of about 24–60 s around the first model's
timestamp) and transcribed again by a larger model. "Agrees" means the second model produced the same
words; it is still machine transcription, not listening. Lines that did not agree were removed from
the character card.

| First model (small.en) | Link | Second model (medium.en), excerpt | Verdict |
|---|---|---|---|
| "a fourth wah with a different caption and that's the forbidden wah. We don't say that in public." | [0:04:52](https://youtu.be/4k_oLA5zeaI?t=292) | "a separate... Separate... A fourth... Fourth... With a different caption, and... That's the forbidden one. We don't say that in public. We are whole..." | **Agrees on the bit, not the word**: the second model hears "the forbidden one" where the first hears "the forbidden wah" |
| "Sorry, I got a little excited there" | [0:50:27](https://youtu.be/EHpxi7khHb0?t=3027) | "Sorry, I got a little excited there. Cute?" | Agrees |
| "good morning afternoon evening everyone could this be tako time" | [0:02:43](https://youtu.be/we8TkYC7__0?t=163) | "Good morning, afternoon, evening, everyone. Could this be taco time? How's everyone doing" | Agrees ("tako" written as "taco") |
| "it is indeed tako time" | [0:03:03](https://youtu.be/we8TkYC7__0?t=183) | "was sleep well? It is indeed taco time. Busy?" | Agrees ("tako" written as "taco") |
| "Anyways, I do have to start getting ready soon." | [1:35:17](https://youtu.be/we8TkYC7__0?t=5717) | "Anyways, I do have to start getting ready soon, but I'm still" | Agrees |
| [a private-routine line; redacted 2026-10-01 and not used on the card] | [1:35:26](https://youtu.be/we8TkYC7__0?t=5726) | (redacted) | Agrees |
| "have a wonderful rest of the morning afternoon evening" | [1:36:54](https://youtu.be/we8TkYC7__0?t=5814) | "Hope you guys have a wonderful rest of the morning, afternoon, evening. I'll see you" | Agrees |
