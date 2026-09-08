/*
 * Run the page's own script against a stub DOM and call the render functions
 * with real data.
 *
 * Everything in tests/test_flow.py that touches index.html does it by grepping
 * for substrings, which proves a line exists and nothing about whether it runs.
 * Four bugs shipped behind that: `artist_tag_models` changed from a list to an
 * object on the Python side and `.includes()` was left on the JS side, so
 * renderPackStyle() threw before writing any HTML and quietly disabled the
 * whole feature - while every string-grep still passed.
 *
 * So this loads the real script and calls the real functions. It is a smoke
 * test, not a rendering test: the assertion is mostly "does this throw", which
 * is exactly the class of bug that got through.
 *
 *   node tests/ui_smoke.js
 *
 * Exits non-zero and prints FAIL lines on failure.
 */
'use strict';

const fs = require('fs');
const path = require('path');
const vm = require('vm');

const ROOT = path.join(__dirname, '..');
const html = fs.readFileSync(path.join(ROOT, 'app', 'static', 'index.html'), 'utf8');
const pack = JSON.parse(
  fs.readFileSync(path.join(ROOT, 'app', 'packs', 'hololive-collection.json'), 'utf8'));

let failures = 0;
const results = [];
function check(ok, label) {
  results.push((ok ? '  ok  ' : '  FAIL ') + label);
  if (!ok) failures += 1;
}
function noThrow(label, fn) {
  try {
    fn();
    check(true, label);
  } catch (e) {
    check(false, `${label} -- threw: ${e.message}`);
  }
}

/* ---------- the smallest DOM that lets the script run ---------- */
// Ids the script reads back after writing innerHTML (buttons it wires up) have
// to resolve to something, so every lookup returns a live stub instead of null.
function el(tag) {
  const node = {
    tagName: tag || 'div',
    _html: '',
    value: '',
    textContent: '',
    checked: false,
    disabled: false,
    hidden: false,
    files: [],
    style: {},
    dataset: {},
    options: [],
    selectedIndex: 0,
    classList: {
      _set: new Set(),
      add(c) { this._set.add(c); },
      remove(c) { this._set.delete(c); },
      toggle(c, on) { if (on === undefined) { this._set.has(c) ? this._set.delete(c) : this._set.add(c); } else if (on) { this._set.add(c); } else { this._set.delete(c); } },
      contains(c) { return this._set.has(c); },
    },
    get innerHTML() { return this._html; },
    set innerHTML(v) { this._html = String(v); },
    querySelector: () => el(),
    querySelectorAll: () => [],
    appendChild() {}, insertBefore() {}, remove() {},
    _attrs: {},
    setAttribute(k, v) { this._attrs[k] = String(v); },
    getAttribute(k) { return k in this._attrs ? this._attrs[k] : null; },
    addEventListener() {}, removeEventListener() {},
    scrollIntoView() {}, focus() {}, click() {},
  };
  return node;
}

const nodes = new Map();
function lookup(sel) {
  if (!nodes.has(sel)) nodes.set(sel, el());
  return nodes.get(sel);
}

const document = {
  querySelector: (sel) => lookup(sel),
  // The tab switcher derives its list from the DOM, so this must be non-empty
  // or every tab lookup below it silently does nothing.
  querySelectorAll: (sel) => {
    if (sel === '.tabs button') {
      return ['gen', 'img', 'lib', 'lora', 'mdl', 'pb', 'set'].map((t) => {
        const b = el('button');
        b.dataset.tab = t;
        return b;
      });
    }
    if (sel === '.modes button') {
      const b = el('button');
      b.dataset.mode = 'plain';
      return [b];
    }
    return [];
  },
  createElement: (tag) => el(tag),
  getElementById: (id) => lookup('#' + id),
  addEventListener() {},
};

