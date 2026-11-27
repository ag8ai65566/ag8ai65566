# Audio check — hololive GAMERS: Shirakami Fubuki, Ookami Mio, Inugami Korone (2026-11-27)

Method: windows from the public stream archive archive.ragtag.moe (YouTube blocks this environment), the first
8 minutes and the last 7 minutes of each stream, transcribed in Japanese with faster-whisper small (multilingual),
pitch measured with Praat (100–600 Hz, speech segments only). Tools and limits: `novel-lab/tools/audiocheck/README.md`.
**This is not a listening check**: the audio was machine-transcribed and acoustically measured, and the transcripts
were reviewed in context. Lines used on the character cards were re-transcribed by a second model (whisper medium,
multilingual, a 30-second clip around the line) and compared after folding katakana to hiragana and dropping
punctuation (see the end of this file). Japanese ASR often picks different kanji or kana for the same word, and both
models mishear names and coined words; only spans both models render the same way are quoted, and coined words heard
as near-matches are reported in romaji or in the member's own written spelling (official profile, stream titles).
Opening music and game audio cover some greetings, so "not heard" does not mean "not said". Measurements describe the
sampled recording and ASR segmentation; game audio, music and singing prevent treating them as isolated vocal
measurements.

All windows are from 2026. Fubuki has six streams (five solo, one collab with Omaru Polka, used for measurement
only), because her first picks did not capture a clean greeting; Mio and Korone have two each. Only in-scope public
performance material is used: personal remarks in the chats are not quoted or summarized here, and stream labels are
neutral.

## Windows measured

