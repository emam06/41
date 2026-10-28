const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const b = await chromium.launch();
  for (const [scale, out] of [[1,'chill-cafe-709x236.png'],[4,'chill-cafe-2836x944.png']]) {
    const pg = await b.newPage({ viewport:{width:709,height:236}, deviceScaleFactor: scale });
    await pg.goto('file://' + path.resolve('design.html')); await pg.waitForTimeout(600);
    await pg.locator('#c').screenshot({ path: out });
  }
  await b.close();
})();
