"""Assemble Ep 1: voice-over parts → clips (EDIT_PLAN.md), dissolves, character-voice FX, music + SFX, loudness.
Usage: python3 assemble.py video|audio|mux|all"""
import sys, os, json, subprocess, numpy as np
sys.path.insert(0, '.')
from anim_core import W, H, Writer
FPS = 25; D = 0.5               # dissolve length
SR = 48000
VO = '../vo/'
CL = 'clips/'
SEG = 'segs/'; os.makedirs(SEG, exist_ok=True)
AUD = '../audio/'               # music/ and sfx/ from the YouTube Audio Library
PRE = 3.0; CARD = 4.48

# ---------------- edit plan (EDIT_PLAN.md) ----------------
# ('pre', [(clip, w)]) | ('P01', [(clip, w[, 'cut'])]) | ('card', 'C_S1b')
PLAN = [
    ('pre', [('O1_lamp', 1)]),
    ('P01', [('O1_lamp', 2), ('O2_drop', 2), ('O3_naran_night', 3)]),
    ('P02', [('O3_naran_night', 1)]),
    ('P03', [('O3_naran_night', 1), ('R14_dawn', 1.2), ('R09_demon@0', 1.2), ('R02_title', 1.5)]),
    ('card', 'C_S1b'),
    ('P04', [('R15_dream', 1), ('PA1_badal_dream', 1.6), ('R03_astro', 1.2)]),
    ('P05', [('R03_astro', 1)]),
    ('P06', [('PA5_prince', 1.2), ('R16_years', 1.2), ('PA2_descent', 1.4), ('PA3_lake_apparition', 2), ('R04_fairies', .8), ('PA4_clothes', 1.2)]),
    ('P07', [('PA4_clothes', 1)]),
    ('P08', [('R17_clothes', 1)]),
    ('P09', [('R09_demon@0', 1)]),
    ('P10', [('R09_demon@8.15', 1, 'cut')]),   # cut straight onto a lightning flash
    ('P11', [('R07_flood', 1.2), ('PA6_escape', 1)]),
    ('card', 'C_S2'),
    ('P12', [('R05_page', 1.3), ('R12_naran', 1.3), ('R11_unesco', 1.4)]),
    ('P13', [('R11_unesco', 1)]),
    ('card', 'C_S3'),
    ('P14', [('R06b_map', 1)]),
    ('P15', [('V1_verse', 1)]),
    ('P16', [('R13_sar', 1), ('R06_photo1907', 1), ('R06b_map', .6)]),
    ('card', 'C_S4'),
    ('P17', [('R18_belief', 1)]),
    ('card', 'C_S5'),
    ('P18', [('R08_moraine', 1.4), ('R21_events', 1.4), ('R07_flood@0', .6)]),
    ('card', 'C_S6'),
    ('P19', [('R19_ending', 1), ('PA7_dance', 1.2)]),
    ('P20', [('V2_verse', 1)]),
    ('P21', [('R19_ending', 1), ('R20_next', .8)]),
]
VIDEO_CLIPS = {'O1_lamp', 'O2_drop', 'O3_naran_night', 'R18_belief'}   # real footage: never slower than 0.6x

