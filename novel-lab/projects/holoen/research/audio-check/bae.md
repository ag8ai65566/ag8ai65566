# Audio check — Hakos Baelz (2026-10-02)

Method: windows from the public stream archive archive.ragtag.moe (YouTube blocks this environment),
transcribed with faster-whisper small.en, pitch measured with Praat (100–600 Hz, word intervals only).
Tools and limits: `novel-lab/tools/audiocheck/README.md`. **This is not a listening check**: the audio was
machine-transcribed and acoustically measured, and the transcripts were reviewed in context. Lines used on
the character card were re-transcribed by a second model (whisper medium.en) and compared (see the end of
this file). Transcription does not write laughs reliably. Measurements describe the sampled recording and
ASR segmentation; game audio, music and other speakers prevent treating them as isolated vocal measurements.

All windows are from 2026 (117 minutes in total, about 1.95 hours, of which 30 minutes are mixed game audio). Only in-scope public performance material is used: long stretches of the April
chatting stream are about personal matters and are not quoted or summarized here. The Tomodachi Life window
mixes in game text-to-speech voices, which lifts its pitch figures; it is not used for voice measurements.

## Windows measured

| Window | Stream | Segment | Speech (min) | Words | Words/min of speech | F0 median | F0 p10–p90 |
|---|---|---|---|---|---|---|---|
| open2026chat | [≪JUST CHATTING≫ lil yaps + thanking supas with s](https://youtu.be/DOZ8rRVH03c) | [0:00:00–0:15:00](https://youtu.be/DOZ8rRVH03c?t=0) | 8.2 | 738 | 89.6 | 200 Hz | 147–333 Hz |
| chat30_2026 | [≪JUST CHATTING≫ lil yaps + thanking supas with s](https://youtu.be/DOZ8rRVH03c) | [0:30:00–1:00:00](https://youtu.be/DOZ8rRVH03c?t=1800) | 20.5 | 2727 | 133.3 | 212 Hz | 152–345 Hz |
| close2026chat | [≪JUST CHATTING≫ lil yaps + thanking supas with s](https://youtu.be/DOZ8rRVH03c) | [2:09:10–2:21:10](https://youtu.be/DOZ8rRVH03c?t=7750) | 7.4 | 912 | 123.1 | 233 Hz | 158–379 Hz |
| festalk30_2026 | [≪FES AFTER-TALK≫ hi :)](https://youtu.be/sPXphrWUOQU) | [0:20:00–0:50:00](https://youtu.be/sPXphrWUOQU?t=1200) | 22.8 | 2736 | 120.1 | 215 Hz | 157–358 Hz |
| game30_2026 | [≪Tomodachi Life: Living the Dream≫ ONE MORE RESI](https://youtu.be/2pn5_pZu8Q4) | [0:40:00–1:10:00](https://youtu.be/2pn5_pZu8Q4?t=2400) | 20.6 | 723 | 35.0 | 278 Hz | 125–505 Hz |

"Words/min of speech" = words ÷ minutes inside whisper's speech segments.

## Claims checked

| Claim in the file | Result (in the machine transcript) | Evidence (ASR, archived audio) |
|---|---|---|
| Self-introduction "Wazzup! I am Chaos the end of ends, a steel rose trapped in a cage of ice…" (HB2) | **Present but garbled** in the first model at the April 2026 opening; kept from the wiki, not quoted from audio. | [0:04:46](https://youtu.be/DOZ8rRVH03c?t=286) |
| Thanks gifts with a rhythmic patter | **Recurring** (first-model counts, not a certified quotation): about 38 "boom" runs and 128 "thank you so much" in about an hour of chat. | [0:32:29](https://youtu.be/DOZ8rRVH03c?t=1949) |
| "You're doing great!" (HB2) | **Confirmed** as encouragement to a viewer. | [0:58:39](https://youtu.be/DOZ8rRVH03c?t=3519) |
| "Febaerary" every year | **Confirmed**: "This year was my fifth…" (the coined word is misheard by both models). | [0:33:20](https://youtu.be/DOZ8rRVH03c?t=2000) |
| Swearing | **Moderate and casual**: "hell yeah" is a shared span; "damn," "God damn it," a joking "bitch" at a fictional rival, "bruh" and "frickin'" are first-model observations. | [2:11:57](https://youtu.be/DOZ8rRVH03c?t=7917) |
| Speech rate | The three chat windows span about 89.6–133.3 words per ASR speech-minute; run-on storytelling. This does not establish perceived speed or loudness. | — |
| 2026 fes stages (her own account) | **Her account**: the final solo number of STAGE 3 ("Idol," her own choreography ending in a breakdance) and "Kakumei Dualism" with Natsuiro Matsuri (she took the T.M.Revolution part, "Bae Aniki"); a venue talk with Cecilia where they "continued the coffee and tea debate." | [0:31:24](https://youtu.be/sPXphrWUOQU?t=1884), [0:36:03](https://youtu.be/sPXphrWUOQU?t=2163), [0:24:27](https://youtu.be/sPXphrWUOQU?t=1467) |
| Collab with Cecilia (2026) | **Confirmed**: Resident Evil "nine" continued on Cecilia's channel. | [2:19:23](https://youtu.be/DOZ8rRVH03c?t=8363) |
| The mock rival-feud bit | **Confirmed**: a mock feud with an "artist" (name garbled by both models) whose claim hit her stream after her own new song. | [2:12:26](https://youtu.be/DOZ8rRVH03c?t=7946) |

## Second-model check (whisper medium.en)

Each line below was cut from the archived audio (a window of about 24–60 s around the first model's
timestamp) and transcribed again by a larger model. Cards may quote only the shared spans. Speaker attribution
rests on the stream itself (a solo stream on her own channel; viewers' superchats she reads aloud are not
attributed to her and are not quoted).

| First model (small.en) | Link | Second model (medium.en), excerpt | Verdict |
|---|---|---|---|
| "It was sabotage" | [0:06:53](https://youtu.be/DOZ8rRVH03c?t=413) | "One of these days the alarm will work. It was sabotage. Sabotage. Anyway, I know what you're talking about. Nothing happened this morning. What? Falsely accused. I was only trying to" | **Shared span (computed):** whole line |
| "They hate me. They hate me" | [0:07:56](https://youtu.be/DOZ8rRVH03c?t=476) | "How did you manage to get a low school than be sabotage I hate me" | **Disagrees**; not used |
| "They hate promise. They hate us. It's a conspiracy" | [0:08:27](https://youtu.be/DOZ8rRVH03c?t=507) | "All the promise have the exact same. They hate promise. They hate us. It's a conspiracy. Welcome to the stream, by the way, um, I have some food and some coffee and we're just gonna chill. We're gonna chat. And then, I have a couple of, um..." | **Shared span (computed):** whole line |
| "I may be dead" | [0:30:45](https://youtu.be/DOZ8rRVH03c?t=1845) | "Does that mean the next time you stream is the weekend? I don't know if I'm streaming on the weekend. I maybe did. I maybe did. I think the next time I'm streaming will be on Friday, cause CC and I are going to be continuing Resident Evil 9 Friday evening." | **Disagrees** ("I maybe did"); not used |
| "Five years! Has it been five years? Oh my god it is." | [0:33:20](https://youtu.be/DOZ8rRVH03c?t=2000) | "Thank you so much. Five years! Has it been five years? Oh my god, it is. This year was my fifth for Bairi." | **Shared span (computed):** whole line |
| "This year was my fifth for berry." | [0:33:25](https://youtu.be/DOZ8rRVH03c?t=2005) | "five years has it been five years oh my god it is oh this year was my fifth for berry that's crazy i've been watching you for half a" | **Shared span (computed):** whole line |
| "oh my gosh oh my gosh ew not ew at you just ew at the passage of time" | [0:33:43](https://youtu.be/DOZ8rRVH03c?t=2023) | "That's crazy Been watching you for half a decade. Oh my gosh. Oh My gosh You" | **Disagrees**; not used |
| "Welcome to the Rat Pack, welcome, welcome." | [0:42:50](https://youtu.be/DOZ8rRVH03c?t=2570) | "Welcome to the Rat Pack! Welcome, welcome. Oh, I should do a membership stream." | **Shared span (computed):** whole line |
| "everything gets better if you're at the bottom you can only go up you're doing great" | [0:58:39](https://youtu.be/DOZ8rRVH03c?t=3519) | "life and end up falling down this rabbit hole. Enjoying your singing, dancing and sometimes gaming skills. Hope everything goes your way. Thank you so much. Everything gets better. If you're at the bottom, you can only go up. You're doing great. Umm, Uvidredna thank you so much." | **Shared span (computed):** whole line |
| "Here I am trying to promote her new song. What does she do claim my video?" | [2:12:26](https://youtu.be/DOZ8rRVH03c?t=7946) | "she's jealous here i am trying to promote her new song and what does she do claim my video new beef bae vs hikki's bells yo that bae situation is crazy have you heard about the beef between bae and" | **Partial (computed):** shared runs "here i am trying to promote her new song" … "what does she do claim my video" |
| "Does she really think that me, of all people, is trying to clout chase by using her?" | [2:13:07](https://youtu.be/DOZ8rRVH03c?t=7987) | "a success i'm just trying to promote her new song does she really think that me of all people is trying to clout chase by using her breaking news bae is trying to clout chase by by by using hey kospels" | **Shared span (computed):** whole line |
| "Breaking news! Bae is trying to clout chase by using hackel spells." | [2:13:16](https://youtu.be/DOZ8rRVH03c?t=7996) | "Is trying to clout chase by using her Breaking news bae is trying to clout chase by by by using hey cos bill That's the new drama, oh my god, how mother thank you so much take off spells is just okay" | **Partial (computed):** shared runs "breaking news bae is trying to clout chase by" |
| "My next video is just exposing Heiko's spells" | [2:14:57](https://youtu.be/DOZ8rRVH03c?t=8097) | "Scandalous. My next video is just exposing Heiko's Bells." | **Partial (computed):** shared runs "my next video is just exposing heiko's" |
| "Please stream my newest song, Snake Eyes, and also my newest cover, Liar Dancer, if you haven't already." | [2:19:11](https://youtu.be/DOZ8rRVH03c?t=8351) | "[out-of-scope material omitted] Please stream my newest song snake eyes and also my newest cover light dancer if you haven't already I really like it. It's really really cute Thank you so much, I'll see you guys on Friday on CC's channel" | **Partial (computed):** shared runs "please stream my newest song snake eyes and also my newest cover" … "dancer if you haven't already" |
| "I'll see you guys on Friday on CC's channel. We're going to be continuing resident evil nine." | [2:19:23](https://youtu.be/DOZ8rRVH03c?t=8363) | "already. I really like it. It's really, really cute. Thank you so much. I'll see you guys on Friday on CC's channel. We're going to be continuing Resident Evil 9. Very fun. [out-of-scope material omitted]" | **Partial (computed):** shared runs "i'll see you guys on friday on cc's channel we're going to be continuing resident evil" |
| "Okey dokey, [out-of-scope material omitted] Bye-bye!" | [2:19:56](https://youtu.be/DOZ8rRVH03c?t=8396) | "Maybe not Koseki Bijou! Let's go say hi to Koseki Bijou. Okey-dokey [out-of-scope material omitted] Bye bye!" | **Partly agrees**: only "okey dokey" and "bye-bye" are shared (two-word runs); not quoted as a line |
| "What do we do? We had we continued the coffee and tea debate" | [0:24:27](https://youtu.be/sPXphrWUOQU?t=1467) | "stream it was like a live quote-unquote live stream with the people there what do we do we we had we continued the coffee and tea debate they're got attacked live by cc the venue exclusive event but" | **Partial (computed):** shared runs "what do we do we" … "had we continued the coffee and tea debate" |
| "So you see only cause me senpai when she wants me wants me to do something for her" | [0:26:03](https://youtu.be/sPXphrWUOQU?t=1563) | "Together she was like, are you sure? Thank you senpai CC only calls me senpai when she wants me wants me to do something for her Oh when she needs help And it works." | **Partial (computed):** shared runs "me senpai when she wants me wants me to do something for her" |
| "Technology be crazy." | [0:29:49](https://youtu.be/sPXphrWUOQU?t=1789) | "the new thing how was the truck it was crazy your technology crazy technology be crazy i don't know if you guys noticed watching the stream but with the box um it's it's it's two-sided you know so like in this frame su and i are facing one side and then miko and noida senpai facing the other side but in middle it's" | **Shared span (computed):** whole line |
| "They decided to put me as the final solo act this year. When I found out, guys, I was so stressed." | [0:31:24](https://youtu.be/sPXphrWUOQU?t=1884) | "and time skip forward what, like two hours? Because for some reason they decided to put me as the final solo act this year. When I found out guys, I was so stressed. I was so stressed. So it was, okay, we'll talk about that later. But first I had my unit song with Matsuri Senpai." | **Shared span (computed):** whole line |
| "yeah I was bey aniki hell yeah" | [0:36:03](https://youtu.be/sPXphrWUOQU?t=2163) | "Did you take the Team Revolution parts? Yeah! I was bae aniki, hell yeah. Man." | **Partial (computed):** shared runs "yeah i was" … "aniki hell yeah" |
| "Okay, I guess I'm doing this now confused rat" | [0:38:05](https://youtu.be/sPXphrWUOQU?t=2285) | "and then suddenly my call and response was decided for me and I was like oh okay I guess I'm doing this now Confused rat" | **Shared span (computed):** whole line |
| "I know, sue me, okay? I'm sorry. I still haven't watched Osinoko, I'm sorry." | [0:42:42](https://youtu.be/sPXphrWUOQU?t=2562) | "before me so thank you so much um i know sue me okay i'm sorry i still haven't watched oshinoko i'm sorry now i had so many things this has been in planning for ever since last fest which normally is what happens i do one fest" | **Partial (computed):** shared runs "i know sue me okay i'm sorry i still haven't watched" |
| "a lot of people have been making jokes that eventually I'm just gonna start breakdancing on stage" | [0:43:15](https://youtu.be/sPXphrWUOQU?t=2595) | "to level up somehow and i know ever since from debut a lot of people have been making jokes that eventually i'm just gonna start breakdancing on stage and i also was treating it as a joke and then it suddenly became not a joke i have started i started" | **Shared span (computed):** whole line |
| "And I also was treating it as a joke and then it suddenly became not a joke" | [0:43:22](https://youtu.be/sPXphrWUOQU?t=2602) | "A lot of people have been making jokes that eventually I'm just gonna start breakdancing on stage And I also was treating it as a joke and then it suddenly became not a joke I have started I started breakdancing lessons everyone. Oh my god" | **Shared span (computed):** whole line |
| "Why would you want the peak of that to be at the end of the performance? Who would think that's a good idea? Me" | [0:49:19](https://youtu.be/sPXphrWUOQU?t=2959) | "song when you're already tired and you're out of out of just out of power you're tired your muscles are dead everything's dead why would you want the peak of that to be at the end of the performance me who would think that's a good idea me these were the two quote unquote i think i will consider them problems because one I've never choreographed idle step before" | **Partial (computed):** shared runs "why would you want the peak of that to be at the end of the performance" … "who would think that's a good idea me" |
| "My name is Koseki Bijuu" | [0:50:30](https://youtu.be/2pn5_pZu8Q4?t=3030) | "Yay! KA-SEK-I-ME-JU! Whoa!" | **Disagrees** (game text-to-speech and a name being typed); not used |
| "Should've picked a big one. God dammit." | [1:01:40](https://youtu.be/2pn5_pZu8Q4?t=3700) | "I got a marble what was that should pick the big one god damn it all righty oh hello sorry what is going on See you soon." | **Disagrees** ("should pick the big one god damn it"); not used |
| "Here I am trying to promote her new song, and what does she do? Claim my video" | [2:12:26](https://youtu.be/DOZ8rRVH03c?t=7946) | "Here I am trying to promote her new song and what does she do claim my video" | Agrees (two-model recheck by Claude, 2026-10-04: small.en and medium.en share these words in the same window; the speaker is the streamer on her own solo stream) |

## Review note (2026-10-02)
GPT's one-round claim check flagged personal material in the second-model excerpts at 2:19:11, 2:19:23 and
2:19:56; those portions are replaced with "[out-of-scope material omitted]". The rival's name is not spelled
because both models garble it.
