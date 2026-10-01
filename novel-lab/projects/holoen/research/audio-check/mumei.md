# Audio check — Nanashi Mumei (2026-10-01)

Method: windows from the public stream archive archive.ragtag.moe (YouTube blocks this environment),
transcribed with faster-whisper small.en, pitch measured with Praat (100–600 Hz, word intervals only).
Tools and limits: `novel-lab/tools/audiocheck/README.md`. **This is not a listening check**: the audio was
machine-transcribed and acoustically measured, and the transcripts were reviewed in context. Lines used on
the character card were re-transcribed by a second model (whisper medium.en) and compared (see the end of
this file). Machine transcription drops some fillers and does not write screeches or hoots reliably, and
small.en can turn Japanese speech into English words, so Japanese phrases below are indicative only. Game
windows include game voices and teammates; only lines that are clearly hers are quoted.

All windows are from March–April 2025, her last active period before she graduated on 2025-04-27 (04-28
JST), which this project weights highest. Stories in the Q&A about her family, school and illnesses are
outside the project's scope and are not used. A planned window from an earlier chatting
stream (fLxgC-r6w1E) could not be fetched from the archive; the Q&A's opening and closing were used
instead.

## Windows measured

| Window | Stream | Segment | Speech (min) | Words | Words/min of speech | F0 median | F0 p10–p90 |
|---|---|---|---|---|---|---|---|
| draw30_2025 | [【MUMEI DRAWS】*Doodles In Complete Silence*](https://youtu.be/47wq1FMoEG0) | [0:30:00–1:00:00](https://youtu.be/47wq1FMoEG0?t=1800) | 0.0 | 0 | None | – Hz | ––– Hz |
| doom45_2025 | [【DOOM Eternal】The Grand Rip and Tear Finale !! #](https://youtu.be/5xL_7PGd3rk) | [2:00:00–2:45:00](https://youtu.be/5xL_7PGd3rk?t=7200) | 25.3 | 1245 | 49.3 | 302 Hz | 213–480 Hz |
| close2025 | [【OH HI】Moom Q&A !! ~](https://youtu.be/7vxLfdBqFac) | [1:22:19–1:34:19](https://youtu.be/7vxLfdBqFac?t=4939) | 6.4 | 1083 | 168.1 | 284 Hz | 214–422 Hz |
| open2025 | [【OH HI】Moom Q&A !! ~](https://youtu.be/7vxLfdBqFac) | [0:00:00–0:10:00](https://youtu.be/7vxLfdBqFac?t=0) | 8.7 | 777 | 89.0 | 293 Hz | 205–412 Hz |
| qa30_2025 | [【OH HI】Moom Q&A !! ~](https://youtu.be/7vxLfdBqFac) | [0:10:00–0:40:00](https://youtu.be/7vxLfdBqFac?t=600) | 23.5 | 3668 | 155.9 | 287 Hz | 208–422 Hz |
| ow30_2025 | [【OVERWATCH 2】im doing this for the fans !! not m](https://youtu.be/zfQJZ6LetCc) | [0:30:00–1:00:00](https://youtu.be/zfQJZ6LetCc?t=1800) | 12.5 | 1047 | 84.0 | 311 Hz | 197–473 Hz |

"Words/min of speech" = words ÷ minutes inside whisper's speech segments (silence between segments
excluded). About 2.1 hours of speech windows; the drawing window is silent by design (the stream's title is
"Doodles In Complete Silence") and gives no data. The opening window includes several minutes of her
fixing the background music. The Overwatch window mixes in teammates and game audio.

## Claims checked

| Claim in the file | Result (in the machine transcript) | Evidence (ASR, archived audio) |
|---|---|---|
| Official greeting "Oh hi! Hoo's this? Nanashi Mumei!" (M1) | **Partly detected.** Caught off guard by her music, she opens with "Oh, hi" and "…hi everybody. What's up? How are you?" (both models). The full official line was not detected. | [0:03:20](https://youtu.be/7vxLfdBqFac?t=200) |
| "Cutest voice," soft (M2) | **Not measurable here.** Median pitch 284–311 Hz, high in this project's samples and close to Fauna's (280–306 Hz). Sample results, not a ranking. | table above |
| Low energy, scattered, short attention span (M2) | **Confirmed.** She loses her train of thought and says so, tells herself to stay on topic, and cuts tangents with "anyways" (11 in 30 minutes) and "sorry" (11). | [0:10:00–0:40:00](https://youtu.be/7vxLfdBqFac?t=600) |
| Fast when chatting | **Confirmed.** 156–168 words per minute of speech in the Q&A and closing; 49 in DOOM and 84 in Overwatch. | table above |
| Fillers | **Confirmed.** "okay" 25 in the Q&A and 31 in the 12-minute closing; "I don't know" 19, "you know" 15, "I guess" 11, "like" 54 in 3,668 words. | throughout |
| Mild language | **Confirmed.** "shoot," "heck," "oh dear," "oh my gosh," "oh my goodness"; no strong swearing in about 2.1 hours. | throughout |
| "don don!" gavel (M2) | **Detected (first model).** "Don don!" six times in the Overwatch window; in the Q&A closing she promises a big one at the end of every stream (the transcripts mishear it as "don't on"). | [0:56:50](https://youtu.be/zfQJZ6LetCc?t=3410); [1:22:19](https://youtu.be/7vxLfdBqFac?t=4939) |
| Guardian-of-civilization authority | **Confirmed.** Ranking chip flavors: "…guardian of civilization! … I decide everything for humanity." | [0:19:41](https://youtu.be/7vxLfdBqFac?t=1181) |
| "Yippee," "hooray" | **Confirmed.** Five of each in the first ten minutes: "I love talking about myself. Yippee, yippee. Hooray." | [0:05:43](https://youtu.be/7vxLfdBqFac?t=343) |
| Short bright game reactions | **Confirmed.** DOOM: "uh oh" 7, "oh shoot" 2, "oh dear" 2; Overwatch: "nice" 21, "yay" 9, "oh no" 5, "Owie! Owie! Owie!" | [0:52:46](https://youtu.be/zfQJZ6LetCc?t=3166) |
| Japanese in games | **Detected.** "Saikou! Saikou desu!" (first model, seven "saikou"); "yowai" for herself (both models hear it, spelled differently); "arigato." | [0:31:25](https://youtu.be/zfQJZ6LetCc?t=1885); [0:40:29](https://youtu.be/zfQJZ6LetCc?t=2429) |
| Long, repeated goodbyes | **Confirmed.** "Goodbye for now. I'll see you probably tomorrow, probably tomorrow." then about a dozen "bye-bye"s. | [1:31:02](https://youtu.be/7vxLfdBqFac?t=5462) |
| High screeches when startled (M2) | **Not detected reliably** (transcription does not write screeches). Kept from the wiki (secondary). | — |

## New material (ASR-transcribed short lines)

Lines not listed in the second-model check at the end of this file are first-model transcriptions only.

- Before reading her genmates' questions: "Okay, are we ready? Are we bracing ourselves? We got our tissue
  box nearby." [0:11:33](https://youtu.be/7vxLfdBqFac?t=693)
- "…but what do I know? Everything." [0:31:35](https://youtu.be/7vxLfdBqFac?t=1895)
- "I've never been scared of anything ever." [0:26:39](https://youtu.be/7vxLfdBqFac?t=1599)
- "Good job homo sapien." [0:26:17](https://youtu.be/7vxLfdBqFac?t=1577)
- Arm-wrestling ranking: "I think I would win against Gura, Kiara, IRyS, Nerissa, and Mococo"; Biboo moves
  to the losing side ("She is a rock"); "But I have other skills and things that make me special, so
  whatever." [0:23:52](https://youtu.be/7vxLfdBqFac?t=1432); [0:27:23](https://youtu.be/7vxLfdBqFac?t=1643); [0:27:44](https://youtu.be/7vxLfdBqFac?t=1664)
- "Sometimes you go through life just not knowing stuff. You can't know everything." … "It's okay not to
  know stuff sometimes. Yeah, unless you're me. Exactly, unless you're me." [1:24:20](https://youtu.be/7vxLfdBqFac?t=5060)
- DOOM upgrades: "I'm too poor. No money." [2:07:07](https://youtu.be/5xL_7PGd3rk?t=7627)
- Overwatch: "Oh dear, that was pointless." [0:52:11](https://youtu.be/zfQJZ6LetCc?t=3131)

## Second-model check (whisper medium.en)

Each line below was cut from the archived audio (a window of about 24–60 s around the first model's
timestamp) and transcribed again by a larger model. "Agrees" means the second model produced the same
words; it is still machine transcription, not listening. Lines that did not agree were removed from
the character card.

| First model (small.en) | Link | Second model (medium.en), excerpt | Verdict |
|---|---|---|---|
| "I'm too poor. No money." | [2:07:07](https://youtu.be/5xL_7PGd3rk?t=7627) | "upgrades I can't I'm too poor No money Huh? Purchase the" | Agrees |
| "He's in the blender. He's in the blender. He's in the blender. He was in the blender." | [2:33:19](https://youtu.be/5xL_7PGd3rk?t=9199) | "He's in the blunder, he's in the blunder, he was in the blunder. Wait, I have to press it." | **Disagrees**: "blender" vs "blunder"; not quoted (described as a line repeated four times) |
| "Gimme gimme gimme gimme I don't care I don't care anymore." | [2:43:32](https://youtu.be/5xL_7PGd3rk?t=9812) | "Give me, give me, I don't care, I don't care anymore. Fine. Ah-hoo! Okay." | **Partly agrees**: "Gimme gimme…" vs "Give me, give me"; only "I don't care, I don't care anymore." is quoted |
| "Hi, everybody! What's up? How are you?" | [0:03:20](https://youtu.be/7vxLfdBqFac?t=200) | "to hear. Oh, hi everybody. What's up? How are you? Oh, dear. Oh," | Agrees on "…hi everybody. What's up? How are you?"; the second model also hears "Oh, hi." |
| "Oh dear. I guess I already started it, so I'm in the middle of it now." | [0:05:02](https://youtu.be/7vxLfdBqFac?t=302) | "Oh, dear. It's... I guess... I guess I already started it, so I'm in the middle of it now. Okay, I'm good." | Agrees (the second model repeats "I guess") |
| "Yippee, I love talking about myself. Yippee, yippee, hooray." | [0:05:43](https://youtu.be/7vxLfdBqFac?t=343) | "answer questions today yippee yippee. I love talking about myself yippee yippee. Hooray Um Yeah," | Agrees ("I love talking about myself… yippee yippee… hooray"; punctuation differs) |
| "Okay, are we ready? Are we bracing ourselves? We got our tissue box nearby." | [0:11:33](https://youtu.be/7vxLfdBqFac?t=693) | "enough um sorry okay are we ready are we bracing ourselves we got our tissue tissue box nearby okay and" | Agrees |
| "No, what am I, opinion, what am I, I'm a guardian of civilization! Uh, objectively, I decide everything for humanity, objectively." | [0:19:41](https://youtu.be/7vxLfdBqFac?t=1181) | "better, in my opinion. No, what am I, opinion? What am I, I'm guardian of civilization! Uh, objectively, I decide everything for humanity. Objectively, I think,…" | **Partly agrees**: "I'm a guardian" vs "I'm guardian"; quoted from "…guardian of civilization!" and "…I decide everything for humanity." |
| "Okay, I think I would win against Gura, Kiara, Iris, Narissa, and Mokoko." | [0:23:52](https://youtu.be/7vxLfdBqFac?t=1432) | "have no clue about. Okay, I think I would win against Gura, Kiarra, Iris, Narissa, and Mococo. I think" | Agrees (names spelled differently: Kiara/Kiarra, IRyS/Iris, Nerissa/Narissa, Mococo/Mokoko) |
| "Good job homo sapien." | [0:26:17](https://youtu.be/7vxLfdBqFac?t=1577) | "the human advantage good job homo sapien you guys ever" | Agrees |
| "I've never been scared of anything ever. I've never had a run from anything. Usually things run for me, so." | [0:26:39](https://youtu.be/7vxLfdBqFac?t=1599) | "true. I wonder. I've never been scared of anything ever. I've never had a run from anything. Usually things run from me, so... Oh yeah, in" | **Partly agrees**: "I've never been scared of anything ever" agrees; "things run for me" vs "run from me" differ, so only the first sentence is quoted |
| "I think I can move Beeboo into who I would lose against okay she is a rock" | [0:27:23](https://youtu.be/7vxLfdBqFac?t=1643) | "I would probably, I think I can move Beeboo into who I would lose against. Okay. She is a rock, this is true." | Agrees ("…I can move Beeboo [Biboo] into who I would lose against. Okay. She is a rock") |
| "unfortunately it looks like most of EN could beat me but um I have other skills and things that make me special so whatever" | [0:27:44](https://youtu.be/7vxLfdBqFac?t=1664) | "I don't know. Okay. Unfortunately it looks like most of Iain could beat me. But I have other skills and things that make me special, so whatever. Next question.…" | **Partly agrees**: "most of EN" vs "most of Iain"; "But I have other skills and things that make me special, so whatever" agrees and is quoted; the rest is paraphrased |
| "I think my answer's the best, but what do I know? everything" | [0:31:35](https://youtu.be/7vxLfdBqFac?t=1895) | "All right, I think I think my answer is the best, but what do I know? Everything." | **Partly agrees**: "answer's" vs "answer is"; quoted as "…but what do I know? Everything." |
| "Sometimes you go through life just not knowing stuff. You can't know everything." | [1:24:20](https://youtu.be/7vxLfdBqFac?t=5060) | "you. That's okay. Sometimes you go through life just not knowing stuff. You can't know everything, and sometimes you" | Agrees |
| "It's okay not to know stuff sometimes. Yeah, unless you're me. Exactly, unless you're me." | [1:24:35](https://youtu.be/7vxLfdBqFac?t=5075) | "how it is it's okay not to know stuff sometimes yeah unless you're me exactly unless you're me let me now" | Agrees |
| "Goodbye for now. I'll see you probably tomorrow, probably tomorrow. Okay, okay, bye-bye, bye-bye for now." | [1:31:02](https://youtu.be/7vxLfdBqFac?t=5462) | "send you over now. Okay, okay, okay, okay. Goodbye for now. I'll see you probably tomorrow. Probably tomorrow. Okay. Bye bye. Bye bye for" | **Partly agrees**: "Goodbye for now. I'll see you probably tomorrow, probably tomorrow." and "bye-bye for now" agree; the "okay, okay" before it differs |
| "Yowai. I am Yowai right now. I have the least damage in the game." | [0:40:29](https://youtu.be/zfQJZ6LetCc?t=2429) | "Uh oh. Yoai! Ahh. I am Yoai right now. I have the least damage in the game. Nooo! Oh no." | **Partly agrees**: the Japanese word is spelled "Yowai"/"Yoai" (the same word heard); "I have the least damage in the game." agrees |
| "Oh dear, that was pointless" | [0:52:11](https://youtu.be/zfQJZ6LetCc?t=3131) | "her! Grab her! Oh dear, that was pointless. Mira, behind! Oh" | Agrees |
| "Owie! Owie! Owie!" | [0:52:46](https://youtu.be/zfQJZ6LetCc?t=3166) | "to say annoying. Owie owie owie owie!" | Agrees |
| "I died happy!" | [0:58:18](https://youtu.be/zfQJZ6LetCc?t=3498) | "Ah, Riga! D'oh... I miss you! Kill" | **Not confirmed**: not in the second model's text; removed |

