# Audio check — Koseki Bijou (2026-10-01)

Method: windows from the public stream archive archive.ragtag.moe (YouTube blocks this environment),
transcribed with faster-whisper small.en, pitch measured with Praat (100–600 Hz, word intervals only).
Tools and limits: `novel-lab/tools/audiocheck/README.md`. **This is not a listening check**: the audio was
machine-transcribed and acoustically measured, and the transcripts were reviewed in context. Lines used on
the character card were re-transcribed by a second model (whisper medium.en) and compared (see the end of
this file). Transcription does not write laughs reliably.

All windows are from 2026. A Tomodachi Life window (FQmt3juKGQ4, 1:00:00–1:40:00) was mostly silent drawing
and game voices (1,149 words in 40 minutes; median pitch pulled to 243 Hz by game audio) and is left out of
the table. Remarks in the RE4 close about dreams, a friend's visit and chores are personal and not used.

## Windows measured

| Window | Stream | Segment | Speech (min) | Words | Words/min of speech | F0 median | F0 p10–p90 |
|---|---|---|---|---|---|---|---|
| open2026 | [【BIRTHDAY 2026】ROCK IN! The Game: Biboo saves th](https://youtu.be/_C5x0uq-xOw) | [0:00:00–0:15:00](https://youtu.be/_C5x0uq-xOw?t=0) | 10.3 | 1428 | 138.6 | 300 Hz | 222–439 Hz |
| close2026 | [【RESIDENT EVIL 4】Where's Biboo going? bingo?](https://youtu.be/adiHNkjKMV0) | [5:58:31–6:10:31](https://youtu.be/adiHNkjKMV0?t=21511) | 8.2 | 1174 | 143.9 | 280 Hz | 217–423 Hz |
| game45_2026 | [【RESIDENT EVIL 4】Where's Biboo going? bingo?](https://youtu.be/adiHNkjKMV0) | [1:00:00–1:45:00](https://youtu.be/adiHNkjKMV0?t=3600) | 28.5 | 1497 | 52.6 | 282 Hz | 167–433 Hz |

An extra window was transcribed after the card was written (first model only): Idol Showdown,
[tR-21zKCBFM 0:30:00–1:10:00](https://youtu.be/tR-21zKCBFM?t=1800), 881 words in 40 minutes, much of it game
text read aloud; no pitch figure (game audio dominates). It has "beep" three more times and no profanity
detected; it adds no quoted lines and is not used on the card.

"Words/min of speech" = words ÷ minutes inside whisper's speech segments. About 1.2 hours used.

## Claims checked

| Claim in the file | Result (in the machine transcript) | Evidence (ASR, archived audio) |
|---|---|---|
| Never swears; says "beep" (KB2) | **Consistent with her stated practice; no profanity detected in the sampled windows** (about 1.2 hours); "beep" six times, including "don't be super beeping early" and a "beep box." | [6:05:33](https://youtu.be/adiHNkjKMV0?t=21933) |
| "super rock rock" for superchats | **Detected (first model).** Eleven times in the 12-minute close. | throughout the close |
| Calm in hard games (KB2) | **Consistent.** 53 words per minute of speech in RE4, with mock outrage rather than rage ("This place is a circus! Everyone's dumb!"). | [1:27:21](https://youtu.be/adiHNkjKMV0?t=5241) |
| Childlike, bubbly host | **Confirmed.** "Welcome to my birthday world! We're gonna save the city!"; repeated orders ("over here" five times, "Make a heart!"). | [0:05:38](https://youtu.be/_C5x0uq-xOw?t=338); [0:10:40](https://youtu.be/_C5x0uq-xOw?t=640) |
| Mock-solemn lore | **Confirmed.** "A worthy sacrifice, I will remember you."; "No, I was eeping. I was eeping. … I was hibernating." | [0:12:35](https://youtu.be/_C5x0uq-xOw?t=755); [6:01:25](https://youtu.be/adiHNkjKMV0?t=21685) |
| Learning Japanese (KB2) | **Confirmed.** Plans a Japanese-lesson stream with a real teacher: "killing two birds with one stone, learning Japanese and making content out of it." | [6:03:51](https://youtu.be/adiHNkjKMV0?t=21831) |
| Laugh ("squeegee," KB2) | **Partly detected.** "ha ha ha ha" bursts and "hehehe" giggles in the transcript; the sound itself is not measurable here. | throughout |
| Pitch | **Measured:** median 280–300 Hz, p10–p90 about 217–439 Hz; high in this project's samples, near Fauna and Mumei. Not a ranking. | table above |

## New material (ASR-transcribed short lines)

Lines not listed in the second-model check at the end of this file are first-model transcriptions only.

- Voicing RE4's merchant back at him: "What are you buying?", "Is that all?", then "Hehehe, thank you." [1:17:37](https://youtu.be/adiHNkjKMV0?t=4657)
- "You were rich a second ago. Well, that's what happens with money, doesn't it?" [1:19:03](https://youtu.be/adiHNkjKMV0?t=4743)
- Humming and scatting in a quiet stretch ("bam bam bam…", "da da da"). [1:26:46](https://youtu.be/adiHNkjKMV0?t=5206)

## Second-model check (whisper medium.en)

Each line below was cut from the archived audio (a window of about 24–60 s around the first model's
timestamp) and transcribed again by a larger model. "Agrees" means the second model produced the same
words; it is still machine transcription, not listening. Lines that did not agree were removed from
the character card.

| First model (small.en) | Link | Second model (medium.en), excerpt | Verdict |
|---|---|---|---|
| "I'm very happy to have you all here with me today. Let's save the city together, right? Together!" | [0:05:27](https://youtu.be/_C5x0uq-xOw?t=327) | "the birthday wishes! I'm very happy to have you all here with me today. Let's save the city together, right? Together! Together! Yes! Umm..." | Agrees |
| "Welcome to my birthday world! We're gonna save the city!" | [0:05:38](https://youtu.be/_C5x0uq-xOw?t=338) | "all right so welcome to my birthday world we're gonna save the city gameplay guide you" | Agrees |
| "Use your bodies and make a heart for Bebo birthday." | [0:10:40](https://youtu.be/_C5x0uq-xOw?t=640) | "can do it! Make a heart! Use your bodies and make a heart for b-ball birthday!" | Agrees (the name in "make a heart for Bebo/Biboo birthday" is spelled differently) |
| "you'll be so happy to give up your life be all right worthy sacrifice i will remember you" | [0:12:35](https://youtu.be/_C5x0uq-xOw?t=755) | "at that. Anyway, you'll be so happy to give up your life and be full of evil, right? A worthy sacrifice, I will remember" | **Partly agrees**: the shared span is "…worthy sacrifice, I will remember you"; the rest differs |
| "Yippee! Yippee, no Leon sandwich!" | [1:01:23](https://youtu.be/adiHNkjKMV0?t=3683) | "it works. It just works No Leon sandwich What" | **Partly agrees**: "Yippee!" is first-model only; "…no Leon sandwich" agrees |
| "so about that skybox. You saw nothing I saw nothing" | [1:07:26](https://youtu.be/adiHNkjKMV0?t=4046) | "that! Stop looking! So, so about that, uh, Skybox, um... You saw nothing. I saw nothing." | Agrees |
| "You were rich a second ago. Well that's what happens with money, doesn't it?" | [1:19:03](https://youtu.be/adiHNkjKMV0?t=4743) | "you were rich a second ago well that's what happens with money doesn't it soon as you" | Agrees |
| "I'm in a surplus. Look at this. Wow, I'm well stocked. Managing my resources like a pro." | [1:23:02](https://youtu.be/adiHNkjKMV0?t=4982) | "so much ammo I'm I'm I'm in a surplus look at this wow I'm well I'm all stocks managing my resources like a" | Agrees ("I'm well stocked" vs "I'm all stocks" differ; quoted only "Managing my resources like a pro" and "I'm in a surplus") |
| "This place is the circus! Everyone's dumb!" | [1:27:21](https://youtu.be/adiHNkjKMV0?t=5241) | "have no idea. This place is a circus! Everyone's dumb! Ashley's dumb! This" | Agrees ("the circus" vs "a circus"; the second model's "a" is used) |
| "Not all girls are Beebo's, but Beebo's are all girls. Wait. Does that make sense? That made more sense in my head" | [1:37:22](https://youtu.be/adiHNkjKMV0?t=5842) | "Not all girls are b-boys, but b-boys are all girls. Wait, does that make sense? That made more sense in my head. What? That doesn't-" | Agrees (the name is spelled "Beebo's"/"b-boys"; read as "Biboos") |
| "Oh, baby throwing a little baby tantrum." | [1:39:02](https://youtu.be/adiHNkjKMV0?t=5942) | "I See me throwing a little baby tran-trom. Oh Here we shall" | **Disagrees**: "baby throwing" vs "me throwing"; not quoted |
| "No, I was eeping. I was eeping. The general emotions was forming while I was eeping. Yes, I was hibernating" | [6:01:29](https://youtu.be/adiHNkjKMV0?t=21689) | "thousands of years? No, I was eeping. I was eeping. The general motion was forming while I was eeping. Yes, I was hibernating. I wasn't just" | Agrees on "No, I was eeping. I was eeping." and "I was hibernating" |
| "it takes millions of years for diamonds to form, you know" | [6:01:50](https://youtu.be/adiHNkjKMV0?t=21710) | "not thousands. Billions. Millions. Millions of years. It takes millions of years for diamonds to form, you" | Agrees |
| "killing two birds with one stone learning Japanese and making content out of it perfect" | [6:03:51](https://youtu.be/adiHNkjKMV0?t=21831) | "it'd be great killing two birds with one stone. Learning Japanese and making content out of it. Perfect. And then we'll" | Agrees |
| "Okay. Yes, but also don't be super beeping early" | [6:05:33](https://youtu.be/adiHNkjKMV0?t=21933) | "Have fun, b-boo. Okay, yes, but also don't be super beeping early. Like for example," | Agrees |
| "Well yes I am. We've established this. I am Queen's. Indeed. And I will embrace it." | [6:07:22](https://youtu.be/adiHNkjKMV0?t=22042) | "TEEHEE. I'm cringe? Well, yes, I am. We've established this. I am cringe. Indeed. I am, and I will embrace it. I" | **Partly agrees**: the first model hears "Queen's," the second "cringe" ("I'm cringe? Well, yes, I am… I embrace the cringe"); only "Well, yes, I am. We've established this." and "I will embrace it" are quoted |
| "Thank you everyone! I will finish RE4 next time!" | [6:08:46](https://youtu.be/adiHNkjKMV0?t=22126) | "girls! Beepoo later! Thank you everyone! I will finish RE4 next time! Beepoo later! A" | Agrees on "Thank you everyone! I will finish RE4 next time!"; the pun before it differs ("Beeple"/"Beepoo later") |

