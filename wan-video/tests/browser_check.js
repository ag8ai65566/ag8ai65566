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
  await page.waitForTimeout(500);
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

  // ---- "why doesn't it look like the stream model" ----
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
  check(likeNote.includes('12,496') || /\d,\d\d\d 張/.test(note), 'it quotes the real post count -> ' + likeNote.slice(0,54).replace(/\s+/g,' '));
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
