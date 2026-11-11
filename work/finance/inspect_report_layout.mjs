import {chromium} from 'playwright';
import path from 'node:path';
import fs from 'node:fs/promises';
import {pathToFileURL} from 'node:url';
await fs.mkdir('tmp/report_layout',{recursive:true});
const browser=await chromium.launch({executablePath:'C:/Program Files/Google/Chrome/Application/chrome.exe',headless:true});
const page=await browser.newPage({viewport:{width:1440,height:1050},deviceScaleFactor:1});
await page.goto(pathToFileURL(path.resolve('deliverables/report/full_strategy_report.html')).href);
await page.waitForFunction(()=>Array.from(document.images).every(i=>i.complete&&i.naturalWidth>0));
const info=await page.evaluate(()=>({images:document.images.length,broken:[...document.images].filter(i=>!i.naturalWidth).length,overflow:document.documentElement.scrollWidth>innerWidth,headings:[...document.querySelectorAll('h2')].map(e=>e.textContent)}));
await page.screenshot({path:'tmp/report_layout/opening.png'});
for(const [id,name] of [['section-5','portfolio'],['section-7','finance'],['section-8','inaction']]){
 await page.locator(`#${id}`).scrollIntoViewIfNeeded();
 await page.screenshot({path:`tmp/report_layout/${name}.png`});
}
await page.setViewportSize({width:760,height:1000});
await page.goto(pathToFileURL(path.resolve('deliverables/report/full_strategy_report.html')).href);
console.log(JSON.stringify({...info,narrowOverflow:await page.evaluate(()=>document.documentElement.scrollWidth>innerWidth)},null,2));
await browser.close();