const store = new Map();
const sandbox = {
  document,
  window: { scrollTo() {}, addEventListener() {}, location: { href: '' } },
  localStorage: {
    getItem: (k) => (store.has(k) ? store.get(k) : null),
    setItem: (k, v) => store.set(k, v),
  },
  // Nothing here should reach the network; boot()'s fetches resolve to empty.
  fetch: () => Promise.resolve({ ok: true, statusText: 'OK', json: () => Promise.resolve({}) }),
  setInterval: () => 0,
  clearInterval: () => {},
  setTimeout: () => 0,
  clearTimeout: () => {},
  URL: { createObjectURL: () => 'blob:x', revokeObjectURL() {} },
  FormData: function FormData() { this.append = () => {}; },
  Image: function Image() {},
  console,
  navigator: { clipboard: { writeText: () => Promise.resolve() } },
};
sandbox.window.document = document;
sandbox.globalThis = sandbox;

const script = html.match(/<script>([\s\S]*)<\/script>/)[1];
const context = vm.createContext(sandbox);
try {
  vm.runInContext(script, context, { filename: 'index.html<script>' });
  check(true, 'the page script loads without throwing');
} catch (e) {
  check(false, `the page script loads without throwing -- ${e.message}`);
  console.log(results.join('\n'));
  process.exit(1);
}

/* ---------- the functions that broke ---------- */
// Top-level `let`/`const` land in the context's lexical scope, not on the
// sandbox object, so everything below is reached by evaluating inside it.
const run = (code) => vm.runInContext(code, context);
const set = (name, value) => {
  context.__v = value;
  run(`${name} = __v;`);
};

// Results are printed at the very end, so an uncaught throw part-way through
// used to discard every line collected before it - which is how the first run
// of this harness reported "0 failures" for a bug it had in fact caught.
function report() {
  console.log(results.join('\n'));
  console.log(failures ? `FAILED ${failures}` : `PASSED ${results.length}`);
  process.exit(failures ? 1 : 0);
}
process.on('uncaughtException', (e) => {
  check(false, `unexpected throw outside a checked call: ${e.message}`);
  report();
});

const who = pack.characters.find((c) => c.key === 'mori-calliope');
const noMama = pack.characters.find((c) => !c.artist_tag);

set('PACK.list', [pack]);
set('PACK.chosen', pack);
set('PACK.who', who.key);
set('PACK.costume', 0);
set('IMG.models', [
  { id: 'noobai', label: 'NoobAI-XL', installed: true, sizes: {}, download_bytes: 1 },
  { id: 'pony', label: 'Pony', installed: true, sizes: {}, download_bytes: 1 },
]);
set('CN.list', [{ name: 'controlnet-union-sdxl-promax.safetensors', label: 'Union' }]);
set('CN.all', [{ id: 'union-promax', label: 'Union', name: 'x.safetensors',
                 best_for: '', size: 1, installed: true }]);

// artist_tag_models is a {model: form} object. This is the exact call that
// threw "includes is not a function" and took the style block with it.
for (const model of ['noobai', 'illustrious', 'pony', '', 'nonsense']) {
  set('IMG.chosen', { id: model, label: model });
  noThrow(`renderPackStyle() survives base model ${model || '(none)'}`,
          () => run('renderPackStyle()'));
}

set('IMG.chosen', { id: 'noobai', label: 'NoobAI-XL' });
noThrow('renderPackStyle() on NoobAI', () => run('renderPackStyle()'));
let out = lookup('#packstyle').innerHTML;
check(out.includes('packstylechk'), 'the style checkbox is rendered at all');
check(out.includes('packstylew'), 'the weight slider is rendered');
check(!out.includes('disabled>'), 'and the checkbox is enabled on a model that takes artist tags');
check(out.includes('artist:yukisame'),
      'the token shown uses the form NoobAI documents');
check(!out.includes('by yukisame'),
      'and not the Illustrious form alongside it');

set('IMG.chosen', { id: 'illustrious', label: 'Illustrious' });
noThrow('renderPackStyle() on Illustrious', () => run('renderPackStyle()'));
out = lookup('#packstyle').innerHTML;
check(out.includes('by yukisame') && !out.includes('artist:yukisame'),
      'on Illustrious it switches to "by <artist>"');

