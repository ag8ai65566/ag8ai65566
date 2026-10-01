# Audio check — Elizabeth Rose Bloodflame (2026-10-01)

Method: windows from the public stream archive archive.ragtag.moe (YouTube blocks this environment),
transcribed with faster-whisper small.en, pitch measured with Praat (100–600 Hz, word intervals only).
Tools and limits: `novel-lab/tools/audiocheck/README.md`. **This is not a listening check**: the audio was
machine-transcribed and acoustically measured, and the transcripts were reviewed in context. Lines used on
the character card were re-transcribed by a second model (whisper medium.en) and compared (see the end of
this file). Transcription does not write laughs reliably. Measurements describe the sampled recording and
ASR segmentation; game audio, music and other speakers prevent treating them as isolated vocal measurements.

The 2026 windows are Tomodachi Life (where Mii characters speak with text-to-speech and she voices them too)
and a Monster Hunter Stories 3 trial (voiced cutscenes she reads along with); their pitch figures are mixed.
The 2025 3D-showcase after-party chat is her cleanest sample. An archived 2025 "RABBIT" chat (gs8QtnwImyc)
returned 404 and was replaced by the after-party.

## Windows measured

| Window | Stream | Segment | Speech (min) | Words | Words/min of speech | F0 median | F0 p10–p90 |
|---|---|---|---|---|---|---|---|
| open2026 | [【 TOMODACHI LIFE】Big M'lord Island ~! 💄](https://youtu.be/LTPi3UtR7pw) | [0:00:00–0:15:00](https://youtu.be/LTPi3UtR7pw?t=0) | 10.7 | 1056 | 98.7 | 201 Hz | 141–367 Hz |
| chat30_2025 | [【 3D SHOWCASE 】After Party Chit Chat! ~ 💄#ERB3D ](https://youtu.be/Rk03Rh8P9ps) | [0:20:00–0:50:00](https://youtu.be/Rk03Rh8P9ps?t=1200) | 25.7 | 2798 | 109.1 | 183 Hz | 140–297 Hz |
| game30b_2026 | [【Monster Hunter Stories 3: Twisted Reflection Tr](https://youtu.be/sL8WXMMEiCw) | [1:00:00–1:30:00](https://youtu.be/sL8WXMMEiCw?t=3600) | 20.5 | 2550 | 124.2 | 194 Hz | 129–387 Hz |
| close2026 | [【 TOMODACHI LIFE】Big Miilord Island Episode 3 ~!](https://youtu.be/vGKcRSrLTuk) | [2:51:22–3:01:22](https://youtu.be/vGKcRSrLTuk?t=10282) | 5.4 | 468 | 86.9 | 226 Hz | 153–373 Hz |
| game30_2026 | [【 TOMODACHI LIFE】Big Miilord Island Episode 3 ~!](https://youtu.be/vGKcRSrLTuk) | [1:00:00–1:30:00](https://youtu.be/vGKcRSrLTuk?t=3600) | 17.1 | 1923 | 112.6 | 208 Hz | 143–371 Hz |

"Words/min of speech" = words ÷ minutes inside whisper's speech segments.

## Claims checked

| Claim in the file | Result (in the machine transcript) | Evidence (ASR, archived audio) |
|---|---|---|
| "Lovely to see you, to see you lovely" (EB2, EB4) | **Confirmed** in a 2026 sign-off with "let my voice be your strength" and "Huzzah!" | [2:58:52](https://youtu.be/vGKcRSrLTuk?t=10732) |
| Rarely swears (EB2) | **Consistent.** Minced oaths ("What the frick?", "What the frig", "freaking/friggin'"); her show bit says "Please do not swear." | [2:54:30](https://youtu.be/vGKcRSrLTuk?t=10470); [0:01:21](https://youtu.be/LTPi3UtR7pw?t=81) |
| British slang | **Confirmed.** "Soz," "bits and bobs," "for funsies," "willy-nilly," "whilst," "Fancies!" | [0:06:55](https://youtu.be/LTPi3UtR7pw?t=415); [0:30:40](https://youtu.be/Rk03Rh8P9ps?t=1840) |
| Singing at the heart (EB1, EB2) | **Confirmed.** "I sing too much everywhere I go, there's always Liz noises"; "singing is good for the soul." | [0:20:07](https://youtu.be/Rk03Rh8P9ps?t=1207) |
| Arranges and directs her own stages | **Confirmed (new).** She arranged "Giri Giri" as a duet for Vestia Zeta, choreographed and taught it, and directed most of her 3D showcase. | [0:28:09–0:30:11](https://youtu.be/Rk03Rh8P9ps?t=1689) |
| Nerissa bit | **Confirmed (new, performed bit).** "She's been calling me her husband, my husband. She's very sweet." | [0:38:00](https://youtu.be/Rk03Rh8P9ps?t=2280) |
| Pitch | **Measured:** the after-party chat median about 183 Hz, p10–p90 about 140–297 Hz; game windows 194–226 Hz are mixed. Not a ranking. | table above |

## New material (ASR-transcribed short lines)

Lines not listed in the second-model check at the end of this file are first-model transcriptions only.

- Testing a Mii's voice: "My name is Pebble. It's nice to meet you." (the game's text-to-speech; not used). [1:01:42](https://youtu.be/vGKcRSrLTuk?t=3702)
- "Oh my blush is strong. Rudy, do you think I put too much blush on today? Don't answer." [1:03:32](https://youtu.be/sL8WXMMEiCw?t=3812)
- "I see what you did there." (to a pun in the game) [1:03:18](https://youtu.be/sL8WXMMEiCw?t=3798)

## Second-model check (whisper medium.en)

Each line below was cut from the archived audio (a window of about 24–60 s around the first model's
timestamp) and transcribed again by a larger model. "Agrees" means the second model produced the same
words; it is still machine transcription, not listening. Lines that did not agree were removed from
the character card.

| First model (small.en) | Link | Second model (medium.en), excerpt | Verdict |
|---|---|---|---|
| "You're live on FTV!" | [0:01:15](https://youtu.be/LTPi3UtR7pw?t=75) | "Hello. You're live on EarpTV. Please do" | **Channel name differs** ("FTV" / "EarpTV"); only "You're live on…" is quoted |
| "Soz game." | [0:06:55](https://youtu.be/LTPi3UtR7pw?t=415) | "it lie idle Soz game Okay, oh my" | **Shared span (computed):** whole line |
| "That's adorable. I like that. Aww. That is cute. Let's put the bits and bobs in the wishing fountain" | [0:11:52](https://youtu.be/LTPi3UtR7pw?t=712) | "Oh, it's cute. That is adorable. I like that. Oh, that is cute. Let's put the bits and bobs in the wishing phone. Wow." | Agrees on "bits and bobs" |
| "Let's have a look at the prizes." | [0:12:20](https://youtu.be/LTPi3UtR7pw?t=740) | "Rank 6 Oh! Two wishes Have a look at the prezzies Street dance," | **"prezzies" second model only**; only "Let's have a look" used |
| "I sing too much everywhere I go there's always Liz noises" | [0:20:07](https://youtu.be/Rk03Rh8P9ps?t=1207) | "all the time I sing too much everywhere I go there's always Liz noises in the-" | **Shared span (computed):** whole line |
| "I think singing is good for the soul" | [0:20:34](https://youtu.be/Rk03Rh8P9ps?t=1234) | "Singing everywhere. But I always think singing is good for the soul or at" | **Partial (computed):** shared runs "think singing is good for the soul" |
| "I want dance fighting I want it to be very cool" | [0:22:13](https://youtu.be/Rk03Rh8P9ps?t=1333) | "I was like, I want dance fighting. I want it to be very cool. And then I" | **Shared span (computed):** whole line |
| "Bobby is the best. Bobby! He's forgiven. He's so cute. He's a cheeky guy." | [0:24:00](https://youtu.be/Rk03Rh8P9ps?t=1440) | "battlefield and my flames dance mmm literally Bobby is the best Bobby Friggin It's so freakin cheeky It showed his" | **Shared span only** ("Bobby is the best"; the rest differs) |
| "Lizzy day. Lizzy day." | [0:27:52](https://youtu.be/Rk03Rh8P9ps?t=1672) | "to check out. Lizzy Day. Yeah, Lizzy Day. All right," | **No shared run of 3+ words (computed)**; do not quote |
| "I wanted to make it more of a duet with more harmonies, more fun vocally bits and bobs for Zeta as well" | [0:28:20](https://youtu.be/Rk03Rh8P9ps?t=1700) | "uh singing so i wanted to make it more of a duet with the more harmonies more fun vocally bits and bobs fazetta as well giddy giddy was" | **Partial (computed):** shared runs "i wanted to make it more of a duet with" … "more harmonies more fun vocally bits and bobs" |
| "Zeta hit it out of the park. She is friggin amazing and it was so fun rehearsing with her" | [0:28:58](https://youtu.be/Rk03Rh8P9ps?t=1738) | "yeah gosh again zetta hit it out of the park she is freaking amazing and it was so fun rehearsing with her um i'm so" | Agrees ("freaking" / "friggin" amazing) |
| "When I was teaching Zeta the dance, it made me so, so happy because obviously singing is more of my forte." | [0:29:59](https://youtu.be/Rk03Rh8P9ps?t=1799) | "um but yeah when I was teaching Zetta the dance it made me so so happy because obviously singing is more of my forte so I don't" | **Partial (computed):** shared runs "when i was teaching" … "the dance it made me so so happy because obviously singing is more of my forte" |
| "I added for funsies" | [0:30:40](https://youtu.be/Rk03Rh8P9ps?t=1840) | "dance move that I added For funsies because I partially" | **Shared span (computed):** whole line |
| "living my K-On dreams, living my K-On dreams, my little girl band dreams" | [0:32:48](https://youtu.be/Rk03Rh8P9ps?t=1968) | "it was a lot of fun living my cayon dreams my cayon dreams my little girl band dreams even though it's" | Agrees ("cayon" / "K-On" spelling) |
| "So it wasn't just me, you know, just willy-nilly playing it" | [0:33:22](https://youtu.be/Rk03Rh8P9ps?t=2002) | "right positions and stuff so it wasn't just me you know it's willy-nilly playing it like I was" | **Partial (computed):** shared runs "so it wasn't just me you know" … "willy nilly playing it" |
| "It's a very feel-good song, a very Liz song." | [0:34:58](https://youtu.be/Rk03Rh8P9ps?t=2098) | "for the lyrics a lot, very feel good song. A very Liz song, I've seen a" | **Partial (computed):** shared runs "very feel good song a very liz song" |
| "they're also workaholics like me" | [0:36:56](https://youtu.be/Rk03Rh8P9ps?t=2216) | "a part of me they're also workaholics they're also workaholics like" | **Partial (computed):** shared runs "they're also workaholics like" |
| "she's been calling me her husband, my husband. She's very sweet" | [0:38:00](https://youtu.be/Rk03Rh8P9ps?t=2280) | "so cute though, she's been calling me her husband, my husband. She's very sweet. I'm happy that" | **Shared span (computed):** whole line |
| "they're all freaking amazing" | [0:38:30](https://youtu.be/Rk03Rh8P9ps?t=2310) | "we can. Because they're all friggin' amazing. They're all friggin'" | Agrees on meaning ("friggin'" / "freaking"); not quoted |
| "I see what you did there" | [1:03:17](https://youtu.be/sL8WXMMEiCw?t=3797) | "Poi-tonage. Poi-tonage. Nice. I see. I see what you did there. I" | **Shared span (computed):** whole line |
| "oh my blush is strong Rudy do you think I put too much blush on today don't answer" | [1:03:33](https://youtu.be/sL8WXMMEiCw?t=3813) | "on the way? Whoa, my blush is strong. Rudy, do you think I put too much blush on today? Don't answer. Simon! Come on," | **Partial (computed):** shared runs "my blush is strong rudy do you think i put too much blush on today don't answer" |
| "I want all the outfits, I want all the fashion." | [1:14:38](https://youtu.be/sL8WXMMEiCw?t=4478) | "ba ba boom I want all the outfits, I want all the fashion Pig" | **Shared span (computed):** whole line |
| "Acceptable!" | [1:06:20](https://youtu.be/vGKcRSrLTuk?t=3980) | "Anybody who's really disliked" | **Disagrees** ("Unacceptable!"); not used |
| "Sorry, I just brought you into a random stranger's house and just had you listen to them sleep." | [1:10:23](https://youtu.be/vGKcRSrLTuk?t=4223) | "Sorry, I just brought you into a random stranger's house and just had you listen to them sleep. Wake up. Wake" | **Shared span (computed):** whole line |
| "Why is it always night on Liz Island?" | [1:11:35](https://youtu.be/vGKcRSrLTuk?t=4295) | "Why is it always night at Liz Island? The show, the" | **Partial (computed):** shared runs "why is it always night" |
| "Oh, nooooooesss." | [1:11:46](https://youtu.be/vGKcRSrLTuk?t=4306) | "Recordings for the show on" | **Not found** by the second model; not used |
| "The Frig!" | [1:16:30](https://youtu.be/vGKcRSrLTuk?t=4590) | "You Oh what the frig I mean I" | **Shared span (computed):** whole line |
| "Okay. Cheeky." | [1:17:44](https://youtu.be/vGKcRSrLTuk?t=4664) | "Stan Proudly there. Okay. Cheeky. Which, uh, which" | **Shared span (computed):** whole line |
| "Fancies! God, I fancy Graham." | [2:52:08](https://youtu.be/vGKcRSrLTuk?t=10328) | "way okay oh fancies hi fancy gram i mean gram is" | **Shared span only** ("Fancies!") |
| "What the frick? Oh my god, you scared them." | [2:54:30](https://youtu.be/vGKcRSrLTuk?t=10470) | "What? Hey! Hey! What the frick oh my god you scared them oh no oh" | **Shared span (computed):** whole line |
| "Which is live on ERB TV. Please do not swear." | [2:58:19](https://youtu.be/vGKcRSrLTuk?t=10699) | "of Big Milord Island, which is live on UrbTV, please do not swear. Don't forget to" | Agrees ("UrbTV" / "ERBTV" spelling) |
| "Don't forget to eat good noms, hydrate, get good sleep, because we want our kingdom to be good and strong!" | [2:58:24](https://youtu.be/vGKcRSrLTuk?t=10704) | "please do not swear. Don't forget to eat good noms, hydrate, get good sleeps, because we want our kingdom to be good and the WRONG! And" | **Partial (computed):** shared runs "don't forget to eat good noms hydrate get good" … "because we want our kingdom to be good and" |
| "have a lovely day, lovely to see you lovely" | [2:58:46](https://youtu.be/vGKcRSrLTuk?t=10726) | "it before it's Gone Have a lovely day lovely this year lovely and most of" | Agrees in the 2:58:52 check ("Have a lovely day, lovely to see you lovely") |
| "and most of all don't forget let my voice be your strength" | [2:58:52](https://youtu.be/vGKcRSrLTuk?t=10732) | "see you lovely, and most of all, don't forget, let my voice be your strength! Now prepare your" | **Shared span (computed):** whole line |
| "Huzzah!" | [2:59:07](https://youtu.be/vGKcRSrLTuk?t=10747) | "your war cries, huzzah!" | Agrees on "…war cries, Huzzah!" (the second model hears "Now prepare your") |
