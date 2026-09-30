"""Audio check pipeline: extract windows from ragtag archives, transcribe (small.en), measure pitch/rate."""
import json, os, sys, subprocess, urllib.request, time, math
import imageio_ffmpeg
FF = imageio_ffmpeg.get_ffmpeg_exe()
PROXY = os.environ.get('HTTPS_PROXY', '')

def rt(vid):
    d = json.load(urllib.request.urlopen(f"https://archive.ragtag.moe/api/v1/search?v={vid}", timeout=30))
    s = d['hits']['hits'][0]['_source']
    files = s['files']
    pref = [f for f in files if f['name'].endswith(('.f251.webm', '.f140.m4a'))]
    if not pref:
        pref = sorted([f for f in files if f['name'].endswith(('.webm', '.mkv', '.mp4')) and '.f' not in f['name'].split(vid)[-1][:3]],
                      key=lambda f: -f['size']) or sorted([f for f in files if f['name'].endswith(('.webm','.mkv','.mp4'))], key=lambda f: -f['size'])
    f = pref[0]['name']
    base = s['drive_base'] if ':' in s['drive_base'] else 'gd:' + s['drive_base']
    url = f"https://content.archive.ragtag.moe/{base}/{vid}/{f}"
    # resolve redirect without downloading the body
    r = subprocess.run(['curl', '-sS', '-m', '30', '-r', '0-0', '-o', '/dev/null', '-w', '%{redirect_url}', url], capture_output=True, text=True)
    return (r.stdout.strip() or url), s['duration'], s['title']

def extract(url, start, dur, out):
    if os.path.exists(out) and os.path.getsize(out) > 10000: return
    cmd = [FF, '-hide_banner', '-loglevel', 'error', '-y', '-http_proxy', PROXY, '-ss', str(start), '-t', str(dur), '-i', url,
           '-vn', '-ac', '1', '-ar', '16000', out]
    for attempt in range(3):
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=1800)
        if r.returncode == 0 and os.path.exists(out) and os.path.getsize(out) > 10000: return
        time.sleep(5)
    raise RuntimeError(r.stderr[-400:])

def pitch_stats(wav, segs):
    import parselmouth, numpy as np
    snd = parselmouth.Sound(wav)
    vals = []
    for s in segs:
        a, b = max(0, s['start']), min(snd.duration, s['end'])
        if b - a < 0.3: continue
        part = snd.extract_part(from_time=a, to_time=b)
        p = part.to_pitch_ac(time_step=0.01, pitch_floor=75, pitch_ceiling=700)
        f = p.selected_array['frequency']
        vals.extend([x for x in f if x > 0])
    if len(vals) < 50: return None
    v = np.array(vals)
    q = lambda x: float(np.percentile(v, x))
    st = lambda hz: 12 * math.log2(hz / 100.0)  # semitones re 100 Hz
    return {'n_frames': int(len(v)), 'median_hz': round(q(50), 1), 'p10_hz': round(q(10), 1), 'p90_hz': round(q(90), 1),
            'p5_hz': round(q(5), 1), 'p95_hz': round(q(95), 1), 'range_p10_p90_semitones': round(st(q(90)) - st(q(10)), 1)}

def transcribe(model, wav):
    segs, info = model.transcribe(wav, language='en', vad_filter=True, word_timestamps=True, beam_size=5,
                                  condition_on_previous_text=False)
    out = []
    for s in segs:
        out.append({'start': round(s.start, 2), 'end': round(s.end, 2), 'text': s.text.strip(),
                    'words': [[round(w.start, 2), round(w.end, 2), w.word] for w in (s.words or [])]})
    return out

def run(jobs, threads):
    from faster_whisper import WhisperModel
    model = WhisperModel('small.en', device='cpu', compute_type='int8', cpu_threads=threads, download_root='models')
    for who, vid, start, dur, label in jobs:
        tag = f"{who}_{vid}_{label}"
        tj = f"trans/{tag}.json"
        if os.path.exists(tj): print('skip', tag, flush=True); continue
        t0 = time.time()
        try:
            url, total, title = rt(vid)
            s = start if start >= 0 else max(0, total + start)
            d = min(dur, total - s)
            wav = f"audio/{tag}.wav"
            extract(url, s, d, wav)
            segs = transcribe(model, wav)
        except Exception as e:
            print('FAIL', tag, str(e)[-300:], flush=True); continue
        words = sum(len(x['words']) for x in segs)
        speech = sum(x['end'] - x['start'] for x in segs)
        res = {'who': who, 'vid': vid, 'title': title, 'label': label, 'offset_s': s, 'dur_s': d,
               'words': words, 'speech_s': round(speech, 1), 'wpm_speech': round(words / (speech / 60), 1) if speech else None,
               'pitch': pitch_stats(wav, segs), 'segments': segs}
        json.dump(res, open(tj, 'w'))
        print(f"done {tag} {d}s audio in {round(time.time()-t0)}s words={words} pitch={res['pitch'] and res['pitch']['median_hz']}", flush=True)

if __name__ == '__main__':
    jobs = json.load(open(sys.argv[1]))
    run(jobs, int(sys.argv[2]) if len(sys.argv) > 2 else 2)
