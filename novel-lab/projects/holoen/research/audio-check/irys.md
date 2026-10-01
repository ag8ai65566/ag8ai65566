# Audio check — IRyS (2026-09-30)

Method: windows from the public stream archive archive.ragtag.moe (YouTube blocks this environment),
transcribed with faster-whisper small.en, pitch measured with Praat (100–600 Hz, word intervals only).
Tools and limits: `novel-lab/tools/audiocheck/README.md`. **This is not a listening check**: the audio was
machine-transcribed and acoustically measured, and the transcripts were reviewed in context. Lines used on
the character card were re-transcribed by a second model (whisper medium.en) and compared (see the end of
this file). Machine transcription drops some fillers and does not write giggles or lip rolls reliably, and
small.en can turn Japanese speech into English words, so Japanese phrases below are indicative only. Game
windows include game voices; only lines that are clearly hers are quoted.

All windows are from 2026, her most recent period, which this project weights highest.

## Windows measured

| Window | Stream | Segment | Speech (min) | Words | Words/min of speech | F0 median | F0 p10–p90 |
|---|---|---|---|---|---|---|---|
| chat40_2026 | [【BDay Live Aftertalk】Let's chat about Racing Tow](https://youtu.be/WZn7zl-NI3A) | [0:45:00–1:25:00](https://youtu.be/WZn7zl-NI3A?t=2700) | 27.9 | 4679 | 167.9 | 219 Hz | 179–355 Hz |
| close2026 | [【BDay Live Aftertalk】Let's chat about Racing Tow](https://youtu.be/WZn7zl-NI3A) | [4:23:20–4:35:20](https://youtu.be/WZn7zl-NI3A?t=15800) | 6.1 | 1107 | 182.6 | 226 Hz | 179–370 Hz |
| open2026 | [【BDay Live Aftertalk】Let's chat about Racing Tow](https://youtu.be/WZn7zl-NI3A) | [0:00:00–0:15:00](https://youtu.be/WZn7zl-NI3A?t=0) | 5.3 | 640 | 121.0 | 214 Hz | 147–328 Hz |
| re9_45 | [【Resident Evil Requiem】I'll miss Leon's one-line](https://youtu.be/qGKtvn8JZtY) | [2:00:00–2:45:00](https://youtu.be/qGKtvn8JZtY?t=7200) | 30.3 | 2020 | 66.6 | 220 Hz | 178–331 Hz |

"Words/min of speech" = words ÷ minutes inside whisper's speech segments (silence between segments
excluded). The opening window includes a pre-stream wait; the horror window is mostly quiet play.

## Claims checked

| Claim in the file | Result (in the machine transcript) | Evidence (ASR, archived audio) |
|---|---|---|
| Name-pun greeting "HiRyS, it's IRyS!" (R1) | **Partly detected.** The stream opens with her name and "it's IRyS"; both models agree only on "…it's IRyS." The full official greeting was not detected. | [0:05:32](https://youtu.be/WZn7zl-NI3A?t=332) |
| "How's the volume?" at the start (R2) | **Not detected in this window.** | — |
| Teases chat by turning it back on them | **Confirmed.** About her new outfit's framing, then a mock guilt trip. | "I think most of you guys are satisfied as long as you can see this, you know, up to here… You guys don't need to see the bottom half." [0:09:48](https://youtu.be/WZn7zl-NI3A?t=588); "I'm trying to make you guys feel guilty. That's what I'm doing here, okay?" [0:12:07](https://youtu.be/WZn7zl-NI3A?t=727) |
| Seiso/"yabai" duality: suggestive remarks | **Confirmed, mild.** About Kronii's goddess look: "I mean, I am a half-angel, half-demon Nephilim. I could pull it off, somehow." The next sentence compares figures; the two models disagree on its key word, so it is not quoted. | [4:23:23](https://youtu.be/WZn7zl-NI3A?t=15803) |
| Gushes fast about outfits and concerts | **Confirmed.** "cute" 42 times in the 40-minute chat window; restarts and repeats ("I knew you guys would! I knew you guys would!"; "I told you guys. I told you guys"). | [4:27:19](https://youtu.be/WZn7zl-NI3A?t=16039); [1:15:58](https://youtu.be/WZn7zl-NI3A?t=4558) |
| Fillers: "like," "you know," "I do think so" | **Confirmed.** "like" 214 times in 8,392 words (about 1 in 30 in the chat window, 1 in 40 overall); "you know" 43; "I do think…" 3. | throughout |
| Audience address: "you guys" more than "chat" | **Confirmed.** "you guys" 48, "chat" 2. | throughout |
| Rarely swears | **Confirmed.** "damn it" twice (both confirmed by the second model), a softened "holy shoot!" in the horror game; no other swear words in about 1.9 hours. | [0:56:27](https://youtu.be/WZn7zl-NI3A?t=3387); [1:20:05](https://youtu.be/WZn7zl-NI3A?t=4805); [2:39:31](https://youtu.be/qGKtvn8JZtY?t=9571) |
| Reads superchats in counted batches | **Confirmed.** "I'll go up to 30." | [4:24:37](https://youtu.be/WZn7zl-NI3A?t=15877) |
| Japanese mid-English | **Detected, indicative only** (first model on Japanese speech): "Masu-de kawaii" (probably "maji de kawaii"), "kawaii yone." | [0:50:39](https://youtu.be/WZn7zl-NI3A?t=3039); [1:02:13](https://youtu.be/WZn7zl-NI3A?t=3733) |
| Horror games: focused, short cheers | **Confirmed.** 67 words per minute of speech in Resident Evil Requiem; "Run Leon, run!" | [2:04:03](https://youtu.be/qGKtvn8JZtY?t=7443) |
| Circling sign-off | **Confirmed.** Several rounds of thanks and goodbyes; both models agree on "Thank you very much! See you guys again tomorrow!" | [4:31:32](https://youtu.be/WZn7zl-NI3A?t=16292) |
| Speaking voice "high-pitched, soft and calm" (R2) | **Revised: mid-range, relative.** Median F0 about 214–226 Hz, in the same band as Calli's upper windows and Ina (Kronii 177–215 Hz; Ame 248–276; Kiara 240–302; Gura 248–333). Soft and calm cannot be measured here. | table above |
| Fast talker when excited | **Confirmed.** 168–183 words per minute of speech in the chat windows, close to Calli (133–197) and Kiara. | table above |

## New material (ASR-transcribed short lines)

Lines not listed in the second-model check at the end of this file are first-model transcriptions only.

- About her birthday-live outfit: "I'm glad you guys liked the outfit. I knew you guys would! I would have
  been disappointed in your guys' taste if you guys didn't like this. No, I don't like it. I love it!"
  [4:27:19](https://youtu.be/WZn7zl-NI3A?t=16039)
- Sincere, to a fan's wish for her concert: "I really hope so too." [4:24:12](https://youtu.be/WZn7zl-NI3A?t=15852)
- Reading the game's price tag: "Price, 120 million dollars, holy shoot!" [2:39:31](https://youtu.be/qGKtvn8JZtY?t=9571)
- On a merch idea from staff: "that's actually a really cute idea." [1:24:17](https://youtu.be/WZn7zl-NI3A?t=5057)

## Second-model check (whisper medium.en)

Each line below was cut from the archived audio (a window of about 24–60 s around the first model's
timestamp) and transcribed again by a larger model. "Agrees" means the second model produced the same
words; it is still machine transcription, not listening. Lines that did not agree were removed from
the character card.

| First model (small.en) | Link | Second model (medium.en), excerpt | Verdict |
|---|---|---|---|
| "IRyS, IRyS, it's IRyS. IRyS from hololive English Promise." | [0:05:37](https://youtu.be/WZn7zl-NI3A?t=337) | "I I high-risk, it's Iris. Wait a sec" | **Partly confirmed**: both models hear "…it's IRyS"; the rest of the opening ("IRyS from hololive English Promise") is first-model only and is not quoted |
| "I think most of you guys are satisfied as long as you can see this, you know, up to here. You guys don't need to see the bottom half." | [0:09:48](https://youtu.be/WZn7zl-NI3A?t=588) | "it this way? I don't know. I think most of you guys are satisfied as long as you can see this up to here. I think. You don't need to see the bottom half. Nah." | Agrees |
| "I'm trying to make you guys feel guilty. That's what I'm doing here, okay? Because you guys should be ashamed of yourself." | [0:12:07](https://youtu.be/WZn7zl-NI3A?t=727) | "I'm trying to make you guys feel guilty that's what I'm doing here okay I'm trying to make you guys feel guilty for being like" | **Partly agrees**: the guilt-trip sentences agree; the closing "ashamed of yourself" is not in the second model (it hears "for being like that") and was removed |
| "I just realized I didn't take picture with the guy races damn it. I forgot about that" | [0:56:28](https://youtu.be/WZn7zl-NI3A?t=3388) | "I see anything? I just realized I didn't take pictures with the gyruses. Damn it, I forgot about that. With the really really" | Agrees ("I just realized I didn't take pictures with the [unclear]. Damn it, I forgot about that"; the models differ only on one word) |
| "Damn it. Should I have it?" | [1:20:05](https://youtu.be/WZn7zl-NI3A?t=4805) | "features race queen outfit Damn it, should I? I ended up going" | Agrees |
| "Anyways, it's so cute. It's so cute." | [1:22:48](https://youtu.be/WZn7zl-NI3A?t=4968) | "Hehehehehe Hmm Anyways, um, it's so cute. It's so cute Obvious, it's" | Agrees |
| "I mean, I am a half-angel, half-demon Nephilim. I could pull it off, somehow. I don't know if I have as big assets as she does." | [4:23:23](https://youtu.be/WZn7zl-NI3A?t=15803) | "Like Crony's goddess I mean I have a half angel, half demon Nephilim I could, I could pull it off somehow I could pull it off I don't know if I have If I" | **Agrees on the first two sentences**; the models disagree on the key word of the third, which was removed |
| "I'm glad you guys liked the outfit. I knew you guys would! I would have been disappointed in your guys' tastes if you guys didn't like this. No, I don't like it. I love it!" | [4:27:19](https://youtu.be/WZn7zl-NI3A?t=16039) | "a while. Thank you so much. I'm glad you guys like the outfit. I knew you guys would. I knew you guys would. I would have been disappointed in your guys' taste …" | Agrees |
| "Thank you very much. See you guys again tomorrow. I'll see you next time. I'm done! I'll see you guys soon! Bye!" | [4:31:46](https://youtu.be/WZn7zl-NI3A?t=16306) | "Okay, that works. Thank you very much! See you guys again tomorrow! Yes, I'll see you guys again tomorrow at 12pm. See you guys tomorrow! Bye, Ris. Bye-bye," | **Partly agrees**: "Thank you very much! See you guys again tomorrow!" agrees; the later goodbyes differ, so only the agreed part is quoted |
| "Run Leon, run!" | [2:04:03](https://youtu.be/qGKtvn8JZtY?t=7443) | "Run, Leon, run! Run! Run! Oh," | Agrees |
| "Price, 120 million dollars, holy shoot!" | [2:39:31](https://youtu.be/qGKtvn8JZtY?t=9571) | "Is this tyrant price 120 million dollars holy shoot. Oh, they're selling" | Agrees |

