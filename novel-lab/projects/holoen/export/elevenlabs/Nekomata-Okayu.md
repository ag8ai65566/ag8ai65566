# ElevenLabs v4 Performance Sheet: Nekomata Okayu

> Built from `bible/characters/Nekomata-Okayu.md` (2026-10-02). Original designed voice matched only to register
> and energy; never clone or imitate the member's real voice (ElevenLabs Use Policy §5; COVER Derivative Works
> Guidelines). Okayu is active at the 2026 baseline. She streams in Japanese; her audio dialogue is Japanese
> (author decision 2026-10-04): spoken lines are Japanese script; romaji and glosses are reading aids, not spoken. Guide:
> `novel-lab/docs/elevenlabs-v4.md`.

## 1. Voice Design prompt (original voice; provisional design choices)
"Perfect audio quality. Young woman, soft, relaxed, boyish voice; lazy and warm, unhurried with trailing vowels,
a playful purr when teasing, a laugh that climbs high."
- The climbing laugh follows a secondary description; the purr is an original performance choice. Neither is a
  listening observation.
- This is an original voice-design choice. Mixed-recording F0 and ASR character-rate measurements are
  descriptive research data, not synthesis targets or evidence of the member's isolated vocal range.
- Design and preview this voice with Japanese text (the §8 lines). Japanese is the project's dialogue language
  for the original voice, not a claim about the member.

## 2. Settings (untested starting choices; verify endpoint behavior)
- `eleven_v4`. Stability **50%** (API `0.50`) (relaxed and steady). Similarity **75%** (API `0.75`).
- Pace comes from the designed voice plus `[relaxed, warm]` or `[playful]`; v4 has no speed slider.
- Dialogue language: **Japanese** (author decision 2026-10-04). Write her spoken turns in Japanese script;
  romaji goes on a `ROMAJI ::` line and any English on `GLOSS ::` (neither is spoken).
  `tools/scene_to_elevenlabs.py` rejects a turn of hers that has no Japanese text.

## 3. Write these habits into the script
- 「僕」 ("boku") for "I"; 「もぐもぐ〜おかゆ〜！」 ("Mogu mogu~ Okayu~!") to greet; 「おにぎりゃー」 ("Onigiryā") for her fans.
- 「ノリで」 ("nori de," "by vibes") appears in one sampled game opening; use it as a situational example. 「レッツラゴー！」 ("Rettsura gō!") is a documented start cue; repeated 「にゃ」 ("nya") is documented during play.
- Narrating her own play in long, relaxed sentences; agreeing with everyone.
- Flirty teasing kept light and non-explicit.

## 4. Tag palette by situation
| Situation | Tags | Line |
|---|---|---|
| Greeting | `[lazy, warm]` | 「もぐもぐ〜おかゆ〜！」 ("Mogu mogu~ Okayu~!", official greeting as romanized in her profile) |
| Starting a game | `[breezy]` | 「ノリで相手をぶっ倒したいと思いまーす」 ("Nori de aite o buttaoshitai to omoimāsu") |
| Exploring a new game | `[contented, chatty]` | 「新しいゲームだから、みんなと一緒に手探り探索なの楽しいなぁ」 ("Atarashii gēmu dakara, minna to issho ni tesaguri tansaku na no tanoshii nā") |
| A move that feels good | `[pleased]` | 「にゃにゃにゃにゃ」 ("Nya nya nya nya") |
| Teasing a member | `[playful]` | **Style demo:** 「かわいいねぇ」 ("Kawaii nē") |
| Found guilty | `[cheerful, unbothered]` | **Style demo:** 「はい、有罪です。償います。」 ("Hai, yūzai desu. Tsugunaimasu.") |
| Laughing hard | `[laughs harder]` | (tag only) |

With people (proposed scene directions, not observed conversational defaults): Korone `[comfortable, fond]`;
Ina `[mellow]`; FUWAMOCO `[fond senpai, teasing]`.

Additional proposed scene directions from the card's Audio Tags (untested): `[easygoing]`, `[soft, tearful]`.

## 5. Signature sounds
- 「もぐもぐ」 ("mogu mogu", spoken); repeated 「にゃ」 ("nya", spoken; documented); `[laughs]` (tag only).

## 6. Pronunciation (provisional; test)
- Japanese reading: ねこまた おかゆ; おにぎりゃー. No regional accent is assigned without an in-scope listening
  check. Listen to how the chosen voice says them and adjust.

## 7. Don't
- Not as default: a high, sugary voice or harsh, aggressive delivery. Stronger reactions follow the scene. Keep flirting non-explicit.

## 8. Example
```
[lazy, warm] もぐもぐ〜おかゆ〜！
ROMAJI :: Mogu mogu~ Okayu~!
[breezy] ノリで相手をぶっ倒したいと思いまーす。
ROMAJI :: Nori de aite o buttaoshitai to omoimāsu.
[contented, chatty] 新しいゲームだから、みんなと一緒に手探り探索なの楽しいなぁ。
ROMAJI :: Atarashii gēmu dakara, minna to issho ni tesaguri tansaku na no tanoshii nā.
[pleased] にゃにゃにゃにゃ。
ROMAJI :: Nya nya nya nya.
[playful] かわいいねぇ。
ROMAJI :: Kawaii nē.
```
(Line 1 is her official greeting; line 5 is a style demo; lines 2–4 are her lines, quoted only where both
transcripts agree; the number of 「にゃ」 in line 4 is illustrative, not fixed. ROMAJI lines are reading aids and are
not spoken.)
