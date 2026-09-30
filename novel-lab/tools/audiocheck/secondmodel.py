"""Build the 'Second-model check' section of each audio-check report from quotes*.out.json."""
import json, glob, re, sys
def norm(s): return re.findall(r"[a-z0-9']+", s.lower())
def hms(t): t = int(t); return f"{t//3600}:{t%3600//60:02d}:{t%60:02d}"
# Manual verdicts where the bag-of-words overlap alone would mislead (read by Claude).
V = json.load(open('verdicts.json'))
def excerpt(exp, med, pad=3):
    E, W = norm(exp), med.split()
    Wn = [''.join(norm(w)) for w in W]
    best, bi = -1, 0
    n = max(1, len(E))
    for i in range(len(W)):
        sc = sum(1 for x in Wn[i:i + n] if x in E)
        if sc > best: best, bi = sc, i
    s = ' '.join(W[max(0, bi - pad): bi + n + pad])
    return s[:160] + ('…' if len(s) > 160 else '')
rows = {}
for f in sorted(glob.glob('quotes*.out.json')):
    for x in json.load(open(f)):
        rows[(x['who'], x['vid'], x['t'])] = x
for who in sys.argv[1:]:
    print("## Second-model check (whisper medium.en)\n")
    print("Each line below was cut from the archived audio (a window of about 24–60 s around the first model's")
    print("timestamp) and transcribed again by a larger model. \"Agrees\" means the second model produced the same")
    print("words; it is still machine transcription, not listening. Lines that did not agree were removed from")
    print("the character card.\n")
    print("| First model (small.en) | Link | Second model (medium.en), excerpt | Verdict |")
    print("|---|---|---|---|")
    for (w, vid, t), x in sorted(rows.items(), key=lambda k: (k[0][1], k[0][2])):
        if w != who: continue
        key = f"{vid}@{t}"
        verdict = V.get(key) or ("Agrees" if x['overlap'] >= 0.9 else f"CHECK {x['overlap']}")
        exp = x['expect'].replace('|', '/')
        med = excerpt(x['expect'], x['medium']).replace('|', '/')
        print(f"| \"{exp}\" | [{hms(x['at'])}](https://youtu.be/{vid}?t={x['at']}) | \"{med}\" | {verdict} |")
    print()
