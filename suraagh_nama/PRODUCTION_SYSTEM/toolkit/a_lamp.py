"""Opening diya, alive: the flame sways, stretches and flickers, its light breathes on the clay lamp and the dark,
heat shimmers above the tip, and an occasional spark lifts off. Built on the real Pexels diya footage."""
import sys; sys.path.insert(0, '.')
import numpy as np
from scipy.ndimage import map_coordinates, gaussian_filter
from anim_core import W, H, glow, film, Writer
from produce import video_frames
FPS = 25; DUR = 14.0
X0, X1, Y0, Y1 = 1040, 1330, 150, 640          # flame box (tip ~ (1155,270), wick ~ (1180,600))
BX, BY = 1180, 595                              # flame base
rng = np.random.default_rng(7)

def smooth_noise(n, sigma, seed):
    r = np.random.default_rng(seed).normal(0, 1, n + 200)
    s = gaussian_filter(r, sigma)[100:100 + n]
    return s / (np.abs(s).max() + 1e-9)
N = int(DUR * FPS) + 2
sway = smooth_noise(N, 6, 1) * .8 + smooth_noise(N, 2.2, 2) * .35        # slow lean + quicker wobble
stretch = smooth_noise(N, 3, 3) * .7 + smooth_noise(N, 1.2, 4) * .3
flick = smooth_noise(N, 1.6, 5) * .6 + smooth_noise(N, .8, 6) * .4      # 3–10 Hz flicker
breath = smooth_noise(N, 10, 8)                                          # slow breathing of the light

yy, xx = np.mgrid[Y0:Y1, X0:X1].astype(np.float32)
up = np.clip((BY - yy) / (BY - 230), 0, 1)                               # 0 at base → 1 at tip
yy_f, xx_f = np.mgrid[0:H, 0:W].astype(np.float32)
fall = np.exp(-(((xx_f - BX) / 700) ** 2 + ((yy_f - (BY - 120)) / 520) ** 2))[..., None]
SY0, SY1, SX0, SX1 = 40, 300, 1060, 1300                                 # shimmer box above the tip
sy, sx = np.mgrid[SY0:SY1, SX0:SX1].astype(np.float32)
sfade = (np.clip((sy - SY0) / 120, 0, 1) * np.clip((SY1 - sy) / 60, 0, 1) * np.exp(-((sx - 1160) / 70) ** 2))

sparks = []
w = Writer('clips/O1_lamp.mp4', FPS)
for k, img in enumerate(video_frames('../more/v_lamp.mp4', 4, DUR)):
    t = k / FPS
    f = img.copy()
    # 1) flame motion: sway grows toward the tip, ripples travel up, height breathes
    h = 1 + .07 * stretch[k]
    dx = (sway[k] * 16 + np.sin(yy * .045 - t * 9.0) * 3.2 + np.sin(yy * .021 - t * 5.3) * 2.0) * up ** 1.5
    src_y = BY + (yy - BY) / h
    src_x = xx - dx
    for c in range(3):
        f[Y0:Y1, X0:X1, c] = map_coordinates(img[..., c], [src_y, src_x], order=1, mode='nearest')
    # 2) flicker and glow
    fb = 1 + .10 * flick[k]
    core = np.clip((f[Y0:Y1, X0:X1].mean(2) - .55) / .45, 0, 1)
    f[Y0:Y1, X0:X1] *= (1 + (fb - 1) * core)[..., None]
    halo = np.zeros((H, W), np.float32); halo[Y0:Y1, X0:X1] = core
    halo = gaussian_filter(halo[::4, ::4], 18)
    halo = np.kron(halo, np.ones((4, 4), np.float32))[:H, :W]
    f += (halo * (.34 + .18 * flick[k] + .08 * breath[k]))[..., None] * np.array([1.0, .62, .25])
    # 3) the light breathes on the lamp and the room
    f *= 1 + fall * (.10 * flick[k] + .06 * breath[k]) * np.array([1.0, .85, .6])
    # 4) heat shimmer above the tip
    dsh = (np.sin(sy * .11 - t * 11 + sx * .03) * 1.8 + np.sin(sy * .05 - t * 6) * 1.2) * sfade
    for c in range(3):
        f[SY0:SY1, SX0:SX1, c] = map_coordinates(f[..., c], [sy, sx + dsh], order=1, mode='nearest')
    # 5) an occasional spark lifts off the wick
    if rng.random() < .025: sparks.append([BX + rng.normal(0, 6), 330.0, rng.normal(0, 8), -rng.uniform(50, 90), t])
    pts = []
    for s in sparks:
        age = t - s[4]
        if age < 1.6: pts.append((s[0] + s[2] * age + np.sin(age * 5) * 4, s[1] + s[3] * age, .9 * (1 - age / 1.6)))
    sparks = [s for s in sparks if t - s[4] < 1.6]
    if pts: f, _ = glow(f, pts, color=(1, .7, .35), core=1.2, halo=6, gain=1.0)
    # warm grade, as before
    f = np.clip(f * .92, 0, 1) ** 1.05 * np.array([1.03, .98, .9])
    w.add(film(f, k, grain=.035, vign=.45, halation=.3))
w.close()
print('done O1_lamp')
