# Audio check — FLOW GLOW: Isaki Riona, Koganei Niko, Mizumiya Su, Rindo Chihaya (2026-11-27)

Method: windows from the public stream archive archive.ragtag.moe (YouTube blocks this environment), the first
8 minutes and the last 7 minutes of two streams per member, transcribed in Japanese with faster-whisper small
(multilingual), pitch measured with Praat (100–600 Hz, speech segments only). Tools and limits:
`novel-lab/tools/audiocheck/README.md`. **This is not a listening check**: the audio was machine-transcribed and
acoustically measured, and the transcripts were reviewed in context. Lines used on the character cards were
re-transcribed by a second model (whisper medium, multilingual, a 30-second clip around the line) and compared after
folding katakana to hiragana and dropping punctuation (see the end of this file). Japanese ASR often picks different
kanji or kana for the same word, and both models mishear names and coined words; only spans both models render the
same way are quoted, and coined words heard as near-matches are reported in romaji. Opening music and game audio
cover some greetings, so "not heard" does not mean "not said". Measurements describe the sampled recording and ASR
segmentation; game audio, music and singing prevent treating them as isolated vocal measurements.

Riona's and Niko's windows are from 2026; Su's and Chihaya's are from August 2025 (no 2026 chat stream of theirs was
picked by the selection rule), so their 2026 manner rests on titles. Only in-scope public performance material is
used: personal remarks in the chats are not quoted or summarized here, and stream labels are neutral.

## Windows measured

