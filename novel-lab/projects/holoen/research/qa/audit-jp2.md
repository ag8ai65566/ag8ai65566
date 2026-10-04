# Cohort audit: jp2 (Marine, Noel, Lamy, Botan, Vivi, JP Senpai Pairs 2; GPT xhigh; merged by Claude 2026-10-04)

Source run: `runs/20261002-0751-check-QA-cohort-jp2/gpt-free.md` (snapshot e8bdd89, before the jp merge). Coverage: complete.
Claude merged it on the author's order of 2026-10-03, with `tools/audit_apply.py --tag jp2` and by hand.
Promotions are author decisions (`research/qa/promotions.md`). With the other cohort audits, this file attests V11, V12 and V15 for the jp2 cards.

## Claude's dispositions

- **JP2-SCOPE-001 (applied).** Fauna's Voice Profile keeps only "she describes her speaking manner as soft-spoken". In `research/audio-check/fauna.md`, the three occurrences of the excluded clause are marked as omitted. The 1:14:21 verdict now says the line is scope-redacted, so it no longer approves the whole line as spoken wording. All of this was done by hand, because the tool needs a single occurrence. span_check still finds 0 quotes outside a shared span.
- **JP2-TIE-001 (partly applied).** This audit and jp agree that the old senior/kouhai labels were reversed. jp, merged first, set AZKi's rows with Marine, Noel and Okayu to "hololive collaborator".
  - That neutral label is kept for AZKi. Her 2018 start predates the others' debuts, but she joined hololive itself in 2022, which is the transfer the audit's own source announces. Seniority there is a convention the sources do not settle.
  - Okayu's row for Noel is now "JP kouhai". Okayu debuted first, and this matches Noel's own row.
- **JP2-ROSTER-003.** Already resolved by jp:JP-TIE-002.
- **JP2-CREDIT-001 (applied).** Botan's and Nerissa's exports and Nerissa's map make clear that Nerissa guested at Botan's birthday live. The resulting 354 words in Nerissa's Relationships were trimmed to 349.
- **JP2-STATUS-001, JP2-EVENT-001 (applied).** JP Senpai Pairs 2's Rules now match JP Senpai Pairs: baseline status, the status at a historical scene's date, and billing versus occurrence.
- **JP2-ROSTER-001/002 (applied).** The original Fantasy and fifth-generation lineups (Rushia and Aloe, reference-only) are now kept apart from current or sub-unit lineups.
- **JP2-ALIAS-001, JP2-TIE-003 (applied).** "TREVIAN KNIGHT" uses the official spelling on the twins' cards. FUWAMOCO's Description says "Their public ties extend to all of Advent".
- **JP2-TIE-002 (applied by hand).** Both occurrences on Kiara's card now say "the Minecraft company 'Usada Kensetsu'".

---

# GPT report (verbatim)

## Coverage

**Cohort coverage: COMPLETE. Release validation remains blocked by the scope finding and material relationship corrections below.** This is an audit and merge recommendation; no files were modified.

**Snapshot:** `git e8bdd89`, factual baseline **2026-09-30**. The supplied snapshot assurance satisfies the hash-comparison step; no hashes were computed or compared.

Recorded packet SHA-256 values from `projects/holoen/research/qa/manifest.json`, built `2026-10-04T10:26Z`:

| Input | Recorded SHA-256 |
|---|---|
| `jp2.md` | `a75d1f19e3f02494efa507af61683714e6a4a59f83e704614ee9d8a1e87c3200` |
| `jp2-incoming.md` | `fc213fb7e062717bf07582b802d268d97473b5d0387e6f6bf37402ae0ef45e1d` |

The registry identifies baseline `2026-09-30` and commit `e8bdd89`. A standalone registry digest was not supplied and was not computed. Its unit and credit indexes explicitly describe themselves as bounded and non-exhaustive.

The manifest records all six owned files:

| File | Recorded source-hash prefix |
|---|---|
| `bible/characters/Houshou-Marine.md` | `363cad47c8c7` |
| `bible/characters/Shirogane-Noel.md` | `383c370fae8f` |
| `bible/characters/Yukihana-Lamy.md` | `bd7bdb48bd86` |
| `bible/characters/Shishiro-Botan.md` | `40c78f4b1201` |
| `bible/characters/Kikirara-Vivi.md` | `e3dae5035b02` |
| `bible/world/JP-Senpai-Pairs-2.md` | `aeeee4dd9074` |

**Examined:** every owned `[SW]` field; all five character Relationship Maps, Background Timelines and Hard Facts; the world card’s relationship sections, History and Hard Facts; supplied incoming claims; registry records; manifest; resolution ledger; relevant source and merge notes. All five character Roles are `Protagonist`.