def dur_of(f):
    return float(subprocess.check_output(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', f]))

def timeline():
    parts = {p['part'][:3]: p for p in json.load(open(VO + 'parts.json'))}
    segs, blocks, t = [], [], 0.0
    for name, spec in PLAN:
        if name == 'card':
            d = CARD; items = [(spec, 1)]
            blocks.append(dict(kind='card', name=spec, t=t, d=d))
        elif name == 'pre':
            d = PRE; items = spec; blocks.append(dict(kind='pre', t=t, d=d))
        else:
            p = parts[name]; d = p['e'] - p['s']; items = spec
            blocks.append(dict(kind='vo', name=p['part'], t=t, d=d, s=p['s'], e=p['e']))
        tw = sum(i[1] for i in items); tt = t
        for it in items:
            sd = d * it[1] / tw
            segs.append(dict(clip=it[0], t=tt, d=sd, cut=len(it) > 2))
            tt += sd
        t += d
    return segs, blocks, t

# ---------------- video ----------------
# every segment plays its clip from a per-clip cursor; long parts slow the clip down (stills to 0.3x, real footage to 0.6x)
# and, if still short, play it back and forth between LO and the end, so nothing visibly restarts.
LO = {'R19_ending': 4.2, 'PA7_dance': 8.2, 'R09_demon': 8.4, 'R16_years': 6.6, 'R18_belief': 2.6}
MIN_SP_VIDEO, MIN_SP_STILL = 0.6, 0.3

def tri(u, lo, hi):
    """virtual play position u (seconds) → clip time, bouncing between lo and hi after the first pass."""
    if u <= hi: return u
    L = hi - lo
    if L <= .2: return hi
    v = (u - hi) % (2 * L)
    return hi - v if v <= L else lo + (v - L)

def plan_segments(segs):
    cursor = {}
    for i, s in enumerate(segs):
        name = s['clip'].split('@')[0]; cd = dur_of(CL + name + '.mp4') - 1.0 / FPS
        need = s['d'] + (D if i < len(segs) - 1 and not segs[i + 1]['cut'] else 0)
        u0 = float(s['clip'].split('@')[1]) if '@' in s['clip'] else cursor.get(name, 0.0)
        lo = min(LO.get(name, 0.0 if name in VIDEO_CLIPS else 2.5), cd * .6)
        room = cd - u0 if u0 < cd - .5 else cd - lo          # forward room, or one bounce pass once past the end
        sp = min(1.0, max(room / need, MIN_SP_VIDEO if name in VIDEO_CLIPS else MIN_SP_STILL))
        s.update(name=name, u0=u0, sp=sp, lo=lo, hi=cd, need=need, n=int(round(need * FPS)), **{'from': u0})
        cursor[name] = u0 + need * sp
        print(f"{i:03d} {name:22s} t={s['t']:7.2f} d={s['d']:5.2f} u0 {u0:5.2f} x{sp:.2f} → u {cursor[name]:5.2f} (clip {cd:.1f})", flush=True)
    json.dump(dict(segs=segs), open(SEG + 'timeline_r.json', 'w'), indent=1)

_cache = {}
def clip_frames(name):
    if name not in _cache:
        if len(_cache) >= 2: _cache.pop(next(iter(_cache)))
        raw = subprocess.check_output(['ffmpeg', '-nostdin', '-loglevel', 'error', '-i', CL + name + '.mp4', '-vf', f'scale={W}:{H}',
                                       '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'])
        _cache[name] = np.frombuffer(raw, np.uint8).reshape(-1, H, W, 3)
    return _cache[name]

def seg_frames(s):
    fr = clip_frames(s['name']); N = len(fr)
    for j in range(s['n'] + 2):
        x = tri(s['u0'] + j / FPS * s['sp'], s['lo'], s['hi']) * FPS
        a = min(int(x), N - 1); b = min(a + 1, N - 1); w = x - int(x)
        if w < .05 or a == b: yield fr[a].astype(np.float32)
        else: yield fr[a].astype(np.float32) * (1 - w) + fr[b].astype(np.float32) * w

def blend(segs, total, out='Ep1_video.mp4'):
    nD = int(D * FPS)
    w = Writer(out, FPS); N = int(round(total * FPS)); k = 0
    prev_tail = []
    for i, s in enumerate(segs):
        g = seg_frames(s)
        end = int(round((s['t'] + s['d']) * FPS)) if i < len(segs) - 1 else N
        j = 0
        while k < end:
            f = next(g)
            if prev_tail and not s['cut'] and j < len(prev_tail):
                a = (j + 1) / (len(prev_tail) + 1); a = a * a * (3 - 2 * a)
                f = prev_tail[j] * (1 - a) + f * a
            w.add(f / 255); k += 1; j += 1
        prev_tail = [] if (i + 1 < len(segs) and segs[i + 1]['cut']) else [next(g) for _ in range(nD)]
        if i % 5 == 0: print(f'blended {i}/{len(segs)}  frame {k}/{N}', flush=True)
    w.close()

# ---------------- audio ----------------
def load_wav(f):
    a = subprocess.check_output(['ffmpeg', '-nostdin', '-loglevel', 'error', '-i', f, '-ac', '2', '-ar', str(SR), '-f', 'f32le', '-'])
    return np.frombuffer(a, np.float32).reshape(-1, 2).copy()

FX = {  # character voices, made from Ahmad's own read
    'LOUDSPEAKER': "highpass=f=450,lowpass=f=3200,acompressor=threshold=0.1:ratio=8:attack=5:release=60,volume=2.2,"
                   "aecho=0.8:0.75:230|520|900:0.45|0.28|0.15",
    'ASTROLOGER': f"asetrate={SR}*0.95,aresample={SR},atempo=1.0526,aecho=0.7:0.5:35|70:0.18|0.10",
    'FAIRY':      f"asetrate={SR}*1.05,aresample={SR},atempo=0.952,chorus=0.6:0.9:45|60:0.35|0.25:0.3|0.4:2|1.5,"
                  "aecho=0.8:0.7:90|180|300:0.32|0.22|0.12",
    'PRINCE':     "aecho=0.7:0.4:30:0.12",
    'DEMON':      f"asplit[o][d];[d]asetrate={SR}*0.74,aresample={SR},atempo=1.351,lowpass=f=2400,volume=1.6[dd];"
                  "[o]volume=0.35[oo];[oo][dd]amix=inputs=2:normalize=0,aecho=0.8:0.8:120|260|480:0.45|0.32|0.2",
    'VERSE':      "aecho=0.8:0.75:80|190|330:0.28|0.18|0.10",
}

def fx(x, chain):
    p = subprocess.run(['ffmpeg', '-nostdin', '-loglevel', 'error', '-f', 'f32le', '-ar', str(SR), '-ac', '2', '-i', '-',
                        '-filter_complex', chain, '-f', 'f32le', '-ar', str(SR), '-ac', '2', '-'], input=x.tobytes(), capture_output=True, check=True)
    y = np.frombuffer(p.stdout, np.float32).reshape(-1, 2)
    out = np.zeros_like(x); n = min(len(x), len(y)); out[:n] = y[:n]
    return out

def at(t): return int(round(t * SR))

def place(track, clip, t, gain=1.0, fade_in=.3, fade_out=.8, dur=None, loop=False):
    """put an audio clip on the track at time t (seconds), optionally trimmed/looped to dur."""
    if clip is None: return
    if dur is not None:
        n = at(dur)
        if loop and len(clip) < n: clip = np.concatenate([clip] * (n // len(clip) + 1))
        clip = clip[:n]
    c = clip.copy() * gain; n = len(c)
    fi, fo = min(at(fade_in), n // 2), min(at(fade_out), n // 2)
    if fi: c[:fi] *= np.linspace(0, 1, fi)[:, None]
    if fo: c[-fo:] *= np.linspace(1, 0, fo)[:, None]
    s = at(t); e = min(len(track), s + n); track[s:e] += c[:e - s]

def audio(blocks, total):
    vo_src = load_wav(VO + 'vo48.wav')
    vo = np.zeros((at(total) + SR, 2), np.float32)
    for b in blocks:
        if b['kind'] != 'vo': continue
        x = vo_src[at(b['s']):at(b['e'])].copy()
        role = b['name'].split('_', 1)[1]
        if role in FX:
            wet = fx(x, FX[role])
            if role == 'LOUDSPEAKER': wet = wet * 0.9
            x = wet
        n = len(x); f = min(at(.02), n // 2)
        x[:f] *= np.linspace(0, 1, f)[:, None]; x[-f:] *= np.linspace(1, 0, f)[:, None]
        s = at(b['t']); vo[s:s + n] += x
    np.save(SEG + 'vo_track.npy', vo)
    bed = np.zeros_like(vo)
    music_sfx(bed, blocks, vo)
    mix = vo + bed
    raw = SEG + 'mix_raw.wav'
    subprocess.run(['ffmpeg', '-nostdin', '-y', '-loglevel', 'error', '-f', 'f32le', '-ar', str(SR), '-ac', '2', '-i', '-', raw],
                   input=mix.astype(np.float32).tobytes(), check=True)
    # two-pass loudness to -14 LUFS, true peak -1.5 dB
    m = subprocess.run(['ffmpeg', '-nostdin', '-i', raw, '-af', 'loudnorm=I=-14:TP=-1.5:LRA=11:print_format=json', '-f', 'null', '-'],
                       capture_output=True, text=True).stderr
    j = json.loads(m[m.rfind('{'):m.rfind('}') + 1])
    af = (f"loudnorm=I=-14:TP=-1.5:LRA=11:measured_I={j['input_i']}:measured_TP={j['input_tp']}:measured_LRA={j['input_lra']}:"
          f"measured_thresh={j['input_thresh']}:offset={j['target_offset']}:linear=true")
    subprocess.run(['ffmpeg', '-nostdin', '-y', '-loglevel', 'error', '-i', raw, '-af', af, '-ar', str(SR), SEG + 'mix.wav'], check=True)
    print('audio done', j['input_i'], '→ -14 LUFS', flush=True)

def music_sfx(bed, blocks, vo):
    """filled in once the YouTube Audio Library files arrive (see AUDIO_GUIDE.md)"""
    import audio_plan
    audio_plan.build(bed, blocks, vo, load_wav, place, at, SR, AUD)

def mux(out='deliver/Ep1_Saiful_Malook_FULL_1080p.mp4'):
    subprocess.run(['ffmpeg', '-nostdin', '-y', '-loglevel', 'error', '-i', 'Ep1_video.mp4', '-i', SEG + 'mix.wav', '-map', '0:v', '-map', '1:a',
                    '-c:v', 'copy', '-c:a', 'aac', '-b:a', '256k', '-shortest', '-movflags', '+faststart', out], check=True)
    print('wrote', out, flush=True)

if __name__ == '__main__':
    segs, blocks, total = timeline()
    json.dump(dict(segs=segs, blocks=blocks, total=total), open(SEG + 'timeline.json', 'w'), indent=1)
    print(f'total {total:.1f} s, {len(segs)} segments', flush=True)
    what = sys.argv[1] if len(sys.argv) > 1 else 'all'
    if what in ('plan', 'video', 'all'): plan_segments(segs)
    if what in ('video', 'all'): blend(segs, total)
    if what in ('audio', 'all'): audio(blocks, total)
    if what in ('mux', 'all'): mux()
