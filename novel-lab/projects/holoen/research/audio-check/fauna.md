# Audio check — Ceres Fauna (2026-10-01)

Method: windows from the public stream archive archive.ragtag.moe (YouTube blocks this environment),
transcribed with faster-whisper small.en, pitch measured with Praat (100–600 Hz, word intervals only).
Tools and limits: `novel-lab/tools/audiocheck/README.md`. **This is not a listening check**: the audio was
machine-transcribed and acoustically measured, and the transcripts were reviewed in context. Lines used on
the character card were re-transcribed by a second model (whisper medium.en) and compared (see the end of
this file). Machine transcription drops some fillers and does not write giggles or "uuuu" reliably, and
small.en can turn Japanese speech into English words. The horror window includes game dialogue that she
reads aloud in character voices; only lines that are clearly her own are quoted.

All windows are from autumn 2024, her last active period before she graduated on 2025-01-03, which this
project weights highest. Stories told in these windows about her family, school, diet and driving are
outside the project's scope and are not used. A members-only window was transcribed by mistake and then
set aside unused (members content is not public).

## Windows measured

| Window | Stream | Segment | Speech (min) | Words | Words/min of speech | F0 median | F0 p10–p90 |
|---|---|---|---|---|---|---|---|
| worldtree30_2024 | [【MINECRAFT】 The world tree isn't gonna build its](https://youtu.be/14S18Ykq0_w) | [1:00:00–1:30:00](https://youtu.be/14S18Ykq0_w?t=3600) | 24.1 | 2879 | 119.6 | 293 Hz | 209–435 Hz |
| horror45_2024 | [【Mouthwashing】 The strange, unsettling horror ga](https://youtu.be/9_Ue4fOMNP8) | [1:00:00–1:45:00](https://youtu.be/9_Ue4fOMNP8?t=3600) | 37.5 | 3453 | 92.2 | 306 Hz | 234–430 Hz |
| supers30_2024 | [chatting and super catchup!](https://youtu.be/TzW6VRf4KjQ) | [0:30:00–1:00:00](https://youtu.be/TzW6VRf4KjQ?t=1800) | 23.8 | 2504 | 105.1 | 289 Hz | 124–432 Hz |
| chat40_2024 | [the first solo fauna stream in 8,000 years](https://youtu.be/iIBywcAIMD0) | [0:40:00–1:20:00](https://youtu.be/iIBywcAIMD0?t=2400) | 28.2 | 3364 | 119.2 | 283 Hz | 126–439 Hz |
| close2024 | [the first solo fauna stream in 8,000 years](https://youtu.be/iIBywcAIMD0) | [3:16:55–3:28:55](https://youtu.be/iIBywcAIMD0?t=11815) | 8.5 | 1318 | 154.3 | 280 Hz | 126–444 Hz |
| open2024 | [the first solo fauna stream in 8,000 years](https://youtu.be/iIBywcAIMD0) | [0:00:00–0:15:00](https://youtu.be/iIBywcAIMD0?t=0) | 13.1 | 1420 | 108.1 | 300 Hz | 225–447 Hz |

"Words/min of speech" = words ÷ minutes inside whisper's speech segments (silence between segments
excluded). About 2.9 hours in all. In the chat, superchat and closing windows p10 drops near 125 Hz
(noise and game or music frames); the cleaner windows run about 210–445 Hz.

## Claims checked

| Claim in the file | Result (in the machine transcript) | Evidence (ASR, archived audio) |
|---|---|---|
| Official greeting "Konfauna~ Your gaming idol kirin Ceres Fauna is here!" (F1) | **Not detected in this window.** The stream opens mid-setup with soft hellos while she fixes her background music. | [0:00:00](https://youtu.be/iIBywcAIMD0?t=0) |
| Soft-spoken (F1, F2) | **Confirmed in her own words.** "I'm pretty soft-spoken. And talking in my head voice like this does not strain my voice at all." | [1:14:21](https://youtu.be/iIBywcAIMD0?t=4461) |
| Pitch | **Measured: high in this project's samples.** Median 280–306 Hz across six windows, near Kiara's (245–300 Hz) and above IRyS's (214–226 Hz). Sample results, not a ranking. | table above |
| Unhurried pace | **Confirmed.** 105–120 words per minute of speech in chat and building, 92 in the horror game; the exception is the closing superchat list (154). | table above |
| Fillers "like," "I don't know," "I guess" | **Confirmed.** "I don't know" 60 times in 14,938 words (17 in the 40-minute chat window); "like" 288 (about 1 in 40 in chat, 1 in 30 while building); "I guess" 27; "kind of" 18. | throughout |
| Rarely swears | **Confirmed.** Her own words: "dang," "what the heck," "oh my gosh." The "damn it" and the one strong swear in the horror window are game lines she reads aloud. | [1:26:25](https://youtu.be/9_Ue4fOMNP8?t=5185); [1:42:31](https://youtu.be/9_Ue4fOMNP8?t=6151) |
| Scared reactions murmured, not shouted | **Confirmed.** "oh no" 8 times and "oh gosh" 5 in 45 minutes of Mouthwashing, at the same median pitch as chat. | throughout the horror window |
| Reads game dialogue aloud in character voices | **Confirmed (new).** The horror window is full of the game's lines read in voices, between her own reactions. | [1:00:00–1:45:00](https://youtu.be/9_Ue4fOMNP8?t=3600) |
| "Fauna Standard Time," lateness bit | **Confirmed.** "…we will be back to Fauna Standard Time. I promise." and, celebrating a milestone late, "I'm always on time." | [3:27:56](https://youtu.be/iIBywcAIMD0?t=12476); [0:46:20](https://youtu.be/iIBywcAIMD0?t=2780) |
| Spells and Fauna Mart during superchats | **Confirmed.** "If you heard your name, you will now be the recipient of my next spell"; "It's not a scam! Fauna Mart is real!" | [0:45:36](https://youtu.be/TzW6VRf4KjQ?t=2736); [0:49:09](https://youtu.be/TzW6VRf4KjQ?t=2949) |
| Superchats as rapid lists of names | **Confirmed.** 62 "thank you"s in the 12-minute closing window; a sung "Happy Birthday" for a Sapling's birthday; a "Plant them, plant them…" chant after a list. | [3:21:39](https://youtu.be/iIBywcAIMD0?t=12099); [0:45:26](https://youtu.be/TzW6VRf4KjQ?t=2726) |
| Japanese in superchats | **Detected.** "Arigatou gozaimasu. Thank you." (second model); "arigato" (first model). | [0:49:09](https://youtu.be/TzW6VRf4KjQ?t=2949) |
| "Return to nature," "uuuu," "Evil Fauna" (F2) | **Not detected in these windows.** Kept from the wiki (secondary). | — |

## New material (ASR-transcribed short lines)

Lines not listed in the second-model check at the end of this file are first-model transcriptions only.

- When something called her a "gaming idol giraffe": "I was like, oh, am I supposed to be a giraffe? … I
  was ready to be a kirin because that's what I am. But if they need me to be a giraffe, I guess I can do
  that" [0:55:48](https://youtu.be/iIBywcAIMD0?t=3348)
- Grand deadpan: "I will be the sole arbitrator of YouTube monetization." [0:42:06](https://youtu.be/iIBywcAIMD0?t=2526)
- Refusing a Sapling's request: "So how can you guys get a jet pack if I don't even have one? I am not the
  keeper of jet packs." [3:24:38](https://youtu.be/iIBywcAIMD0?t=12278)
- On a murder-mystery collab: "I just wanted to use the gun… it would be dramatic and funny."
  [3:20:24](https://youtu.be/iIBywcAIMD0?t=12024)
- Choosing a role in a game: "Me. I'll be the mean manager." [0:55:28](https://youtu.be/TzW6VRf4KjQ?t=3328)
- A flat, fake laugh at her own pun ("Ha ha, I'm so…"; the pun word differs between models).
  [1:12:53](https://youtu.be/iIBywcAIMD0?t=4373)

## Second-model check (whisper medium.en)

Each line below was cut from the archived audio (a window of about 24–60 s around the first model's
timestamp) and transcribed again by a larger model. "Agrees" means the second model produced the same
words; it is still machine transcription, not listening. Lines that did not agree were removed from
the character card.

| First model (small.en) | Link | Second model (medium.en), excerpt | Verdict |
|---|---|---|---|
| "Plant them, plant them, got them, plant them all, sapling wrap." | [0:45:26](https://youtu.be/TzW6VRf4KjQ?t=2726) | "S, Tash, fool. Plant them, plant them, got them, plant them all, got them, plant them all," | Agrees (a chant; only "Plant them, plant them…" is quoted) |
| "If you heard your name, you will now be the recipient of my next spell, which will make you want to spend money at Fauna Mart" | [0:45:36](https://youtu.be/TzW6VRf4KjQ?t=2736) | "Am I hexing you? Yes. If you heard your name, you will now be the recipient of my next spell. Which will make you want to spend money at Fauna Martins. Which" | **Partly agrees**: the first sentence agrees; the shop name differs ("Fauna Mart" vs "Fauna Martins"), so the rest is paraphrased |
| "It's not a scam! Fauna Mart is real. It's not a scam!" | [0:49:09](https://youtu.be/TzW6VRf4KjQ?t=2949) | "It's not a scam! Fauna Mart is real! Is that what you're going for? Because" | Agrees |
| "Me. I'll be the mean manager" | [0:55:28](https://youtu.be/TzW6VRf4KjQ?t=3328) | "mean manager, though? Me. I'll be the mean manager. But the answer" | Agrees |
| "Send it directly into my brain. I will be the sole arbitrator of YouTube monetization." | [0:42:06](https://youtu.be/iIBywcAIMD0?t=2526) | "the YouTube oxcord send it directly into my brain and I will be the sole arbitrator of YouTube monetization three seconds" | Agrees on the shared spans ("send it directly into my brain" / "I will be the sole arbitrator of YouTube monetization"); only the second is quoted |
| "It's okay. We can celebrate 900,000. I'm always on time." | [0:46:20](https://youtu.be/iIBywcAIMD0?t=2780) | "of the doubt that I was right on time. It's okay. We can celebrate. Nine hundred thousand." | **Partly agrees**: the number differs ("900,000" vs "Nine hundred thousand. Nine hundred and four thousand"); quoted as "It's okay. We can celebrate… I'm always on time." |
| "I was like, oh, am I supposed to be a giraffe?" | [0:55:48](https://youtu.be/iIBywcAIMD0?t=3348) | "said giraffe. And I was like, oh, am I supposed to be a giraffe? And I was" | Agrees |
| "I was ready to be a Kirin because that's what I am. But if they need me to be a giraffe, I guess I can do that" | [0:56:02](https://youtu.be/iIBywcAIMD0?t=3362) | "gonna be like i was i was ready to be a kieran because that's what i am but if they need me to be a giraffe i guess i can do that gaming" | Agrees (the second model spells kirin "kieran"; its full text continues "…but if they need me to be a giraffe i guess i can do that") |
| "Ha ha, I'm so humerus, ha ha ha ha ha." | [1:12:53](https://youtu.be/iIBywcAIMD0?t=4373) | "go. Just kidding. Ha ha, I'm so humorous, ha ha ha ha ha ha. Okay, let" | **Partly agrees**: the pun word differs ("humerus" vs "humorous"); described, not quoted |
| "And I think I'm lucky that, well, I'm pretty soft spoken. And talking in my head voice like this does not strain my voice at all." | [1:14:21](https://youtu.be/iIBywcAIMD0?t=4461) | "i don't know and i think i'm lucky that well i'm pretty soft-spoken and talking in my head voice like this does not strain my voice at all i can pretty much" | Agrees |
| "Also. I just wanted to use the gun cuz it would be dramatic and funny" | [3:20:24](https://youtu.be/iIBywcAIMD0?t=12024) | "had no choice. Also, I just wanted to use the gun because it would be dramatic and funny. Even if I" | **Partly agrees**: "cuz"/"because" differ; quoted as "I just wanted to use the gun… it would be dramatic and funny" |
| "So how can you guys get a jet pack if I don't even have one? I am not the keeper of jet packs." | [3:24:38](https://youtu.be/iIBywcAIMD0?t=12278) | "stealing their answer? I don't have a jetpack So, how can you guys get a jetpack if I don't even have one I am NOT the keeper of jetpacks" | Agrees (the second model writes "jetpack(s)" and stresses "NOT") |
| "We'll see you tomorrow for the race, and then eventually we will be back to Fauna Standard Time. I promise. Thank you so much for hanging out, and I will see you tomorrow." | [3:27:56](https://youtu.be/iIBywcAIMD0?t=12476) | "hanging out today i will see you tomorrow for the race and then eventually we will be back to fauna standard time i promise thank you so much for hanging out an…" | Agrees on "…we will be back to Fauna Standard Time. I promise. Thank you so much for hanging out, and I will see you tomorrow." |
| "Wish me luck. Bye!" | [3:28:14](https://youtu.be/iIBywcAIMD0?t=12494) | "will see you tomorrow. Wish me luck. I'm gonna practice" | **Partly agrees**: "Wish me luck." agrees; "Bye!" is not in the second model (it continues "I'm gonna practice…"), so only "Wish me luck." is quoted |

