import json, glob, re, sys, os
PAT = {
 'kronii': {'greeting kroniichiwa': r"kron+i+ ?chiwa|kronichiwa|kroni chiwa|chronichiwa", 'perfection': r"perfection", "that's on me": r"that'?s on me",
            'my bad': r"\bmy bad\b", 'just be better': r"just be better", 'kroyasumi/oyasumi': r"kro ?yasumi|oyasumi",
            'kronies/kromies': r"\bkro[nm]ies\b|\bcronies\b|\bhomies\b", 'gwak': r"\bgwa+k|\bgua+k|\bkwak", 'chat': r"\bchat\b",
            'yay': r"\byay\b", 'bro': r"\bbro\b", 'yap': r"\byap", 'rizz': r"\brizz", 'ragebait': r"rage ?bait", 'okay': r"\bokay\b"},
 'calli': {"what's up": r"what'?s up|what is up", 'dead beats': r"dead ?beats", 'guh': r"\bguh\b", 'listen': r"\blisten\b", 'whatever man': r"whatever,? man",
           'your boy': r"your boy", 'big ups': r"big ups", 'peace': r"\bpeace\b", 'remember me': r"remember me", 'dad': r"\bdad\b", 'cringe': r"cringe",
           "y'all": r"\by'?all\b", 'senpai': r"senpai", 'gonna': r"\bgonna\b", 'dude': r"\bdude\b", 'man': r"\bman\b"},
 'kiara': {'kikkeriki (any)': r"kik+eri|kicker|kikeri|kiki ?ri|kiki nikki|key ?caddy|kitty key", 'oh my god': r"oh my god|oh my gosh", 'wawa': r"\bwawa\b",
           'okie dokie': r"okie|okey ?dokey|okie ?dokie", 'in german we say': r"in german,? we say", 'tangent': r"tangent", 'chat': r"\bchat\b",
           'cute chicken': r"cute chicken", 'kfp': r"\bkfp\b", 'danke': r"danke|vielen", 'auf wiedersehen': r"auf wieder|wiedersehen", 'guys': r"\bguys\b"},
 'ina': {'wah': r"\bwah+\b", 'tako time': r"tako ?time|taco time", 'good morning afternoon evening': r"morning,? afternoon,? (and )?evening", 'humu': r"\bhumu|\bhmm",
         'inaff': r"\binaff|ina ?enough", 'anyways': r"\banyways?\b", 'like': r"\blike\b", 'bye-bye': r"bye[- ]bye", 'crowbar/bonk': r"crowbar|bonk",
         'i think': r"\bi think\b", 'tomorrow': r"tomorrow", 'takodachi': r"takodachi|tako ?dachi", "we'll see": r"we'?ll see"},
 'gura': {'hello x3': r"hello,? hello,? hello", 'hello': r"\bhello\b", 'chumbuds': r"chum ?buds?", 'shrimp': r"shrimp", 'hungry': r"hungry", "i'm cute": r"i'?m cute",
          'what do you mean': r"what do you mean", 'let me in': r"let me in", 'goodbye': r"good ?bye", 'ban pants': r"ban pants|pants", 'heck': r"\bheck\b",
          'freaking': r"freak(ing|in)", 'oh no': r"oh no", 'wait wait': r"wait,? wait", 'you guys': r"you guys"},
 'ame': {'ground pound': r"ground ?pound", 'your mom': r"your mom", 'ping': r"\bping\b", 'okay/ahkay': r"\bokay\b|\bahkay\b|\bokey\b", 'time travel': r"time[- ]?travel",
         'detective': r"detective", 'hello x2+': r"hello,? hello", 'bye-bye': r"bye[- ]bye", 'cute cute': r"cute,? cute", 'teamates': r"team ?mates",
         'you guys': r"you guys", 'hic': r"\bhic\b|hiccup", 'wait what': r"wait,? what", 'british': r"british|ello|luvs?"},
}
SWEAR = r"\bf+u+c*k+\w*|\bf\*+\w*|\bshit\w*|\bdamn\w*|\bbitch\w*|\bass\b|\basshole|\bhell\b|\bgoddamn|\bcrap\b|\bdick\b|\bbastard"

def load(who):
    out = []
    for f in sorted(glob.glob(f'trans/{who}_*.json')):
        out.append(json.load(open(f)))
    return out

def yt(vid, t): return f"https://youtu.be/{vid}?t={int(t)}"

def report(who):
    runs = load(who)
    lines = []
    tot_speech = sum(r['speech_s'] for r in runs)
    tot_audio = sum(r['dur_s'] for r in runs)
    lines.append(f"## {who}: {len(runs)} windows, {round(tot_audio/60)} min of audio, {round(tot_speech/60)} min of detected speech")
    for r in runs:
        p = r['pitch'] or {}
        lines.append(f"- {r['label']}: {r['vid']} @{r['offset_s']}s +{r['dur_s']}s | {r['title'][:60]} | words {r['words']} | wpm {r['wpm_speech']} | F0 median {p.get('median_hz')} Hz, p10–p90 {p.get('p10_hz')}–{p.get('p90_hz')} Hz ({p.get('range_p10_p90_semitones')} st)")
    pats = dict(PAT[who]); pats['SWEARS'] = SWEAR
    hours = tot_audio / 3600
    for name, rx in pats.items():
        hits = []
        for r in runs:
            for s in r['segments']:
                for m in re.finditer(rx, s['text'], re.I):
                    hits.append((r, s, m.group(0)))
        if not hits:
            lines.append(f"  * {name}: 0"); continue
        words = {}
        for _, _, g in hits: words[g.lower()] = words.get(g.lower(), 0) + 1
        lines.append(f"  * {name}: {len(hits)} ({round(len(hits)/hours,1)}/h) {dict(sorted(words.items(), key=lambda x:-x[1])[:8])}")
        for r, s, g in hits[:int(sys.argv[2]) if len(sys.argv) > 2 else 3]:
            t = r['offset_s'] + s['start']
            lines.append(f"      - [{r['label']} {int(t//3600)}:{int(t%3600//60):02d}:{int(t%60):02d}] {s['text'][:160]}  ({yt(r['vid'], t)})")
    return "\n".join(lines)

if __name__ == '__main__':
    print(report(sys.argv[1]))
