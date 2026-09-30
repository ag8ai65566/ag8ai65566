# Audio check — Ninomae Ina'nis (2026-09-30)

Method: short windows from the public stream archive archive.ragtag.moe (YouTube blocks this
environment), transcribed with faster-whisper small.en, pitch measured with Praat (100–600 Hz, word
intervals only). Tools and limits: `novel-lab/tools/audiocheck/README.md`. Machine transcription, read
in context; it drops some fillers and does not write "WAH" reliably or non-speech sounds. The 2026 chat
stream (we8TkYC7__0) is the same stream Claude's earlier caption study (I3) used, so this is an audio
cross-check of those caption quotes.

## Windows measured

| Window | Stream | Segment | Speech (min) | Words | Words/min of speech | F0 median | F0 p10–p90 |
|---|---|---|---|---|---|---|---|
| tomorrow | [Nintendo Direct Feb 2022 Watchalong! ※Not a Mirr](https://youtu.be/EHpxi7khHb0) | [0:49:00–0:51:30](https://youtu.be/EHpxi7khHb0?t=2940) | 1.5 | 68 | 45.7 | 244 Hz | 179–397 Hz |
| chat30 | [【CHAT】Chill Chatting......Eepy....](https://youtu.be/we8TkYC7__0) | [0:30:00–1:00:00](https://youtu.be/we8TkYC7__0?t=1800) | 24.7 | 1999 | 81.0 | 230 Hz | 143–363 Hz |
| close | [【CHAT】Chill Chatting......Eepy....](https://youtu.be/we8TkYC7__0) | [1:26:14–1:38:14](https://youtu.be/we8TkYC7__0?t=5174) | 9.2 | 766 | 82.9 | 232 Hz | 139–365 Hz |
| open | [【CHAT】Chill Chatting......Eepy....](https://youtu.be/we8TkYC7__0) | [0:00:00–0:15:00](https://youtu.be/we8TkYC7__0?t=0) | 10.4 | 990 | 95.0 | 223 Hz | 149–363 Hz |

## Claims checked

| Claim in the file | Result | Evidence (audio) |
|---|---|---|
| Opening: "Good morning, afternoon, evening, everyone." → "Could this be Tako time?" → "It is indeed Tako time." | **Confirmed** (whisper spells it "taco time"). The caption quote was right. | [0:02:43](https://youtu.be/we8TkYC7__0?t=163), "it is indeed taco time" [0:03:03](https://youtu.be/we8TkYC7__0?t=183) |
| Sign-off: "have a wonderful rest of the morning, afternoon, evening… until next time" with "We'll see." | **Confirmed.** | "Anyways, I do have to start getting ready soon." [1:35:17](https://youtu.be/we8TkYC7__0?t=5717); "have a wonderful rest of the morning afternoon evening" [1:36:42](https://youtu.be/we8TkYC7__0?t=5802); "we'll see… anyway thank you until next time" [1:37:06](https://youtu.be/we8TkYC7__0?t=5826) |
| "I'm still in my jammies right now. I literally woke up and turned on stream." (caption quote) | **Confirmed verbatim.** | [1:35:26](https://youtu.be/we8TkYC7__0?t=5726) |
| "like" as a constant hedge (about 1 in 33 words from captions) | **Consistent.** 103 hits in about 3,700 transcribed words (1 in 36); whisper tends to drop fillers, so this is a floor. "I think" about 20 times an hour. | chat windows |
| "TOMORROW?!" at the 2022 Nintendo Direct (locator 50:05) | **Confirmed as a moment**: an "Oh" at 50:09, an outburst whisper does not transcribe, then her apology. | "Sorry, I got a little excited there" [0:50:27](https://youtu.be/EHpxi7khHb0?t=3027) |
| Silly epithets on her own name ("Hell Flame Ninomae Ina'nis") | **Confirmed in context** (playing with a chat suggestion). | "Can I also be hell flame nino-…" [0:40:00](https://youtu.be/we8TkYC7__0?t=2400); "I should call this outfit the hell flame outfit" [0:40:12](https://youtu.be/we8TkYC7__0?t=2412) |
| Profanity near zero | **Consistent.** No swearing in her own words in these windows (the only "hell" hits are "Hell Flame"). | — |
| Soft, unhurried voice | **Confirmed, relative.** The slowest speaker of the six (81–95 words per minute of speech); median F0 223–232 Hz, in the middle of the group (Kronii 177–188, Gura and Ame about 250–270). "Mid-to-low" is therefore too low; "mid" fits. | table above |

## New material (audio-verified short lines)

- "I literally woke up and turned on stream." [1:35:30](https://youtu.be/we8TkYC7__0?t=5730)
- "Anyways, I do have to start getting ready soon." [1:35:17](https://youtu.be/we8TkYC7__0?t=5717)
- "Sorry, I got a little excited there" (after the Nintendo Direct outburst) [0:50:27](https://youtu.be/EHpxi7khHb0?t=3027)