Case-insensitive searches across the **33 character and 28 world cards** included canonical names, aliases, Japanese names, pair names and units. They returned 43 files: six owned files, 35 relevant incoming files, and two incidental matches confined to a merge note or unrelated word. Unit-only matches and surrounding bullets were also inspected. No owned card was missing.

**Freshly verified on 2026-10-04:** Botan’s birthday-live identity and Nerissa’s guest credit; AZKi’s public activity-start date; Okayu’s debut date; the historical Fantasy and fifth-generation rosters; the official spelling of `TREVIAN KNIGHT`; and Blue Journey’s roster. Relevant links appear below. Blue Journey’s roster agrees with the incoming Botan/Koyori/Lui claims; Botan’s shorter Groups field is not a contradiction.

**Inherited evidence, not reopened:** other collaboration records, status announcements, secondary observations and existing ASR attestations. Selected quotation rows in the five JP2 audio reports were inspected; no audio was listened to or newly transcribed. Lamy’s report explicitly approves its complete thank-you line, although the displayed medium-model excerpt is shorter. That omission alone does **not** establish a quotation mismatch or justify reversing the earlier review.

The attempted archive openings for `8RjOCCH2sac` and `q_IXZIRCbwI` returned errors. Their collaboration evidence remains inherited; the failed openings do not disprove it.

No snapshot changes or missing required inputs were reported. Some initial tool output was truncated; required owned-field passages were recovered through narrower reads. No `runs/` files were opened. Detailed voice enrichment, release-package validation and unrelated isolated claims remain outside this audit.

For compact locators below, `C/`, `W/` and `A/` mean `projects/holoen/bible/characters/`, `projects/holoen/bible/world/` and `projects/holoen/research/audio-check/`. Old-text cells are literal replacement targets; `<br>` represents an existing newline.

## Findings

