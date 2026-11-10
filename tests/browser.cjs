const {chromium}=require('playwright');
const assert=require('node:assert/strict');
(async()=>{
 const browser=await chromium.launch({executablePath:'/usr/bin/chromium',args:['--no-sandbox']});
 const page=await browser.newPage({ignoreHTTPSErrors:true});const errors=[];page.on('pageerror',e=>errors.push(e.message));
 const base=process.env.PRIME_TEST_URL || 'http://localhost:8000/';
 for(const width of [320,768,1024,1440]){
  await page.setViewportSize({width,height:900});
  for(const name of ['index','eventos','peleadores','penthouse','media','contacto']){
   await page.goto(base+name+'.html');
   await page.waitForTimeout(100);
   assert(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth),`${name}: overflow ${width}`);
   assert.equal(await page.locator('h1').count(),1);
   for(const image of await page.locator('img[src^="assets/"]').all()){if(await image.isVisible()){await image.scrollIntoViewIfNeeded();await image.evaluate(el=>el.decode());}}
  }
 }
 await page.setViewportSize({width:390,height:844});await page.goto(base+'index.html');
 await page.locator('#menuButton').click();assert.equal(await page.locator('#menuButton').getAttribute('aria-expanded'),'true');
 await page.keyboard.press('Escape');assert.equal(await page.locator('#menuButton').getAttribute('aria-expanded'),'false');
 await page.locator('[data-video]').first().click();assert(await page.locator('dialog').isVisible());await page.keyboard.press('Escape');
 await page.emulateMedia({reducedMotion:'reduce'});await page.reload();
 assert.equal(await page.evaluate(()=>document.getAnimations().length),0);
 await page.screenshot({path:'/tmp/prime-mobile.png',fullPage:true});
 await page.setViewportSize({width:1440,height:1000});await page.goto(base+'penthouse.html');await page.screenshot({path:'/tmp/prime-penthouse.png',fullPage:true});
 assert.deepEqual(errors,[]);console.log('PASS: 24 páginas/tamaños, logos locales, menú, Escape, diálogo de video y movimiento reducido.');await browser.close();
})();
