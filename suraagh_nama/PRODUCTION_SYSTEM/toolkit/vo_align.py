"""Align the full voice-over ASR to the 21 script parts. Writes parts.json [{part, s, e}] and prints a table."""
import json, re, sys, glob, os, difflib, unicodedata
PARTS = sorted(glob.glob('/home/user/Files/suraagh_nama/03_legends_lane/ep01_saiful_malook/vo_parts/P*.txt'))
asr = json.load(open('asr.json'))

def norm(s):
    s = unicodedata.normalize('NFKC', s)
    s = re.sub('[ً-ٰٟ۪-ۭ]', '', s)            # harakat
    for a, b in (('ے', 'ی'), ('ئ', 'ی'), ('ي', 'ی'), ('ك', 'ک'), ('ۂ', 'ہ'), ('ة', 'ہ'), ('ھ', ''), ('ں', 'ن'), ('ؤ', 'و'), ('آ', 'ا'), ('أ', 'ا')):
        s = s.replace(a, b)
    return re.sub(r'[^\w]|[_0-9a-zA-Z]', '', s)

# script chars with part index
sc, sp = [], []
for i, p in enumerate(PARTS):
    t = norm(open(p).read())
    sc += list(t); sp += [i] * len(t)
# asr chars with time
ac, at = [], []
for seg in asr:
    for s, e, w in seg['w']:
        t = norm(w)
        for j, ch in enumerate(t):
            ac.append(ch); at.append(s + (e - s) * j / max(len(t), 1))
end_time = asr[-1]['e']
m = difflib.SequenceMatcher(None, sc, ac, autojunk=False)
s2a = {}
for a, b, n in m.get_matching_blocks():
    for k in range(n): s2a[a + k] = b + k
starts = []
for i in range(len(PARTS)):
    idx = [k for k in range(len(sc)) if sp[k] == i]
    hit = next((s2a[k] for k in idx if k in s2a), None)
    cov = sum(1 for k in idx if k in s2a) / max(len(idx), 1)
    starts.append((at[hit] if hit is not None else None, cov))
out = []
for i, p in enumerate(PARTS):
    s = starts[i][0]; e = next((starts[j][0] for j in range(i + 1, len(PARTS)) if starts[j][0] is not None), end_time)
    out.append(dict(part=os.path.basename(p)[:-4], s=s, e=e, cov=round(starts[i][1], 2)))
    print(f"{out[-1]["part"]:18s} {str(None if s is None else round(s,2)):>8} {round(e,2):>8}  cov {out[-1]['cov']}")
json.dump(out, open('parts_raw.json', 'w'), ensure_ascii=False, indent=1)
