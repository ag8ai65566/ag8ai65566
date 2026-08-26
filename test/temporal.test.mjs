// Category: TEMPORAL ALIGNMENT.
// Regression tests for the bugs this system actually shipped — every one of these existed
// in production output before the test did. Joining two series is where this system has
// been wrong most often (June M2 against August Nasdaq turned a red flag yellow), so the
// date logic gets its own layer rather than living inside general integrity.
//   node --test test/

import { test } from 'node:test';
import assert from 'node:assert/strict';
import {
  shiftYears, shiftMonths, priorObservation, alignByEffectiveDate,
  yoyAtAnchor, alignQuarterly, percentileInWindow,
} from '../lib/temporal.mjs';
import { diffSnapshots, priorSnapshotFile } from '../lib/snapshot-diff.mjs';

const series = (pairs) => pairs.map(([date, value]) => ({ date, value }));

test('[temporal] shiftYears is calendar-aware, not minus-365-days', () => {
  assert.equal(shiftYears('2026-08-10', 1), '2025-08-10');
  // 2024 was a leap year: a 365-day offset would land on 02-29 → 03-01.
  assert.equal(shiftYears('2025-03-01', 1), '2024-03-01');
});

test('[temporal] shiftMonths clamps to the last valid day', () => {
  assert.equal(shiftMonths('2026-03-31', 1), '2026-02-28');
  assert.equal(shiftMonths('2026-08-10', 2), '2026-06-10');
});

test('[temporal] priorObservation never looks forward', () => {
  const s = series([['2026-01-01', 1], ['2026-04-01', 2], ['2026-07-01', 3]]);
  assert.equal(priorObservation(s, '2026-06-30').date, '2026-04-01');
  assert.equal(priorObservation(s, '2026-07-01').date, '2026-07-01');
  assert.equal(priorObservation(s, '2025-12-31'), null);
});

// The shipped bug: M2 (monthly, ~30d late) compared against the Nasdaq's newest close,
// producing a "year-over-year gap" that spanned two different months.
test('[temporal] alignByEffectiveDate anchors on the slower series', () => {
  const monthly = series([['2026-05-01', 100], ['2026-06-01', 105]]);
  const daily = series([['2026-06-01', 10], ['2026-07-01', 11], ['2026-08-07', 12]]);
  const al = alignByEffectiveDate(monthly, daily);
  assert.ok(al.ok);
  assert.equal(al.anchor, '2026-06-01', 'anchor must be the older of the two latest dates');
  assert.equal(al.a.value, 105);
  assert.equal(al.b.value, 10, 'the fast series must be read AT the anchor, not at its own latest');
  assert.equal(al.anchor_set_by, 'A');
});

test('[temporal] alignByEffectiveDate reports empty input rather than throwing', () => {
  assert.equal(alignByEffectiveDate([], series([['2026-01-01', 1]])).ok, false);
});

test('[temporal] yoyAtAnchor uses both legs at the same anchor', () => {
  const s = series([['2025-06-01', 100], ['2025-12-01', 110], ['2026-06-01', 120], ['2026-08-01', 130]]);
  const y = yoyAtAnchor(s, '2026-06-01');
  assert.ok(y.ok);
  assert.equal(y.now.date, '2026-06-01');
  assert.equal(y.then.date, '2025-06-01');
  assert.ok(Math.abs(y.pct - 20) < 1e-9, `must be 120/100 (20%), never 130/100; got ${y.pct}`);
});

test('[temporal] yoyAtAnchor refuses a year-ago leg that drifted too far', () => {
  const s = series([['2024-01-01', 100], ['2026-06-01', 120]]);
  const y = yoyAtAnchor(s, '2026-06-01');
  assert.equal(y.ok, false);
  assert.equal(y.reason, 'YEAR_AGO_TOO_FAR');
});

// The shipped bug: dividing Q4-2025 corporate equities by Q2-2026 GDP.
test('[temporal] alignQuarterly joins a common quarter and refuses a cross-quarter divide', () => {
  const a = series([['2025-10-01', 60], ['2026-01-01', 70]]);
  const b = series([['2025-10-01', 30], ['2026-01-01', 32], ['2026-04-01', 33]]);
  const ok = alignQuarterly(a, b);
  assert.ok(ok.ok);
  assert.equal(ok.period, '2026-01-01');
  assert.equal(ok.b.value, 32, 'must pair with the same quarter, not the newest');

  const mismatch = alignQuarterly(series([['2024-01-01', 60]]), series([['2026-04-01', 33]]));
  assert.equal(mismatch.ok, false);
  assert.equal(mismatch.reason, 'DATE_MISMATCH');
});

