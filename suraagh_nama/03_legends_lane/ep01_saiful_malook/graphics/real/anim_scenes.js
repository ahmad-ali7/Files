// Per-frame animation for real.html scenes (loaded by anim.js after window.setup).
(() => {
const S = document.getElementById('stage');
const ease = x => { x = Math.min(Math.max(x, 0), 1); return x * x * (3 - 2 * x); };
const lin = (t, a, b) => Math.min(Math.max((t - a) / (b - a), 0), 1);
const nz = (t, s) => (Math.sin(t * 7.1 + s) * .5 + Math.sin(t * 11.3 + s * 2.1) * .3 + Math.sin(t * 2.3 + s * 3.7) * .6 + Math.sin(t * 17.9 + s * .7) * .15) / 1.55;
// real candle footage instead of the still frame
const candleImgs = () => [...S.querySelectorAll('img')].filter(i => (i.getAttribute('src') || '').includes('candle'));
async function candle(t) {
  const src = 'out/candle_seq/c' + String(Math.min(549, Math.floor(t * 25) + 1)).padStart(4, '0') + '.jpg';
  for (const i of candleImgs()) { if (i.getAttribute('src') !== src) { i.src = src; try { await i.decode(); } catch (e) {} } }
}
window.ANIM = {}; window.ANIM_INIT = {};

// ---------- sitting cards: the title writes itself in (right to left), the subtitle settles, candlelight moves ----------
const card = n => {
  let p, title, sub, warm, glint;
  window.ANIM_INIT[n] = () => {
    p = S.children[1]; title = p.children[2]; sub = p.children[3]; warm = p.children[1];
    glint = document.createElement('div'); glint.className = 'abs';
    glint.style.cssText = 'inset:0;mix-blend-mode:soft-light;pointer-events:none;opacity:0';
    p.appendChild(glint);
  };
  window.ANIM[n] = async t => {
    await candle(t);
    const fl = nz(t, 1.3);
    // paper floats gently, slow push-in
    const s = 1 + .025 * ease(t / 5), ry = Math.sin(t * .9) * 2.5;
    p.style.transform = `translate(0px, ${ry}px) rotate(${-1.2 + Math.sin(t * .6) * .25}deg) scale(${s})`;
    p.style.opacity = String(.25 + .75 * ease(lin(t, 0, .45)));
    // candlelight on the paper breathes
    warm.style.opacity = String(.85 + .2 * fl);
    // title: ink write-on from the right, with a soft feathered edge
    const r = ease(lin(t, .35, 2.0)) * 120 - 10;
    const m = `linear-gradient(to left, #000 ${r}%, transparent ${r + 12}%)`;
    title.style.webkitMaskImage = m; title.style.maskImage = m;
    title.style.filter = `url(#rough) blur(${(1 - ease(lin(t, .35, 2.2))) * 1.2}px)`;
    // subtitle settles in
    const u = ease(lin(t, 1.7, 2.6));
    sub.style.opacity = String(u); sub.style.transform = `translateY(${(1 - u) * 14}px)`;
    // a warm glint passes over the card once
    const g = lin(t, 2.7, 3.9);
    glint.style.opacity = String(Math.sin(g * Math.PI) * .9);
    glint.style.background = `linear-gradient(105deg, rgba(255,210,140,0) ${g * 140 - 40}%, rgba(255,214,150,.75) ${g * 140 - 25}%, rgba(255,210,140,0) ${g * 140 - 10}%)`;
  };
};
['C_S1', 'C_S1b', 'C_S2', 'C_S3', 'C_S4', 'C_S5', 'C_S6', 'V2_verse'].forEach(card);

// ---------- first verse over the real lake water ----------
{
  let bg, line, sub, cred;
  window.ANIM_INIT.V1_water = () => { bg = S.querySelector('.bgw'); line = S.querySelector('.vline'); sub = S.querySelector('.vsub'); cred = S.querySelector('.vcred'); };
  window.ANIM.V1_water = async t => {
    const src = 'out/water_seq/w' + String(Math.min(185, Math.floor(t * 25) + 1)).padStart(4, '0') + '.jpg';
    if (bg.getAttribute('src') !== src) { bg.src = src; try { await bg.decode(); } catch (e) {} }
    bg.style.transform = `scale(${1.02 + .04 * ease(t / 7.4)})`;
    const r = ease(lin(t, .2, 2.0)) * 120 - 10, m = `linear-gradient(to left, #000 ${r}%, transparent ${r + 12}%)`;
    line.style.webkitMaskImage = m; line.style.maskImage = m;
    const u = ease(lin(t, 1.8, 2.7)); sub.style.opacity = String(u); sub.style.transform = `translateY(${(1 - u) * 12}px)`;
    cred.style.opacity = String(ease(lin(t, 2.4, 3.2)));
  };
}

// ---------- the astrologer's chart: lines draw themselves, signs ink in, the stars wake, a line of fate points to Kaghan ----------
{
  let pg, shapes, texts, light, capEls, stars = [], fate, svg;
  window.ANIM_INIT.R03_astro = () => {
    pg = S.children[0]; light = S.children[2]; capEls = [S.children[3], S.children[4]];
    svg = pg.querySelector('svg');
    shapes = [...svg.querySelectorAll('g')[0].children];
    shapes.forEach(e => { e.setAttribute('pathLength', '1'); e.style.strokeDasharray = '1 1'; e.style.strokeDashoffset = '1'; });
    texts = [...svg.querySelectorAll('text')];
    texts.forEach(e => { e.style.opacity = '0'; });
    const NS = 'http://www.w3.org/2000/svg';
    // stars in a few houses
    [[500, 380], [300, 300], [720, 640], [260, 680], [640, 160], [820, 420], [500, 620]].forEach(([x, y], i) => {
      const c = document.createElementNS(NS, 'circle'); c.setAttribute('cx', x); c.setAttribute('cy', y); c.setAttribute('r', 7);
      c.setAttribute('fill', '#ffd27a'); c.style.filter = 'drop-shadow(0 0 10px #ffb347) drop-shadow(0 0 22px #ff9a2e)'; c.style.opacity = '0';
      svg.appendChild(c); stars.push(c);
    });
    // the line of fate: from the centre up to the northern house (Kaghan)
    fate = document.createElementNS(NS, 'path'); fate.setAttribute('d', 'M500 500 Q520 330 500 140');
    fate.setAttribute('stroke', '#ffcf73'); fate.setAttribute('stroke-width', '6'); fate.setAttribute('fill', 'none'); fate.setAttribute('stroke-linecap', 'round');
    fate.setAttribute('pathLength', '1'); fate.style.strokeDasharray = '1 1'; fate.style.strokeDashoffset = '1';
    fate.style.filter = 'drop-shadow(0 0 8px #ffb347) drop-shadow(0 0 18px #ff8c1a)';
    svg.appendChild(fate);
  };
  window.ANIM.R03_astro = async t => {
    await candle(t);
    const fl = nz(t, .7);
    // slow camera on the paper only (the caption stays put)
    pg.style.transform = `perspective(1600px) rotateX(${32 - 4 * ease(t / 19)}deg) rotateZ(${4 - 2.5 * ease(t / 19)}deg) scale(${1 + .07 * ease(t / 19)})`;
    light.style.opacity = String(.85 + .25 * fl);
    // lines draw in order: frame, diagonals, diamond
    const seq = [[.2, 1.6], [1.4, 2.6], [1.6, 2.8], [2.6, 4.2]];
    shapes.forEach((e, i) => { const [a, b] = seq[Math.min(i, seq.length - 1)]; e.style.strokeDashoffset = String(1 - ease(lin(t, a, b))); });
    // signs ink in one by one
    texts.forEach((e, i) => { const a = 3.4 + i * .32; const u = ease(lin(t, a, a + .7)); e.style.opacity = String(u * .95); e.style.filter = `blur(${(1 - u) * 3}px)`; });
    // stars wake and twinkle
    stars.forEach((c, i) => { const a = 7.5 + i * .45; const u = ease(lin(t, a, a + 1.2)); c.style.opacity = String(u * (.65 + .35 * Math.sin(t * (2.2 + i * .37) + i))); });
    // the line of fate (during "...کاغان کے پہاڑوں میں ملے گی")
    fate.style.strokeDashoffset = String(1 - ease(lin(t, 12.0, 13.8)));
    fate.style.opacity = String(.75 + .25 * Math.sin(t * 3));
    capEls.forEach(e => { e.style.opacity = String(ease(lin(t, 0, .8))); });
  };
}

// ---------- the travelling story: the route draws itself stop by stop, the camera follows ----------
{
  let cam, paths, dots, labels, head, title, titleScrim;
  const KF = [ // t, centre x, centre y, scale
    [0, 330, 290, 1.55], [6.2, 380, 300, 1.72], [7.0, 600, 360, 1.45], [8.6, 1100, 760, 1.38], [10.7, 1560, 800, 1.4],
    [13.0, 1200, 470, 1.42], [15.6, 1180, 380, 1.55], [16.6, 1180, 350, 1.7], [18.6, 960, 540, 1.0], [20.6, 1020, 470, 1.08]];
  const STOP = [[6.2, 6.8], [6.9, 8.5], [8.6, 10.6], [10.7, 13.0], [15.5, 16.4]];     // when each leg of the route draws
  const LABEL = [.6, 6.6, 8.5, 10.6, 13.0, 16.4];
  function camAt(t) {
    let i = 0; while (i < KF.length - 2 && t > KF[i + 1][0]) i++;
    const [t0, x0, y0, s0] = KF[i], [t1, x1, y1, s1] = KF[i + 1]; const u = ease(lin(t, t0, t1));
    return [x0 + (x1 - x0) * u, y0 + (y1 - y0) * u, s0 + (s1 - s0) * u];
  }
  window.ANIM_INIT.R06b_map = () => {
    const kids = [...S.children];
    cam = document.createElement('div'); cam.className = 'abs'; cam.style.cssText = 'left:0;top:0;width:1920px;height:1080px;transform-origin:0 0';
    S.insertBefore(cam, kids[0]);
    kids.slice(0, 8).forEach(k => cam.appendChild(k));          // map, route svg, six labels move with the camera
    title = kids[10]; titleScrim = kids[9];
    const svg = cam.querySelector('svg'); const g = svg.querySelectorAll('g');
    paths = [...g[0].children]; dots = [...g[1].children];
    labels = kids.slice(2, 8);
    const NS = 'http://www.w3.org/2000/svg'; const defs = document.createElementNS(NS, 'defs'); svg.prepend(defs);
    paths.forEach((p, i) => {   // reveal each dotted leg through a solid stroke mask that grows along it
      const m = document.createElementNS(NS, 'mask'); m.setAttribute('id', 'leg' + i); m.setAttribute('maskUnits', 'userSpaceOnUse');
      const mp = document.createElementNS(NS, 'path'); mp.setAttribute('d', p.getAttribute('d')); mp.setAttribute('stroke', '#fff'); mp.setAttribute('stroke-width', '26');
      mp.setAttribute('fill', 'none'); mp.setAttribute('pathLength', '1'); mp.style.strokeDasharray = '1 1'; mp.style.strokeDashoffset = '1';
      m.appendChild(mp); defs.appendChild(m); p.setAttribute('mask', `url(#leg${i})`); p._m = mp;
    });
    head = document.createElementNS(NS, 'circle'); head.setAttribute('r', '10'); head.setAttribute('fill', '#ffcf73');
    head.style.filter = 'drop-shadow(0 0 8px #ffb347) drop-shadow(0 0 20px #ff8c1a)'; svg.appendChild(head);
  };
  window.ANIM.R06b_map = async t => {
    const [cx, cy, s] = camAt(t);
    let tx = 960 - cx * s, ty = 540 - cy * s;
    tx = Math.min(0, Math.max(1920 - 1920 * s, tx)); ty = Math.min(-36 * s, Math.max(1080 - 1044 * s, ty));
    if (s <= 1.001) { tx = 0; ty = 0; }
    cam.style.transform = `translate(${tx}px, ${ty}px) scale(${s})`;
    let hx = null, hy = null;
    paths.forEach((p, i) => {
      const u = ease(lin(t, STOP[i][0], STOP[i][1])); p._m.style.strokeDashoffset = String(1 - u);
      if (u > 0 && u < 1) { const L = p.getTotalLength(), pt = p.getPointAtLength(L * u); hx = pt.x; hy = pt.y; }
    });
    head.style.opacity = hx === null ? '0' : '1'; if (hx !== null) { head.setAttribute('cx', hx); head.setAttribute('cy', hy); }
    dots.forEach((d, i) => { const u = ease(lin(t, LABEL[i] - .2, LABEL[i] + .3)); d.style.opacity = String(u); });
    labels.forEach((l, i) => { const u = ease(lin(t, LABEL[i], LABEL[i] + .6)); l.style.opacity = String(u); l.style.transform = `scale(${.92 + .08 * u})`; });
    // Kaghan pulses when the story arrives
    const k = lin(t, 16.4, 20.6); dots[5].setAttribute('r', String(9 + 6 * Math.abs(Math.sin(k * Math.PI * 3)) * (k > 0 ? 1 : 0)));
    title.style.opacity = titleScrim.style.opacity = String(ease(lin(t, .3, 1.3)));
  };
}
})();
