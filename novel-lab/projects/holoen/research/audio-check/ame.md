# Audio check — Watson Amelia (2026-09-30)

Method: windows from the public stream archive archive.ragtag.moe (YouTube blocks this environment),
transcribed with faster-whisper small.en, pitch measured with Praat (100–600 Hz, word intervals only).
Tools and limits: `novel-lab/tools/audiocheck/README.md`. **This is not a listening check**: the audio was
machine-transcribed and acoustically measured, and the transcripts were reviewed in context. Lines used on
the character card were re-transcribed by a second model (whisper medium.en) and compared (see the end of
this file). Machine transcription drops some fillers and does not write screeches, hiccups or laughter
reliably. Game windows include game voices; only lines that are clearly hers are quoted.

## Windows measured

| Window | Stream | Segment | Speech (min) | Words | Words/min of speech | F0 median | F0 p10–p90 |
|---|---|---|---|---|---|---|---|
| time_travel | [【FALL GUYS】 I WANT TO GET A WIN #amelive #hololi](https://youtu.be/-M2BKL3KU9s) | [0:43:40–0:46:40](https://youtu.be/-M2BKL3KU9s?t=2620) | 1.3 | 132 | 97.9 | 257 Hz | 201–412 Hz |
| mario_full | [【Mario Osyssey】Let's Explore!](https://youtu.be/6VBQyNHxlR8) | [0:00:00–1:37:37](https://youtu.be/6VBQyNHxlR8?t=0) | 64.6 | 7969 | 123.4 | 248 Hz | 128–385 Hz |
| chat20_2024 | [【4 Years of AME】Happy 4 Years! YIPPIE ! ! Remini](https://youtu.be/OAmx8R0HuF4) | [0:40:00–1:00:00](https://youtu.be/OAmx8R0HuF4?t=2400) | 9.4 | 1074 | 113.8 | 267 Hz | 144–417 Hz |
| open2024 | [【4 Years of AME】Happy 4 Years! YIPPIE ! ! Remini](https://youtu.be/OAmx8R0HuF4) | [0:00:00–0:15:00](https://youtu.be/OAmx8R0HuF4?t=0) | 9.6 | 654 | 68.0 | 271 Hz | 152–408 Hz |
| valorant45 | [【VALORANT】Toxic Detective](https://youtu.be/OE-BmnlBKJ8) | [0:30:00–1:15:00](https://youtu.be/OE-BmnlBKJ8?t=1800) | 27.4 | 3634 | 132.7 | 276 Hz | 158–425 Hz |

"Words/min of speech" = words ÷ minutes inside whisper's speech segments (silence between segments
excluded). The 2024 opening window includes a pre-recorded intro, so its rate is low. The Mario stream was
transcribed in full; its low p10 pitch reflects game audio that slipped into word intervals.

## Claims checked

| Claim in the file | Result (in the machine transcript) | Evidence (ASR, archived audio) |
|---|---|---|
| Ground-pound mom joke (wiki A2, clip A5) | **Confirmed.** She reads the game's tutorial line aloud, makes the joke, then says "Sorry, it's late." | "Nothing beats a ground pound." [1:21:39](https://youtu.be/6VBQyNHxlR8?t=4899) → "That's funny cause uh, you guys know that's actually what I did to your mom last night." [1:21:41](https://youtu.be/6VBQyNHxlR8?t=4901) |
| Time-traveler identity as a bit | **Confirmed.** The Fall Guys reveal, and a later throwaway in Mario. | "you see this clock? … you guys can't tell anybody, but I'm actually a time traveler" [0:45:04](https://youtu.be/-M2BKL3KU9s?t=2704); "As a time traveler, I would know." [1:03:15](https://youtu.be/6VBQyNHxlR8?t=3795) |
| Salty when losing; "It's the ping!" | **Salt confirmed, ping excuse not detected.** In 45 minutes of VALORANT she blames her team and the game, rage-quits in words, and also owns a bad play. "Ping" appears only as the game marker ("I thought they pinged"). | "Why do my team die so fast?" [0:43:17](https://youtu.be/OE-BmnlBKJ8?t=2597); "Alright, I've had enough of this game. This game fucking sucks. It sucks. I'm done. I'm done." [1:00:33](https://youtu.be/OE-BmnlBKJ8?t=3633); "What's wrong with my team?" [1:13:47](https://youtu.be/OE-BmnlBKJ8?t=4427); "That was a bad play on my part." [1:14:44](https://youtu.be/OE-BmnlBKJ8?t=4484) |
| Swears when angry | **Confirmed, mostly in the shooter.** 14 swear words detected by the first model in about 3 hours of audio; most in VALORANT ("fucking sucks," "Shit," "Fuck, I don't know," "Holy shit, damn!"). Trash talk at chat. | "You guys are being so sassy in chat, but I bet I could 1v1 at least 80% of you and kick your ass." [0:44:49](https://youtu.be/OE-BmnlBKJ8?t=2689) |
| "Okay" as her most frequent filler | **Confirmed.** About 65 an hour across the windows (148 in the 98-minute Mario stream). | throughout |
| Stacks of thank-yous for superchats | **Confirmed.** 149 "thank you" in the Mario stream. | Mario stream, superchat sections |
| Audience address: "you guys" more than "chat" | **Confirmed.** "you guys" 51, "chat" 11 across the windows. | throughout |
| "Alright, bye-bye!" sign-off | **Confirmed** (2020). | "Okay, thank you for watching, I'll see you guys next time! Very soon, very soon. Okay, don't miss me too much, okay? Alright, bye-bye!" [1:37:03](https://youtu.be/6VBQyNHxlR8?t=5823) |
| Opener "hello hello hello" (A3, 2021 captions) | **Not detected in these windows.** The 2020 Mario stream opens "Good evening, hello, and welcome!"; the 2024 stream opens "Hello everybody!" after its intro. | [0:00:07](https://youtu.be/6VBQyNHxlR8?t=7); [0:41:51](https://youtu.be/OAmx8R0HuF4?t=2511) |
| "Fast-talking" | **Revised: middle pace.** 114–133 words per minute of speech, slower than Calli (161–186) and Kiara (133–179), faster than Ina (81–95). The stumbling comes from restarts and fillers. | table above |
| Light voice in the higher range | **Confirmed, relative.** Median F0 about 248–276 Hz, the upper group with Gura and Kiara (Kronii 177–188 Hz). | table above |
| Screech, hiccups, gremlin laugh, British bit | **Not checkable here.** Whisper does not write these sounds, and no British-accent bit fell in these windows. | — |

## New material (ASR-transcribed short lines)

Lines not listed in the second-model check at the end of this file are first-model transcriptions only.

- 2024 (her last regular period): "I'm four years old! I can barely talk!" [0:06:01](https://youtu.be/OAmx8R0HuF4?t=361);
  "I had to learn how to do so many things to make the intro." [0:06:37](https://youtu.be/OAmx8R0HuF4?t=397);
  "Yeah, quick maths, gains for your brains." [0:57:55](https://youtu.be/OAmx8R0HuF4?t=3475);
  "I'm gonna connect the world with my fist. I'm gonna connect the world by force."
  [0:58:16](https://youtu.be/OAmx8R0HuF4?t=3496)

- Caster-style narration while spectating a teammate: "Let's see if she can pull off a 1v4, full health.
  15 seconds left on the clock." [0:33:43](https://youtu.be/OE-BmnlBKJ8?t=2023)
- Cheering a teammate's ace: "Holy shit, damn! Nice! That was clutch."
  [0:39:37](https://youtu.be/OE-BmnlBKJ8?t=2377)
- Team blame with a question stack: "This game sucks! Why, you guys?" [1:08:00](https://youtu.be/OE-BmnlBKJ8?t=4080)
- Detective branding as a throwaway: "because my big detective brain I was able to fix the…"
  [0:11:10](https://youtu.be/6VBQyNHxlR8?t=670)
- 2024: the anniversary opens with a pre-recorded "special message, from small Amei, from the past!"
  [0:05:33](https://youtu.be/OAmx8R0HuF4?t=333)


## Second-model check (whisper medium.en)

Each line below was cut from the archived audio (a window of about 24–60 s around the first model's
timestamp) and transcribed again by a larger model. "Agrees" means the second model produced the same
words; it is still machine transcription, not listening. Lines that did not agree were removed from
the character card.

| First model (small.en) | Link | Second model (medium.en), excerpt | Verdict |
|---|---|---|---|
| "What I was telling you guys before is, you see this clock? you guys can't tell anybody but I'm actually a time traveler" | [0:45:04](https://youtu.be/-M2BKL3KU9s?t=2704) | "you know why the clock is there it's because you can't you guys can't tell anybody but i'm actually I'm actually a time traveler. Yeah I bet you guys" | **Partial (computed):** shared runs "you guys can't tell anybody but i'm actually" … "a time traveler" |
| "Bitch." | [0:50:03](https://youtu.be/6VBQyNHxlR8?t=3003) | "this area though that" | **Not confirmed** (second model: "A chick, is that a chick?"); removed |
| "As a time traveler, I would know." | [1:03:16](https://youtu.be/6VBQyNHxlR8?t=3796) | "dinosaurs have feathers. As a time traveler, I would know. What is that?" | **Shared span (computed):** whole line |
| "Nothing beats a ground pound. That's funny cause uh, you guys know that's actually what I did to your mom last night." | [1:21:39](https://youtu.be/6VBQyNHxlR8?t=4899) | "in the road nothing beats a ground pound that's funny because uh you guys know that's actually what i did to your mom last night sorry it's late" | **Partial (computed):** shared runs "nothing beats a ground pound that's funny" … "uh you guys know that's actually what i did to your mom last night" |
| "Alright, bye-bye!" | [1:37:11](https://youtu.be/6VBQyNHxlR8?t=5831) | "Okay. All right. Bye. Bye Bye" | Agrees ("All right. Bye. Bye bye") |
| "I'm four years old! I can barely talk!" | [0:06:01](https://youtu.be/OAmx8R0HuF4?t=361) | "by year, really. I'm four years old. I can barely talk. Yahoo! 6.9 out" | **Shared span (computed):** whole line |
| "I had to learn how to do so many things to make the intro." | [0:06:37](https://youtu.be/OAmx8R0HuF4?t=397) | "kind of did I had to learn how to do so many things to make the intro like I learned" | **Shared span (computed):** whole line |
| "I think this is lore that you've never heard before but I am like 95% sure that I was the one who brought up, like, having schedules." | [0:09:24](https://youtu.be/OAmx8R0HuF4?t=564) | "Alright, well, shall we start off strong with some karaoke already? I have a few songs. I mean, they're mostly songs you guys have heard before, I'm pretty sure…" | **Not located** (the window caught the lines after it); not used |
| "Yeah, quick maths, gains for your brains." | [0:57:55](https://youtu.be/OAmx8R0HuF4?t=3475) | "Waaahaha! Easy... Yeah, quick maths. Gains for your brains. Anyways... Umm... We" | **Shared span (computed):** whole line |
| "I'm gonna connect the world with my fist. I'm gonna connect the world by force." | [0:58:16](https://youtu.be/OAmx8R0HuF4?t=3496) | "world how about connect the world i'm gonna connect the world with my fist i'm gonna connect the world by force" | **Shared span (computed):** whole line |
| "Let's see if she can pull off a 1v4. Full health. 10, 15 seconds left on the clock." | [0:33:43](https://youtu.be/OE-BmnlBKJ8?t=2023) | "teapot. It's Raze again. Let's see if she can pull off a 1v4 full health. 15 seconds left on the clock, but bomb is" | Agrees (second model omits "10") |
| "Holy shit, damn! Nice! I was clutch." | [0:39:37](https://youtu.be/OE-BmnlBKJ8?t=2377) | "on our team! Holy shit, damn! Nice! That was clutch. Okay, I'm gonna..." | Agrees, except the second model hears "That was clutch" (first: "I was clutch"); the file uses "That was clutch." |
| "Why do my team die so fast?" | [0:43:17](https://youtu.be/OE-BmnlBKJ8?t=2597) | "Why do my team die so fast? How do they" | **Shared span (computed):** whole line |
| "You guys being so sassy in chat, but I bet I could 1v1 at least 80% of you and kick your ass." | [0:44:49](https://youtu.be/OE-BmnlBKJ8?t=2689) | "You guys are being so sassy in chat, but I bet I could 1v1 at least 80% of you and kick your ass. At least 80%." | Agrees (second model: "You guys are being so sassy"; the file uses that wording) |
| "Alright, I've had enough. This game fucking sucks. It sucks. I'm done. I'm done." | [1:00:33](https://youtu.be/OE-BmnlBKJ8?t=3633) | "can't leave early. Alright, I've had enough of this game. This game fucking sucks. It sucks! I'm done. I'm done." | Agrees (second model: "I've had enough of this game"; the file uses that wording) |
| "This game sucks! Why, guys?" | [1:08:00](https://youtu.be/OE-BmnlBKJ8?t=4080) | "This game sucks! Why, you guys? We keep" | Agrees (second model: "Why, you guys?") |
| "What's wrong with my team?" | [1:13:47](https://youtu.be/OE-BmnlBKJ8?t=4427) | "to push What what's wrong with my team why why how" | **Shared span (computed):** whole line |
| "That was a bad play on my part." | [1:14:44](https://youtu.be/OE-BmnlBKJ8?t=4484) | "That was a bad play on my part, that was a" | **Shared span (computed):** whole line |
