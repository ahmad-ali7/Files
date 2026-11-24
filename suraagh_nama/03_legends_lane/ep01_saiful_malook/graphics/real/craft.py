"""Realistic 'Dastan Night' frames built from REAL plates (Pixabay/Pexels footage, 1907 public-domain scans).
Day-for-night grade + physically-motivated light compositing + film grain/halation."""
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from scipy.ndimage import gaussian_filter, binary_dilation
import sys, os

R = os.path.dirname(os.path.abspath(__file__))
F = os.path.join(R, '..', 'sm', 'web', 'fonts')
OUT = os.path.join(R, 'out'); os.makedirs(OUT, exist_ok=True)
W, H = 1920, 1080
rng = np.random.default_rng(7)

def load(p, size=(W, H)):
    im = Image.open(p).convert('RGB')
    # cover-fit
    s = max(size[0] / im.width, size[1] / im.height)
    im = im.resize((round(im.width * s), round(im.height * s)), Image.LANCZOS)
    l = (im.width - size[0]) // 2; t = (im.height - size[1]) // 2
    return np.asarray(im.crop((l, t, l + size[0], t + size[1]))).astype(np.float32) / 255

def smooth(x, a, b): x = np.clip((x - a) / (b - a), 0, 1); return x * x * (3 - 2 * x)

def sky_mask(img):
    from scipy.ndimage import label, binary_fill_holes, binary_opening
    r, g, b = img[..., 0], img[..., 1], img[..., 2]
    lum = .2126 * r + .7152 * g + .0722 * b
    sat = np.max(img, 2) - np.min(img, 2)
    blue = (b - r > .10) & (lum > .38)
    white = (lum > .72) & (sat < .16)
    cand = binary_opening(blue | white, iterations=2)
    lab, n = label(cand)
    top = set(np.unique(lab[0][lab[0] > 0]))
    m = np.isin(lab, list(top))
    m = binary_fill_holes(m)
    # snow on peaks is also white & unsaturated: exclude pixels below the lowest sky row of blue in that column
    m = gaussian_filter(m.astype(np.float32), 1.8)
    return np.clip(m, 0, 1)

def day_for_night(img, ridge=None, moon=(0.78, 0.86, 1.0), expo=0.30, sky_top=(0.02, 0.035, 0.09), sky_bot=(0.07, 0.10, 0.20), keep_clouds=0.10):
    lum = (.2126 * img[..., 0] + .7152 * img[..., 1] + .0722 * img[..., 2])[..., None]
    sm = sky_mask(img)
    if ridge is not None:
        xs=np.arange(img.shape[1]); ry=np.interp(xs,[p[0] for p in ridge],[p[1] for p in ridge])
        yy0=np.arange(img.shape[0])[:,None]
        sm = sm*gaussian_filter((yy0 < ry[None,:]+6).astype(np.float32),1.5)
    sky = sm[..., None]
    # ground: desaturate 70%, underexpose, cool tint, gentle toe (keep snow as moonlit silver)
    g = img * .3 + lum * .7
    g = g * expo
    g = g * np.array(moon)
    snow = smooth(lum, .62, .9)
    g = g + snow * .22 * np.array(moon)          # snow catches moonlight
    g = np.power(np.clip(g, 0, 1), 1.12)
    # sky: night gradient + faint moonlit clouds
    yy = np.linspace(0, 1, img.shape[0])[:, None, None]
    s = np.array(sky_top) * (1 - yy) + np.array(sky_bot) * yy
    clouds = smooth(lum, .7, .98) * keep_clouds
    s = s + clouds * np.array([.75, .8, .95])
    out = g * (1 - sky) + s * sky
    return out, sky[..., 0]

def stars(out, sky, n=900, seed=3):
    r = np.random.default_rng(seed)
    ys = r.integers(0, out.shape[0], n); xs = r.integers(0, out.shape[1], n)
    st = np.zeros(out.shape[:2], np.float32)
    st[ys, xs] = r.random(n) ** 3 * 1.2
    st = gaussian_filter(st, .6) * 3
    out += (st * sky)[..., None] * np.array([.9, .93, 1.0])
    return out

def add_glow_points(out, pts, color=(1.0, .86, .58), core=1.6, halo=14, gain=1.0):
    acc = np.zeros(out.shape[:2], np.float32)
    for (x, y, a) in pts:
        xi, yi = int(x), int(y)
        if 0 <= xi < out.shape[1] and 0 <= yi < out.shape[0]:
            acc[yi, xi] += a
    c = gaussian_filter(acc, core) * core * core * 6.3
    h = gaussian_filter(acc, halo) * halo * halo * 6.3 * .04
    light = (c + h)[..., None] * np.array(color) * gain
    return out + light, (c + h)

def reflect_lights(out, glow, water_mask, horizon_y, strength=.35):
    # mirror the light map about the water line, stretch vertically (a shimmer column)
    refl = np.zeros_like(glow)
    hy = int(horizon_y)
    above = glow[:hy][::-1]
    n = min(above.shape[0], glow.shape[0] - hy)
    refl[hy:hy + n] = above[:n]
    refl = gaussian_filter(refl, (6, 1.5))
    rip = (np.sin(np.arange(glow.shape[0])[:, None] * .9) * .5 + .5)
    refl *= rip
    return out + (refl * water_mask)[..., None] * np.array([1.0, .82, .55]) * strength

def film(out, grain=.035, halation=.35, vign=.55, seed=1):
    # halation: bright areas bleed warm
    lum = out.mean(2)
    hl = gaussian_filter(np.clip(lum - .55, 0, None), 18)
    out = out + hl[..., None] * np.array([1.0, .45, .25]) * halation
    # gate weave free vignette
    yy, xx = np.mgrid[0:out.shape[0], 0:out.shape[1]]
    d = np.sqrt(((xx - out.shape[1] / 2) / (out.shape[1] / 2)) ** 2 + ((yy - out.shape[0] / 2) / (out.shape[0] / 2)) ** 2)
    out = out * (1 - vign * smooth(d, .55, 1.45))[..., None]
    # grain: luminance-weighted, slightly blurred (film-like, not digital noise)
    r = np.random.default_rng(seed)
    gr = gaussian_filter(r.standard_normal(out.shape[:2]).astype(np.float32), .7)
    out = out + gr[..., None] * grain * (.4 + .6 * np.sqrt(np.clip(out.mean(2, keepdims=True), 0, 1)))
    return np.clip(out, 0, 1)

def to_img(a): return Image.fromarray((np.clip(a, 0, 1) * 255 + .5).astype(np.uint8))

def font(name, size): return ImageFont.truetype(os.path.join(F, name), size)
