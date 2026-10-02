#!/usr/bin/env python3
"""Build the two one-round GPT claim-check prompts for the hololive JP additions (author order 2026-10-02).

    python3 tools/mk_jp_review.py

Run A (written to the Suisei run): Hoshimachi Suisei and AZKi, their audio reports and performance sheets.
Run B (written to the Ayame run): Nakiri Ayame, Nekomata Okayu, the world card "JP Senpai Pairs", and the lines
about the four that were added to the English cast's cards. Each prompt is self-contained (the drafts are not in
bible/ yet) and carries a run budget so it fits one GPT quota window.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
import qa_runs  # noqa: E402

P = ROOT / "projects" / "holoen"
RUN = {s: P / "runs" / f"20261002-0529-{k}-{s}" for k, s in
       [("character", "Hoshimachi-Suisei"), ("character", "AZKi"), ("character", "Nakiri-Ayame"),
        ("character", "Nekomata-Okayu"), ("world", "JP-Senpai-Pairs")]}
REPORT = {"Hoshimachi-Suisei": "suisei", "AZKi": "azki", "Nakiri-Ayame": "ayame", "Nekomata-Okayu": "okayu"}
EN = ["Mori-Calliope", "Takanashi-Kiara", "Ninomae-Inanis", "IRyS", "Fuwawa-Abyssgard", "Mococo-Abyssgard",
      "Gawr-Gura", "Gigi-Murin", "Nanashi-Mumei", "Hakos-Baelz"]
PAT = re.compile(r"Suisei|AZKi|Ayame|Okayu|Star Flower|Death Star|TakoNeko|OkaGigi|FWMCAZ|HOLOTALK")

BUDGET = """## Run budget and scope (Claude, 2026-10-02)
- The author ordered four hololive members from Japan added as full cards (2026-10-02): Hoshimachi Suisei, AZKi,
  Nakiri Ayame and Nekomata Okayu, with their ties to the English cast. {scope}
- They stream in Japanese. Quotes on the cards are Japanese (with romanization and an English gloss); the audio
  reports list both models' renderings. A Japanese quote passes the gate only if the report marks it shared.
  Private life stays out (family, childhood, health, trips, daily routine, how often someone streams, breaks).
- This run must finish inside one quota window (about 200k tokens). Every tool call re-sends the conversation,
  so keep to about 15 tool calls in total, including web searches; batch local lookups. Prioritize the exported
  [SW] fields, then the dossier facts dated 2025–2026, then the sheets.
- Your working directory is a copy of the project taken when this run started (no `runs/`, no git). The new
  cards are not in `bible/`; their full text is inline below. Do not re-open the inline files.
- If the budget runs short, stop and report what you could not check in the Verification note.
"""


def draft(stem):
    return (RUN[stem] / "claude-draft.md").read_text(encoding="utf-8")


def en_lines():
    out = []
    for s in EN:
        p = qa_runs.run_of(s)
        if not p:
            continue
        t = p.read_text(encoding="utf-8")
        sw = t.split("\n## [SW] Name")[1]
        rel = re.search(r"## \[SW\] Relationships\n(.*?)(?=\n## )", sw, re.S)
        sents = [x for x in re.split(r'(?<=[.!?"])\s+(?=[A-Z])', rel.group(1)) if PAT.search(x)] if rel else []
        if sents:
            out += [f"### {s} (Relationships)", " ".join(sents), ""]
    return "\n".join(out)


def build(name, stems, scope, extra=""):
    tpl = (ROOT / "framework" / "prompts" / "gpt-claimcheck-review.md").read_text(encoding="utf-8")
    tpl = tpl.replace(" (template; Claude fills the {{…}} parts)", "")
    parts = [BUDGET.format(scope=scope)]
    for i, s in enumerate(stems, 1):
        parts += [f"## Card {i}: {s.replace('-', ' ')} (draft, full file)", "", draft(s), ""]
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
    out = RUN[stems[0]] / "to-gpt.free.md"
    out.write_text(text, encoding="utf-8")
    print(f"{name}: {len(text):,} chars -> {out.relative_to(ROOT)}")


if __name__ == "__main__":
    build("A", ["Hoshimachi-Suisei", "AZKi"],
          "This is run A of two: Suisei and AZKi. Run B covers Ayame, Okayu, the pairs card and the English-cast lines.")
    build("B", ["Nakiri-Ayame", "Nekomata-Okayu", "JP-Senpai-Pairs"],
          "This is run B of two: Ayame, Okayu, the world card \"JP Senpai Pairs\" and the lines about the four added "
          "to the English cast's cards (listed at the end). Run A covered Suisei and AZKi.",
          "## Lines about the four added to the English cast's cards (2026-10-02; not yet promoted)\n\n" + en_lines())
