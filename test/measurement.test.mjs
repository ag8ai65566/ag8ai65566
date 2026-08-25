// Category: MEASUREMENT VALIDITY.
// Not "is the arithmetic right" (that is integrity) and not "does the signal predict"
// (that is validation). This layer asks the question the fourth review named as the
// current bottleneck: **under this label, which financial concept are we actually measuring?**

import { test } from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync, existsSync, readdirSync } from 'node:fs';
import { join, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';
import { fetchFundamentals } from '../lib/fundamentals.mjs';
import { expectedLatestPeriod, quarterLabel, decisionRobustness } from '../lib/capex-freshness.mjs';

const repo = join(dirname(fileURLToPath(import.meta.url)), '..');
const read = (p) => readFileSync(join(repo, p), 'utf8');
const gauges = JSON.parse(read('data/gauges.json'));
const concepts = JSON.parse(read('config/concepts.json'));
const capex = gauges.gauges.find((g) => g.id === 'capex');

test('[measurement] every issuer in an aggregate maps to the same financial concept', () => {
  const contract = concepts.concepts.CASH_PPE_CAPEX;
  const variants = contract.known_tag_variants;
  // Amazon uses a different tag for the same concept. The contract must key on the
  // concept and list tags as variants, never the other way round.
  assert.notEqual(variants.AMZN, variants.MSFT,
    'the fixture is pointless if all four happen to share a tag');
  assert.equal(contract.includes_finance_lease_principal, false,
    'cash PP&E must not silently include finance-lease principal');
  assert.equal(concepts.concepts.INFRASTRUCTURE_CAPEX_BROAD.includes_finance_lease_principal, true);
  assert.notEqual(concepts._selection.hyperscaler_capex_series, 'INFRASTRUCTURE_CAPEX_BROAD',
    'the series in use must be the one every issuer reports comparably');
});

test('[measurement] the known concept gap is disclosed, not silently carried', () => {
  assert.ok(concepts._selection.gap_disclosed,
    'excluding finance leases understates infrastructure spend; that must be stated');
  assert.ok(capex.layers.B_finance_leases.startsWith('NOT_WIRED'));
});

test('[measurement] an ingestion gap cannot be reported as source lag', () => {
  const f = capex.freshness_layers;
  assert.ok(f, 'capex must carry the three freshness layers');
  for (const k of ['latest_expected_period', 'latest_available_period', 'latest_ingested_period']) {
    assert.ok(f[k], `missing ${k}`);
  }
  if (f.latest_available_period > f.latest_ingested_period) {
    assert.equal(f.state, 'INGESTION_OVERDUE',
      'available beyond ingested is an ingestion problem, whatever the source cadence is');
    assert.notEqual(capex.status.data_state, 'LAGGED_BY_DESIGN',
      '"the source is slow" must never cover for "the pipeline did not pick this up"');
  }
});

test('[measurement] expectedLatestPeriod tracks the calendar, not the last fetch', () => {
  // Mid-August: Q2 has ended and the reporting window has passed, so Q2 is expected.
  assert.equal(quarterLabel(expectedLatestPeriod(new Date('2026-08-10T00:00:00Z'))), '2026-Q2');
  // Early April: Q1 ended days ago and nobody has filed yet, so Q4 of last year still stands.
  assert.equal(quarterLabel(expectedLatestPeriod(new Date('2026-04-05T00:00:00Z'))), '2025-Q4');
});

test('[measurement] coverage figures are never labelled as confidence', () => {
  const c = capex.coverage;
  assert.ok(c, 'capex must report evidence coverage');
  for (const k of Object.keys(c)) {
    assert.ok(!/confidence|probability|certainty/i.test(k), `coverage key ${k} implies probability`);
  }
  assert.ok(c.aggregate_measurement_status);
  assert.ok(c._naming_rule.includes('not a confidence'));
});

test('[measurement] the rule is blocked only when the unverified part could flip it', () => {
  const r = capex.decision_robustness;
  assert.ok(['ROBUST', 'SENSITIVE', 'UNKNOWN'].includes(r.robustness));
  assert.equal(r.label, 'SENSITIVITY_RANGE', 'never a confidence interval — no model backs it');
  if (r.robustness === 'SENSITIVE' || r.robustness === 'UNKNOWN') {
    assert.equal(capex.decision, 'NO_DECISION');
  } else {
    assert.notEqual(capex.decision, 'NO_DECISION',
      'blanket contagion was the thing the review ruled against');
  }
});

test('[measurement] robustness actually flips when a component dominates the change', () => {
  // A component at 15% of the level can be the whole of the movement — the exact reason
  // amount coverage must not stand in for confidence.
  const series = [
    { period_end: '2026-03-31', parts: [{ ticker: 'A', val: 85 }, { ticker: 'B', val: 15 }] },
    { period_end: '2026-06-30', parts: [{ ticker: 'A', val: 85 }, { ticker: 'B', val: 16 }] },
  ];
  const r = decisionRobustness({ series, unverifiedTickers: ['B'], shockPct: 0.25,
    ruleFn: (qoq) => (qoq < 0 ? 'ROLLED_OVER' : 'NOT_ROLLED_OVER') });
  assert.equal(r.robustness, 'SENSITIVE',
    'a 15% component swinging ±25% straddles zero growth here, so the verdict must flip');
});

test('[measurement] a gauge evaluated on a superseded period says so', () => {
  if (capex.decision !== 'RULE_EVALUATED_ON_SUPERSEDED_PERIOD') return;
  assert.ok(capex.superseded_note, 'the reading is valid but no longer the latest — say it');
  assert.ok(capex.ingestion_alert);
  assert.ok(capex.henren?.status, 'a superseded evaluation is still an evaluation');
});

test('[measurement] as-of query hides filings that had not been made yet', async () => {
  // `filed` was stored and the registry claimed point-in-time metadata, but no as-of query
  // had ever been run — a capability asserted and never exercised. Sandisk's quarter ending
  // 2026-06-30 was filed 2026-08-06, so a model standing on 2026-07-15 must not see it.
  const asOf = '2026-07-15';
  const f = await fetchFundamentals('SNDK', '0002012383', { asOf });
  for (const [name, c] of Object.entries(f.concepts)) {
    for (const p of c.series) {
      assert.ok(p.filed <= asOf,
        `${name}: fact filed ${p.filed} leaked into an as-of ${asOf} view`);
    }
  }
  const rev = f.concepts.revenue?.series.at(-1);
  assert.ok(rev, 'as-of view should still contain earlier filings');
  assert.ok(rev.end < '2026-06-30',
    `as-of ${asOf} must not reach the quarter ending 2026-06-30; got ${rev.end}`);
});

test('[measurement] snapshot history is being written for behaviour diagnostics', () => {
  const dir = join(repo, 'data', 'snapshots');
  assert.ok(existsSync(dir), 'snapshots directory must exist — behaviour diagnostics need it');
  const files = readdirSync(dir).filter((f) => f.endsWith('.json'));
  assert.ok(files.length >= 1, 'at least one snapshot');
  const snap = JSON.parse(read(join('data', 'snapshots', files.at(-1))));
  for (const g of snap.gauges) {
    for (const k of ['id', 'value', 'rule_state', 'data_state', 'decision']) {
      assert.ok(k in g, `snapshot gauge missing ${k}`);
    }
  }
});

test('[measurement] a gauge about to go dark warns before it goes, not after', () => {
  // When a reading ages past its SLA it becomes NO_DECISION and the red count drops by one.
  // A falling red count looks exactly like a risk receding, and it is the opposite: the
  // gauge went dark. So the warning has to exist while the number is still on the page.
  for (const g of gauges.gauges) {
    const c = g.sla_countdown;
    if (!c) continue;
    assert.ok(c.days_until_no_decision >= 0, `${g.id}: already expired but still counting down`);
    assert.ok(c.days_until_no_decision < c.publication_period_days,
      `${g.id}: warned with ${c.days_until_no_decision} days left against a `
      + `${c.publication_period_days}-day cadence — the next release lands first, so there `
      + 'is nothing to warn about');
    assert.ok(c.tally_note.includes('不代表'),
      `${g.id}: the countdown must say what the falling tally does NOT mean`);
    assert.equal(g.decision === 'NO_DECISION', false,
      `${g.id}: a countdown on an already-undecided gauge is noise`);
  }
});

test('[measurement] the countdown fires on lateness that only a person can fix', () => {
  // The first version warned on ten gauges, most of them daily FRED series three days from
  // a five-day SLA — a state they are in every single run. A warning that is always on is
  // wallpaper. The condition worth surfacing is that the reading expires BEFORE its source
  // is next due to publish, which no amount of waiting resolves.
  const warned = gauges.gauges.filter((g) => g.sla_countdown);
  const daily = warned.filter((g) => g.sla_countdown.publication_period_days <= 1);
  assert.equal(daily.length, 0,
    `a daily series can always be refreshed tomorrow; warning about it is noise: `
    + daily.map((g) => g.id).join(', '));
});
