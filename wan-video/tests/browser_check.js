/*
 * Load the running app in a real browser and check what only a browser can see.
 *
 * Optional - it needs Playwright and a running server, so test_flow.py does not
 * invoke it. Everything else in tests/ reasons about the page as text; this
 * renders it. That difference is not academic: this found two bugs that the
 * static checks and the stub-DOM harness both passed clean.
 *
 *   1. `.chk { white-space: nowrap }` made a long checkbox label push the whole
 *      page 112px wider than a 375px phone.
 *   2. No favicon, so every single page load logged a 404.
 *
 *   # terminal 1
 *   cd app && python -m uvicorn server:app --port 8811
 *   # terminal 2
 *   npm install playwright
 *   node tests/browser_check.js
 *
 * The Chromium path below is the one this dev container ships; on a normal
 * machine drop the executablePath and let Playwright find its own.
 */
const { chromium } = require('playwright');
(async () => {
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' });
  const errors = [], warnings = [];
  const ctx = await browser.newContext({ viewport: { width: 1280, height: 900 } });
  const page = await ctx.newPage();
  page.on('console', (m) => { if (m.type() === 'error') errors.push(m.text()); });
  page.on('pageerror', (e) => errors.push('pageerror: ' + e.message));
  await page.goto('http://127.0.0.1:8811/', { waitUntil: 'networkidle' });

  const say = (ok, label) => console.log((ok ? '  ok   ' : '  FAIL ') + label);
  let bad = 0;
  const check = (ok, label) => { if (!ok) bad++; say(ok, label); };

  check(errors.length === 0, `no console errors on load (${errors.slice(0,3).join(' | ') || 'clean'})`);

  // Every tab still opens, and only its own panel is visible.
  const tabs = await page.$$eval('.tabs button', (bs) => bs.map((b) => b.dataset.tab));
  check(tabs.length === 7, `all 7 tabs present (${tabs.join(',')})`);
  for (const t of tabs) {
    await page.click(`.tabs button[data-tab="${t}"]`);
    await page.waitForTimeout(120);
    const shown = await page.$$eval('[role="tabpanel"]',
      (ps) => ps.filter((p) => !p.classList.contains('hidden')).map((p) => p.id));
    check(shown.length === 1 && shown[0] === 'tab-' + t, `${t}: only its panel is visible (${shown})`);
    const sel = await page.$eval(`.tabs button[data-tab="${t}"]`, (b) => b.getAttribute('aria-selected'));
    check(sel === 'true', `${t}: announced as selected`);
  }
  check(errors.length === 0, `no console errors after visiting every tab (${errors.slice(0,2).join(' | ') || 'clean'})`);

  // Keyboard: one tab stop, arrows move, and focus is actually visible.
  await page.click('.tabs button[data-tab="gen"]');
  await page.keyboard.press('ArrowRight');
  const after = await page.evaluate(() => document.activeElement.dataset.tab);
  check(after === 'img', `ArrowRight moves focus to the next tab (${after})`);
  const ring = await page.evaluate(() => {
    const s = getComputedStyle(document.activeElement);
    return { w: s.outlineWidth, style: s.outlineStyle };
  });
  check(parseFloat(ring.w) >= 2 && ring.style !== 'none',
        `the focused tab has a real ring (${ring.w} ${ring.style})`);

  // The image tab is the busiest one; make sure it renders and nothing overflows.
  await page.click('.tabs button[data-tab="img"]');
  await page.waitForTimeout(400);
  const overflow = await page.evaluate(() =>
    document.documentElement.scrollWidth - document.documentElement.clientWidth);
  check(overflow <= 0, `no horizontal overflow at 1280px (${overflow}px)`);
  await page.screenshot({ path: 'shot-img-1280.png', fullPage: false });

  // 375px is the small-phone case the checklist calls for.
  await page.setViewportSize({ width: 375, height: 800 });
  await page.waitForTimeout(300);
  const overflowMobile = await page.evaluate(() =>
    document.documentElement.scrollWidth - document.documentElement.clientWidth);
  check(overflowMobile <= 1, `no horizontal overflow at 375px (${overflowMobile}px)`);
  await page.screenshot({ path: 'shot-img-375.png', fullPage: false });

  await page.setViewportSize({ width: 1280, height: 900 });
  await page.click('.tabs button[data-tab="set"]');
  await page.waitForTimeout(400);
  await page.screenshot({ path: 'shot-set-1280.png' });

  console.log(bad ? `FAILED ${bad}` : 'PASSED');
  await browser.close();
  process.exit(bad ? 1 : 0);
})();
