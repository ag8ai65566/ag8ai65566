# Audio check — Gigi Murin (2026-10-01)

Method: windows from the public stream archive archive.ragtag.moe (YouTube blocks this environment),
transcribed with faster-whisper small.en, pitch measured with Praat (100–600 Hz, word intervals only).
Tools and limits: `novel-lab/tools/audiocheck/README.md`. **This is not a listening check**: the audio was
machine-transcribed and acoustically measured, and the transcripts were reviewed in context. Lines used on
the character card were re-transcribed by a second model (whisper medium.en) and compared (see the end of
this file). Transcription does not write laughs reliably. Measurements describe the sampled recording and
ASR segmentation; game audio, music and other speakers prevent treating them as isolated vocal measurements.

All windows are from 2026. The 13 Sentinels window mixes in voiced game characters (its pitch and pace are
not hers alone) and no line from it is used. Only in-scope public performance material is used; a sponsored segment
is left out.

## Windows measured

| Window | Stream | Segment | Speech (min) | Words | Words/min of speech | F0 median | F0 p10–p90 |
|---|---|---|---|---|---|---|---|
| chat30_2026 | [【SC KETCHUP】im thinkin about holodori](https://youtu.be/LgDuyqoaqT4) | [1:00:00–1:30:00](https://youtu.be/LgDuyqoaqT4?t=3600) | 23.8 | 3041 | 127.6 | 265 Hz | 185–406 Hz |
| open2026 | [【SC KETCHUP】im thinkin about holodori](https://youtu.be/LgDuyqoaqT4) | [0:00:00–0:15:00](https://youtu.be/LgDuyqoaqT4?t=0) | 5.0 | 577 | 114.9 | 267 Hz | 182–404 Hz |
| close2026 | [【RHYTHM HEAVEN GROOVE】sweating all over the A bu](https://youtu.be/RplRUa_21Ng) | [3:32:41–3:42:41](https://youtu.be/RplRUa_21Ng?t=12761) | 4.1 | 488 | 119.2 | 291 Hz | 149–443 Hz |
| game30_2026 | [【13 SENTINELS: AEGIS RIM】i have to eat my vegeta](https://youtu.be/mo4XRT84Jo8) | [1:00:00–1:30:00](https://youtu.be/mo4XRT84Jo8?t=3600) | 21.7 | 2139 | 98.8 | 233 Hz | 129–384 Hz |

"Words/min of speech" = words ÷ minutes inside whisper's speech segments.

## Claims checked

| Claim in the file | Result (in the machine transcript) | Evidence (ASR, archived audio) |
|---|---|---|
| Talks for a long time before the game (GG4) | **Consistent.** The SC KETCHUP stream opens with about 8 minutes of setup and merch talk. | [0:07:58](https://youtu.be/LgDuyqoaqT4?t=478) |
| Turns things into bits (GG2) | **Confirmed.** A blurred merch photo becomes a crime scene; bad luck becomes an "Etsy witch" hex. | [0:13:46](https://youtu.be/LgDuyqoaqT4?t=826); [0:14:20](https://youtu.be/LgDuyqoaqT4?t=860) |
| Quick deadpan in superchats | **Confirmed.** "I require context." (twice); "I'm sure that's true. I don't remember the context, but I'm sure it's true." | [1:03:16](https://youtu.be/LgDuyqoaqT4?t=3796); [1:01:24](https://youtu.be/LgDuyqoaqT4?t=3684) |
| Crude jokes and casual swearing (GG2) | **Consistent.** "hell" and "shit" appear in passing (first model); no slurs. | throughout |
| Ties with Kiara (Ultra Orange) | **Confirmed (new detail).** "I know Kiara saved the world. Literally." (Hytale); she decorated a friendship-journal entry Kiara brought to fes. | [1:01:53](https://youtu.be/LgDuyqoaqT4?t=3713); [1:16:19](https://youtu.be/LgDuyqoaqT4?t=4579) |
| Pitch | **Measured:** chat window medians about 265–267 Hz, p10–p90 about 182–406 Hz. Not a ranking. | table above |

## New material (ASR-transcribed short lines)

Lines not listed in the second-model check at the end of this file are first-model transcriptions only.

- Sound effects and scatting: "BAM BAM BAM BAM", "Talalalalala". [1:06:53](https://youtu.be/LgDuyqoaqT4?t=4013)
- "Thank you … for the Super. I need validation." [1:00:17](https://youtu.be/LgDuyqoaqT4?t=3617)
- A Hytale "wedding" bit with Kiara proposed by chat ("we need to have a Hytale wedding"), a performed joke. [1:03:58](https://youtu.be/LgDuyqoaqT4?t=3838)

## Second-model check (whisper medium.en)

Each line below was cut from the archived audio (a window of about 24–60 s around the first model's
timestamp) and transcribed again by a larger model. "Agrees" means the second model produced the same
words; it is still machine transcription, not listening. Lines that did not agree were removed from
the character card.

| First model (small.en) | Link | Second model (medium.en), excerpt | Verdict |
|---|---|---|---|
| "We're still trying to find the killer so the victim has been, their face has been blurred out of consideration for their family." | [0:13:46](https://youtu.be/LgDuyqoaqT4?t=826) | "is We're chill. We're still trying to find the the killer So the victim has been Their face has been blurred out of consideration for their family But someone" | **Partial (computed):** shared runs "we're still trying to find the" … "killer so the victim has been their face has been blurred out of consideration for their family" |
| "I feel like someone hired an Etsy witch to curse me and to hex me" | [0:14:20](https://youtu.be/LgDuyqoaqT4?t=860) | "feel like um i feel like someone hired an etsy witch to curse me and to hex me so i'm gonna" | **Shared span (computed):** whole line |
| "I need validation." | [1:00:21](https://youtu.be/LgDuyqoaqT4?t=3621) | "for the Supa. I need validation. Does anyone remember" | **Shared span (computed):** whole line |
| "If it works, 51% of the time, that's enough." | [1:00:35](https://youtu.be/LgDuyqoaqT4?t=3635) | "you ask that. If it works 51% of the time, that's enough. Yeah, if you" | **Shared span (computed):** whole line |
| "I'm sure that's true. I don't remember the context, but I'm sure it's true." | [1:01:24](https://youtu.be/LgDuyqoaqT4?t=3684) | "because she's wild I'm sure that's true. I don't remember the context and I'm sure it's true Thank you pip" | Agrees ("and I'm sure it's true" in the second model; the sentence is used) |
| "I know Kiara saved the world. Literally." | [1:01:53](https://youtu.be/LgDuyqoaqT4?t=3713) | "content updates ASAP. I know Kiara saved the world, literally, she saved my" | **Shared span (computed):** whole line |
| "i require context what was the context" | [1:03:19](https://youtu.be/LgDuyqoaqT4?t=3799) | "probably enjoy it. I require context. What was the context? Maybe I would." | **Shared span (computed):** whole line |
| "Yes, make sure to keep your tails clean, everyone. No one likes a dirty, stinky tail." | [1:15:40](https://youtu.be/LgDuyqoaqT4?t=4540) | "my tail! Weeee! Yes, make sure to keep your tails clean, everyone. No one likes a dirty, stinky tail. And your tail" | **Shared span (computed):** whole line |
| "I require context." | [1:17:36](https://youtu.be/LgDuyqoaqT4?t=4656) | "in your bra? I require context. Thank you, Nishizomi," | **Shared span (computed):** whole line |
| "Thanks grems for hanging out" | [3:41:11](https://youtu.be/RplRUa_21Ng?t=13271) | "a good time! Thanks, Grams, for hanging out. I will see" | **Name differs** ("Thanks, Grams" / "Thanks Squams"); only "…for hanging out" is quoted |
| "I'll be back tomorrow. You'll see me again." | [3:41:18](https://youtu.be/RplRUa_21Ng?t=13278) | "see you guys tomorrow I'll be back tomorrow. You'll see me again. I will" | **Shared span (computed):** whole line |
| "Okay guys, chill, chill, chill, chill." | [1:00:39](https://youtu.be/mo4XRT84Jo8?t=3639) | "yourself so hard Okay, guys chill chill chill chill My turn now," | Agrees, but the window mixes in voiced game characters; **not used** |
| "Good job everyone, why are you taking so much damage?" | [1:07:35](https://youtu.be/mo4XRT84Jo8?t=4055) | "We made it. Good job everyone. Why do you take so much damage? The fight is" | Close ("Why do you take so much damage?"); game window, **not used** |
| "Oh my vegetables! My vegetables!" | [1:08:02](https://youtu.be/mo4XRT84Jo8?t=4082) | "that one. No! My big rules! Oh! My big rules! Where" | **Disagrees** ("My big rules!"); not used |
| "Can you please sing for us while we have- please, please, please!" | [1:14:24](https://youtu.be/mo4XRT84Jo8?t=4464) | "to worry about can you can you please sing for us while we have please please please bard" | Agrees, but likely a game character's line; **not used** |
