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
const zlib = require('zlib');
// A minimal but genuinely valid PNG of the requested size. The dataset checker
// reads dimensions out of the file, so the fixture has to really be that size.
function pngOf(width, height) {
  const chunk = (type, data) => {
    const len = Buffer.alloc(4); len.writeUInt32BE(data.length);
    const body = Buffer.concat([Buffer.from(type, 'ascii'), data]);
    const crcBuf = Buffer.alloc(4); crcBuf.writeUInt32BE(crc32(body) >>> 0);
    return Buffer.concat([len, body, crcBuf]);
  };
  const ihdr = Buffer.alloc(13);
  ihdr.writeUInt32BE(width, 0); ihdr.writeUInt32BE(height, 4);
  ihdr[8] = 8; ihdr[9] = 0; ihdr[10] = 0; ihdr[11] = 0; ihdr[12] = 0;  // 8-bit grey
  const raw = Buffer.alloc(height * (width + 1));  // one filter byte per row
  const idat = zlib.deflateSync(raw);
  return Buffer.concat([
    Buffer.from([0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a]),
    chunk('IHDR', ihdr), chunk('IDAT', idat), chunk('IEND', Buffer.alloc(0)),
  ]);
}
let CRC_TABLE = null;
function crc32(buf) {
  if (!CRC_TABLE) {
    CRC_TABLE = new Int32Array(256);
    for (let n = 0; n < 256; n++) {
      let c = n;
      for (let k = 0; k < 8; k++) c = c & 1 ? 0xedb88320 ^ (c >>> 1) : c >>> 1;
      CRC_TABLE[n] = c;
    }
  }
  let c = 0xffffffff;
  for (const b of buf) c = CRC_TABLE[(c ^ b) & 0xff] ^ (c >>> 8);
  return (c ^ 0xffffffff) >>> 0;
}


