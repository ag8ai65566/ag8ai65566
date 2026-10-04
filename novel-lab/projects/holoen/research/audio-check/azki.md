# Audio check — AZKi (2026-10-02)

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
| horror20_2026 | [【パラノマサイト FILE23 本所七不思議】完全初見！ホラー×群像ミステリーの名作 #1【ホロ](https://youtu.be/22FaM0PkTwU) | [0:05:00–0:25:00](https://youtu.be/22FaM0PkTwU?t=300) | 13.6 | 3809 | 281.1 | 297 Hz | 137–470 Hz |
| geo30_2026 | [【GeoGuessr】1分ジオゲッサー！京王電鉄の駅をゲス！【ホロライブ / AZKi】](https://youtu.be/3ri2_FG67uY) | [0:05:00–0:35:00](https://youtu.be/3ri2_FG67uY?t=300) | 20.0 | 4460 | 222.6 | 312 Hz | 192–498 Hz |
| aprilfool_2026 | [【#AZKi初配信】AZKi Debut. はじめまして――？【新人Vtuber】](https://youtu.be/Y5BPxMCI6oU) | [0:00:00–0:20:00](https://youtu.be/Y5BPxMCI6oU?t=0) | 13.0 | 2829 | 218.4 | 340 Hz | 232–492 Hz |
| game30_2026 | [【クロノ・トリガー】完全初見！時を超える名作RPG、はじめます―― #2【ホロライブ / AZK](https://youtu.be/ZlaE59NgPpg) | [0:10:00–0:40:00](https://youtu.be/ZlaE59NgPpg?t=600) | 18.7 | 3798 | 203.4 | 244 Hz | 110–453 Hz |

"Characters/min of speech" = transcribed kana and kanji (punctuation dropped) ÷ minutes inside whisper's speech segments; it is a rough pace index for comparing windows, not a mora count.

## Marker counts (first model)

| Marker | horror20_2026 | geo30_2026 | aprilfool_2026 | game30_2026 |
|---|---|---|---|---|
| first person 余 (yo) | 0 | 1 | 0 | 0 |
| first person 僕 (boku) | 0 | 0 | 0 | 1 |
| first person 私 | 3 | 0 | 0 | 3 |
| third person あずき/AZKi | 15 | 5 | 17 | 1 |
| なんか | 15 | 5 | 7 | 19 |
| まあ | 3 | 3 | 0 | 0 |
| ちょっと待って | 3 | 2 | 0 | 2 |
| やばい | 1 | 9 | 0 | 21 |
| えっ/え? | 10 | 3 | 3 | 23 |
| laugh (はは/ふふ/笑) | 0 | 0 | 1 | 0 |
| ありがとう | 3 | 5 | 0 | 1 |
| English (Latin letters) | 6 | 4 | 4 | 8 |

## Claims checked

| Claim in the file | Result (in the machine transcript) | Evidence (ASR, archived audio) |
|---|---|---|
| April Fools 2026: plays a nervous "newly debuted" VTuber | **Confirmed**: she introduces herself as if for the first time ("Bācharu dībā AZKi, kasō sekai no utahime desu"), with slides, while chat "guesses" her likes; "Ē, chotto chotto, naande sonna minna jōhō o motteru no?" (both models). | [0:06:36](https://youtu.be/Y5BPxMCI6oU?t=396), [0:08:05](https://youtu.be/Y5BPxMCI6oU?t=485) |
| Likes and dislikes (her own list in that stream) | **Her account**: likes music, singing, composing, anime, maps, puns, sour food, animals, the long-tailed tit; dislikes cilantro ("Pakuchī! Iya, ichiban kirai! Iranai!", both models), very sweet food, bugs and horror. | [0:09:30](https://youtu.be/Y5BPxMCI6oU?t=570), [0:12:09](https://youtu.be/Y5BPxMCI6oU?t=729) |
| Key visual novels and anime shaped her | **Her account**: AIR, CLANNAD, Angel Beats!, Charlotte, Little Busters!, Nanoha, Macross Frontier and Delta ("Kagikko"). | [0:15:12](https://youtu.be/Y5BPxMCI6oU?t=912) |
| Mock-villain flourish | **Confirmed**: "Kono mojisū ni kyōfu suru ga ii" ("Tremble at this word count") before a dense slide (both models). | [0:17:10](https://youtu.be/Y5BPxMCI6oU?t=1030) |
| RPG first playthrough (Chrono Trigger, 2026-05-15) | **Confirmed** reactions: "Senryakuteki tettai" ("strategic retreat") and "Iyā, osoroshii yume datta nā" ("What a frightening dream that was") after a forced loss; "Bottakuri!" ("Rip-off!") at a shop; "Azu maō ja nai desu!" ("Azu is not the Demon King!") about her party name (both models). | [0:21:58](https://youtu.be/ZlaE59NgPpg?t=1318), [0:31:25](https://youtu.be/ZlaE59NgPpg?t=1885), [0:33:39](https://youtu.be/ZlaE59NgPpg?t=2019) |
| "Guess!" in GeoGuessr | **Confirmed** (2026-05-12, a one-minute GeoGuessr on Keio line stations): she locks answers in with "Gesu!" / "Gēsu!" (the second model agrees on the long "Gēsu!"), cheers herself on ("Yoshū ga ikiteru," "my prep is paying off"; "Azayaka na manten o totte ikimasu," "I'll take a brilliant perfect score"), and reads street signs, shop logos and shadows out loud. | [0:11:03](https://youtu.be/3ri2_FG67uY?t=663), [0:15:50](https://youtu.be/3ri2_FG67uY?t=950), [0:16:23](https://youtu.be/3ri2_FG67uY?t=983) |
| Horror mystery (Paranormasight, 2026-07-13) | **Observed**: she names her player "Azukichi" ("meitantei Azukichi ni omakase," "leave it to great detective Azukichi"), links the mystery to "guess" elements, and yelps "abune" at sudden sounds. The game's narrator is voiced, so this window is not used for her pitch. | [0:14:47](https://youtu.be/22FaM0PkTwU?t=887) |
| Speech pace | About 200–220 transcribed characters a minute of speech in the April Fools and RPG windows (measured, careful delivery), about 280 in the horror mystery (reading text aloud). | — |
| Register | The April Fools window (a nervous "new VTuber" act, median about 340 Hz) and the excited GeoGuessr window (about 312 Hz) sit well above her RPG window (about 244 Hz). | — |

Private-life material is excluded under the project's scope rule.

## Second model (whisper medium) on quoted lines

| First model (small) | At | Second model (medium), excerpt | Verdict |
|---|---|---|---|
| "バーチャルディーバーあずき、仮想世界の歌姫です" | [0:06:36](https://youtu.be/Y5BPxMCI6oU?t=396) | "…バーチャルディーバーあずき 仮想世界のうたひめです音楽と歌うことが大大大大好きです…" | **Shared span (computed):** whole line (same reading; the models spell a word differently) |
| "ちょっとちょっとなんでそんなみんな情報を持ってるの" | [0:08:05](https://youtu.be/Y5BPxMCI6oU?t=485) | "…え、ちょっとちょっと、なんでそんなみんな情報を持ってるの?…" | **Shared span (computed):** whole line (kana/kanji folded) |
| "ダジャレも好きなんです" | [0:09:30](https://youtu.be/Y5BPxMCI6oU?t=570) | "…地図を見るなんで?なんで?え、ダジャーレ、あ、ダジャーレ" | **Not confirmed** by the second model; not quoted |
| "パクチー！いや、一番嫌い！いらない！" | [0:12:09](https://youtu.be/Y5BPxMCI6oU?t=729) | "…苦手なものパクチーいや一番嫌いいらない激甘なもの…" | **Shared span (computed):** whole line (kana/kanji folded) |
| "この文字数に恐怖するがいい" | [0:17:10](https://youtu.be/Y5BPxMCI6oU?t=1030) | "同時 に 大好き でこの 世界 に 行っ て き たので アズキ の 頑張っ て [Private-life material removed; this bracketed note is not spoken text.] を まとめ て き まし た の で みんな さんこの 文字 数 に 恐怖 する が いいはい こちらうわぁ" | **Shared span (computed):** whole line (kana/kanji folded) |
| "戦略的撤退" | [0:21:58](https://youtu.be/ZlaE59NgPpg?t=1318) | "2回目にして終わってない終わってないよまだ戦略的撤退いや恐ろしい夢だったなとこれみんなみんな生きてるみんな生きてるみんな生きてるねセーブ" | **Shared span (computed):** whole line (kana/kanji folded) |
| "いやー恐ろしい夢だったなぁ" | [0:22:04](https://youtu.be/ZlaE59NgPpg?t=1324) | "戦略的撤退!いやー恐ろしい夢だったなーとこれみんなーみんな生きてる、みんな生きてるみんな生きてるねセーブなんもなかったんやご視聴ありがとうございました" | **Partial (computed):** shared run "いや恐ろしい夢だったな"; only that part is quoted |
| "ぼったくり" | [0:31:25](https://youtu.be/ZlaE59NgPpg?t=1885) | "…お金!やば!ぼったくり、ぼったくり、ぼったくりです、ぼったくりの店…" | **Shared span (computed):** whole line (kana/kanji folded) |
| "アズ魔王じゃないです" | [0:33:39](https://youtu.be/ZlaE59NgPpg?t=2019) | "へぇはぁアズ魔王じゃないです 魔王はアズ魔王じゃないですこの世界でアズノでしょ? え?待って何も別にできない?もうできなさそうんー?えぇーえ、これ" | **Shared span (computed):** whole line (kana/kanji folded) |
| "ゲス" | [0:11:01](https://youtu.be/3ri2_FG67uY?t=661) | "動かなくてもいけるかもしれん高く見積もるといいよいいよいいよいいよよしよし残しませんいけっすいや、1分はね意外とすぐ過ぎ去るからなこう来てるからこう来てるからここか?寝台、寝台高いいねいいねいいですよヨシウが生きてる" | **Partial (computed):** shared run "す"; only that part is quoted |
| "予習が生きてる" | [0:11:23](https://youtu.be/3ri2_FG67uY?t=683) | "いいねいいねいいですよ 予習が生きてるよしどんどんこの感じで全駅をゲスしていきたいと思う行くぞ!ケイオーダガヤマは、ケイオーダガヤマは、玉の、玉、玉…" | **Shared span (computed):** whole line (kana/kanji folded) |
| "ゲース" | [0:15:50](https://youtu.be/3ri2_FG67uY?t=950) | "このフォル…このロゴのマック古いかえ、井の頭線…これ聖歯かここでしょ!ゲース!オーケーイ!ちょ、みんな…見てください!みなさん!ちょっと…え、ちょ、余臭が生きてるわ余臭…余臭って大事コマバー東大前待って、このレー…この…この…K.O.いろがしらせんこ…こ…" | **Shared span (computed):** whole line (kana/kanji folded) |
| "鮮やかな満点を取っていきます" | [0:16:23](https://youtu.be/3ri2_FG67uY?t=983) | "池農部 駒場東大前鮮やかな満点を取っていきますみなさん待ってKO戦ってここだけ?そんなことないここ、あれ?KO戦ってここ、ここここ渋谷からゆっくりやる" | **Shared span (computed):** whole line (kana/kanji folded) |
| "この野郎!この野郎!この案内に" | [0:24:22](https://youtu.be/22FaM0PkTwU?t=1462) | "…この野郎、この野郎、この案内に おっと失礼いたしました…" | **Not confirmed as hers:** both models hear it, but the surrounding lines are the game's voiced narrator; not quoted, and "kono yarō" stays a secondary transcription (quotation pass, Claude, 2026-10-04) |

Second-model excerpts are trimmed to the span needed for each line ("…" marks cuts); out-of-scope
personal material was removed after GPT's 2026-10-02 review.
