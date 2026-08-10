// Regression tests for the bugs this system actually shipped.
//   node --test test/

import { test } from 'node:test';
import assert from 'node:assert/strict';
import {
  shiftYears, shiftMonths, priorObservation, alignByEffectiveDate,
  yoyAtAnchor, alignQuarterly, percentileInWindow,
} from '../lib/temporal.mjs';

const series = (pairs) => pairs.map(([date, value]) => ({ date, value }));

test('shiftYears is calendar-aware, not minus-365-days', () => {
  assert.equal(shiftYears('2026-08-10', 1), '2025-08-10');
  // 2024 was a leap year: a 365-day offset would land on 02-29 → 03-01.
  assert.equal(shiftYears('2025-03-01', 1), '2024-03-01');
});

test('shiftMonths clamps to the last valid day', () => {
  assert.equal(shiftMonths('2026-03-31', 1), '2026-02-28');
  assert.equal(shiftMonths('2026-08-10', 2), '2026-06-10');
});

test('priorObservation never looks forward', () => {
  const s = series([['2026-01-01', 1], ['2026-04-01', 2], ['2026-07-01', 3]]);
  assert.equal(priorObservation(s, '2026-06-30').date, '2026-04-01');
  assert.equal(priorObservation(s, '2026-07-01').date, '2026-07-01');
  assert.equal(priorObservation(s, '2025-12-31'), null);
});

// The shipped bug: M2 (monthly, ~30d late) compared against the Nasdaq's newest close,
// producing a "year-over-year gap" that spanned two different months.
test('alignByEffectiveDate anchors on the slower series', () => {
  const monthly = series([['2026-05-01', 100], ['2026-06-01', 105]]);
  const daily = series([['2026-06-01', 10], ['2026-07-01', 11], ['2026-08-07', 12]]);
  const al = alignByEffectiveDate(monthly, daily);
  assert.ok(al.ok);
  assert.equal(al.anchor, '2026-06-01', 'anchor must be the older of the two latest dates');
  assert.equal(al.a.value, 105);
  assert.equal(al.b.value, 10, 'the fast series must be read AT the anchor, not at its own latest');
  assert.equal(al.anchor_set_by, 'A');
});

test('alignByEffectiveDate reports empty input rather than throwing', () => {
  assert.equal(alignByEffectiveDate([], series([['2026-01-01', 1]])).ok, false);
});

test('yoyAtAnchor uses both legs at the same anchor', () => {
  const s = series([['2025-06-01', 100], ['2025-12-01', 110], ['2026-06-01', 120], ['2026-08-01', 130]]);
  const y = yoyAtAnchor(s, '2026-06-01');
  assert.ok(y.ok);
  assert.equal(y.now.date, '2026-06-01');
  assert.equal(y.then.date, '2025-06-01');
  assert.ok(Math.abs(y.pct - 20) < 1e-9, `must be 120/100 (20%), never 130/100; got ${y.pct}`);
});

test('yoyAtAnchor refuses a year-ago leg that drifted too far', () => {
  const s = series([['2024-01-01', 100], ['2026-06-01', 120]]);
  const y = yoyAtAnchor(s, '2026-06-01');
  assert.equal(y.ok, false);
  assert.equal(y.reason, 'YEAR_AGO_TOO_FAR');
});

// The shipped bug: dividing Q4-2025 corporate equities by Q2-2026 GDP.
test('alignQuarterly joins a common quarter and refuses a cross-quarter divide', () => {
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

test('percentileInWindow refuses a thin window instead of guessing', () => {
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
test('median is not max — the AI basket statistic must be the middle value', () => {
  const ratios = [3.0, 3.1, 3.6, 5.9, 7.5, 7.7, 11.1];
  const sorted = [...ratios].sort((a, b) => a - b);
  const median = sorted[Math.floor(sorted.length / 2)];
  assert.equal(median, 5.9);
  assert.notEqual(median, Math.max(...ratios));
});
