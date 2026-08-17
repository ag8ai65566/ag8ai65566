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
    setAttribute() {}, getAttribute: () => null,
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

report();
