"""Second-model check for Japanese quotes: re-transcribe a clip around each candidate line with whisper medium
(multilingual, ja) and report whether the candidate (normalized: katakana -> hiragana, punctuation and spaces
dropped) appears verbatim in the second model's text, plus the longest shared run.

    python3 jconfirm.py items.json [threads]
items: [[who, vid, t_seconds_absolute, "candidate line"], ...]
"""
import json, glob, sys, re, os, subprocess
from difflib import SequenceMatcher
import imageio_ffmpeg
FF = imageio_ffmpeg.get_ffmpeg_exe()
wins = [json.load(open(f)) | {'_f': f} for f in glob.glob('trans/*.json')]


def locate(vid, t):
    for w in wins:
        if w['vid'] == vid and w['offset_s'] <= t < w['offset_s'] + w['dur_s']:
            return w


def norm(s):
    s = ''.join(chr(ord(c) - 0x60) if 'ァ' <= c <= 'ヶ' else c for c in s)
    s = s.translate(str.maketrans('ぁぃぅぇぉ', 'あいうえお'))
    return re.sub(r"[\s、。！？!?…・,.「」『』（）()〜~ーｰ\-－♪★☆♡❤]", "", s.lower())


def longest_shared(a, b):
    m = SequenceMatcher(None, a, b, autojunk=False).find_longest_match(0, len(a), 0, len(b))
    return a[m.a:m.a + m.size]


if __name__ == '__main__':
    from faster_whisper import WhisperModel
    m = WhisperModel('medium', device='cpu', compute_type='int8',
                     cpu_threads=int(sys.argv[2]) if len(sys.argv) > 2 else 2, download_root='models')
    items = json.load(open(sys.argv[1]))
    out = []
    os.makedirs('clips', exist_ok=True)
    for who, vid, t, expect in items:
        w = locate(vid, t)
        if not w:
            print('NOWIN', who, vid, t, flush=True)
            continue
        wav = w['_f'].replace('trans/', 'audio/').replace('.json', '.wav')
        rel = t - w['offset_s']
        a = max(0, rel - 6)
        clip = f"clips/{vid}_{int(t)}.wav"
        subprocess.run([FF, '-hide_banner', '-loglevel', 'error', '-y', '-ss', str(a), '-t', '30', '-i', wav, clip],
                       check=True)
        segs, _ = m.transcribe(clip, language='ja', beam_size=5, vad_filter=False, condition_on_previous_text=False)
        text = ''.join(s.text.strip() for s in segs)
        ne, nt = norm(expect), norm(text)
        shared = longest_shared(ne, nt)
        res = {'who': who, 'vid': vid, 't': t, 'expect': expect, 'medium': text, 'verbatim': ne in nt,
               'shared': shared, 'shared_ratio': round(len(shared) / max(1, len(ne)), 2)}
        out.append(res)
        print(f"{'OK ' if res['verbatim'] else res['shared_ratio']} {who} {vid} t={t} | {expect} || {text[:140]}",
              flush=True)
    json.dump(out, open(sys.argv[1].replace('.json', '.out.json'), 'w'), indent=1, ensure_ascii=False)
