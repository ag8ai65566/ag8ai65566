# Audio check — Cecilia Immergreen (2026-10-01)

Method: windows from the public stream archive archive.ragtag.moe (YouTube blocks this environment),
transcribed with faster-whisper small.en, pitch measured with Praat (100–600 Hz, word intervals only).
Tools and limits: `novel-lab/tools/audiocheck/README.md`. **This is not a listening check**: the audio was
machine-transcribed and acoustically measured, and the transcripts were reviewed in context. Lines used on
the character card were re-transcribed by a second model (whisper medium.en) and compared (see the end of
this file). Transcription does not write laughs reliably. Measurements describe the sampled recording and
ASR segmentation; game audio, music and other speakers prevent treating them as isolated vocal measurements.

All windows are from 2026 (May–June, before a summer break that is not written per the author's rule). In
one Zelda window she talks about her family; that stretch is personal and not used.

## Windows measured

| Window | Stream | Segment | Speech (min) | Words | Words/min of speech | F0 median | F0 p10–p90 |
|---|---|---|---|---|---|---|---|
| close2026 | [【ZELDA: A LINK TO THE PAST】I have awakened~ what](https://youtu.be/PryFPuyr9Lg) | [2:29:18–2:39:18](https://youtu.be/PryFPuyr9Lg?t=8958) | 6.3 | 683 | 108.5 | 221 Hz | 130–411 Hz |
| chat30_2026 | [Explaining the entire plot of NARUTO from very b](https://youtu.be/UhXQ7dxDltk) | [0:30:00–1:00:00](https://youtu.be/UhXQ7dxDltk?t=1800) | 28.1 | 4069 | 144.9 | 254 Hz | 183–418 Hz |
| open2026 | [Explaining the entire plot of NARUTO from very b](https://youtu.be/UhXQ7dxDltk) | [0:00:00–0:15:00](https://youtu.be/UhXQ7dxDltk?t=0) | 9.5 | 1203 | 126.4 | 234 Hz | 165–384 Hz |
| game30_2026 | [【ZELDA: A LINK TO THE PAST】I must find the princ](https://youtu.be/wZLK-gSqZnY) | [1:00:00–1:30:00](https://youtu.be/wZLK-gSqZnY?t=3600) | 19.2 | 2678 | 139.4 | 220 Hz | 115–436 Hz |

"Words/min of speech" = words ÷ minutes inside whisper's speech segments.

## Claims checked

| Claim in the file | Result (in the machine transcript) | Evidence (ASR, archived audio) |
|---|---|---|
| Fast, talkative storyteller | **Confirmed.** About 145 words a minute of speech explaining Naruto's plot from memory, with stacked asides. | [0:30:00–1:00:00](https://youtu.be/UhXQ7dxDltk?t=1800) |
| German comes up in jokes (CI2) | **Confirmed.** "In German he says…" (the jutsu name). | [0:35:26](https://youtu.be/UhXQ7dxDltk?t=2126) |
| Sarcastic, self-congratulating | **Confirmed.** "Oh my god, I'm so smart." "My memory is really good." "…a calculated mistake." | [0:39:57](https://youtu.be/UhXQ7dxDltk?t=2397); [1:01:20](https://youtu.be/wZLK-gSqZnY?t=3680) |
| Theatrical in games | **Confirmed.** "Come then, die by my hands, you foolish mortals!" "No, I will not die, I shall not perish." | [2:31:19](https://youtu.be/PryFPuyr9Lg?t=9079); [2:33:25](https://youtu.be/PryFPuyr9Lg?t=9205) |
| Light swearing | **Detected.** "yippee type shit" (both models). | [0:07:56](https://youtu.be/UhXQ7dxDltk?t=476) |
| Pitch | **Measured:** chat window medians about 234–254 Hz, p10–p90 about 165–418 Hz. Not a ranking. | table above |

## New material (ASR-transcribed short lines)

Lines not listed in the second-model check at the end of this file are first-model transcriptions only.

- Runs of repeated words when fixing her setup: "okay, okay, okay…", "perfect, perfect, perfect…". [0:11:13](https://youtu.be/UhXQ7dxDltk?t=673)
- A pun on Kronii while drawing Orochimaru ("Orokroni Senpai"; spelling differs between models). [0:40:53](https://youtu.be/UhXQ7dxDltk?t=2453)
- The day after the CCGG 3D live: "I'm so tired, but in like a happy relief type of way." [0:07:49](https://youtu.be/UhXQ7dxDltk?t=469)

## Second-model check (whisper medium.en)

Each line below was cut from the archived audio (a window of about 24–60 s around the first model's
timestamp) and transcribed again by a larger model. "Agrees" means the second model produced the same
words; it is still machine transcription, not listening. Lines that did not agree were removed from
the character card.

| First model (small.en) | Link | Second model (medium.en), excerpt | Verdict |
|---|---|---|---|
| "Come then, die by my hands, you foolish mortals" | [2:31:19](https://youtu.be/PryFPuyr9Lg?t=9079) | "activate it? Yes. Come then, die by my hands, you foolish mortals! Ow. Okay, I" | Agrees |
| "Well, it's over for me. It's over for me." | [2:31:59](https://youtu.be/PryFPuyr9Lg?t=9119) | "He's here. Ow. It's over for me. I'm dead. It's over for me. The world's" | Agrees ("It's over for me") |
| "No, I will not die, I shall not perish" | [2:33:25](https://youtu.be/PryFPuyr9Lg?t=9205) | "to activate this No, I will not die I shall not perish I'm gonna use" | Agrees |
| "Well, thank you very much for spending time with me today and listening to me be a little bit weird. A little bit weird. What else is new? Shut up." | [2:37:04](https://youtu.be/PryFPuyr9Lg?t=9424) | "very interesting question well thank you very much for spending time with me today and been listening to me be a little bit weird a little bit weird what else i…" | Agrees |
| "Hello, everyone. It's me, Cecilia Immergreen" | [0:04:48](https://youtu.be/UhXQ7dxDltk?t=288) | "and streamed yet again. Hello everyone, it's me Cecilia and we have" | **Shared span only** ("Hello, everyone, it's me"); her name is misheard by both |
| "we did it yippee type shit" | [0:07:58](https://youtu.be/UhXQ7dxDltk?t=478) | "like ah, yeah did it we did it yippee type shit Yeah," | Agrees |
| "maybe skipper skipper the stream just as much as I skipper skipper the filler" | [0:08:26](https://youtu.be/UhXQ7dxDltk?t=506) | "maybe skip this stream maybe skipper skipper this stream just as much as I skipper skipper the filter may fill" | Agrees ("skipper skipper") |
| "In German he says" | [0:35:28](https://youtu.be/UhXQ7dxDltk?t=2128) | "says in English. In German he says, shuten doppelgänger, shuten," | Agrees |
| "every cool story needs a trio" | [0:36:45](https://youtu.be/UhXQ7dxDltk?t=2205) | "dynamic trio, because every cool story needs a trio. So we have..." | Agrees |
| "don't tell me" | [0:39:48](https://youtu.be/UhXQ7dxDltk?t=2388) | "later on and it's I don't have any kobashi" | **Disagrees** on the attempts at the name; "don't tell me" not quoted |
| "oh my god I'm so smart it's kabuto" | [0:39:57](https://youtu.be/UhXQ7dxDltk?t=2397) | "Kabuto! Is it Kabuto? Oh my god, I'm so smart. It's Kabuto. And he's" | Agrees |
| "It's Orokroni Senpai, Oroshimaru." | [0:41:08](https://youtu.be/UhXQ7dxDltk?t=2468) | "are his hands. It's Orochroni Senpai Oroshimaru. This is our" | Agrees on the pun ("Orochroni" / "Orokroni" Senpai); spelling differs; not quoted |
| "Wow, he's just like me." | [0:44:55](https://youtu.be/UhXQ7dxDltk?t=2695) | "he's really smart wow he's just like me and he has" | Agrees |
| "Calculated. I knew that there was gonna be another heart and that's why I did that" | [1:00:53](https://youtu.be/wZLK-gSqZnY?t=3653) | "A cal- a calculated mistake. I knew that there was gonna be another heart. Aaand that's why I did that. Duh! Dun" | Agrees on "calculated mistake … I knew that there was gonna be another heart … that's why I did that" |
| "My memory is really good." | [1:01:20](https://youtu.be/wZLK-gSqZnY?t=3680) | "up i remember my memory is really good and then i" | Agrees |
| "Okay, okay, okay, okay, okay, easy, easy, easy, easy, easy." | [1:01:24](https://youtu.be/wZLK-gSqZnY?t=3684) | "went up here okay okay okay okay okay okay okay easy easy easy easy I just" | Agrees |
| "Come on, Princess, I'll protect you!" | [1:06:22](https://youtu.be/wZLK-gSqZnY?t=3982) | "Do you think if I fall off a cliff," | **Disagrees**; not used |
| "Wrong way, Princess, wrong way!" | [1:06:54](https://youtu.be/wZLK-gSqZnY?t=4014) | "wrong way princess wrong way she's so bad" | Agrees |
| "She's so bad at back-seating." | [1:07:03](https://youtu.be/wZLK-gSqZnY?t=4023) | "way princess wrong way she's so bad at back seeding oh my" | Agrees ("back seeding" spelling) |
