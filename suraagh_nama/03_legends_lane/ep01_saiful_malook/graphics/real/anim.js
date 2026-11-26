// Frame-by-frame animation of real.html scenes: node anim.js SCENE OUT.mp4 DURATION
// The scene is built with window.setup(SCENE); anim_scenes.js then drives it per frame via window.ANIM[SCENE](t).
const { chromium } = require('playwright'); const path = require('path'); const { spawn } = require('child_process');
(async () => {
  const [scene, out, durS] = process.argv.slice(2); const dur = parseFloat(durS), FPS = 25, N = Math.round(dur * FPS);
  const b = await chromium.launch({ args: ['--allow-file-access-from-files'] });
  const pg = await b.newPage({ viewport: { width: 1920, height: 1080 } });
  await pg.goto('file://' + path.resolve('real.html')); await pg.evaluate(() => document.fonts.ready);
  await pg.evaluate(() => { window.MODE = 'full'; });
  await pg.evaluate(n => window.setup(n), scene);
  await pg.addScriptTag({ path: path.resolve('anim_scenes.js') });
  await pg.evaluate(n => window.ANIM_INIT && window.ANIM_INIT[n] && window.ANIM_INIT[n](), scene);
  const ff = spawn('ffmpeg', ['-y', '-loglevel', 'error', '-f', 'image2pipe', '-framerate', String(FPS), '-i', '-',
    '-vf', 'noise=alls=5:allf=t,vignette=PI/5', '-c:v', 'libx264', '-crf', '16', '-pix_fmt', 'yuv420p', '-movflags', '+faststart', out]);
  const stage = await pg.$('#stage');
  for (let k = 0; k < N; k++) {
    await pg.evaluate(([n, t]) => window.ANIM[n](t), [scene, k / FPS]);
    const buf = await stage.screenshot({ type: 'jpeg', quality: 93 });
    if (!ff.stdin.write(buf)) await new Promise(r => ff.stdin.once('drain', r));
    if (k % 50 === 0) console.log(scene, k, '/', N);
  }
  ff.stdin.end(); await new Promise(r => ff.on('close', r)); await b.close(); console.log('done', scene);
})();
