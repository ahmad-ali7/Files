"""Render every Ep 1 scene as a clip (1920x1080, 25 fps). Usage: python3 produce.py JOB [JOB...]"""
import sys, subprocess, numpy as np
sys.path.insert(0, '.')
from PIL import Image
from scipy.ndimage import gaussian_filter
from anim_core import W, H, cam_crop, glow, film, Writer
import craft
FPS = 25
M = '../more/'

def big_of(arr, s=1.1):
    im = Image.fromarray((np.clip(arr, 0, 1) * 255).astype(np.uint8))
    return np.asarray(im.resize((int(W * s), int(H * s)), Image.LANCZOS)).astype(np.float32) / 255

def png(path):
    return np.asarray(Image.open(path).convert('RGB').resize((W, H), Image.LANCZOS)).astype(np.float32) / 255

def text_layer(name):
    t = np.asarray(Image.open(f'out/T_{name}.png').convert('RGBA')).astype(np.float32) / 255
    return t[..., :3], t[..., 3:]

def ease(x): x = min(max(x, 0), 1); return x * x * (3 - 2 * x)

def comp_text(f, T, t, t0=1.0, t1=2.0, mask=None):
    if T is None: return f
    rgb, a = T
    a = a * ease((t - t0) / (t1 - t0))
    if mask is not None: a = a * mask
    return f * (1 - a) + rgb * a

def still(name, src, dur=9, z1=1.06, dx=0, dy=0, flicker=0.0, grain=.03):
    big = big_of(png(src)); w = Writer(f'clips/{name}.mp4', FPS); r = np.random.default_rng(1)
    for k in range(int(dur * FPS)):
        t = k / FPS
        f = cam_crop(big, t, dur, 1.0, z1, dx, dy)
        if flicker: f = f * (1 + flicker * (np.sin(t * 9) * .5 + np.sin(t * 23) * .3 + r.normal(0, .3)))
        f *= ease(t / .6) * ease((dur - t) / .6) * 0 + 1   # cuts handled in the edit
        w.add(film(f, k, grain=grain, vign=.25, halation=.1))
    w.close()

def video(name, src, ss, dur, grade='warm'):
    vf = {'warm': "eq=brightness=-0.03:contrast=1.08:saturation=1.05,colorbalance=rs=.04:gs=.01:bs=-.04",
          'cool': "eq=brightness=-0.10:contrast=1.15:saturation=.75,colorbalance=rs=-.06:gs=-.02:bs=.08"}[grade]
    vf += ",scale=1920:1080:flags=lanczos,noise=alls=7:allf=t,vignette=PI/5"
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-ss', str(ss), '-t', str(dur), '-i', src, '-vf', vf, '-r', str(FPS),
                    '-an', '-c:v', 'libx264', '-crf', '16', '-pix_fmt', 'yuv420p', f'clips/{name}.mp4'], check=True)

def video_frames(src, ss, dur):
    p = subprocess.Popen(['ffmpeg', '-loglevel', 'error', '-ss', str(ss), '-t', str(dur), '-i', src, '-vf', f'scale={W}:{H},fps={FPS}',
                          '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'], stdout=subprocess.PIPE)
    while True:
        b = p.stdout.read(W * H * 3)
        if len(b) < W * H * 3: break
        yield np.frombuffer(b, np.uint8).reshape(H, W, 3).astype(np.float32) / 255

# ---------------- jobs ----------------
def j_lamp(): video('O1_lamp', M + 'v_lamp.mp4', 4, 10, 'warm')
def j_drop(): video('O2_drop', M + 'v_drop.mp4', 6, 9, 'cool')

