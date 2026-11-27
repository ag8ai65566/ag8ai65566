# ElevenLabs v4 Performance Sheet: Mizumiya Su

> Source voice fields SHA-256 (Name, Dialogue Style, Catchphrases, Voice & Delivery, Audio Tags): `12ba35496115cd8c17eaf2951f82060fb47ae06b5df1dd1beac4c0bc8890f2b6` — reviewed 2026-11-27: Claude 2026-11-27 (r02): all 40 sheets checked against the r02 voice-field changes (no removed quote left in a sheet; status and dialogue language match the cards; V20 palettes and span check pass); JP sheets gained the r02 greetings and sign-offs; 7 new sheets (FLOW GLOW, GAMERS); Gemini Neon review pending
> Built from `bible/characters/Mizumiya-Su.md` (2026-11-27). Original designed voice matched only to register and
> energy; never clone or imitate the member's real voice (ElevenLabs Use Policy §5; COVER Derivative Works
> Guidelines). Su is active at the 2026 baseline. She streams in Japanese; her audio dialogue is Japanese
> (author decision 2026-10-04 for the JP members): spoken lines are Japanese script; romaji and glosses are reading
> aids, not spoken. Guide: `novel-lab/docs/elevenlabs-v4.md`. Gemini Neon review pending (Claude-only sheet, 2026-11-27; the author dropped the GPT review).

## 1. Voice Design prompt (original voice; provisional design choices)
"Perfect audio quality. Young woman, light, high, sweet voice with a playful bounce; bright and quick when promoting or thanking people, pouty when teased, soft and sleepy when saying good night."
- The original voice's register is an independent design choice; mixed-recording pitch estimates are not synthesis targets.
- Giggles and timbre are provisional choices for the original voice, not listening observations.
- Design and preview this voice with Japanese text (the §8 lines). Japanese is the project's dialogue language
  for the original voice, not a claim about the member.

## 2. Settings (untested starting choices; verify endpoint behavior)
- `eleven_v4`. Stability **45%** (API `0.45`) (sweet and steady with playful lifts; an untested starting choice).
  Similarity **75%** (API `0.75`), referring only to the selected original voice.
- Pace comes from the designed voice plus `[bubbly, sweet]` or `[sleepy, soft]`; v4 has no speed slider.
- Dialogue language: **Japanese**. Write her spoken turns in Japanese script; romaji goes on a `ROMAJI ::` line and
  any English on `GLOSS ::` (neither is spoken). `tools/scene_to_elevenlabs.py` rejects a turn of hers that has no
  Japanese text.

## 3. Write these habits into the script
- Opens with 「しゅぴしゅわ〜！すうの充電たりてる？」 and 「宣伝担当、水宮枢です」.
- Calls herself 「水宮」 (her surname) more than 「すう」; thanks people one by one.
- Leads a group goodbye: 「いきますよー、せーの！」, then 「おやすみだよー」.
- Pouts when called small. No regional accent is assigned.

## 4. Tag palette by situation
| Situation | Tags | Line |
|---|---|---|
| Default | `[bubbly, sweet]` | **Style demo:** 「水宮ね、それめっちゃ好き！」 ("Mizumiya really loves that!") |
| Opening | `[bright, upbeat]` | 「しゅぴしゅわ〜！すうの充電たりてる？」 (official line) |
| Thanking viewers | `[grateful, quick]` | **Style demo:** 「ありがとう！ありがとうね！」 |
| Promoting | `[upbeat, salesy]` | **Style demo:** 「みんな、これ見てってね！」 ("Everyone, check this out!") |
| Teased about her height | `[pouting]` | **Style demo:** 「すう、成長中だもん！」 ("I'm still growing!") |
| Signing off | `[sleepy, soft]` | 「おやすみだよー」 ("Good night~") |
| A duet partner's turn | `[cheerful]` | **Style demo:** 「次、ヴィヴィの番！」 |

With people (proposed scene directions, not observed conversational defaults): Vivi `[giggly]`; Chihaya `[cheerful]`; Marine `[bossy, playful]`.

## 5. Signature sounds (provisional; tag plus a written word is a scripting convention, not a guarantee of engine behavior)
- `[giggles]` (tag only); 「おいしょ」 ("oisho," spoken)

## 6. Pronunciation (provisional; test)
- Reading guide (untested): みずみや すう; しゅぴしゅわ; すうりす. Listen to how the chosen voice says them and adjust.

## 7. Don't
- A low, sultry or mature voice, cool aloofness, or a slow monotone.

## 8. Example
```
[bright, upbeat] しゅぴしゅわ〜！すうの充電たりてる？
ROMAJI :: Shupi-shuwa! Sū no jūden tariteru?
[grateful, quick] ありがとう！ありがとうね！
ROMAJI :: Arigatō! Arigatō ne!
[sleepy, soft] おやすみだよー。
ROMAJI :: Oyasumi da yo.
```
(Line 1 is her official line; line 2 is a Style demo; line 3 is a shared ASR span. ROMAJI lines are reading aids and are not spoken.)
