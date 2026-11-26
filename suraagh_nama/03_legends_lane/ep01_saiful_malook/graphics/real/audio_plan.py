"""Music beds and sound effects for Ep 1, placed against the timeline. Missing files are skipped, so a partial
download still mixes. Music ducks under the voice."""
import os, json, glob, numpy as np
from scipy.ndimage import uniform_filter1d

def build(bed, blocks, vo, load_wav, place, at, SR, AUD):
    segs = json.load(open('segs/timeline_r.json'))['segs'] if os.path.exists('segs/timeline_r.json') else json.load(open('segs/timeline.json'))['segs']
    B = {b.get('name', b['kind'])[:3] if b['kind'] == 'vo' else (b.get('name') or 'pre'): b for b in blocks}
    cards = [b for b in blocks if b['kind'] == 'card']
    cache = {}
    def snd(name):
        if name not in cache:
            fs = sorted(glob.glob(AUD + '**/' + name + '.*', recursive=True))
            cache[name] = load_wav(fs[0]) if fs else None
            if not fs: print('  (missing)', name, flush=True)
        return cache[name]
    def seg_t(clip, nth=0):
        hits = [s for s in segs if s['clip'].split('@')[0] == clip]
        return hits[nth] if len(hits) > nth else None
    def span(a, b): return B[a]['t'], B[b]['t'] + B[b]['d']

    # ---------- music (each section's bed, ducked later) ----------
    music = np.zeros_like(bed)
    def bed_music(name, t0, t1, gain, fin=2.0, fout=3.0):
        m = snd(name)
        if m is None: return
        place(music, m, t0, gain, fin, fout, dur=t1 - t0, loop=True)
    t0, t1 = 0, B['P03']['t'] + B['P03']['d']
    bed_music('M1_mystery_opening', 0.0, t1 + 1.5, .55, 3.0, 2.5)
    bed_music('M2_romantic_dastan', B['P04']['t'] - 1.0, B['P08']['t'] + B['P08']['d'] + 1.0, .50, 3.0, 2.0)
    bed_music('M3_storm_tension', B['P09']['t'] - .5, B['P11']['t'] + B['P11']['d'] * .7, .55, 1.5, 3.0)
    bed_music('M4_investigation_bed', B['P12']['t'] - .5, B['P18']['t'] + B['P18']['d'] + .5, .42, 3.0, 3.0)
    bed_music('M5_ending_mystic', B['C_S6']['t'] + 1.0, B['P21']['t'] + B['P21']['d'] + 2.0, .55, 3.0, 4.0)
    # duck under the voice: -9 dB while speaking, smooth 0.35 s
    env = np.abs(vo).max(1); env = uniform_filter1d(env, at(.35))
    env = np.clip(env / (np.percentile(env[env > 1e-4], 70) + 1e-6), 0, 1)
    env = uniform_filter1d(env, at(.5))
    music *= (1 - .65 * env)[:, None]
    bed += music

    # ---------- sound effects ----------
    def fx(name, t, gain, dur=None, fin=.2, fout=.8, loop=False):
        s = snd(name)
        if s is not None and t is not None: place(bed, s, max(0, t), gain, fin, fout, dur=dur, loop=loop)
    end = B['P21']['t'] + B['P21']['d']
    # opening night
    fx('S09_candle_fire', 0, .35, dur=B['P01']['t'] + B['P01']['d'] * .3, fin=.5, fout=2)
    s = seg_t('O2_drop'); fx('S08_water_drop', s and s['t'] + 1.2, .8, dur=3)
    s = seg_t('O3_naran_night'); o3 = s['t'] if s else B['P01']['t']
    fx('S01_night_mountain_wind', o3 - 1, .35, dur=B['P03']['t'] + B['P03']['d'] * .4 - o3 + 1, fin=2, fout=2, loop=True)
    fx('S02_river_stream', o3, .30, dur=B['P03']['t'] + B['P03']['d'] * .4 - o3, fin=2.5, fout=2, loop=True)
    fx('S15_dog_barking_distant', B['P02']['t'] + .4, .30, dur=6, fin=.3, fout=2)
    fx('S14_footsteps_running', B['P03']['t'] + .3, .45, dur=5, fin=.3, fout=1.5)
    s = seg_t('R09_demon'); fx('S04_thunder_distant', s and s['t'] + .2, .55, dur=6)
    s = seg_t('R02_title'); fx('S13_deep_boom', s and s['t'], .55, dur=4, fin=.01, fout=2.5)
    # sitting cards: candle and a soft whoosh
    for c in cards:
        fx('S12_whoosh_soft', c['t'] - .25, .35, dur=1.5, fin=.05, fout=.6)
        fx('S09_candle_fire', c['t'], .30, dur=c['d'], fin=.4, fout=1.0)
    # dastan night
    fx('S07_night_crickets', B['P04']['t'], .22, dur=B['P05']['t'] + B['P05']['d'] - B['P04']['t'], fin=2, fout=2, loop=True)
    s = seg_t('PA5_prince'); fx('S16_snow_wind', s and s['t'], .35, dur=s and s['d'] + .6, fin=1, fout=1.2, loop=True)
    s = seg_t('PA2_descent'); s2 = seg_t('R17_clothes')
    if s and s2: fx('S02_river_stream', s['t'], .26, dur=s2['t'] + s2['d'] - s['t'], fin=2, fout=2, loop=True)
    for c in ('PA2_descent', 'PA3_lake_apparition', 'R04_fairies'):
        s = seg_t(c); fx('S11_magic_shimmer', s and s['t'] + .6, .35, dur=4, fin=.3, fout=2)
    s = seg_t('R04_fairies'); fx('S17_bells_soft', s and s['t'], .18, dur=s and s['d'], fin=1, fout=1, loop=True)
    # the demon: storm under P09–P10, thunder on every lightning flash in the clip
    fx('S05_heavy_rain', B['P09']['t'], .30, dur=B['P10']['t'] + B['P10']['d'] - B['P09']['t'] + 1, fin=2, fout=1.5, loop=True)
    fx('S04_thunder_distant', B['P09']['t'] + .2, .5, dur=6)
    FLASH = (1.6, 4.9, 8.2)
    for s in segs:
        if s['clip'].split('@')[0] != 'R09_demon' or 'from' not in s: continue
        for f in FLASH:
            tt = s['t'] + (f - s['from']) / s['sp']
            if s['t'] <= tt < s['t'] + s['d']: fx('S03_thunder_close', tt - .05, .55 if s['t'] < B['P09']['t'] else .8, dur=5, fin=.01, fout=2)
    # the flood
    s = seg_t('R07_flood')
    if s:
        fx('S13_deep_boom', s['t'], .7, dur=4, fin=.01, fout=2.5)
        fx('S06_flood_rushing', s['t'], .55, dur=s['d'] + .6, fin=.4, fout=1.5, loop=True)
    # evidence
    for c in ('R05_page', 'R11_unesco'):
        s = seg_t(c); fx('S10_paper_page', s and s['t'] + .3, .45, dur=2.5, fin=.02, fout=1)
    fx('S01_night_mountain_wind', B['P17']['t'], .30, dur=B['P17']['d'], fin=2, fout=2, loop=True)
    fx('S01_night_mountain_wind', B['P18']['t'], .25, dur=B['P18']['d'], fin=2, fout=2, loop=True)
    t = phrase_time(['دیو', 'سوتا'], B['P18'])
    fx('S13_deep_boom', t, .55, dur=4, fin=.01, fout=2.5)
    s = seg_t('R07_flood', 1); fx('S06_flood_rushing', s and s['t'], .35, dur=s and s['d'] + .5, fin=.5, fout=1.5, loop=True)
    # ending
    fx('S01_night_mountain_wind', B['P19']['t'], .28, dur=end - B['P19']['t'] + 1, fin=2, fout=3, loop=True)
    s = seg_t('PA7_dance')
    if s:
        fx('S11_magic_shimmer', s['t'] + .4, .30, dur=4, fin=.3, fout=2)
        fx('S17_bells_soft', s['t'], .20, dur=s['d'] + .5, fin=1.2, fout=1.5, loop=True)
    fx('S09_candle_fire', end - 5, .30, dur=5, fin=1, fout=.25)      # the candle goes out

def phrase_time(words, block):
    """vo time of a phrase inside a part → timeline time."""
    asr = json.load(open('../vo/asr.json'))
    ws = [(s, w.strip()) for seg in asr for s, e, w in seg['w']]
    for i in range(len(ws) - len(words) + 1):
        if all(words[k] in ws[i + k][1] for k in range(len(words))) and block['s'] <= ws[i][0] < block['e']:
            return block['t'] + ws[i][0] - block['s'] + .9
    return None