def j_naran_night():
    w = Writer('clips/O3_naran_night.mp4', FPS); prev = None
    for k, img in enumerate(video_frames(M + 'v_naran.mp4', 2, 10)):
        sm = craft.sky_mask(img)
        prev = sm if prev is None else prev * .85 + sm * .15
        lum = img.mean(2, keepdims=True)
        g = (img * .3 + lum * .7) * .27 * np.array([.78, .86, 1.0])
        g = np.power(np.clip(g, 0, 1), 1.1)
        yy = np.linspace(0, 1, H)[:, None, None]
        s = np.array([.02, .035, .09]) * (1 - yy) + np.array([.07, .10, .20]) * yy + craft.smooth(lum, .7, .98) * .08
        f = g * (1 - prev[..., None]) + s * prev[..., None]
        w.add(film(f, k, grain=.04, vign=.55, halation=.25))
    w.close()

def j_fairies(): subprocess.run(['python3', 'a_fairies.py'], check=True)

def j_demon():
    src = open('f_demon.py').read()
    pre, rest = src.split("# ---- the demon", 1)
    demon_part = rest.split("out=ground*(1-sky[...,None])+S*sky[...,None]")[0]
    g = {}; exec(pre, g); S_storm = g['S'].copy()
    exec("# demon" + demon_part, g); S_dem = g['S']; rim = g['rim']; ground = g['ground']; sky = g['sky']
    T = text_layer('R09_demon'); dur = 11
    flashes = [(1.6, .9), (1.85, .5), (4.9, 1.0), (5.1, .6), (8.2, 1.0), (8.45, .7)]
    big_g = None
    w = Writer('clips/R09_demon.mp4', FPS)
    for k in range(dur * FPS):
        t = k / FPS
        fl = sum(a * np.exp(-((t - t0) / .07) ** 2) + a * .35 * np.exp(-((t - t0 - .12) / .18) ** 2) for t0, a in flashes)
        reveal = ease((t - 4.6) / 2.2)
        S = (S_storm * (1 - reveal) + S_dem * reveal) * (.6 + .8 * fl) + (rim * fl * reveal)[..., None] * np.array([.62, .58, .85]) * 1.2
        gr = ground * (1 + fl * .6)
        f = gr * (1 - sky[..., None]) + S * sky[..., None]
        w.add(film(comp_text(f, T, t, 7.2, 8.2), k, grain=.045, vign=.6, halation=.45))
    w.close()

def j_flood():
    sys.path.insert(0, '../flood'); import importlib.util
    src = open('../flood/flood2d.py').read().split("for k,f in")[0].replace("img.resize((1920,int(1920*H2/W2)),Image.LANCZOS)\n    t=(img.height-1080)//2;img.crop((0,t,1920,t+1080)).save(out)",
                                                                       "img=img.resize((1920,int(1920*H2/W2)),Image.LANCZOS)\n    t=(img.height-1080)//2;return np.asarray(img.crop((0,t,1920,t+1080))).astype(np.float32)/255")
    import os; cwd = os.getcwd(); os.chdir('../flood'); g = {}; exec(src, g); os.chdir(cwd)
    T = text_layer('R07_flood'); dur = 13; w = Writer('clips/R07_flood.mp4', FPS)
    for k in range(dur * FPS):
        t = k / FPS
        front = ease((t - 1.0) / 10.0)
        os.chdir('../flood'); f = g['frame'](front, out=None); os.chdir(cwd)
        w.add(film(comp_text(f, T, t, .5, 1.5), k, grain=.02, vign=.35, halation=.1))
    w.close()

def j_belief():
    T = text_layer('R18_belief'); w = Writer('clips/R18_belief.mp4', FPS); r = np.random.default_rng(4)
    pts0 = np.stack([r.integers(0, W, 160), r.integers(700, 1000, 160)], 1); ph = r.random(160) * 6.28; br = .2 + .6 * r.random(160)
    for k, img in enumerate(video_frames(M + 'fog3138755.mp4', 1, 11)):
        t = k / FPS; lum = img.mean(2, keepdims=True)
        f = (img * .3 + lum * .7) * np.array([.5, .6, .85]) * .68
        fog = craft.smooth(lum[..., 0], .35, .65)
        pts = [(x + np.sin(t * .4 + p) * 14, y + np.cos(t * .3 + p) * 6, b * fog[min(int(y), H - 1), min(int(x), W - 1)] * (.6 + .4 * np.sin(t * 2 + p)))
               for (x, y), p, b in zip(pts0, ph, br)]
        f, gl = glow(f, pts, core=2.6, halo=26, gain=1.6)
        w.add(film(comp_text(f, T, t, 1.5, 2.5), k, grain=.04, vign=.55, halation=.4))
    w.close()

