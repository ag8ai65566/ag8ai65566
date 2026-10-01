# Audio check — Raora Panthera (2026-10-01)

Method: windows from the public stream archive archive.ragtag.moe (YouTube blocks this environment),
transcribed with faster-whisper small.en, pitch measured with Praat (100–600 Hz, word intervals only).
Tools and limits: `novel-lab/tools/audiocheck/README.md`. **This is not a listening check**: the audio was
machine-transcribed and acoustically measured, and the transcripts were reviewed in context. Lines used on
the character card were re-transcribed by a second model (whisper medium.en) and compared (see the end of
this file). Transcription does not write laughs reliably. Measurements describe the sampled recording and
ASR segmentation; game audio, music and other speakers prevent treating them as isolated vocal measurements.

All windows are from 2026. Only in-scope public performance material is used. The Pragmata window mixes in game
voices (a child character), which lifts its pitch figures.

## Windows measured

| Window | Stream | Segment | Speech (min) | Words | Words/min of speech | F0 median | F0 p10–p90 |
|---|---|---|---|---|---|---|---|
| close2026 | [【ODDCORE】NOTHING MAKES SENSE HERE ?!? 【Raora Pan](https://youtu.be/97aydhssGYs) | [3:27:54–3:37:54](https://youtu.be/97aydhssGYs?t=12474) | 6.4 | 299 | 46.5 | 285 Hz | 199–441 Hz |
| chat30_2026 | [LETS CHAT BIG CAT WANTS TO YAP](https://youtu.be/pTPX4PAk7Qw) | [0:30:00–1:00:00](https://youtu.be/pTPX4PAk7Qw?t=1800) | 25.5 | 3194 | 125.5 | 251 Hz | 197–385 Hz |
| open2026 | [LETS CHAT BIG CAT WANTS TO YAP](https://youtu.be/pTPX4PAk7Qw) | [0:00:00–0:15:00](https://youtu.be/pTPX4PAk7Qw?t=0) | 8.4 | 1100 | 131.0 | 256 Hz | 206–406 Hz |
| game30_2026 | [【Pragmata】BIG CAT MEANS BIG RESPONSIBILITIES【Rao](https://youtu.be/zc_JRHPep9c) | [1:00:00–1:30:00](https://youtu.be/zc_JRHPep9c?t=3600) | 18.8 | 1022 | 54.3 | 267 Hz | 175–445 Hz |

"Words/min of speech" = words ÷ minutes inside whisper's speech segments.

## Claims checked

| Claim in the file | Result (in the machine transcript) | Evidence (ASR, archived audio) |
|---|---|---|
| "big cat means big trouble" (RP4) | **Confirmed** as a sign-off ("…and remember, big cat means big trouble"). | [3:35:48](https://youtu.be/97aydhssGYs?t=12948) |
| Gentle, rarely swears (RP2) | **Consistent.** Only "frick" and "damn" when muted by accident. | [0:05:21](https://youtu.be/pTPX4PAk7Qw?t=321) |
| Firm about her rules | **Confirmed (playfully).** "Hear me out. … First, you guys have no rights. … No, thank you. I refuse." | [0:40:52](https://youtu.be/pTPX4PAk7Qw?t=2452); [0:42:29](https://youtu.be/pTPX4PAk7Qw?t=2549) |
| Chattini lore | **Confirmed.** "Oh, you're one of those zipper Chattini." "I swear I live in the Justice headquarters." | [0:33:19](https://youtu.be/pTPX4PAk7Qw?t=1999); [0:37:54](https://youtu.be/pTPX4PAk7Qw?t=2274) |
| Italian-accented English | **Consistent in the transcript:** a few non-native constructions in fast speech; the accent itself is not measurable here. | throughout |
| Pitch | **Measured:** chat window medians about 251–256 Hz, p10–p90 about 197–406 Hz. Not a ranking. | table above |

## New material (ASR-transcribed short lines)

Lines not listed in the second-model check at the end of this file are first-model transcriptions only.

- "I'm sure you guys like my cooking shorts because they are made with so much love." [0:39:55](https://youtu.be/pTPX4PAk7Qw?t=2395)
- "If I was a kid and I had all this entertainment, I would go crazy." [1:18:34](https://youtu.be/zc_JRHPep9c?t=4714)

## Second-model check (whisper medium.en)

Each line below was cut from the archived audio (a window of about 24–60 s around the first model's
timestamp) and transcribed again by a larger model. "Agrees" means the second model produced the same
words; it is still machine transcription, not listening. Lines that did not agree were removed from
the character card.

| First model (small.en) | Link | Second model (medium.en), excerpt | Verdict |
|---|---|---|---|
| "go big or go home" | [3:31:59](https://youtu.be/97aydhssGYs?t=12719) | "must be hard. Go beaker, go home! Go beaker, go home!" | **Disagrees** ("Go beaker, go home"); not used |
| "Hope you guys gonna have a good day no matter what. Thank you Chattini for watching" | [3:35:25](https://youtu.be/97aydhssGYs?t=12925) | "to work we're gonna have a good day it's a teeny for watching went to the team have a good team a" | **Disagrees**; not used |
| "Remember, big cat means big trouble" | [3:35:48](https://youtu.be/97aydhssGYs?t=12948) | "take care and remember big cat means big trouble goodnight all too" | Agrees; the second model adds "goodnight … Ciao! Buh-Bye!" |
| "Frick I was muted" | [0:05:21](https://youtu.be/pTPX4PAk7Qw?t=321) | "frick i was muted damn whoopsie oh" | **Shared span (computed):** whole line |
| "Whoopsie. That was totally intentional, that was totally intentional everyone" | [0:05:27](https://youtu.be/pTPX4PAk7Qw?t=327) | "whoopsie uh oh that was totally intentional that was totally intentional everyone that was yeah no" | **Partial (computed):** shared runs "that was totally intentional that was totally intentional everyone" |
| "We back, you guys are so back" | [0:06:33](https://youtu.be/pTPX4PAk7Qw?t=393) | "of my control we back you guys are so back it works sometime" | **Shared span (computed):** whole line |
| "Oh, you're one of those zipper chattini. I love those kind" | [0:33:21](https://youtu.be/pTPX4PAk7Qw?t=2001) | "mess with it oh you're one of those zipper chatini i love those kind because i stuff" | **Partial (computed):** shared runs "oh you're one of those zipper" … "i love those kind" |
| "No, Chattini, you cannot get any of my plushies." | [0:36:04](https://youtu.be/pTPX4PAk7Qw?t=2164) | "Can't sell anyone. No. No Chotini! Chotini, you cannot get any of my plushies. I'm" | Agrees ("Chotini" spelling) |
| "I'll be honest. I'm a hater now. Okay, let me be a hater" | [0:36:10](https://youtu.be/pTPX4PAk7Qw?t=2170) | "I kinda hate I'll be honest I'm a hater now okay let me be a hater so I have" | **Shared span (computed):** whole line |
| "I swear I live in the Justice headquarters. I promise." | [0:37:56](https://youtu.be/pTPX4PAk7Qw?t=2276) | "so blue and I swear I live in the justice at quarter I promise hola okay" | Agrees ("justice at quarter") |
| "I'm sure you guys like my cooking shorts because they are made with so much love" | [0:39:55](https://youtu.be/pTPX4PAk7Qw?t=2395) | "happy someone likes I'm sure you guys like my cooking shorts because they are made with so much love and I love" | **Shared span (computed):** whole line |
| "Okay, okay, okay, okay. Hear me out. I have something to say about this comment. First, you guys have no rights." | [0:40:51](https://youtu.be/pTPX4PAk7Qw?t=2451) | "in the future okay okay okay okay hear me out um I have something to say about this comment first you guys have no rights by any" | **Partial (computed):** shared runs "okay okay okay okay hear me out" … "i have something to say about this comment first you guys have no rights" |
| "it's not negotiable it's not even a question" | [0:41:12](https://youtu.be/pTPX4PAk7Qw?t=2472) | "things are mine it's not negotiable it's not even a question you know like" | **Shared span (computed):** whole line |
| "No, thank you. I refuse." | [0:42:29](https://youtu.be/pTPX4PAk7Qw?t=2549) | "make me happy no, no thank you i refuse yeah, the" | **Shared span (computed):** whole line |
| "Oh boy, this makes me so emotional. She's so cute." | [1:00:04](https://youtu.be/zc_JRHPep9c?t=3604) | "i can help she's next why this makes me so emotional she's so cute" | Agrees on "this makes me so emotional. She's so cute." |
| "Because I'm a big cat. It's a big cat, it's literally me" | [1:13:12](https://youtu.be/zc_JRHPep9c?t=4392) | "cat? She's giving me a big cat drawing? It's a big cat! It's literally me! Thank you, Dion!" | **Shared span only** ("It's a big cat, it's literally me") |
| "If I was a kid and I had all this entertainment, I would go crazy." | [1:18:34](https://youtu.be/zc_JRHPep9c?t=4714) | "to do huh no if i was a kid and i had all this entertainment i'll go crazy what is in" | **Partial (computed):** shared runs "if i was a kid and i had all this entertainment" |
