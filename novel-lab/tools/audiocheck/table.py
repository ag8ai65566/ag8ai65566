import json, glob, sys
who = sys.argv[1]
print("| Window | Stream | Segment | Speech (min) | Words | Words/min of speech | F0 median | F0 p10–p90 |")
print("|---|---|---|---|---|---|---|---|")
for f in sorted(glob.glob(f'trans/{who}_*.json')):
    r = json.load(open(f)); p = r.get('pitch_f') or {}
    s = r['offset_s']; e = s + r['dur_s']
    title = r['title'][:48].replace('|', '/')
    hm = lambda t: f"{int(t//3600)}:{int(t%3600//60):02d}:{int(t%60):02d}"
    print(f"| {r['label']} | [{title}](https://youtu.be/{r['vid']}) | [{hm(s)}–{hm(e)}](https://youtu.be/{r['vid']}?t={int(s)}) | {round(r['speech_s']/60,1)} | {r['words']} | {r['wpm_speech']} | {p.get('median_hz','–')} Hz | {p.get('p10_hz','–')}–{p.get('p90_hz','–')} Hz |")
