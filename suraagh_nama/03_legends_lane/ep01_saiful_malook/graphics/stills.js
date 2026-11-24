const { chromium } = require('playwright'); const path=require('path');
(async()=>{const [web,out,...pairs]=process.argv.slice(2);
const b=await chromium.launch({args:['--allow-file-access-from-files']});const pg=await b.newPage({viewport:{width:1920,height:1080}});
pg.on('pageerror',e=>console.log('ERR',e.message));pg.on('console',m=>{if(m.type()==='error')console.log('CONSOLE',m.text())});
await pg.goto('file://'+path.join(web,'scenes.html'));await pg.evaluate(()=>document.fonts.ready);
for(const pr of pairs){const [n,t]=pr.split('@');await pg.evaluate(n=>window.setup(n),n);await pg.waitForTimeout(400);await pg.evaluate(t=>window.renderFrame(t),+t);await pg.waitForTimeout(100);
await (await pg.$('#stage')).screenshot({path:path.join(out,`${n}.png`)});console.log('ok',n);}
await b.close();})();
