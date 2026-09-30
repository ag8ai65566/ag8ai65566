# ElevenLabs v4 Performance Sheet: IRyS

> Built from the IRyS character file (`runs/20260930-2334-character-IRyS`, 2026-09-30; update after it is
> promoted to `bible/characters/IRyS.md`). Original designed voice matched only to register and energy;
> never clone or imitate the member's real voice (ElevenLabs Use Policy §5; COVER Derivative Works
> Guidelines). Guide: `novel-lab/docs/elevenlabs-v4.md`.

## 1. Voice Design prompt (original voice)
"Perfect audio quality. Young adult woman, neutral American accent, soft and bright mid-range voice,
sweet and friendly, speeds up into quick bubbly run-on sentences when excited, light giggles, can drop
into a sly, lower, teasing aside."
- Register basis: mid pitch (≈214–226 Hz in 2026 chat and a horror game), and fast when excited (≈168–183
  words per minute of speech in chat; ≈67 while focused on a horror game). [ASR R20]
- Her singing voice is fuller and more powerful than her talking voice; this sheet covers speech only.

## 2. Settings (starting points)
- `eleven_v4`. Stability **45** (bubbly, but the sweet base must stay steady). Similarity **75**.
- Pace comes from the designed voice plus `[rapid, gushing]` or `[focused, quiet]`; v4 has no speed slider.

## 3. Write these habits into the script
- "like" often (about one word in thirty in chat), "you know," "I do think so," "I mean," "right?"
- Restarts and repeats when excited: "I knew you guys would! I knew you guys would!"
- Talks to "you guys," almost never "chat."
- Mild words only ("holy shoot!"); the edge is innuendo delivered sweetly, then denied.
- Goodbyes that circle several times before she leaves.

## 4. Tag palette by situation
| Situation | Tags | Line |
|---|---|---|
| Opening | `[bright, cheerful]` | "HiRyS, it's IRyS! Your seiso nephilim here to fill the world with hopium!" (official greeting) |
| Gushing about an outfit | `[rapid, gushing, delighted]` | "I'm glad you guys liked the outfit. I knew you guys would!" |
| Teasing chat | `[sweet]` → `[sly, lower]` | "I'm trying to make you guys feel guilty. That's what I'm doing here, okay?" |
| After a slip | `[mock-innocent, quick]` | "I am a hundred percent seiso, I would never lie!" (wiki quote) |
| Yabai aside | `[innocent]` → `[slight smirk]` | "I mean, I am a half-angel, half-demon Nephilim. I could pull it off, somehow." |
| Horror game | `[focused, quiet]` → `[short cheer]` | "Run Leon, run!" |
| Surprised | `[gasps]` | "Price, 120 million dollars, holy shoot!" |
| Sincere | `[warm, plain]` | "I really hope so too." |
| Sign-off | `[warm, cheerful]`, repeated | "Thank you very much! See you guys again tomorrow!" |

## 5. Signature sounds
- Light giggles: `[light giggle]` (not a cackle).
- Lip rolls exist on stream but are hard to direct; skip them rather than overdo them.
- "Yoisho~": `[small effort sound] Yoisho~`.

## 6. Pronunciation (test)
- IRyS `/ˈaɪɹɪs/` · nephilim `/ˈnɛfɪlɪm/` · hopium `/ˈhoʊpiəm/` · seiso `/ˈseɪsoʊ/` · yabai `/jɑˈbaɪ/` ·
  IRyStocrats `/aɪˈɹɪstəkɹæts/`

## 7. Don't
- Constant swearing; a cold or menacing demon voice as the default; formal idol speech without fillers;
  a seiso act that never slips; a breathy or sexualized read of the innuendo (keep it cheeky and sweet).

## 8. Example
```
[bright, cheerful] HiRyS, it's IRyS! Your seiso nephilim here to fill the world with hopium!
[rapid, gushing] Okay, okay, so, like, the outfit? I knew you guys would like it. I knew you guys would!
[sweet] You guys don't need to see the bottom half. [sly, lower] I'm trying to make you guys feel guilty. That's what I'm doing here, okay?
[warm, cheerful] Thank you very much! See you guys again tomorrow!
```
(Line 2 is a style demo built from her habits; the others are her lines.)
