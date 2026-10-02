# Audio check — Nekomata Okayu (2026-10-02)

Method: windows from the public stream archive archive.ragtag.moe (YouTube blocks this environment),
transcribed in Japanese with faster-whisper small (multilingual), pitch measured with Praat (100–600 Hz, speech
segments only). Tools and limits: `novel-lab/tools/audiocheck/README.md`. **This is not a listening check**: the
audio was machine-transcribed and acoustically measured, and the transcripts were reviewed in context. Lines used
on the character card were re-transcribed by a second model (whisper medium, multilingual) and compared after
folding katakana to hiragana and dropping punctuation (see the end of this file). Transcription does not write
laughs reliably, and Japanese ASR often picks different kanji or kana for the same word; only spans both models
render identically are quoted. Measurements describe the sampled recording and ASR segmentation; game audio,
music and other voices prevent treating them as isolated vocal measurements.

All windows are from 2026. Only in-scope public performance material is used: personal remarks in the chats
(family, childhood, health, trips, daily life) are not quoted or summarized here.

## Windows measured

| Window | Stream | Segment | Speech (min) | Characters | Characters/min of speech | F0 median | F0 p10–p90 |
|---|---|---|---|---|---|---|---|
| game20c_2026 | [【 萌えろ!!ホロ野球 】ぷれいぼ～～～る！⚾✦【 猫又おかゆ/ホロライブ 】](https://youtu.be/lTRy_mp5ODI) | [0:05:00–0:25:00](https://youtu.be/lTRy_mp5ODI?t=300) | 13.5 | 2651 | 196.4 | 296 Hz | 146–495 Hz |
| pixel25_2026 | [【 🔴Mina the Hollower 】ソウルライク × 2Dゼルダ!? 神ドットゲー✦#0](https://youtu.be/mDwTkQBtFQE) | [0:10:00–0:35:00](https://youtu.be/mDwTkQBtFQE?t=600) | 17.2 | 4106 | 238.8 | 261 Hz | 154–449 Hz |
| game30_2026 | [【 FF7リバース 】みんなと冒険だああ!! #08 ｜ FINAL FANTASY VII R](https://youtu.be/vrnsDry3DNY) | [0:05:00–0:35:00](https://youtu.be/vrnsDry3DNY?t=300) | 19.0 | 4819 | 253.8 | 262 Hz | 131–464 Hz |

"Characters/min of speech" = transcribed kana and kanji (punctuation dropped) ÷ minutes inside whisper's speech segments; it is a rough pace index for comparing windows, not a mora count.

## Marker counts (first model)

| Marker | game20c_2026 | pixel25_2026 | game30_2026 |
|---|---|---|---|
| first person 僕 (boku) | 3 | 4 | 3 |
| first person 私 | 0 | 4 | 5 |
| なんか | 2 | 12 | 11 |
| まあ | 2 | 8 | 7 |
| ちょっと待って | 0 | 1 | 0 |
| やばい | 2 | 4 | 0 |
| かわいい | 3 | 1 | 1 |
| えっ/え? | 3 | 4 | 6 |
| laugh (はは/ふふ/笑) | 3 | 1 | 5 |
| swear (くそ/ふざけ/殺) | 0 | 1 | 0 |
| ありがとう | 1 | 0 | 1 |
| English (Latin letters) | 2 | 0 | 3 |

## Claims checked

| Claim in the file | Result (in the machine transcript) | Evidence (ASR, archived audio) |
|---|---|---|
| First person "boku" | **Confirmed** throughout (e.g. "Boku yakyū wa ne…," both models). | [0:05:06](https://youtu.be/lTRy_mp5ODI?t=306) |
| Calls her fans "Onigiryā" | **Confirmed** (both models), while picking teammates in a baseball game. | [0:23:35](https://youtu.be/lTRy_mp5ODI?t=1415) |
| Plays "by vibes" | **Confirmed**: "Hai, nori de aite o buttaoshitai to omoimāsu" ("Okay, I'm going to beat them on vibes"), after skipping part of a tutorial (both models). | [0:20:37](https://youtu.be/lTRy_mp5ODI?t=1237) |
| Enjoys exploring a new game with chat | **Confirmed**: "Atarashii gēmu dakara, minna to issho ni tesaguri tansaku na no tanoshii nā" (both models). | [0:27:58](https://youtu.be/mDwTkQBtFQE?t=1678) |
| Puns | **Observed**: a pun on "ki" (tree / mind): "Ki ga sa… ki dake ni?" (both models). | [0:32:35](https://youtu.be/mDwTkQBtFQE?t=1955) |
| Cat noises when pleased | **Observed**: "nya nya nya nya nya" while swinging a weapon (both models write nya; the exact count differs). | [0:29:12](https://youtu.be/mDwTkQBtFQE?t=1752) |
| Relaxed, narrating play style | **Observed**: she reads game text aloud in a calm voice and narrates her choices; "Rettsura gō" to start. Lines she reads from the game are not her own and are not quoted. | — |
| Low voice | **Partly supported**: her lower range reaches further down than the other three (p10 about 131–155 Hz against about 160–200 Hz), but window medians (about 260 Hz) are similar; game audio is mixed in. Treat "low, boyish" as a style description, not a measured fact. | — |
| Laugh rising to a whistle | **Not checked** (whisper does not write laughs); kept from the Japanese Wikipedia (secondary). | — |

Not used: a story about her off-stream schedule at the start of the Final Fantasy VII window, and a stream title about an illness (personal matters). The Moero!! Holo Yakyū window has voiced members and crowd audio; its pitch figures are not used.

## Second model (whisper medium) on quoted lines

| First model (small) | At | Second model (medium), excerpt | Verdict |
|---|---|---|---|
| "僕野球はね" | [0:05:06](https://youtu.be/lTRy_mp5ODI?t=306) | "でもいけますやる気満々じゃん えー楽しみ僕野球はね見はしますけどゲームの経験とあんまりない のですよね楽しみです ならだいぶキャラ多いよねなのかなぁ同山所蔵" | **Shared span (computed):** whole line (kana/kanji folded) |
| "ノリで相手をぶっ倒したいと思いまーす" | [0:20:37](https://youtu.be/lTRy_mp5ODI?t=1237) | "はいノリで相手をぶっ倒したいと思いまーすホロライブリーグやってみましょうか まあノリで行きましょうホロライブリーグヘルプ えーホロライブリーグは選んだホロメン2人でチームを組んでリーグを勝ち抜いていく一人用モードですうー" | **Shared span (computed):** whole line (kana/kanji folded) |
| "おにぎりゃー" | [0:23:35](https://youtu.be/lTRy_mp5ODI?t=1415) | "おねがいしますお待たせあ!すごーい!おにぎりゃー コロネスキー コロネスキーおにぎりゃー ポコベいるんだけどーおにぎりゃー ミオファーこれ買えれるのかな?ここは固定なのね味噌スープとマトンカレーあ、超えれるー!" | **Shared span (computed):** whole line (kana/kanji folded) |
| "新しいゲームだから、みんなと一緒に手探り探索なの楽しいなぁ" | [0:27:58](https://youtu.be/mDwTkQBtFQE?t=1678) | "ねーすごいこの人ー 気象が荒いわーいやいいね新しいゲームだからみんなと一緒に手探り探索なの楽しいなぁここは? なんか上のやつを下ろすとショートカットで橋に登り降りできるようになるって感じっぽいね オッケーオッケーん いろいろチョコの" | **Shared span (computed):** whole line (kana/kanji folded) |
| "木がさ" | [0:32:35](https://youtu.be/mDwTkQBtFQE?t=1955) | "登っていこっかぁよしこのねー木がさ、当選簿してんの気になるけど木だけに?ふふっでも多分まだ開けられないんだろうねーよいしょーどん!あっあっ!やばい!強そう強そう強そう強そう!強そう強そう強そう!" | **Shared span (computed):** whole line (kana/kanji folded) |
| "ニャニャニャニャニャ" | [0:29:12](https://youtu.be/mDwTkQBtFQE?t=1752) | "はっはっは、よしいや結構このブーメラン強い気がするにゃんにゃにゃにゃーにゃーにゃーにゃーにゃーにゃーにゃーあはははは音楽めっちゃいいにゃんにゃんにゃーにゃーひゃー、ぴよっ、あっひゃーご視聴ありがとうございました" | **Shared span (computed):** whole line (kana/kanji folded) |
| "びっくりしたもやめてよー" | [0:14:20](https://youtu.be/mDwTkQBtFQE?t=860) | "あ ちょっとびっくりした もうやめてよこれにする あ 他の武器も自由に試すといい 準備ができたら交番に上がっても安心だこの騒ぎクラー券の仕業じゃねえといいんだがなぁ くれぐれも気をつけろあ、ほんとだ" | **Partial (computed):** shared run "びっくりしたも"; only that part is quoted |
| "レッツラゴー" | [0:08:55](https://youtu.be/vrnsDry3DNY?t=535) | "またあれかな 今日霧の良いところで終われたら遊びに行ってみようかなではではレッツラゴーロードゲームえーこれですねちょっと今さっき潜ってやり残しってどのぐらいあるかなーって見てたんでどんぐらい当てたんだろう昨日のセーブデータがこれか" | **Shared span (computed):** whole line (kana/kanji folded) |
