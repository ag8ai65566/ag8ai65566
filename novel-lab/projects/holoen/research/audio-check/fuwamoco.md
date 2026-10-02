# Audio check — FUWAMOCO: Fuwawa and Mococo Abyssgard (2026-10-01)

Method: windows from the public stream archive archive.ragtag.moe (YouTube blocks this environment),
transcribed with faster-whisper small.en, pitch measured with Praat (100–600 Hz, word intervals only).
Tools and limits: `novel-lab/tools/audiocheck/README.md`. **This is not a listening check**: the audio was
machine-transcribed and acoustically measured, and the transcripts were reviewed in context. Lines used on
the cards were re-transcribed by a second model (whisper medium.en) and compared (see the end of this file).

The twins share one channel and usually one microphone, and transcription cannot tell their voices apart. So
this report uses three kinds of windows: a 2026 **Fuwawa solo** stream (Hitman), a 2025 **Mococo solo**
stream (Phasmophobia), and a 2026 **duo** after-party chat whose lines stay unattributed. Parts of both solo
streams touch on personal matters outside the project's scope; those parts are not quoted, and the stream
titles are shortened below for the same reason.

## Windows measured

### Fuwawa (solo)
| Window | Stream | Segment | Speech (min) | Words | Words/min of speech | F0 median | F0 p10–p90 |
|---|---|---|---|---|---|---|---|
| close2026 | [【HITMAN】 (FUWAWA SOLO)](https://youtu.be/L93K3U4Hrjg) | [5:47:07–5:59:07](https://youtu.be/L93K3U4Hrjg?t=20827) | 5.1 | 443 | 87.6 | 406 Hz | 313–521 Hz |
| game40_2026 | [【HITMAN】 (FUWAWA SOLO)](https://youtu.be/L93K3U4Hrjg) | [1:00:00–1:40:00](https://youtu.be/L93K3U4Hrjg?t=3600) | 19.6 | 1850 | 94.2 | 330 Hz | 169–459 Hz |
| open2026 | [【HITMAN】 (FUWAWA SOLO)](https://youtu.be/L93K3U4Hrjg) | [0:00:00–0:15:00](https://youtu.be/L93K3U4Hrjg?t=0) | 6.6 | 503 | 76.2 | 353 Hz | 254–479 Hz |

### Mococo (solo, 2025; a quiet stream with few words)
| Window | Stream | Segment | Speech (min) | Words | Words/min of speech | F0 median | F0 p10–p90 |
|---|---|---|---|---|---|---|---|
| close2025 | [【PHASMOPHOBIA】 (MOCOCO SOLO)](https://youtu.be/Sxx4UW3XKnc) | [2:51:59–3:03:59](https://youtu.be/Sxx4UW3XKnc?t=10319) | 3.6 | 262 | 73.3 | 359 Hz | 151–523 Hz |
| game40_2025 | [【PHASMOPHOBIA】 (MOCOCO SOLO)](https://youtu.be/Sxx4UW3XKnc) | [0:50:00–1:30:00](https://youtu.be/Sxx4UW3XKnc?t=3000) | 23.6 | 609 | 25.8 | 423 Hz | 270–543 Hz |
| open2025 | [【PHASMOPHOBIA】 (MOCOCO SOLO)](https://youtu.be/Sxx4UW3XKnc) | [0:00:00–0:15:00](https://youtu.be/Sxx4UW3XKnc?t=0) | 0.5 | 81 | 152.4 | 364 Hz | 292–472 Hz |

### FUWAMOCO (duo; voices not separated)
| Window | Stream | Segment | Speech (min) | Words | Words/min of speech | F0 median | F0 p10–p90 |
|---|---|---|---|---|---|---|---|
| chat30_2026 | [【#holoSerendipity CONCERT AFTERPARTY 雑談】los ange](https://youtu.be/YDP2JT3gce4) | [0:30:00–1:00:00](https://youtu.be/YDP2JT3gce4?t=1800) | 21.1 | 2479 | 117.6 | 405 Hz | 289–531 Hz |
| close2026 | [【#holoSerendipity CONCERT AFTERPARTY 雑談】los ange](https://youtu.be/YDP2JT3gce4) | [2:07:40–2:19:40](https://youtu.be/YDP2JT3gce4?t=7660) | 5.1 | 616 | 121.0 | 401 Hz | 294–525 Hz |
| open2026 | [【#holoSerendipity CONCERT AFTERPARTY 雑談】los ange](https://youtu.be/YDP2JT3gce4) | [0:00:00–0:15:00](https://youtu.be/YDP2JT3gce4?t=0) | 5.5 | 518 | 94.4 | 410 Hz | 280–530 Hz |

"Words/min of speech" = words ÷ minutes inside whisper's speech segments.

## Claims checked

| Claim | Result (in the machine transcript) | Evidence (ASR, archived audio) |
|---|---|---|
| Duo opening "Hello hello bau bau! … I'm not a chihuahua, I'm Fuwawa! …" (wiki) | **Not detected in the sampled 2026 chat opening**, which starts after a waiting screen. | [0:06:11](https://youtu.be/YDP2JT3gce4?t=371) |
| "bau bau" everywhere (wiki) | **Not transcribed** in these windows ("bau" 0); the models may not write it. Kept from the wiki. | — |
| Very high voices | **Measured:** Fuwawa solo medians 330–406 Hz; Mococo's quiet 2025 solo 359–423 Hz (thin sample); duo 401–410 Hz (the combined recording; not assignable to either twin). Measurements describe the sampled recording and ASR segmentation, not isolated voices. Not a ranking. | tables above |
| Fuwawa: chatty, polite, confident nonsense (wiki) | **Consistent.** "Hello, ma'am. Nice day, ma'am." "Should I run? Is running suspicious?" "I'm blending in right now, right?"; "okay" 42, "right?" 34, "maybe" 21 in about an hour. | [0:12:13](https://youtu.be/L93K3U4Hrjg?t=733); [1:12:32](https://youtu.be/L93K3U4Hrjg?t=4352) |
| Fuwawa defers Pup Talks to Mococo | **Confirmed.** After her own gym pep talk ("…be the main character of the gym") she says Moco-chan is "just better suited for it." Her description of her own voice differs between the models and is not quoted. | [5:48:33](https://youtu.be/L93K3U4Hrjg?t=20913); [5:52:55](https://youtu.be/L93K3U4Hrjg?t=21175) |
| Duo echo / "sync" (wiki) | **Consistent.** "yeah" about once every 40 words; "Right! … Exactly."; "Did we see any princesses? No. No. No princesses." | [2:12:18](https://youtu.be/YDP2JT3gce4?t=7938); [0:31:51](https://youtu.be/YDP2JT3gce4?t=1911) |
| Mococo's vowel tail, sneezes (wiki) | **Not detectable** by transcription. Kept from the wiki. | — |
| No swearing | **Consistent** in all windows. | — |

## Second-model check (whisper medium.en)

Each line below was cut from the archived audio (a window of about 24–60 s around the first model's
timestamp) and transcribed again by a larger model. "Agrees" means the second model produced the same
words; it is still machine transcription, not listening. Lines that did not agree were removed from
the character card.

| First model (small.en) | Link | Second model (medium.en), excerpt | Verdict |
|---|---|---|---|
| "Yeah, he did not look at me. Hello, ma'am. Nice day, ma'am." | [0:12:13](https://youtu.be/L93K3U4Hrjg?t=733) | "at me Don't look at me Yeah, he did not look at me Hello ma'am, nice day ma'am" | **Shared span (computed):** whole line |
| "Should I run? Is running suspicious?" | [0:13:41](https://youtu.be/L93K3U4Hrjg?t=821) | "out of here. Should I run? Is running suspicious? I could go" | **Shared span (computed):** whole line |
| "Question, is his clothes better than mine? No. In you go." | [1:05:17](https://youtu.be/L93K3U4Hrjg?t=3917) | "Okay, now question. Is his clothes better than mine? No. Okay, in you go. Oh, wrong" | **Partial (computed):** shared runs "question is his clothes better than mine no" … "in you go" |
| "Princess in a different castle." | [1:08:26](https://youtu.be/L93K3U4Hrjg?t=4106) | "on another building. Princess is in a different castle. I was" | Agrees ("Princess in" vs "Princess is in"; quoted "…in a different castle") |
| "Can I have one? I like one. Can I have one? Get away from me, you creep. I want one. I want one." | [1:11:16](https://youtu.be/L93K3U4Hrjg?t=4276) | "That looks yummy. Can I have one? I like one. Can I have one? I want one. I want one. I want one. Can I have one? What are" | **Partly agrees**: "That looks yummy. Can I have one? I like one. Can I have one?" agrees; "Get away from me, you creep" is first-model only (probably a game voice) and is not quoted |
| "Please give me your snacks. I'm not even asking for a full loaf." | [1:11:41](https://youtu.be/L93K3U4Hrjg?t=4301) | "and I'll go away Please give me your snacks not even asking for a full loaf just one of" | **Partly agrees**: "Please give me your snacks… not even asking for a full loaf" (the second model lacks "I'm") |
| "If I go into the crowd, too, I blend in. Right? I'm blending in right now, right?" | [1:12:32](https://youtu.be/L93K3U4Hrjg?t=4352) | "it go well? If I go into the crowd too... I blend in Right? I'm blending in right now, right? So... Do I" | **Shared span (computed):** whole line |
| "But it's gonna be good because you're gonna be stronger and you're gonna be healthy." | [5:48:21](https://youtu.be/L93K3U4Hrjg?t=20901) | "ahhh I'm sweaty But it's gonna be good because you gonna be Stronger and you gonna be healthy And you gonna" | **Partly agrees** ("you're gonna" vs "you gonna"); not quoted; the next line is |
| "So go do that, go to the gym and be the main character of the gym." | [5:48:33](https://youtu.be/L93K3U4Hrjg?t=20913) | "can do anything so go do that go to the gym and be the main character of the gym okay you got" | **Shared span (computed):** whole line |
| "But mocha-chan's just better suited for it, you know? But I'm a bit fuffier. My voice is a bit softer, so..." | [5:52:55](https://youtu.be/L93K3U4Hrjg?t=21175) | "same as Moko-chan's pop-talks But Moko-chan's is better suited for it, you know? But I'm a bit full for it My voice is a bit slow too, so..." | **Partly agrees**: "Moco-chan's [is] just better suited for it, you know?" agrees; her description of her own voice differs ("fuffier… softer" vs "full for it… slow too") and is not quoted |
| "It was a lot of fun! I'm going to have lots and lots of cake!" | [5:55:28](https://youtu.be/L93K3U4Hrjg?t=21328) | "much, Raffias Wow! It was a lot of fun Please be sure to support Mukocha lots and lots, okay? Listen to" | **Partly agrees**: "It was a lot of fun!" agrees; the cake line is first-model only |

## Second-model check (whisper medium.en)

Each line below was cut from the archived audio (a window of about 24–60 s around the first model's
timestamp) and transcribed again by a larger model. "Agrees" means the second model produced the same
words; it is still machine transcription, not listening. Lines that did not agree were removed from
the character card.

| First model (small.en) | Link | Second model (medium.en), excerpt | Verdict |
|---|---|---|---|
| "I die. If I die, I die." | [0:57:47](https://youtu.be/Sxx4UW3XKnc?t=3467) | "I If I die I die if I die I" | Agrees ("If I die, I die") |

## Second-model check (whisper medium.en)

Each line below was cut from the archived audio (a window of about 24–60 s around the first model's
timestamp) and transcribed again by a larger model. "Agrees" means the second model produced the same
words; it is still machine transcription, not listening. Lines that did not agree were removed from
the character card.

| First model (small.en) | Link | Second model (medium.en), excerpt | Verdict |
|---|---|---|---|
| "a real senpai a real senpai" | [0:13:12](https://youtu.be/YDP2JT3gce4?t=792) | "it to Santa-senpai, Popo-senpai, Ami-o-senpai, what do we senpai? Who else eat?" | **Disagrees**: the second model hears a list of senpai names; not quoted |
| "A courteous half bite?" | [0:13:44](https://youtu.be/YDP2JT3gce4?t=824) | "them it was dessert! Karate-senpai got a whole piece, and" | **Disagrees**: not in the second model's text; not quoted |
| "Do you know when you hold a cat up by its armpit? And then its arms are straight out." | [0:13:57](https://youtu.be/YDP2JT3gce4?t=837) | "didn't like it. And you know, when you hold a cat up by its armpits. And then its arms are straight out. That's why she" | **Partly agrees** ("when you hold a cat up by…"); not quoted |
| "I'm a donut pro, okay?" | [0:30:33](https://youtu.be/YDP2JT3gce4?t=1833) | "did though. Cause I'm a donut pro, okay? That's a lie." | Agrees; the second model continues "That's a lie." (the other twin, apparently; not quoted on the card) |
| "But Chewbacca is basically a princess. Chewbacca is the princess." | [0:31:51](https://youtu.be/YDP2JT3gce4?t=1911) | "No. No princesses. But Chewbacca is basically a princess. Chewbacca is the princess. Okay. Yeah. Yeah." | **Shared span (computed):** whole line |
| "They're not Bulbasaur shaped, he's just sitting there on the package. I'm scammed, right!" | [0:38:16](https://youtu.be/YDP2JT3gce4?t=2296) | "What is he on the package? They just watermelons They're not Bulbasaur shaped He's just sitting there on the package" | **Partly agrees** ("They're not Bulbasaur shaped"); not quoted |
| "I wanted to eat Bulbasaur." | [0:38:32](https://youtu.be/YDP2JT3gce4?t=2312) | "was the point? Huh? I wanted to eat boba-so-shaped candies Yeah" | **Disagrees** ("Bulbasaur" vs "boba-so-shaped"); not quoted |
| "Special memories! Thank you!" | [0:42:50](https://youtu.be/YDP2JT3gce4?t=2570) | "and everything It'll be another really special memory too And" | **Disagrees**: not quoted |
| "The moon!" | [2:08:10](https://youtu.be/YDP2JT3gce4?t=7690) | "Florida New York The moon Chicago Las Vegas" | **Shared span (computed):** whole line |
| "So again, guys, talk about this. Maybe, um, they need to put us in charge." | [2:12:03](https://youtu.be/YDP2JT3gce4?t=7923) | "all on the cruise here we go again guys i do feel like we talked about this maybe around fast? i" | **Partly agrees**: "they need to put us in charge" is in both; the lead-in differs |
| "Right! Right! Exactly." | [2:12:18](https://youtu.be/YDP2JT3gce4?t=7938) | "put us in charge. Right. Exactly. Endurance concert. Yeah." | Agrees on "Right!" and "Exactly." (the second model has "Right. They need to put us in charge. Right. Exactly.") |