| Window | Stream | Segment | Speech (min) | Characters | Characters/min of speech | F0 median | F0 p10–p90 |
|---|---|---|---|---|---|---|---|
| fubuki_open_0kjX | [2026-10-05 birthday-live thank-you talk — Shirakami Fubuki](https://youtu.be/0kjXUGCIoZU) | [0:00:00–0:08:00](https://youtu.be/0kjXUGCIoZU?t=0) | 5.8 | 1976 | 341.3 | 336 Hz | 223–508 Hz |
| fubuki_end_0kjX | (same stream) | [1:07:52–1:14:52](https://youtu.be/0kjXUGCIoZU?t=4072) | 5.6 | 2189 | 393.6 | 324 Hz | 233–506 Hz |
| fubuki_open_GSMy | [2026-06-03 event pep-rally chat — Shirakami Fubuki](https://youtu.be/GSMyPNRANvc) | [0:00:00–0:08:00](https://youtu.be/GSMyPNRANvc?t=0) | 4.9 | 1627 | 332.0 | 326 Hz | 198–478 Hz |
| fubuki_end_GSMy | (same stream) | [1:04:35–1:11:35](https://youtu.be/GSMyPNRANvc?t=3875) | 5.5 | 1954 | 355.4 | 321 Hz | 222–505 Hz |
| fubuki_open_avWv | [2026-06-26 Star Fox stream — Shirakami Fubuki](https://youtu.be/avWvfYnaOQE) | [0:00:00–0:08:00](https://youtu.be/avWvfYnaOQE?t=0) | 2.0 | 539 | 273.3 | 302 Hz | 138–493 Hz |
| fubuki_end_avWv | (same stream) | [2:12:17–2:19:17](https://youtu.be/avWvfYnaOQE?t=7937) | 3.7 | 1103 | 301.8 | 306 Hz | 150–505 Hz |
| fubuki_open__vvb | [2026-09-18 pre-debut "delusion profile" stream — Shirakami Fubuki](https://youtu.be/_vvbn7kgqj4) | [0:00:00–0:08:00](https://youtu.be/_vvbn7kgqj4?t=0) | 3.0 | 916 | 306.3 | 350 Hz | 243–522 Hz |
| fubuki_end__vvb | (same stream) | [1:53:24–2:00:24](https://youtu.be/_vvbn7kgqj4?t=6804) | 5.3 | 1521 | 286.1 | 354 Hz | 236–533 Hz |
| fubuki_open_gbCs | [2026-10-11 Hollow Knight: Silksong #2 — Shirakami Fubuki](https://youtu.be/gbCsK3KnVVE) | [0:00:00–0:08:00](https://youtu.be/gbCsK3KnVVE?t=0) | 3.1 | 815 | 264.3 | 326 Hz | 218–515 Hz |
| fubuki_end_gbCs | (same stream) | [2:21:18–2:28:18](https://youtu.be/gbCsK3KnVVE?t=8478) | 3.6 | 1084 | 305.0 | 315 Hz | 137–501 Hz |
| fubuki_open_zTD4 | [2026-09-15 chill radio collab with Omaru Polka — Shirakami Fubuki](https://youtu.be/zTD4n-B41u4) | [0:00:00–0:08:00](https://youtu.be/zTD4n-B41u4?t=0) | 4.9 | 1762 | 360.7 | 318 Hz | 205–505 Hz |
| fubuki_end_zTD4 | (same stream) | [1:49:02–1:56:02](https://youtu.be/zTD4n-B41u4?t=6542) | 5.9 | 2436 | 411.3 | 288 Hz | 204–474 Hz |
| mio_open_v49b | [2026-10-11 #朝ミオ morning show — Ookami Mio](https://youtu.be/v49bZ8yH0I0) | [0:00:00–0:08:00](https://youtu.be/v49bZ8yH0I0?t=0) | 5.7 | 1019 | 178.9 | 248 Hz | 130–396 Hz |
| mio_end_v49b | (same stream) | [1:04:40–1:11:40](https://youtu.be/v49bZ8yH0I0?t=3880) | 3.9 | 1060 | 271.4 | 249 Hz | 167–446 Hz |
| mio_open_3b1W | [2026-09-18 quiet late-night chat — Ookami Mio](https://youtu.be/3b1W_NGeIgs) | [0:00:00–0:08:00](https://youtu.be/3b1W_NGeIgs?t=0) | 3.9 | 1076 | 275.9 | 203 Hz | 171–282 Hz |
| mio_end_3b1W | (same stream) | [1:21:40–1:28:40](https://youtu.be/3b1W_NGeIgs?t=4900) | 3.3 | 998 | 304.7 | 197 Hz | 164–267 Hz |
| korone_open_Zlnq | [2026-05-03 朝ころ first episode — Inugami Korone](https://youtu.be/Zlnqxdwg5Io) | [0:00:00–0:08:00](https://youtu.be/Zlnqxdwg5Io?t=0) | 4.7 | 956 | 203.2 | 301 Hz | 204–454 Hz |
| korone_end_Zlnq | (same stream) | [0:53:34–1:00:34](https://youtu.be/Zlnqxdwg5Io?t=3214) | 3.3 | 787 | 238.2 | 321 Hz | 235–452 Hz |
| korone_open_alUD | [2026-10-20 game stream — Inugami Korone](https://youtu.be/alUDRkSYyc8) | [0:00:00–0:08:00](https://youtu.be/alUDRkSYyc8?t=0) | 4.2 | 1105 | 261.4 | 295 Hz | 204–463 Hz |
| korone_end_alUD | (same stream) | [2:01:53–2:08:53](https://youtu.be/alUDRkSYyc8?t=7313) | 5.1 | 1077 | 209.9 | 257 Hz | 117–441 Hz |

"Characters/min of speech" = transcribed kana and kanji (punctuation dropped) ÷ minutes inside whisper's speech
segments; it is a rough pace index for comparing windows, not a mora count. mio_open_v49b is partly opening music
(178.9 characters a minute) and is excluded from the pace range on Mio's card; the late-night chat is billed as a
quiet stream, so its narrow pitch range reflects the format. korone_end_alUD has game audio throughout (its low p10
is not her voice alone). fubuki_*_zTD4 is a two-person collab and is not used for her ranges.

## Marker counts (first model)

| Marker | Fubuki (10 windows) | Mio (4) | Korone (4) |
|---|---|---|---|
| 白上 / 白紙 / しらかみ (Fubuki's self-reference; 白紙 is the first model's spelling of しらかみ) | 10 | 0 | 0 |
| うち (Mio's "I") | — | 20 | 2 |
| ころね / コロネ | 0 | 0 | 1 |
| ではではでは | 4 | 0 | 0 |
| なんか | 47 | 16 | 13 |
| ちょっと待って | 4 | 0 | 7 |
| ありがとう | 11 | 4 | 10 |
| めっちゃ | 4 | 1 | 0 |
| マジ | 4 | 0 | 2 |
| かわいい | 8 | 0 | 0 |
| English (Latin letters) | 16 | 11 | 12 |

Fubuki's うち count (12) is not shown: in her windows it is the ordinary word ("our," "inside"), not a pronoun.

## Claims checked

| Claim in the files | Result (in the machine transcripts) | Evidence (ASR, archived audio) |
|---|---|---|
| Fubuki calls herself 白上 (Shirakami) | **Observed**: about ten times (the first model writes 白紙, the second しらかみ; both are the reading Shirakami). Her official Q&A uses 白上 the same way. | [0:02:03](https://youtu.be/0kjXUGCIoZU?t=123), [0:03:53](https://youtu.be/gbCsK3KnVVE?t=233) |
| Fubuki's greetings | **Partly observed**: her name plus 「でーす」 in both models; "Hi, Friends!" heard as a near-match by both (ハイフレーンズー / ハイフレーズ / はーいフェーズ); the evening 「こんばんきーつねー」 heard by the second model only, once. Her official profile lists 「こんこんきーつね！」, "Hi, Friends!" and the others; the card relies on that. | [0:02:03](https://youtu.be/0kjXUGCIoZU?t=123), [0:03:53](https://youtu.be/gbCsK3KnVVE?t=233) |
| Fubuki's closing formula | **Observed** in three streams: 「といったところで」 / 「ということで」 + "today we'll end around here," then 「ではでは」. | [1:13:15](https://youtu.be/0kjXUGCIoZU?t=4395), [1:59:37](https://youtu.be/_vvbn7kgqj4?t=7177), [2:27:12](https://youtu.be/gbCsK3KnVVE?t=8832) |
| Fubuki's sign-off "otsukon" | **Observed as a near-match** in four streams: the second model writes おつこん (でした / でございました) three times and オスコン once; the first model writes おつこみ, おつかん, おつとん. The official profile spells it 「おつこーん」. | [1:14:19](https://youtu.be/0kjXUGCIoZU?t=4459), [1:11:25](https://youtu.be/GSMyPNRANvc?t=4285), [2:27:12](https://youtu.be/gbCsK3KnVVE?t=8832) |
| Fubuki's advice to the newcomers | **Observed** in both models: don't be swayed by "this fox senpai," stream your own way. | [1:58:45](https://youtu.be/_vvbn7kgqj4?t=7125) |
| Mio calls herself うち | **Observed** about twenty times; her greeting stacks it (the second model hears 「うちうちうちだよ」 in both streams; the first model 「すっちうち うちだよ」 once and 「うちだよー」 once). Her 2021 title writes 「うちうち、うちだよ」. | [0:01:52](https://youtu.be/v49bZ8yH0I0?t=112), [0:01:56](https://youtu.be/3b1W_NGeIgs?t=116) |
| Mio's greetings | **Observed as near-matches**: the morning 「おはみぉーん」 (おはみよー / オハ見用) and the evening 「こんばんみぉーん」 (こんばんみょーん / こんばんみよ). Her titles write 「おはみぉーん」; the official profile 「こんばんみぉーん！大神ミオだよ～！」. | [0:01:59](https://youtu.be/v49bZ8yH0I0?t=119), [0:01:59](https://youtu.be/3b1W_NGeIgs?t=119) |
| Mio's sign-offs | **Observed**: 「それではまた明日ねー」 and 「また明日会いましょう、じゃあねー」, each followed by a coined "otsu-mion" (a near-match in both models). | [1:10:36](https://youtu.be/v49bZ8yH0I0?t=4236), [1:26:44](https://youtu.be/3b1W_NGeIgs?t=5204) |
| Mio's morning-show format | **Observed**: a corner reading viewers' posts on a weekly theme, the theme for next week, then goodbye. Paraphrased, not quoted. | [1:10:00](https://youtu.be/v49bZ8yH0I0?t=4200) |
| Korone's morning opening | **Observed**: 「はい、おはよー」 in both models. | [0:01:50](https://youtu.be/Zlnqxdwg5Io?t=110) |
| Korone narrates herself in the third person | **Observed** once, in both models, at the end of the first 朝ころ. | [0:59:55](https://youtu.be/Zlnqxdwg5Io?t=3595) |

## Second model (whisper medium) on quoted lines

| First model (small) | At | Second model (medium), excerpt | Verdict |
|---|---|---|---|
| "朝みょでーす すっちうち うちだよ 大神みょだよー おはみよー" | [0:01:50](https://youtu.be/v49bZ8yH0I0?t=110) | "…朝見用ですウチウチウチだよオオカミ見用だよオハ見用…" | **Partly agrees:** both models hear "うちうちだよ" and her name with "だよ" (both mishear ミオ); the second model hears three うち; the coined greeting is a near-match (おはみよー / オハ見用), so the card uses the spelling of her titles, 「おはみぉーん」, and her 2021 title for 「うちうち、うちだよ」 |
| "それではまた明日ねー おつみよう" | [1:10:36](https://youtu.be/v49bZ8yH0I0?t=4236) | "…来週のアサミオもよろしくお願いいたしますそれでは また明日ねーおつみよー" | **Partial (computed):** shared run "それではまた明日ね"; the coined sign-off is a near-match (おつみよう / おつみよー), reported in romaji as "otsu-mion" |
| "うちだよー おかみみよだよー こんばんみょーん" | [0:01:56](https://youtu.be/3b1W_NGeIgs?t=116) | "…うちうちうちだよオオカミミオだよこんばんみよ今日はまったりしっとり行きたいと思います" | **Partly agrees:** both models hear "うちだよ", her name with "だよ" and a near-match of the evening greeting (こんばんみょーん / こんばんみよ); the card uses the official spelling 「こんばんみぉーん！大神ミオだよ～！」 |
| "ということで皆さんありがとうございました また明日会いましょう じゃあねー おつみようー" | [1:26:40](https://youtu.be/3b1W_NGeIgs?t=5200) | "…よろしくお願いしますということで皆さんありがとうございましたまた明日会いましょうじゃあねおつみよー" | **Partial (computed):** shared run "ということで皆さんありがとうございましたまた明日会いましょうじゃあね"; the coined sign-off is a near-match (おつみようー / おつみよー) |
| "はいおはよう おはよう" | [0:01:50](https://youtu.be/Zlnqxdwg5Io?t=110) | "はい、おはよーおはよー…" | Agrees (spelling): おはよう / おはよー, a long-vowel spelling; same words. |
| "楽しかった! なんか朝訳もいいなって思う コロネなのであった" | [0:59:52](https://youtu.be/Zlnqxdwg5Io?t=3592) | "…みんな、朝ありがとうね、楽しかったなんか朝枠もいいなって思うコロネなのであった…" | Agrees (spelling): the first model writes 朝訳 for 朝枠 ("morning slot," same reading); both write コロネ, which the card writes ころね, the spelling of her name. |
| "撮っていた白紙でーす! ハイフレーンズー!" | [0:02:03](https://youtu.be/0kjXUGCIoZU?t=123) | "はい!明日配信予約を取っていたしらかみでーす!ハイフレーズ!…" | **Partly agrees:** both models hear her name (白紙 / しらかみ, read Shirakami) with "でーす" and a near-match of "Hi, Friends!" (ハイフレーンズー / ハイフレーズ); her official profile lists "Hi, Friends!" as her signature greeting; reported, not quoted from ASR |
| "はい!ではではでは! おつこみです!" | [1:14:19](https://youtu.be/0kjXUGCIoZU?t=4459) | "…はいではではでは落ちコンでしたおやすみなさーい" | **Partly agrees:** shared "はいではではでは"; the sign-off is a near-match (おつこみです / 落ちコンでした); her official profile spells it 「おつこーん」 |
| "はい、といたところで 今日はこの辺で終わっていこうかなと思っております" | [1:13:15](https://youtu.be/0kjXUGCIoZU?t=4395) | "…といったところで今日はこの辺で終わっていこうかなと思っておりまーす…" | **Partial (computed):** shared run "ところで今日はこの辺で終わっていこうかなと思っており"; the first model drops the small っ of といったところで ("with that said"), so the card quotes 「といったところで」 as the second model and the other streams have it |
| "おつかん!" | [1:11:25](https://youtu.be/GSMyPNRANvc?t=4285) | "…アルケミストの定めを背負って頑張りましょー!オスコンでしたー!" | **Not confirmed** as a quotation: both models hear a near-match of "otsukon" (おつかん / オスコン) |
| "白紙でーす はい! さて、シルクソングを続きやっていこうと思います!" | [0:03:53](https://youtu.be/gbCsK3KnVVE?t=233) | "はいみなさんどうもこんばんきーつねー 白紙でーすはーいフェーズさてシルクソング続きやっていこうと思います…" | **Partly agrees:** both models hear "白紙でーす" (her name, Shirakami) and "続きやっていこうと思います"; only the second model hears the greeting before it, 「はいみなさんどうもこんばんきーつねー」, and a near-match of "Hi, Friends!" after it, so the evening greeting is reported, not quoted as verified |
| "といたところで皆さんおつとんでございました また次回一かじかやろうと思います" | [2:27:12](https://youtu.be/gbCsK3KnVVE?t=8832) | "…といったところで皆さんおつこんでございましたまた次回、いちかじかやろうと思いますではでは、おつこんでした今日もありがとうございました…" | **Partly agrees:** shared "でございましたまた次回"; the sign-off word is a near-match in the first model (おつとん) and おつこん in the second, which also hears "ではでは、おつこんでした" |
| "ではでは 今日もありがとうございました" | [2:27:19](https://youtu.be/gbCsK3KnVVE?t=8839) | "…ではでは、おつこんでした今日もありがとうございました…" | **Partial (computed):** shared runs "ではでは" and "今日もありがとうございました" |
| "ということで、今日はこの辺りで終わっていこうと思います" | [1:59:37](https://youtu.be/_vvbn7kgqj4?t=7177) | "…ということで今日はこのあたりで終わっていこうと思います勝手に妄想プロフィール楽しかったです…ではではおつこんでした" | Agrees (spelling): 辺り / あたり; same words. The second model also hears "ではではおつこんでした" after it. |
| "このキツネの先輩の言葉に流されず是非自分らしく配信をしてほしいです" | [1:58:45](https://youtu.be/_vvbn7kgqj4?t=7125) | "新人の諸君遊び回り隊の諸君この配信を見ていたらこのキツネの先輩の言葉に流されずぜひ自分らしく配信をしてほしいです…" | Agrees (spelling): 是非 / ぜひ; same words. |

Per-line output of the second model: scratch files `jconfirm` runs of 2026-11-27 (15 clips); the excerpts above are
copied from them, trimmed to the quoted line and cleared of personal remarks.
