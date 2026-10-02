#!/usr/bin/env python3
"""Build the one-round GPT claim-check prompts for the second JP batch (author orders 2026-10-02).

    python3 tools/mk_b2_review.py

The author ordered Houshou Marine, Shirogane Noel, Yukihana Lamy, Shishiro Botan, all of Secret Society holoX
(La+ Darknesss, Takane Lui, Hakui Koyori, Sakamata Chloe, Kazama Iroha) and Kikirara Vivi added as full cards.
Four self-contained prompts, each sized for one GPT quota window, are written to the first run of each group:

  C  Marine, Noel, Lamy
  D  Botan, Vivi, the world card "JP Senpai Pairs 2", and the lines about Marine, Noel, Lamy, Botan and Vivi
     added to the other cast cards
  E  La+, Lui, Koyori
  F  Chloe, Iroha, the world card "holoX", and the lines about the holoX members added to the other cast cards
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
import qa_runs  # noqa: E402

P = ROOT / "projects" / "holoen"
STAMP = "20261002-0615"
WORLD = {"JP-Senpai-Pairs-2", "holoX"}
REPORT = {"Houshou-Marine": "marine", "Shirogane-Noel": "noel", "Yukihana-Lamy": "lamy", "Shishiro-Botan": "botan",
          "Kikirara-Vivi": "vivi", "Laplus-Darknesss": "laplus", "Takane-Lui": "lui", "Hakui-Koyori": "koyori",
          "Sakamata-Chloe": "chloe", "Kazama-Iroha": "iroha"}
# cards that received lines about the batch-2 members (English cast plus the first JP additions)
OTHERS = ["Mori-Calliope", "Takanashi-Kiara", "Ninomae-Inanis", "Gawr-Gura", "Watson-Amelia", "IRyS",
          "Nerissa-Ravencroft", "Ouro-Kronii", "Ceres-Fauna", "Nanashi-Mumei", "Shiori-Novella", "Koseki-Bijou",
          "Fuwawa-Abyssgard", "Mococo-Abyssgard", "Elizabeth-Rose-Bloodflame", "Gigi-Murin", "Cecilia-Immergreen",
          "Raora-Panthera", "Hakos-Baelz", "Hoshimachi-Suisei", "AZKi", "Nakiri-Ayame", "Nekomata-Okayu"]
PAT_JP2 = re.compile(r"Marine|Noel|Lamy|Botan|Vivi|FLOW GLOW|Apex Predators|HOLOYOI")
PAT_HX = re.compile(r"holoX|La\+|Laplus|Lui\b|Koyori|Chloe|Iroha|HOLOTORI|KoMeHa")

BUDGET = """## Run budget and scope (Claude, 2026-10-02)
- The author ordered these hololive members from Japan added as full cards (2026-10-02): Houshou Marine,
  Shirogane Noel, Yukihana Lamy, Shishiro Botan, Kikirara Vivi and all of Secret Society holoX (La+ Darknesss,
  Takane Lui, Hakui Koyori, Sakamata Chloe, Kazama Iroha), with their ties to the rest of the cast. {scope}
- They stream in Japanese. Quotes on the cards are Japanese (with romanization and an English gloss); the audio
  reports list both models' renderings. A Japanese quote passes the gate only if the report marks it shared
  (the same kana reading in both models counts as shared). Never stitch separately timed spans.
- Public persona only. Do not propose adding body measurements, drinking amounts, family, home region, pets,
  health, sleep or daily routine, trips, romance, auditions, breaks or their reasons, or pre-debut history, even
  when an official profile or wiki lists them; the cards leave these out on purpose. Accents are voice features
  only; do not assign a regional accent without an in-scope listening check.
- Sakamata Chloe concluded her regular activities on 2025-01-26 and is a hololive affiliate; her card covers
  2021-11 to 2025 plus affiliate appearances. Everyone else is active at the 2026-09-30 baseline.
- Performance sheets: original designed voices only (never imitate a member); pitch and pace measurements are
  research data, not synthesis targets; partner tags are proposed scene directions; laughs and timbre are
  provisional choices unless a source is named.
- This run must finish inside one quota window (about 200k tokens). Every tool call re-sends the conversation,
  so keep to about 15 tool calls in total, including web searches; batch local lookups. Prioritize the exported
  [SW] fields, then the dossier facts dated 2025–2026, then the sheets.
