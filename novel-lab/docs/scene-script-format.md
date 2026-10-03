# Scene script format (novel-lab audio handoff)

> 中文摘要：要配音的場景用這個純文字格式寫（一行一輪，`全名 :: 台詞`），再用 `tools/scene_to_elevenlabs.py`
> 轉成 ElevenLabs v4 Text to Dialogue 的請求檔和試聽單。這是本專案自訂的格式，不是 Sudowrite 或 ElevenLabs
> 的原生匯入格式。旁白預設不送去合成；STAGE、SFX、PAUSE、ROMAJI、GLOSS 都不會被唸出來。

This is a **project format**, not a native Sudowrite or ElevenLabs import format. Draft prose normally; when a
scene is going to audio, ask Sudowrite for it in this format (Draft/Guided Write with
`framework/templates/audio-scene-prompt.txt` as Extra Instructions), then lint and convert it:

```text
python3 tools/scene_to_elevenlabs.py scenes/s001.scene.txt --voice-map voice-map.json \
    --sheets projects/holoen/export/elevenlabs --lint-only
python3 tools/scene_to_elevenlabs.py scenes/s001.scene.txt --voice-map voice-map.json \
    --sheets projects/holoen/export/elevenlabs --out requests/r01
```

In a delivered package use `performance/tools/scene_to_elevenlabs.py` and `performance/sheets/`. The converter
makes no network calls, takes no keys, never overwrites, and writes one JSON request body (`model_id`
`eleven_v4`, `inputs[]` of `text` + `voice_id`) and one listening sheet per scene. Submit the body to
`POST /v1/text-to-dialogue` with your own client, or follow the listening sheet in the app.

## Grammar

| Element | Required syntax and behavior |
|---|---|
| Encoding | UTF-8 plain text. One physical line per turn or metadata item. No Markdown fences in the saved script. |
| Scene boundary | `@@scene s001`; lowercase ASCII letters, digits, `_` and `-`, maximum 80 characters. IDs must be unique. Each identifies one output request. |
| Scene date | `@@date 2026-09-30`, before scene content. The date is metadata, never spoken. |
| Speaker | `Mori Calliope :: text`; exact canonical card/voice-map name. No aliases, combined speakers or inferred attribution. |
| Tags | One to three directions in the original spoken turn, immediately before affected words. `[casual, fast]` is one complete palette entry; the converter does not automatically permit its components separately. |
| Allowed palette | Bracketed directions in performance-sheet sections **2, 4 and 5**. Section 7 prohibitions and section 8 examples do not grant permission. Case and repeated whitespace are normalized for comparison. |
| Nonverbal sound | A permitted sound tag such as `[laughs]` can occupy a whole turn. Do not also write its vocalization. Duplicate detection is heuristic and requires listening review. |
| Spoken interjection | Write the intended word once with an appropriate delivery direction. The project’s distinction between an interjection and a nonverbal sound is not an acoustic guarantee. |
| Narration | `narrator :: text`, always untagged. Default: excluded from synthesis. `--narrator include` routes it through the map’s `narrator` voice. |
| Stage direction | `STAGE :: description`; retained for the director, excluded from synthesis. Parenthetical directions placed inside a spoken turn remain speech input. |
| SFX | `SFX :: cue description`; excluded from dialogue generation and implemented during assembly. |
| Precise pause | `PAUSE :: 0.4`, in seconds, greater than zero and at most 60. An assembly instruction, not SSML or an API timing guarantee. Conversational pauses within speech use punctuation. |
| Japanese | Spoken text retains Japanese characters. Immediately follow it with `ROMAJI :: ...`; optional `GLOSS :: ...`. Neither is synthesized. Other intended code-switching remains in the spoken turn. |
| Pronunciation override | Prefer a tested versioned dictionary. A tested inline `/IPA/` substitution is allowed; do not append IPA as a second spoken copy of the name. |
| Turn length | Aim below 500 characters including tags. Longer turns are split at sentence/space/Japanese-character boundaries. Tags and slash-delimited pronunciation spans remain intact. Directions are not automatically replayed on continuation fragments. |
| Request length | Project ceiling: 2,000 aggregate text units, conservatively counted as UTF-16 units; ten unique voice IDs maximum. A longer scene must become successive IDs such as `s001a`, `s001b`. |
| Interruptions/overlap | Separate speaker turns remain ordered. Use punctuation for a cut-off; put intentional overlap instructions in STAGE and implement precise overlap during assembly. |
| Comments | `# note`; not spoken. Use a comment to label calibration material as `Style demo: invented lines, not quotations.` |
| Explicit-content marker | Any `【Sudowrite 處理】` marker blocks conversion. It is a hold marker, not material to synthesize. |

Short **Style demo—entirely invented, not quotations**:

```text
@@scene demo
@@date 2026-09-30
# Style demo: invented calibration lines, not quotations.
STAGE :: A game map appears.
Mori Calliope :: [hesitant] Okay, whose map is this?
AZKi :: [mock-dignified] これは練習です。
ROMAJI :: Kore wa renshū desu.
GLOSS :: This is practice.
PAUSE :: 0.4
narrator :: The cursor stops.
Mori Calliope :: [laughs]
```

## Allowed tags

A speaker's allowed directions are the bracketed tags in sections 2, 4 and 5 of that speaker's performance sheet,
which include every tag in the card's Audio Tags trait (`release.py` V20 checks this). The list is the project's
permitted palette, not a complete ElevenLabs vocabulary: v4 tags are free natural-language directions and are
not guaranteed to be followed. Test them with the chosen original voice.

## What the converter does not check

It cannot verify that a voice ID exists, belongs to you or is an original design. It does not establish
quotation provenance (V13), pronunciation correctness or policy compliance, and its duplicate-sound check covers
common forms only. Listen to every take.
