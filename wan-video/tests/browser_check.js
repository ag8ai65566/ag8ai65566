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
  // ---- the pose library: 285 entries rendered, filtered and clicked ----
  await page.click('.tabs button[data-tab="pb"]');
  await page.waitForTimeout(600);
  const poseCount = await page.evaluate(() =>
    document.querySelectorAll('#pklist button.pk').length);
  check(poseCount > 0, `the pose library renders (${poseCount} buttons)`);
  const countLabel = await page.textContent('#pkcount');
  check(/\d+ 個動作/.test(countLabel || ''), `…and says how many (${countLabel})`);

  await page.fill('#pkq', 'paizuri');
  await page.waitForTimeout(250);
  const filtered = await page.evaluate(() =>
    document.querySelectorAll('#pklist button.pk').length);
  check(filtered > 0 && filtered < poseCount,
    `search narrows the list (${poseCount} -> ${filtered})`);
  await page.fill('#pkq', 'zzzz-no-such-pose');
  await page.waitForTimeout(250);
  check((await page.textContent('#pklist')).includes('沒有符合'),
    'an empty result says so rather than showing a blank area');
  await page.fill('#pkq', '');
  await page.waitForTimeout(250);

  // Open one that carries artist tags anywhere in the entry. Picking on the
  // first variant alone finds nothing: in this document the canonical `主要 Tag`
  // string is always artist-free, so NO pose has artists on the version shown
  // first. That is exactly the bug this check found - the switch did nothing on
  // every pose - and the fix was to treat the artist run as belonging to the
  // entry, which is why targeting the entry is now the right thing to assert.
  const opened = await page.evaluate(() => {
    const target = PK.poses.find((p) => (p.artist_names || []).length);
    if (!target) return '';
    const btn = document.querySelector(`#pklist button.pk[data-pose="${target.id}"]`);
    if (btn) { btn.click(); return target.title; }
    return '';
  });
  await page.waitForTimeout(500);
  check(!!opened, `clicking a pose opens it (${opened})`);
  const built = await page.inputValue('#pkprompt');
  check(built.length > 10, `…with a prompt assembled (${built.slice(0, 48)}…)`);
  check(!/[{}\[\]]/.test(built) && !built.includes('::'),
    'the assembled prompt carries no NAI syntax');
  check(!/\bartist\s*:/i.test(built),
    'artists stay out by default, so they cannot overrule the character pack');

  await page.check('#pkartists');
  await page.waitForTimeout(500);
  const withArtists = await page.inputValue('#pkprompt');
  check(/\bartist\s*:/i.test(withArtists), 'ticking the box brings the artists in');
  check(await page.isVisible('#pkawrap'), '…and reveals the artist weight slider');
  await page.uncheck('#pkartists');
  await page.waitForTimeout(400);
  check(!await page.isVisible('#pkawrap'), 'unticking hides it again');

  await page.fill('#pkhead', 'mori calliope, hololive');
  await page.dispatchEvent('#pkhead', 'change');
  await page.waitForTimeout(500);
  check((await page.inputValue('#pkprompt')).startsWith('mori calliope, hololive'),
    'the character you type goes to the front of the prompt');

  await page.click('#pkuse');
  await page.waitForTimeout(400);
  const sent = await page.inputValue('#iprompt');
  check(sent.startsWith('mori calliope, hololive'),
    'sending it lands in the image prompt and switches tab');
  check(await page.evaluate(() =>
    !document.getElementById('tab-img').classList.contains('hidden')),
    '…on the image tab');

  await page.click('.tabs button[data-tab="img"]');
  await page.waitForTimeout(400);
  const overflow = await page.evaluate(() =>
    document.documentElement.scrollWidth - document.documentElement.clientWidth);
  check(overflow <= 0, `no horizontal overflow at 1280px (${overflow}px)`);
  await page.screenshot({ path: 'shot-img-1280.png', fullPage: false });

  // The pose library is the widest new thing on the page, so it gets its own
  // small-screen measurement rather than trusting the image tab to represent it.
  await page.click('.tabs button[data-tab="pb"]');
  await page.setViewportSize({ width: 375, height: 800 });
  await page.waitForTimeout(400);
  const pkNarrow = await page.evaluate(() =>
    document.documentElement.scrollWidth - document.documentElement.clientWidth);
  check(pkNarrow <= 1, `the pose library does not overflow at 375px (${pkNarrow}px)`);
  await page.screenshot({ path: 'shot-pose-375.png', fullPage: false });
  await page.setViewportSize({ width: 1280, height: 900 });
  await page.waitForTimeout(200);

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