| Window | Stream | Segment | Speech (min) | Characters | Characters/min of speech | F0 median | F0 p10–p90 |
|---|---|---|---|---|---|---|---|
| riona_open_uH9A | [2026-10-15 morning game stream — Isaki Riona](https://youtu.be/uH9AFj1qbyA) | [0:00:00–0:08:00](https://youtu.be/uH9AFj1qbyA?t=0) | 2.6 | 725 | 276.1 | 273 Hz | 118–444 Hz |
| riona_end_uH9A | (same stream) | [0:59:06–1:06:06](https://youtu.be/uH9AFj1qbyA?t=3546) | 3.2 | 1038 | 327.3 | 270 Hz | 197–458 Hz |
| riona_open_WJz- | [2026-10-20 morning game stream — Isaki Riona](https://youtu.be/WJz-YOx6fsE) | [0:00:00–0:08:00](https://youtu.be/WJz-YOx6fsE?t=0) | 2.6 | 787 | 298.9 | 256 Hz | 184–360 Hz |
| riona_end_WJz- | (same stream) | [0:57:46–1:04:46](https://youtu.be/WJz-YOx6fsE?t=3466) | 3.5 | 1108 | 321.1 | 273 Hz | 190–416 Hz |
| niko_open_7NOh | [2026-08-08 朝ガオ episode — Koganei Niko](https://youtu.be/7NOhe2tKZLA) | [0:00:00–0:08:00](https://youtu.be/7NOhe2tKZLA?t=0) | 3.8 | 1070 | 281.0 | 292 Hz | 207–425 Hz |
| niko_end_7NOh | (same stream) | [0:52:53–0:59:53](https://youtu.be/7NOhe2tKZLA?t=3173) | 3.7 | 1115 | 298.0 | 263 Hz | 180–428 Hz |
| niko_open_MmkP | [2026-09-12 朝ガオ vol.14 — Koganei Niko](https://youtu.be/MmkPfYSIJ0s) | [0:00:00–0:08:00](https://youtu.be/MmkPfYSIJ0s?t=0) | 3.1 | 377 | 121.9 | 336 Hz | 208–547 Hz |
| niko_end_MmkP | (same stream) | [0:52:12–0:59:12](https://youtu.be/MmkPfYSIJ0s?t=3132) | 5.1 | 1935 | 375.8 | 286 Hz | 194–477 Hz |
| su_open_8fyV | [2025-08-22 morning chat — Mizumiya Su](https://youtu.be/8fyVCoPWMb8) | [0:00:00–0:08:00](https://youtu.be/8fyVCoPWMb8?t=0) | 5.0 | 1288 | 258.8 | 288 Hz | 131–432 Hz |
| su_end_8fyV | (same stream) | [2:14:30–2:21:30](https://youtu.be/8fyVCoPWMb8?t=8070) | 4.4 | 1470 | 334.9 | 301 Hz | 149–480 Hz |
| su_open_ZIke | [2025-08-09 late-night chat — Mizumiya Su](https://youtu.be/ZIkex-Hye6E) | [0:00:00–0:08:00](https://youtu.be/ZIkex-Hye6E?t=0) | 4.9 | 1579 | 323.4 | 312 Hz | 156–471 Hz |
| su_end_ZIke | (same stream) | [2:25:34–2:32:34](https://youtu.be/ZIkex-Hye6E?t=8734) | 3.8 | 1417 | 370.9 | 308 Hz | 152–491 Hz |
| chihaya_open_kNFi | [2025-08-21 late-night chat — Rindo Chihaya](https://youtu.be/kNFiSEYSUeo) | [0:00:00–0:08:00](https://youtu.be/kNFiSEYSUeo?t=0) | 3.7 | 1192 | 326.3 | 248 Hz | 168–443 Hz |
| chihaya_end_kNFi | (same stream) | [2:29:50–2:36:50](https://youtu.be/kNFiSEYSUeo?t=8990) | 4.2 | 1213 | 287.4 | 291 Hz | 198–427 Hz |
| chihaya_open_dtVU | [2025-08-09 chat — Rindo Chihaya](https://youtu.be/dtVUhrM1cPQ) | [0:00:00–0:08:00](https://youtu.be/dtVUhrM1cPQ?t=0) | 3.9 | 1176 | 301.1 | 208 Hz | 150–302 Hz |
| chihaya_end_dtVU | (same stream; mostly singing) | [2:23:12–2:30:12](https://youtu.be/dtVUhrM1cPQ?t=8592) | 4.1 | 544 | 131.7 | 220 Hz | 173–301 Hz |

"Characters/min of speech" = transcribed kana and kanji (punctuation dropped) ÷ minutes inside whisper's speech
segments; it is a rough pace index for comparing windows, not a mora count. niko_open_MmkP is mostly opening music
(121.9 characters a minute) and chihaya_end_dtVU is mostly singing; both are excluded from the ranges on the cards.

## Marker counts (first model, four windows per member)

| Marker | Riona | Niko | Su | Chihaya |
|---|---|---|---|---|
| ニコたん (self) | 0 | 23 | 0 | 0 |
| 水宮 (self) | 0 | 0 | 30 | 0 |
| すう/スー | 0 | 0 | 12 | 0 |
| ちは (self) | 0 | 0 | 0 | 4 |
| リオナ | 3 | 0 | 0 | 0 |
| ほんま | 1 | 2 | 0 | 0 |
| めっちゃ | 3 | 1 | 18 | 4 |
| マジ | 4 | 4 | 5 | 5 |
| なんか | 4 | 15 | 24 | 20 |
| ちょっと待って | 4 | 0 | 0 | 7 |
| ありがとう | 10 | 6 | 57 | 7 |
| かわいい | 6 | 3 | 8 | 1 |
| English (Latin letters) | 5 | 10 | 36 | 2 |

## Claims checked

| Claim in the files | Result (in the machine transcripts) | Evidence (ASR, archived audio) |
|---|---|---|
| Riona welcomes viewers with "okaeri-ona" | **Observed by the second model only** (twice, just before her greeting); the first model's transcript starts after it. Her descriptions write 「おかえりおな〜！」. | [0:03:40](https://youtu.be/uH9AFj1qbyA?t=220) |
| Riona's formal opening | **Observed**: 「それでは挨拶をさせてください」, then "in da house" and FLOW GLOW's leader with her name (the name is misheard differently by each model). | [0:03:42](https://youtu.be/uH9AFj1qbyA?t=222) |
| Riona's sign-off | **Observed**: "bye-bye," a coined "otsu-Riona" (near-match in both models), and in morning streams a cheer for the viewers' day. | [1:04:03](https://youtu.be/uH9AFj1qbyA?t=3843), [1:02:51](https://youtu.be/WJz-YOx6fsE?t=3771) |
| Riona's ending video | **Observed** in both streams: a calm "mindfulness" voice-over that ends by asking viewers to post with the fans' hashtag, subscribe and comment. Paraphrased, not quoted. | [1:03:00](https://youtu.be/WJz-YOx6fsE?t=3780) |
| Niko calls herself "Nikotan" | **Observed** about two dozen times. | [0:58:22](https://youtu.be/MmkPfYSIJ0s?t=3502) |
| Niko's sign-off call | **Observed** in both episodes: "Nikotan ga… kitaku" (both models write 来たく), then "bye-bye." | [0:58:26](https://youtu.be/7NOhe2tKZLA?t=3506), [0:58:22](https://youtu.be/MmkPfYSIJ0s?t=3502) |
| Su's opening | **Observed** in both streams: the coined "shupi-shuwa" (near-match), "Su-charge" and "publicity manager Mizumiya Su." | [0:01:35](https://youtu.be/8fyVCoPWMb8?t=95), [0:01:20](https://youtu.be/ZIkex-Hye6E?t=80) |
| Su calls herself "Mizumiya" | **Observed** about thirty times. | [0:03:36](https://youtu.be/8fyVCoPWMb8?t=216) |
| Su's group goodbye | **Observed** in both streams: "Here we go, ready, set!" then a group "otsu~"; the word after "otsu" differs between the models; "good night." | [2:20:04](https://youtu.be/8fyVCoPWMb8?t=8404), [2:31:12](https://youtu.be/ZIkex-Hye6E?t=9072) |
| Chihaya calls herself "Chiha" | **Observed** (the first model sometimes writes 自派). | [0:06:46](https://youtu.be/kNFiSEYSUeo?t=406), [2:34:11](https://youtu.be/kNFiSEYSUeo?t=9251) |
| Chihaya's polite sign-off | **Observed** in one stream verbatim in both models; "sweet dreams" in both streams. | [2:36:04](https://youtu.be/kNFiSEYSUeo?t=9364), [2:29:17](https://youtu.be/dtVUhrM1cPQ?t=8957) |

## Second model (whisper medium) on quoted lines

| First model (small) | At | Second model (medium), excerpt | Verdict |
|---|---|---|---|
| "それでは挨拶をさせてください" | [0:03:42](https://youtu.be/uH9AFj1qbyA?t=222) | "…かえりょうなーそれでは、あいさつをさせてくださいわたしのもとに…" | Agrees (spelling): the second model writes あいさつ in kana; same words. |
| "フログローのりだ いさきにゃんなねーす" | [0:03:48](https://youtu.be/uH9AFj1qbyA?t=228) | "…インダハンスフログロウのリーダー、いさきりょうなでーす…" | **Partly agrees:** both models hear "in da house" before it and FLOW GLOW's leader with her name; the name is misheard differently, so the line is reported, not quoted |
| "おちにょらでした" | [1:04:03](https://youtu.be/uH9AFj1qbyA?t=3843) | "…バイバーイおつによらでしたーありがと…" | **Not confirmed** as a quotation: both models hear a near-match of a coined sign-off; reported in romaji as "otsu-Riona" |
| "おちによなー" | [1:02:51](https://youtu.be/WJz-YOx6fsE?t=3771) | "…バイバーイありがとーオチリオナーありがとー…" | **Not confirmed** as a quotation: a near-match, as above |
| "ありがとうみんなも今日一日頑張ってね" | [1:04:06](https://youtu.be/uH9AFj1qbyA?t=3846) | "…ありがとみんなも今日一日頑張ってね応援してるよバイバーイ…" | **Partial (computed):** shared run "みんなも今日一日頑張ってね" |
| "応援してるよ" | [1:04:08](https://youtu.be/uH9AFj1qbyA?t=3848) | "…今日一日頑張ってね応援してるよバイバーイ…" | **Shared span (computed):** whole line |
| "それではニコタンが来たくてよろしくお願いします" | [0:58:26](https://youtu.be/7NOhe2tKZLA?t=3506) | "…それではにこたんが来たくでよろしくお願いしますにこたんが来たくバイバーイ…" | Agrees (spelling): both models write 来たく for "kitaku"; the card writes 帰宅 ("going home") as our reading; one model has the particle て, the other で. |
| "それじゃあ2個担が来たくでお願いします" | [0:58:22](https://youtu.be/MmkPfYSIJ0s?t=3502) | "…それじゃあにこたんが来たーくでお願いしますにこたんがー来たーくーばいばーい" | Agrees (spelling): the first model writes 2個担 (read "niko-tan," like ニコたん); both write 来たく. |
| "ほんまにごめん" | [0:58:01](https://youtu.be/7NOhe2tKZLA?t=3481) | "…ほんまにごめんほんまにごめん…" | **Shared span (computed):** whole line |
| "シピシワースーの充電足りてる?" | [0:01:35](https://youtu.be/8fyVCoPWMb8?t=95) | "…シュピシュワースーの充電足りてる…" | **Partial (computed):** shared run "すの充電足りてる"; the coined opening is a near-match (シピシワー / シュピシュワー); the card uses the official spelling |
| "…依頼宣伝担当水宮数です" | [0:01:39](https://youtu.be/8fyVCoPWMb8?t=99) | "…フローグルの依頼宣伝担当水宮数ですお願いします…" | Agrees (spelling): both models write 水宮数 for 水宮枢 (same reading すう); the card quotes 「宣伝担当、水宮枢です」. |
| "いきますよーせーのー" | [2:20:04](https://youtu.be/8fyVCoPWMb8?t=8404) | "…いきますよ、せーのおつ…" | **Shared span (computed):** whole line |
| "おつすれお願いします!" | [2:31:12](https://youtu.be/ZIkex-Hye6E?t=9072) | "…お手伝いお願いします!いきますよーせーの!おうつー…" | **Not confirmed**: the word after "otsu" differs (おつすれ / お手伝い; おつすめ in the other stream); not quoted |
| "おやすみだよー!" | [2:31:16](https://youtu.be/ZIkex-Hye6E?t=9076) | "…おやすみだよーバイバーイ!" | **Shared span (computed):** whole line |
| "こんばんはーということ自雑談でございます" | [0:03:32](https://youtu.be/kNFiSEYSUeo?t=212) | "…こんばんはということで雑談でございますちょっと遅れちゃって…" | **Partial (computed):** shared runs "こんばんはということ" and "雑談でございます"; one mora differs between the models, so only the shared parts are quoted |
| "ということでお疲れ様でした" | [2:36:04](https://youtu.be/kNFiSEYSUeo?t=9364) | "…ということでお疲れ様でした遅くまでお付き合いありがとうございましたまたねー…" | **Shared span (computed):** whole line |
| "遅くまでお付き合いありがとうございました" | [2:36:05](https://youtu.be/kNFiSEYSUeo?t=9365) | "…ということでお疲れ様でした遅くまでお付き合いありがとうございましたまたねー…" | **Shared span (computed):** whole line |
| "いい夢見てね" | [2:36:19](https://youtu.be/kNFiSEYSUeo?t=9379) | "…出てくるといいねいい夢見てねおや…" | **Shared span (computed):** whole line |
| "夢見てね、みんなのおかげで9ヶ月でした" | [2:29:17](https://youtu.be/dtVUhrM1cPQ?t=8957) | "…夢見てねーみんなのおかげで9ヶ月でした1周年までもっともっと…" | **Shared span (computed):** whole line |
| "ニクたち大好きだよ" | [2:29:32](https://youtu.be/dtVUhrM1cPQ?t=8972) | "…これからもよろしくお願いしますニックたち大好きだよ…" | Agrees (spelling): the second model writes ニック, her fans' name; the first writes ニク. |

Per-line output of the second model: scratch file `jconfirm` run of 2026-11-27 (14 clips); the excerpts above are
copied from it, trimmed to the quoted line and cleared of personal remarks.
