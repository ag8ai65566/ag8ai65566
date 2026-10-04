# Cohort audit: jp (Suisei, AZKi, Ayame, Okayu, JP Senpai Pairs; GPT xhigh; merged by Claude 2026-10-04)

Source run: `runs/20261002-0751-check-QA-cohort-jp/gpt-free.md`. Coverage: complete, 5/5 owned cards.
Claude merged it on the author's order of 2026-10-03, with `tools/audit_apply.py --tag jp`. The tool now also accepts `A/` locators for research/audio-check/.
Promotions are author decisions (`research/qa/promotions.md`). With the other cohort audits, this file attests V11, V12 and V15 for the jp cards.

## Claude's dispositions

All 22 finding rows were applied by the tool.
- **Scope (CLAUDE-SCOPE-002 ×6, JP-SCOPE-001).**
  - Exclusion notes in the AZKi and Okayu cards and in four audio reports no longer name what was excluded. The technical audio notes are kept.
  - The AZKi ASR excerpt keeps the approved span, and its surrounding context is replaced by a bracketed non-spoken note.
  - Claude applied the same rule beyond the audit:
    - The generic topic list "(family, childhood, health, trips, daily life)" was removed from 14 more audio reports, and Fauna's report no longer names topics.
    - The audio-status notes of Nerissa, Fauna and Mumei now say only that private details are excluded.
- **Relationships (JP-CREDIT-001, JP-TIE-001/002).**
  - Okayu's export says she contributed chorus vocals to Chloe's cover.
  - The unsupported "JP senior"/"JP kouhai" labels between AZKi, Okayu, Noel and Marine are now "hololive collaborator". Debut order contradicted several of them.
  - AZKi's export separates KoZMy (Koyori and Lamy) from the four-person 3D karaoke (Koyori, Riona, Niko).
- **Rules and records (JP-STATUS-001, JP-EVENT-001, JP-ALIAS-001, JP-UNIT-001, MYTH-TIE-002, MYTH-EVENT-002).**
  - JP Senpai Pairs' Rules give baseline status and use each member's status at a historical scene's date. A title shows advertised content, not a held collaboration.
  - "Death Star" is labelled a fan-wiki pair label.
  - holoX distinguishes the 2026 Hoshimatic credits from Chloe's earlier, secondary-sourced lineup.
  - Calli's "starstruck" characterization is marked unverified.
  - Suisei's unresolved UNCUT ROCK!! row is no longer dated, so the registry no longer lists it as a dated event.

Deferred:
- **JP-QUOTE-001 (P0 before release).** Secondary-only spoken quotations remain: Suisei's "Hi, honey!", AZKi's "kono yarō" and Ayame's "Yo da yo!" and horns answer. The same pattern exists on other cards, so these go to the project-wide quotation pass in `research/qa/voice-delivery.md`, after voice audit v4. Each quote either gets a two-model ASR check on an identified window or is paraphrased out of the exports. V13 stays blocked until then.
- **MYTH-EVENT-002.** The Suisei–Calliope appearance stays unresolved until a direct event locator is found.

---

# GPT report (verbatim)

## Coverage

**Owned-card coverage: COMPLETE, 5/5. Release clearance remains open.**

Snapshot: git 0b372b1. Baseline: **2026-09-30**. Checked: **2026-10-04**.

The supplied snapshot assurance satisfies hash verification. No hashes were computed or compared.

| Input | Recorded identity |
|---|---|
| Owned packet | `b257d52167d14d6bc321fc49bdc39d290e116f3b102cb98fb83f6025a5f37ec5` |
| Incoming packet | `9f27ba9e135e2b7d95b97d294b1108bb18008d5b7914c8d758de9726e35944ed` |
| Registry | Commit `0b372b1`; baseline `2026-09-30`; separate registry hash not supplied |
| Source-hash manifest | `projects/holoen/research/qa/manifest.json`, built `2026-10-04T10:13Z`; 61 source files |
| Owned source hashes | Suisei `cc7453e0e0dc`; AZKi `f9ef7601a752`; Ayame `675a9db7cbb2`; Okayu `80148bfc0586`; JP Senpai Pairs `26d530531779` |

