const { chromium } = require('playwright');
const path = require('path'), fs = require('fs');
(async () => {
  const b = await chromium.launch();
  fs.mkdirSync('layers', { recursive: true });
  for (const [scale, out] of [[1,'chill-cafe-709x236'],[4,'chill-cafe-2836x944']]) {
    const pg = await b.newPage({ viewport:{width:709,height:236}, deviceScaleFactor: scale });
    await pg.goto('file://' + path.resolve('design.html')); await pg.waitForTimeout(600);
    await pg.locator('#c').screenshot({ path: out + '.png' });
    const names = await pg.$$eval('[data-l]', els => els.map(e => e.dataset.l));
    await pg.addStyleTag({ content: 'html,body,#c{background:transparent!important}#c>*{visibility:hidden}' });
    for (const n of names) {
      await pg.addStyleTag({ content: `[data-l="${n}"]{visibility:visible!important}` });
      await pg.screenshot({ path: `layers/${out}__${n}.png`, omitBackground: true });
      await pg.evaluate(() => document.querySelectorAll('style:last-of-type').forEach(()=>{}));
      // remove the style just added
      await pg.evaluate(() => { const s=document.head.querySelectorAll('style'); s[s.length-1].remove(); });
    }
  }
  fs.writeFileSync('layers/order.json', JSON.stringify(await (async()=>{const pg=await b.newPage();await pg.goto('file://'+path.resolve('design.html'));return pg.$$eval('[data-l]',els=>els.map(e=>e.dataset.l));})()));
  await b.close();
})();
