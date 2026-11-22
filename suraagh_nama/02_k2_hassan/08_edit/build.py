#!/usr/bin/env python3
"""Build the full K2 Hassan episode from timeline.json.

Usage:  python3 08_edit/build.py            (run from the episode folder or anywhere)
Output: 09_export/K2_Hassan_<version>.mp4, re-timed captions, chapters and an edit report.

Missing Earth Studio / news clips become labelled placeholders; missing music roles
get quiet synthesized interim pads. Drop the real files in and run again.
"""
import json, math, os, re, subprocess, sys, shutil, wave
import numpy as np

EP = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
J = lambda *p: os.path.join(EP, *p)
FPS, W, H, SR = 30, 1920, 1080, 48000
VERSION = sys.argv[1] if len(sys.argv) > 1 else "v1"
WORK = J("08_edit", "_work"); os.makedirs(WORK, exist_ok=True)
os.makedirs(J("09_export"), exist_ok=True)

def run(cmd, **kw):
    r = subprocess.run(cmd, capture_output=True, text=True, **kw)
    if r.returncode:
        sys.exit("FAILED: " + " ".join(cmd[:12]) + "\n" + r.stderr[-1500:])
    return r.stdout

def dur(path):
    return float(run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", path]).strip())

TL = json.load(open(J("08_edit", "timeline.json")))
ROWS = [l.split("\t") for l in open(J("01_voiceover", "cues_ur_en_hi.tsv"), encoding="utf-8").read().strip().split("\n")]
T = json.load(open(J("01_voiceover", "cue_speech_times.json")))      # [start, end, quality] per cue, VO seconds
NC = len(T)

# ---------- time map: voice-over time -> final video time ----------
INTRO = TL["intro"]["disclaimer_len"] + TL["intro"]["black_after"]
GAPS = []
for g in TL["gaps"]:
    a = g["after_cue"]
    cut = (T[a][1] + T[a + 1][0]) / 2 if a + 1 < NC else T[a][1] + 0.25
    GAPS.append(dict(g, cut=cut))
GAPS.sort(key=lambda g: g["cut"])
def F(v):            # final time of VO time v (gaps at cut <= v are already inserted)
    return INTRO + v + sum(g["len"] for g in GAPS if g["cut"] <= v)
def gap_start(g):    # final time where the gap's silence begins
    return INTRO + g["cut"] + sum(x["len"] for x in GAPS if x["cut"] < g["cut"])
cue_start = lambda i: 0.0 if i == 0 else T[i][0] - 0.15

# ---------- sources ----------
SCENES = {re.match(r"(S\d+[ab]?)_", f).group(1): J("04_scenes", f) for f in os.listdir(J("04_scenes")) if f.endswith(".mp4")}
FONT = J("08_edit", "fonts", "Inter600.ttf"); FONT2 = J("08_edit", "fonts", "Inter400.ttf")
MISSING = []
def placeholder(kind, name):
    p = os.path.join(WORK, f"ph_{kind}_{name}.mp4")
    if not os.path.exists(p):
        label = {"GES": "GOOGLE EARTH STUDIO", "NEWS": "NEWS FOOTAGE (credit the channel)"}[kind]
        folder = {"GES": "05_earth_studio", "NEWS": "10_news_footage"}[kind]
        esc = lambda s: s.replace(":", r"\:").replace("'", "")
        vf = (f"drawtext=fontfile={FONT}:text='{esc('PLACEHOLDER  ·  ' + label)}':fontcolor=0xF2B35B:fontsize=40:x=(w-text_w)/2:y=h/2-70,"
              f"drawtext=fontfile={FONT}:text='{esc(name)}':fontcolor=white:fontsize=72:x=(w-text_w)/2:y=h/2,"
              f"drawtext=fontfile={FONT2}:text='{esc('drop ' + folder + '/' + name + '.mp4 and run build.py again')}':fontcolor=0x9aa3b5:fontsize=30:x=(w-text_w)/2:y=h/2+110")
        run(["ffmpeg", "-y", "-v", "error", "-f", "lavfi", "-i", f"color=c=0x0b1020:s={W}x{H}:r={FPS}:d=60", "-vf", vf,
             "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", "-pix_fmt", "yuv420p", p])
    return p
def resolve(src):
    if src in SCENES: return SCENES[src]
    if src == "MAP": return J("03_motion_graphics", "map.mp4")
    if src.startswith("MG:"):
        n = src[3:]; p = J("03_motion_graphics", n + (".mov" if n.endswith("_alpha") else ".mp4"))
        if not os.path.exists(p): sys.exit("missing motion graphic " + p)
        return p
    kind, name = src.split(":")
    folder = {"GES": "05_earth_studio", "NEWS": "10_news_footage"}[kind]
    for ext in (".mp4", ".mov", ".mkv", ".webm"):
        p = J(folder, name + ext)
        if os.path.exists(p): return p
    MISSING.append(f"{folder}/{name}.mp4"); return placeholder(kind, name)
DURS = {}
def sdur(p):
    if p not in DURS: DURS[p] = dur(p)
    return DURS[p]

# ---------- visual timeline (final seconds) ----------
segs = TL["segments"]
vo_len = dur(J("01_voiceover", "k2_hassan_voiceover.m4a"))
pieces = [dict(t0=0.0, t1=TL["intro"]["disclaimer_len"], src=TL["intro"]["disclaimer"], inn=0.0, note="disclaimer"),
          dict(t0=TL["intro"]["disclaimer_len"], t1=INTRO, src="BLACK", inn=0.0, note="black")]
for k, s in enumerate(segs):
    t0 = F(cue_start(s["cue"])) if s["cue"] else INTRO
    if k + 1 < len(segs): t1 = F(cue_start(segs[k + 1]["cue"]))
    else: t1 = max(t0 + 12.0, F(vo_len) + 0.5)
    pieces.append(dict(t0=t0, t1=t1, src=s["src"], inn=s["in"], note=s.get("note", ""), cue=s["cue"]))
# paint chapter cards over the timeline
for g in GAPS:
    if "card" not in g: continue
    c0 = gap_start(g) + g.get("card_at", 0.0); cp = resolve(g["card"]); c1 = min(c0 + sdur(cp), gap_start(g) + g["len"])
    out = []; added = False
    for p in pieces:
        if p["t1"] <= c0 or p["t0"] >= c1: out.append(p); continue
        if p["t0"] < c0: out.append(dict(p, t1=c0))
        if not added: out.append(dict(t0=c0, t1=c1, src=g["card"], inn=0.0, note=g["why"])); added = True
        if p["t1"] > c1: out.append(dict(p, t0=c1, inn=p["inn"] + (c1 - p["t0"]), cont=True))
    pieces = sorted(out, key=lambda p: p["t0"])
TOTAL = pieces[-1]["t1"]

# overlays: AI tag at the start of reconstruction segments, plus the counter
OVER = []
for p in pieces:
    if p["src"] in TL["ai_tag_sources"] and not p.get("cont") and p["t1"] - p["t0"] >= 4.0:
        OVER.append(dict(src=J("03_motion_graphics", "aitag_alpha.mov"), t0=p["t0"] + 0.3, len=min(8.0, p["t1"] - p["t0"] - 0.3)))
for o in TL["overlays"]:
    pth = resolve(o["src"]); t0 = F(cue_start(o["at_cue"])) + o.get("offset", 0.0)
    OVER.append(dict(src=pth, t0=t0, len=sdur(pth)))

# ---------- render pieces ----------
print(f"timeline: {len(pieces)} pieces, {int(TOTAL//60)}:{TOTAL%60:04.1f}")
fr = lambda t: int(round(t * FPS))
listfile = os.path.join(WORK, "concat.txt"); lines = []
for i, p in enumerate(pieces):
    nfr = fr(p["t1"]) - fr(p["t0"])
    if nfr <= 0: continue
    out = os.path.join(WORK, f"p{i:03d}.mp4"); lines.append(f"file '{out}'")
    D = nfr / FPS; P0 = fr(p["t0"]) / FPS
    cmd = ["ffmpeg", "-y", "-v", "error"]
    if p["src"] == "BLACK":
        cmd += ["-f", "lavfi", "-i", f"color=c=black:s={W}x{H}:r={FPS}"]
    else:
        src = resolve(p["src"]); sd = sdur(src)
        # clips that fade out at their end: never hold a faded frame, hold the last fully visible one
        fades = (p["src"].startswith("MG:") and p["src"] != "MG:endcard") or p["src"] in ("S27", "MAP")
        usable = sd - (1.0 if fades else 0.05)
        inn = min(p["inn"], max(0.0, usable - 0.2))
        cmd += ["-ss", f"{inn:.3f}", "-t", f"{max(0.2, usable - inn):.3f}", "-i", src]
    ovs = [o for o in OVER if o["t0"] < P0 + D and o["t0"] + o["len"] > P0]
    for o in ovs:
        cmd += ["-ss", f"{max(0.0, P0 - o['t0']):.3f}", "-itsoffset", f"{max(0.0, o['t0'] - P0):.3f}", "-t", f"{o['len']:.3f}", "-i", o["src"]]
    fc = f"[0:v]scale={W}:{H}:force_original_aspect_ratio=decrease,pad={W}:{H}:(ow-iw)/2:(oh-ih)/2,fps={FPS},setsar=1,tpad=stop_mode=clone:stop_duration={D + 1:.2f}[b0]"
    for k, o in enumerate(ovs):
        fc += f";[{k+1}:v]fps={FPS},format=yuva420p[o{k}];[b{k}][o{k}]overlay=eof_action=pass:format=auto[b{k+1}]"
    fc += f";[b{len(ovs)}]format=yuv420p[v]"
    cmd += ["-filter_complex", fc, "-map", "[v]", "-frames:v", str(nfr), "-an", "-c:v", "libx264", "-preset", "veryfast", "-crf", "17", out]
    run(cmd)
    sys.stdout.write(f"\r  rendered {i+1}/{len(pieces)}"); sys.stdout.flush()
print()
open(listfile, "w").write("\n".join(lines) + "\n")
BASE = os.path.join(WORK, "base.mp4")
run(["ffmpeg", "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", listfile, "-c", "copy", BASE])
TOTAL = dur(BASE)

# ---------- audio ----------
N = int(TOTAL * SR) + SR
rng = np.random.default_rng(7)
def load_audio(path):
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", path, "-ac", "2", "-ar", str(SR), "-f", "f32le", "-"], capture_output=True).stdout
    return np.frombuffer(raw, np.float32).reshape(-1, 2).copy()
def shaped_noise(n, lo, hi, tilt=-1.0, stereo=True):
    out = []
    for _ in range(2 if stereo else 1):
        x = rng.standard_normal(n).astype(np.float32); X = np.fft.rfft(x); f = np.fft.rfftfreq(n, 1 / SR)
        g = ((f > lo) & (f < hi)) * np.power(np.maximum(f, 20), tilt / 2); X *= g; y = np.fft.irfft(X, n).astype(np.float32)
        out.append(y / (np.std(y) + 1e-9))
    return np.stack(out, 1) if stereo else out[0]
def env_ad(n, a, d):
    t = np.arange(n) / SR; return np.minimum(1, t / max(a, 1e-4)) * np.exp(-np.maximum(0, t - a) / d)
def fade(x, fi=1.5, fo=2.0):
    n = len(x); a = np.ones(n, np.float32); i = min(n, int(fi * SR)); o = min(n, int(fo * SR))
    if i: a[:i] = np.linspace(0, 1, i)
    if o: a[-o:] = np.minimum(a[-o:], np.linspace(1, 0, o))
    return x * a[:, None]
def put(buf, x, t, gain=1.0):
    i = int(t * SR); j = min(len(buf), i + len(x))
    if j > i >= 0: buf[i:j] += x[:j - i] * gain
db = lambda d: 10 ** (d / 20)

# voice-over with inserted gaps
vo = load_audio(J("01_voiceover", "k2_hassan_voiceover.m4a")); vo /= (np.max(np.abs(vo)) + 1e-9); vo *= db(-1.5)
VO = np.zeros((N, 2), np.float32)
cuts = [0.0] + [g["cut"] for g in GAPS] + [len(vo) / SR]
for a, b in zip(cuts[:-1], cuts[1:]):
    chunk = vo[int(a * SR):int(b * SR)]
    if len(chunk): put(VO, fade(chunk, 0.01, 0.01), F(a + 1e-6) if a > 0 else INTRO)
vo_rms = np.sqrt(np.mean(vo[np.abs(vo[:, 0]) > 0.02] ** 2))
# VO activity envelope for ducking (100 ms windows)
def movavg(x, w):
    c = np.cumsum(np.concatenate([[0.0], x])); y = (c[w:] - c[:-w]) / w
    return np.concatenate([np.full(w // 2, y[0]), y, np.full(len(x) - len(y) - w // 2, y[-1])]).astype(np.float32)
act = np.sqrt(movavg(VO[:, 0].astype(np.float64) ** 2, SR // 10))
act = movavg((act > vo_rms * 0.25).astype(np.float64), SR // 2)
duck = 1 - 0.5 * np.clip(act, 0, 1)                              # up to -6 dB under the voice

# ---- sound effects (synthesized, original) ----
SFX = np.zeros((N, 2), np.float32)
def wind(t0, t1, level=-30):
    n = int((t1 - t0) * SR)
    if n <= 0: return
    x = shaped_noise(n, 60, 2500, -1.3); tt = np.arange(n) / SR
    gust = 0.55 + 0.25 * np.sin(2 * np.pi * 0.07 * tt) + 0.2 * np.sin(2 * np.pi * 0.19 * tt + 1.3)
    put(SFX, fade(x * gust[:, None], 2.0, 2.5), t0, db(level))
def steps(t0, t1, level=-22):
    t = t0; k = 0
    while t < t1:
        n = int(0.16 * SR); c = shaped_noise(n, 900, 6000, 0.0) * env_ad(n, 0.004, 0.05)[:, None]
        c += shaped_noise(n, 150, 900, -1.0) * env_ad(n, 0.002, 0.03)[:, None] * 0.6
        put(SFX, c, t, db(level - 3 * (k % 2))); t += 0.82 + 0.06 * math.sin(k); k += 1
def impact(t, level=-8):
    n = int(1.6 * SR); tt = np.arange(n) / SR; f = 70 * np.exp(-tt * 1.2) + 30
    s = np.sin(2 * np.pi * np.cumsum(f) / SR) * env_ad(n, 0.003, 0.35)
    x = np.stack([s, s], 1) + shaped_noise(n, 40, 600, -1.0) * env_ad(n, 0.002, 0.12)[:, None] * 0.5
    put(SFX, x.astype(np.float32), t, db(level))
def heartbeat(t0, secs=12.0, level=-12):
    t = t0; bpm = 66.0
    while t < t0 + secs:
        g = db(level) * (1 - 0.6 * (t - t0) / secs)
        for off, amp in ((0, 1.0), (0.26, 0.65)):
            n = int(0.25 * SR); tt = np.arange(n) / SR; s = np.sin(2 * np.pi * 48 * tt) * env_ad(n, 0.006, 0.06) * amp
            put(SFX, np.stack([s, s], 1).astype(np.float32), t + off, g)
        bpm = max(44.0, bpm - 1.6); t += 60 / bpm
def creak(t, level=-26):
    n = int(0.5 * SR); x = shaped_noise(n, 250, 1400, -0.5); tt = np.arange(n) / SR
    x *= (0.5 + 0.5 * np.sin(2 * np.pi * 23 * tt))[:, None] * env_ad(n, 0.08, 0.18)[:, None]; put(SFX, x, t, db(level))
def breathing(t0, t1, level=-28):
    t = t0
    while t < t1 - 3:
        for a, d, g in ((1.1, 0.2, 1.0), (0.2, 1.1, 0.8)):
            n = int((a + d + 0.3) * SR); e = env_ad(n, a, d * 0.6); x = shaped_noise(n, 300, 2600, -0.6) * e[:, None]
            put(SFX, x, t, db(level) * g); t += a + d + 0.2
        t += 0.9
def river(t0, t1, level=-34):
    n = int((t1 - t0) * SR)
    if n > 0: put(SFX, fade(shaped_noise(n, 120, 1800, -0.8), 2, 2), t0, db(level))
def helicopter(t0, t1, level=-30):
    n = int((t1 - t0) * SR); tt = np.arange(n) / SR
    x = shaped_noise(n, 40, 500, -1.0) * (0.35 + 0.65 * (np.sin(2 * np.pi * 15.5 * tt) > 0.2))[:, None]
    put(SFX, fade(x, 3, 3), t0, db(level))
fc = lambda i: F(cue_start(i))
gapF = {g["after_cue"]: (gap_start(g), gap_start(g) + g["len"]) for g in GAPS}
wind(INTRO - 0.5, fc(22), -27); [creak(INTRO + x) for x in (2.5, 9.0, 16.5)]
steps(fc(9) - 0.8, gapF[9][1] + 0.3); steps(gapF[91][0] - 0.6, gapF[91][1] + 0.3)
wind(fc(48), fc(92), -29); impact(fc(53) + 1.1); heartbeat(fc(53) + 1.9, 13); creak(fc(53) + 1.6, -20)
breathing(fc(73), fc(77)); wind(fc(111), fc(115), -27); wind(fc(137), fc(138) + 0.5, -27)
river(fc(29), fc(34)); river(fc(115), fc(117)); river(fc(150), fc(154))
helicopter(fc(148), fc(150)); wind(fc(169), gapF[171][1] + 0.5, -26)

# ---- music: real tracks from 06_music, or interim synthesized pads ----
MUS = np.zeros((N, 2), np.float32); MUSIC_LOG = []
def synth_pad(role, n):
    tt = np.arange(n) / SR
    chords = {"1_main_theme": [110, 164.8, 261.6, 329.6, 493.9], "2_dark_drone": [41.2, 55.0, 82.4],
              "3_warm_strings": [174.6, 220.0, 261.6, 349.2, 440.0], "4_cold_bed": [880.0, 932.3, 1318.5],
              "5_build": [98.0, 146.8, 196.0, 246.9, 293.7]}[role]
    s = np.zeros(n, np.float32)
    for k, f in enumerate(chords):
        lfo = 1 + 0.002 * np.sin(2 * np.pi * (0.11 + 0.03 * k) * tt)
        for h, a in ((1, 1.0), (2, 0.35), (3, 0.15)):
            s += a * np.sin(2 * np.pi * f * h * np.cumsum(lfo) / SR).astype(np.float32) / (k + 2)
    if role == "2_dark_drone": s += shaped_noise(n, 30, 300, -1.5, stereo=False) * 0.15
    if role == "5_build": s *= np.linspace(0.45, 1.0, n).astype(np.float32); s *= (1 + 0.25 * (np.sin(2 * np.pi * 1.0 * tt) > 0.92))
    s *= 0.75 + 0.25 * np.sin(2 * np.pi * 0.05 * tt)
    return np.stack([s, np.roll(s, 240)], 1)
TRACKS = {}
for f in sorted(os.listdir(J("06_music"))):
    m = re.match(r"([1-5]_[a-z_]+?)(?:__|\.|_-)", f)
    if m and os.path.splitext(f)[1].lower() in (".mp3", ".wav", ".m4a", ".aac", ".flac", ".ogg"):
        role = next((r for r in TL["music_roles"] if f.startswith(r)), None)
        if role and role not in TRACKS: TRACKS[role] = load_audio(J("06_music", f)); MUSIC_LOG.append(f"{role}: {f}")
target = vo_rms * db(-17)
for role, ranges in TL["music_roles"].items():
    cursor = 0
    for a, b in ranges:
        t0, t1 = F(cue_start(a)) - 0.3, F(cue_start(b)) - 0.2
        n = int((t1 - t0) * SR)
        if n <= 0: continue
        if role in TRACKS:
            tr = TRACKS[role]; start = 0 if role == "1_main_theme" else cursor
            idx = (np.arange(n) + start) % len(tr); x = tr[idx]; cursor = (start + n) % len(tr)
        else:
            x = synth_pad(role, n)
        rms = np.sqrt(np.mean(x ** 2)) + 1e-9; lvl = target / rms * (1.0 if role in TRACKS else db(-4))
        put(MUS, fade(x, 1.5, 2.2) * lvl, t0)
    if role not in TRACKS: MUSIC_LOG.append(f"{role}: INTERIM synthesized pad (add 06_music/{role}__<title>.mp3)")
MUS *= duck[:, None]

mix = VO + SFX * (0.6 + 0.4 * duck[:, None]) + MUS
peak = np.max(np.abs(mix)); mix = np.tanh(mix / max(peak, 1e-9) * 1.2) * 0.89
wav = os.path.join(WORK, "mix.wav")
with wave.open(wav, "wb") as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes((np.clip(mix[:int(TOTAL * SR)], -1, 1) * 32767).astype("<i2").tobytes())
OUT = J("09_export", f"K2_Hassan_{VERSION}.mp4")
run(["ffmpeg", "-y", "-v", "error", "-i", BASE, "-i", wav, "-map", "0:v", "-map", "1:a", "-c:v", "copy",
     "-af", "loudnorm=I=-14:TP=-1.5:LRA=11", "-ar", "48000", "-c:a", "aac", "-b:a", "256k", "-movflags", "+faststart", "-shortest", OUT])

# ---------- captions re-timed to the final cut ----------
os.makedirs(J("02_captions", "final"), exist_ok=True)
def parse_srt(p):
    blocks = open(p, encoding="utf-8").read().strip().split("\n\n"); out = []
    for b in blocks:
        ls = b.split("\n"); a, c = ls[1].split(" --> ")
        ts = lambda s: int(s[:2]) * 3600 + int(s[3:5]) * 60 + int(s[6:8]) + int(s[9:12]) / 1000
        out.append((ts(a), ts(c), "\n".join(ls[2:])))
    return out
fmt = lambda x: "%02d:%02d:%02d,%03d" % (int(x // 3600), int(x // 60 % 60), int(x % 60), int(round(x * 1000)) % 1000)
for lang in ("ur", "hi", "en"):
    cs = parse_srt(J("02_captions", f"K2_Hassan_{lang}.srt")); res = []
    for i, (a, b, txt) in enumerate(cs):
        fa = F(a); fb = fa + (b - a)
        if i + 1 < len(cs): fb = min(fb, F(cs[i + 1][0]) - 0.02)
        res.append(f"{i+1}\n{fmt(fa)} --> {fmt(fb)}\n{txt}\n")
    open(J("02_captions", "final", f"K2_Hassan_{lang}_{VERSION}.srt"), "w", encoding="utf-8").write("\n".join(res))

# ---------- chapters + report ----------
mmss = lambda x: f"{int(x//60)}:{int(x%60):02d}"
ch = {g["card"]: gap_start(g) + g.get("card_at", 0) for g in GAPS if "card" in g}
chapters = [("0:00", "Ek raat, ek qatar | ایک رات، ایک قطار"), (mmss(ch["MG:ch1"]), "Pehla hissa: Rassi | رسّی"),
            (mmss(ch["MG:ch2"]), "Doosra hissa: Ajnabi | اجنبی"), (mmss(ch["MG:ch3"]), "Teesra hissa: Wapsi | واپسی"),
            (mmss(ch["MG:ch4"]), "Summit ki tasveer | Summit کی تصویر")]
open(J("09_export", "chapters.txt"), "w", encoding="utf-8").write("\n".join(f"{a} {b}" for a, b in chapters) + "\n")
rep = [f"# Edit report {VERSION}", f"Length {mmss(TOTAL)} ({TOTAL:.1f} s)", "", "## Missing (placeholders in this cut)"]
rep += [f"- {m}" for m in sorted(set(MISSING))] or ["- none"]
rep += ["", "## Music", *[f"- {m}" for m in MUSIC_LOG], "", "## Chapters", *[f"- {a} {b}" for a, b in chapters], "", "## Timeline", "| time | visual | voice-over cue | note |", "|---|---|---|---|"]
for p in pieces:
    cue = ROWS[p["cue"]][0][:40] if "cue" in p else ""
    rep.append(f"| {mmss(p['t0'])} | {p['src']} | {cue} | {p.get('note','')} |")
open(J("09_export", f"edit_report_{VERSION}.md"), "w", encoding="utf-8").write("\n".join(rep) + "\n")
print("done:", OUT, mmss(TOTAL)); print("missing:", sorted(set(MISSING))); print("\n".join(MUSIC_LOG))
