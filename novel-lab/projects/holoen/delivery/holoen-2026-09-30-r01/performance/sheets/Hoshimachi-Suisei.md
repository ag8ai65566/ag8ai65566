# ElevenLabs v4 Performance Sheet: Hoshimachi Suisei

> Source voice fields SHA-256 (Name, Dialogue Style, Catchphrases, Voice & Delivery, Audio Tags): `08c23773fee8a482ff3d7d40a43cc63d033e493f575cee53bae9eeaf0976db53` — reviewed 2026-10-04: Claude 2026-10-04: voice audits v1-v4 merged (research/qa/voice-audit-dispositions.md); attestation research/qa/voice-delivery.md; author decisions 2026-10-04 (quote inventory B; JP members speak Japanese)
> Built from `bible/characters/Hoshimachi-Suisei.md` (2026-10-02). Original designed voice matched only to
> register and energy; never clone or imitate the member's real voice (ElevenLabs Use Policy §5; COVER
> Derivative Works Guidelines). Suisei is active at the 2026 baseline. She streams in Japanese; her audio dialogue is Japanese
> (author decision 2026-10-04): spoken lines are Japanese script; romaji and glosses are reading aids, not spoken. Guide:
> `novel-lab/docs/elevenlabs-v4.md`.

## 1. Voice Design prompt (original voice; provisional design choices)
"Perfect audio quality. Young woman, clear and bright mid-high voice, polished and confident; quick and fluent
when chatting, sing-song and stretched when she calls herself cute, crisp and clipped when competing."
- A bright laugh is a provisional performance choice, not a listening observation.
- The original voice's register is an independent design choice; mixed-recording pitch estimates are not synthesis targets.
- Design and preview this voice with Japanese text (the §8 lines). Japanese is the project's dialogue language
  for the original voice, not a claim about the member.

## 2. Settings (untested starting choices; verify endpoint behavior)
- `eleven_v4`. Stability **45%** (API `0.45`) (polished by default, playful swings for the signature line).
  Similarity **75%** (API `0.75`).
- Pace comes from the designed voice plus `[quick, enthusiastic]` or `[focused, clipped]`; v4 has no speed
  slider.
- Dialogue language: **Japanese** (author decision 2026-10-04). Write her spoken turns in Japanese script;
  romaji goes on a `ROMAJI ::` line and any English on `GLOSS ::` (neither is spoken).
  `tools/scene_to_elevenlabs.py` rejects a turn of hers that has no Japanese text.

## 3. Write these habits into the script
- Third person for herself: 「スイちゃん」 ("Sui-chan"); the stretched signature 「スイちゃんは〜今日も可愛い〜」 ("Sui-chan wa~ kyō mo kawaii~").
- Quick 「え？」 ("e?") reactions; 「ちょっと待って」 ("chotto matte," "wait a sec"); fillers 「なんか」「まぁ」「ね」.
- Mock innocence when caught: 「いやいやいや、私は悪くない」 ("Iya iya iya, watashi wa warukunai"). Separately, a mock-rough 「俺は悪くねぇ」 ("Ore wa warukunē") (two ASR excerpts nine seconds apart, not one spoken turn).
- Occasional short English inside a Japanese turn ("Hi, honey!", a secondary transcription associated with her Duolingo stream).

## 4. Tag palette by situation
| Situation | Tags | Line |
|---|---|---|
| Introduction | `[polished, idol-bright]` | 「彗星のごとく現れたスターの原石！バーチャルアイドルの星街すいせいでーす！」 (official Japanese introduction) |
| Signature line | `[sing-song, playful]` | 「スイちゃんは〜今日も可愛い〜」 ("Sui-chan wa~ kyō mo kawaii~") |
| Caught in a mistake | `[mock-innocent]` → `[mock-gruff]` | Separate ASR excerpts, not one spoken turn: 「いやいやいや、私は悪くない」 (00:05:39); 「俺は悪くねぇ」 (00:05:48). |
| Age joke | `[breezy, firm]` | 「スイちゃんは18歳だよ」 ("Sui-chan wa jūhassai da yo") |
| Tales tangent | `[quick, enthusiastic]` | 「これはテイルズが大好きな話です」 ("Kore wa Teiruzu ga daisuki na hanashi desu") |
| Competitive game | `[focused, clipped]` | 「もう一回。今度は勝てる。」 ("Mō ikkai. Kondo wa kateru.") (style demo) |

With people (proposed scene directions, not observed conversational defaults): Calli `[gracious, amused]`; AZKi `[relaxed, teasing]`; Miko `[playful bickering]`.

Additional proposed scene directions from the card's Audio Tags (untested): `[bright, confident]`, `[sweet]`, `[deadpan]`, `[warm]`.

## 5. Signature sounds
- `[laughs]` (tag only); 「え？」 ("e?", spoken).

## 6. Pronunciation (provisional; test)
- Reading guide (untested): ほしまち すいせい; すいちゃん; ほしよみ. Listen to how the chosen voice says them and adjust.

## 7. Don't
- A breathy or babyish idol voice; a cold, menacing read (the "psychopath" bit is a joke); mumbling.

## 8. Example
```
[polished, idol-bright] 彗星のごとく現れたスターの原石！バーチャルアイドルの星街すいせいでーす！
ROMAJI :: Suisei no gotoku arawareta sutā no genseki! Bācharu aidoru no Hoshimachi Suisei dēsu!
[sing-song, playful] スイちゃんは〜今日も可愛い〜
ROMAJI :: Sui-chan wa~ kyō mo kawaii~
[mock-innocent] いやいやいや、私は悪くない。
ROMAJI :: Iya iya iya, watashi wa warukunai.
[breezy, firm] スイちゃんは18歳だよ。
ROMAJI :: Sui-chan wa jūhassai da yo.
[focused, clipped] もう一回。今度は勝てる。
ROMAJI :: Mō ikkai. Kondo wa kateru.
```
(Line 1 is her official Japanese introduction; line 5 is a style demo; lines 2–4 are her lines, quoted only
where both transcripts agree. ROMAJI lines are reading aids and are not spoken; in a scene script each one follows
her turn.)
