"""Recompute pitch with female-voice settings (100-600 Hz) over word intervals only; merge adjacent words."""
import json, glob, math, sys
import parselmouth, numpy as np
def intervals(segs, gap=0.25):
    iv = []
    for s in segs:
        for a, b, w in s['words']:
            if iv and a - iv[-1][1] < gap: iv[-1][1] = max(iv[-1][1], b)
            else: iv.append([a, b])
    return [x for x in iv if x[1] - x[0] >= 0.25]
def stats(v):
    q = lambda p: float(np.percentile(v, p)); st = lambda hz: 12 * math.log2(hz / 100.0)
    return {'n_frames': int(len(v)), 'median_hz': round(q(50)), 'p10_hz': round(q(10)), 'p90_hz': round(q(90)),
            'range_p10_p90_semitones': round(st(q(90)) - st(q(10)), 1)}
out = {}
for f in sorted(glob.glob('trans/*.json')):
    r = json.load(open(f))
    wav = f"audio/{f.split('/')[-1][:-5]}.wav"
    try: snd = parselmouth.Sound(wav)
    except Exception: continue
    vals = []
    for a, b in intervals(r['segments']):
        b = min(b, snd.duration)
        if b - a < 0.25: continue
        p = snd.extract_part(from_time=a, to_time=b).to_pitch_ac(time_step=0.01, pitch_floor=100, pitch_ceiling=600)
        vals += [x for x in p.selected_array['frequency'] if x > 0]
    if len(vals) < 200: continue
    r['pitch_f'] = stats(np.array(vals)); json.dump(r, open(f, 'w'))
    out[f] = r['pitch_f']
    print(f.split('/')[-1][:-5], r['pitch_f'], 'wpm', r['wpm_speech'])
