// Category: OUTPUT CONTRACT.
// Replaces the HTML keyword scan. Guardrails run against structured data before rendering,
// so a system claim and a piece of static copy are different objects rather than adjacent
// substrings — which is what let the old scan flag its own disclaimer three times.

import { test } from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { join, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';
import { validateOutput, FORBIDDEN_KEYS, PROSE_FIELDS } from '../lib/output-contract.mjs';

const repo = join(dirname(fileURLToPath(import.meta.url)), '..');
const gauges = JSON.parse(readFileSync(join(repo, 'data/gauges.json'), 'utf8'));

test('[contract] the committed output satisfies its own contract', () => {
  const r = validateOutput(gauges);
  assert.equal(r.valid, true, `violations: ${JSON.stringify(r.violations, null, 2)}`);
});

test('[contract] the engine records its contract check in the payload', () => {
  assert.equal(gauges.output_contract?.valid, true);
  assert.deepEqual(gauges.output_contract.violations, []);
});

test('[contract] a forbidden key is rejected, not ignored', () => {
  const bad = structuredClone(gauges);
  bad.gauges[0].target_price = 1234;
  const r = validateOutput(bad);
  assert.equal(r.valid, false);
  assert.ok(r.violations.some((v) => v.type === 'FORBIDDEN_KEY'),
    'a renderer that silently drops the key would hide that the producer already broke contract');
});

test('[contract] an undeclared key fails, so new fields get reviewed before shipping', () => {
  const bad = structuredClone(gauges);
  bad.gauges[0].some_new_field = 'whatever';
  const r = validateOutput(bad);
  assert.ok(r.violations.some((v) => v.type === 'UNKNOWN_KEY'));
});

test('[contract] advisory prose is caught in prose fields, including the phrasing regex missed', () => {
  // The review pointed out that "這個位置的風險報酬比很有吸引力" walks straight past a
  // BUY/SELL keyword scan. It is caught here because the check knows which field can carry
  // generated prose and looks for the construction, not the vocabulary.
  for (const phrase of ['目前風險報酬比極具吸引力', 'STRONG BUY', '建議加碼']) {
    const r = validateOutput({ gauges: [], commentary: phrase });
    assert.ok(r.violations.some((v) => v.type === 'ADVISORY_LANGUAGE'),
      `advisory phrase not caught: ${phrase}`);
  }
});

test('[contract] static disclaimer copy is out of scope by construction', () => {
  // This is the whole point. A disclaimer saying the system emits no price targets must
  // never trip the guardrail, and it cannot, because it is not a scanned prose field.
  const payload = {
    gauges: [],
    no_composite_score: '本系統不輸出任何綜合分數。',
    point_in_time_note: '這是尚未實作，不是結構上不可能。',
    disclaimer: '本工具不輸出買賣訊號、目標價或部位建議。',
  };
  const r = validateOutput(payload);
  assert.equal(r.valid, true,
    `static copy must not be scanned; got ${JSON.stringify(r.violations)}`);
});

test('[contract] the forbidden list covers the shapes a recommendation could take', () => {
  for (const k of ['recommendation', 'target_price', 'position_size', 'expected_return', 'rating']) {
    assert.ok(FORBIDDEN_KEYS.has(k), `${k} should be forbidden`);
  }
  assert.ok(PROSE_FIELDS.length > 0, 'there must be a declared prose surface to scan');
});
