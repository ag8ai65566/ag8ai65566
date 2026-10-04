# ElevenLabs v4 Performance Sheet: AZKi

> Built from `bible/characters/AZKi.md` (2026-10-02). Original designed voice matched only to register and
> energy; never clone or imitate the member's real voice (ElevenLabs Use Policy §5; COVER Derivative Works
> Guidelines). AZKi is active at the 2026 baseline. She streams in Japanese; her audio dialogue is Japanese
> (author decision 2026-10-04): spoken lines are Japanese script; romaji and glosses are reading aids, not spoken. Guide:
> `novel-lab/docs/elevenlabs-v4.md`.

## 1. Voice Design prompt (original voice; provisional design choices)
"Perfect audio quality. Young woman, clear and warm mid-range singer's voice; poised
and friendly when she talks, a playful lilt for jokes, a bright shout of triumph when she wins a guessing game."
- The original voice's register is an independent design choice; mixed-recording pitch estimates are not synthesis targets.
- Design and preview this voice with Japanese text (the §8 lines). Japanese is the project's dialogue language
  for the original voice, not a claim about the member.

## 2. Settings (untested starting choices; verify endpoint behavior)
- `eleven_v4`. Stability **50%** (API `0.50`) (poised delivery with occasional bursts; an untested starting choice).
  Similarity **75%** (API `0.75`).
- Pace comes from the designed voice plus `[warm, clear]` or `[focused, quick]`; v4 has no speed slider.
- Dialogue language: **Japanese** (author decision 2026-10-04). Write her spoken turns in Japanese script;
  romaji goes on a `ROMAJI ::` line and any English on `GLOSS ::` (neither is spoken).
  `tools/scene_to_elevenlabs.py` rejects a turn of hers that has no Japanese text.

## 3. Write these habits into the script
- A soft 「はい」 ("hai") to close a topic; a drawn-out 「えぇ〜？」 ("e~?") when surprised; 「ちょっとちょっと」 ("chotto chotto") when flustered.
- Grand narration of her own losses: 「戦略的撤退」 ("Senryakuteki tettai," "strategic retreat").
- 「ゲース！」 ("Gēsu!") when locking in an answer; 「ゆか！」/「天井！」 ("Yuka!" / "Tenjō!", "Floor!" / "Ceiling!") for strong feelings (kana for 床, which a voice can misread).
- Puns and mock-villain flourishes; a following giggle is an optional, provisional performance choice.

## 4. Tag palette by situation
| Situation | Tags | Line |
|---|---|---|
| Introduction | `[poised, diva]` | 「バーチャルディーバーあずき、仮想世界の歌姫です」 (shared ASR span, debut parody; the official English profile line is "I'm the Virtual Diva AZKi! I love music and singing!") |
| Chat knows too much (debut parody) | `[mock-flustered]` | 「ちょっとちょっと、なんでそんなみんな情報を持ってるの？」 ("Chotto chotto, naande sonna minna jōhō o motteru no?") |
| Mock villain (debut parody) | `[mock-menacing]` (a following `[giggles]` is optional and provisional) | 「この文字数に恐怖するがいい」 ("Kono mojisū ni kyōfu suru ga ii") |
| Losing a fight | `[mock-dignified]` | 「戦略的撤退」 ("Senryakuteki tettai") |
| A shop price | `[indignant, playful]` | 「ぼったくり！」 ("Bottakuri!") |
| Overwhelmed | `[overjoyed]` | 「ゆか！」 ("Yuka!", official word) |

With people (proposed scene directions, not observed conversational defaults): Suisei `[relaxed, teasing]`;
FUWAMOCO `[cheerful]`; IRyS `[friendly]`.

Additional proposed scene directions from the card's Audio Tags (untested): `[triumphant]`, `[playful]`, `[mock-indignant]`, `[soft, gentle]`, `[nervous]`.

## 5. Signature sounds
- `[giggles]` (tag only; a provisional performance choice); 「えぇ〜？」 ("e~?", spoken).

## 6. Pronunciation (provisional; test)
- Reading guide (untested): あずき; かいたくしゃ. Listen to how the chosen voice says them and adjust.

## 7. Don't
- A cold, aloof diva; constant shouting; a babyish voice.

## 8. Example
```
[poised, diva] バーチャルディーバーあずき、仮想世界の歌姫です。
ROMAJI :: Bācharu dībā AZKi, kasō sekai no utahime desu.
[mock-flustered] ちょっとちょっと、なんでそんなみんな情報を持ってるの？
ROMAJI :: Chotto chotto, naande sonna minna jōhō o motteru no?
[mock-menacing] この文字数に恐怖するがいい。
ROMAJI :: Kono mojisū ni kyōfu suru ga ii.
[mock-dignified] 戦略的撤退。
ROMAJI :: Senryakuteki tettai.
[overjoyed] ゆか！
ROMAJI :: Yuka!
```
(Line 5 is official profile wording. Lines 1–3 are shared ASR excerpts from her April Fools 2026 debut parody; line 4 is a shared ASR excerpt from a game. These are separate examples. Their delivery tags are proposed performance directions, not listening findings. ROMAJI lines are reading aids and are not spoken.)
