#!/usr/bin/env python3
"""Build the task-09 voice and performance audit runs (one GPT quota window each).

    python3 tools/mk_voice_audit.py v1 v2 v3     # v4 once the holoX cards are promoted (runs E and F merged)

v1: Myth and Promise (Calli, Kiara, Ina, Gura, Ame, Kronii, IRyS, Fauna, Mumei, Bae)
v2: Advent and Justice (Shiori, Bijou, Nerissa, Fuwawa, Mococo, Elizabeth, Gigi, Cecilia, Raora)
v3: hololive JP (Suisei, AZKi, Ayame, Okayu, Marine, Noel, Lamy, Botan, Vivi)
v4: Secret Society holoX (La+, Lui, Koyori, Chloe, Iroha), after runs E and F are merged

Each run gets a run directory `runs/<stamp>-check-QA-voice-<group>/` with to-gpt.free.md; inputs are read from
the bible and export/elevenlabs/ at build time, so rebuild right before queueing if cards changed. The result
is merged into research/qa/voice-delivery.md (V13, V19); sheets are stamped after their fixes are merged.
"""
import datetime as dt
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
import qa_runs  # noqa: E402

P = ROOT / "projects" / "holoen"
GROUPS = {
    "v1": ("Myth and Promise", ["Mori-Calliope", "Takanashi-Kiara", "Ninomae-Inanis", "Gawr-Gura", "Watson-Amelia",
                                "Ouro-Kronii", "IRyS", "Ceres-Fauna", "Nanashi-Mumei", "Hakos-Baelz"]),
    "v2": ("Advent and Justice", ["Shiori-Novella", "Koseki-Bijou", "Nerissa-Ravencroft", "Fuwawa-Abyssgard",
                                  "Mococo-Abyssgard", "Elizabeth-Rose-Bloodflame", "Gigi-Murin", "Cecilia-Immergreen",
                                  "Raora-Panthera"]),
    "v3": ("hololive JP", ["Hoshimachi-Suisei", "AZKi", "Nakiri-Ayame", "Nekomata-Okayu", "Houshou-Marine",
                           "Shirogane-Noel", "Yukihana-Lamy", "Shishiro-Botan", "Kikirara-Vivi"]),
    "v4": ("Secret Society holoX", ["Laplus-Darknesss", "Takane-Lui", "Hakui-Koyori", "Sakamata-Chloe",
                                    "Kazama-Iroha"]),
}
VOICE = ["Name", "Dialogue Style", "Catchphrases", "Voice & Delivery", "Audio Tags"]


def fields(text):
    return {m.group(1).strip(): m.group(2).strip()
            for m in re.finditer(r"^## \[SW\] ([^\n]+)\n(.*?)(?=^## |\Z)", text, re.M | re.S)}


def build(gid):
    title, stems = GROUPS[gid]
    parts = ["## Shared inputs", "",
             "### export/elevenlabs/sudowrite-style.md (the Style block every scene uses)", "",
             (P / "export" / "elevenlabs" / "sudowrite-style.md").read_text(encoding="utf-8"), "",
             "### novel-lab/docs/elevenlabs-v4.md (the project's ElevenLabs guide)", "",
             (ROOT / "docs" / "elevenlabs-v4.md").read_text(encoding="utf-8"), ""]
    missing = []
    for s in stems:
        card = P / "bible" / "characters" / f"{s}.md"
        sheet = P / "export" / "elevenlabs" / f"{s}.md"
        if not card.exists() or not sheet.exists():
            missing.append(s)
            continue
        f = fields(card.read_text(encoding="utf-8"))
        parts += [f"## Member: {f.get('Name', s)} (`{s}`)", "", "### Card voice fields (bible)", ""]
        parts += [f"**{k}:** {f[k]}" for k in VOICE if k in f] + [""]
        parts += [f"### Sheet: export/elevenlabs/{s}.md", "", sheet.read_text(encoding="utf-8"), ""]
    if missing:
        sys.exit(f"{gid}: not in the bible or no sheet yet: {', '.join(missing)}")
    tpl = (ROOT / "framework" / "prompts" / "gpt-voice-audit.md").read_text(encoding="utf-8")
    text = (tpl.replace("{{group}}", f"{title} ({len(stems)} members)").replace("{{group_id}}", gid.upper())
            .replace("{{rules}}", qa_runs.RULES).replace("{{inputs}}", "\n".join(parts)))
    assert "{{" not in text
    existing = sorted((P / "runs").glob(f"*-check-QA-voice-{gid}"))
    run = existing[-1] if existing and not (existing[-1] / "gpt-free.md").exists() else \
        P / "runs" / f"{dt.datetime.utcnow():%Y%m%d-%H%M}-check-QA-voice-{gid}"
    run.mkdir(parents=True, exist_ok=True)
    (run / "brief.md").write_text(f"# Task 09 voice audit: {title}\n\nBuilt by tools/mk_voice_audit.py; the prompt "
                                  "is to-gpt.free.md. Merge into research/qa/voice-delivery.md.\n", encoding="utf-8")
    (run / "to-gpt.free.md").write_text(text, encoding="utf-8")
    print(f"{gid}: {len(text):,} chars -> {run.relative_to(ROOT)}")


if __name__ == "__main__":
    if len(sys.argv) < 2 or any(g not in GROUPS for g in sys.argv[1:]):
        sys.exit(__doc__)
    for g in sys.argv[1:]:
        build(g)
