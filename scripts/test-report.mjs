#!/usr/bin/env node
// Runs the suite and writes data/test-report.json, grouped by the category each test
// belongs to.
//
// Why grouping matters more than the total. "52 tests passing" is a number that sounds
// like assurance and carries almost none: it says nothing about WHICH question was
// answered. This system's tests answer four different questions, and only the first two
// are anywhere near complete:
//
//   TEMPORAL     — are two series joined at the same point in time?
//   INTEGRITY    — does the rendered page equal what the engine computed?
//   CONTRACT     — can the output carry a recommendation, a score, or advisory prose?
//   MEASUREMENT  — under this label, which financial concept is actually being measured?
//
// There is deliberately no VALIDATION category, and its absence is the honest headline:
// nothing here tests whether any signal predicts anything. A green suite means the
// pipeline is faithful, not that the framework works.

import { spawnSync } from 'node:child_process';
import { writeFileSync, readdirSync } from 'node:fs';
import { join, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';

const repo = join(dirname(fileURLToPath(import.meta.url)), '..');

const CATEGORIES = {
  temporal: { label: '時間對齊', asks: '兩條序列是不是在同一個時間點上被比較？',
    why: '這一層的每個測試都對應一個真的出過的錯 —— 六月的 M2 對上八月的那斯達克，'
      + '把一個紅燈壓成黃燈。' },
  integrity: { label: '計算一致性', asks: '畫面上的數字，是不是引擎算出來的那一個？',
    why: 'renderer 不准做任何金融運算，連 /1e9 和四捨五入都不行。這一層負責讓這條規則'
      + '不只是註解。' },
  contract: { label: '輸出契約', asks: '這份輸出有沒有可能夾帶買賣建議、目標價或綜合評分？',
    why: '在結構化資料上檢查，不是掃 HTML —— 舊做法連續三次抓到自己的免責聲明。' },
  measurement: { label: '量測效度', asks: '這個標籤底下，量到的到底是哪一個財務概念？',
    why: '第四次審查指出這是目前的瓶頸：算對了，不代表算的是你以為的那個東西。' },
};

const files = readdirSync(join(repo, 'test')).filter((f) => f.endsWith('.test.mjs'));
const res = spawnSync('node', ['--test', ...files.map((f) => join('test', f))],
  { cwd: repo, encoding: 'utf8', maxBuffer: 32 * 1024 * 1024 });
const out = `${res.stdout}\n${res.stderr}`;

// TAP lines: "ok 12 - [integrity] ..." / "not ok 12 - [integrity] ..."
const cases = [];
for (const line of out.split('\n')) {
  const m = /^(not ok|ok) \d+ - (?:\[(\w+)\] )?(.+?)(?: # SKIP.*)?$/.exec(line.trim());
  if (!m) continue;
  cases.push({ passed: m[1] === 'ok', category: m[2] ?? 'uncategorised', name: m[3].trim() });
}

const categories = Object.entries(CATEGORIES).map(([key, meta]) => {
  const mine = cases.filter((c) => c.category === key);
  return { key, ...meta, total: mine.length, passed: mine.filter((c) => c.passed).length,
    failed: mine.filter((c) => !c.passed).map((c) => c.name) };
});
const uncategorised = cases.filter((c) => !(c.category in CATEGORIES));

const report = {
  generated_at: new Date().toISOString(),
  total: cases.length,
  passed: cases.filter((c) => c.passed).length,
  exit_code: res.status,
  categories,
  uncategorised: uncategorised.map((c) => c.name),
  absent_category: {
    key: 'validation',
    label: '訊號驗證',
    asks: '這些門檻在歷史上真的能分辨後續報酬嗎？',
    state: 'NO_TESTS_EXIST',
    why: '這一格是空的，而且空得很重要。全部通過只證明管線忠實，不證明框架有效。'
      + '要填滿它需要的是回測與樣本外檢驗，不是再多寫幾個單元測試。',
  },
  reading: '測試分類比總數誠實。通過的是「管線有沒有騙人」，沒有測的是「訊號準不準」。',
};

writeFileSync(join(repo, 'data', 'test-report.json'), `${JSON.stringify(report, null, 2)}\n`);

for (const c of categories) {
  console.log(`${c.passed === c.total ? '✅' : '❌'} ${c.key.padEnd(12)} ${c.passed}/${c.total}  ${c.asks}`);
}
console.log(`⬜ validation   0/0   ${report.absent_category.asks}`);
console.log(`\n共 ${report.passed}/${report.total} 通過`);
if (uncategorised.length) console.log(`未分類：${uncategorised.length} 筆`);
process.exit(res.status === 0 ? 0 : 1);
