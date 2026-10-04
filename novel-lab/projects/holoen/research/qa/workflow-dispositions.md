# GPT program 2026-10-02: plan audit (P1) and workflow research (W1), dispositions

Claude merged both on the author's order of 2026-10-03. Sources:
- `runs/20261002-1715-check-GPT-plan/gpt-free.md` (P1)
- `runs/20261002-1715-research-workflow-SW-EL/gpt-free.md` (W1)

## W1: Sudowrite + ElevenLabs workflow

Platform facts were checked by GPT on 2026-10-02 and are adopted as written. Points that matter here:
- The Text to Dialogue body is `model_id` + `inputs[]` of `text` and `voice_id`. Set `eleven_v4` explicitly, because the endpoint still defaults to v3.
- Keep a request to 2,000 characters in total and at most ten voices.
- v4 has Stability and Similarity only.
- There is no documented public Sudowrite API.
- Hidden cards and traits are unavailable to Sudowrite's AI.

| ID | Disposition |
|---|---|
| WF-001, WF-002 | Applied: `tools/scene_to_elevenlabs.py` and `tools/test_scene_to_elevenlabs.py`. The test imports from its own folder. Claude also extended the converter: a tag-only turn may be any listed sound (sneezes, hiccups, coughs, humming, groans, yawns, vocal percussion, and adjectives such as "dramatic gasp"), not only laughs, sighs, gasps, sobs, screams and snorts. Tests: the fixture passes, all 33 real sheets load, and an end-to-end run against the real sheets covers lint, write, refused overwrite and Japanese with ROMAJI. |
| WF-003 | Applied: `docs/scene-script-format.md`, with a Chinese summary, run commands, the allowed-tag rule and the converter's limits. |
| WF-004 | Applied: `framework/templates/audio-scene-prompt.txt`, shipped as `sudowrite/scene-prompt.txt`. |
| WF-005 | Adapted. The proposed Style made the scene-script format mandatory. Style applies to every generation, so that would turn ordinary prose into scripts. The revised block (119 words) adds the metadata-outside-speech rule, the nonverbal/interjection rule and uncensored swears. It asks for the script format only "when asked for an audio script". The script grammar lives in the scene prompt. V17 passes. |
| WF-006 | Applied. The Style notes point to the script format and the converter's 2,000-unit and ten-voice limits. |
| WF-007 – WF-010, WF-028 | Applied, in Chinese, to `docs/elevenlabs-v4.md`. Voice Design defines an independent fictional voice. Measurements are not used in design. Generation goes through the converter with a record of settings, seed and request IDs. Japanese romanization and glosses go on non-spoken lines, and `pronunciation.tsv` is labelled incomplete. |
| WF-011 – WF-013 | Already satisfied by voice audit v1. Claude also replaced Calli's research-note "Flawless, native-sounding Japanese" with the sheet's no-caricature wording. |
| WF-014 | Applied: Calli's Kobo tag is `[exasperated]`. In the same spirit, partner tags that were descriptions became performable directions: Nerissa ×3, IRyS→Bae, Gura→Ame and Ame→Kronii. |
| WF-015, WF-016 | Generalized. Every card tag missing from its sheet palette (107 across 30 sheets) is listed in §4 as "Additional proposed scene directions from the card's Audio Tags (untested)". |
| WF-017 | Not applied. A sheet tag missing from the card does not block anything. Sudowrite simply won't propose it, and the director can still use it. |
| WF-018 | Applied to all 33 sheets: "## 2. Settings (untested audition choices; verify endpoint behavior)". |
| WF-019 | Applied. V20 now runs the converter fixture and the card-to-sheet palette check, and it passes. |
| WF-020, WF-021 | Applied with P1's V24 fix. Runtime tests include `elevenlabs-japanese`. A failed or unknown outcome blocks. A pass needs all four tests passing with their fields filled. |
| WF-022 | Applied, as P1's fix: the manifest records shipped counts, and V22 compares them with the authorized inventory. |
| WF-023, WF-024 | Adapted. The author reads Chinese, so START-HERE stays in Chinese (`start-here-zh.md`). Its §2 lists the new files. Its §6 now gives the workflow: production folder, original voice design, script via the scene prompt, lint, convert, API or app, a test scene, the Japanese test, and the disclosure line. |
| WF-025 – WF-027 | Applied. The package ships the converter, its test, the script format, the scene prompt and the platform docs. V22 requires them, and V01 hashes them. |
| WF-029 | Applied, in Chinese, to `docs/sudowrite-2026-09.md`. |
| Risks and policy | Adopted. No member clips in Voice Design, Voice Changer or Actor Mode. The proposed disclosure is in START-HERE §6. COVER's song-extraction rule is kept separate from the project's broader no-imitation rule. |
| Open questions 1–5 | Put to the author in the report: audio language, narration, generation route, initial delivery and assembly. Until they answer, the defaults are English with Japanese phrases, narration excluded, both routes supported, private listening files, and either Studio or an editor. |
| Open question 1 (answered 2026-10-04) | **Author decision:** the 14 hololive JP members (including holoX and DEV_IS's Vivi) speak Japanese in audio scripts. Their spoken turns are in Japanese script, with romaji and glosses on ROMAJI/GLOSS lines. EN members stay in English. The cards' Audio Tags and the sheets' §2 state the dialogue language, and the converter rejects a Japanese-language speaker's turn that has no Japanese text. Questions 2–5 keep their defaults. |

## P1: plan audit

| Item | Disposition |
|---|---|
| Stale cohort and bridge prompt counts (18/24, Baelz reference-only) | Fixed before the queue resumed. The cohort prompt lists the 33/28 ownership and reports INCOMPLETE when an owned card is missing. The bridge prompt says 33/28. |
| Shared finding-ID namespace | Fixed: IDs are now per run (MYTH1 … HOLOX, GLOBAL). |
| Voice prompt allowed "labelled secondary transcription" as a quote | Fixed in the prompt and in the queued v4 run. Spoken quotes need the two-model gate. The span_check limit is stated. |
| V24 passed failed tests; the manifest wrote expected counts | Fixed (see WF-020 and WF-022). |
| Validation spec V02 said 18/24/18 | Fixed: it points to the authorized inventory (33/28/33). |
| `qa_runs.py` claimed "seven cohort audits" covered all ties | Wording fixed. |
| holoX audits need canonical cards first | Satisfied. The five holoX cards and the holoX world card were promoted (runs E and F) before the cohort-holoX and voice-v4 runs, which are still queued. |
| Post-merge verification rounds M0–M7 (13 GPT windows) | Accepted as the plan after the current queue. They will be built once Claude's merges of R1–R7 and the cohort audits land. A merge-closure round with nothing changed is closed by hash carry-forward, without spending a GPT window. |
| Deeper release.py hardening (structured attestations, full CSV record equality, candidate staging, stamping only cleared sheets) | Deferred to M0. It is recorded in GPT-PROGRAM.md and not done in this merge. |
| R5/R6 rebalance, bounded R7, temporal-eligibility wording | The research runs have already run. Their dispositions apply the baseline rule: post-2026-09-30 events are out of r01, and a pre-baseline announcement stays an announcement. |
