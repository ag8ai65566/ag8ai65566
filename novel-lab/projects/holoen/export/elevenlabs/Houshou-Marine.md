# ElevenLabs v4 Performance Sheet: Houshou Marine

> Built from `bible/characters/Houshou-Marine.md` (2026-10-02). Original designed voice matched only to register and
> energy; never clone or imitate the member's real voice (ElevenLabs Use Policy §5; COVER Derivative Works
> Guidelines). Marine is active at the 2026 baseline. She streams in Japanese; her audio dialogue is Japanese
> (author decision 2026-10-04): spoken lines are Japanese script; romaji and glosses are reading aids, not spoken. Guide:
> `novel-lab/docs/elevenlabs-v4.md`.

## 1. Voice Design prompt (original voice; provisional design choices)
"Perfect audio quality. Young woman, bright, brassy, mature-sounding mid-high voice; rapid-fire and comic, jumping into shrieks when startled and loud cackles; switches on demand to a cutesy idol voice."
- The original voice's register is an independent design choice; mixed-recording pitch estimates are not synthesis targets.
- Laughter, shrieks, breathiness and timbre are provisional choices for the original voice, not listening observations.
- Design and preview this voice with Japanese text (the §8 lines). Japanese is the project's dialogue language
  for the original voice, not a claim about the member.

## 2. Settings (untested starting choices; verify endpoint behavior)
- `eleven_v4`. Stability **35%** (API `0.35`) (big comic swings; an untested starting choice).
  Similarity **75%** (API `0.75`), referring only to the selected original voice.
- Pace comes from the designed voice plus `[energetic, brassy]` or `[panicked, rapid]`; v4 has no speed slider.
- Dialogue language: **Japanese** (author decision 2026-10-04). Write her spoken turns in Japanese script;
  romaji goes on a `ROMAJI ::` line and any English on `GLOSS ::` (neither is spoken).
  `tools/scene_to_elevenlabs.py` rejects a turn of hers that has no Japanese text.

## 3. Write these habits into the script
- "Ahoy!" (official) to open, said inside a Japanese turn; calls herself 「船長」 ("Senchō," Captain); official 「ヨーソロー」 (yōsorō); her sign-off is 「出航！」 ("Shukkō!", set sail; both ASR models, two 2026 streams).
- Rapid, emphatic delivery for game reactions; pace and volume follow the scene.
- Regroups out loud: 「一回落ち着こうよ」 ("let's calm down for a sec").
- Flips into a cutesy idol voice for a bit, then straight back. Crude jokes keep their teasing register; nothing explicit.

## 4. Tag palette by situation
| Situation | Tags | Line |
|---|---|---|
| Opening | `[bright, theatrical]` | "Ahoy!" (official; say it inside a Japanese turn, as in §8 line 1) |
| Startled | `[panicked, rapid]` | **Style demo:** 「うわっ、なになになに！？」 ("Uwa, nani nani nani!?", "Whoa, what what what!?") |
| Regrouping | `[comic, self-scolding]` | 「一回落ち着こうよ」 ("Ikkai ochitsukō yo," "let's calm down for a sec") |
| Arguing with a game | `[rough, comic]` | **Style demo:** 「バカ言うな！」 ("Baka iu na!", "Don't be stupid!") |
| Idol mode | `[cutesy, sweet]` | **Style demo:** 「船長のこと、好きになっちゃダメだよ♡」 ("Senchō no koto, suki ni naccha dame da yo♡", "You mustn't fall for the Captain♡") |
| Closing | `[bright]` | 「出航！」 ("Shukkō!", shared ASR span) |

With people (proposed scene directions, not observed conversational defaults): Pekora `[bickering, fond]`; Suisei `[playful]`; Kiara `[playful, teasing]`; FUWAMOCO `[doting]`.

Additional proposed scene directions from the card's Audio Tags (untested): `[mischievous]`, `[warm]`.

## 5. Signature sounds (provisional; tag plus a written word is a scripting convention, not a guarantee of engine behavior)
- "Ahoy!" (spoken, inside a Japanese turn)
- `[cackles]` (tag only); `[shrieks]` (tag only)

## 6. Pronunciation (provisional; test)
- Reading guide (untested): ほうしょう まりん; せんちょう; ようそろー; しゅっこう. Listen to how the chosen voice says them and adjust.

## 7. Don't
- Not as default: quiet, shy, slow or sleepy delivery. Pace and volume follow the scene. Keep humor non-explicit.

## 8. Example
```
[bright, theatrical] Ahoy! 船長の宝鐘マリンです！
ROMAJI :: Ahoy! Senchō no Houshou Marine desu!
[panicked, rapid] うわっ、なになになに！？
ROMAJI :: Uwa, nani nani nani!?
[comic, self-scolding] 一回落ち着こうよ。
ROMAJI :: Ikkai ochitsukō yo.
[cutesy, sweet] 船長のこと、好きになっちゃダメだよ♡
ROMAJI :: Senchō no koto, suki ni naccha dame da yo♡
[bright] それでは行きますよー！出航ー！
ROMAJI :: Sore de wa ikimasu yō! Shukkō!
```
(Line 1 joins her official "Ahoy!" to a style-demo self-introduction; line 3 is her line and line 5 her sign-off,
each quoted only where both transcripts agree; lines 2 and 4 are style demos. ROMAJI lines are reading aids and are
not spoken.)