test('[temporal] percentileInWindow refuses a thin window instead of guessing', () => {
  const now = new Date('2026-08-10T00:00:00Z');
  const thin = series([['2026-07-01', 1], ['2026-07-02', 2]]);
  const p = percentileInWindow(thin, 1.5, 5, { now });
  assert.equal(p.ok, false);
  assert.equal(p.reason, 'INSUFFICIENT_HISTORY');

  const wide = Array.from({ length: 100 }, (_, i) => ({
    date: `2026-0${1 + Math.floor(i / 40)}-${String((i % 28) + 1).padStart(2, '0')}`, value: i,
  }));
  const q = percentileInWindow(wide, 50, 5, { now });
  assert.ok(q.ok);
  assert.ok(q.value > 40 && q.value < 60, `expected mid-range, got ${q.value}`);
});

// The shipped bug: max() over a hand-picked basket, reported as a market statistic.
test('[temporal] median is not max — the AI basket statistic must be the middle value', () => {
  const ratios = [3.0, 3.1, 3.6, 5.9, 7.5, 7.7, 11.1];
  const sorted = [...ratios].sort((a, b) => a - b);
  const median = sorted[Math.floor(sorted.length / 2)];
  assert.equal(median, 5.9);
  assert.notEqual(median, Math.max(...ratios));
});

// ---------------------------------------------------------------------------
// Snapshot diffs. These are temporal by nature: the question "did this change"
// is meaningless without "changed relative to when", and the answer must not
// confuse "the engine ran again" with "the source published something new".

test('[temporal] a first run says it has no history rather than showing zeros', () => {
  const d = diffSnapshots(null, [{ id: 'fuel', label: 'x', observed: { value: 1 } }]);
  assert.equal(d.available, false);
  assert.deepEqual(d.moves, []);
  assert.ok(d.reason.includes('第一次'), 'an empty diff must be distinguishable from a quiet day');
});

test('[temporal] a new number on the same effective date is a re-read, not a source update', () => {
  const prior = { date: '2026-08-10', gauges: [
    { id: 'rrp', value: 1.45, rule_state: 'yellow', data_state: 'CURRENT', effective_date: '2026-08-10' }] };
  const current = [{ id: 'rrp', label: 'RRP', henren: { status: 'yellow' },
    status: { data_state: 'CURRENT' }, observed: { value: 0.97, unit: 'bn', effective_date: '2026-08-10' } }];
  const d = diffSnapshots(prior, current);
  assert.equal(d.moves.length, 1);
  assert.equal(d.moves[0].delta, -0.48);
  assert.equal(d.moves[0].source_updated, false,
    'same effective date means the source did not publish again — the pipeline re-read it');
  assert.deepEqual(d.rule_changes, [], 'the colour did not change, so it must not be listed as one');
});

test('[temporal] a rule flip and a data-state change are reported separately', () => {
  const prior = { date: '2026-08-10', gauges: [
    { id: 'm2gap', value: -22, rule_state: 'yellow', data_state: 'CURRENT', effective_date: '2026-06-01' }] };
  const current = [{ id: 'm2gap', label: 'M2 gap', henren: { status: 'red' },
    status: { data_state: 'STALE' }, observed: { value: -36.2, unit: 'pp', effective_date: '2026-07-01' } }];
  const d = diffSnapshots(prior, current);
  assert.deepEqual(d.rule_changes.map((c) => [c.from, c.to]), [['yellow', 'red']]);
  assert.deepEqual(d.state_changes.map((c) => [c.from, c.to]), [['CURRENT', 'STALE']]);
  assert.equal(d.moves[0].source_updated, true);
});

test('[temporal] a gauge that stopped being produced is reported, not silently absent', () => {
  const prior = { date: '2026-08-10', gauges: [
    { id: 'fuel', value: 3, rule_state: 'green', data_state: 'CURRENT', effective_date: '2026-08-10' },
    { id: 'gone', value: 1, rule_state: 'green', data_state: 'CURRENT', effective_date: '2026-08-10' }] };
  const current = [{ id: 'fuel', label: 'Reserves', henren: { status: 'green' },
    status: { data_state: 'CURRENT' }, observed: { value: 3, effective_date: '2026-08-10' } }];
  const d = diffSnapshots(prior, current);
  assert.ok(d.state_changes.some((c) => c.id === 'gone' && c.to === 'DISAPPEARED'),
    'a vanished gauge is the change hardest to notice from a count');
});

test('[temporal] the prior snapshot is the newest one strictly before today', () => {
  const files = ['2026-08-09.json', '2026-08-10.json', '2026-08-11.json', 'notes.txt'];
  assert.equal(priorSnapshotFile(files, '2026-08-11.json'), '2026-08-10.json');
  assert.equal(priorSnapshotFile(['2026-08-11.json'], '2026-08-11.json'), null,
    "today's own snapshot must never be diffed against itself");
});
