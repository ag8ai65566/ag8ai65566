# ElevenLabs v4 Performance Sheet: IRyS

> Source voice fields SHA-256 (Name, Dialogue Style, Catchphrases, Voice & Delivery, Audio Tags): `a7dd2131953841ed0aaca1416d71b070385cd28d4f2dd3609d217f310b894d5f` — reviewed 2026-10-04: Claude 2026-10-04: voice audits v1-v4 merged (research/qa/voice-audit-dispositions.md); attestation research/qa/voice-delivery.md; author decisions 2026-10-04 (quote inventory B; JP members speak Japanese)
> Built from the IRyS character file (`runs/20260930-2334-character-IRyS`, 2026-09-30; update after it is
> promoted to `bible/characters/IRyS.md`; promoted 2026-10-01). Original designed voice matched only to register and energy;
> never clone or imitate the member's real voice (ElevenLabs Use Policy §5; COVER Derivative Works
> Guidelines). Guide: `novel-lab/docs/elevenlabs-v4.md`.

## 1. Voice Design prompt (original voice)

The prompt's timbre, laughter and delivery details are provisional creative choices for the original voice. Performance tags throughout this sheet propose readings; they do not certify how an archived quotation sounded. Regional accents require a separate in-scope listening check.
"Perfect audio quality. Young adult woman, English speech with no prescribed regional accent, soft and bright mid-range voice,
sweet and friendly, speeds up into quick bubbly run-on sentences when excited, light giggles, can drop
into a sly, lower, teasing aside."
- Register basis (sample observations from the audio check, not synthesis targets): mid pitch (≈214–226 Hz in 2026 chat and a horror game), and fast when excited (≈168–183
  words per minute of speech in chat; ≈67 while focused on a horror game). [ASR R20]
- Her singing voice is fuller and more powerful than her talking voice; this sheet covers speech only.

## 2. Settings (untested starting choices; verify endpoint behavior)
- `eleven_v4`. Stability **45%** (API `0.45`) (bubbly, but the sweet base must stay steady). Similarity **75%** (API `0.75`).
- Pace comes from the designed voice plus `[rapid, gushing]` or `[focused, quiet]`; v4 has no speed slider.

## 3. Write these habits into the script
- "like" often (about one word in thirty in chat), "you know," "I do think so," "I mean," "right?"
- Restarts and repeats when excited: "It's so cute. It's so cute."
- Talks to "you guys," almost never "chat."
- Strong profanity is uncommon in the sampled streams ("holy shoot!", "damn it"); her usual edge is innuendo delivered sweetly, then denied.
- Goodbyes that circle several times before she leaves.

## 4. Tag palette by situation
| Situation | Tags | Line |
|---|---|---|
| Opening | `[bright, cheerful]` | "HiRyS, iiiit's IRyS! … Your seiso nephilim here to fill the world with hopium!" (official written greetings) |
| Gushing about an outfit | `[rapid, gushing, delighted]` | "I knew you guys would!" |
| Teasing chat | `[sweet]` → `[sly, lower]` | "I'm trying to make you guys feel guilty. That's what I'm doing here, okay?" |
| After a slip | `[mock-innocent, quick]` | (claims to be "a hundred percent seiso"; the full wiki line is unverified by audio) |
| Outfit speculation | `[innocent]` → `[sly, lightly amused]` | "could pull it off somehow" (ASR excerpt about an outfit; proposed lightly amused reading) |
| Horror game | `[focused, quiet]` → `[short cheer]` | "Run Leon, run!" |
| Surprised | `[gasps]` | "Price, 120 million dollars, holy shoot!" |
| Sincere | `[warm, plain]` | Style demo: "That means a lot. Thank you." |
| Sign-off | `[warm, cheerful]`, repeated | "Thank you very much! See you guys again tomorrow!" |

Additional proposed scene directions from the card's Audio Tags (untested): `[sweet, bright]`, `[mock-bickering]`, `[chaotic, giggly]`, `[competitive, teasing]`, `[cheerful, polite Japanese]`, `[warm senpai]`.

## 5. Signature sounds
- Light giggles: `[light giggle]` (usually, rather than a cackle).
- Lip rolls exist on stream but are hard to direct; skip them rather than overdo them.
- "Yoisho~": `[small effort sound] Yoisho~`.

## 6. Pronunciation (provisional; test)
- IRyS `/ˈaɪɹɪs/` · nephilim `/ˈnɛfɪlɪm/` · hopium `/ˈhoʊpiəm/` · seiso `/ˈseɪsoʊ/` · yabai `/jɑˈbaɪ/` ·
  IRyStocrats `/aɪˈɹɪstəkɹæts/`

## 7. Don't
- Constant swearing; a cold or menacing demon voice as the default; formal idol speech without fillers;
  a seiso act that never slips; a breathy or sexualized read of the innuendo (keep it cheeky and sweet).

## 8. Example
```
[bright, cheerful] HiRyS, iiiit's IRyS! Your seiso nephilim here to fill the world with hopium!
[rapid, gushing] It's so cute. It's so cute!
[sweet] …don't need to see the bottom half.
[sly, lower] I'm trying to make you guys feel guilty. That's what I'm doing here, okay?
[warm, cheerful] Thank you very much! See you guys again tomorrow!
```
(Line 2 is a style demo built from her habits; line 1 is her official written greeting; the others are her lines, quoted only where both transcripts agree; lines 3 and 4 are separate moments, not one utterance.)
