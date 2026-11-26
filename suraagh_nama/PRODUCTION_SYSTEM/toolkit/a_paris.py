"""Animate the Gemini pari paintings and composite the black-background figures into the real lake.
Usage: python3 a_paris.py JOB [JOB ...]"""
import sys; sys.path.insert(0, '.')
import numpy as np
from PIL import Image, ImageFilter
from scipy.ndimage import gaussian_filter
from anim_core import W, H, cam_crop, glow, film, Writer
from produce import text_layer, comp_text, ease, big_of, png
FPS = 25
P = '../paris/'

def load_up(name, s=1.1):
    im = Image.open(P + name + '.png').convert('RGB')
    im = im.resize((int(W * s), int(H * s)), Image.LANCZOS).filter(ImageFilter.UnsharpMask(radius=1.6, percent=60, threshold=2))
    return np.asarray(im).astype(np.float32) / 255

rng = np.random.default_rng(9)
def motes(n, box, seed):
    r = np.random.default_rng(seed)
    x0, y0, x1, y1 = box
    return dict(x=r.uniform(x0, x1, n), y=r.uniform(y0, y1, n), vx=r.normal(0, 6, n), vy=r.uniform(-14, -4, n),
                ph=r.uniform(0, 6.28, n), b=.15 + .6 * r.random(n) ** 2)
def mote_pts(m, t):
    return [(x + vx * t + np.sin(t * .8 + p) * 8, y + vy * t, b * (.55 + .45 * np.sin(t * 2.2 + p)))
            for x, y, vx, vy, p, b in zip(m['x'], m['y'], m['vx'], m['vy'], m['ph'], m['b'])]

