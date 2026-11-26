"""SRT captions from the script text (correct spelling), timed by the ASR alignment, on the final timeline."""
import json, re, glob, os, difflib
exec(open('align.py').read().split('starts = []')[0])          # reuses norm, sc, sp, ac, at, s2a
tl = json.load(open('../real/segs/timeline.json')); blocks = [b for b in tl['blocks'] if b['kind'] == 'vo']
B = {b['name']: b for b in blocks}
def to_tl(t):
    for b in blocks:
        if b['s'] - .3 <= t < b['e'] + .3: return b['t'] + t - b['s']
    return None
cues = []
for i, p in enumerate(PARTS):
    name = os.path.basename(p)[:-4]; raw = open(p).read().strip()
    for k2 in ('Hazara University', 'Khari Sharif', 'glacial lake'): raw = raw.replace(k2, k2.replace(' ', '\u00a0'))
    # phrases: split at sentence ends / ellipses / commas, max ~9 words each
    pieces = [x.strip() for x in re.split(r'(?<=[۔؟!])\s+|(?<=\.\.\.)\s+|(?<=،)\s+|\n+', raw) if x.strip()]
    ph = []
    for x in pieces:
        ws = [w for w in x.split(" ") if w]
        while len(ws) > 10: ph.append(' '.join(ws[:8])); ws = ws[8:]
        ph.append(' '.join(ws))
    b = B[name]
    if name.endswith('VERSE') or name.endswith('LOUDSPEAKER') or name.endswith('DEMON') or name.endswith('FAIRY') or name.endswith('PRINCE'):
        # short character/verse parts: spread evenly over the part (verse not in the ASR)
        lines = [l.strip() for l in raw.replace('"', '').split('\n') if l.strip()] if name.endswith('VERSE') else [raw.replace('"', '')]
        n = len(lines); d = (b['e'] - b['s']) / n
        for k, l in enumerate(lines): cues.append((b['t'] + k * d + .1, b['t'] + (k + 1) * d - .1, l))
        continue
    # char offsets of each phrase inside this part's normalised text
    idx = [k for k in range(len(sc)) if sp[k] == i]; base = idx[0]; pos = 0
    for x in ph:
        n = len(norm(x)); ks = range(base + pos, base + pos + n); pos += n
        hit = [s2a[k] for k in ks if k in s2a]
        if not hit: continue
        t0, t1 = to_tl(at[hit[0]]), to_tl(at[hit[-1]] + .25)
        if t0 is None or t1 is None: continue
        cues.append((t0, max(t1, t0 + .8), x.replace('"', '')))
cues.sort()
for k in range(len(cues) - 1):                                  # no overlaps
    a, b_, c = cues[k]; cues[k] = (a, min(b_, cues[k + 1][0] - .04), c)
def ts(t):
    ms = int(round(t * 1000)); h, ms = divmod(ms, 3600000); m, ms = divmod(ms, 60000); s, ms = divmod(ms, 1000)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"
EN = {'Hazara University': 'ہزارہ یونیورسٹی', 'glacial lake': 'گلیشیائی جھیل', 'Khari Sharif': 'کھڑی شریف', 'Gazetteer': 'گزیٹیئر',
      'UNESCO': 'یونیسکو', 'loudspeaker': 'لاؤڈ اسپیکر', 'landslide': 'لینڈ سلائیڈ', 'glacier': 'گلیشیئر', 'record': 'ریکارڈ',
      'Kunhar': 'کنہار', 'Arakan': 'اراکان'}
def ur(c):
    c = c.replace('\u00a0', ' ')
    for k, v in EN.items(): c = c.replace(k, v)
    return c
with open('Ep1_Saiful_Malook_ur.srt', 'w') as f:
    for k, (a, b_, c) in enumerate(cues, 1): f.write(f"{k}\n{ts(a)} --> {ts(b_)}\n{ur(c)}\n\n")
print(len(cues), 'cues')