Examined all **67 [SW] fields**, the four character Relationship Maps, Background Timelines and Hard Facts, and the world card’s relationship sections, History and Hard Facts. All four character Roles are `Protagonist`.

Incoming coverage included the supplied packet and a case-insensitive search across all 61 bible files using canonical names, aliases, Japanese forms and shared units. Additional unit-only rows and their context were checked. Missing reciprocal entries were not treated as contradictions.

The inline constitution, shared rules and resolution ledger were read. Registry status intervals, units, credits and relevant event records were examined, together with targeted passages in the four audio reports and relevant earlier audit findings.

**Freshly verified:** the archived chorus credits for Chloe’s cover; the archived “BEEP BEEP” vocal credits and official release date; relevant official profile data for Okayu, AZKi and Noel. Other external evidence is **inherited, not reopened**. YouTube and the attempted ckworks page for Chloe’s cover were inaccessible; its archived description was accessible. No audio was independently heard.

No required owned card or manifest was missing. Initial tool-output truncation was addressed with targeted reads of the required sections. No snapshot change was identified. No `runs/` files were accessed, files modified or sub-agents launched.

Quotation clearance remains incomplete for previously deferred secondary-only speech transcriptions, detailed below. Later website content was not used to advance the baseline.

## Findings

Paths below are relative to `projects/holoen/`: `C/` = `bible/characters/`; `W/` = `bible/world/`; `A/` = `research/audio-check/`. `<br>` represents an existing newline. Each old-text target below was located exactly once in its specified file.

