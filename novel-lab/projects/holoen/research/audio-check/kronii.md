# Audio check — Ouro Kronii (2026-09-30)

Method: short windows taken from the public stream archive archive.ragtag.moe (YouTube blocks this
environment), transcribed with faster-whisper small.en and measured with Praat (pitch floor 100 Hz,
ceiling 600 Hz, word intervals only). Tools and limits: `novel-lab/tools/audiocheck/README.md`. **This is not a listening check**: the audio was
machine-transcribed and acoustically measured, and the transcripts were reviewed in context. Lines used on
the character card were re-transcribed by a second model (whisper medium.en) and compared (see the end of
this file).
Transcription is machine transcription, read in context by Claude; it drops some fillers and does not
write non-speech sounds (squawks, laughs). Quotes are short; timestamps link to the stream.

## Windows measured

| Window | Stream | Segment | Speech (min) | Words | Words/min of speech | F0 median | F0 p10–p90 |
|---|---|---|---|---|---|---|---|
| thats_on_me | [【SUPERHOT】That's Hot](https://youtu.be/6WFU2wzPKfA) | [1:39:00–1:41:30](https://youtu.be/6WFU2wzPKfA?t=5940) | 2.1 | 46 | 21.7 | 203 Hz | 159–300 Hz |
| horror45 | [【Resident Evil Requiem】Crying / #2](https://youtu.be/esjpYSrvjB4) | [2:00:00–2:45:00](https://youtu.be/esjpYSrvjB4?t=7200) | 32.6 | 1526 | 46.8 | 215 Hz | 164–338 Hz |
| chat45 | [【Superchat Catchup】B-Day Supas ✨](https://youtu.be/tdLRQtJ3kkY) | [1:00:00–1:45:00](https://youtu.be/tdLRQtJ3kkY?t=3600) | 36.2 | 4347 | 120.1 | 188 Hz | 108–290 Hz |
| close | [【Superchat Catchup】B-Day Supas ✨](https://youtu.be/tdLRQtJ3kkY) | [2:40:51–2:52:51](https://youtu.be/tdLRQtJ3kkY?t=9651) | 9.7 | 1225 | 126.6 | 187 Hz | 111–310 Hz |
| open | [【Superchat Catchup】B-Day Supas ✨](https://youtu.be/tdLRQtJ3kkY) | [0:00:00–0:15:00](https://youtu.be/tdLRQtJ3kkY?t=0) | 7.5 | 413 | 55.2 | 177 Hz | 111–310 Hz |

"Words/min of speech" = words ÷ minutes inside whisper's speech segments (silence between segments
excluded; pauses inside a segment and game audio included). Use the chat windows for her conversational
rate; the horror window is mostly quiet play.

## Claims checked

| Claim in the file | Result (in the machine transcript) | Evidence (ASR, archived audio) |
|---|---|---|
| "that's on me" / "that was my bad" when she misplays (wiki K8, stream 6WFU2wzPKfA t=5981) | **"That was my bad" confirmed** once by both models; a second first-model hit at 1:39:01 was not confirmed by the second model. "That's on me" was not detected in this window's transcript. | "Okay, okay. That was my bad" [1:40:41](https://youtu.be/6WFU2wzPKfA?t=6041); 2026: "whoops my bad" [1:39:33](https://youtu.be/tdLRQtJ3kkY?t=5973) |
| Greeting "Kroniichiwa!" | **Consistent.** A stack of hellos, then the greeting (whisper writes it as the ordinary word "Konnichiwa"), then "Yay". Exact pun form not provable from a machine transcript. | "Hello… hello!" [0:07:10](https://youtu.be/tdLRQtJ3kkY?t=430) → greeting [0:07:17](https://youtu.be/tdLRQtJ3kkY?t=437) → "Yay, oh, yeah, yippee" [0:07:20](https://youtu.be/tdLRQtJ3kkY?t=440) |
| "Yay" was treated as title vocabulary only (removed from the card in verify round 1) | **Overturned: "Yay!" is a spoken habit.** 21 hits in about 2 hours of audio, plus "Yippee!". Its tone (flat or ironic) cannot be read from a transcript. | "Yay!" [1:04:37](https://youtu.be/tdLRQtJ3kkY?t=3877), [1:10:25](https://youtu.be/tdLRQtJ3kkY?t=4225); horror stream "Yay!" [2:33:47](https://youtu.be/esjpYSrvjB4?t=9227); "Yippee! Oh, man! I've been so productive every single day." [0:10:45](https://youtu.be/tdLRQtJ3kkY?t=645) |
| Swears when startled or frustrated | **Not observed in these samples.** The only hits were superchats she read aloud ("you'd be damn right", "Why the hell are you so pretty"). Her swearing rests on the clip titles (K32); it is not constant. | — |
| GWAK when scared | **Not checkable here.** Whisper does not write squawks; the 45-minute horror window shows fright in words instead. | "Oh my god, that hand scared me" [2:41:44](https://youtu.be/esjpYSrvjB4?t=9704) |
| Low speaking register | **Confirmed, relative.** Lowest median F0 of the six Myth/Kronii/Calli files measured the same way (chat 177–188 Hz; Calli 197–214 Hz; Gura and Ame about 250–270 Hz). | table above |

## New material (ASR-transcribed short lines)

Lines not listed in the second-model check at the end of this file are first-model transcriptions only.

- Fear narrated deadpan: "I'm scared that one day I'm gonna run through here and then… they're gonna be
  like, oh, yeah, you thought it was safe, right?" [2:02:51](https://youtu.be/esjpYSrvjB4?t=7371)
- Self-roast while reading her own journal aloud: "I'm so funny. I can't read this."
  [0:14:31](https://youtu.be/tdLRQtJ3kkY?t=871)
- Talking herself out of (and into) a purchase: "why why am I doing this whatever but I really think my
  setup is really good anyway" [2:52:06](https://youtu.be/tdLRQtJ3kkY?t=10326)
- Game-planning narration: stacked "yeah, yeah, yeah…" and "okay, and then…" while routing
  ([2:35:15](https://youtu.be/esjpYSrvjB4?t=9315)).

## Second-model check (whisper medium.en)

Each line below was cut from the archived audio (a window of about 24–60 s around the first model's
timestamp) and transcribed again by a larger model. Verdicts name the exact shared span (corrected 2026-10-01
after the GPT project consult: a bare "Agrees" is not enough). "Agrees" formerly meant the second model produced the same
words; it is still machine transcription, not listening. Lines that did not agree were removed from
the character card.

| First model (small.en) | Link | Second model (medium.en), excerpt | Verdict |
|---|---|---|---|
| "Oh, okay. That was my bad." | [1:39:19](https://youtu.be/6WFU2wzPKfA?t=5959) | "Okay. Who else? Who else? Oh. Okay, let's go." | **Not confirmed** (the second model hears game shouting here); the 1:40:41 instance is the one used |
| "Okay, okay. That was my bad" | [1:40:41](https://youtu.be/6WFU2wzPKfA?t=6041) | "Okay, that was my bad. Getting impatient." | **Shared span:** "that was my bad" (the lead-in differs: "Okay, okay." / "Okay,") |
| "I'm scared that one day I'm gonna run through here and then you know that they're gonna be like, oh, yeah, you thought it was safe, right?" | [2:02:52](https://youtu.be/esjpYSrvjB4?t=7372) | "bloody and scary I'm scared that one day I'm gonna run through here and then and then you know they're gonna be like oh yeah you thought it was safe right it's …" | **Shared spans:** "I'm scared that one day I'm gonna run through here and then" … "they're gonna be like, oh, yeah, you thought it was safe, right?" (the middle differs: "you know that" / "and then you know") |
| "Oh my god, that hand scared me" | [2:41:44](https://youtu.be/esjpYSrvjB4?t=9704) | "Okay Oh my god, that hand scared me. What is this?" | **Shared span:** "Oh my god, that hand scared me" |
| "Hello. Hello. Hello. Hello." | [0:06:04](https://youtu.be/tdLRQtJ3kkY?t=364) | "I'm almost there, hold on. I will" | **Not confirmed** (window caught different words); the hellos before the greeting at 0:07:17 are confirmed instead |
| "Konnichiwa Yay, oh, yeah, yippee" | [0:07:17](https://youtu.be/tdLRQtJ3kkY?t=437) | "uh, uh, hello! Kedlanichiwa! Yay! Oh yay, yippee! Woohoo! Yeah! How" | **Agrees on the sequence** (hellos → greeting → "Yay! Oh yay, yippee! Woohoo!"); both models misspell the greeting word |
| "Yippee! Oh, man! I've been so productive every single day." | [0:10:45](https://youtu.be/tdLRQtJ3kkY?t=645) | "I will die? Yippee! Oh man! I've been so productive every single day. I do productive" | **Shared span:** "Yippee! Oh, man! I've been so productive every single day." |
| "I'm so funny. I can't read this." | [0:14:46](https://youtu.be/tdLRQtJ3kkY?t=886) | "week before... Oh, I'm so funny, I can't read this. Oh!" | **Shared span:** "I'm so funny" / "I can't read this" (punctuation normalized) |
| "Yay!" | [1:04:37](https://youtu.be/tdLRQtJ3kkY?t=3877) | "by the police. Yay! Uh, and V-Faction," | **Shared span:** "Yay" |
| "Yay!" | [1:10:25](https://youtu.be/tdLRQtJ3kkY?t=4225) | "bunch thank you yay and her can" | **Shared span:** "Yay" |
