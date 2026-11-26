"""Fix the two Punjabi verses (ASR skipped them) and put every boundary in the pause before the part's first word."""
import json
asr = json.load(open('asr.json'))
words = [(s, e, w) for seg in asr for s, e, w in seg['w']]
end = asr[-1]['e'] + 0.6
raw = {}
for line in open('align.out'):
    p = line.split()
    if len(p) >= 2 and p[0].startswith('P'): raw[p[0]] = None if p[1] == 'None' else float(p[1])
def seg_end(t):   # end of the last word of the ASR segment that starts at ~t
    seg = min(asr, key=lambda s: abs(s['s'] - t)); return seg['w'][-1][1]
raw['P15_VERSE'] = seg_end(287.7)          # after "...ایک مصرع ہے:"
raw['P16_NARRATOR'] = 296.1
raw['P20_VERSE'] = seg_end(435.9)          # after "...محمد بخش کہتے ہیں:"
raw['P21_NARRATOR'] = 447.3
names = list(raw)
def snap(t, verse_start=False):
    if verse_start: return t + .12
    prev = max((e for s, e, w in words if e <= t + .01), default=0)
    return max(prev + .05, t - .25) if prev < t else t
out = []
for i, n in enumerate(names):
    s = 0.0 if i == 0 else snap(raw[n], n.endswith('VERSE'))
    out.append(dict(part=n, s=round(s, 3)))
for i in range(len(out)): out[i]['e'] = out[i + 1]['s'] if i + 1 < len(out) else round(end, 3)
for o in out: print(f"{o['part']:17s} {o['s']:8.2f} {o['e']:8.2f} {o['e']-o['s']:6.2f}")
json.dump(out, open('parts.json', 'w'), indent=1)
# snap each boundary to the quietest 60 ms inside [t-0.35, t+0.15] (whisper's word times run together on fast lines)
import wave, numpy as np
wf = wave.open('vo16.wav'); x = np.frombuffer(wf.readframes(wf.getnframes()), np.int16).astype(np.float32); sr = wf.getframerate()
hop = sr // 100; rms = np.sqrt(np.convolve(x[:len(x)//hop*hop].reshape(-1, hop).__pow__(2).mean(1), np.ones(6) / 6, 'same'))
for i in range(1, len(out)):
    t = out[i]['s']; a, b = int((t - .35) * 100), int((t + .15) * 100)
    k = a + int(np.argmin(rms[a:b])); out[i]['s'] = round(k / 100, 3); out[i - 1]['e'] = out[i]['s']
print('--- snapped'); [print(f"{o['part']:17s} {o['s']:8.2f} {o['e']:8.2f} {o['e']-o['s']:6.2f}  rms {rms[int(o['s']*100)]:.0f}") for o in out]
json.dump(out, open('parts.json', 'w'), indent=1)