| ID | Priority | Claim key | File + field/line | Exact old text | Problem | Exact replacement | Evidence URL + type + checked date | Propagate to | Author decision? |
|---|---|---|---|---|---|---|---|---|---|
| CLAUDE-SCOPE-002 | P0 | `cast[AZKi].excluded-process-notes` | `C/AZKi.md` › opening Audio status | Personal remarks (family, childhood, trips) are not quoted or<br>> summarized here. | Residual of the existing finding: a member-specific removal note records excluded subject matter. | The project's public-persona scope applies to the reviewed material. | Binding scope and existing ledger; local check 2026-10-04. | Audio report; merge notes | No |
| CLAUDE-SCOPE-002 | P0 | `cast[Nekomata Okayu].excluded-process-notes` | `C/Nekomata-Okayu.md` › opening Audio status | A remark about her off-stream schedule is not<br>> used. | Same residual defect. | The project's public-persona scope applies to the reviewed material. | Binding scope and existing ledger; local check 2026-10-04. | Audio report; merge notes | No |
| CLAUDE-SCOPE-002 | P0 | `cast[Hoshimachi Suisei].excluded-process-notes` | `A/suisei.md` › paragraph before Second model | Not used: long stretches of the chat about family, childhood games, a trip home and a trip abroad (personal matters). | The exclusion note retains specific excluded material. Preserve the following technical note about mixed game audio. | Private-life material is excluded under the project's scope rule. | Binding scope and existing ledger; local check 2026-10-04. | Audio-report owner | No |
| CLAUDE-SCOPE-002 | P0 | `cast[AZKi].excluded-process-notes` | `A/azki.md` › paragraph before Second model | Not used: remarks in the April Fools stream about her family and childhood, and her travel habits (personal matters). | Same residual defect. | Private-life material is excluded under the project's scope rule. | Binding scope and existing ledger; local check 2026-10-04. | Audio-report owner | No |
| CLAUDE-SCOPE-002 | P0 | `cast[Nakiri Ayame].excluded-process-notes` | `A/ayame.md` › paragraph before Second model | Not used: most of the February chat (dance practice, physical complaints, seasonal allergies, taxi rides, gifts, an injury), which is about personal matters. | Same residual defect. Preserve the following technical note about game voices. | Private-life material is excluded under the project's scope rule. | Binding scope and existing ledger; local check 2026-10-04. | Audio-report owner | No |
| CLAUDE-SCOPE-002 | P0 | `cast[Nekomata Okayu].excluded-process-notes` | `A/okayu.md` › paragraph before Second model | Not used: a story about her off-stream schedule at the start of the Final Fantasy VII window, and a stream title about an illness (personal matters). | Same residual defect. Preserve the following technical note about mixed audio. | Private-life material is excluded under the project's scope rule. | Binding scope and existing ledger; local check 2026-10-04. | Audio-report owner | No |
| JP-SCOPE-001 | P0 | `cast[AZKi].ASR-context-scope` | `A/azki.md` › Second model › 0:17:10 › medium excerpt | 小さい 頃 から今 まで に 影響 を 受け て き たアーティスト さん 音楽 編 歴 | The surrounding transcription retains excluded personal-history context beyond the useful performance span. | [Private-life material removed; this bracketed note is not spoken text.] | [Identified window](https://youtu.be/Y5BPxMCI6oU?t=1030), ASR: faster-whisper small / whisper medium. Report examined 2026-10-04; recording not reopened. | Task 09: keep the approved performance span separate from edited context | No |
| JP-CREDIT-001 | P1 | `cast[Nekomata Okayu].credits[Bling-Bang-Bang-Born]` | `C/Nekomata-Okayu.md` › `[SW] Relationships` | Sakamata Chloe: chorus on her "Bling-Bang-Bang-Born" cover (2025). | The compressed relationship entry reverses or obscures the contributor and cover owner. Both dossiers and the archived credits identify Okayu as a chorus contributor to Chloe’s cover. | Sakamata Chloe: Okayu contributed chorus vocals to Chloe's "Bling-Bang-Bang-Born" cover (2025). | [Archived upload description](https://archive.ragtag.moe/watch?v=wxnTKRkpePs), ARCHIVE_METADATA, freshly checked 2026-10-04; upload dated 2025-01-24. | Okayu export; retain the correctly directed dossier rows; notify holoX owner | No |
| JP-TIE-001 | P1 | `cast[AZKi].relationships[Nekomata Okayu]` | `C/AZKi.md` › Relationship Map | \| Nekomata Okayu \| JP senior \| | This ranking conflicts with the recorded debut order; the cited collaboration metadata does not establish a different seniority convention. Use the supported collaboration relation. | \| Nekomata Okayu \| hololive collaborator \| | Registry debut intervals; [Okayu profile](https://hololive.hololivepro.com/en/talents/nekomata-okayu/), OFFICIAL, freshly checked 2026-10-04. No direct-address evidence established. | Linked reciprocal patch | No |
| JP-TIE-001 | P1 | `cast[Nekomata Okayu].relationships[AZKi]` | `C/Nekomata-Okayu.md` › Relationship Map | \| AZKi \| JP kouhai \| | Reciprocal instance of the unsupported ranking. | \| AZKi \| hololive collaborator \| | Same registry comparison; [AZKi profile](https://hololive.hololivepro.com/en/talents/azki/), OFFICIAL Generation 0 listing, freshly checked 2026-10-04. | AZKi map | No |
| JP-TIE-001 | P1 | `cast[AZKi].relationships[Shirogane Noel]` | `C/AZKi.md` › Relationship Map | \| Shirogane Noel \| JP senior \| | The event citation establishes participation, not this rank; the registry records AZKi’s earlier debut. | \| Shirogane Noel \| hololive collaborator \| | Registry; [Noel profile](https://hololive.hololivepro.com/en/talents/shirogane-noel/), OFFICIAL debut date, freshly checked 2026-10-04. | Linked reciprocal patch; JP2 owner | No |
| JP-TIE-001 | P1 | `cast[Shirogane Noel].relationships[AZKi]` | `C/Shirogane-Noel.md` › Relationship Map | \| AZKi \| JP kouhai \| | Reciprocal instance of the unsupported ranking. | \| AZKi \| hololive collaborator \| | Same registry and profile comparison, checked 2026-10-04. | JP2 owner; AZKi map | No |
| JP-TIE-001 | P1 | `cast[AZKi].relationships[Houshou Marine]` | `C/AZKi.md` › Relationship Map | \| Houshou Marine \| JP senior \| | The commentary credit does not establish seniority; the registry records AZKi’s earlier debut. | \| Houshou Marine \| hololive collaborator \| | Registry dates and cited event metadata, inherited/not reopened; local comparison 2026-10-04. | Linked reciprocal patch; JP2 owner | No |
| JP-TIE-001 | P1 | `cast[Houshou Marine].relationships[AZKi]` | `C/Houshou-Marine.md` › Relationship Map | \| AZKi \| JP kouhai \| | Reciprocal instance of the unsupported ranking. | \| AZKi \| hololive collaborator \| | Same inherited evidence; local comparison 2026-10-04. | JP2 owner; AZKi map | No |
| JP-TIE-001 | P1 | `cast[Nekomata Okayu].relationships[Shirogane Noel]` | `C/Nekomata-Okayu.md` › Relationship Map | \| Shirogane Noel \| JP senior \| | The cards call each other senior. Official dates place Okayu’s debut before Noel’s; the shared contest needs no rank claim. | \| Shirogane Noel \| hololive collaborator \| | [Okayu](https://hololive.hololivepro.com/en/talents/nekomata-okayu/) and [Noel](https://hololive.hololivepro.com/en/talents/shirogane-noel/), OFFICIAL debut dates, freshly checked 2026-10-04; reciprocal maps examined. | JP2 owner | No |
| JP-TIE-002 | P1 | `cast[AZKi].events[2026-02-03-karaoke].participants` | `C/AZKi.md` › `[SW] Relationships` | Hakui Koyori and Yukihana Lamy: "KoZMy" cover partners on "Ai♡Scream!" (2025), and a 3D karaoke with Koyori, Isaki Riona and Koganei Niko (2026); | The plural subject can carry Lamy into the unrelated karaoke. Both Relationship Maps identify a four-person event and expressly distinguish it from KoZMy. | Hakui Koyori and Yukihana Lamy: "KoZMy" cover partners on "Ai♡Scream!" (2025). Koyori also joined AZKi, Isaki Riona and Koganei Niko for a four-person 3D karaoke (2026); | [Cited karaoke archive](https://www.youtube.com/watch?v=1HQL3WJPBHA), ARCHIVE_METADATA, inherited/not reopened; AZKi and Koyori maps compared 2026-10-04. | AZKi export; holoX owner | No |
| JP-UNIT-001 | P2 | `Hoshimatic Project.historical-lineup-and-song-credits` | `W/holoX.md` › With the other Japanese members on the cards | Suisei: Hoshimatic Project with Koyori, Chloe and Iroha. | The compressed roster loses the historical distinction retained in Suisei’s and Chloe’s cards. Song credits establish participation in that work, not an all-time roster. | Suisei: Hoshimatic Project; Koyori and Iroha are credited on "BEEP BEEP" (2026), while secondary sources place Chloe in the earlier lineup. | [Archived vocal credits](https://archive.ragtag.moe/watch?v=kPqmld3_lSs), ARCHIVE_METADATA, freshly checked 2026-10-04; earlier lineup SECONDARY, inherited/not reopened. | holoX owner; preserve historical Chloe material | No |
| MYTH-TIE-002 | P1 | `Mori Calliope ↔ Hoshimachi Suisei / withheld-characterization` | `W/JP-Senpai-Pairs.md` › Hoshimachi Suisei with the cast | Calli's own card describes her as starstruck by Suisei (secondary;<br>  the pair name and reaction stay here in the dossier). | Residual propagation failure: Calli’s current card explicitly withholds this characterization. Suisei’s map also marks it unverified. | [Unverified: the secondary characterization of Calli as starstruck.] | Calli and Suisei Relationship Maps; existing MYTH-TIE-002. SECONDARY source not reopened; local comparison 2026-10-04. | Myth1 and Global owners; reopen only this residual | No |
| MYTH-EVENT-002 | P1 | `Hoshimachi Suisei / UNCUT-ROCK-guest-identification` | `C/Hoshimachi-Suisei.md` › Background Timeline › unresolved Calliope appearance row | \| 2026-04-04 \| [Unverified: identification | The event text says its date is unverified, but the date cell still generates a day-precision registry event. | \| Date unverified \| [Unverified: identification | Existing MYTH-EVENT-002; [SU20 window](https://youtu.be/GQMY5Vl9Dfk?t=4371), ASR report examined locally 2026-10-04; recording not reopened. | Regenerate the corresponding registry event and packet; Myth1 owner | No |
| JP-STATUS-001 | P1 | `world[JP Senpai Pairs].historical-scene-status` | `W/JP-Senpai-Pairs.md` › `[SW] Rules` | Gura and Mumei appear only as memories; Ame is an affiliate. | The unrestricted rule excludes active-period historical scenes, contradicting the dated collaborations retained in this card. | At the 2026-09-30 baseline, Gura and Mumei are graduates and Ame is an affiliate. Historical scenes use each member's status at the scene's date. | Binding baseline rule and registry status intervals; local comparison 2026-10-04. | World export; scene-continuity checks | No |
| JP-EVENT-001 | P1 | `world[JP Senpai Pairs].metadata-evidence-rule` | `W/JP-Senpai-Pairs.md` › `[SW] Rules` | A collab title shows that a collab happened, not how close two members are. | A title can describe scheduled or advertised content. It does not alone prove a held collaboration or attendance. | A title identifies advertised content; confirmation that a collaboration occurred requires evidence of the broadcast. Neither establishes private closeness. | Binding ARCHIVE_METADATA rule; local check 2026-10-04. | World export; retain announcement/held-event distinctions | No |
| JP-ALIAS-001 | P2 | `world[JP Senpai Pairs].aliases[Death Star].evidence` | `W/JP-Senpai-Pairs.md` › Glossary | \| Death Star \| Calli and Suisei \| fans, titles \| | “Titles” adds evidence not identified here. Calli’s map specifically classifies the name as a fan-wiki label. | \| Death Star \| Calli and Suisei \| fan-wiki pair label (secondary) \| | Calli Relationship Map and existing source classification; SECONDARY, not reopened; local comparison 2026-10-04. | Keep dossier-only treatment; no alias promotion | No |

## New verified facts

None.

## Merge handoff

Recommended propagation order:

1. **Accept the scope repairs first:** the six residual `CLAUDE-SCOPE-002` patches and `JP-SCOPE-001`. Preserve technical audio limitations and approved in-scope spans. New merge notes should say only that excluded material was removed.
2. **Accept the material consistency fixes:** `JP-CREDIT-001`, `JP-TIE-001`, `JP-TIE-002`, `JP-STATUS-001`, `JP-EVENT-001`, and the residuals under `MYTH-TIE-002` and `MYTH-EVENT-002`.
3. **Optional clarity fixes:** accept `JP-UNIT-001` and `JP-ALIAS-001`. Neither requires removing supported historical collaborations.
4. Update the resolution ledger with these individual dispositions. Existing IDs retain their identities; their earlier “applied” status does not close the newly identified residual locations.
5. Regenerate the registry, source manifest, JP packets and affected incoming packets. The unresolved Suisei appearance must cease appearing as an established day-precision event. Rebuild affected exports after the source edits.

The following evidence work remains open; it is not a request to reopen the underlying persona claims:

| ID | Priority | Affected material | Required disposition |
|---|---|---|---|
| JP-QUOTE-001 | P0 before release | Suisei: secondary-only Duolingo greeting in Voice Profile, Catchphrases and Audio Tags. AZKi: secondary-only prank insult in Voice Profile, Personality and Catchphrases. Ayame: secondary-only stock introduction and horns question in Voice Profile, Tone Shifts, Sample Lines, Personality and Catchphrases. | Continue the previously deferred task 09 quotation gate. The examined audio reports do not supply identified shared spans for these particular quotations. Supply both models, the same audio window, an explicit contiguous approved span and independent speaker attribution; otherwise use attributed dossier paraphrase and remove unsupported verbatim speech from exports. Preserve any verified profanity unchanged. Inspect derived performance sheets as part of propagation. |
| MYTH-EVENT-002 | P1 | Identification and event date of Suisei’s reported Calliope appearance | Keep unresolved after removing the falsely precise date cell. A direct event locator is still required before restoring a dated attendance claim. |

Downstream owners: **JP2** for Marine/Noel relationship labels; **holoX** for Chloe’s credit and Hoshimatic chronology; **Myth1/Global** for existing residual IDs; **task 09** for quotation clearance; **tasks 10–11** for regenerated release artifacts and validation.

Material P1 contradictions still block consistency validation until resolved. This audit recommends changes; it does not claim they were merged or authorize promotion.

**Open questions**

None.