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

test('[integrity] every gauge carries the five status dimensions', () => {
  const dims = ['data_state', 'source_authority', 'measurement_integrity', 'signal_validation', 'automation_mode'];
  for (const g of gauges.gauges) {
    for (const d of dims) {
      assert.ok(g.status?.[d], `${g.id} is missing status.${d}`);
    }
  }
});

test('[integrity] unusable data never becomes a clean rule evaluation', () => {
  const usable = ['CURRENT', 'LAGGED_BY_DESIGN'];
  for (const g of gauges.gauges) {
    if (usable.includes(g.status.data_state)) continue;
    assert.notEqual(g.decision, 'RULE_EVALUATED',
      `${g.id} is ${g.status.data_state} but presents as a clean evaluation`);

    // Exactly one middle state is permitted, and it has to pay for itself. It exists to end
    // an inconsistency this suite did not catch: capex once reported decision NO_DECISION
    // sitting next to rule_state green — the reading was valid arithmetic on a period that
    // had since been superseded, and neither label said so. The state may only be used when
    // something newer genuinely exists and the gauge admits it in words.
    if (g.decision === 'RULE_EVALUATED_ON_SUPERSEDED_PERIOD') {
      const f = g.freshness_layers;
      assert.ok(g.superseded_note, `${g.id}: superseded evaluation carrying no note`);
      assert.ok(f?.latest_available_period > f?.latest_ingested_period,
        `${g.id}: claims a superseded period while nothing newer is actually available`);
    } else {
      assert.equal(g.decision, 'NO_DECISION',
        `${g.id} is ${g.status.data_state} but was still evaluated`);
    }
  }
});

test('[integrity] counts exclude undecided gauges', () => {
  const t = gauges.henren_rule_tally;
  const colours = (t.green ?? 0) + (t.yellow ?? 0) + (t.red ?? 0);
  assert.equal(colours, t.evaluated, 'colour counts must sum to evaluated, not to total');
  assert.equal(t.evaluated + t.no_decision, t.total);
});