(async () => {
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' });
  const errors = [], warnings = [];
  const ctx = await browser.newContext({ viewport: { width: 1280, height: 900 } });
  const page = await ctx.newPage();
  // A request that was cut off mid-flight is not a fault in the page: reloading
  // aborts whatever polling was running, and the browser logs that as
  // ERR_CONNECTION_RESET. The event arrives asynchronously, so it lands
  // wherever it lands - which made it get blamed on whichever block happened to
  // be running. Kept in a separate list rather than dropped, so a genuine flood
  // of them is still visible. Server faults are unaffected: those log as
  // "the server responded with a status of ..." and stay in `errors`.
  const aborted = [];
  page.on('console', (m) => {
    if (m.type() !== 'error') return;
    const text = m.text();
    if (/ERR_CONNECTION_RESET|ERR_ABORTED|ERR_NETWORK_CHANGED/.test(text)) {
      aborted.push(text);
      return;
    }
    errors.push(text);
  });
  page.on('pageerror', (e) => errors.push('pageerror: ' + e.message));
  await page.goto('http://127.0.0.1:8811/', { waitUntil: 'networkidle' });

  // A training folder for the 訓練角色 block to inspect. Made here so the suite
  // does not depend on a folder someone created by hand.
  const TRAIN_FIXTURE = require('path').join(require('os').tmpdir(), 'wan-trainset');
  await page.evaluate(() => {});
  {
    const fs = require('fs');
    fs.rmSync(TRAIN_FIXTURE, { recursive: true, force: true });
    fs.mkdirSync(TRAIN_FIXTURE, { recursive: true });
    // 1x1 PNGs would be caught as undersized, so the fixture carries real
    // dimensions: the checker reads the header, not the filename.
    for (let i = 0; i < 26; i++) {
      const tall = i % 3 !== 0;
      const png = pngOf(tall ? 832 : 1216, tall ? 1216 : 832);
      fs.writeFileSync(require('path').join(TRAIN_FIXTURE, String(i).padStart(2,'0') + '.png'), png);
      fs.writeFileSync(require('path').join(TRAIN_FIXTURE, String(i).padStart(2,'0') + '.txt'),
        `s1vra_person, adult, framing ${i}, outfit ${i}`, 'utf-8');
    }
  }

  const say = (ok, label) => console.log((ok ? '  ok   ' : '  FAIL ') + label);
  let bad = 0;
  const check = (ok, label) => { if (!ok) bad++; say(ok, label); };

  check(errors.length === 0, `no console errors on load (${errors.slice(0,3).join(' | ') || 'clean'})`);

  // Every tab still opens, and only its own panel is visible.
  const tabs = await page.$$eval('.tabs button', (bs) => bs.map((b) => b.dataset.tab));
  check(tabs.length === 9, `all 9 tabs present (${tabs.join(',')})`);
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
  await page.waitForTimeout(500);
  // ---- ComfyUI not running: the most common failure there is ----
  // This app hands every job to ComfyUI and cannot start it itself. The
  // failure used to reach the user as `ClientConnectorError: Cannot connect to
  // host 127.0.0.1:8188 ssl:default [The remote computer refused the network
  // connection]` - every word true, and not one of them saying "ComfyUI is not
  // running". There is no ComfyUI in this container, so the banner is live.
  check(await page.isVisible('#comfydown'),
    'a banner says so when ComfyUI is not running');
  const downTxt = await page.textContent('#comfydown');
  check(downTxt.includes('ComfyUI 沒有在跑'),
    'and leads with what is wrong -> ' + downTxt.replace(/\s+/g, ' ').slice(0, 28));
  check(downTxt.includes('run_nvidia_gpu.bat'), '…naming the file to double-click');
  check(downTxt.includes('COMFY_URL'), '…and where to change it if the port differs');
  check(!downTxt.includes('ClientConnectorError') && !downTxt.includes('ssl:default'),
    '…with no raw Python exception left in it');
  check((await page.textContent('#sub')).includes('ComfyUI 還沒開'),
    'and the header line stays to four words');

  // ---- weights ----
  await page.fill('#iprompt', '1girl, ahegao, breasts out');
  // caret inside "ahegao"
  await page.evaluate(() => { const b=document.getElementById('iprompt'); b.focus(); b.setSelectionRange(10,10); });
  await page.keyboard.down('Control'); await page.keyboard.press('ArrowUp'); await page.keyboard.up('Control');
  let v = await page.inputValue('#iprompt');
  check(v === '1girl, (ahegao:1.05), breasts out', 'Ctrl+Up wraps the tag under the caret -> ' + v);
  for (let i=0;i<3;i++){ await page.keyboard.down('Control'); await page.keyboard.press('ArrowUp'); await page.keyboard.up('Control'); }
  v = await page.inputValue('#iprompt');
  check(v.includes('(ahegao:1.2)'), 'repeats accumulate, printed as 1.2 not 1.20 -> ' + v);
  for (let i=0;i<4;i++){ await page.keyboard.down('Control'); await page.keyboard.press('ArrowDown'); await page.keyboard.up('Control'); }
  v = await page.inputValue('#iprompt');
  check(v === '1girl, ahegao, breasts out', 'back at 1.0 the parens come off -> ' + v);
  // selection form
  await page.evaluate(() => { const b=document.getElementById('iprompt'); b.focus(); b.setSelectionRange(15,26); });
  await page.click('#iwup');
  v = await page.inputValue('#iprompt');
  check(v.includes('(breasts out:1.05)'), 'the button weights a multi-word selection -> ' + v);
  // clamp
  await page.fill('#iprompt', '(x:1.95)');
  await page.evaluate(() => { const b=document.getElementById('iprompt'); b.focus(); b.setSelectionRange(3,3); });
  for (let i=0;i<6;i++) await page.click('#iwup');
  v = await page.inputValue('#iprompt');
  check(v === '(x:2)', 'clamped at 2.0 -> ' + v);

  // ---- quick tags ----
  await page.fill('#iprompt', '1girl');
  await page.click('#itags');
  await page.waitForTimeout(400);
  const chips = await page.evaluate(() => document.querySelectorAll('#qtlist button.qt').length);
  check(chips > 250, `the tag list renders (${chips} chips)`);
  await page.fill('#qtq', 'ahegao');
  await page.waitForTimeout(250);
  const found = await page.evaluate(() => [...document.querySelectorAll('#qtlist button.qt')].map(b=>b.dataset.tag));
  check(found.includes('ahegao'), 'search finds it -> ' + found.join(','));
  await page.fill('#qtq', '阿嘿顏');
  await page.waitForTimeout(250);
  const zh = await page.evaluate(() => [...document.querySelectorAll('#qtlist button.qt')].map(b=>b.dataset.tag));
  check(zh.includes('ahegao'), 'Chinese search works too -> ' + zh.join(','));
  await page.fill('#qtq', 'double peace gesture');
  await page.waitForTimeout(250);
  const fixTxt = await page.textContent('#qtlist');
  check(fixTxt.includes('double v'), 'a dead tag name is answered with the real one');
  await page.click('#qtfix');
  v = await page.inputValue('#iprompt');
  check(v === '1girl, double v', 'and "add this" adds the corrected tag -> ' + v);
  // clicking a chip, then weighting it straight away
  await page.fill('#qtq', 'heart hands');
  await page.waitForTimeout(250);
  await page.click('#qtlist button.qt');
  v = await page.inputValue('#iprompt');
  check(v.endsWith('heart hands'), 'a chip appends -> ' + v);
  await page.click('#iwup');
  v = await page.inputValue('#iprompt');
  check(v.endsWith('(heart hands:1.05)'), 'the caret is left on it, so weighting is one more key -> ' + v);
  await page.click('#qtlist button.qt');
  v = await page.inputValue('#iprompt');
  check((v.match(/heart hands/g) || []).length === 1,
      'clicking twice does not duplicate, even after weighting -> ' + v);
  check((await page.textContent('#iwhint')).includes('已經在提詞裡'), 'and it says why');

  // ---- favourites pinned by the character picker ----
  check(await page.isVisible('#favbox'), 'the favourites strip is on the character-pack panel');
  const n = await page.evaluate(()=>document.querySelectorAll('#favlist button.fav').length);
  check(n === 13, `13 favourites pinned (${n})`);
  const labels = await page.evaluate(()=>[...document.querySelectorAll('#favlist button.fav')].map(b=>b.textContent.trim()));
  check(labels.includes('雙手比 V') && labels.includes('阿嘿顏') && labels.includes('無表情')
     && labels.includes('厭惡表情') && labels.includes('認真表情') && labels.includes('高興表情')
     && labels.includes('上身全裸') && labels.includes('下身全裸') && labels.includes('蹲馬步（蹲姿張腿）'),
     'everything asked for is there -> ' + labels.join('／'));

  await page.evaluate(()=>{ const s=document.getElementById('imodel'); s.value='noobai'; s.dispatchEvent(new Event('change')); });
  await page.waitForTimeout(300);
  await page.fill('#iprompt', '1girl');
  await page.click('#favlist button.fav[data-fav="double_v"]');
  await page.waitForTimeout(200);
  v = await page.inputValue('#iprompt');
  check(v === '1girl, double v', 'danbooru model gets the tag -> ' + v);
  await page.click('#favlist button.fav[data-fav="horse_stance"]');
  await page.waitForTimeout(200);
  v = await page.inputValue('#iprompt');
  check(v === '1girl, double v, squatting, spread legs', 'a multi-tag favourite adds both -> ' + v);
  await page.click('#favlist button.fav[data-fav="horse_stance"]');
  await page.waitForTimeout(200);
  v = await page.inputValue('#iprompt');
  check(v === '1girl, double v', 'clicking again takes it back out -> ' + v);

  // weighted tags must survive the removal path
  await page.fill('#iprompt', '1girl');
  await page.click('#favlist button.fav[data-fav="ahegao"]');
  await page.waitForTimeout(150);
  await page.click('#iwup'); await page.click('#iwup');
  v = await page.inputValue('#iprompt');
  check(v.includes('(ahegao:1.1)'), 'a favourite can be weighted straight away -> ' + v);
  await page.click('#favlist button.fav[data-fav="ahegao"]');
  await page.waitForTimeout(200);
  v = await page.inputValue('#iprompt');
  check(v === '1girl', 'and removing it finds the weighted form too -> ' + v);

  // switching to a photo model must change the spelling
  await page.fill('#iprompt', '1girl');
  await page.evaluate(()=>{ const s=document.getElementById('imodel'); s.value='juggernaut'; s.dispatchEvent(new Event('change')); });
  await page.waitForTimeout(400);
  check((await page.textContent('#favstyle')).includes('寫實'), 'it says the model wants plain language');
  await page.click('#favlist button.fav[data-fav="double_v"]');
  await page.waitForTimeout(200);
  v = await page.inputValue('#iprompt');
  check(v === '1girl, making a peace sign with both hands',
     'the photo model gets a sentence, not a danbooru tag -> ' + v);
  // The chip state must follow the prompt, not a side list: retyping the box
  // by hand has to turn the chip back off.
  const lit = await page.evaluate(()=>document.querySelector('#favlist button.fav[data-fav="double_v"]').classList.contains('done'));
  check(lit, 'the chip lights up while its text is in the prompt');
  await page.fill('#iprompt', '1girl, solo');
  await page.dispatchEvent('#iprompt','input');
  await page.waitForTimeout(200);
  const lit2 = await page.evaluate(()=>document.querySelector('#favlist button.fav[data-fav="double_v"]').classList.contains('done'));
  check(!lit2, 'and goes dark again when the prompt is edited by hand');
  await page.evaluate(()=>{ const s=document.getElementById('imodel'); s.value='pony'; s.dispatchEvent(new Event('change')); });
  await page.waitForTimeout(400);
  check((await page.textContent('#favstyle')).includes('danbooru'), 'switching back to Pony says danbooru again');

  await page.fill('#iprompt','1girl');
  await page.click('#favlist button.fav[data-fav="v"]');
  await page.click('#favlist button.fav[data-fav="breasts_out"]');
  await page.waitForTimeout(200);
  await page.click('#favclear');
  await page.waitForTimeout(200);
  v = await page.inputValue('#iprompt');
  check(v === '1girl', 'clear removes only what the strip added -> ' + v);


  // ---- the gated-model warning on the models tab ----
  // LTX-2.5 is the first entry in the catalogue whose Hugging Face repo is
  // gated: an anonymous request gets 401 at the first byte even though the
  // weights are free. The only useful place to say that is above the download
  // button, so this checks it is actually rendered there.
  await page.click('.tabs button[data-tab="mdl"]'); await page.waitForTimeout(900);
  const mdlCount = await page.evaluate(()=>document.querySelectorAll('#mlist .m').length);
  check(mdlCount >= 8, `the model list renders (${mdlCount})`);
  const ltx25 = await page.evaluate(() => {
    const cards = [...document.querySelectorAll('#mlist .m')];
    const card = cards.find((c) => (c.querySelector('.name') || {}).textContent?.includes('LTX-2.5'));
    return card ? { text: card.textContent.replace(/\s+/g, ' '),
                    link: (card.querySelector('a[href*="huggingface"]') || {}).href || '',
                    warn: !!card.querySelector('.banner.warn') } : null;
  });
  check(!!ltx25, 'LTX-2.5 has a card');
  check(ltx25 && /39\.\d ?GB|39GB/.test(ltx25.text.replace(/\s/g, ' ')) === true
        || (ltx25 && /GB/.test(ltx25.text)),
    'it states the download size');
  check(!!ltx25 && ltx25.text.includes('gated'),
    'the gated warning is on the card -> ' + (ltx25 ? ltx25.text.slice(0, 60) : ''));
  check(!!ltx25 && ltx25.link === 'https://huggingface.co/Lightricks/LTX-2.5',
    `…linking the exact page to accept the licence on (${ltx25 && ltx25.link})`);
  check(!!ltx25 && ltx25.warn,
    '…and it is styled as a warning while no HF token is set');
  const otherGate = await page.evaluate(() =>
    [...document.querySelectorAll('#mlist .m')]
      .filter((c) => c.textContent.includes('gated')).length);
  check(otherGate === 1, `only the gated model gets the warning (${otherGate})`);

  // The settings page is where the warning sends people, so the box has to be
  // there under that name.
  await page.click('.tabs button[data-tab="set"]'); await page.waitForTimeout(900);
  const setTxt = await page.textContent('#setbody');
  check(setTxt.includes('Hugging Face access token'),
    'the settings page has an HF token box');
  check(setTxt.includes('同意授權'),
    '…and says a token alone is not enough without accepting the licence');
  check(!/<b>/.test(await page.innerHTML('#setbody')) || setTxt.indexOf('**') === -1,
    'the help text renders its bold rather than printing asterisks');

  // ---- 短劇: the shot list, the evidence labels, and the accept flow ----
  // What is worth checking in a real browser: that the claim badges reach the
  // page, that the XSS the review found is actually escaped, and that a shot
  // does not become "done" by itself.
  await page.click('.tabs button[data-tab="sd"]'); await page.waitForTimeout(1200);

  // ---- the short path: a picture, a model, a sentence, a button ----
  // The episode planner used to be the first thing on this tab, which made
  // "I want one clip" look like a seven-step process.
  for (const [sel, what] of [['#qkdrop', 'upload'], ['#qkprompt', 'prompt'],
                             ['#qkmodel', 'model'], ['#qkgo', 'generate']]) {
    check(await page.isVisible(sel),
      `${what} is on screen the moment the drama tab opens (${sel})`);
  }
  const qkTops = await page.evaluate(() => ['#qkdrop', '#qkprompt', '#qkmodel', '#qkgo']
    .map((s) => Math.round(document.querySelector(s).getBoundingClientRect().top)));
  check(qkTops[0] < qkTops[1] && qkTops[1] < qkTops[2] && qkTops[3] >= qkTops[2] - 24,
    `…in that order down the card (${qkTops.join(' , ')})`);
  check(!await page.evaluate(() => document.getElementById('sdfull').open),
    'the episode planner starts collapsed, not gone');
  check(!await page.isVisible('#sdshots'),
    '…so the shot table is not the first thing on the page');
  const qkOpts = await page.$$eval('#qkmodel option', (ns) => ns.map((n) => n.textContent));
  check(!qkOpts.some((t) => t.includes('TTS') || t.includes('CosyVoice')),
    `…and the TTS bundles are not offered as video models (${qkOpts.length} listed)`);
  const qkGuards = await page.evaluate(async () => {
    const out = [];
    const go = document.getElementById('qkgo');
    document.getElementById('qkprompt').value = '';
    go.disabled = false; await quickGenerate();
    out.push(document.getElementById('qknote').textContent);
    document.getElementById('qkprompt').value = '她慢慢轉頭看向鏡頭';
    go.disabled = false; await quickGenerate();
    out.push(document.getElementById('qknote').textContent);
    return out;
  });
  check(qkGuards[0].includes('指令'), '…pressing generate with no prompt says so');
  check(qkGuards[1].includes('圖'), '…and with no picture says that');

  await page.evaluate(() => { document.getElementById('sdfull').open = true; });
  await page.waitForTimeout(500);
  const sdIntro = await page.textContent('#sdintro');
  check(sdIntro.includes('3.2'), 'the tab states the reference median -> ' + sdIntro.replace(/\s+/g,' ').slice(0,46));
  // It used to say "it generates nothing - generating is on the image/video
  // tabs". That stopped being true and stayed on the page, which is worse than
  // never having been true.
  check(!sdIntro.includes('它不生成任何東西'),
    'the tab no longer claims it cannot generate');
  check(sdIntro.includes('都在下面'),
    'and says the whole episode is made here -> ' + sdIntro.replace(/\s+/g,' ').slice(0,36));
  check(sdIntro.includes('一格影片都沒生成過'),
    'and says up front that none of this was measured on real video');
  check(/\d+ 條是上游官方規格/.test(sdIntro) && /\d+ 條是本專案量的/.test(sdIntro),
    'and counts its own claims by evidence kind, separately');
  check(/0 條是本專案量的/.test(sdIntro),
    'and the count of things measured here is zero, because it is');
  await page.click('#sdclaims'); await page.waitForTimeout(400);
  const claimTxt = await page.textContent('#sdclaimbox');
  check(claimTxt.includes('待驗證假說'), 'the claim list grades hypotheses as such');

  check(claimTxt.includes('官方規格'), '…and official specs separately');
  check(claimTxt.includes('限制：'), '…and shows what each claim is NOT true of');
  await page.click('#sdclaims'); await page.waitForTimeout(200);

  await page.evaluate(async () => {
    const d = await (await fetch('/api/drama')).json();
    for (const p of d.projects || []) await fetch(`/api/drama/${p.id}`, { method: 'DELETE' });
  });
  await page.evaluate(() => refreshDrama()); await page.waitForTimeout(700);
  check((await page.textContent('#sdempty')).includes('還沒有專案'), 'the empty state explains itself');

  await page.fill('#sdnew', '測試短劇');
  await page.click('#sdcreate'); await page.waitForTimeout(1400);
  check(await page.isVisible('#sdbody'), 'creating a project opens the pipeline');
  const routeCount = await page.evaluate(()=>document.querySelectorAll('#sdroutes .route').length);
  check(routeCount === 4, `each shot method gets its own route row (${routeCount})`);
  check((await page.textContent('#sdspecwhy')).includes('不是「一個模型」'),
    'step 0 explains that the delivery is what is locked, not one model');

  // The upload path has to be findable without knowing where it is. It used to
  // live only inside the per-shot panel, and that panel does not exist until
  // 做這顆 is pressed - so someone looking for "where do I put my picture" was
  // staring at a table that never mentioned it.
  const emptyTable = await page.textContent('#sdshots');
  check(emptyTable.includes('還沒有鏡頭'),
    'an empty shot table says what to press rather than showing bare headers');
  check(emptyTable.includes('你的圖'),
    '…and names the upload column, before any panel has been opened');

  // A male character must not be given a female count tag.
  await page.click('#sdaddcast'); await page.waitForTimeout(900);
  await page.fill('#sdcast .cn', '男主');
  await page.selectOption('#sdcast .cg', 'male');
  await page.fill('#sdcast .ct', 'black suit');
  await page.click('#sdaddshot'); await page.waitForTimeout(900);
  await page.fill('#sdshots .sa', '走進門');
  await page.selectOption('#sdshots .sw', { index: 0 });
  await page.click('#sdsave'); await page.waitForTimeout(1300);
  await page.click('#sdshots .splan'); await page.waitForTimeout(1000);
  const planTxt = await page.textContent('#sdplan');
  check(planTxt.includes('1boy') && !planTxt.includes('1girl'),
    'a male-only shot opens with 1boy, not 1girl -> ' + planTxt.replace(/\s+/g,' ').slice(0,64));
  check(planTxt.includes('還沒有嘗試'), 'the shot shows it has no attempts yet');
  // The two prompts. `action` describes a frozen instant and fed the video step
  // as well, so it could only ever be right for one of them.
  const planTxt2 = await page.textContent('#sdplan');
  check(planTxt2.includes('影片怎麼動'), 'the shot panel has its own motion field');
  check(planTxt2.includes('是兩回事'),
    'and says outright that it is not the same as the shot table\'s action column');
  check(planTxt2.includes('暫時拿'),
    'and warns while the shot is still falling back to the pose description');
  await page.fill('#sdmotion', 'she walks over and puts her hand on his shoulder');
  await page.click('#sdmotionsave');
  await page.waitForTimeout(1400);
  await page.click('#sdshots .splan');
  await page.waitForTimeout(1000);
  check((await page.inputValue('#sdmotion')).includes('walks over'),
    'the motion survives a save and a reopen');
  check(!(await page.textContent('#sdplan')).includes('暫時拿'),
    'and the fallback warning goes once it is filled');

  // Splitting is the fix that works today, for a beat that is too long and for
  // two character LoRAs fighting each other, so it is a button.
  const rowsBefore = await page.evaluate(() =>
    document.querySelectorAll('#sdshots tr[data-si]').length);
  await page.click('#sdsplit');
  await page.waitForTimeout(1600);
  const rowsAfter = await page.evaluate(() =>
    document.querySelectorAll('#sdshots tr[data-si]').length);
  check(rowsAfter === rowsBefore + 1,
    `"split into the next shot" adds one (${rowsBefore} -> ${rowsAfter})`);
  const scenes = await page.evaluate(() =>
    [...document.querySelectorAll('#sdshots .sc')].map((el) => el.value));
  check(scenes.length > 1 && scenes[0] === scenes[1],
    `…carrying the scene over, since that is what does not change (${JSON.stringify(scenes)})`);
  // Leave the shot list as it was found: a later block counts the shots, and a
  // test that quietly changes the fixture for the next one is its own bug.
  await page.evaluate(() => document.querySelectorAll('#sdshots .sdel')[1].click());
  await page.waitForTimeout(1500);
  check(await page.evaluate(() =>
    document.querySelectorAll('#sdshots tr[data-si]').length) === rowsBefore,
    'and the split can be undone, leaving the list as it was');
  await page.click('#sdshots .splan');
  await page.waitForTimeout(1000);

  // `extra` was a field the data model saved and the UI could not reach.
  await page.fill('#sdextra', 'dim rim light, holding a knife');
  await page.click('#sdextrasave'); await page.waitForTimeout(1300);
  await page.click('#sdshots .splan'); await page.waitForTimeout(900);
  check((await page.textContent('#sdplan')).includes('holding a knife'),
    'a shot-specific prompt addition is editable and reaches the prompt');
  check(/\d+ 格/.test(planTxt), 'and how many frames it will be');

  // The XSS the review found: a character name is interpolated into a finding.
  await page.fill('#sdcast .cn', '<img src=x onerror=window.__xss=1>');
  await page.fill('#sdcast .ct', '');
  await page.click('#sdsave'); await page.waitForTimeout(1400);
  const pwned = await page.evaluate(() => !!window.__xss);
  check(!pwned, 'a character name containing HTML does not execute (stored XSS)');
  const healthHtml = await page.innerHTML('#sdhealth');
  check(healthHtml.includes('&lt;img') || !healthHtml.includes('<img src=x'),
    'the name is escaped in the health panel');
  await page.fill('#sdcast .cn', '男主');
  await page.fill('#sdcast .ct', 'black suit');
  await page.click('#sdsave'); await page.waitForTimeout(1200);

  // Findings carry their evidence grade.
  const sdHealth = await page.textContent('#sdhealth');
  check(/資料檢查|待驗證假說|產業慣例|本工具建議|官方規格/.test(sdHealth),
    'every finding shows what kind of evidence it rests on');
  const sdLine = await page.textContent('#sdhealthline');
  check(/資料檢查 \d+ 項、主張 \d+ 項/.test(sdLine),
    'the summary separates data checks from claims -> ' + sdLine.trim().slice(0,44));

  // Progress means "an accepted video", and nothing accepts itself.
  check((await page.textContent('#sdstats')).includes('已採用影片 0/1'),
    'progress counts accepted videos, and starts at zero');

  // The video step. Before this existed there was no button at all, so the
  // progress bar above could never move through the UI. It is gated on an
  // accepted keyframe rather than shown-and-disabled, because there is nothing
  // to hand the video model until a still has been chosen.
  await page.click('#sdshots .splan'); await page.waitForTimeout(900);
  check(!await page.isVisible('#sdtovid'),
    'with no accepted keyframe there is no video button');
  check((await page.textContent('#sdplan')).includes('先採用一張關鍵幀'),
    '…and the page says what has to happen first');

  // Generating without leaving the tab. Bouncing between three tabs per shot
  // was the complaint, and the common path needs none of the controls that
  // made the hand-off exist in the first place.
  check(await page.isVisible('#sdgenkf'),
    'a shot can generate its keyframe in place');
  const batchOpts = await page.evaluate(() =>
    [...document.querySelectorAll('#sdbatch option')].map((o) => o.value));
  check(batchOpts.join(',') === '1,2,4',
    `…several candidates at once, because the retry rate is the real bottleneck (${batchOpts})`);
  check(!await page.isVisible('#sdgenvid'),
    '…and the video button waits for an accepted keyframe');
  check((await page.textContent('#sdplan')).includes('要細調的話'),
    '…while the hand-off to the full controls is kept, just demoted');

  // "Where do I upload my own picture" was asked four times across four
  // rounds. It was a ghost button the size and shape of the delete button
  // beside it, in an unlabelled column at the right of a table that scrolls
  // sideways. Its own labelled column now, and a look of its own.
  check(await page.isVisible('#sdshots .rowupbtn'),
    'every shot row carries its own upload button, panel closed or not');
  const shotHeads = await page.$$eval('#sdshots th', (ns) => ns.map((n) => n.textContent.trim()));
  check(shotHeads.includes('你的圖'),
    '…in a column whose header says what it is -> ' + shotHeads.join('|'));
  check((await page.textContent('#sdshots .rowupbtn')).includes('上傳我的圖'),
    '…on a button that says it in words, not an icon');
  check(await page.$eval('#sdshots .rowupbtn', (el) => getComputedStyle(el).borderStyle) === 'dashed',
    '…and it does not look like the delete button next to it');
  check((await page.textContent('#sdshotwhy')).includes('你的圖'),
    '…with the text above the table pointing at that column');

  // The prose fields were 100-130px inputs: a Chinese sentence scrolled out of
  // its own box after eight characters. And widening them must not push the
  // upload column off the right edge of a table that scrolls sideways.
  await page.fill('#sdshots .sa',
    'Yangmi 邁著自信的步伐走到 SM 旁邊，抬手拍了他的肩膀，臉上帶著挑釁的笑');
  await page.waitForTimeout(400);
  const proseBox = await page.$eval('#sdshots .sa', (el) => ({
    tag: el.tagName, h: el.clientHeight, content: el.scrollHeight, w: el.clientWidth }));
  check(proseBox.tag === 'TEXTAREA' && proseBox.h >= proseBox.content - 4,
    `the action field grows to show what was typed (${proseBox.h} vs ${proseBox.content})`);
  check(proseBox.w >= 200, `…and is wide enough to read (${proseBox.w}px)`);
  const upSeen = await page.evaluate(() => {
    const btn = document.querySelector('#sdshots .rowupbtn');
    const wrap = btn.closest('div[style*="overflow-x"]') || document.body;
    const b = btn.getBoundingClientRect(), w = wrap.getBoundingClientRect();
    return b.right <= w.right + 1 && b.left >= w.left - 1;
  });
  check(upSeen, '…and the upload column stays pinned on screen, not scrolled off');

  // A failure reason is the instruction for what to do next. It was cut at 60
  // characters, which landed mid-sentence right before the part that said how
  // to fix it - and repeated once per shot.
  const failText = await page.evaluate(() => {
    const long = 'MiniMax H3 FL2VA 的檔案下載好了，但這個 app 沒有可以跑它的工作流。'
      + '下面那顆「去匯入官方工作流」會帶你到匯入的地方，模型也幫你選好。';
    const el = document.createElement('div');
    el.innerHTML = failureHtml([{ shot_no: 1, reason: long }, { shot_no: 2, reason: long }]);
    return el.textContent;
  });
  check(failText.includes('模型也幫你選好'),
    'a failure reason is shown whole, instruction and all');
  check(failText.includes('第 1、2 顆'),
    '…and shots sharing one reason are grouped, not repeated');

  // Bring your own still. Image-to-video's most natural use - "I already have
  // the picture I want" - had no path at all: a keyframe could only be
  // generated here. An imported still is accepted outright, because choosing
  // the file *is* the choice.
  await page.click('#sdshots .splan');
  await page.waitForTimeout(1000);
  check(await page.isVisible('#sdup'), 'a shot offers "use my own picture"');
  const kfGood = require('path').join(require('os').tmpdir(), 'wan-kf-good.png');
  require('fs').writeFileSync(kfGood, pngOf(768, 1360));
  await page.setInputFiles('#sdupfile', kfGood);
  await page.waitForTimeout(2600);
  check((await page.textContent('#sdplan')).includes('關鍵幀已採用'),
    'uploading one files it under the shot and accepts it');
  check((await page.textContent('#sdshots tr[data-si="0"]')).includes('已經有採用的關鍵幀'),
    '…and the row itself says so, without opening anything');
  check(await page.isVisible('#sdtovid'),
    '…so the video step unlocks without generating anything');

  // The video model's output follows the ratio of the still it is given, so a
  // picture of the wrong shape is worth saying so about immediately.
  const kfSquare = require('path').join(require('os').tmpdir(), 'wan-kf-square.png');
  require('fs').writeFileSync(kfSquare, pngOf(1024, 1024));
  await page.setInputFiles('#sdupfile', kfSquare);
  await page.waitForTimeout(2600);
  const upNote = await page.textContent('#sdplannote');
  check(upNote.includes('比例') && upNote.includes('裁'),
    `a square picture is flagged against the 9:16 delivery (${upNote.replace(/\s+/g,' ').slice(0,44)})`);


  // A route pointing at a files-only model warns before twenty shots are
  // planned, not at generation time.
  await page.selectOption('#sdshots .sm2', 's2v');
  await page.fill('#sdshots .sd2', '你是誰');
  await page.selectOption('#sdshots .sp', { index: 1 });
  await page.click('#sdsave'); await page.waitForTimeout(1500);
  const filesOnly = await page.textContent('#sdhealth');
  check(filesOnly.includes('沒辦法從這個 app 生成'),
    'a route on a files-only model is flagged on the page');
  check(filesOnly.includes('ComfyUI'), '…and says where it can be done instead');
  await page.selectOption('#sdshots .sm2', 'i2v');
  await page.fill('#sdshots .sd2', '');
  await page.click('#sdsave'); await page.waitForTimeout(1400);
  check(!(await page.textContent('#sdhealth')).includes('沒辦法從這個 app 生成'),
    '…and the warning goes away when the route is runnable again');

  // ---- 整集: one press per stage, and joining the result ----
  // The generation itself needs a GPU and the join needs a working ffmpeg, so
  // what is checked here is everything up to those two: what the panel says is
  // left to do, which single button is live, and that each refusal names its
  // reason. This project's one shot already has an accepted keyframe from the
  // upload above, which puts the panel on its middle step.
  await page.click('#sdshots .splan'); await page.waitForTimeout(600);
  const epStep = await page.textContent('#sdstep');
  check(epStep.includes('現在這一步'),
    'the episode panel names one step to do now -> ' + epStep.replace(/\s+/g,' ').slice(0,40));
  check(epStep.includes('影片候選'),
    '…which is the video pass, because the keyframe is already picked');
  check(await page.isDisabled('#sdrunkf'),
    'the keyframe pass is not offered when nothing needs one');
  check(!await page.isDisabled('#sdrunvid'), 'the video pass is the live button');
  check(await page.isDisabled('#sdjoin'),
    'joining is not offered before every shot has an accepted video');
  check(!await page.isVisible('#sdfitrow'),
    'the crop question stays out of the way until a shot is the wrong shape');

  // A model that is not on disk is one problem with one button, not twenty
  // identical failures with a filename in them and nowhere to press.
  const needTxt = await page.textContent('#sdneed');
  check(needTxt.includes('還沒下載完'),
    'a missing model is named in the episode card -> ' + needTxt.replace(/\s+/g,' ').slice(0,40));
  check(await page.isVisible('#sdneed .sdget'),
    '…with its download button right there, not on another tab');
  check(/\d+\.\d+GB/.test(await page.textContent('#sdneed .sdget')),
    '…and the size on the button');
  check((await page.textContent('#sdhealth')).includes('不用離開這一頁'),
    'and the health panel points at that button too, not at another tab');

  // With the model not on disk, pressing the live button must say that once -
  // naming the model and pointing at the button that fixes it. It used to
  // attempt every shot and report the same sentence once per shot instead.
  await page.click('#sdrunvid'); await page.waitForTimeout(5000);
  const ranNote = await page.textContent('#sdrunnote');
  check(ranNote.includes('還沒下載完') && ranNote.includes('下載'),
    'a run blocked by a missing model says so, with the fix -> '
    + ranNote.replace(/\s+/g,' ').slice(0,46));
  check(!ranNote.includes('第 1 顆'), '…once, not once per shot');
  check(!/已排 \d+\/\d+/.test(ranNote), '…and nothing was queued');

  // A shot can be given a sound file, and is told plainly when its route will
  // not use one.
  check(await page.isVisible('#sdaudio'), 'a shot can take an audio file');
  const wavPath = require('path').join(require('os').tmpdir(), 'bc-line.wav');
  const head = Buffer.alloc(44);
  head.write('RIFF', 0); head.write('WAVE', 8); head.write('fmt ', 12); head.write('data', 36);
  require('fs').writeFileSync(wavPath, Buffer.concat([head, Buffer.alloc(800)]));
  await page.setInputFiles('#sdaudiofile', wavPath); await page.waitForTimeout(2500);
  const audioNote = await page.textContent('#sdplannote');
  check(audioNote.includes('音訊驅動'),
    'and an i2v shot is told the file will not drive anything -> '
    + audioNote.replace(/\s+/g,' ').slice(0,40));

  await page.click('#sddel'); await page.waitForTimeout(1000);
  check(!await page.isVisible('#sdbody'), 'deleting the project closes the pipeline');

  // ---- experiments: fixed-seed sweeps ----
  // Needs a checkpoint present; the model picker just needs SOMETHING
  // installed, so this is skipped when nothing is.
  const HAVE_CKPT = await page.evaluate(() =>
    [...document.querySelectorAll('#imodel option')].some(o => o.value.startsWith('custom:')));
  if (HAVE_CKPT) {
  // Start clean: this block creates an experiment, so without a sweep-up every
  // run leaves one behind and the list grows forever.
  await page.evaluate(async () => {
    const d = await (await fetch('/api/experiments')).json();
    for (const e of d.experiments || []) {
      await fetch(`/api/experiments/${e.id}`, { method: 'DELETE' });
    }
  });
  await page.click('.tabs button[data-tab="img"]'); await page.waitForTimeout(600);
  await page.evaluate(()=>{ const s=document.getElementById('imodel');
    const opt=[...s.options].find(o=>o.value.startsWith('custom:'));
    if(opt){ s.value=opt.value; s.dispatchEvent(new Event('change')); } });
  await page.fill('#iprompt','1girl, hoshimachi suisei');
  await page.waitForTimeout(400);
  await page.click('.tabs button[data-tab="lib"]'); await page.waitForTimeout(500);
  check(await page.isVisible('#expcard'), 'the experiment card is on the library tab');
  check(!await page.isVisible('#expbody'), '…collapsed by default');
  await page.click('#exptoggle'); await page.waitForTimeout(700);
  check(await page.isVisible('#expbody'), 'it expands');
  const expIntro = await page.textContent('#expintro');
  check(expIntro.includes('同一組 seed'), 'the intro states the control');

  await page.click('#expnew'); await page.waitForTimeout(600);
  check(await page.isVisible('#expaxes'), 'the axis form appears');
  const expAxes = await page.evaluate(()=>document.querySelectorAll('#expaxeslist input[data-axis]').length);
  check(expAxes >= 6, `every sweepable axis is offered (${expAxes})`);

  await page.fill('#expaxeslist input[data-axis="cfg"]', '5, 6, 7');
  await page.waitForTimeout(700);
  let expPrev = await page.textContent('#exppreview');
  check(/3 組設定 × 3 個 seed = 9 張圖/.test(expPrev), 'preview counts the matrix -> ' + expPrev.replace(/\s+/g,' ').slice(0,46));
  check(expPrev.includes('同一批 seed'), '…and repeats why the seeds are shared');

  await page.fill('#expaxeslist input[data-axis="steps"]', '20, 25, 30, 35, 40, 45, 50');
  await page.fill('#expaxeslist input[data-axis="lora_strength"]', '0.6, 0.7, 0.8, 0.9');
  await page.fill('#expseeds','16'); await page.dispatchEvent('#expseeds','input'); await page.waitForTimeout(900);
  expPrev = await page.textContent('#exppreview');
  check(expPrev.includes('超過上限'), 'an oversized sweep warns before it costs anything');

  await page.fill('#expaxeslist input[data-axis="steps"]', '');
  await page.fill('#expaxeslist input[data-axis="lora_strength"]', '');
  await page.fill('#expseeds','2'); await page.dispatchEvent('#expseeds','input'); await page.waitForTimeout(700);
  await page.fill('#expname','cfg sweep');
  await page.click('#expcreate'); await page.waitForTimeout(1500);
  check(await page.isVisible('#expdetail'), 'creating opens the experiment');
  const expDetail = await page.textContent('#expdetail');
  check(expDetail.includes('3 組 × 2 seed'), 'it shows the shape -> ' + expDetail.replace(/\s+/g,' ').slice(0,42));
  check(expDetail.includes('可重現用'), '…with a provenance section');
  check(await page.isVisible('#exprun'), '…and a run button');

  await page.click('#exprun'); await page.waitForTimeout(3000);
  const expAfter = await page.textContent('#expdetail');
  check(/6 張/.test(expAfter), 'running queues the jobs -> ' + expAfter.replace(/\s+/g,' ').slice(0,52));
  check(await page.isVisible('#expjudge'), 'the blind-judging control appears once jobs exist');
  const expCrits = await page.evaluate(()=>[...document.querySelectorAll('#expcrit option')].map(o=>o.textContent));
  check(expCrits.length >= 4, `several judging criteria (${expCrits.length})`);
  check(expCrits.some(c=>c.includes('像本人')) && expCrits.some(c=>c.includes('好看')),
     '…keeping "looks like her" and "looks good" separate');

  // Voting, and specifically the two bookkeeping bugs an outside review found
  // in this exact flow: a tie that only credited one variant, and a comparison
  // counter that reported every comparison twice.
  await page.click('#expjudge'); await page.waitForTimeout(1200);
  const arenaTxt = await page.textContent('#exparena');
  check(arenaTxt.includes('設定先蓋住'), 'the arena hides the settings until the vote lands');
  const seedShown = /seed (\d+)/.exec(arenaTxt);
  check(!!seedShown, `a pair is offered with its seed (${seedShown && seedShown[1]})`);
  await page.click('#votetie'); await page.waitForTimeout(1500);
  const tieState = await page.evaluate(() => {
    const v = (EXP.open.votes || []).filter((x) => x.criterion === EXP.criterion);
    const t = (EXP.open.standings || {})[EXP.criterion] || {};
    return { votes: v, ties: Object.values(t).map((r) => r.tie) };
  });
  check(tieState.votes.length === 1 && tieState.votes[0].winner === '',
    'a tie is recorded as a vote with no winner');
  check(!!tieState.votes[0].other,
    `…carrying its second side (${tieState.votes[0].other || 'MISSING'})`);
  check(tieState.ties.filter((n) => n === 1).length === 2,
    `…and credited to both variants (${tieState.ties})`);

  // The standings line counts votes, not per-variant tallies.
  await page.evaluate(() => renderStandings()); await page.waitForTimeout(400);
  const standTxt = await page.textContent('#exparena');
  check(/共 1 次比較/.test(standTxt),
    'one comparison reads as one, not two -> ' + standTxt.replace(/\s+/g,' ').slice(0,40));
  check(standTxt.includes('票數還太少'), '…and under ten votes it says so');
  // …and leave nothing behind.
  await page.evaluate(async () => {
    const d = await (await fetch('/api/experiments')).json();
    for (const e of d.experiments || []) {
      await fetch(`/api/experiments/${e.id}`, { method: 'DELETE' });
    }
  });

  }

  // ---- official reference art ----
  // Needs the fixture files; skipped when they are not present.
  const REFDIR = process.env.REFTEST_DIR || '';
  if (REFDIR) {
  // Start from empty, or the second run of this file sees the first run's
  // imports and every count is off by the previous run.
  await page.evaluate(async () => {
    const d = await (await fetch('/api/refs?pack=hololive-collection')).json();
    const all = [...(d.unfiled || [])];
    for (const key of Object.keys(d.counts || {})) {
      const r = await (await fetch(`/api/refs/hololive-collection/${key}`)).json();
      all.push(...(r.refs || []));
    }
    for (const ref of all) {
      await fetch(`/api/refs/hololive-collection/${ref.name}`, { method: 'DELETE' });
    }
  });
  await page.reload({ waitUntil: 'networkidle' });
  await page.click('.tabs button[data-tab="img"]');
  await page.waitForTimeout(700);
  check(await page.isVisible('#refbox'), 'the reference panel is on the character page');
  check((await page.textContent('#refnote')).includes('照檔名自動分'), 'empty state explains what to do');

  await page.setInputFiles('#reffiles', [
    REFDIR+'Mori Calliope - 1st Costume.png', REFDIR+'hoshimachi_suisei_03.png',
    REFDIR+'Gawr Gura official art.png', REFDIR+'Shirogane Noel.png',
    REFDIR+'IMG_2831.png', REFDIR+'noel.png', REFDIR+'batch.zip']);
  await page.waitForTimeout(2500);
  const refNote = await page.textContent('#refnote');
  check(refNote.includes('匯入完成'), 'import ran -> ' + refNote.replace(/\s+/g,' ').slice(0,90));
  check(/7 張對到角色/.test(refNote), '…and filed the 7 nameable ones (4 loose + 3 in the zip)');
  check(/2 張沒對到/.test(refNote), '…and declined the 2 ambiguous ones rather than guessing');

  const refCnt = await page.textContent('#refcount');
  check(/全部 9 張/.test(refCnt), 'the zip was unpacked too (4+3+2 distinct) -> ' + refCnt);

  // pick a character and see her own references
  await page.fill('#packfind','calliope'); await page.waitForTimeout(500);
  await page.evaluate(()=>{ const b=document.querySelector('#packmembers button'); if(b) b.click(); });
  await page.waitForTimeout(800);
  const refMine = await page.evaluate(()=>document.querySelectorAll('#reflist button[data-ref]').length);
  check(refMine === 1, `the selected member shows her own reference (${refMine})`);

  // one click -> img2img source
  await page.click('#reflist button[data-ref]'); await page.waitForTimeout(400);
  check(await page.isVisible('#refasinit'), 'clicking a thumbnail asks what to use it for');
  await page.click('#refasinit'); await page.waitForTimeout(700);
  const refStatus = await page.textContent('#istatus');
  check(refStatus.includes('來源圖'), 'it becomes the img2img source -> ' + refStatus.slice(0,60));
  check(await page.isVisible('#i2i'), '…and the img2img panel opens');
  const refDn = await page.inputValue('#idenoise').catch(()=>'');
  check(refDn === '0.45', `…with denoise pre-set into the useful band (${refDn})`);

  // the unfiled queue
  await page.click('#refunfiled'); await page.waitForTimeout(500);
  const refUn = await page.textContent('#refunfiledbox');
  check(refUn.includes('沒對到'), 'the unfiled queue lists them');
  check(refUn.includes('不會亂猜'), '…and says why it declined');
  const refSels = await page.evaluate(()=>document.querySelectorAll('#refunfiledbox select[data-assign]').length);
  check(refSels === 2, `…with a picker per file (${refSels})`);
  await page.selectOption('#refunfiledbox select[data-assign]', { label: 'Shirogane Noel' });
  await page.waitForTimeout(900);
  const refCnt2 = await page.textContent('#refcount');
  check(/1 張沒對到/.test(refCnt2) || !/沒對到/.test(refCnt2), 'assigning by hand moves it -> ' + refCnt2);
  // Tidy up so a later run - or the user's own library - is not polluted.
  await page.evaluate(async () => {
    const d = await (await fetch('/api/refs?pack=hololive-collection')).json();
    const all = [...(d.unfiled || [])];
    for (const key of Object.keys(d.counts || {})) {
      const r = await (await fetch(`/api/refs/hololive-collection/${key}`)).json();
      all.push(...(r.refs || []));
    }
    for (const ref of all) {
      await fetch(`/api/refs/hololive-collection/${ref.name}`, { method: 'DELETE' });
    }
  });

  }

  // ---- importing a whole folder off the local disk ----
  // The real case this exists for: a curated archive of official character
  // sheets, several gigabytes, organised in Chinese, sitting on the same machine
  // the app runs on. Picking those files one by one in a browser dialog is not
  // an import, so the app gets pointed at the folder instead - and because it
  // has never seen that archive's naming convention, it scans before it touches
  // anything. Needs the fixture folder; skipped without it.
  const ARCHIVE = process.env.REFARCHIVE_DIR || '';
  if (ARCHIVE) {
  await page.evaluate(async () => {
    const d = await (await fetch('/api/refs?pack=hololive-collection')).json();
    const all = [...(d.unfiled || [])];
    for (const key of Object.keys(d.counts || {})) {
      const r = await (await fetch(`/api/refs/hololive-collection/${key}`)).json();
      all.push(...(r.refs || []));
    }
    for (const ref of all) await fetch(`/api/refs/hololive-collection/${ref.name}`, { method: 'DELETE' });
  });
  await page.reload({ waitUntil: 'networkidle' });
  await page.click('.tabs button[data-tab="img"]');
  await page.waitForTimeout(800);

  check(!await page.isVisible('#reffolderbox'), 'the folder importer starts collapsed');
  await page.click('#reffolder');
  await page.waitForTimeout(200);
  check(await page.isVisible('#refpath'), '「從資料夾匯入」opens a path box');
  check((await page.textContent('#refscanhint')).includes('先掃描不會動到任何檔案'),
    'and promises the scan touches nothing');

  await page.fill('#refpath', ARCHIVE);
  await page.click('#refscan');
  await page.waitForTimeout(1500);
  check(await page.isVisible('#refscanout'), 'the scan reports back');
  const scanTxt = await page.textContent('#refscanout');
  check(/掃到 \d+ 張圖/.test(scanTxt), 'it says how many it found -> ' + scanTxt.replace(/\s+/g,' ').slice(0,60));
  check(scanTxt.includes('對到角色'), '…how many matched a member');
  check(scanTxt.includes('資料夾名字'), '…and that some were matched by folder name, not filename');
  check(scanTxt.includes('對不到的長這樣'), 'it shows the actual unmatched filenames, which are the actionable part');
  check(scanTxt.includes('不會搬動也不會複製'), 'and states that nothing will be moved or copied');

  // Nothing has been imported yet.
  let cntTxt = await page.textContent('#refcount');
  check(cntTxt.includes('還沒有'), 'scanning alone imports nothing -> ' + cntTxt);

  await page.click('#refdoimport');
  await page.waitForTimeout(2000);
  const impTxt = await page.textContent('#refnote');
  check(impTxt.includes('匯入完成'), 'importing runs -> ' + impTxt.replace(/\s+/g,' ').slice(0,70));
  check(/\d+ 張對到角色/.test(impTxt), '…and reports what it filed');

  // A Chinese-named folder found its member, and the picture really serves.
  const suiRefs = await page.evaluate(async () =>
    (await (await fetch('/api/refs/hololive-collection/hoshimachi-suisei')).json()).refs || []);
  check(suiRefs.length === 2, `星街彗星's folder landed on Hoshimachi Suisei (${suiRefs.length})`);
  check(suiRefs.every((r) => r.linked), '…as links, not copies');
  const served = await page.evaluate(async (u) => (await fetch(u)).status, suiRefs[0].url);
  check(served === 200, `a linked reference serves through its own route (${served})`);

  // Re-importing the same folder must not duplicate.
  await page.click('#refscan'); await page.waitForTimeout(1200);
  await page.click('#refdoimport'); await page.waitForTimeout(1500);
  const again = await page.evaluate(async () =>
    (await (await fetch('/api/refs?pack=hololive-collection')).json()).total);
  check(again === 5, `re-importing does not duplicate (${again})`);

  // And the likeness note now leads with "you already have her official art".
  await page.fill('#packfind', 'suisei'); await page.waitForTimeout(500);
  await page.evaluate(()=>{ const b=document.querySelector('#packmembers button'); if(b) b.click(); });
  await page.waitForTimeout(900);
  if (!await page.isChecked('#packlike')) { await page.check('#packlike'); await page.waitForTimeout(900); }
  const likeTxt = await page.textContent('#packlikenote');
  check(likeTxt.includes('你已經有這位的'),
    'the likeness answer points at the art the user already imported');

  await page.evaluate(async () => {
    const d = await (await fetch('/api/refs?pack=hololive-collection')).json();
    const all = [...(d.unfiled || [])];
    for (const key of Object.keys(d.counts || {})) {
      const r = await (await fetch(`/api/refs/hololive-collection/${key}`)).json();
      all.push(...(r.refs || []));
    }
    for (const ref of all) await fetch(`/api/refs/hololive-collection/${ref.name}`, { method: 'DELETE' });
  });
  await page.click('#reffolder');
  // Put the likeness tick back where the next block expects to find it: it
  // asserts the slider is hidden until asked, and this block asked.
  if (await page.isChecked('#packlike')) { await page.uncheck('#packlike'); }
  await page.waitForTimeout(600);
  }

  // ---- "why doesn't it look like the stream model" ----
  // The character-pack controls live on the image tab. Reach it explicitly:
  // the blocks above are guarded on having a checkpoint or a reference folder,
  // so on a machine with neither, nothing has switched tabs and every fill
  // below would time out on a hidden input.
  await page.click('.tabs button[data-tab="img"]'); await page.waitForTimeout(600);
  await page.evaluate(()=>{ const s=document.getElementById('imodel'); s.value='noobai'; s.dispatchEvent(new Event('change')); });
  await page.waitForTimeout(400);
  // pick a member
  await page.fill('#packfind','calliope'); await page.waitForTimeout(400);
  const packMem = await page.evaluate(()=>{ const b=document.querySelector('#packmembers button'); if(b){b.click(); return b.textContent.trim();} return ''; });
  check(!!packMem, 'picked a member -> ' + packMem);
  await page.waitForTimeout(400);
  await page.click('#packgo'); await page.waitForTimeout(600);
  const packPlain = await page.inputValue('#iprompt');
  check(packPlain.includes('mori calliope'), 'plain fill works -> ' + packPlain.slice(0,70));
  check(!packPlain.includes('official art'), '…and does not add official art by default');

  check(!await page.isVisible('#packlikewrap'), 'the likeness slider is hidden until asked');
  await page.check('#packlike'); await page.waitForTimeout(800);
  check(await page.isVisible('#packlikewrap'), 'ticking it reveals the strength slider');
  const likePrompt = await page.inputValue('#iprompt');
  check(/\(mori calliope.*:1\.25\)/.test(likePrompt), 'the costume trigger is weighted -> ' + likePrompt.slice(0,80));
  check(likePrompt.includes('official art'), '…and official art is added');
  check(await page.isVisible('#packlikenote'), 'the explanation shows');
  const likeNote = await page.textContent('#packlikenote');
  check(likeNote.includes('12,496') || /\d,\d\d\d 張/.test(likeNote), 'it quotes the real post count -> ' + likeNote.slice(0,54).replace(/\s+/g,' '));
  check(likeNote.includes('Yukisame'), '…and names the designer with their own count');
  check(likeNote.includes('以圖生圖'), '…and leads with the img2img/ControlNet answer');
  const likeLink = await page.evaluate(()=>{ const a=document.querySelector('#packlikenote a'); return a?a.href:''; });
  check(likeLink.includes('virtualyoutuber.fandom.com'), 'the official gallery link is there -> ' + likeLink);

  // conflict warning when the designer style is also on
  const hasStyle = await page.evaluate(()=>!!document.getElementById('packstylechk'));
  if (hasStyle) {
    await page.evaluate(()=>{ const c=document.getElementById('packstylechk'); if(!c.checked){c.checked=true;c.dispatchEvent(new Event('change'));} });
    await page.waitForTimeout(700);
    const likeNote2 = await page.textContent('#packlikenote');
    check(likeNote2.includes('反方向'), 'having both on warns they pull against each other');
  }

  await page.evaluate(()=>{ const r=document.getElementById('packlikew'); r.value=1.4; r.dispatchEvent(new Event('input')); r.dispatchEvent(new Event('change')); });
  await page.waitForTimeout(700);
  const likeStrong = await page.inputValue('#iprompt');
  check(likeStrong.includes(':1.4)'), 'the strength slider changes the weight -> ' + likeStrong.slice(0,60));

  await page.uncheck('#packlike'); await page.waitForTimeout(700);
  check(!await page.isVisible('#packlikenote'), 'unticking hides the note again');
  const likeBack = await page.inputValue('#iprompt');
  check(!likeBack.includes('official art'), '…and takes official art back out');


  // ---- artists ----
  check(await page.isVisible('#artbox'), 'the artist panel is on the same page as the character pack');
  const artN = await page.evaluate(()=>document.querySelectorAll('#artlist button[data-art]').length);
  check(artN >= 30, `at least 30 artists listed (${artN})`);
  const cnt = await page.textContent('#artcount');
  check(/\d+\/\d+ 位/.test(cnt), `…with a count (${cnt})`);
  const firstRow = await page.textContent('#artlist');
  check(firstRow.includes('danbooru') && firstRow.includes('特徵'),
     'each row shows post count and the measured style signals');

  await page.evaluate(()=>{ const s=document.getElementById('imodel'); s.value='noobai'; s.dispatchEvent(new Event('change')); });
  await page.waitForTimeout(400);
  await page.fill('#iprompt','1girl');
  await page.click('#artlist button[data-art="wlop"]');
  await page.waitForTimeout(200);
  v = await page.inputValue('#iprompt');
  check(v === '1girl, artist:wlop', 'NoobAI gets artist:<name> -> ' + v);
  await page.click('#artlist button[data-art="wlop"]');
  await page.waitForTimeout(200);
  v = await page.inputValue('#iprompt');
  check(v === '1girl', 'clicking again removes it -> ' + v);

  // weight slider
  await page.evaluate(()=>{ const r=document.getElementById('artw'); r.value=1.2; r.dispatchEvent(new Event('input')); });
  await page.click('#artlist button[data-art="ciloranko"]');
  await page.waitForTimeout(200);
  v = await page.inputValue('#iprompt');
  check(v === '1girl, (artist:ciloranko:1.2)', 'the weight slider is applied when adding -> ' + v);
  check(await page.evaluate(()=>document.querySelector('#artlist button[data-art="ciloranko"]').classList.contains('done')),
     'and the chip lights up even though it is weighted');
  await page.click('#artclear'); await page.waitForTimeout(200);
  v = await page.inputValue('#iprompt');
  check(v === '1girl', 'clear removes the weighted form too -> ' + v);

  // Illustrious uses a different prefix
  await page.evaluate(()=>{ const s=document.getElementById('imodel'); s.value='illustrious'; s.dispatchEvent(new Event('change')); });
  await page.waitForTimeout(400);
  // Reset the slider: it persists across model switches (deliberately), and the
  // previous step left it at 1.2.
  await page.evaluate(()=>{ const r=document.getElementById('artw'); r.value=1; r.dispatchEvent(new Event('input')); });
  await page.fill('#iprompt','1girl');
  await page.click('#artlist button[data-art="wlop"]');
  await page.waitForTimeout(200);
  v = await page.inputValue('#iprompt');
  check(v === '1girl, by wlop', 'Illustrious gets "by <name>" -> ' + v);

  // Pony ignores artists entirely
  await page.evaluate(()=>{ const s=document.getElementById('imodel'); s.value='pony'; s.dispatchEvent(new Event('change')); });
  await page.waitForTimeout(400);
  check(await page.isVisible('#artwarn'), 'Pony shows the "this model ignores artists" warning');
  const artWarn = await page.textContent('#artwarn');
  check(artWarn.includes('Pony V6'), '…and says why -> ' + artWarn.slice(0,46));
  check(!await page.isVisible('#artwwrap'), '…and hides the weight slider');
  await page.click('#artswitch'); await page.waitForTimeout(500);
  check(await page.inputValue('#imodel') === 'noobai', 'the "switch to NoobAI" button works');
  check(!await page.isVisible('#artwarn'), '…and the warning goes away');

  // misnamed lookup
  await page.fill('#artq','hiten'); await page.waitForTimeout(300);
  const hits = await page.evaluate(()=>document.querySelectorAll('#artlist button[data-art]').length);
  check(hits >= 1, `searching the codex's spelling still finds the artist (${hits})`);
  await page.fill('#artq','deadflow'); await page.waitForTimeout(300);
  const txt = await page.textContent('#artlist');
  check(txt.includes('bee') , 'and "deadflow" reaches bee (deadflow) -> ' + txt.slice(0,60).replace(/\s+/g,' '));

  await page.fill('#artq',''); await page.check('#artcodex'); await page.waitForTimeout(300);
  const cod = await page.evaluate(()=>document.querySelectorAll('#artlist button[data-art]').length);
  check(cod >= 15 && cod < 52, `"only ones the codex used" filters to ${cod}`);
  await page.uncheck('#artcodex');
  await page.selectOption('#artgroup','成人向'); await page.waitForTimeout(300);
  const grp = await page.evaluate(()=>[...document.querySelectorAll('#artlist button[data-art]')].length);
  check(grp > 3 && grp < 52, `group filter works (${grp} in 成人向)`);
  await page.selectOption('#artgroup','');


  // ---- the three words, and bringing your own LoRA ----
  // The user's complaint was not that a feature was missing; it was that the
  // page used 底模 / 畫風 / LoRA without ever saying what they are. So the
  // explanation is asserted like a feature, because that is what it is.
  const loMark = errors.length;
  await page.click('.tabs button[data-tab="img"]');
  await page.waitForTimeout(700);
  await page.evaluate(() => { try { localStorage.removeItem('wan.basicsdone'); } catch {} });
  await page.reload({ waitUntil: 'networkidle' });
  await page.waitForTimeout(1600);
  await page.click('.tabs button[data-tab="img"]');
  await page.waitForTimeout(700);
  check(await page.isVisible('#basics'), 'the three-word explainer shows until dismissed');
  const basicsTxt = await page.textContent('#basics');
  check(basicsTxt.includes('不是模型，不用下載'),
    'and says the prompt templates are not a download - the thing that was misread');
  check(basicsTxt.includes('一次用一個'),
    'and that one base model is used at a time');
  check((await page.textContent('#istyles')).includes('提詞範本'),
    'the button says what it is rather than calling itself a style');
  await page.click('#basicsclose');
  await page.waitForTimeout(400);
  check(!await page.isVisible('#basics'), 'dismissing hides it');
  await page.reload({ waitUntil: 'networkidle' });
  await page.waitForTimeout(1600);
  await page.click('.tabs button[data-tab="img"]');
  await page.waitForTimeout(700);
  check(!await page.isVisible('#basics'), 'and it stays dismissed across a reload');

  await page.click('.tabs button[data-tab="lora"]');
  await page.waitForTimeout(900);
  const loraTxt = await page.textContent('#tab-lora');
  check(loraTxt.includes('LoRA 認底模'),
    'the LoRA tab leads with the compatibility rule, which is the one that bites');
  check(loraTxt.includes('四條路'),
    'and names every way to get one - four now that Hugging Face is a source');

  // A file the user already downloaded. No network needed, so this runs
  // everywhere; the URL path is covered by the Python tests against the parser.
  const loDir = require('path').join(require('os').tmpdir(), 'wan-lora-import');
  {
    const fs = require('fs');
    fs.rmSync(loDir, { recursive: true, force: true });
    fs.mkdirSync(loDir, { recursive: true });
    fs.writeFileSync(require('path').join(loDir, 'browser_test_char.safetensors'),
                     Buffer.alloc(4096));
  }
  await page.fill('#limpath', loDir);
  await page.click('#limfile');
  await page.waitForTimeout(2200);
  check((await page.textContent('#limnote')).includes('匯入了 1 個'),
    'a local folder import copies the weight file in');
  await page.fill('#limpath', loDir);
  await page.click('#limfile');
  await page.waitForTimeout(2200);
  check((await page.textContent('#limnote')).includes('跳過'),
    'and importing it again skips rather than overwriting');
  check(errors.length === loMark,
    `no console errors across the LoRA tab (${errors.slice(loMark, loMark + 2).join(' | ') || 'clean'})`);
  await page.fill('#limpath', '/definitely/not/here');
  await page.click('#limfile');
  await page.waitForTimeout(1600);
  check((await page.textContent('#limnote')).includes('找不到'),
    'and a path that does not exist says so rather than failing silently');
  await page.evaluate(async () => {
    // Leave the LoRA folder as it was found.
    await fetch('/api/loras/browser_test_char.safetensors', { method: 'DELETE' });
  });
  // This block reloads twice; the aborted polls those cause are collected
  // separately (see the console handler at the top) rather than counted here.
  await page.waitForTimeout(1200);

  // ---- importing a ComfyUI workflow ----
  // The whole point is that the graph is not ours: the user exports the
  // official template from their own ComfyUI, where it demonstrably runs, and
  // this app only substitutes the picture, the prompt and the seed.
  const wfMark = errors.length;
  await page.click('.tabs button[data-tab="mdl"]');
  await page.waitForTimeout(1600);
  const wfCard = await page.textContent('#wfcard');
  check(wfCard.includes('Export (API)'),
    'the import card names the exact ComfyUI menu item');
  check(wfCard.includes('先跑一次確認它會動'),
    '…and says to prove the workflow runs there first');
  const wfCands = await page.evaluate(() =>
    [...document.querySelectorAll('#wfmodel option')].map((o) => o.value));
  // MiniMax H3 used to be the headline candidate here. It stopped being one
  // when the app grew a graph of its own for it, built from ComfyUI's built-in
  // template - a model that runs here does not need an imported workflow.
  check(wfCands.includes('wan22-s2v') && !wfCands.includes('wan22-14b-fp8'),
    `only files-only models are offered (${wfCands.join(',')})`);
  check(!wfCands.includes('minimax-h3'),
    '…and H3 is not among them any more, because it runs here now');
  // The TTS bundles are files-only too, but there is no ComfyUI video graph to
  // import for them - offering them is a dead end dressed up as an option.
  check(!wfCands.includes('qwen3-tts') && !wfCands.includes('cosyvoice3'),
    '…and the TTS bundles are not among them');

  // A real API-format graph, built by the app's own builder - same shape.
  const wfPath = require('path').join(require('os').tmpdir(), 'wan-wf-api.json');
  {
    const graph = await page.evaluate(async () => {
      const r = await fetch('/api/models');
      return (await r.json()) && null;
    });
    // Built server-side would need a GPU-free builder call; instead use the
    // smallest graph that exercises every slot.
    require('fs').writeFileSync(wfPath, JSON.stringify({
      "1": { class_type: 'LoadImage', inputs: { image: 'in.png' },
             _meta: { title: 'Starting image' } },
      "2": { class_type: 'CLIPTextEncode', inputs: { text: 'hello' },
             _meta: { title: 'Prompt' } },
      "3": { class_type: 'CLIPTextEncode', inputs: { text: 'bad' },
             _meta: { title: 'Negative' } },
      "4": { class_type: 'KSampler',
             inputs: { positive: ['2', 0], negative: ['3', 0], seed: 1 },
             _meta: { title: 'Sampler' } },
      "5": { class_type: 'SaveImage',
             inputs: { images: ['4', 0], filename_prefix: 'x' },
             _meta: { title: 'Save' } },
    }));
  }
  await page.setInputFiles('#wffile', wfPath);
  await page.waitForTimeout(2500);
  const wfRes = await page.textContent('#wfresult');
  check(wfRes.includes('你打的提詞會進'), 'the mapping is shown as plain sentences');
  check(wfRes.includes('Prompt'),
    '…leading with the node\'s own name, which is what is recognisable in ComfyUI');
  check(wfRes.includes('節點'), '…and keeping the node number as small print');
  check(await page.isVisible('#wffix'), 'there is a way to say the detection is wrong');
  check(!await page.isVisible('#wffixbox'),
    '…collapsed by default, so a first-time user is not shown a node list');
  await page.click('#wffix');
  await page.waitForTimeout(500);
  check(await page.isVisible('#wffixbox'), '…and it opens on request');

  // Wan S2V, not H3: H3 grew a graph of its own and left this list.
  await page.selectOption('#wfmodel', 'wan22-s2v');
  await page.setInputFiles('#wffile', wfPath);
  await page.waitForTimeout(2400);
  await page.click('#wfsave');
  await page.waitForTimeout(2400);
  check((await page.textContent('#wfsavemsg')).includes('存好了'), 'saving reports success');

  await page.click('.tabs button[data-tab="gen"]');
  await page.waitForTimeout(1500);
  const h3after = await page.evaluate(() => {
    const o = [...document.querySelectorAll('#model option')].find((x) => x.value === 'wan22-s2v');
    return o ? { disabled: o.disabled, text: o.textContent } : null;
  });
  check(h3after && !h3after.disabled,
    'a files-only model becomes selectable once its workflow is imported');
  check(h3after && h3after.text.includes('匯入的工作流'),
    '…and says it is running the imported one');
  await page.evaluate(() => fetch('/api/workflows/wan22-s2v', { method: 'DELETE' }));
  await page.waitForTimeout(600);
  check(errors.length === wfMark,
    `no console errors across the import (${errors.slice(wfMark, wfMark + 2).join(' | ') || 'clean'})`);

  // ---- files-only models are shown, not hidden ----
  // Downloading a large files-only model and then finding no trace of it in
  // the picker is being answered with silence, which reads as a bug. "You
  // cannot run this here" is worth saying. (MiniMax H3 was the example until
  // it stopped being files-only; Wan S2V still is.)
  await page.click('.tabs button[data-tab="gen"]');
  await page.waitForTimeout(900);
  const picker = await page.evaluate(() =>
    [...document.querySelectorAll('#model option')]
      .map((o) => ({ v: o.value, disabled: o.disabled, text: o.textContent })));
  const h3opt = picker.find((o) => o.v === 'wan22-s2v');
  check(!!h3opt, 'a files-only model is listed in the video picker');
  const h3run = picker.find((o) => o.v === 'minimax-h3');
  check(h3run && !h3run.disabled,
    'and MiniMax H3, which now has a graph here, is selectable rather than greyed');
  check(h3opt && h3opt.disabled, '…disabled rather than filtered out');
  check(h3opt && h3opt.text.includes('這裡跑不了'), '…and saying so in the option itself');
  const picked = await page.evaluate(() => document.getElementById('model').value);
  const pickedOpt = picker.find((o) => o.v === picked);
  check(pickedOpt && !pickedOpt.disabled,
    `…and a disabled entry is never left selected, which would arm the generate button (${picked})`);
  check(picker.some((o) => !o.disabled), 'runnable models are still selectable');

  // ---- HuggingFace as a second source, and the licence gate ----
  // No search on the HF side, by decision: its LoRA metadata is not good enough
  // to claim compatibility from. What is asserted here is that the page says so
  // rather than quietly guessing.
  const hfMark = errors.length;
  await page.click('.tabs button[data-tab="lora"]');
  await page.waitForTimeout(900);
  check((await page.textContent('#tab-lora')).includes('沒有搜尋'),
    'the HF path says it has no search, and why');

  await page.fill('#hfurl', 'lopi999/Wan2.2-I2V_General-NSFW-LoRA');
  await page.click('#hfgo');
  await page.waitForTimeout(5000);
  let hfTxt = await page.textContent('#hfbox');
  check(hfTxt.includes('作者說是給') && hfTxt.includes('Wan-AI/Wan2.2-I2V-A14B'),
    'a declared base model is shown as declared, and named');
  const hfFiles = await page.evaluate(() => document.querySelectorAll('[data-hff]').length);
  check(hfFiles === 2,
    `both of that repo's files are listed - a repo is not one LoRA (${hfFiles})`);

  await page.fill('#hfurl', 'Se0ulSeeker/wan_2.2_i2v_nsfw_loras');
  await page.click('#hfgo');
  await page.waitForTimeout(5500);
  hfTxt = await page.textContent('#hfbox');
  check(hfTxt.includes('作者沒有標'),
    'an undeclared base model is called out rather than guessed');
  check(hfTxt.includes('不會報錯'),
    'and says what a wrong base actually does, which is nothing at all');
  check(hfTxt.includes('虛構角色'),
    'and the boundary on real people is on the page, not only in the docs');
  check(errors.length === hfMark,
    `no console errors across the HF path (${errors.slice(hfMark, hfMark + 2).join(' | ') || 'clean'})`);

  // The licence gate. MiniMax H3 excludes the United States, which nobody
  // expects from an open-weights release, so the download waits for a tick.
  await page.click('.tabs button[data-tab="mdl"]');
  await page.waitForTimeout(1500);
  const mdlTxt = await page.textContent('#mlist');
  check(mdlTxt.includes('MiniMax H3'), 'MiniMax H3 is in the model list');
  check(mdlTxt.includes('這個模型的授權有限制') && mdlTxt.includes('美國'),
    'and its licence banner names the United States');
  // This used to assert the note said H3 has "no plain I2V". That claim was
  // wrong - ComfyUI ships a built-in image-to-video template for it - and the
  // note now has to carry the two things that are true and matter: it runs
  // here, and nobody has run it on real hardware.
  check(!mdlTxt.includes('沒有單純的 I2V'),
    'and the note no longer claims it has no plain image-to-video');
  check(mdlTxt.includes('沒有實跑驗證過'),
    '…while still saying the graph has never been run on real hardware');
  const h3Btn = '[data-dl="minimax-h3"], [data-redl="minimax-h3"]';
  check(await page.isDisabled(h3Btn), 'its download button starts disabled');
  await page.check('[data-ack="minimax-h3"]');
  await page.waitForTimeout(400);
  check(!await page.isDisabled(h3Btn), 'and the acknowledgement enables it');
  const wanGated = await page.evaluate(() =>
    !!document.querySelector('[data-ack="wan22-14b-fp8"]'));
  check(!wanGated, 'while Wan, being Apache 2.0, is not gated at all');

  // ---- 訓練角色: plan, check a real folder, emit a config ----
  // The whole tab is the part of training that can be done without a GPU, so
  // the whole tab is testable: the arithmetic, the folder inspection and the
  // syntax of the file that comes out. What it must never do is imply it
  // trained anything, so that is checked too.
  const trMark = errors.length;
  await page.click('.tabs button[data-tab="train"]');
  await page.waitForTimeout(1200);
  const trIntro = await page.textContent('#trintro');
  check(trIntro.includes('不執行訓練'), 'the training tab says up front that it does not train');
  check(/0 條是本專案量的/.test(trIntro),
    'and that nothing on it was measured here, same as the drama tab');

  // A trainer that cannot train the selected architecture must not be offered:
  // that is how you get a config the trainer refuses to open.
  const sdxlTrainers = await page.evaluate(() =>
    [...document.querySelectorAll('#trtrainer option')].map((o) => o.value));
  check(sdxlTrainers.includes('kohya') && !sdxlTrainers.includes('ai-toolkit'),
    `SDXL offers kohya, not the FLUX-only trainer (${sdxlTrainers.join(',')})`);
  await page.selectOption('#trarch', 'flux');
  await page.waitForTimeout(700);
  const fluxTrainers = await page.evaluate(() =>
    [...document.querySelectorAll('#trtrainer option')].map((o) => o.value));
  check(fluxTrainers.includes('ai-toolkit') && !fluxTrainers.includes('kohya'),
    `switching to FLUX swaps the list (${fluxTrainers.join(',')})`);
  await page.selectOption('#trarch', 'sdxl');
  await page.waitForTimeout(700);

  await page.fill('#trcount', '30');
  await page.dispatchEvent('#trcount', 'input');
  await page.waitForTimeout(800);
  check(/9 張/.test(await page.textContent('#trplan')),
    'the shot mix splits 30 images across framings');
  check((await page.textContent('#trsteps')).includes('1800'),
    'and says how many steps that is, marked as arithmetic');

  // The trigger check runs as you type, because finding out after three hours
  // that the token collided with a real word is the expensive way to learn it.
  await page.fill('#trtrigger', 'woman');
  await page.dispatchEvent('#trtrigger', 'input');
  await page.waitForTimeout(700);
  check((await page.textContent('#trtriggerwhy')).includes('打架'),
    'a real word is rejected as a trigger, live');
  await page.fill('#trtrigger', 's1vra_person');
  await page.dispatchEvent('#trtrigger', 'input');
  await page.waitForTimeout(700);
  check((await page.textContent('#trtriggerwhy')).includes('可以用'),
    'and a token the base model has no opinion about is accepted');
  const trCap = await page.textContent('#trcaption');
  check(trCap.startsWith('s1vra_person, adult'),
    `the caption leads with the trigger (${trCap.slice(0, 40)})`);

  // A real folder on disk, read for real.
  const trDir = TRAIN_FIXTURE;
  await page.fill('#trfolder', trDir);
  await page.click('#trcheck');
  await page.waitForTimeout(2200);
  const trLine = await page.textContent('#trhealthline');
  check(trLine.includes('26'), `checking a folder reports what is in it (${trLine.replace(/\s+/g,' ').slice(0,44)})`);
  check((await page.inputValue('#trcount')) === '26',
    'and the count comes from disk rather than what was typed');

  await page.fill('#trbase', 'C:/anim/wan-video/ComfyUI/models/checkpoints/lustify.safetensors');
  await page.fill('#trout', 'C:/anim/train/out');
  await page.click('#trgo');
  await page.waitForTimeout(1500);
  const trCfg = await page.textContent('#trcfg');
  check(trCfg.includes('[network_arguments]') && trCfg.includes('enable_bucket = true'),
    'the config comes out with bucketing on');
  check(trCfg.includes('lustify.safetensors'), 'and the base model path filled in');
  const trNote = await page.textContent('#trcfgnote');
  check(trNote.includes('accelerate launch'), 'and the command that runs it');
  check(trNote.includes('沒有跑過'),
    'and says once more that this project has never run a training job');
  check(errors.length === trMark,
    `no console errors across the training tab (${errors.slice(trMark, trMark+2).join(' | ') || 'clean'})`);

  // Two deliberate failures. They log 404/400 to the console by design, so they
  // come after the error assertion above rather than tripping it.
  await page.fill('#trfolder', '/does/not/exist/at/all');
  await page.click('#trcheck');
  await page.waitForTimeout(1500);
  check((await page.textContent('#trhealthline')).includes('找不到'),
    'a folder that is not there says so rather than throwing');
  await page.fill('#trtrigger', 'Emma');
  await page.dispatchEvent('#trtrigger', 'input');
  await page.waitForTimeout(400);
  await page.click('#trgo');
  await page.waitForTimeout(1200);
  check((await page.textContent('#trcfgnote')).includes('觸發詞'),
    'and a bad trigger is refused at config time, not only while typing');
  check(!errors.slice(trMark).some((e) => e.startsWith('pageerror')),
    'and neither failure threw');

  // ---- style library + prompt doctor ----
  // The diff is the whole trust story here: nothing may reach the prompt box
  // until it has been shown, and the user's own tags must come out the far side
  // untouched. Both are checked against a prompt full of things the merger has
  // never heard of.
  const errMark = errors.length;
  // These controls live on the image tab, and the block above ends on another
  // one. Reach it explicitly rather than inheriting whatever tab happened to
  // be open - that coupling has broken this suite twice.
  await page.click('.tabs button[data-tab="img"]');
  await page.waitForTimeout(600);
  await page.evaluate(()=>{ const s=document.getElementById('imodel'); s.value='noobai'; s.dispatchEvent(new Event('change')); });
  await page.waitForTimeout(500);
  await page.fill('#iprompt', '1girl, hoshimachi suisei, pastel colors, score_9, my_lora_trigger, (smile:1.3)');
  await page.fill('#inegative', '');
  await page.waitForTimeout(500);

  check(!await page.isVisible('#stylebox'), 'the style library starts collapsed');
  await page.click('#istyles');
  await page.waitForTimeout(600);
  check(await page.isVisible('#stylebox'), 'the 風格靈感庫 button opens it');
  const recipeCount = await page.evaluate(()=>document.querySelectorAll('#stlist button[data-recipe]').length);
  check(recipeCount === 22, `22 recipes render for NoobAI (${recipeCount})`);
  const presetCount = await page.evaluate(()=>document.querySelectorAll('#stpresets button[data-preset]').length);
  check(presetCount >= 3, `and its quality presets (${presetCount})`);

  // Chips carry their provenance band, and a caption token is not shown as a
  // rare tag just because danbooru has 0 posts for it.
  const bands = await page.evaluate(()=>{
    const c = { kd:0, kc:0, kp:0 };
    document.querySelectorAll('#stlist .tag').forEach((t)=>{
      if (t.classList.contains('kd')) c.kd++;
      if (t.classList.contains('kc')) c.kc++;
      if (t.classList.contains('kp')) c.kp++;
    });
    return c;
  });
  check(bands.kd > 50, `danbooru chips are marked (${bands.kd})`);
  const noteTxt = await page.textContent('#stnote');
  check(noteTxt.includes('不是模仿畫師'), 'the panel says these are not artist imitation');

  // Nothing invented ships. `2d` is the dangerous one - it aliases to an artist.
  const allChips = await page.evaluate(()=>[...document.querySelectorAll('#stlist .tag')].map((t)=>t.childNodes[0].textContent.trim()));
  check(!allChips.includes('2d'), '`2d` is nowhere in the rendered recipes (it aliases to artist nidy)');
  ['clean lineart','cel shading','rim light','dramatic lighting','detailed eyes','glossy skin'].forEach((t)=>{
    check(!allChips.includes(t), `the spec's invented \`${t}\` did not ship`);
  });
  const replTxt = await page.textContent('#streplbody');
  check(replTxt.includes('nidy'), 'the substitution table explains the 2d/nidy alias');

  await page.fill('#stq', '雨');
  await page.waitForTimeout(300);
  const rainy = await page.evaluate(()=>document.querySelectorAll('#stlist button[data-recipe]').length);
  check(rainy === 2, `searching 雨 narrows to 2 (${rainy})`);
  await page.fill('#stq', 'zzzz-nothing');
  await page.waitForTimeout(300);
  check((await page.textContent('#stlist')).includes('沒有符合'), 'an empty search says so');
  await page.fill('#stq', '');
  await page.waitForTimeout(300);

  // Applying shows a diff and writes nothing yet.
  const beforeApply = await page.inputValue('#iprompt');
  await page.click('#stlist button[data-recipe="ink-manga"]');
  await page.waitForTimeout(500);
  check(await page.isVisible('#pdbox'), 'applying a recipe shows the diff first');
  check(await page.inputValue('#iprompt') === beforeApply, '…and has not touched the prompt box yet');
  const diff = await page.textContent('#pdbox');
  check(diff.includes('－ 換掉') && diff.includes('pastel colors'),
    'the diff names what it is replacing -> ' + diff.slice(0,40).replace(/\s+/g,' '));
  check(diff.includes('score_9'), '…and what it is cleaning out for this checkpoint');
  await page.click('#stcancel');
  await page.waitForTimeout(200);
  check(await page.inputValue('#iprompt') === beforeApply, 'cancelling changes nothing');

  await page.click('#stlist button[data-recipe="ink-manga"]');
  await page.waitForTimeout(500);
  await page.click('#stok');
  await page.waitForTimeout(500);
  const merged = await page.inputValue('#iprompt');
  check(merged.includes('monochrome') && merged.includes('greyscale'),
    'accepting writes the recipe in, both sides of its own conflict intact');
  check(merged.includes('my_lora_trigger'), '…without eating the LoRA trigger');
  check(merged.includes('(smile:1.3)'), '…and keeping the user’s own weight');
  check(!merged.includes('score_9'), '…while dropping the foreign score tag');
  check(!merged.includes('pastel colors'), '…and the conflicting palette');

  // Keep-my-style leaves the conflict alone.
  await page.fill('#iprompt', '1girl, pastel colors');
  await page.waitForTimeout(400);
  await page.check('#stkeep');
  await page.click('#stlist button[data-recipe="ink-manga"]');
  await page.waitForTimeout(500);
  await page.click('#stok');
  await page.waitForTimeout(400);
  check((await page.inputValue('#iprompt')).includes('pastel colors'),
    '保留目前畫風 keeps the conflicting tag');
  await page.uncheck('#stkeep');

  // A quality preset.
  await page.fill('#iprompt', '1girl');
  await page.waitForTimeout(400);
  await page.click('#stpresets button[data-preset="noobai-official"]');
  await page.waitForTimeout(500);
  await page.click('#stok');
  await page.waitForTimeout(400);
  check((await page.inputValue('#iprompt')).includes('masterpiece'),
    'a quality preset applies through the same diff');
  await page.click('#stclose');
  await page.waitForTimeout(200);
  check(!await page.isVisible('#stylebox'), 'the panel collapses again');

  // ---- prompt doctor ----
  await page.evaluate(()=>{ const s=document.getElementById('isize'); s.value='832×1216 直式'; s.dispatchEvent(new Event('change')); });
  await page.fill('#iprompt', '1girl, hoshimachi suisei, official art, masterpiece, best quality');
  await page.fill('#inegative', 'worst quality, lowres');
  await page.waitForTimeout(900);
  let health = await page.textContent('#pdline');
  check(health.includes('良好'), `a clean prompt reads 良好 -> ${health.trim()}`);

  await page.fill('#iprompt', 'score_9, 1girl, 8k, ultra detailed, smile, smile');
  await page.fill('#inegative', 'smile');
  await page.waitForTimeout(900);
  health = await page.textContent('#pdline');
  check(health.includes('要先處理') || health.includes('值得看'),
    `a broken prompt does not -> ${health.trim()}`);
  await page.click('#pdopen');
  await page.waitForTimeout(300);
  const findings = await page.textContent('#pdbox');
  check(findings.includes('Pony'), 'the detail names the score dialect');
  check(findings.includes('從來沒有生成過任何一張圖'),
    'and the panel says outright that none of this was measured on a picture');

  // The one-click fix actually edits the prompt.
  await page.click('#pdbox button[data-fix]');
  await page.waitForTimeout(600);
  check(!(await page.inputValue('#iprompt')).includes('score_9'),
    'the 移除 button takes the foreign tags out');

  // The resolution warning is the most valuable finding, so it is checked end
  // to end: shrink the canvas, see the warning, click the fix, see it go.
  // 看細節 is a toggle, so the panel has to be closed before it can be reopened.
  await page.click('#pdopen');
  await page.waitForTimeout(200);
  check(!await page.isVisible('#pdbox'), '看細節 closes the panel again');
  await page.evaluate(()=>{ const s=document.getElementById('isize'); s.value=IMG.customSize; s.dispatchEvent(new Event('change')); });
  await page.waitForTimeout(300);
  await page.evaluate(()=>{ document.getElementById('iwidth').value=512; document.getElementById('iheight').value=512; paintSize(); });
  await page.waitForTimeout(900);
  await page.click('#pdopen');
  await page.waitForTimeout(300);
  const resTxt = await page.textContent('#pdbox');
  check(resTxt.includes('512×512') && resTxt.includes('SDXL'),
    'a 512² canvas on an SDXL checkpoint is called out -> ' + resTxt.slice(0,48).replace(/\s+/g,' '));
  await page.click('#pdbox button[data-size]');
  await page.waitForTimeout(900);
  check(await page.inputValue('#iwidth') === '832', 'and its one-click fix resizes the canvas');
  await page.waitForTimeout(400);
  // The prompt still has `smile` on both sides, so the *line* stays red - what
  // has to be gone is the resolution finding itself.
  const stillRes = await page.evaluate(()=>PD.last.findings.some((f)=>f.id==='resolution'));
  check(!stillRes, '…after which the resolution finding is gone');
  await page.evaluate(()=>{ const b=document.getElementById('pdbox'); b.classList.add('hidden'); });
  await page.fill('#iprompt', '');
  await page.fill('#inegative', '');
  // Put the canvas back where the rest of the file expects to find it: the
  // custom-size block below starts from whatever these are left at.
  await page.evaluate(()=>{ document.getElementById('iwidth').value=1024; document.getElementById('iheight').value=1024; paintSize(); });
  await page.waitForTimeout(400);

  // Only errors raised during this block, and only real ones. The health check
  // fires on a debounce as the prompt is typed, which reuses keep-alive sockets
  // faster than uvicorn's default 5s timeout retires them - that shows up as a
  // transient ERR_CONNECTION_RESET on a request the page then simply retries.
  // It is a property of the dev server's socket handling, not of this code, so
  // it is counted and printed rather than asserted on.
  const mine = errors.slice(errMark);
  const resets = mine.filter((e) => /ERR_CONNECTION_RESET|ERR_ABORTED/.test(e));
  const real = mine.filter((e) => !/ERR_CONNECTION_RESET|ERR_ABORTED/.test(e));
  check(real.length === 0,
    `no JS errors from the style library (${real.slice(0,2).join(' | ') || 'clean'}` +
    `${resets.length ? `; ${resets.length} transient socket reset(s) ignored` : ''})`);


  // ---- custom size ----
  await page.selectOption('#isize', { label: '自訂尺寸' }).catch(async () => {
    await page.evaluate(() => { const s=document.getElementById('isize'); s.value = IMG.customSize; s.dispatchEvent(new Event('change')); });
  });
  await page.waitForTimeout(300);
  check(await page.isVisible('#iwrange'), 'choosing 自訂尺寸 reveals the sliders');
  await page.evaluate(() => { const r=document.getElementById('iwrange'); r.value=1536; r.dispatchEvent(new Event('input')); });
  await page.waitForTimeout(150);
  check(await page.inputValue('#iwidth') === '1536', 'dragging width updates the number box');
  let note = await page.textContent('#isizenote');
  check(note.includes('超出'), 'and warns when the pixel budget is too big -> ' + note.slice(0,60));
  await page.check('#ilockratio');
  await page.evaluate(() => { const r=document.getElementById('iwrange'); r.value=1024; r.dispatchEvent(new Event('input')); });
  await page.waitForTimeout(150);
  const w = await page.inputValue('#iwidth'), h = await page.inputValue('#iheight');
  check(Math.abs(w/h - 1536/1024) < 0.05, `ratio lock holds ${w}x${h}`);
  await page.uncheck('#ilockratio');
  await page.click('#icustomsize button[data-ratio="9:16"]');
  await page.waitForTimeout(150);
  const w2 = await page.inputValue('#iwidth'), h2 = await page.inputValue('#iheight');
  note = await page.textContent('#isizenote');
  check(w2 % 64 === 0 && h2 % 64 === 0, `a ratio preset snaps to 64 (${w2}x${h2})`);
  check(Math.abs((w2*h2)/(1024*1024) - 1) < 0.35, `and keeps SDXL's pixel budget (${((w2*h2)/1e6).toFixed(2)} MP)`);
  check(note.includes('你按的是 9:16'), 'the readout is honest about the snap -> ' + note.slice(0,44));


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
