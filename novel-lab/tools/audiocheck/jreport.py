"""Build research/audio-check/<who>.md for a Japanese-speaking member.

    python3 jreport.py <who> <Display Name> <claims.md> <out.md> <confirm.out.json> [...]

claims.md holds the hand-written "Claims checked" table and notes (Claude's reading of the transcripts).
"""
import json, glob, re, sys
from jstats import MARK
from collections import Counter

HEAD = """# Audio check — {name} (2026-10-02)

Method: windows from the public stream archive archive.ragtag.moe (YouTube blocks this environment),
transcribed in Japanese with faster-whisper small (multilingual), pitch measured with Praat (100–600 Hz, speech
segments only). Tools and limits: `novel-lab/tools/audiocheck/README.md`. **This is not a listening check**: the
audio was machine-transcribed and acoustically measured, and the transcripts were reviewed in context. Lines used
on the character card were re-transcribed by a second model (whisper medium, multilingual) and compared after
folding katakana to hiragana and dropping punctuation (see the end of this file). Transcription does not write
laughs reliably, and Japanese ASR often picks different kanji or kana for the same word; only spans both models
render identically are quoted. Measurements describe the sampled recording and ASR segmentation; game audio,
music and other voices prevent treating them as isolated vocal measurements.

All windows are from 2026. Only in-scope public performance material is used: personal remarks in the chats
(family, childhood, health, trips, daily life) are not quoted or summarized here.
"""


def reading(s):
    """Hiragana reading (pykakasi), so that 歌姫 and うたひめ compare equal; falls back to the surface form."""
    try:
        import pykakasi
    except ImportError:
        return s
    from jconfirm import norm
    return norm("".join(x["hira"] for x in pykakasi.kakasi().convert(s)))


def excerpt(medium, key, margin=6):
    """The part of the second model's text around `key` (normalized), so the report never carries the rest of the
    clip (which may hold out-of-scope personal remarks). Falls back to the first 60 characters."""
    from jconfirm import norm
    idx, chars = [], []
    for i, c in enumerate(medium):
        n = norm(c)
        if n:
            idx.append(i)
            chars.append(n)
    flat = "".join(chars)
    k = norm(key)
    pos = flat.find(k) if k else -1
    if pos < 0:
        return medium[:60] + "…"
    a, b = idx[pos], idx[min(pos + len(k), len(idx)) - 1] + 1
    lo, hi = max(0, a - margin), min(len(medium), b + margin)
    return ("…" if lo else "") + medium[lo:hi] + ("…" if hi < len(medium) else "")


def ts(sec):
    sec = int(sec)
    return f"{sec // 3600}:{sec % 3600 // 60:02d}:{sec % 60:02d}"


def main(who, name, claims, out, confirms):
    rows, cnt, labels = [], Counter(), []
    for f in sorted(glob.glob(f'trans/{who}_*.json')):
        d = json.load(open(f))
        p = d['pitch'] or {}
        a, b = d['offset_s'], d['offset_s'] + d['dur_s']
        rows.append(f"| {d['label']} | [{d['title'][:48].replace('|', '｜')}](https://youtu.be/{d['vid']}) | "
                    f"[{ts(a)}–{ts(b)}](https://youtu.be/{d['vid']}?t={int(a)}) | {round(d['speech_s'] / 60, 1)} | "
                    f"{d['words']} | {d.get('cpm_speech')} | {round(p.get('median_hz', 0))} Hz | "
                    f"{round(p.get('p10_hz', 0))}–{round(p.get('p90_hz', 0))} Hz |")
        labels.append(d['label'])
        for s in d['segments']:
            for k, pat in MARK.items():
                cnt[(d['label'], k)] += len(re.findall(pat, s['text']))
    md = [HEAD.format(name=name), "## Windows measured", "",
          "| Window | Stream | Segment | Speech (min) | Characters | Characters/min of speech | F0 median | F0 p10–p90 |",
          "|---|---|---|---|---|---|---|---|"] + rows + [
          "", '"Characters/min of speech" = transcribed kana and kanji (punctuation dropped) ÷ minutes inside whisper\'s '
          "speech segments; it is a rough pace index for comparing windows, not a mora count.", "",
          "## Marker counts (first model)", "", "| Marker | " + " | ".join(labels) + " |",
          "|---|" + "---|" * len(labels)]
    for k in MARK:
        vals = [cnt[(l, k)] for l in labels]
        if any(vals):
            md.append(f"| {k} | " + " | ".join(str(v) for v in vals) + " |")
    md += ["", open(claims).read().rstrip(), "", "## Second model (whisper medium) on quoted lines", "",
           "| First model (small) | At | Second model (medium), excerpt | Verdict |", "|---|---|---|---|"]
    for c in confirms:
        for r in json.load(open(c)):
            if r['who'] != who:
                continue
            ex = excerpt(r['medium'], r['expect'] if r['verbatim'] else (r.get('shared') or r['expect'])).replace('|', '｜')
            same_reading = not r['verbatim'] and reading(r['expect']) in reading(r['medium'])
            if r['verbatim']:
                v = "**Shared span (computed):** whole line (kana/kanji folded)"
            elif same_reading:
                v = "**Shared span (computed):** whole line (same reading; the models spell a word differently)"
            elif r['shared_ratio'] >= 0.5:
                v = f"**Partial (computed):** shared run \"{r['shared']}\"; only that part is quoted"
            else:
                v = "**Not confirmed** by the second model; not quoted"
            md.append(f"| \"{r['expect']}\" | [{ts(r['t'])}](https://youtu.be/{r['vid']}?t={int(r['t'])}) | \"{ex}\" | {v} |")
    open(out, 'w').write("\n".join(md) + "\n")
    print('wrote', out)


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5:])
