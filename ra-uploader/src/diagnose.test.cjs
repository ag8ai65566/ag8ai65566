/* Thresholds of the day/month diagnostic, tested directly on synthetic
   populations so this runs without the weekly source files. */
require('./core.js');
const C = globalThis.RACore;

let pass = 0, fail = 0;
const check = (name, got, want) => {
  const ok = JSON.stringify(got) === JSON.stringify(want);
  console.log((ok ? '  PASS  ' : '  FAIL  ') + name + (ok ? '' : `  got ${JSON.stringify(got)} want ${JSON.stringify(want)}`));
  ok ? pass++ : fail++;
};

/* Build rows whose ETA cells are date-typed and ATA cells text-typed,
   in the proportions a given scenario produces. */
function makeRows(realTotal, realGt12, textTotal, textGt12) {
  const columns = { eta: 0, ata: 1 };
  const rows = [];
  const dateCell = day => ({ kind: 'serial-date', date: new Date(Date.UTC(2026, 5, day)) });
  const textCell = day => ({ kind: 'text-date', date: new Date(Date.UTC(2026, 5, day)) });
  const n = Math.max(realTotal, textTotal);
  for (let i = 0; i < n; i++) {
    const cells = [];
    cells[0] = i < realTotal ? dateCell(i < realGt12 ? 20 : 5) : { kind: 'empty' };
    cells[1] = i < textTotal ? textCell(i < textGt12 ? 20 : 5) : { kind: 'empty' };
    rows.push({ excelRow: i + 2, cells: cells });
  }
  return { rows, columns };
}
const diag = (...a) => { const { rows, columns } = makeRows(...a); return C.diagnose(rows, columns); };

console.log('\n=== the classic defect: no date cell past the 12th ===');
{
  const d = diag(670, 0, 1149, 1149);
  check('flagged corrupted', d.corrupted, true);
  check('not merely partial', d.partial, false);
}

console.log('\n=== 19 Nov 2026: swapped, but a few cells untouched ===');
{
  /* 15 of 2138 date cells (0.7%) fell past the 12th. Requiring zero
     exceptions classified this as only suspicious and left the dates
     uncorrected, so the threshold is proportional. */
  const d = diag(2138, 15, 3064, 3064);
  check('flagged corrupted', d.corrupted, true);
  check('gt12 share reported', +(d.gt12Share * 100).toFixed(1), 0.7);
}

console.log('\n=== a clean file must stay clean ===');
{
  const d = diag(2013, 1299, 79, 51);   /* 64.5% past the 12th */
  check('not corrupted', d.corrupted, false);
  check('not partial', d.partial, false);
}
{
  const d = diag(1150, 700, 1717, 1717); /* 60.9%, all text past the 12th */
  check('natural rate stays clean even with separated text', d.corrupted, false);
}

console.log('\n=== the band between: flagged, never auto-corrected ===');
{
  const d = diag(1000, 250, 500, 500);   /* 25% - below natural, above the swap line */
  check('not corrupted', d.corrupted, false);
  check('is partial', d.partial, true);
}

console.log('\n=== boundaries ===');
check('14.9% is corrupted', diag(1000, 149, 500, 500).corrupted, true);
check('15.0% is not', diag(1000, 150, 500, 500).corrupted, false);
check('39.9% is partial', diag(1000, 399, 500, 500).partial, true);
check('40.0% is clean', diag(1000, 400, 500, 500).partial, false);

console.log('\n=== guards ===');
check('too few date cells to judge', diag(19, 0, 100, 100).corrupted, false);
check('no text column to compare against', diag(1000, 0, 0, 0).corrupted, false);
check('text not separated -> not the defect', diag(1000, 0, 500, 250).corrupted, false);

console.log(`\n${pass} passed, ${fail} failed\n`);
process.exit(fail ? 1 : 0);
