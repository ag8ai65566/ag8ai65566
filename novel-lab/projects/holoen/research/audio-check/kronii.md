# Audio check — Ouro Kronii (2026-09-30)

Method: short windows taken from the public stream archive archive.ragtag.moe (YouTube blocks this
environment), transcribed with faster-whisper small.en and measured with Praat (pitch floor 100 Hz,
ceiling 600 Hz, word intervals only). Tools and limits: `novel-lab/tools/audiocheck/README.md`.
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

| Claim in the file | Result | Evidence (audio) |
|---|---|---|
| "that's on me" / "that was my bad" when she misplays (wiki K8, stream 6WFU2wzPKfA t=5981) | **"That was my bad" confirmed** (twice). "That's on me" was not heard in this window. | "Oh, okay. That was my bad." [1:39:01](https://youtu.be/6WFU2wzPKfA?t=5941); "Okay, okay. That was my bad" [1:40:41](https://youtu.be/6WFU2wzPKfA?t=6041); 2026: "whoops my bad" [1:39:33](https://youtu.be/tdLRQtJ3kkY?t=5973) |
| Greeting "Kroniichiwa!" | **Consistent.** A stack of hellos, then the greeting (whisper writes it as the ordinary word "Konnichiwa"), then "Yay". Exact pun form not provable from a machine transcript. | "Hello. Hello. Hello. Hello." [0:06:04](https://youtu.be/tdLRQtJ3kkY?t=364) → greeting [0:07:17](https://youtu.be/tdLRQtJ3kkY?t=437) → "Yay, oh, yeah, yippee" [0:07:20](https://youtu.be/tdLRQtJ3kkY?t=440) |
| "Yay" was treated as title vocabulary only (removed from the card in verify round 1) | **Overturned: "Yay!" is a spoken habit.** 21 hits in about 2 hours of audio, plus "Yippee!". Its tone (flat or ironic) cannot be read from a transcript. | "Yay!" [1:04:37](https://youtu.be/tdLRQtJ3kkY?t=3877), [1:10:25](https://youtu.be/tdLRQtJ3kkY?t=4225); horror stream "Yay!" [2:33:47](https://youtu.be/esjpYSrvjB4?t=9227); "Yippee! Oh, man! I've been so productive every single day." [0:10:45](https://youtu.be/tdLRQtJ3kkY?t=645) |
| Swears when startled or frustrated | **Not observed in these samples.** The only hits were superchats she read aloud ("you'd be damn right", "Why the hell are you so pretty"). Her swearing rests on the clip titles (K32); it is not constant. | — |
| GWAK when scared | **Not checkable here.** Whisper does not write squawks; the 45-minute horror window shows fright in words instead. | "Oh my god, that hand scared me" [2:41:44](https://youtu.be/esjpYSrvjB4?t=9704) |
| Low speaking register | **Confirmed, relative.** Lowest median F0 of the six Myth/Kronii/Calli files measured the same way (chat 177–188 Hz; Calli 197–214 Hz; Gura and Ame about 250–270 Hz). | table above |

## New material (audio-verified short lines)

- Fear narrated deadpan: "I'm scared that one day I'm gonna run through here and then… they're gonna be
  like, oh, yeah, you thought it was safe, right?" [2:02:51](https://youtu.be/esjpYSrvjB4?t=7371)
- Self-roast while reading her own journal aloud: "I'm so funny. I can't read this."
  [0:14:31](https://youtu.be/tdLRQtJ3kkY?t=871)
- Talking herself out of (and into) a purchase: "why why am I doing this whatever but I really think my
  setup is really good anyway" [2:52:06](https://youtu.be/tdLRQtJ3kkY?t=10326)
- Game-planning narration: stacked "yeah, yeah, yeah…" and "okay, and then…" while routing
  ([2:35:15](https://youtu.be/esjpYSrvjB4?t=9315)).
