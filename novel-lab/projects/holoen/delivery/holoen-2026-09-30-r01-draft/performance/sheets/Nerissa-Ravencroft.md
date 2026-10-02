# ElevenLabs v4 Performance Sheet: Nerissa Ravencroft

> Built from the Nerissa character file (`runs/20260930-2334-character-Nerissa-Ravencroft`, 2026-09-30;
> promoted 2026-10-01). Original designed voice matched only to register and energy; never clone
> or imitate the member's real voice (ElevenLabs Use Policy §5; COVER Derivative Works Guidelines).
> Guide: `novel-lab/docs/elevenlabs-v4.md`.

## 1. Voice Design prompt (original voice)
"Perfect audio quality. Young adult woman, neutral American accent, warm, relaxed mid-range voice,
relaxed and chatty, playful and teasing, can turn sweet and coaxing or flat and deadpan, big theatrical
swings when telling a story."
- Register basis (sample observations from the audio check, not synthesis targets): mid pitch (≈214 Hz median in a 2026 solo chat, 172–297 Hz) and an easy, fairly quick
  pace (≈159 words per minute of speech). [ASR N20]
- Not a high, cutesy anime voice. Her singing voice is the persona's centerpiece; this sheet covers speech.

## 2. Settings (starting points)
- `eleven_v4`. Stability **40%** (API `0.40`) (she swings between deadpan, coaxing and mock outrage). Similarity **75%** (API `0.75`).

## 3. Write these habits into the script
- "like," "okay," "mind you," "oh my god," "man," and the tag question "You know what I'm saying?"
- Long run-on anecdotes with escalating mock-drama, then "anyway" back to the point.
- Crude or flirty line, flat, often followed by a quick correction.
- Rage-bait claim, then a quick retreat ("I'm sorry. They are donuts.").
- Casual swears, then "I need to stop swearing so much."
- Calls chat "you guys" or "Jailbirds," a friend "girl"; Japanese honorifics ("Kiara-senpai").

## 4. Tag palette by situation
| Situation | Tags | Line |
|---|---|---|
| Opening / hosting | `[bright, theatrical]` | "Hiya Darlings, this is the Devilish Diva, the one and only Nerissa Ravencroft!" (official written introduction, 2026) |
| Chatting | `[relaxed, chatty]` | "You know what I'm saying?" |
| Crude or flirty aside | `[sweet]` → `[flat, deadpan]` → `[quick, brighter]` | "Makes me want to take all my clothes off, but that's inappropriate, so I won't do that." |
| Rage-bait | `[confident, smug]` → `[sheepish, rushed]` | "I'm sorry. They are donuts." |
| Teased by chat | `[mock-whiny]` | "Come on, Jailbirds, be nice, I'm kicking!" |
| Self-aware | `[amused, matter-of-fact]` | (agrees she's weird and says that's why she's a VTuber; paraphrase, the two transcripts differ) |
| Story voice | `[exaggerated caveman voice]` | (a caveman voice: "…go hunt, … get food, … run from big predator") |
| Flirting with a friend | `[sweet, coaxing, low]` | (style demo) "Girl, you know I'd follow you anywhere." |
| Fangirling (Kiara, Marine) | `[excited, flustered, fast]` | (no verified line yet) |

## 5. Signature sounds
- "Ope!": `[startled] Ope!` (short, a little sheepish).
- Mock-dramatic gasps and groans in stories: `[dramatic gasp]`, `[exaggerated groan]`.

## 6. Pronunciation (provisional; test)
- Nerissa `/nəˈɹɪsə/` · Ravencroft `/ˈɹeɪvənkɹɒft/` · Mofufu `/moʊˈfuːfuː/` · Ope `/oʊp/` ·
  senpai `/ˈsɛnpaɪ/` · kohai `/ˈkoʊhaɪ/`

## 7. Don't
- A high anime voice; a prim idol who never swears; a cold demon menace outside a bit; flirting read as
  breathy or explicit (keep it cheeky).

## 8. Example
```
[relaxed, chatty] Okay, so, like, it's so warm today. I can't stand it.
[flat, deadpan] Makes me want to take all my clothes off, [quick, brighter] but that's inappropriate, so I won't do that.
[amused, matter-of-fact] Yeah, I am weird. That's kind of why I'm a VTuber, you know what I'm saying?
```
(Lines 1 and 3 are style demos built from her habits and a paraphrased answer; line 2 is her line, both transcripts agree.)
