# Sudowrite Style: audio-ready dialogue (ElevenLabs v4)

Paste the block below into Sudowrite's **Story Bible → Style** box (under the project's own style notes,
about 120 words; wording from GPT's 2026-10-01 review, revised 2026-10-03 for the scene-script handoff). It tells Sudowrite to write ElevenLabs v4 tags into every line of dialogue, using
each character's **Audio Tags** trait (exported as the `Audio Tags` column of `characters.csv`).

```text
Write dialogue for original designed voices, never to reproduce a member's identifiable voice. Place one to three brief square-bracket performance directions from the speaker's Audio Tags trait inside each spoken turn, before the words affected. Change delivery only when the scene warrants it. Preserve her established fillers, restarts, repetitions, code-switching and uncensored swears without forcing a quota. Use a tag alone for a nonverbal sound ([laughs]); never also spell it out. Spoken interjections stay words with a delivery direction ([startled squawk] GWAK!). Keep narration untagged, and keep stage directions, sound effects, romanization and glosses out of spoken words. Use punctuation for pauses. Tags are provisional until tested. When asked for an audio script, follow the supplied scene-script format exactly.
```

## Notes
- Tags are performance directions for an **original** designed voice. Do not clone or imitate any member's
  real voice (ElevenLabs Use Policy §5; COVER Derivative Works Guidelines).
- For audio, draft the scene in the scene-script format (`docs/scene-script-format.md`; give Sudowrite
  `framework/templates/audio-scene-prompt.txt` as Extra Instructions), then run `tools/scene_to_elevenlabs.py`.
  Narration is excluded unless `--narrator include` is chosen. Each request must fit the converter's
  2,000-unit budget and ten-voice limit; longer scenes become successive scene IDs (s001a, s001b).
- If Sudowrite overuses tags, lower it to "one or two tags" in the Style text; if it drifts to generic
  tags ([happy], [sad]), add "Use only tags listed in the speaker's Audio Tags trait."
- Guide: `novel-lab/docs/elevenlabs-v4.md`.