- Your working directory is a copy of the project taken when this run started (no `runs/`, no git). The new
  cards are not in `bible/`; their full text is inline below. Do not re-open the inline files.
- If the budget runs short, stop and report what you could not check in the Verification note.
"""


def run_dir(stem):
    kind = "world" if stem in WORLD else "character"
    return P / "runs" / f"{STAMP}-{kind}-{stem}"


def lines_about(pat, title):
    out = []
    for s in OTHERS:
        p = qa_runs.run_of(s)
        if not p:
            continue
        t = p.read_text(encoding="utf-8")
        head, _, sw = t.partition("\n## [SW] Name")
        rows = [r for r in head.split("\n") if r.startswith("| ") and pat.search(r.split("|")[1])]
        rel = re.search(r"## \[SW\] Relationships\n(.*?)(?=\n## )", sw, re.S)
        sents = [x for x in re.split(r'(?<=[.!?"])\s+(?=[A-Z])', rel.group(1)) if pat.search(x)] if rel else []
        if rows or sents:
            out.append(f"### {s.replace('-', ' ')}")
            if sents:
                out += ["Relationships field (exported):", " ".join(sents)]
            if rows:
                out += ["Dossier rows (with sources):"] + rows
            out.append("")
    return f"## {title}\n\n" + "\n".join(out)


def build(name, stems, scope, extra=""):
    tpl = (ROOT / "framework" / "prompts" / "gpt-claimcheck-review.md").read_text(encoding="utf-8")
    tpl = tpl.replace(" (template; Claude fills the {{…}} parts)", "")
    parts = [BUDGET.format(scope=scope)]
    for i, s in enumerate(stems, 1):
        label = "World card" if s in WORLD else "Card"
        parts += [f"## {label} {i}: {s.replace('-', ' ')} (draft, full file)", "",
                  (run_dir(s) / "claude-draft.md").read_text(encoding="utf-8"), ""]
        if s in REPORT:
            rep = P / "research" / "audio-check" / f"{REPORT[s]}.md"
            sheet = P / "export" / "elevenlabs" / f"{s}.md"
            if rep.exists():
                parts += [f"## Audio report: research/audio-check/{REPORT[s]}.md", "", rep.read_text(encoding="utf-8"), ""]
            if sheet.exists():
                parts += [f"## Performance sheet: export/elevenlabs/{s}.md", "", sheet.read_text(encoding="utf-8"), ""]
    parts.append(extra)
    text = tpl.replace("{{rules}}", qa_runs.RULES).replace("{{files}}", "\n".join(parts))
    assert "{{" not in text
    out = run_dir(stems[0]) / "to-gpt.free.md"
    out.write_text(text, encoding="utf-8")
    print(f"{name}: {len(text):,} chars -> {out.relative_to(ROOT)}")


if __name__ == "__main__":
    build("C", ["Houshou-Marine", "Shirogane-Noel", "Yukihana-Lamy"],
          "This is run C of four: Marine, Noel and Lamy. Run D covers Botan, Vivi, \"JP Senpai Pairs 2\" and the "
          "cross-card lines about these five; runs E and F cover holoX.")
    build("D", ["Shishiro-Botan", "Kikirara-Vivi", "JP-Senpai-Pairs-2"],
          "This is run D of four: Botan, Vivi, the world card \"JP Senpai Pairs 2\" and the lines about Marine, Noel, "
          "Lamy, Botan and Vivi added to the other cast cards (listed at the end). Run C covered Marine, Noel and "
          "Lamy's own cards.",
          lines_about(PAT_JP2, "Lines about Marine, Noel, Lamy, Botan and Vivi on the other cast cards "
                               "(2026-10-02; promoted ahead of this review)"))
    build("E", ["Laplus-Darknesss", "Takane-Lui", "Hakui-Koyori"],
          "This is run E of four: La+, Lui and Koyori. Run F covers Chloe, Iroha, the world card \"holoX\" and the "
          "cross-card lines about holoX.")
    build("F", ["Sakamata-Chloe", "Kazama-Iroha", "holoX"],
          "This is run F of four: Chloe, Iroha, the world card \"holoX\" and the lines about the holoX members "
          "added to the other cast cards (listed at the end). Run E covered La+, Lui and Koyori's own cards.",
          lines_about(PAT_HX, "Lines about the holoX members on the other cast cards "
                              "(2026-10-02; promoted ahead of this review)"))
