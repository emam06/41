// Renders each designN.html to flat PNGs (1x and 4x) and one transparent PNG per layer.
const { chromium } = require('playwright');
const path = require('path'), fs = require('fs');
const only = process.argv.slice(2).map(Number);
(async () => {
  const b = await chromium.launch();
  fs.mkdirSync('layers', { recursive: true });
  fs.mkdirSync('out', { recursive: true });
  for (const d of [1, 2, 3, 4]) {
    if (only.length && !only.includes(d)) continue;
    const order = [];
    for (const [scale, tag] of [[1, '709x236'], [4, '2836x944']]) {
      const pg = await b.newPage({ viewport: { width: 709, height: 236 }, deviceScaleFactor: scale });
      await pg.goto('file://' + path.resolve(`design${d}.html`));
      await pg.evaluate(() => document.fonts.ready); await pg.waitForTimeout(500);
      await pg.locator('#c').screenshot({ path: `out/safari-${d}-${tag}.png` });
      const names = await pg.$$eval('[data-l]', els => els.map(e => e.dataset.l));
      if (!order.length) order.push(...names);
      await pg.addStyleTag({ content: 'html,body,#c{background:transparent!important}#c>*{visibility:hidden}' });
      for (const n of names) {
        const h = await pg.addStyleTag({ content: `[data-l="${n}"]{visibility:visible!important}` });
        await pg.screenshot({ path: `layers/d${d}-${tag}__${n}.png`, omitBackground: true });
        await h.evaluate(el => el.remove());
      }
      await pg.close();
    }
    fs.writeFileSync(`layers/d${d}-order.json`, JSON.stringify(order));
  }
  await b.close();
})();
