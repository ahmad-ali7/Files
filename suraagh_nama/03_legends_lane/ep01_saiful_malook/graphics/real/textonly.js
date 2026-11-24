const { chromium } = require('playwright'); const path=require('path');
(async()=>{const [html,out,...names]=process.argv.slice(2);
const b=await chromium.launch({args:['--allow-file-access-from-files']});const pg=await b.newPage({viewport:{width:1920,height:1080}});
await pg.goto('file://'+html);await pg.evaluate(()=>{window.TEXTONLY=true;return document.fonts.ready});
for(const n of names){await pg.evaluate(n=>window.setup(n),n);await pg.waitForTimeout(400);await (await pg.$('#stage')).screenshot({path:path.join(out,'T_'+n+'.png'),omitBackground:true});console.log('ok',n);}
await b.close();})();
