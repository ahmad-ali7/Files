const { chromium } = require('playwright'); const path=require('path');
(async()=>{const [html,out,...names]=process.argv.slice(2);
const b=await chromium.launch({args:['--allow-file-access-from-files']});const pg=await b.newPage({viewport:{width:1920,height:1080}});
await pg.goto('file://'+html);await pg.evaluate(()=>document.fonts.ready);
for(const n of names){for(const mode of ['textonly','notext']){await pg.evaluate(m=>{window.MODE=m},mode);await pg.evaluate(n=>window.setup(n),n);await pg.waitForTimeout(350);
 await (await pg.$('#stage')).screenshot({path:path.join(out,(mode==='textonly'?'T_':'B_')+n+'.png'),omitBackground:mode==='textonly'});}
 console.log('ok',n);}
await b.close();})();
