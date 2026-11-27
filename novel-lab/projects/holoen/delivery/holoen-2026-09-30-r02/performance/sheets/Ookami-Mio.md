# ElevenLabs v4 Performance Sheet: Ookami Mio

> Source voice fields SHA-256 (Name, Dialogue Style, Catchphrases, Voice & Delivery, Audio Tags): `d3d412d03fa23abf783afc6aecc896360e494b64606704e89b92a66c0ba09ccc` — reviewed 2026-11-27: Claude 2026-11-27 (r02): all 40 sheets checked against the r02 voice-field changes (no removed quote left in a sheet; status and dialogue language match the cards; V20 palettes and span check pass); JP sheets gained the r02 greetings and sign-offs; 7 new sheets (FLOW GLOW, GAMERS); GPT review pending
> Built from `bible/characters/Ookami-Mio.md` (2026-11-27). Original designed voice matched only to register and
> energy; never clone or imitate the member's real voice (ElevenLabs Use Policy §5; COVER Derivative Works
> Guidelines). Mio is active at the 2026 baseline. She streams in Japanese; her audio dialogue is Japanese
> (author decision 2026-10-04 for the JP members): spoken lines are Japanese script; romaji and glosses are reading
> aids, not spoken. Guide: `novel-lab/docs/elevenlabs-v4.md`. GPT review pending (Claude-only sheet, 2026-11-27).

## 1. Voice Design prompt (original voice; provisional design choices)
"Perfect audio quality. Young woman, warm, mellow mid-range voice, gentle and composed; even, conversational pacing like a friendly morning radio host; softer and lower late at night; grand and theatrical when she plays a fortune-teller; bright when she sings or wins."
- The original voice's register is an independent design choice; mixed-recording pitch estimates are not synthesis targets.
- Laughter and timbre are provisional choices for the original voice, not listening observations.
- Design and preview this voice with Japanese text (the §8 lines). Japanese is the project's dialogue language
  for the original voice, not a claim about the member.

## 2. Settings (untested starting choices; verify endpoint behavior)
- `eleven_v4`. Stability **55%** (API `0.55`) (calm and steady by default; an untested starting choice).
  Similarity **75%** (API `0.75`), referring only to the selected original voice.
- Pace comes from the designed voice plus `[warm, gentle]` or `[soft, calm]`; v4 has no speed slider.
- Dialogue language: **Japanese**. Write her spoken turns in Japanese script; romaji goes on a `ROMAJI ::` line and
  any English on `GLOSS ::` (neither is spoken). `tools/scene_to_elevenlabs.py` rejects a turn of hers that has no
  Japanese text.

## 3. Write these habits into the script
- Calls herself 「うち」 (uchi); greets 「おはみぉーん！」 in the morning and 「こんばんみぉーん！大神ミオだよ～！」 (official) at night, stacking 「うちうち、うちだよ」 (written in her titles) before her name.
- Runs her morning show like radio: a corner reading viewers' posts, next week's theme, then goodbye.
- Signs off 「それではまた明日ねー」 or 「また明日会いましょう、じゃあねー」, then "otsu-mion" (spell it おつみぉーん in a script; untested).
- As "Big God Mion" she reads tarot in a grand, playful oracle voice.
- No regional accent is assigned.

## 4. Tag palette by situation
| Situation | Tags | Line |
|---|---|---|
| Default | `[warm, gentle]` | **Style demo:** 「今日もゆっくりしていってね」 ("Take it easy here today too") |
| Morning opening | `[bright, cheerful]` | 「おはみぉーん！」 (her titles) |
| Reading posts | `[attentive, warm]` | **Style demo:** 「おー、おいしそう！ありがとう〜」 ("Ooh, that looks tasty! Thank you~") |
| Tarot reading | `[mysterious, playful]` | **Style demo:** 「ビッグゴッドミオーンが占ってしんぜよう」 ("Big God Mion shall read your fortune") |
| Horror | `[nervous]` | **Style demo:** 「待って待って、こわいこわい！」 ("Wait, wait, scary, scary!") |
| Late-night chat | `[soft, calm]` | **Style demo:** 「今日はまったりいこうね」 ("Let's take it slow tonight") |
| Saying goodbye | `[gentle]` | 「それではまた明日ねー」 ("Well then, see you tomorrow") |

With people (proposed scene directions, not observed conversational defaults): Fubuki `[playful, teasing]`; Korone `[amused]`; Okayu `[relaxed]`.

## 5. Signature sounds (provisional; tag plus a written word is a scripting convention, not a guarantee of engine behavior)
- `[laughs softly]` (tag only)

## 6. Pronunciation (provisional; test)
- Reading guide (untested): おおかみ みお; うち; おはみぉーん (ohamyōn); こんばんみぉーん (konbanmyōn); ミオファ (Mio-fam). Listen to how the chosen voice says them and adjust.

## 7. Don't
- A shrill, hyper idol voice, a cold, clipped read or frantic speed.

## 8. Example
```
[bright, cheerful] おはみぉーん！
ROMAJI :: Ohamyōn!
[mysterious, playful] ビッグゴッドミオーンが占ってしんぜよう。
ROMAJI :: Biggu Goddo Mion ga uranatte shinzeyō.
[gentle] それではまた明日ねー。
ROMAJI :: Soredewa mata ashita ne.
```
(Line 1 is her written greeting; line 2 is a Style demo; line 3 is a shared ASR span. ROMAJI lines are reading aids and are not spoken.)
