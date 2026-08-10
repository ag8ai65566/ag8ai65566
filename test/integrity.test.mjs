// System-integrity gate. Runs against the committed data/gauges.json and the rendered
// dashboard, and fails if the renderer has drifted from the canonical engine.
//   node --test test/

import { test } from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync, existsSync } from 'node:fs';
import { join, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';

const repo = join(dirname(fileURLToPath(import.meta.url)), '..');
const read = (p) => readFileSync(join(repo, p), 'utf8');

const gauges = JSON.parse(read('data/gauges.json'));
const registry = JSON.parse(read('config/data-sources.json'));
const html = existsSync(join(repo, 'reports/us-market-dashboard.html'))
  ? read('reports/us-market-dashboard.html') : null;
const renderer = read('.claude/skills/us-market-brief/scripts/render-dashboard.mjs');
const holdings = existsSync(join(repo, 'data/holdings.json'))
  ? JSON.parse(read('data/holdings.json')) : null;

test('every gauge carries the five status dimensions', () => {
  const dims = ['data_state', 'source_authority', 'measurement_integrity', 'signal_validation', 'automation_mode'];
  for (const g of gauges.gauges) {
    for (const d of dims) {
      assert.ok(g.status?.[d], `${g.id} is missing status.${d}`);
    }
  }
});

test('missing data never becomes a rule evaluation', () => {
  const usable = ['CURRENT', 'LAGGED_BY_DESIGN'];
  for (const g of gauges.gauges) {
    if (!usable.includes(g.status.data_state)) {
      assert.equal(g.decision, 'NO_DECISION', `${g.id} is ${g.status.data_state} but was still evaluated`);
      assert.equal(g.henren?.status ?? null, g.henren === null ? null : g.henren.status);
    }
  }
});

test('counts exclude undecided gauges', () => {
  const t = gauges.henren_rule_tally;
  const colours = (t.green ?? 0) + (t.yellow ?? 0) + (t.red ?? 0);
  assert.equal(colours, t.evaluated, 'colour counts must sum to evaluated, not to total');
  assert.equal(t.evaluated + t.no_decision, t.total);
});

test('no composite score is emitted', () => {
  // Match KEYS, not substrings — `no_composite_score` legitimately contains one of these,
  // and the first version of this test failed on the very field that declares compliance.
  const banned = new Set(['bubble_score', 'market_score', 'composite_score', 'overall_score', 'risk_score']);
  const walk = (node, path = '') => {
    if (Array.isArray(node)) return node.forEach((v, i) => walk(v, `${path}[${i}]`));
    if (!node || typeof node !== 'object') return;
    for (const [k, v] of Object.entries(node)) {
      assert.ok(!banned.has(k), `banned composite field at ${path}.${k}`);
      walk(v, `${path}.${k}`);
    }
  };
  walk(gauges);
  assert.ok(gauges.no_composite_score, 'the explicit no-composite declaration must be present');
});

test('every evaluated gauge names a registered source and carries provenance', () => {
  const known = new Set([...Object.keys(registry.sources), 'manual']);
  for (const g of gauges.gauges) {
    const p = g.provenance;
    assert.ok(p, `${g.id} has no provenance`);
    assert.ok(known.has(p.source_id), `${g.id} cites unregistered source ${p.source_id}`);
    for (const f of ['effective_date', 'transformation', 'calculation_version']) {
      assert.ok(p[f] !== undefined, `${g.id} provenance missing ${f}`);
    }
  }
});

test('a composite gauge inherits its weakest source authority', () => {
  const m2 = gauges.gauges.find((g) => g.id === 'm2gap');
  if (m2 && m2.decision === 'RULE_EVALUATED') {
    assert.equal(m2.status.source_authority, 'UNOFFICIAL_FREE',
      'M2 (FRED) + Nasdaq (Yahoo) must report as the weaker of the two');
  }
});

test('proxy gauges declare themselves and name a replacement', () => {
  for (const g of gauges.gauges.filter((x) => x.proxy)) {
    assert.ok(g.proxy_warning, `${g.id} is a proxy without a warning`);
    assert.ok(g.proxy_replacement, `${g.id} is a proxy without a named replacement`);
  }
});

test('thresholds this system invented are flagged as ours', () => {
  // Anything not traceable to his own words must say so rather than borrowing his authority.
  for (const g of gauges.gauges.filter((x) => x.henren?.threshold_is_ours)) {
    assert.match(g.henren.quote ?? '', /本系統|非他的原話|未給/,
      `${g.id} claims an invented threshold but its quote does not say so`);
  }
});

test('the renderer performs no financial calculation', () => {
  const banned = [
    /Math\.log\s*\(/, /Math\.sqrt\s*\(/, /\*\s*252\b/, /\/\s*1e9\b/,
    /function\s+percentile/, /function\s+rvol/, /\.reduce\([^)]*\+[^)]*value/,
  ];
  for (const re of banned) {
    assert.ok(!re.test(renderer), `renderer contains what looks like a calculation: ${re}`);
  }
});

test('dashboard numbers match the engine exactly', { skip: !html }, () => {
  for (const g of gauges.gauges) {
    if (g.decision !== 'RULE_EVALUATED' || g.observed?.value === null) continue;
    assert.ok(html.includes(String(g.observed.value)),
      `${g.id}: engine says ${g.observed.value} but the dashboard does not contain it`);
  }
});

test('dashboard states the calculation version it was rendered from', { skip: !html }, () => {
  assert.ok(html.includes(gauges.calculation_version), 'dashboard must show the calc version');
  assert.ok(html.includes(gauges.code_commit), 'dashboard must show the code commit');
});

test('no buy/sell language reaches the rendered output', { skip: !html }, () => {
  // Assertive constructions only. A disclaimer that says "no price targets" contains the
  // words "price target" — the first version of this test flagged its own guardrail text.
  const assertive = [
    /STRONG\s+(BUY|SELL)/i,
    /\b(建議|應該)\s*(買進|買入|賣出|加碼|減碼|清倉|出清)/,
    /目標價\s*[:：$＄\d]/,
    /price\s+target\s*[:：$\d]/i,
    /\b(BUY|SELL)\s+RATING\b/i,
  ];
  for (const re of assertive) {
    assert.ok(!re.test(html), `guardrail breach: ${re} matched in the dashboard`);
  }
});

test('the Serenity gate escalates only with a citation', { skip: !holdings }, () => {
  for (const h of holdings.holdings) {
    const g = h.serenity_gate;
    if (!g) continue;
    for (const [field, v] of Object.entries(g)) {
      if (['unverified', 'not_yet', 'observed_not_judged'].includes(v.value)) continue;
      if (field === 'conclusion') continue;
      assert.ok(v.citations?.length || v.evidence?.length,
        `${h.ticker}.${field} escalated to "${v.value}" with no cited evidence`);
    }
  }
});

test('the gate never reaches an investable conclusion without valuation work', { skip: !holdings }, () => {
  for (const h of holdings.holdings) {
    assert.notEqual(h.serenity_gate?.conclusion?.value, '可投资结论',
      `${h.ticker} reached an investable conclusion; no valuation stage exists yet`);
  }
});

test('a flagged plausibility check is surfaced, not swallowed', { skip: !holdings || !html }, () => {
  for (const h of holdings.holdings) {
    if (h.fundamentals?.plausibility?.status !== 'FLAGGED') continue;
    assert.ok(html.includes('合理性檢查未通過'),
      `${h.ticker} has a plausibility flag that never reaches the dashboard`);
  }
});

test('concentration is judged on the broad sector, not the niche', { skip: !holdings }, () => {
  const c = holdings.concentration;
  if (c.distinct_niches > c.distinct_sectors) {
    assert.equal(c.same_sector, c.distinct_sectors === 1,
      'niche labels must not be able to manufacture apparent diversification');
  }
});

test('signal validation is honest about being untested', () => {
  const validated = gauges.gauges.filter((g) => g.status.signal_validation !== 'UNTESTED');
  for (const g of validated) {
    assert.fail(`${g.id} claims ${g.status.signal_validation} — no backtest exists to support that`);
  }
});