test('[integrity] no composite score is emitted', () => {
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

test('[integrity] every evaluated gauge names a registered source and carries provenance', () => {
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

test('[integrity] a composite gauge inherits its weakest source authority', () => {
  const m2 = gauges.gauges.find((g) => g.id === 'm2gap');
  if (m2 && m2.decision === 'RULE_EVALUATED') {
    assert.equal(m2.status.source_authority, 'UNOFFICIAL_FREE',
      'M2 (FRED) + Nasdaq (Yahoo) must report as the weaker of the two');
  }
});

test('[integrity] proxy gauges declare themselves and name a replacement', () => {
  for (const g of gauges.gauges.filter((x) => x.proxy)) {
    assert.ok(g.proxy_warning, `${g.id} is a proxy without a warning`);
    assert.ok(g.proxy_replacement, `${g.id} is a proxy without a named replacement`);
  }
});

test('[integrity] thresholds this system invented are flagged as ours', () => {
  // Anything not traceable to his own words must say so rather than borrowing his authority.
  for (const g of gauges.gauges.filter((x) => x.henren?.threshold_is_ours)) {
    assert.match(g.henren.quote ?? '', /本系統|非他的原話|未給/,
      `${g.id} claims an invented threshold but its quote does not say so`);
  }
});

test('[integrity] the renderer performs no financial calculation', () => {
  const banned = [
    /Math\.log\s*\(/, /Math\.sqrt\s*\(/, /\*\s*252\b/, /\/\s*1e9\b/,
    /function\s+percentile/, /function\s+rvol/, /\.reduce\([^)]*\+[^)]*value/,
  ];
  for (const re of banned) {
    assert.ok(!re.test(renderer), `renderer contains what looks like a calculation: ${re}`);
  }
});

test('[integrity] dashboard numbers match the engine exactly', { skip: !html }, () => {
  for (const g of gauges.gauges) {
    if (g.decision !== 'RULE_EVALUATED' || g.observed?.value === null) continue;
    assert.ok(html.includes(String(g.observed.value)),
      `${g.id}: engine says ${g.observed.value} but the dashboard does not contain it`);
  }
});

test('[integrity] every gauge the engine produced reaches the page', { skip: !html }, () => {
  // A card went missing in silence: the renderer bucketed on `decision === 'RULE_EVALUATED'`,
  // the engine gained a third decision state, and capex fell through both filters while the
  // summary above it went on counting 13 rules. Nothing failed — the page was simply one
  // card short. A count check alone would not have caught it either, since the counts are
  // read from the engine, not from what was drawn.
  for (const g of gauges.gauges) {
    assert.ok(html.includes(`>${g.label}`) || html.includes(g.label),
      `${g.id} (${g.label}) was computed but never rendered — decision ${g.decision} `
      + 'is not in any bucket the renderer draws');
  }
});

test('[integrity] dashboard states the calculation version it was rendered from', { skip: !html }, () => {
  assert.ok(html.includes(gauges.calculation_version), 'dashboard must show the calc version');
  assert.ok(html.includes(gauges.code_commit), 'dashboard must show the code commit');
});

// The buy/sell scan used to run over the rendered HTML and kept flagging the disclaimer
// that promised no price targets. It now lives in test/contract.test.mjs, against
// structured data, where static copy is a different object rather than an adjacent
// substring. What remains here is only that the guardrail ran at all.
test('[integrity] the output contract was enforced before rendering', () => {
  assert.equal(gauges.output_contract?.valid, true,
    'the engine must refuse to emit a payload that violates its contract');
});

test('[integrity] the Serenity gate escalates only with a citation', { skip: !holdings }, () => {
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

test('[integrity] the gate never reaches an investable conclusion without valuation work', { skip: !holdings }, () => {
  for (const h of holdings.holdings) {
    assert.notEqual(h.serenity_gate?.conclusion?.value, '可投资结论',
      `${h.ticker} reached an investable conclusion; no valuation stage exists yet`);
  }
});

test('[integrity] plausibility findings reach the dashboard, graded by severity', { skip: !holdings || !html }, () => {
  for (const h of holdings.holdings) {
    const p = h.fundamentals?.plausibility;
    if (!p || p.level === 'PASS') continue;
    if (p.structural?.length) {
      assert.ok(html.includes('STRUCTURAL_ERROR'), `${h.ticker} structural error never surfaced`);
    }
    if (p.outliers?.length) {
      assert.ok(html.includes('ECONOMIC_OUTLIER'), `${h.ticker} economic outlier never surfaced`);
    }
  }
});

test('[integrity] an economic outlier blocks nothing, a structural error blocks something', { skip: !holdings }, () => {
  for (const h of holdings.holdings) {
    const p = h.fundamentals?.plausibility;
    if (!p) continue;
    if (p.level === 'ECONOMIC_OUTLIER') {
      assert.deepEqual(p.blocks_metrics, [], `${h.ticker}: an outlier must not block a metric`);
      for (const o of p.outliers) assert.equal(o.advisory_only, true);
    }
    if (p.structural?.length) assert.ok(p.blocks_metrics.length > 0);
  }
});

test('[integrity] concentration is judged on the broad sector, not the niche', { skip: !holdings }, () => {
  const c = holdings.concentration;
  if (c.distinct_niches > c.distinct_sectors) {
    assert.equal(c.same_sector, c.distinct_sectors === 1,
      'niche labels must not be able to manufacture apparent diversification');
  }
});

test('[integrity] display precision is coarser than storage precision, and the exact value survives',
  { skip: !html }, () => {
  for (const g of gauges.gauges) {
    const o = g.observed;
    if (!o || !o.display_rounded) continue;
    assert.notEqual(o.display_value, o.exact_value, `${g.id} claims rounding but the values match`);
    assert.ok(html.includes(String(o.exact_value)),
      `${g.id}: the exact value must remain retrievable in the audit drawer`);
  }
});

test('[integrity] validation status is rendered before the reading, not after it', { skip: !html }, () => {
  // The badge markup must precede the measurement block inside a card.
  const firstCard = html.slice(html.indexOf('<article class="g"'));
  const badge = firstCard.indexOf('vbadge');
  const number = firstCard.indexOf('bignum');
  assert.ok(badge > -1 && number > -1, 'card must contain both a validation badge and a reading');
  assert.ok(badge < number, 'UNTESTED must be read before the number it qualifies');
});

test('[integrity] the front page does not present a red/green market tally', { skip: !html }, () => {
  const head = html.slice(0, html.indexOf('Framework Triggers'));
  for (const banned of ['綠燈</span>', '紅燈</span>']) {
    assert.ok(!head.includes(banned),
      'a colour tally above the fold reads as a market verdict, whatever it is labelled');
  }
  assert.ok(head.includes('經統計驗證的訊號'), 'the front page must state the validated-signal count');
});

test('[integrity] legacy ledger entries are excluded from any performance claim', () => {
  const lines = read('data/predictions.jsonl').trim().split('\n').map((l) => JSON.parse(l));
  for (const p of lines) {
    assert.ok(p.protocol, `${p.prediction_id} has no protocol label`);
    if (p.protocol === 'LEGACY_EXPLORATORY') {
      assert.equal(p.eligible_for_performance, false,
        `${p.prediction_id} is legacy but still counts toward performance`);
    }
  }
});

test('[integrity] an unverified transformation blocks the rule unless sensitivity shows it cannot matter', () => {
  // The original form of this test blocked any gauge whose arithmetic was not fully
  // reconciled. That is blanket contagion, and it was ruled against: one issuer that cannot
  // be reconciled should not freeze an aggregate whose verdict does not turn on it. The
  // exemption is not free, though — it costs a sensitivity test that was actually run and
  // actually came back insensitive, with the unverified components named.
  for (const g of gauges.gauges) {
    if (!g.transformation_validation || g.transformation_validation === 'CHECKED') continue;
    if (g.decision === 'NO_DECISION') continue;

    const r = g.decision_robustness;
    assert.ok(r, `${g.id} evaluated on ${g.transformation_validation} arithmetic `
      + 'with no sensitivity test to justify it');
    assert.equal(r.robustness, 'ROBUST',
      `${g.id} evaluated its rule on ${g.transformation_validation} arithmetic `
      + `while the decision is ${r.robustness} to the unverified part`);
    assert.equal(r.label, 'SENSITIVITY_RANGE',
      'the exemption rests on a sensitivity range; calling it anything probabilistic '
      + 'would claim a model that does not exist');
    assert.ok(r.unverified_components?.length,
      `${g.id}: arithmetic is ${g.transformation_validation} but robustness names nothing unverified`);
  }
});

test('[integrity] the page never claims a capability the engine says it lacks', { skip: !html }, () => {
  // The masthead rendered `data.point_in_time ? '是' : '否'` and printed 「是」, because the
  // engine emits the string 'NOT_IMPLEMENTED' and every non-empty string is truthy. For one
  // render the page advertised point-in-time backtesting directly above a footer explaining
  // it does not exist. Status fields are strings with meaning; treating one as a boolean
  // inverts it silently, so the assertion is on what the reader ends up seeing.
  const mast = html.slice(html.indexOf('<dl class="session">'), html.indexOf('</dl>'));
  assert.ok(mast.includes('Point-in-time'), 'the masthead must state point-in-time status at all');
  if (gauges.point_in_time !== 'IMPLEMENTED') {
    assert.ok(!/Point-in-time<\/dt><dd>是</.test(mast.replace(/\s+/g, '')),
      `engine says point_in_time=${gauges.point_in_time} but the masthead reads 是`);
    assert.ok(mast.includes(gauges.point_in_time),
      'the masthead should name the actual state rather than reduce it to a yes/no');
  }
});

test('[integrity] point-in-time is described as not implemented, never as impossible', () => {
  // Reduced to a structural assertion. The previous version scanned the note's wording and
  // flagged the very sentence establishing compliance — the third instance of that pattern.
  assert.equal(gauges.point_in_time, 'NOT_IMPLEMENTED');
  assert.ok(/尚未實作|NOT_IMPLEMENTED|vintage/.test(gauges.point_in_time_note),
    'the note must say a backtest path exists but is unbuilt');
});

test('[integrity] every plausibility tier is reachable, not just declared', { skip: !holdings }, () => {
  // A three-grade system whose middle grade can never fire is a two-grade system with
  // extra vocabulary. The first version of the reconciliation tier was exactly that:
  // it tested a variable that was hardcoded to null.
  const p = holdings.holdings.find((h) => h.fundamentals?.plausibility)?.fundamentals.plausibility;
  assert.ok(p, 'no plausibility block to inspect');
  for (const tier of ['structural', 'reconciliation', 'outliers']) {
    assert.ok(Array.isArray(p[tier]), `tier ${tier} is not even an array`);
  }
  // The reconciliation tier needs its inputs present, or it is decorative.
  for (const h of holdings.holdings) {
    const f = h.fundamentals;
    if (!f) continue;
    assert.ok(f.liabilities_usd !== undefined,
      `${h.ticker}: reconciliation tier requires liabilities to be fetched at all`);
  }
});

test('[integrity] signal validation is honest about being untested', () => {
  const validated = gauges.gauges.filter((g) => g.status.signal_validation !== 'UNTESTED');
  for (const g of validated) {
    assert.fail(`${g.id} claims ${g.status.signal_validation} — no backtest exists to support that`);
  }
});

test('[integrity] the summary verdict cannot disagree with the gauges underneath it',
  { skip: !html }, () => {
  // The three layer boxes carried a hardcoded colour and headline. When TGA flipped to
  // yellow, the liquidity box went on saying 「平靜」in green — static prose asserting a
  // state the data no longer supported, which is this file's oldest recurring bug.
  const liquidityIds = ['fuel', 'sofr', 'tga', 'rrp', 'hyoas', 'nfci'];
  const rank = { green: 0, yellow: 1, red: 2 };
  const states = gauges.gauges.filter((g) => liquidityIds.includes(g.id) && g.henren?.status)
    .map((g) => g.henren.status);
  if (!states.length) return;
  const worst = states.reduce((a, b) => (rank[b] > rank[a] ? b : a));
  const box = html.slice(html.indexOf('流動性 · 管顛簸'));
  const headline = box.slice(0, box.indexOf('</div>', box.indexOf('vstat')));
  if (worst !== 'green') {
    assert.ok(!headline.includes('var(--ok)'),
      `a liquidity gauge is ${worst} but the summary box is still painted green`);
  }
});

test('[integrity] an intraday price is never labelled as a close', { skip: !html }, () => {
  // Runs during market hours printed 「收在」over a live quote. A price is a close or it
  // is not, and the label has to follow the session rather than the habit.
  if (gauges.market_session?.us_market !== 'OPEN') return;
  const verdict = html.slice(html.indexOf('class="verdict"'), html.indexOf('Framework Triggers'));
  assert.ok(!verdict.includes('標普收在'),
    'the market is open, so the headline price is intraday and must not be called a close');
  assert.ok(verdict.includes('標普現價'), 'an open session must say so');
});

test('[integrity] a rule band either comes from his words or is marked as ours', { skip: !html }, () => {
  // The SOFR gauge carried bands of green <1 / yellow 1-3 / red >=3 while his quote, printed
  // directly underneath it, said 「黃色預警是利差衝過三個基點」. His yellow had been redrawn as
  // this system's red, and a yellow invented at 1bp he never mentioned — with no
  // threshold_is_ours flag. That is borrowing his authority for a line he did not draw, and
  // it is worse than an invented threshold that admits it, because the quote makes it look
  // sourced. Every numeric band must either be traceable to the quote or declared as ours.
  for (const g of gauges.gauges) {
    const h = g.henren;
    if (!h?.thresholds || h.threshold_is_ours) continue;
    // He speaks numbers, so the quote writes them the way a person says them: 「衝過三個基點」
    // carries the same 3 that the threshold does. Normalise the quote before comparing, or
    // the check flags a threshold that IS traceable and pushes toward the wrong fix —
    // relabelling his line as ours to make a test pass would be exactly backwards.
    const CN = { 零: '0', 一: '1', 二: '2', 兩: '2', 三: '3', 四: '4', 五: '5',
      六: '6', 七: '7', 八: '8', 九: '9', 十: '10' };
    const quote = (h.quote ?? '').replace(/[零一二兩三四五六七八九十]/g, (c) => CN[c]);
    for (const [band, text] of Object.entries(h.thresholds)) {
      const numbers = String(text).match(/\d+(?:\.\d+)?/g) ?? [];
      for (const n of numbers) {
        assert.ok(quote.includes(n) || /本系統|他未給|未給|沒有給/.test(String(text)),
          `${g.id}.${band} uses ${n}, which appears nowhere in his quote and is not `
          + 'declared as this system\'s own line');
      }
    }
  }
});
