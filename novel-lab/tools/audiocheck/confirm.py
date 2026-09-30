"""Second-model check: re-transcribe short windows around quoted lines with whisper medium.en and compare."""
import json, glob, sys, re, os, subprocess
import imageio_ffmpeg
FF = imageio_ffmpeg.get_ffmpeg_exe()
wins = [json.load(open(f)) | {'_f': f} for f in glob.glob('trans/*.json')]
def locate(vid, t):
    for w in wins:
        if w['vid'] == vid and w['offset_s'] <= t < w['offset_s'] + w['dur_s']:
            return w
def norm(s): return re.findall(r"[a-z']+", s.lower())
def overlap(a, b):
    A, B = norm(a), norm(b)
    if not A: return 0
    hit = sum(1 for x in A if x in B)
    return round(hit / len(A), 2)
from faster_whisper import WhisperModel
m = WhisperModel('medium.en', device='cpu', compute_type='int8', cpu_threads=int(sys.argv[2]) if len(sys.argv) > 2 else 2, download_root='models')
items = json.load(open(sys.argv[1]))
out = []
os.makedirs('clips', exist_ok=True)
for who, vid, t, expect in items:
    w = locate(vid, t)
    if not w: print('NOWIN', who, vid, t); continue
    wav = w['_f'].replace('trans/', 'audio/').replace('.json', '.wav')
    rel = t - w['offset_s']
    exp = norm(expect)
    words = [(a, b, norm(x)) for s in w['segments'] for a, b, x in s['words'] if rel - 20 <= a <= rel + 60]
    best, besta = -1, rel
    for i in range(len(words)):
        seq = [z for (_, _, ws) in words[i:i + len(exp)] for z in ws][:len(exp)]
        sc0 = sum(1 for x, y in zip(seq, exp) if x == y)
        if sc0 > best: best, besta = sc0, words[i][0]
    lo = min(besta, rel)
    dur = max(24, (besta - lo) + len(exp) * 0.5 + 14)
    a = max(0, lo - 6)
    clip = f"clips/{vid}_{int(t)}.wav"
    subprocess.run([FF, '-hide_banner', '-loglevel', 'error', '-y', '-ss', str(a), '-t', str(dur), '-i', wav, clip], check=True)
    segs, _ = m.transcribe(clip, language='en', beam_size=5, vad_filter=False, condition_on_previous_text=False)
    text = ' '.join(s.text.strip() for s in segs)
    sc = overlap(expect, text)
    at = int(w['offset_s'] + besta)
    out.append({'who': who, 'vid': vid, 't': t, 'at': at, 'expect': expect, 'medium': text, 'overlap': sc})
    print(f"{sc:4} {who} {vid} at={at} | {expect[:70]} || {text[:160]}", flush=True)
json.dump(out, open(sys.argv[1].replace('.json', '.out.json'), 'w'), indent=1)
