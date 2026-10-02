#!/usr/bin/env python3
"""Build the GPT work program the author ordered on 2026-10-02: plan all later reviews, find new material, and
plan and integrate the Sudowrite + ElevenLabs workflow. GPT runs the whole queue unattended
(tools/gpt_autorun.py); Claude merges the results only when the author says so (Claude's weekly budget).

    python3 tools/mk_gpt_program.py          # (re)builds the runs below; prints the queue commands

Runs (one GPT quota window each, sequential):
  P1  check-GPT-plan                     audit the review program, design the post-merge verification rounds
  W1  research-workflow-SW-EL            verify Sudowrite and ElevenLabs as of now; end-to-end workflow, script
                                         format, converter code, package gap analysis
  R1–R6 research-new-<group>             new sourced material per member (recency first), corrections, ties
  R7  research-new-R7-Ties               documented interactions for pairs the relationship web lacks
Inputs are read from the bible (and the holoX drafts, not yet promoted) at build time; rebuild before queueing
if cards changed.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
import qa_runs  # noqa: E402

P = ROOT / "projects" / "holoen"
STAMP = "20261002-1715"
HOLOX_DRAFTS = {"Laplus-Darknesss", "Takane-Lui", "Hakui-Koyori", "Sakamata-Chloe", "Kazama-Iroha"}
GROUPS = {
    "R1-Myth": ("hololive -Myth-", ["Mori-Calliope", "Takanashi-Kiara", "Ninomae-Inanis", "Gawr-Gura",
                                    "Watson-Amelia"]),
    "R2-Promise": ("hololive -Promise-", ["IRyS", "Ouro-Kronii", "Ceres-Fauna", "Nanashi-Mumei", "Hakos-Baelz"]),
    "R3-Advent": ("hololive -Advent-", ["Shiori-Novella", "Koseki-Bijou", "Nerissa-Ravencroft", "Fuwawa-Abyssgard",
                                        "Mococo-Abyssgard"]),
    "R4-Justice": ("hololive -Justice-", ["Elizabeth-Rose-Bloodflame", "Gigi-Murin", "Cecilia-Immergreen",
                                          "Raora-Panthera"]),
    "R5-JP1": ("hololive JP, part 1", ["Hoshimachi-Suisei", "AZKi", "Nakiri-Ayame", "Nekomata-Okayu",
                                       "Houshou-Marine", "Shirogane-Noel", "Yukihana-Lamy"]),
    "R6-JP2": ("hololive JP, part 2", ["Shishiro-Botan", "Kikirara-Vivi", "Laplus-Darknesss", "Takane-Lui",
                                       "Hakui-Koyori", "Sakamata-Chloe", "Kazama-Iroha"]),
}
HEAD = """You are GPT, the senior researcher and QA reviewer for novel-lab's holoen project. Use the project-required
GPT-6 model at xhigh with live web search. Work read-only and answer in English. This is one task in a sequential
queue; do not launch parallel GPT work. Never read projects/*/runs/. Do not modify files; return the complete
result in your final response. The factual baseline is 2026-09-30 (today is 2026-10-02).

## Binding rules

{rules}
- Never propose (even when an official profile or wiki lists it): body measurements, drinking amounts, family,
  home or home region, pets, health, sleep or daily routine, trips, romance, audition history, breaks or their
  reasons, pre-debut history or the performer behind the persona. A Merge Record that says "private details
  deliberately excluded" means a topic was left out on purpose: do not re-propose it.
- No explicit sexual content, no lyrics, no long quotes. Spoken quotations are not accepted from you: list them
  as candidates for Claude's two-model audio check (video, timestamp, approximate words). Official written
  lines (profiles, post text, titles) may be quoted short with their source.
- No member rankings or comparisons. Partner tags and voice directions are proposed scene directions for
  original designed voices, never imitation; no pitch, F0 or speaking-rate targets.
- Evidence classes: OFFICIAL (hololive/COVER pages, official accounts), PRIMARY (the member's own stream title,
  description or post), ARCHIVE_METADATA, SECONDARY (wiki, fan sites; label it), ASR (Claude's audio reports).
  Fan transcription cannot establish exact spoken words.
"""
BUDGET = """## Run budget
One task must finish inside one quota window (about 200k tokens); every tool call re-sends the conversation.
Batch local lookups (`rg -n -e A -e B files`), prefer official pages, and stop at about {calls} tool calls.
Your working directory is a copy of the project taken when this run started (no `runs/`, no git). If the
budget runs short, stop and list what you could not check under Coverage; a complete answer with disclosed
limits beats a lost one.
"""


def sw_fields(text):
    return [(m.group(1).strip(), m.group(2).strip())
            for m in re.finditer(r"^## \[SW\] ([^\n]+)\n(.*?)(?=^## |^---|\Z)", text, re.M | re.S)]


def card_text(stem):
    if stem in HOLOX_DRAFTS:
        draft = P / "runs" / f"20261002-0615-character-{stem}" / "claude-draft.md"
        return draft.read_text(encoding="utf-8"), "draft (claim check run E/F pending; not promoted)"
    return (P / "bible" / "characters" / f"{stem}.md").read_text(encoding="utf-8"), "promoted (bible)"


def member_block(stem):
    text, status = card_text(stem)
    keep = ("Name", "Groups", "Other Names", "Personality", "Background", "Dialogue Style", "Catchphrases",
            "Relationships")
    rows = [f"**{k}:** {v}" for k, v in sw_fields(text) if k in keep]
    hist = re.search(r"^## (?:History|Timeline|Background Timeline)[^\n]*\n(.*?)(?=^## )", text, re.M | re.S)
    hist_rows = [r for r in (hist.group(1).split("\n") if hist else []) if re.match(r"\|\s*20(2[5-6])", r)]
    out = [f"### {stem.replace('-', ' ')} (`{stem}`; {status})", "", *rows, ""]
    if hist_rows:
        out += ["Dossier history rows dated 2025–2026 (already on the card):", *hist_rows, ""]
    if stem not in HOLOX_DRAFTS:
        out += [f"Full card: projects/holoen/bible/characters/{stem}.md (Merge Record lists deliberate exclusions).", ""]
    return "\n".join(out)


def write_run(name, title, text):
    run = P / "runs" / f"{STAMP}-{name}"
    run.mkdir(parents=True, exist_ok=True)
    (run / "brief.md").write_text(f"# {title}\n\nBuilt by tools/mk_gpt_program.py (author order 2026-10-02); the prompt "
                                  "is to-gpt.free.md. Claude merges the result only on the author's word.\n",
                                  encoding="utf-8")
    assert "{{" not in text
    (run / "to-gpt.free.md").write_text(text, encoding="utf-8")
    print(f"{name}: {len(text):,} chars -> {run.relative_to(ROOT)}")
    return run


def research(gid, title, stems):
    web = (P / "research" / "qa" / "relationship-web.md").read_text(encoding="utf-8")
    one_way = web[web.find("## One-way ties"):]
    text = f"""# Task 10 — New material: {title} ({len(stems)} members)

{HEAD.format(rules=qa_runs.RULES)}
## Goal

The author wants new, sourced material for these members' cards: what the cards lack that helps a writer put
each member in a scene and give her a playable voice. Priorities, in order: (1) corrections to wrong or outdated
claims; (2) her present-day manner and running bits from 2025–2026 streams (recency weighting; alumni and
affiliates: their last active period); (3) 2025–2026 milestones, songs, concerts, official lore updates;
(4) documented interactions with the other cast members (list below), above all pairs the relationship web
lacks; (5) recurring segments, catchphrases and in-jokes with their official or primary source. Skip trivia that
does not change how a scene plays.

The cast: Mori Calliope, Takanashi Kiara, Ninomae Ina'nis, Gawr Gura (graduated), Watson Amelia (affiliate),
IRyS, Ouro Kronii, Ceres Fauna (graduated), Nanashi Mumei (graduated), Hakos Baelz, Shiori Novella, Koseki Bijou,
Nerissa Ravencroft, Fuwawa and Mococo Abyssgard (FUWAMOCO), Elizabeth Rose Bloodflame, Gigi Murin, Cecilia
Immergreen, Raora Panthera, Hoshimachi Suisei, AZKi, Nakiri Ayame, Nekomata Okayu, Houshou Marine, Shirogane Noel,
Yukihana Lamy, Shishiro Botan, Kikirara Vivi, La+ Darknesss, Takane Lui, Hakui Koyori, Sakamata Chloe (affiliate
since 2025-01-26), Kazama Iroha. COVER unified its female branches as "hololive" on 2026-09-07.

## Method
1. Read the member's block below (exported fields plus the 2025–2026 history rows already on the card); open the
   full card only to check the dossier or the Merge Record's exclusions.
2. Search official sources first (hololive talent and music pages, hololivepro.com news, COVER press, official X
   accounts), then the member's own stream titles and descriptions, then secondary sources (label them).
3. Propose only what is new or corrects the card; at most about 8 proposals per member. Give exact English text
   that fits the card's voice; for [SW] fields note that Relationships is capped at 350 words (many cards are at
   the cap: propose a dossier row instead, or say which clause it should replace).

## Exact output format (these headings, in this order)

## Coverage
Members examined, sources opened, what you could not check.

## Proposals
| ID | Priority | Member | Target | Proposed text (exact) | Why it helps scenes or voice | Evidence URL + class + checked date | Event date |
|---|---|---|---|---|---|---|---|
IDs NEW-{gid.split('-')[0]}-NNN. Priority P1 (material: correction-adjacent, present-day manner, major 2025–2026
event), P2 (useful enrichment), P3 (optional). Target is `C/<stem> › <field>` for an exported field or
`D/<stem> › <section>` for the dossier. Escape table pipes; use <br> for newlines.

## Corrections
| ID | Member | Exact old text | Problem | Exact replacement | Evidence URL + class + checked date |
|---|---|---|---|---|---|
IDs FIX-{gid.split('-')[0]}-NNN. Copy the old text exactly. "None." if none.

## Cast ties found
| Pair | Interaction | Date | Evidence URL + class | Fills a one-way tie or an empty pair? |
|---|---|---|---|---|

## After the baseline (author decision)
Items dated 2026-10-01 or later, or announcements of future events, listed separately.

## Quotation candidates for Claude's audio check
| Member | Video URL | Timestamp | Approximate words | What it would show |
|---|---|---|---|---|

## Merge handoff
Dependencies, propagation to other cards, up to five questions for the author ("None" if none).

{BUDGET.format(calls=20)}
## Current one-way ties (from research/qa/relationship-web.md)

{one_way}
## Members

""" + "\n".join(member_block(s) for s in stems)
    return write_run(f"research-new-{gid}", f"Task 10 new material: {title}", text)


def ties():
    web = (P / "research" / "qa" / "relationship-web.md").read_text(encoding="utf-8")
    text = f"""# Task 10 — New material: relationship web across the whole cast

{HEAD.format(rules=qa_runs.RULES)}
## Goal

Relationships across all branches matter to the author. The matrix below (computed from the cards' exported
Relationships fields; holoX cards are drafts and not yet in it) shows who names whom. Find documented, dated
public interactions for (a) the one-way ties listed and (b) empty pairs where a real interaction exists (collab
streams, off-collabs, songs and covers, concerts and events, game sessions, guest appearances, public posts).
Do not invent ties to fill the matrix: an empty pair with no documented interaction stays empty, and saying so is
a valid result. Include the holoX members (La+ Darknesss, Takane Lui, Hakui Koyori, Sakamata Chloe, Kazama Iroha)
as rows and columns. Prefer 2024–2026 and named, dated events; label secondary sources.

For each tie you propose, write one Relationships clause for each side in the cards' style ("Name: what, year.")
and say whether it should go in the exported field or only the dossier (many cards are at the 350-word cap).

## Exact output format

## Coverage
## Ties
| ID | Pair | Interaction | Date | Evidence URL + class + checked date | Clause for A | Clause for B | Export or dossier |
|---|---|---|---|---|---|---|---|
IDs TIE-NNN, most useful for scenes first.
## Pairs checked with no documented interaction
## Corrections to existing ties
| ID | Card | Exact old text | Problem | Exact replacement | Evidence |
|---|---|---|---|---|---|
## Merge handoff

{BUDGET.format(calls=25)}
## Relationship web (computed)

{web}
"""
    return write_run("research-new-R7-Ties", "Task 10 new material: relationship web", text)


def workflow():
    text = f"""# Task 11 — Sudowrite + ElevenLabs workflow: verify, plan, integrate

{HEAD.format(rules=qa_runs.RULES)}
## Goal

The project's product is dialogue for AI voice performance. A writer drafts scenes in Sudowrite from the Story
Bible cards (Characters, Worldbuilding, Style); an ElevenLabs v4 voice that is original (designed, never cloned
or imitating the member) performs each character's lines with inline audio tags. The author wants the whole
Sudowrite + ElevenLabs workflow planned and integrated: what the writer and the voice director do, step by step,
with which files, and exactly what our package must change to support it.

## Read first (in your working copy; do not re-open them repeatedly)
- novel-lab/docs/sudowrite-2026-09.md and novel-lab/docs/elevenlabs-v4.md (our platform notes)
- novel-lab/projects/holoen/project.md (the author's rules) and novel-lab/framework/sudowrite-fields.json
- novel-lab/projects/holoen/export/sudowrite-paste.md, export/characters.csv, export/worldbuilding.csv (what
  the writer pastes or imports), export/elevenlabs/sudowrite-style.md (the Style block) and one sheet, e.g.
  export/elevenlabs/Mori-Calliope.md and export/elevenlabs/AZKi.md
- novel-lab/tools/release.py (delivery package layout, START-HERE text, checks V01–V25)

## Verify live (official documentation first, as of 2026-10)
- Sudowrite: Story Bible structure and fields (Characters, Worldbuilding, Style, Synopsis, Outline, Braindump,
  Genre), field limits, visibility toggles, import paths (paste, CSV, others), Write/Draft/Rewrite/Describe and
  scene or chapter tools, Plugins, Muse or current model choices, export formats, any API.
- ElevenLabs: the current v4 model name and ID, the audio-tag set and how tags are written, Text to Dialogue
  (multi-speaker) in the app and API (request shape, limits), Voice Design (text-to-voice), voice settings and
  their API ranges, pronunciation dictionaries, Studio/projects for long-form assembly, output formats, and the
  terms on voices of real people (consent, impersonation, voice library rules).
- COVER's fan-work and derivative-work guidelines that bear on fan fiction and synthetic voice of its talents
  (official URLs).

## Exact output format (these headings, in this order)

## Verified platform facts
| Platform | Feature | What it does now | Source URL | Checked | What our docs say | Agree? |
|---|---|---|---|---|---|---|

## End-to-end workflow
Numbered stages: 0 setup; 1 load the bible into Sudowrite; 2 plan a scene; 3 draft dialogue with tags;
4 lint the script; 5 design the original voices; 6 generate in ElevenLabs; 7 listen and fix; 8 assemble and
deliver; 9 version and archive. For each: inputs, actions, outputs with file names, who does it, checks, common
failures and their fixes.

## Script format spec
The scene format Sudowrite should be prompted to output and the converter reads: speaker labels, where tags go,
narration and stage directions (excluded from audio or sent to a narrator voice), line length, pauses and SFX,
multi-speaker turns, language mixing (Japanese lines with romanization). Include a short example using only
labelled Style demo lines (no real quotations).

## Converter
Full Python 3 standard-library code for `novel-lab/tools/scene_to_elevenlabs.py`: parse a script file in the
spec's format; validate speakers against a voice map (JSON: speaker → voice_id, set by the voice director) and
tags against each character's allowed tags (parsed from export/elevenlabs/<stem>.md); flag nonverbal tags that
are also spelled out; split over-long turns; emit the Text to Dialogue request body as JSON (one file per scene)
plus a plain-text listening sheet. No network calls, no keys. Then a minimal test (sample script in, expected
JSON out) as a second code block.

## Package gap analysis
| ID | Priority | File + section | Exact old text | Problem | Exact replacement | Evidence |
|---|---|---|---|---|---|---|
IDs WF-NNN; P0 (blocks the workflow or breaks platform terms), P1 (material), P2 (clarity). Copy old text
exactly; DELETE for deletions; escape pipes; <br> for newlines.

## Writer's quick-start
One page in English for the delivery package's START-HERE: the workflow in ten lines or fewer per role.

## Risks and policy
Voice cloning and impersonation, disclosure of synthetic voice, platform terms, COVER guidelines, explicit
content (never written; the project marks such scenes 【Sudowrite 處理】 without content).

## Open questions for the author
Up to five, each answerable with a short choice.

{BUDGET.format(calls=30)}"""
    return write_run("research-workflow-SW-EL", "Task 11 Sudowrite + ElevenLabs workflow", text)


def plan():
    text = f"""# Task 12 — Review program: audit Claude's plan and design the post-merge verification

{HEAD.format(rules=qa_runs.RULES)}
## Context

The author ordered (2026-10-02) that GPT plan and carry out all later reviews, find new material, and plan the
Sudowrite + ElevenLabs workflow. Claude wrote the queue in `novel-lab/projects/holoen/GPT-PROGRAM.md` (read it
first) and merges results only when the author says so. Read also: projects/holoen/NEXT.md (top status block
only), research/qa/validation-spec.md, research/qa/validation.json, research/qa/resolutions.md (headings and
open items), novel-lab/framework/prompts/rubric.md, tools/release.py (checks V01–V25), tools/qa_runs.py and
tools/qa_packets.py (how the cohort audits are built).

## Deliverables (exact headings)

## Gaps in the queue
Reviews the release needs that the queue does not cover (for example world cards, performance sheets after the
voice fixes, the Sudowrite paste file and CSVs, cross-card consistency after merges, holoX cohort and voice
audits after runs E and F, recency drift), each with why it matters.

## Post-merge verification plan
Rounds that should run after Claude merges the queue's results, in order: what each round checks, its inputs,
its output format, its budget (one quota window each), and exit criteria. The author's rule is one GPT round per
card; promotions are author decisions; say where a second look is a spot check of a merge rather than a re-review.

## Release criteria
Map each blocking check (V01–V25) to the run or round that clears it and what "done" means for release r01.

## Recommended changes to the queue
Order changes, splits or merges of runs, prompts to tighten (cite the file and line), with reasons.

## Risks
Budget, staleness, merge conflicts between runs that touch the same cards, scope risks.

{BUDGET.format(calls=15)}"""
    return write_run("check-GPT-plan", "Task 12 review program plan", text)


if __name__ == "__main__":
    runs = [plan(), workflow()] + [research(g, t, s) for g, (t, s) in GROUPS.items()] + [ties()]
    print("\nQueue commands:")
    for r in runs:
        print(f"python3 novel-lab/tools/lab.py gpt novel-lab/projects/holoen/runs/{r.name} free")