FOG = [gaussian_filter(np.random.default_rng(s).random((H // 4, W // 2)).astype(np.float32), 9) for s in (1, 2)]
def mist(t, strength=.10, band=(0, H)):
    a = np.roll(FOG[0], int(t * 6), 1); b = np.roll(FOG[1], -int(t * 4), 1)
    m = np.asarray(Image.fromarray(((a * .5 + b * .5) * 255).astype(np.uint8)).resize((W, H), Image.BILINEAR)).astype(np.float32) / 255
    m = np.clip((m - .45) * 3, 0, 1)
    yy = np.linspace(0, 1, H)[:, None]; lo, hi = band[0] / H, band[1] / H
    m = m * np.clip((yy - lo) / .08, 0, 1) * np.clip((hi - yy) / .08, 0, 1)
    return (m * strength)[..., None] * np.array([.8, .85, 1.0])

def painting(name, src, dur, z1=1.07, dx=0, dy=0, mbox=(0, 0, W, H), nm=90, mistband=None, mist_s=.10, snow=False, T=None, t0=1.0, lamp=None):
    big = load_up(src); m = motes(nm, mbox, hash(name) % 1000)
    snowp = None
    if snow:
        r = np.random.default_rng(3); snowp = dict(x=r.uniform(0, W, 500), y=r.uniform(-H, H, 500), s=r.uniform(.6, 2.2, 500), sp=r.uniform(40, 110, 500))
    w = Writer(f'clips/{name}.mp4', FPS)
    for k in range(int(dur * FPS)):
        t = k / FPS
        f = cam_crop(big, t, dur, 1.0, z1, dx, dy)
        if mistband: f = f + mist(t, mist_s, mistband)
        f, _ = glow(f, mote_pts(m, t), core=1.4, halo=10, gain=.9)
        if snow:
            ys = (snowp['y'] + snowp['sp'] * t) % H; xs = (snowp['x'] + np.sin(t + snowp['y']) * 15) % W
            f, _ = glow(f, [(x, y, .25 * s) for x, y, s in zip(xs, ys, snowp['s'])], color=(.9, .93, 1), core=1.0, halo=3, gain=1.0)
        if lamp:
            lx, ly = lamp; fl = 1 + .12 * np.sin(t * 11) + .07 * np.sin(t * 27)
            yy, xx = np.ogrid[:H, :W]; g = np.exp(-(((xx - lx) / 160) ** 2 + ((yy - ly) / 120) ** 2)) * .10 * fl
            f = f + g[..., None] * np.array([1, .7, .35])
        if T is not None: f = comp_text(f, T, t, t0, t0 + 1)
        w.add(film(f, k, grain=.035, vign=.5, halation=.3))
    w.close()

def key_black(name, lo=.05, hi=.20):
    a = np.asarray(Image.open(P + name + '.png').convert('RGB')).astype(np.float32) / 255
    lum = a.max(2)
    al = np.clip((lum - lo) / (hi - lo), 0, 1)
    rgb = np.clip(a / np.maximum(al[..., None], 1e-3), 0, 1) * (al[..., None] > 0)   # un-premultiply against black
    return rgb, al

def place(base, rgb, al, cx, by, h, opacity=1.0, tint=(.86, .9, 1.0)):
    """put a keyed figure with its bottom-centre at (cx, by), height h px"""
    sc = h / rgb.shape[0]; w_ = int(rgb.shape[1] * sc); h_ = int(h)
    R = np.asarray(Image.fromarray((rgb * 255).astype(np.uint8)).resize((w_, h_), Image.LANCZOS)).astype(np.float32) / 255
    A = np.asarray(Image.fromarray((al * 255).astype(np.uint8)).resize((w_, h_), Image.LANCZOS)).astype(np.float32) / 255 * opacity
    x0 = int(cx - w_ / 2); y0 = int(by - h_)
    xs, ys = max(0, x0), max(0, y0); xe, ye = min(W, x0 + w_), min(H, y0 + h_)
    if xe <= xs or ye <= ys: return base, None
    r = R[ys - y0:ye - y0, xs - x0:xe - x0] * np.array(tint); a = A[ys - y0:ye - y0, xs - x0:xe - x0, None]
    out = base.copy(); out[ys:ye, xs:xe] = out[ys:ye, xs:xe] * (1 - a) + r * a
    full = np.zeros((H, W), np.float32); full[ys:ye, xs:xe] = a[..., 0]
    return out, full

# ---------------- jobs ----------------
def j_pa_dream(): painting('PA1_badal_dream', 'P01_badal_portrait', 10, 1.08, 60, -20, mbox=(300, 100, 1400, 1000), nm=70,
                           mistband=(500, 1080), mist_s=.12, T=text_layer('R15_dream'), t0=2.0)
def j_pa_descent(): painting('PA2_descent', 'P03_descent', 12, 1.06, -80, 30, mbox=(500, 0, 1500, 900), nm=140)
def j_pa_clothes(): painting('PA4_clothes', 'P05_stolen_clothes', 10, 1.07, 40, 10, mbox=(800, 100, 1920, 800), nm=60)
def j_pa_prince(): painting('PA5_prince', 'P06_prince_devotion', 10, 1.06, 30, 0, mbox=(0, 0, 1, 1), nm=0, snow=True, lamp=(1030, 800))
def j_pa_escape(): painting('PA6_escape', 'P08_lovers_escape', 10, 1.05, 0, -30, mbox=(0, 0, 1, 1), nm=0, mistband=(450, 900), mist_s=.08)
def j_pa_dance(): painting('PA7_dance', 'P09_paris_dance', 12, 1.06, 20, 20, mbox=(700, 450, 1500, 800), nm=120, mistband=(380, 700), mist_s=.10,
                           T=text_layer('R19_ending'), t0=7.0)

def j_pa_lake():
    """Badal Jamal and her procession composited into the REAL night lake (drone plate, graded day-for-night)."""
    base = png('out/bg_wide_night.png')
    big = big_of(base)
    brgb, bal = key_black('P02_badal_fullfigure_black')
    grgb, gal = key_black('P04_paris_group_black')
    m = motes(120, (700, 300, 1500, 820), 5)
    dur = 12; w = Writer('clips/PA3_lake_apparition.mp4', FPS)
    yy = np.linspace(0, 1, H)[:, None]
    for k in range(dur * FPS):
        t = k / FPS
        f = cam_crop(big, t, dur, 1.0, 1.05, -30, 10)
        # procession descending from the upper left toward the water
        u = ease(t / 9.0)
        f, ga = place(f, grgb, gal, 520 + 420 * u, 330 + 360 * u, 260 + 120 * u, opacity=.55 + .3 * u)
        # Badal Jamal appears on the water, translucent, with her reflection
        op = ease((t - 2.5) / 3.0) * .92
        bx, by, bh = 1080, 800, 520 + 25 * ease(t / dur)
        f2, ba = place(f, brgb, bal, bx, by, bh, opacity=op)
        if ba is not None:
            refl = np.flipud(np.roll(f2 - f, 0, 0))  # mirror the figure about the water line
            shift = 2 * by - H
            refl = np.roll(refl, shift, 0) if shift > 0 else refl
            mask = (np.arange(H)[:, None] > by).astype(np.float32) * np.clip(1 - (np.arange(H)[:, None] - by) / 260, 0, 1)
            ripple = (np.sin(np.arange(H)[:, None] * .9 + t * 4) * .5 + .5)
            f = f2 + refl * (mask * ripple * .35)[..., None]
            f = f + gaussian_filter(ba, 25)[..., None] * np.array([.35, .32, .22]) * op   # her glow lights the air
        f, _ = glow(f, mote_pts(m, t), core=1.4, halo=10, gain=1.0)
        w.add(film(f, k, grain=.035, vign=.55, halation=.4))
    w.close()


def j_pa_portrait(): painting('PA1b_badal_portrait', 'P01_badal_portrait', 8, 1.10, -40, 30, mbox=(300, 100, 1400, 1000), nm=60,
                              mistband=(500, 1080), mist_s=.10)        # no caption: used in the Alf Laila sentence

if __name__ == '__main__':
    for j in sys.argv[1:]:
        globals()['j_' + j](); print('done', j, flush=True)
