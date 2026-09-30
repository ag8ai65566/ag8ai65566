# Audio check — Takanashi Kiara (2026-09-30)

Method: short windows from the public stream archive archive.ragtag.moe (YouTube blocks this
environment), transcribed with faster-whisper small.en, pitch measured with Praat (100–600 Hz, word
intervals only). Tools and limits: `novel-lab/tools/audiocheck/README.md`. **This is not a listening
check**: the audio was machine-transcribed and acoustically measured, and the transcripts were reviewed
in context. Lines used on the character card were re-transcribed by a second model (whisper medium.en)
and compared (see the end of this file). Whisper does not write "Kikkeriki" or non-speech sounds reliably,
and game voices in Slay the Spire 2 and DOOM Eternal mix into the transcript; only lines that are clearly
hers are quoted.

## Windows measured

| Window | Stream | Segment | Speech (min) | Words | Words/min of speech | F0 median | F0 p10–p90 |
|---|---|---|---|---|---|---|---|
| chat45 | [【SLAY THE SPIRE 2】this thumbnail says i must pla](https://youtu.be/-5P17BxVZTE) | [1:00:00–1:45:00](https://youtu.be/-5P17BxVZTE?t=3600) | 21.7 | 2890 | 133.4 | 290 Hz | 191–455 Hz |
| close | [【SLAY THE SPIRE 2】this thumbnail says i must pla](https://youtu.be/-5P17BxVZTE) | [2:37:31–2:49:31](https://youtu.be/-5P17BxVZTE?t=9451) | 8.8 | 1577 | 179.3 | 243 Hz | 185–389 Hz |
| open | [【SLAY THE SPIRE 2】this thumbnail says i must pla](https://youtu.be/-5P17BxVZTE) | [0:00:00–0:15:00](https://youtu.be/-5P17BxVZTE?t=0) | 5.3 | 805 | 152.2 | 302 Hz | 205–454 Hz |
| rage45 | [【DOOM ETERNAL】doom is eternal, joy is not #KFP #](https://youtu.be/gqQoOjKBmLw) | [1:30:00–2:15:00](https://youtu.be/gqQoOjKBmLw?t=5400) | 37.6 | 3435 | 91.3 | 264 Hz | 192–442 Hz |

## Claims checked

| Claim in the file | Result (in the machine transcript) | Evidence (ASR, archived audio) |
|---|---|---|
| Sign-off lesson "In German we say ___" | **Confirmed.** | "In German we say auf wiedersehen." [2:47:40](https://youtu.be/-5P17BxVZTE?t=10060) |
| Third-person "Wawa" | **Confirmed**, about 6 times an hour in the Slay the Spire sample, also while telling a story in DOOM. | "So actually, tomorrow, Calli, Ina, Wawa, Wawa, Wawa, lots of people in Hytale." [2:39:41](https://youtu.be/-5P17BxVZTE?t=9581); "but wawa still have nightmares" [2:07:32](https://youtu.be/gqQoOjKBmLw?t=7652) |
| Frequent, casual swearing (T3 counted masked caption tokens) | **Confirmed, with the actual words.** Slay the Spire (chat and closing, about 1 hour): 11 detections ("damn it," "fucking," "fuck," "shit"). DOOM (45 min): about 37 lines with swears, many of them "fucking." Aimed at games, objects, cars and stories, and playfully at people. | "everybody is fucking good at making Miis" [2:42:58](https://youtu.be/-5P17BxVZTE?t=9778); "Holy shit, they're all cracked" [2:43:03](https://youtu.be/-5P17BxVZTE?t=9783); "what the fuck am I supposed to do with 16" [1:40:15](https://youtu.be/gqQoOjKBmLw?t=6015); "They look like shit." [1:49:35](https://youtu.be/gqQoOjKBmLw?t=6575) |
| "Oh my god" as a constant reaction | **Present but not "every few sentences"**: about 3 times an hour in the sampled transcripts (whisper drops some interjections, so this is a floor). | "Oh my god, you're so cute!" [1:26:53](https://youtu.be/-5P17BxVZTE?t=5213) |
| "cute" | **New: very frequent.** Stacks of "It's so cute!" / "You're so cute!" while looking at game art. | [1:25:31](https://youtu.be/-5P17BxVZTE?t=5131)–[1:31:15](https://youtu.be/-5P17BxVZTE?t=5475) |
| "Kikkeriki!" | **Not checkable here.** Whisper does not write it; the openings of these windows are game audio and chat. | — |
| Pace and pitch | **Fast, upper-middle.** About 133–179 words per minute of speech in chat (with Calli the fastest); DOOM 91 (busy play). Median pitch about 245–300 Hz (game voices push the chat windows up; the closing talk measures 244 Hz). | table above |

## New material (ASR-transcribed short lines)

- "It's like tiny in size, but it's so fucking heavy." [2:37:42](https://youtu.be/-5P17BxVZTE?t=9462)
- "How why the fuck did she not make me yet? Because she loves me" [2:43:52](https://youtu.be/-5P17BxVZTE?t=9832)
- "Yes! Me! One woman! One doom girl will stop the armies of hell" [2:13:15](https://youtu.be/gqQoOjKBmLw?t=7995)
- "that is a big fucking gun" [1:43:18](https://youtu.be/gqQoOjKBmLw?t=6198)
