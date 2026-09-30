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
| Swearing mostly softened; harder under gaming pressure | **Consistent.** Resident Evil 2 (45 min): "Damn.", "god damn", "what the hell", "Bastards"; no f-word in this window (the f-word evidence stays with the compilation, G11). 2024 chat: "what the heck", "freaking". | "Yo Bastards… god damn, no" [3:01:47](https://youtu.be/JELLJ3osUUQ?t=10907); "oh what the hell" [3:02:16](https://youtu.be/JELLJ3osUUQ?t=10936) |
| Triplets / stacked words | **Confirmed.** | "Okay, okay, wait, okay, wait, wait, wait." [0:01:47](https://youtu.be/JUvdnKuBMDQ?t=107) |
| Sign-off with care lines and stacked goodbyes | **Partly.** The 2022 horror stream ended warmly but plainly. | "Thank you guys for hanging with me today. I appreciate it. I'll see you tomorrow… Have a nice day" [3:48:58](https://youtu.be/_aeIw9DJnBw?t=13738) |
| Relatively high voice | **Confirmed, relative.** Median F0 about 248–270 Hz, the highest group with Ame (Kronii 177–188 Hz). Chat pace about 122–139 words per minute of speech. | table above |

## New material (ASR-transcribed short lines)

- "hey do you want to know a really stupid fact about me" [0:03:29](https://youtu.be/_aeIw9DJnBw?t=209)
- "You don't scare me. Cheap party city lady. I see better makeup on clowns these days."
- "Bro, you cooked." (2024 birthday, about a fan project) [0:01:20](https://youtu.be/JUvdnKuBMDQ?t=80)
- "Well, I don't usually wear pants." [9:57:56](https://youtu.be/54ysrFu09hA?t=35876)
