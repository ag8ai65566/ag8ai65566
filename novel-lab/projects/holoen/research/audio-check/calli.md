# Audio check — Mori Calliope (2026-09-30)

Method: short windows from the public stream archive archive.ragtag.moe (YouTube blocks this
environment), transcribed with faster-whisper small.en, pitch measured with Praat (100–600 Hz, word
intervals only). Tools and limits: `novel-lab/tools/audiocheck/README.md`. **This is not a listening check**: the audio was
machine-transcribed and acoustically measured, and the transcripts were reviewed in context. Lines used on
the character card were re-transcribed by a second model (whisper medium.en) and compared (see the end of
this file). Machine transcription, read
in context; it drops some fillers and does not write non-speech sounds (so "Guh" cannot be checked this
way). In Fields of Mistria she also reads NPC dialogue aloud; only lines that are clearly her own
reactions are quoted.

## Windows measured

| Window | Stream | Segment | Speech (min) | Words | Words/min of speech | F0 median | F0 p10–p90 |
|---|---|---|---|---|---|---|---|
| chat45 | [【Fields of Mistria】checking in to show off my si](https://youtu.be/76-YKpxYL4g) | [1:00:00–1:45:00](https://youtu.be/76-YKpxYL4g?t=3600) | 34.3 | 5540 | 161.3 | 214 Hz | 144–325 Hz |
| close | [【Fields of Mistria】checking in to show off my si](https://youtu.be/76-YKpxYL4g) | [4:35:17–4:47:17](https://youtu.be/76-YKpxYL4g?t=16517) | 9.1 | 1688 | 186.5 | 205 Hz | 109–321 Hz |
| open | [【Fields of Mistria】checking in to show off my si](https://youtu.be/76-YKpxYL4g) | [0:00:00–0:15:00](https://youtu.be/76-YKpxYL4g?t=0) | 8.8 | 1540 | 174.1 | 197 Hz | 109–331 Hz |
| game45 | [【Pragmata】you're my dad! boogie woogie woogie (p](https://youtu.be/y0WsNvXOdns) | [1:30:00–2:15:00](https://youtu.be/y0WsNvXOdns?t=5400) | 34.1 | 4522 | 132.7 | 225 Hz | 162–364 Hz |

## Claims checked

| Claim in the file | Result (in the machine transcript) | Evidence (ASR, archived audio) |
|---|---|---|
| Swearing "in bursts at the breaking point" | **Revised: she swears casually in ordinary talk too.** About 16 hits in 2 hours (mostly "shit"), in calm farming and in a platformer, not only at breaking points. | "Feel like I just have a bunch of shit in my yard" [1:30:20](https://youtu.be/76-YKpxYL4g?t=5420); "kids love doing this shit" [1:32:30](https://youtu.be/y0WsNvXOdns?t=5550); "Let's try this shit." [1:58:57](https://youtu.be/y0WsNvXOdns?t=7137) |
| Calls fans Dead Beats | **Confirmed**, about 5.6 times an hour. | "That's the big scary question dead beats." [1:05:15](https://youtu.be/76-YKpxYL4g?t=3915); "Oh, I don't know, Deadbeats." [1:43:53](https://youtu.be/76-YKpxYL4g?t=6233) |
| "Big ups!" as thanks | **Confirmed** (superchat thanks). | "big ups to…" [4:42:38](https://youtu.be/76-YKpxYL4g?t=16958), [4:44:30](https://youtu.be/76-YKpxYL4g?t=17070) |
| Greeting "What's up, Dead Beats?!" | **Not detected in this stream's transcript.** She opened by settling in instead. The greeting stays sourced to the official interview (C11). | "I'm here I got my yum-yum drink" [0:05:08](https://youtu.be/76-YKpxYL4g?t=308) |
| Sign-off "I'm your Mori…" / "PEACE." | **Not detected in this stream's transcript.** The sign-off observed was a casual one. The sourced variants stay (C3, C11); the observed one is added. | "I'll catch you guys on the flip side" [4:45:37](https://youtu.be/76-YKpxYL4g?t=17137); "I guess I'm out of here. All right, take care everybody. I'll see you soon. Goodbye" [4:46:24](https://youtu.be/76-YKpxYL4g?t=17184) |
| "Listen," "whatever, man," "your boy" | **Not detected in these 2 hours of transcripts.** They stay sourced to the wiki quote list; the sample says they are not constant. | — |
| "A low speaking voice" | **Confirmed, relative.** Second-lowest median F0 of the six files (chat 197–214 Hz; Kronii 177–188 Hz; Gura and Ame about 250–270 Hz). The wiki's "one of the lowest in hololive" was not measured against hololive as a whole. | table above |
| Pace | **New: the fastest talker of the six.** About 161–186 words per minute of speech while chatting (Kronii 120–127, Ina 81–95). | table above |

## New material (ASR-transcribed short lines)

Lines not listed in the second-model check at the end of this file are first-model transcriptions only.

- Settling in: "I'm here I got my yum-yum drink" [0:05:08](https://youtu.be/76-YKpxYL4g?t=308); "I'm really just not
  very organized. I'm gonna be honest with you guys" [0:05:25](https://youtu.be/76-YKpxYL4g?t=325)
- Irritation: "Oh my god. I'm gonna lose it. What an annoying guy." [1:02:20](https://youtu.be/76-YKpxYL4g?t=3740)
- Sign-off: "I'll catch you guys on the flip side" … "I guess I'm out of here. All right, take care everybody.
  I'll see you soon. Goodbye"

## Second-model check (whisper medium.en)

Each line below was cut from the archived audio (a window of about 24–60 s around the first model's
timestamp) and transcribed again by a larger model. "Agrees" means the second model produced the same
words; it is still machine transcription, not listening. Lines that did not agree were removed from
the character card.

| First model (small.en) | Link | Second model (medium.en), excerpt | Verdict |
|---|---|---|---|
| "I'm here I got my yum-yum drink" | [0:05:08](https://youtu.be/76-YKpxYL4g?t=308) | "I'm here I got my yum yum drink it's the I" | **Shared span (computed):** whole line |
| "I'm really just not very organized. I'm gonna be honest with you guys" | [0:05:27](https://youtu.be/76-YKpxYL4g?t=327) | "Where's my BGM? I'm really just not very organized. I'm gonna be honest with you guys I'm really just" | **Shared span (computed):** whole line |
| "Oh my god. I'm gonna lose it. What an annoying guy." | [1:02:20](https://youtu.be/76-YKpxYL4g?t=3740) | "in the world Oh my god, I'm gonna lose it What an annoying guy Flame spirit hat" | **Shared span (computed):** whole line |
| "Fucking adorable." | [1:28:37](https://youtu.be/76-YKpxYL4g?t=5317) | "fluff her hair and adorable I don't like" | **Not confirmed** (second model: "and adorable"); removed from the card |
| "But I'll catch you guys on the flip side" | [4:45:37](https://youtu.be/76-YKpxYL4g?t=17137) | "this evening says busy busy but I'll catch you guys on the flipside yeah I'll" | Agrees ("flipside" written as one word) |
| "All right. Take care everybody. I'll see you soon Goodbye Bye I'm out" | [4:46:25](https://youtu.be/76-YKpxYL4g?t=17185) | "Yeah, I guess I'm out of here all right take care everybody. I'll see you soon Goodbye, and bye" | **Partial (computed):** shared runs "all right take care everybody i'll see you soon goodbye" |
| "is she gonna climb up the slide I knew it kids love doing this shit oh my god" | [1:32:30](https://youtu.be/y0WsNvXOdns?t=5550) | "hoops up there is she gonna climb up the slide I knew it kids love doing this shit oh my god yeah oh my" | **Shared span (computed):** whole line |
| "Let's try it again. Let's try this shit." | [1:59:06](https://youtu.be/y0WsNvXOdns?t=7146) | "a platformer. Okay. Let's try it again. Let's try this shit again. Retry, okay." | **Shared span (computed):** whole line |