| ID | Priority | Claim key | File + field/line | Exact old text | Problem | Exact replacement | Evidence URL + type + checked date | Propagate to | Author decision? |
|---|---|---|---|---|---|---|---|---|---|
| JP2-SCOPE-001 | P0 | `voice[Fauna].public_scope` | `C/Ceres-Fauna.md` › Voice Profile › self-description | "I'm pretty soft-spoken. And talking in my head voice like this does not strain my<br>    voice at all." | The speaking-style observation is eligible; the physiological assertion exceeds this task’s scope. | She describes her speaking manner as soft-spoken. | [F20 source window](https://youtu.be/iIBywcAIMD0?t=4461), ASR; inherited, not reopened. Local scope check 2026-10-04. | Promise owner; linked audio-report patches below. | No |
| JP2-SCOPE-001 | P0 | Same | `A/fauna.md` › Claims checked, 1:14:21; Second model, 1:14:21, both model columns — three occurrences | does not strain my voice at all | The same excluded assertion survives in the supporting report. An explicit redaction preserves the distinction between recorded wording and approved material. | [scope-excluded clause omitted] | Same [F20 window](https://youtu.be/iIBywcAIMD0?t=4461), ASR; not reopened. Local check 2026-10-04. | All three specified occurrences; regenerate dependent evidence extracts. | No |
| JP2-SCOPE-001 | P0 | Same | `A/fauna.md` › Second model › 1:14:21 verdict only | **Shared span (computed):** whole line | After scope redaction, the verdict must not approve the entire displayed, edited line as spoken wording. | **Scope-redacted:** only the public speaking-style observation is retained for use; omitted text and editorial markers are not approved quotations. | Same [F20 window](https://youtu.be/iIBywcAIMD0?t=4461), ASR; not reopened. Local check 2026-10-04. | Task 09 evidence checks. | No |
| JP2-TIE-001 | P1 | `seniority[AZKi,Marine]` | `C/Houshou-Marine.md` › Relationship Map › AZKi | \| AZKi \| JP kouhai \| | Reverses debut-based seniority. AZKi began public activities in 2018; Marine debuted in 2019. | \| AZKi \| JP senior \| | [AZKi announcement](https://hololive.hololivepro.com/news/20221111-01-101/), OFFICIAL, opened 2026-10-04; Marine’s 2019 debut is also supported by the [Fantasy report](https://hololive.hololivepro.com/events/fanfunisland/), OFFICIAL, opened 2026-10-04. | Reciprocal AZKi row below; relationship extraction. | No |
| JP2-TIE-001 | P1 | `seniority[AZKi,Marine]` | `C/AZKi.md` › Relationship Map › Marine | \| Houshou Marine \| JP senior \| | Reciprocal reversal of the same relationship. | \| Houshou Marine \| JP kouhai \| | [AZKi announcement](https://hololive.hololivepro.com/news/20221111-01-101/) and [Fantasy report](https://hololive.hololivepro.com/events/fanfunisland/), OFFICIAL, opened 2026-10-04. | JP owner; Marine row above. | No |
| JP2-TIE-001 | P1 | `seniority[AZKi,Noel]` | `C/Shirogane-Noel.md` › Relationship Map › AZKi | \| AZKi \| JP kouhai \| | AZKi’s 2018 start precedes Noel’s 2019 debut. | \| AZKi \| JP senior \| | [AZKi announcement](https://hololive.hololivepro.com/news/20221111-01-101/) and [Fantasy report](https://hololive.hololivepro.com/events/fanfunisland/), OFFICIAL, opened 2026-10-04. | Reciprocal AZKi row below. | No |
| JP2-TIE-001 | P1 | `seniority[AZKi,Noel]` | `C/AZKi.md` › Relationship Map › Noel | \| Shirogane Noel \| JP senior \| | Reciprocal reversal of the same relationship. | \| Shirogane Noel \| JP kouhai \| | [AZKi announcement](https://hololive.hololivepro.com/news/20221111-01-101/) and [Fantasy report](https://hololive.hololivepro.com/events/fanfunisland/), OFFICIAL, opened 2026-10-04. | JP owner; Noel row above. | No |
| JP2-TIE-001 | P1 | `seniority[Okayu,Noel]` | `C/Nekomata-Okayu.md` › Relationship Map › Noel | \| Shirogane Noel \| JP senior \| | Okayu debuted in April 2019, before Noel. Noel’s reciprocal Okayu row already gives the correct direction. | \| Shirogane Noel \| JP kouhai \| | [Okayu profile](https://hololive.hololivepro.com/en/talents/nekomata-okayu/) and [Fantasy report](https://hololive.hololivepro.com/events/fanfunisland/), OFFICIAL, opened 2026-10-04. | JP owner; preserve Noel’s correct reciprocal row. | No |
| JP2-CREDIT-001 | P1 | `events[Stray&Stay,2026].host_guest` | `C/Shishiro-Botan.md` › `[SW] Relationships` | Nerissa Ravencroft: a guest at her birthday 3D live "Stray&Stay" (2026). | The pronoun permits the host and guest to be reversed. The source names Botan’s birthday live and credits Nerissa as a guest. | Nerissa Ravencroft: credited as a guest in Botan's birthday 3D live "Stray&Stay" (2026). | [Birthday-live metadata](https://tw.yutura.net/channel/35550/video/cI535pJp-TQ/), ARCHIVE_METADATA, opened 2026-10-04. | Nerissa export and map below; registry directional records. | No |
| JP2-CREDIT-001 | P1 | Same | `C/Nerissa-Ravencroft.md` › `[SW] Relationships` | Shishiro Botan: a guest at her birthday live "Stray&Stay" (2026). | In Nerissa’s card this reads as Botan guesting at Nerissa’s birthday live, contrary to the credited event. | Shishiro Botan: Nerissa is credited as a guest in Botan's birthday 3D live "Stray&Stay" (2026). | [Birthday-live metadata](https://tw.yutura.net/channel/35550/video/cI535pJp-TQ/), ARCHIVE_METADATA, opened 2026-10-04. | Advent owner; Botan export above. | No |
| JP2-CREDIT-001 | P1 | Same | `C/Nerissa-Ravencroft.md` › Relationship Map › Botan | A credited guest at Botan's birthday 3D live "Stray&Stay" (2026-09-19). | The row’s Person column names Botan; the unnamed guest must be made explicit for reliable extraction. | Nerissa is credited as a guest in Botan's birthday 3D live "Stray&Stay"; the archive lists the broadcast under 2026-09-19. | [Birthday-live metadata](https://tw.yutura.net/channel/35550/video/cI535pJp-TQ/), ARCHIVE_METADATA, opened 2026-10-04. | Advent owner; preserve Botan’s already-correct dossier guest attribution. | No |
| JP2-STATUS-001 | P1 | `historical_scenes[Gura,Mumei,Amelia].status` | `W/JP-Senpai-Pairs-2.md` › `[SW] Rules` | Gura and Mumei appear only as memories; Ame is an affiliate. | Applies baseline status to every historical scene, despite the card documenting collaborations during their active periods. | At the 2026-09-30 baseline, Gura and Mumei are graduates and Ame is an affiliate. Historical scenes use each member's status at the scene date. | Project constitution and registry status intervals, examined 2026-10-04; external status evidence inherited, not reopened. | Global/history owners; scene-date validation. | No |
| JP2-EVENT-001 | P1 | `evidence[collaboration_title].event_occurrence` | `W/JP-Senpai-Pairs-2.md` › `[SW] Rules` | A collab title shows that a collab happened, not how close two members are; | A title can establish billing without establishing that an announced event occurred or every billed person attended. | A collaboration title identifies its billing; occurrence and participation depend on the available archive and credits. These records do not establish private closeness; | Task’s ARCHIVE_METADATA rule; local rule check 2026-10-04. No external factual assertion added. | Event extraction and downstream cohort owners. | No |
| JP2-ROSTER-001 | P2 | `units[hololive Fantasy].original_members` | `C/Houshou-Marine.md` › `[SW] Background` | the "hololive Fantasy" group with Usada Pekora, Shiranui Flare and Shirogane Noel | The debut-time sentence lists the surviving lineup without identifying the list as selective. History to 2022 correctly includes Rushia. Clarify the historical roster. | the "hololive Fantasy" group, whose original lineup comprised Marine, Usada Pekora, Uruha Rushia, Shiranui Flare and Shirogane Noel | [Fantasy event report](https://hololive.hololivepro.com/events/fanfunisland/), OFFICIAL, opened 2026-10-04. | Noel patch below; preserve current Groups and the correct History row. Rushia remains reference-only. | No |
| JP2-ROSTER-001 | P2 | Same | `C/Shirogane-Noel.md` › `[SW] Background` | the "hololive Fantasy" group with Usada Pekora, Shiranui Flare and Houshou Marine | Same historical/current-list ambiguity. | the "hololive Fantasy" group, whose original lineup comprised Noel, Usada Pekora, Uruha Rushia, Shiranui Flare and Houshou Marine | [Fantasy event report](https://hololive.hololivepro.com/events/fanfunisland/), OFFICIAL, opened 2026-10-04. | Marine patch above; Global history owner. | No |
| JP2-ROSTER-002 | P2 | `units[hololive fifth generation,NePoLaBo].members` | `C/Yukihana-Lamy.md` › `[SW] Background` | She debuted on 2020-08-12 in hololive's 5th generation with Shishiro Botan, Omaru Polka and Momosuzu Nene (with whom she forms NePoLaBo). | Conflates the original generation roster with the four-member NePoLaBo lineup; History to 2022 distinguishes them. | She debuted on 2020-08-12 in hololive's 5th generation; its original lineup included Lamy, Shishiro Botan, Omaru Polka, Momosuzu Nene and Mano Aloe. Lamy forms NePoLaBo with Botan, Polka and Nene. | [COVER’s fifth-generation announcement](https://files.microcms-assets.io/assets/6368857617454c2591b02acff18e76bb/19dbf61408864631901ed6c87f9f6c61/_______________5____________________________________________________________________________________________________________.pdf), OFFICIAL, opened 2026-10-04. The announcement establishes the original roster; Lamy’s existing debut date is retained. | Global/history owner; Aloe remains reference-only. Botan’s existing separation needs no patch. | No |
| JP2-ROSTER-003 | P2 | `events[1HQL3WJPBHA].participants` | `C/AZKi.md` › `[SW] Relationships` | Hakui Koyori and Yukihana Lamy: "KoZMy" cover partners on "Ai♡Scream!" (2025), and a 3D karaoke with Koyori, Isaki Riona and Koganei Niko (2026); | The shared heading can carry Lamy into the karaoke clause. AZKi’s and Koyori’s dossiers explicitly identify a separate four-person event. | Hakui Koyori and Yukihana Lamy: "KoZMy" cover partners on "Ai♡Scream!" (2025). Separately, AZKi joined Koyori, Isaki Riona and Koganei Niko for 3D karaoke (2026); | [Karaoke upload](https://www.youtube.com/watch?v=1HQL3WJPBHA), ARCHIVE_METADATA; inherited, not reopened. Cross-file check 2026-10-04. | JP owner; preserve the correctly bounded dossier rows. | No |
| JP2-ALIAS-001 | P2 | `works[TREVIAN KNIGHT].title` | `C/Fuwawa-Abyssgard.md` › Relationship Map › Marine/Noel/Vivi row | "Très Bien Night" | Unpropagated alternative spelling of the song already standardized on Noel’s and JP2’s cards. | "TREVIAN KNIGHT" | [Official music entry](https://hololive.hololivepro.com/en/music/622/), OFFICIAL, opened 2026-10-04. Dance participation remains inherited metadata. | Mococo row below; Advent owner. | No |
| JP2-ALIAS-001 | P2 | Same | `C/Mococo-Abyssgard.md` › Relationship Map › Marine/Noel/Vivi row | "Très Bien Night" | Same unpropagated title spelling. | "TREVIAN KNIGHT" | [Official music entry](https://hololive.hololivepro.com/en/music/622/), OFFICIAL, opened 2026-10-04. | Advent owner; preserve the existing dance-short evidence. | No |
| JP2-TIE-002 | P2 | `units[Usada Kensetsu].affiliation_wording` | `C/Takanashi-Kiara.md` › `[SW] Relationships` | Botan's Minecraft "Usada Kensetsu" | The possessive can imply ownership, while Botan’s dossier describes fellow membership in Pekora’s circle. | the Minecraft company "Usada Kensetsu" | [Festival archive locator](https://ckworks.jp/vinforadar/video/q_IXZIRCbwI), ARCHIVE_METADATA, inherited; opening failed 2026-10-04. Existing Botan/Kiara membership statements agree. | Kiara dossier patch below; Myth3 owner. | No |
| JP2-TIE-002 | P2 | Same | `C/Takanashi-Kiara.md` › Relationship Map › Botan | Botan's Minecraft "Usada Kensetsu" | Same unnecessary ownership implication. | the Minecraft company "Usada Kensetsu" | Same [archive locator](https://ckworks.jp/vinforadar/video/q_IXZIRCbwI), ARCHIVE_METADATA; inaccessible 2026-10-04, evidence not freshly verified. | Myth3 owner; no ownership fact is added. | No |
| JP2-TIE-003 | P2 | `relationships[FUWAMOCO,JP2].public_basis` | `W/FUWAMOCO.md` › `[SW] Description` | Close to all of Advent | The sentence combines collaborations, a concert unit and oshi references into an unqualified degree of closeness. Concrete public ties are sufficient. | Their public ties extend to all of Advent | [Touhou collaboration locator](https://www.youtube.com/watch?v=x7gRHgQ0yI0), ARCHIVE_METADATA, inherited, not reopened; existing relationship records examined 2026-10-04. | Advent owner; retain the following collaboration names, fictional sister bit and individual oshi assignments. | No |

## New verified facts

None. Fresh checks support corrections or confirm existing claims; no additional enrichment is proposed.

## Merge handoff

Apply the changes in this order:

1. **Accept JP2-SCOPE-001.** Apply the character-card removal, all three audio-report redactions and the corresponding verdict change together. Promise/task 09 owns the supporting report. Re-extract quotations after the edit; editorial redaction markers must never become approved speech.
2. **Accept JP2-TIE-001 and JP2-CREDIT-001 before validation.** These are material P1 corrections. Coordinate with JP and Advent so the incoming and outgoing records remain consistent.
3. **Accept JP2-STATUS-001 and JP2-EVENT-001.** These prevent present status and archive billing from being used as universal historical facts.
4. **Recommend accepting the P2 patches:** JP2-ROSTER-001–003, JP2-ALIAS-001 and JP2-TIE-002–003. They clarify historical membership, participation, naming and relationship wording without adding private interpretations.

Existing findings:

| Existing ID | Recommendation |
|---|---|
| `BR-UNIT-002` | Retain as applied. Marine and Noel now distinguish the six-member Bara☆Dice credit from Yakamashi Musume. |
| `PROMISE-CREDIT-001` | Retain as applied. The seven-singer “PARADISE!” statements do not require adding Noel, Botan or Vivi. |
| `CONSULT-R2-001` | Retain. The supplementary name/alias/unit search found no additional material incoming-claim omission. |
| `CONSULT-P1-006` | Do not reopen solely because an ASR excerpt is abbreviated. No new lexical mismatch was established here. |

The failed dance-short and Usaken archive openings remain evidence limitations, not contrary evidence. Lamy’s full raw two-model window was unavailable in the snapshot; her existing explicit shared-span attestation is inherited rather than independently reproduced. Neither limitation warrants inventing replacement facts.

After accepted edits, regenerate `registry.json`, `manifest.json`, JP2 packets and affected incoming packets. Preserve historical roster dates and explicit host/guest direction. The bounded registry need not acquire every secondary pair label.

Task 10 should rebuild the exported cards and dependent delivery artifacts from the corrected sources. Task 11 must validate that regenerated snapshot. No promotion or merged state is asserted by this audit.

Downstream owners: **JP, Advent, Promise/task 09, Myth3, Global/history, and tasks 10–11**.

**Open questions**

None.