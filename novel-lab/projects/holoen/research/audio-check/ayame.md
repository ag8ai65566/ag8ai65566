# Audio check — Nakiri Ayame (2026-10-02)

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
| costume25_2026 | [【新衣装】超超超超かわ余な新衣装お披露目❣👀【百鬼あやめ/ホロライブ】](https://youtu.be/7RG6f33ZOvU) | [0:05:00–0:30:00](https://youtu.be/7RG6f33ZOvU?t=300) | 17.9 | 4991 | 278.4 | 283 Hz | 199–484 Hz |
| horror20_2026 | [【バイオハザード レクイエム】ステルスを覚え始めました。＃2【百鬼あやめ/ホロライブ】](https://youtu.be/E1DuNe3uIrY) | [0:30:00–0:50:00](https://youtu.be/E1DuNe3uIrY?t=1800) | 12.1 | 3379 | 280.2 | 283 Hz | 198–449 Hz |
| talkgame25_2026 | [【誰かの心霊写真】ちゃんとしゃべって百鬼さん（？）【百鬼あやめ/ホロライブ】](https://youtu.be/JqaYwRmGKHQ) | [0:05:00–0:30:00](https://youtu.be/JqaYwRmGKHQ?t=300) | 14.6 | 3140 | 215.0 | 288 Hz | 131–475 Hz |
| chat25b_2026 | [【雑談】おはなししよ？【百鬼あやめ/ホロライブ】](https://youtu.be/hhsGMjt_Ix0) | [1:20:00–1:45:00](https://youtu.be/hhsGMjt_Ix0?t=4800) | 18.8 | 5058 | 268.6 | 244 Hz | 177–443 Hz |
| chat30_2026 | [【雑談】おはなししよ？【百鬼あやめ/ホロライブ】](https://youtu.be/hhsGMjt_Ix0) | [0:00:00–0:30:00](https://youtu.be/hhsGMjt_Ix0?t=0) | 17.1 | 4503 | 263.2 | 263 Hz | 183–491 Hz |

"Characters/min of speech" = transcribed kana and kanji (punctuation dropped) ÷ minutes inside whisper's speech segments; it is a rough pace index for comparing windows, not a mora count.

## Marker counts (first model)

| Marker | costume25_2026 | horror20_2026 | talkgame25_2026 | chat25b_2026 | chat30_2026 |
|---|---|---|---|---|---|
| first person 僕 (boku) | 1 | 0 | 0 | 0 | 0 |
| first person 私 | 1 | 0 | 1 | 1 | 1 |
| third person すいちゃん | 0 | 0 | 0 | 0 | 2 |
| なんか | 38 | 21 | 19 | 56 | 46 |
| まあ | 5 | 0 | 2 | 16 | 10 |
| ちょっと待って | 0 | 8 | 2 | 0 | 1 |
| やばい | 4 | 2 | 1 | 0 | 4 |
| かわいい | 33 | 0 | 2 | 3 | 0 |
| えっ/え? | 4 | 10 | 1 | 10 | 2 |
| laugh (はは/ふふ/笑) | 0 | 0 | 0 | 0 | 4 |
| swear (くそ/ふざけ/殺) | 0 | 2 | 0 | 0 | 0 |
| ありがとう | 9 | 0 | 0 | 7 | 2 |
| English (Latin letters) | 3 | 2 | 0 | 3 | 2 |

## Claims checked

| Claim in the file | Result (in the machine transcript) | Evidence (ASR, archived audio) |
|---|---|---|
| Polite with chat at the start, then casual | **Observed**: "Kikoete orimasu deshō ka" ("Can you hear me?") opening the February chat, then casual "maji de," "meccha," "yabē." | [0:07:34](https://youtu.be/hhsGMjt_Ix0?t=454) |
| First person "Yo" (余) | **Observed**; the first model often writes it as 世 ("世が好きな…"), so no line with it is quoted from audio. | [1:22:41](https://youtu.be/hhsGMjt_Ix0?t=4961) |
| Teasing scolds at chat | **Observed**: "Urusai!" … "Mō~" … "komatta hitotachi" ("you troublesome people") when chat teases her. | [1:36:30](https://youtu.be/hhsGMjt_Ix0?t=5790) |
| Scared by horror games | **Confirmed** in Resident Evil Requiem: "Koe ga furuechau" ("my voice is shaking"), "Ima odorokasaretara hontō ni shinzō ga tomarisō" ("if something startles me now my heart might really stop"), a long "ochitsuite, ochitsuite" ("calm down"). | [0:35:07](https://youtu.be/E1DuNe3uIrY?t=2107), [0:46:02](https://youtu.be/E1DuNe3uIrY?t=2762) |
| Persona play | **Observed**: in a photo-hunting horror game (2026-03-19) she talks as a polite narrator who cheers on "Nakiri-san" in the third person. | [0:05:01](https://youtu.be/JqaYwRmGKHQ?t=301) |
| A playful reveal | **Observed** (2026-02-14): she unveils her Valentine's outfit behind a "mosaic roulette," spinning to decide how much to uncover, protests "ステイ！このまま！" ("Stay! Keep it like this!") at a near-miss, and then reads viewers' fan-art guesses. | [0:10:27](https://youtu.be/7RG6f33ZOvU?t=627), [0:13:50](https://youtu.be/7RG6f33ZOvU?t=830) |
| Speech pace and pitch | About 260–270 transcribed characters a minute of speech in chat (slower than Suisei), about 280 in the excited outfit reveal and in the horror game; window medians 244–263 Hz in chat, about 283 Hz in the reveal and the horror game. | — |

Private-life material is excluded under the project's scope rule. The photo-hunting window mixes in game voices; its pitch figures are not used.

## Second model (whisper medium) on quoted lines

| First model (small) | At | Second model (medium), excerpt | Verdict |
|---|---|---|---|
| "聞こえておりますでしょうか" | [0:07:34](https://youtu.be/hhsGMjt_Ix0?t=454) | "ちょっとバタバタしておりましたーすみませんお待たせしましたーこれ聞こえておりますでしょうかちょっと自分の声がうるせぇですねちょっと待ってこんなもんでしょうかどうでしょうか聞こえちゃいますかこんばんはわわ" | **Shared span (computed):** whole line (kana/kanji folded) |
| "うるさい" | [1:36:30](https://youtu.be/hhsGMjt_Ix0?t=5790) | "最近使ってないな持って参るようるさいウェードってちっちゃいよって言うから大きくしたのにごまった人たちくっ" | **Shared span (computed):** whole line (kana/kanji folded) |
| "困った人たち" | [1:36:48](https://youtu.be/hhsGMjt_Ix0?t=5808) | "もう困った人たち声大きいよめんどくせえなもうあれだなこれだなあれやだこれやだ言いやがって" | **Shared span (computed):** whole line (kana/kanji folded) |
| "声が震えちゃう" | [0:35:05](https://youtu.be/E1DuNe3uIrY?t=2105) | "だいぶ近づいたよ、だいぶだいぶガチコン距離で行かせていただいたよし声が震えちゃうこれ何?感染者の血液が入って受血バック使用すると採血キットに補充される採血キットから溢れた分は排気されるえっ、ってことはじゃあ50空きを突っ込んないと排気されちゃうからでも今いけるないけるな入れちゃっ" | **Shared span (computed):** whole line (kana/kanji folded) |
| "今驚かされたら本当に心臓が止まりそう" | [0:46:00](https://youtu.be/E1DuNe3uIrY?t=2760) | "問題はここなんだよねなんか今、今驚かされたら本当に心臓が止まりそう止まってもおかしくないパズルポックスが映っている待って!なに?これは太陽ではないですか?これ、まだこれ、要は手に入れてないやつだよこれこれこれまだ手に入れてない" | **Shared span (computed):** whole line (kana/kanji folded) |
| "落ち着いて落ち着いて" | [0:38:55](https://youtu.be/E1DuNe3uIrY?t=2335) | "落ち着いて落ち着いて殺し切ったほうがいいですから落ち着いてん?落ち着いてよしOK落ち着いて落ち着いて 落ち着いて落ち着け 落ち着け 落ち着け落ち着け 落ち着けいただきましてよしんーで" | **Shared span (computed):** whole line (kana/kanji folded) |
| "いや行きたくねー" | [0:49:05](https://youtu.be/E1DuNe3uIrY?t=2945) | "そもそも出てないからここの先か?まだ見つけられてないここか?いや、行きたくねーいや、行きたくなくて臭っえ、でも行かなきゃ無理だな無理だな、行かなきゃいや、あの先でしょ、絶対え、でもさ、歌姫のことを置いてこんなにさ、ズンズン新エリア開拓してていいのかなっていう気持ちもあるんだけど" | **Shared span (computed):** whole line (kana/kanji folded) |