// On a model that cannot use artist tags the switch button must appear, which
// needs the first *key* of the map - an object has no [0].
set('IMG.chosen', { id: 'pony', label: 'Pony' });
noThrow('renderPackStyle() on Pony', () => run('renderPackStyle()'));
out = lookup('#packstyle').innerHTML;
check(out.includes('packstyleswitch'), 'on Pony the "switch base model" button appears');
check(out.includes('NoobAI'), 'and it names a model where artist tags work');

set('PACK.who', noMama ? noMama.key : who.key);
noThrow('renderPackStyle() survives a character with no artist tag',
        () => run('renderPackStyle()'));
set('PACK.who', '');
noThrow('renderPackStyle() survives no character selected',
        () => run('renderPackStyle()'));
set('PACK.who', who.key);

/* ---------- the token preview must match the server ---------- */
const expected = JSON.parse(process.argv[2] || '{}');
for (const [weight, want] of Object.entries(expected)) {
  const got = (context.__w = Number(weight), run('artistToken("artist:x", __w)'));
  check(got === want, `artistToken(${weight}) === ${want} (got ${got})`);
}

/* ---------- the tab switcher, which the a11y pass refactored ---------- */
// This is the one piece of existing behaviour the accessibility work rewrote,
// so it gets exercised rather than grepped: the class, the ARIA state and the
// panel visibility all have to move together, or the page says one thing and
// announces another.
noThrow('showTab() runs', () => run('showTab(TABBTNS[1])'));
const btns = run('TABBTNS');
const selected = btns.filter((b) => b.getAttribute('aria-selected') === 'true');
check(selected.length === 1, `exactly one tab is selected (${selected.length})`);
check(btns[1].classList.contains('on'), 'the clicked tab is the styled one');
check(btns[1].getAttribute('aria-selected') === 'true', '…and the announced one');
check(btns[0].getAttribute('aria-selected') === 'false', 'the previous tab is deselected');
check(btns.filter((b) => b.tabIndex === 0).length === 1,
      'the tablist is a single tab stop');
noThrow('arrow keys move between tabs',
        () => btns[1].onkeydown({ key: 'ArrowRight', preventDefault() {} }));
check(btns[2].getAttribute('aria-selected') === 'true',
      'ArrowRight lands on the next tab');
noThrow('Home jumps to the first tab',
        () => run('TABBTNS')[2].onkeydown({ key: 'Home', preventDefault() {} }));
check(btns[0].getAttribute('aria-selected') === 'true', '…and it is selected');
// A key the tablist does not handle must fall through untouched.
let prevented = false;
btns[0].onkeydown({ key: 'a', preventDefault() { prevented = true; } });
check(!prevented, 'an unrelated key is left alone');

/* ---------- everything else that renders from server data ---------- */
noThrow('renderPackState()', () => run('renderPackState()'));
noThrow('renderPackMembers()', () => run('renderPackMembers()'));
noThrow('renderPackCostumes()', () => run('renderPackCostumes()'));
noThrow('renderControlHelp()', () => run('renderControlHelp()'));
noThrow('renderControlnetModels()', () => run('renderControlnetModels()'));
noThrow('renderRestageReady()', () => run('renderRestageReady()'));
noThrow('renderLock() with nothing locked', () => run('renderLock()'));
set('COMIC.locked', { count: 5, name: 'page01.png' });
noThrow('renderLock() with a locked layout', () => run('renderLock()'));
noThrow('clearRestage() puts everything back', () => run('clearRestage(true)'));
check(run('COMIC.locked') === null && run('CN.controls.length') === 0,
      'and it really did clear the lock and the crops');
noThrow('loraBudget()', () => run('loraBudget()'));
noThrow('controlPayload()', () => run('controlPayload()'));

