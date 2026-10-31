"""Pull greetings, sign-offs, catchphrases, vocabulary, speech traits, tone shifts, sources and ASR-checked lines
out of the novel-lab character files into one list."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2] / "projects" / "holoen"

def section(text, title_rx, level="## "):
    m = re.search(rf"^{level}{title_rx}.*$", text, re.M)
    if not m:
        return ""
    rest = text[m.end():]
    end = re.search(r"^## ", rest, re.M)
    return rest[: end.start()] if end else rest

def top_bullets(block):
    """[(label, [sub-bullet texts], own text)] for '- **Label:** ...' bullets (sub-bullets indented)."""
    out, cur = [], None
    lines = block.split("\n")
    for ln in lines:
        if re.match(r"^### ", ln):
            break
        m = re.match(r"^- \*\*(.+?)\*\*:?\s*(.*)$", ln)
        if m:
            cur = [m.group(1).rstrip(":").strip(), [], m.group(2).strip()]
            out.append(cur)
            continue
        if cur is None:
            continue
        sm = re.match(r"^  - (.*)$", ln)
        if sm:
            cur[1].append(sm.group(1).strip())
        elif re.match(r"^    \S", ln) and cur[1]:
            cur[1][-1] += " " + ln.strip()
        elif re.match(r"^  \S", ln):
            if cur[1]:
                cur[1][-1] += " " + ln.strip()
            else:
                cur[2] += " " + ln.strip()
    return out

def sw(text, field):
    m = re.search(rf"^## \[SW\] {re.escape(field)}\s*\n(.*?)(?=^## |\Z)", text, re.M | re.S)
    return m.group(1).strip() if m else ""

def sources(text):
    sec = section(text, r"Sources")
    out = {}
    for ln in sec.split("\n"):
        m = re.match(r"^- \*?\*?([A-Z]{1,3}\d+[a-z]?)\*?\*?[\s:：]+(.*)$", ln.strip())
        if m:
            urls = re.findall(r"https?://\S+", m.group(2))
            out[m.group(1)] = {"desc": m.group(2).strip(), "urls": [u.rstrip(").,;") for u in urls]}
    return out

def tone_table(text):
    vp = section(text, r"Voice Profile")
    m = re.search(r"### Tone Shifts(.*?)(?=^### |\Z)", vp, re.M | re.S)
    rows = []
    if m:
        for ln in m.group(1).split("\n"):
            if ln.startswith("|") and not re.match(r"^\|\s*-", ln) and "Situation" not in ln:
                cells = [c.strip() for c in ln.strip().strip("|").split("|")]
                if len(cells) >= 3:
                    rows.append(cells[:3])
    return rows

def sample_lines(text):
    vp = section(text, r"Voice Profile")
    m = re.search(r"### Sample Lines(.*?)(?=^### |\Z)", vp, re.M | re.S)
    return [re.sub(r"^\d+\.\s*", "", l).strip() for l in (m.group(1).split("\n") if m else []) if re.match(r"^\d+\.", l.strip())]

def extract() -> list[dict]:
    members = []
    for f in sorted((ROOT / "bible" / "characters").glob("*.md")):
        t = f.read_text(encoding="utf-8")
        vp = section(t, r"Voice Profile")
        members.append({
            "file": f.stem, "name": sw(t, "Name"), "groups": sw(t, "Groups"), "other_names": sw(t, "Other Names"),
            "dialogue_style": sw(t, "Dialogue Style"), "catchphrases_sw": sw(t, "Catchphrases"),
            "voice": sw(t, "Voice & Delivery"), "bullets": top_bullets(vp), "tone": tone_table(t),
            "samples": sample_lines(t), "sources": sources(t),
            "checked": (re.search(r"^## Sources \(checked ([\d-]+)\)", t, re.M) or [None, ""])[1],
        })
    return members
