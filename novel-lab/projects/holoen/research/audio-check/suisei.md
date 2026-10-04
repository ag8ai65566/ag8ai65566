# Audio check — Hoshimachi Suisei (2026-10-02)

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
are not quoted or summarized here.

## Windows measured

| Window | Stream | Segment | Speech (min) | Characters | Characters/min of speech | F0 median | F0 p10–p90 |
|---|---|---|---|---|---|---|---|
| chat20b_2026 | [【雑談 / 告知アリ】話題募集中💭【星街すいせい / #ほしまちすたじお】](https://youtu.be/GQMY5Vl9Dfk) | [1:10:00–1:30:00](https://youtu.be/GQMY5Vl9Dfk?t=4200) | 13.9 | 4701 | 338.0 | 246 Hz | 164–465 Hz |
| chat30_2026 | [【雑談 / 告知アリ】話題募集中💭【星街すいせい / #ほしまちすたじお】](https://youtu.be/GQMY5Vl9Dfk) | [0:00:00–0:30:00](https://youtu.be/GQMY5Vl9Dfk?t=0) | 20.2 | 6698 | 332.2 | 262 Hz | 162–493 Hz |
| horror20_2026 | [【BIOHAZARD requiem】※ネタバレあり‼この街の重さに打ち勝て───【星街すいせい](https://youtu.be/a1rcws7ellI) | [0:40:00–1:00:00](https://youtu.be/a1rcws7ellI?t=2400) | 10.9 | 2731 | 250.4 | 268 Hz | 179–447 Hz |
| game25_2026 | [【リズム天国ミラクルスターズ 】初めてのリズム天国！！たのしみ！！！✨✨【星街すいせい / #ほ](https://youtu.be/aUlbTsnMGNE) | [0:20:00–0:45:00](https://youtu.be/aUlbTsnMGNE?t=1200) | 16.7 | 3239 | 194.1 | 318 Hz | 168–513 Hz |

"Characters/min of speech" = transcribed kana and kanji (punctuation dropped) ÷ minutes inside whisper's speech segments; it is a rough pace index for comparing windows, not a mora count.

## Marker counts (first model)

| Marker | chat20b_2026 | chat30_2026 | horror20_2026 | game25_2026 |
|---|---|---|---|---|
| first person 私 | 10 | 19 | 6 | 1 |
| third person すいちゃん | 7 | 10 | 0 | 4 |
| なんか | 20 | 43 | 18 | 3 |
| まあ | 13 | 12 | 2 | 1 |
| ちょっと待って | 2 | 2 | 0 | 0 |
| やばい | 1 | 1 | 5 | 0 |
| かわいい | 0 | 4 | 0 | 0 |
| えっ/え? | 1 | 8 | 4 | 3 |
| laugh (はは/ふふ/笑) | 0 | 1 | 1 | 0 |
| ありがとう | 4 | 0 | 0 | 4 |
| English (Latin letters) | 1 | 23 | 0 | 2 |
| こんなきり/こんにちは | 1 | 0 | 0 | 0 |

## Claims checked

| Claim in the file | Result (in the machine transcript) | Evidence (ASR, archived audio) |
|---|---|---|
| Official introduction ("A shooting star that appeared from diamonds in the rough…") | **Present but garbled**: the first model garbles it; the second model comes closer ("…のごとく現れたスターの…バーチャルアイデルの…"). The card keeps the official profile wording. | [0:04:22](https://youtu.be/GQMY5Vl9Dfk?t=262) |
| "Sui-chan wa~ kyō mo kawaii~" right after the introduction | **Confirmed** (both models, verbatim); said twice at the opening, stretched and sing-song. Her 2026 shorts use the line as a hashtag. | [0:04:27](https://youtu.be/GQMY5Vl9Dfk?t=267) |
| Mock blame of chat | **Confirmed**: "Iya iya iya, watashi wa warukunai" … "Komento-ran ga yarette ittan da" … "Ore wa warukunē" (both models on each span; the second model writes ねえ for ねぇ). | [0:05:39](https://youtu.be/GQMY5Vl9Dfk?t=339) |
| Forever-18 bit | **Confirmed**: "Sui-chan wa jūhassai da yo" answering a viewer's age joke. | [0:12:43](https://youtu.be/GQMY5Vl9Dfk?t=763) |
| Tales fan; Tales of the Abyss is her favorite | **Confirmed** (both models): "Watashi Teiruzu shirīzu de ichiban suki desu kara, Abisu ga"; "Kore wa Teiruzu ga daisuki na hanashi desu." | [0:15:36](https://youtu.be/GQMY5Vl9Dfk?t=936) |
| Guest appearances at members' concerts in 2026, including Mori Calliope's | **Her own account**: since April 2026 she has appeared at several members' lives ("the one with Calliope," Otonose Kanade's, Todoroki Hajime's); after setting up her own agency she wanted to show she still works with hololive members, and she accepts invitations from members whose stages she has not joined yet. | [1:12:51](https://youtu.be/GQMY5Vl9Dfk?t=4371), [1:14:19](https://youtu.be/GQMY5Vl9Dfk?t=4459), [1:15:41](https://youtu.be/GQMY5Vl9Dfk?t=4541) |
| Gaming register (Resident Evil Requiem, June 2026) | **Observed**: mock-rough "ore" talk with herself ("Hando-gan o tsukaisugi nan da ore wa"), "Rasuto erikusā shōkōgun" (hoarding items), a mock-solemn "sasuga ni rekuiemu anken" when an enemy will not die; focused, clipped reactions rather than screams. | [0:42:23](https://youtu.be/a1rcws7ellI?t=2543), [0:55:01](https://youtu.be/a1rcws7ellI?t=3301) |
| Speech pace | About 330–340 transcribed characters a minute of speech in chat, about 250 in the horror game (more silence and reading). | — |

Private-life material is excluded under the project's scope rule. The Rhythm Heaven window is full of game music and voiced cues, so its pitch figures (median about 318 Hz) are not used for her voice.

## Second model (whisper medium) on quoted lines

| First model (small) | At | Second model (medium), excerpt | Verdict |
|---|---|---|---|
| "スイちゃんは今日も可愛い" | [0:04:27](https://youtu.be/GQMY5Vl9Dfk?t=267) | "…星町スイセイですスイちゃんは今日も可愛いみんなありがとう…" | **Shared span (computed):** whole line (kana/kanji folded) |
| "いやいやいや、私は悪くないよ" | [0:05:39](https://youtu.be/GQMY5Vl9Dfk?t=339) | "いやいやいや、私は悪くない、だって、コメント欄が言ったんだ。コメント欄が。やれって言ったんだ。俺は悪くねえ、俺は悪くねえ。…" | **Partial (computed):** shared run "いやいやいや私は悪くない"; only that part is quoted |
| "コメント欄がやれって言ったんだ" | [0:05:42](https://youtu.be/GQMY5Vl9Dfk?t=342) | "いやいやいや、私は悪くない、だって、コメント欄が言ったんだ、コメント欄が。やれって言ったんだ。俺は悪くね、俺は悪くね。…" | **Shared span (computed):** whole line (kana/kanji folded) |
| "俺は悪くねぇ" | [0:05:48](https://youtu.be/GQMY5Vl9Dfk?t=348) | "…コメント欄が言ったんだ。コメント欄が。やれって言ったんだ。俺は悪くねえ。俺は悪くねえ。…" | **Shared span (computed):** whole line (same reading; the models spell a word differently) |
| "スイちゃんは18歳だよ" | [0:12:41](https://youtu.be/GQMY5Vl9Dfk?t=761) | "…スイちゃん同年代の香りがぷんぷんする?スイちゃんは18歳だよ18って今は8歳18って8歳だよ…" | **Shared span (computed):** whole line (kana/kanji folded) |
| "アビスはね、私テイルズシリーズで一番好きですから" | [0:15:36](https://youtu.be/GQMY5Vl9Dfk?t=936) | "…アビスはねアビスはね私テイルズシリーズで一番好きですからアビスが…" | **Shared span (computed):** whole line (kana/kanji folded) |
| "これはテイルズが大好きな話です" | [0:15:44](https://youtu.be/GQMY5Vl9Dfk?t=944) | "…これって何の話ですかこれはテイルズが大好きな話です…" | **Shared span (computed):** whole line (kana/kanji folded) |
| "カリオペとのやつを話したか" | [1:12:51](https://youtu.be/GQMY5Vl9Dfk?t=4371) | "…それって全部話したっけカリオペトのやつを話したか キャナデのやつも話したか…" | **Shared span (computed):** whole line (kana/kanji folded) |
| "スイちゃんじゃあもうホロメン絡まないのかな" | [1:14:19](https://youtu.be/GQMY5Vl9Dfk?t=4459) | "…人事務所を作りました…スイちゃんじゃあもうホロメンと絡まないのかなホロメンとのコラボとかなくなっていするのかな…" | **Partial (computed):** shared run "すいちゃんじゃあもうほろめん"; only that part is quoted |
| "今までまだ出たことがない人のライブは誘ってくださったらなるべく出たいなと思って" | [1:15:41](https://youtu.be/GQMY5Vl9Dfk?t=4541) | "…今までまだ出て出たことがない人のライブは誘ってくださったらなるべく出たいなぁと思って あのスケジュールが合わなかったらあのやむなくごとりはしてるんだけど…" | **Partial (computed):** shared run "出たことがない人のらいぶは誘ってくださったらなるべく出たいな"; only that part is quoted |

Second-model excerpts are trimmed to the span needed for each line ("…" marks cuts); out-of-scope
personal material was removed after GPT's 2026-10-02 review.