/* ---------- the experiment vote payload and the standings line ---------- */
// A review found two bookkeeping bugs in this exact pair of functions: a tie
// sent only one of the two variants, and the standings line summed per-variant
// tallies so every comparison was reported twice. The Chromium run cannot reach
// them without a real checkpoint installed, so they are exercised here with the
// network stubbed - which is enough, because what is being checked is the shape
// of the payload and one line of arithmetic.
const posted = [];
set('EXP.open', {
  id: 'e1',
  variants: [{ id: 'v0', label: 'A' }, { id: 'v1', label: 'B' }],
  votes: [
    { criterion: 'likeness', winner: 'v0', loser: 'v1', other: '', seed: 11 },
    { criterion: 'likeness', winner: '', loser: 'v0', other: 'v1', seed: 22 },
    { criterion: 'beauty', winner: 'v1', loser: 'v0', other: '', seed: 11 },
  ],
  standings: {
    likeness: { v0: { win: 1, loss: 0, tie: 1, played: 2, rate: 0.5 },
                v1: { win: 0, loss: 1, tie: 1, played: 2, rate: 0 } },
  },
});
set('EXP.criterion', 'likeness');
set('EXP.criteria', { likeness: '哪張比較像本人？' });
set('EXP.pair', { seed: 33, a: { variant: 'v0', job: 'j1' }, b: { variant: 'v1', job: 'j2' } });
run(`fetch = async (url, opts) => { POSTED.push([url, JSON.parse(opts.body)]);
       return { ok: true, json: async () => ({}) }; };`.replace('POSTED', '__posted'));
set('__posted', posted);
set('openExperiment', function () {});
set('nextJudgement', function () {});

noThrow('castVote() on a tie', () => run("castVote('')"));
const tieBody = posted.length ? posted[posted.length - 1][1] : {};
check(tieBody.winner === '' && tieBody.loser === 'v0' && tieBody.other === 'v1',
      `a tie posts both variants (${JSON.stringify(tieBody)})`);
check(tieBody.seed === 33, '…and the seed it was judged on');

noThrow('castVote() with a winner', () => run("castVote('v1')"));
const winBody = posted[posted.length - 1][1];
check(winBody.winner === 'v1' && winBody.loser === 'v0' && winBody.other === '',
      `a decided vote has no third side (${JSON.stringify(winBody)})`);

noThrow('renderStandings()', () => run('renderStandings()'));
const stand = run("$('#exparena').innerHTML");
// Two votes on `likeness`. Summing `played` across the two rows gives 4, which
// is the bug; counting the votes for this criterion gives 2.
check(/共 2 次比較/.test(stand),
      `the standings count votes, not per-variant tallies (${
        (/共 \d+ 次比較/.exec(stand) || ['no count found'])[0]})`);
check(stand.includes('票數還太少'), '…and two votes is still too few to conclude from');

// ---- seconds -> frames, both grids -------------------------------------
// The page derived this with Wan's 4n+1 written in, for every model. Picking
// 5 seconds of MiniMax H3 quoted 121 frames on screen while the graph built
// 124. The numbers below are the ones tests/test_flow.py checks on the Python
// side, so if either implementation drifts one of the two suites fails.
const h3grid = { fps: 24, frame_period: 17, frame_phase: 5 };
const wangrid = { fps: 16, frame_period: 4, frame_phase: 1 };
noThrow('framesFor() is reachable', () => run('framesFor({fps:16}, 3)'));
const h3got = [2, 5, 10].map((s) => run(`framesFor(${JSON.stringify(h3grid)}, ${s})`));
check(String(h3got) === '56,124,243', `H3 rounds up onto 17n+5 (${h3got})`);
const wangot = [3, 5].map((s) => run(`framesFor(${JSON.stringify(wangrid)}, ${s})`));
check(String(wangot) === '49,81', `Wan stays on 4n+1 (${wangot})`);
check(run('framesFor({fps:16}, 5)') === 81,
      'a model with no grid declared falls back to 4n+1');

report();
