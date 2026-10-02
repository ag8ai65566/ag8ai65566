"""Marker counts and window table for the Japanese audio check.

    python3 jstats.py <who>
"""
import json, glob, re, sys
from collections import Counter

MARK = {
    'first person 余 (yo)': r'余', 'first person 僕 (boku)': r'僕|ぼく|ボク', 'first person 私': r'私|わたし|あたし',
    'third person すいちゃん': r'すいちゃん|スイちゃん|スイッちゃん|水星ちゃん', 'third person あずき/AZKi': r'AZKi|あずき|アズキ',
    'なんか': r'なんか', 'まあ': r'まあ|まぁ', 'ちょっと待って': r'ちょっと待って', 'やばい': r'やば',
    'かわいい': r'かわいい|可愛い|カワイイ', 'えっ/え?': r'^え[っ?？!！]|^えぇ', 'laugh (はは/ふふ/笑)': r'ははは|ふふ|笑|ひひ|へへ',
    'swear (くそ/ふざけ/殺)': r'くそ|クソ|ふざけ|殺す|死ね', 'ありがとう': r'ありがとう', 'English (Latin letters)': r'[A-Za-z]{3,}',
    'もぐもぐ': r'もぐもぐ|モグモグ', 'こんなきり/こんにちは': r'こんなきり|こんにちは|こんばんは',
}


def main(who):
    rows = []
    cnt = Counter()
    for f in sorted(glob.glob(f'trans/{who}_*.json')):
        d = json.load(open(f))
        p = d['pitch'] or {}
        rows.append((d['label'], d['vid'], d['title'][:50], d['offset_s'], d['dur_s'], round(d['speech_s'] / 60, 1),
                     d['words'], d.get('cpm_speech'), p.get('median_hz'), p.get('p10_hz'), p.get('p90_hz')))
        for s in d['segments']:
            for k, pat in MARK.items():
                cnt[(d['label'], k)] += len(re.findall(pat, s['text']))
    print('| Window | Stream | start | dur | speech min | chars | chars/min | F0 median | p10–p90 |')
    for r in rows:
        print(f"| {r[0]} | {r[1]} {r[2]} | {r[3]} | {r[4]} | {r[5]} | {r[6]} | {r[7]} | {r[8]} | {r[9]}–{r[10]} |")
    labels = [r[0] for r in rows]
    print('\nmarker', *labels, sep=' | ')
    for k in MARK:
        print(k, *[cnt[(l, k)] for l in labels], sep=' | ')


if __name__ == '__main__':
    main(sys.argv[1])
