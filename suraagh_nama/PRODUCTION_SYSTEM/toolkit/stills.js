const { chromium } = require('playwright'); const path=require('path');
(async()=>{const [html,out,...names]=process.argv.slice(2);
const b=await chromium.launch({args:['--allow-file-access-from-files']});const pg=await b.newPage({viewport:{width:1920,height:1080}});
pg.on('pageerror',e=>console.log('ERR',e.message));
await pg.goto('file://'+html);
for(const n of names){await pg.evaluate(n=>window.setup(n),n);await pg.waitForTimeout(500);await (await pg.$('#stage')).screenshot({path:path.join(out,n+'.png')});console.log('ok',n);}
await b.close();})();