def j_years():
    s = craft.np.asarray(Image.open(M + 'pex34948624.jpg').convert('RGB')).astype(np.float32) / 255
    def c16(path, y0f, mul=1.0):
        im = Image.open(path).convert('RGB'); w_ = im.width; h_ = int(w_ * 9 / 16); y0 = int((im.height - h_) * y0f)
        return np.asarray(im.crop((0, y0, w_, y0 + h_)).resize((int(W * 1.1), int(H * 1.1)), Image.LANCZOS)).astype(np.float32) / 255 * mul
    A = c16(M + 'pex34948624.jpg', .55); B = c16(M + 'pex29717097.jpg', .80, .85)
    T = text_layer('R16_years'); dur = 11; w = Writer('clips/R16_years.mp4', FPS)
    left = (np.arange(W) < W / 2).astype(np.float32)[None, :, None]
    for k in range(dur * FPS):
        t = k / FPS; m = ease((t - 4.5) / 2.0)
        f = cam_crop(A, t, dur, 1.0, 1.05) * (1 - m) + cam_crop(B, t, dur, 1.0, 1.05) * m
        rgb, a = T; top = np.zeros((H, 1, 1), np.float32); top[:300] = 1
        a2 = a * (top + (1 - top) * (left * (1 - m) + (1 - left) * m))
        f = comp_text(f, (rgb, a2), t, .8, 1.8)
        w.add(film(f, k, grain=.025, vign=.4, halation=.12))
    w.close()

def overlay_still(name, bg, tname, dur=10, z1=1.06, dx=0, dy=0, t0=1.0):
    big = big_of(png(bg)); T = text_layer(tname); w = Writer(f'clips/{name}.mp4', FPS)
    for k in range(dur * FPS):
        t = k / FPS; f = cam_crop(big, t, dur, 1.0, z1, dx, dy)
        w.add(film(comp_text(f, T, t, t0, t0 + 1), k, grain=.035, vign=.35, halation=.2))
    w.close()

def j_clothes(): overlay_still('R17_clothes', 'out/bg_clothes.png', 'R17_clothes', 10, 1.07, 40, 20)
def j_dream(): overlay_still('R15_dream', 'out/bg_dream.png', 'R15_dream', 10, 1.08, 30, -10)
def j_ending(): overlay_still('R19_ending', 'out/bg_ending.png', 'R19_ending', 12, 1.05, 0, -20, 3.0)

STILLS = {'R02_title': 8, 'R03_astro': 9, 'R05_page': 9, 'R06_photo1907': 9, 'R06b_map': 12, 'R08_moraine': 10, 'R11_unesco': 9,
          'R12_naran': 10, 'R13_sar': 7, 'R14_dawn': 8, 'R20_next': 8, 'C_S1': 4.5, 'C_S1b': 4.5, 'C_S2': 4.5, 'C_S3': 4.5,
          'C_S4': 4.5, 'C_S5': 4.5, 'C_S6': 4.5}
def j_stills():
    for n, d in STILLS.items():
        still(n, f'out/{n}.png', d, 1.05, flicker=.025 if n.startswith('C_') or n in ('R03_astro', 'R20_next', 'R05_page') else 0)
        print('still', n, flush=True)

if __name__ == '__main__':
    for j in sys.argv[1:]:
        globals()['j_' + j](); print('done', j, flush=True)
