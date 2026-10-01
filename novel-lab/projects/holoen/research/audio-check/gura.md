# Audio check — Gawr Gura (2026-09-30)

Method: short windows from the public stream archive archive.ragtag.moe (YouTube blocks this
environment), transcribed with faster-whisper small.en, pitch measured with Praat (100–600 Hz, word
intervals only). Tools and limits: `novel-lab/tools/audiocheck/README.md`. **This is not a listening check**: the audio was
machine-transcribed and acoustically measured, and the transcripts were reviewed in context. Lines used on
the character card were re-transcribed by a second model (whisper medium.en) and compared (see the end of
this file). Machine transcription, read
in context; it drops some fillers and does not write screams, humming or laughter reliably. Horror-game
windows include game voices; only lines that are clearly hers are quoted.

## Windows measured

| Window | Stream | Segment | Speech (min) | Words | Words/min of speech | F0 median | F0 p10–p90 |
|---|---|---|---|---|---|---|---|
| ban_pants | [[DEVIL MAY CRY 3] I am Awakened](https://youtu.be/54ysrFu09hA) | [9:56:30–9:59:50](https://youtu.be/54ysrFu09hA?t=35790) | 2.2 | 357 | 159.0 | 269 Hz | 211–470 Hz |
| re2_45 | [[RESIDENT EVIL: 2] X GON' GIV'IT TO YA](https://youtu.be/JELLJ3osUUQ) | [2:30:00–3:15:00](https://youtu.be/JELLJ3osUUQ?t=9000) | 27.7 | 2392 | 86.3 | 254 Hz | 204–422 Hz |
| re2_mid | [[RESIDENT EVIL: 2] X GON' GIV'IT TO YA](https://youtu.be/JELLJ3osUUQ) | [1:15:00–2:30:00](https://youtu.be/JELLJ3osUUQ?t=4500) | 52.5 | 4076 | 77.6 | – Hz | ––– Hz |
| re2_rest | [[RESIDENT EVIL: 2] X GON' GIV'IT TO YA](https://youtu.be/JELLJ3osUUQ) | [3:15:00–4:22:51](https://youtu.be/JELLJ3osUUQ?t=11700) | 45.5 | 3835 | 84.3 | – Hz | ––– Hz |
| re2_start | [[RESIDENT EVIL: 2] X GON' GIV'IT TO YA](https://youtu.be/JELLJ3osUUQ) | [0:00:00–1:15:00](https://youtu.be/JELLJ3osUUQ?t=0) | 52.4 | 5303 | 101.1 | – Hz | ––– Hz |
| chat30_2024 | [【BIRTHDAY CHAT】birthday fishe! ✨🎉🎂 #gurabirthday](https://youtu.be/JUvdnKuBMDQ) | [1:00:00–1:30:00](https://youtu.be/JUvdnKuBMDQ?t=3600) | 23.6 | 2872 | 121.8 | 257 Hz | 178–445 Hz |
| open2024 | [【BIRTHDAY CHAT】birthday fishe! ✨🎉🎂 #gurabirthday](https://youtu.be/JUvdnKuBMDQ) | [0:00:00–0:15:00](https://youtu.be/JUvdnKuBMDQ?t=0) | 12.1 | 1688 | 139.0 | 259 Hz | 116–470 Hz |
| close | [【THE MORTUARY ASSISTANT】Shark help!](https://youtu.be/_aeIw9DJnBw) | [3:40:25–3:50:25](https://youtu.be/_aeIw9DJnBw?t=13225) | 6.4 | 1142 | 178.8 | 248 Hz | 196–428 Hz |
| humming | [【THE MORTUARY ASSISTANT】Shark help!](https://youtu.be/_aeIw9DJnBw) | [0:59:30–1:02:50](https://youtu.be/_aeIw9DJnBw?t=3570) | 1.9 | 207 | 109.0 | 333 Hz | 184–503 Hz |
| laugh | [【THE MORTUARY ASSISTANT】Shark help!](https://youtu.be/_aeIw9DJnBw) | [2:40:00–2:43:20](https://youtu.be/_aeIw9DJnBw?t=9600) | 1.4 | 226 | 163.4 | 249 Hz | 173–471 Hz |
| let_me_in | [【THE MORTUARY ASSISTANT】Shark help!](https://youtu.be/_aeIw9DJnBw) | [1:14:40–1:18:00](https://youtu.be/_aeIw9DJnBw?t=4480) | 1.5 | 168 | 109.1 | 270 Hz | 178–480 Hz |
| open | [【THE MORTUARY ASSISTANT】Shark help!](https://youtu.be/_aeIw9DJnBw) | [0:00:00–0:10:00](https://youtu.be/_aeIw9DJnBw?t=0) | 8.6 | 815 | 95.1 | 266 Hz | 198–429 Hz |

## Claims checked

| Claim in the file | Result (in the machine transcript) | Evidence (ASR, archived audio) |
|---|---|---|
| Opener "hello hello hello" | **Confirmed** (2022). | "Hello, hello, hello, how's this one, oh yeah, oh yeah" [0:06:37](https://youtu.be/_aeIw9DJnBw?t=397) |
| "Shrimp" for members, from "simp? Do you mean shrimp?" | **Confirmed**: she retells it herself in 2024. | "What is simp? Do you mean shrimp?" [1:15:30](https://youtu.be/JUvdnKuBMDQ?t=4530) |
| Horror bargaining, "Please let me in!!" (HoloIndex 1:15:31) | **Partly confirmed.** The segment is partly garbled by the scream: "…please let me okay". | [1:15:20](https://youtu.be/_aeIw9DJnBw?t=4520) |
| Humming (HoloIndex 1:00:16) | **Confirmed.** Sung nonsense syllables. | "Oh, deey, oh, deey…" [1:00:22](https://youtu.be/_aeIw9DJnBw?t=3622) |
| Triumphant laugh (HoloIndex 2:40:44) | **Confirmed, with the line before it.** | "You don't scare me. Cheap party city lady. I see better makeup on clowns these days. Ha, ha, ha, ha." [2:40:44](https://youtu.be/_aeIw9DJnBw?t=9644) |
| "BAN PANTS!" (DMC3, stream time 9:57:37 cited by the wiki) | **Context confirmed**: the pants question, "If you could get away with not wearing pants, would you?", "Pants are stupid". The chant itself comes out as "…pants and pants and pants", consistent with "ban pants" but not provable. | [9:58:19](https://youtu.be/54ysrFu09hA?t=35899), [9:58:50](https://youtu.be/54ysrFu09hA?t=35930), [9:59:01](https://youtu.be/54ysrFu09hA?t=35941) |
| Swearing mostly softened; harder under gaming pressure | **Consistent, with a rare f-word.** Resident Evil 2 transcribed in full (4.4 h): both models agree on "Oh, what the hell?", "Yo bastard!", "Oh my god, shit shit" and "You bastard. Yeah, get him, Leon." Both hear one f-word from her while she riffs on an in-game memo, with different surrounding words. The clearest "get me the fuck out of here" (3:42:48) is a game character (Ben). "Damn.", "god damn" and "No, damn it" were not confirmed. 2024 chat: "what the heck", "freaking". | "Yo bastard!" [3:01:47](https://youtu.be/JELLJ3osUUQ?t=10907); "Oh, what the hell?" [3:03:15](https://youtu.be/JELLJ3osUUQ?t=10995); f-word [1:05:27](https://youtu.be/JELLJ3osUUQ?t=3927) |
| Triplets / stacked words | **Confirmed.** | "Okay, okay, wait, okay, wait, wait, wait." [0:01:47](https://youtu.be/JUvdnKuBMDQ?t=107) |
| Sign-off with care lines and stacked goodbyes | **Partly.** The 2022 horror stream ended warmly but plainly. | "Thank you guys for hanging with me today. I appreciate it. I'll see you tomorrow… Have a nice day" [3:48:58](https://youtu.be/_aeIw9DJnBw?t=13738) |
| Relatively high voice | **Confirmed, relative.** Median F0 about 248–270 Hz, the highest group with Ame (Kronii 177–188 Hz). Chat pace about 122–139 words per minute of speech. | table above |

## New material (ASR-transcribed short lines)

Lines not listed in the second-model check at the end of this file are first-model transcriptions only.

- Mocking a game character's delivery: after Leon's "Son of a bitch," "Come on Leon, say it with a bit more
  oomph. Say it like it's really bothering you, Leon." [1:38:48](https://youtu.be/JELLJ3osUUQ?t=5928)

- "hey do you want to know a really stupid fact about me" [0:03:29](https://youtu.be/_aeIw9DJnBw?t=209)
- "You don't scare me. Cheap party city lady. I see better makeup on clowns these days."
- "Bro, you cooked." (2024 birthday, about a fan project) [0:01:20](https://youtu.be/JUvdnKuBMDQ?t=80)
- "Well, I don't usually wear pants." [9:57:56](https://youtu.be/54ysrFu09hA?t=35876)

## Second-model check (whisper medium.en)

Each line below was cut from the archived audio (a window of about 24–60 s around the first model's
timestamp) and transcribed again by a larger model. "Agrees" means the second model produced the same
words; it is still machine transcription, not listening. Lines that did not agree were removed from
the character card.

| First model (small.en) | Link | Second model (medium.en), excerpt | Verdict |
|---|---|---|---|
| "Well, I don't usually wear pants." | [9:57:56](https://youtu.be/54ysrFu09hA?t=35876) | "shark girl anatomy. Well, I don't usually wear pants. Uh...I don't usually" | **Shared span (computed):** whole line |
| "If you could get away with not wearing pants, would you?" | [9:58:19](https://youtu.be/54ysrFu09hA?t=35899) | "me rephrase that. If you could get away with not wearing pants, would you? Yes Yes, you" | **Shared span (computed):** whole line |
| "Please tell me it's down this alleyway. Shit." | [0:23:31](https://youtu.be/JELLJ3osUUQ?t=1411) | "We're gonna go down this alleyway. Please tell me it's down this alleyway. Yeah," | **Not confirmed**: the second model has the sentence but no "Shit." |
| "You know who you are, you bastard. Who wants to fuck up these badly?" | [1:05:25](https://youtu.be/JELLJ3osUUQ?t=3925) | "this right now! You know who you are, you bastard? Who else is fucking with you badly? You don't know" | **Agrees on an f-word, not on the words**: second model "You know who you are, you bastard? Who else is fucking with you badly?" (she is riffing on an in-game memo) |
| "oh my god that shit shit" | [1:28:29](https://youtu.be/JELLJ3osUUQ?t=5309) | "something on like my... no? Oh my god shit shit" | Agrees ("Oh my god shit shit") |
| "come on Leon say it with a bit more oomph say it like it's really bothering you Leon" | [1:38:48](https://youtu.be/JELLJ3osUUQ?t=5928) | "Come on Leo, say it with a bit more. Say it with a bit more oomph. Say it like it's really bothering you, Leon." | Agrees (after the game's "Son of a bitch") |
| "You bastard. Yeah, get him Leon, get him Leon" | [1:56:16](https://youtu.be/JELLJ3osUUQ?t=6976) | "go from behind. You bastard. Yeah, get him, Leon. Get him, Leon. Whoa, baby! Back" | **Shared span (computed):** whole line |
| "Damn. Wait, what? This is the third floor." | [2:56:18](https://youtu.be/JELLJ3osUUQ?t=10578) | "Here. He flinched! I'm gonna get you, Michael. You're gonna be" | **Not confirmed** (the second model heard different words); "Damn." dropped |
| "Yo Bastards, bullets on you, god damn, no" | [3:01:47](https://youtu.be/JELLJ3osUUQ?t=10907) | "No, no, no, no, no. Yo bastard! Stop, put your hands" | **Partly**: "Yo bastard!" agrees; "god damn" is not confirmed and was removed from the card |
| "oh what the hell" | [3:03:15](https://youtu.be/JELLJ3osUUQ?t=10995) | "sorry I'm sorry. Oh what the hell? You telling me" | **Shared span (computed):** whole line |
| "I really don't like that shit wasted a bullet bitch" | [3:54:07](https://youtu.be/JELLJ3osUUQ?t=14047) | "They're so fast, they're gonna kick my butt! I really don't like that." | **Not confirmed** (second model: "I really don't like that." without the swears) |
| "No, damn it" | [4:11:48](https://youtu.be/JELLJ3osUUQ?t=15108) | "Hi Marvin! Marvin, please die with" | **Not confirmed** (second model: "Marvin, please die with one bullet.") |
| "Bro, you cooked." | [0:01:20](https://youtu.be/JUvdnKuBMDQ?t=80) | "Featuring all of you! Bro, you cooked. A lot" | **Shared span (computed):** whole line |
| "Okay, okay, wait, okay, wait, wait, wait." | [0:01:47](https://youtu.be/JUvdnKuBMDQ?t=107) | "jumpscare. Is that me? Okay, okay wait, okay wait wait" | **Partial (computed):** shared runs "okay okay wait okay wait wait" |
| "What is simp? Do you mean shrimp?" | [1:15:34](https://youtu.be/JUvdnKuBMDQ?t=4534) | "it? Oh yeah, simp. What is simp? Do you mean shrimp? Cute! Wait," | **Shared span (computed):** whole line |
| "Hello, hello, hello, how's this one, oh yeah, oh yeah" | [0:06:37](https://youtu.be/_aeIw9DJnBw?t=397) | "Gain... How much gain do we need? Hello? Hello? Hello? How's this one? What's that again?" | Agrees on "Hello? Hello? Hello? How's this one?"; the trailing "oh yeah, oh yeah" is not confirmed |
| "You don't scare me. Cheap party city lady. I see better makeup on clowns these days." | [2:40:44](https://youtu.be/_aeIw9DJnBw?t=9644) | "very, uh huh. You don't scare me, cheap party city lady. I see better makeup on clowns these days. Okay, does anyone" | **Shared span (computed):** whole line |
