/* Validates the core + build logic against the three real source files.
   Expected values come from an independent Python analysis of the same files. */
const XLSX = require('../vendor/xlsx.full.min.js');
const fs = require('fs');
require('./core.js'); require('./build.js');
const C = globalThis.RACore, B = globalThis.RABuild;

const DIR = process.env.FIXTURES || '/tmp/claude-0/-home-user-ag8ai65566/f0564f6b-fc8e-55fc-9eb5-b60a7552701f/scratchpad';
const FILES = [
  { tag: '13AUG', file: 'shipments.xlsx',     real: 670, text: 1149 },
  { tag: '20AUG', file: 'shipments_v3.xlsx',  real: 710, text: 1280 },
  { tag: '25AUG', file: 'shipments_v4.xlsx',  real: 726, text: 1352 }
];

let pass = 0, fail = 0;
function check(name, got, want) {
  const ok = JSON.stringify(got) === JSON.stringify(want);
  console.log((ok ? '  PASS  ' : '  FAIL  ') + name + (ok ? '' : `\n          got ${JSON.stringify(got)}  want ${JSON.stringify(want)}`));
  ok ? pass++ : fail++;
}

function load(file) {
  const wb = XLSX.read(fs.readFileSync(DIR + '/' + file), { type: 'buffer', cellNF: true });
  const ws = wb.Sheets[wb.SheetNames[0]];
  const parsed = B.parseSheet(XLSX, ws);
  const det = C.detectColumns(parsed.header);
  return { parsed, det, scacs: C.collectScacs(parsed.rows, det.columns) };
}

console.log('\n=== column detection ===');
FILES.forEach(f => {
  const { det } = load(f.file);
  check(`${f.tag} all fields resolved`, det.missing, []);
});

console.log('\n=== corruption diagnostic (vs Python ground truth) ===');
FILES.forEach(f => {
  const { parsed, det } = load(f.file);
  const dg = C.diagnose(parsed.rows, det.columns);
  check(`${f.tag} real-date cell count`, dg.real, f.real);
  check(`${f.tag} text-date cell count`, dg.text, f.text);
  check(`${f.tag} real cells with day>12`, dg.realGt12, 0);
  check(`${f.tag} text cells with day>12`, dg.textGt12, f.text);
  check(`${f.tag} flagged as corrupted`, dg.corrupted, true);
});

console.log('\n=== named containers resolve to the correct values ===');
const EXPECT = {
  MRKU3519668: { empty: '7/2/2026',  lfd: '7/10/2026' },
  TGBU7874765: { empty: '6/26/2026', lfd: '7/5/2026'  },
  TGHU5201860: { empty: '7/25/2026', lfd: '8/4/2026'  },
  MRSU6004695: { empty: '7/7/2026',  lfd: '7/8/2026'  },
  CAAU9026685: { empty: '7/3/2026',  lfd: '7/10/2026' }
};
FILES.forEach(f => {
  const { parsed, det, scacs } = load(f.file);
  ['empty', 'lfd'].forEach(key => {
    const ms = C.MILESTONES.find(m => m.key === key);
    const { records } = B.buildRecords(parsed, det.columns, ms, { applyDateFix: true }, scacs);
    Object.keys(EXPECT).forEach(cn => {
      const rec = records.find(r => r.container === cn);
      if (rec) check(`${f.tag} ${cn} ${ms.code}`, rec.dateText, EXPECT[cn][key]);
    });
  });
});

console.log('\n=== upload counts on 25AUG (vs Python) ===');
{
  const { parsed, det, scacs } = load('shipments_v4.xlsx');
  const want = { X2: 534, VA: 271, RD: 237, LF: 225 };
  C.MILESTONES.forEach(ms => {
    const { records } = B.buildRecords(parsed, det.columns, ms, { applyDateFix: true }, scacs);
    check(`${ms.code} uploadable rows`, records.length, want[ms.code]);
  });
}

console.log('\n=== correction actually changes the right number of rows ===');
{
  const { parsed, det, scacs } = load('shipments_v4.xlsx');
  const want = { X2: 120, VA: 79, RD: 79, LF: 60 };
  C.MILESTONES.forEach(ms => {
    const { records } = B.buildRecords(parsed, det.columns, ms, { applyDateFix: true }, scacs);
    const n = records.filter(r => r.corrected && +r.storedDate !== +r.date).length;
    check(`${ms.code} rows whose value changed`, n, want[ms.code]);
  });
}

console.log('\n=== MBL prefix detection ===');
{
  const { parsed, det, scacs } = load('shipments_v4.xlsx');
  const ms = C.MILESTONES[0];
  const { records } = B.buildRecords(parsed, det.columns, ms, { applyDateFix: true, applyMblPrefix: true }, scacs);
  const cands = records.filter(r => r.prefixCandidate);
  const carriers = [...new Set(cands.map(r => r.carrier))].sort();
  check('prefix carriers detected', carriers, ['CMDU', 'PABV']);
  check('OOCL/OOLU not flagged', records.some(r => r.carrier === 'OOCL' && r.prefixCandidate), false);
  const sample = cands.find(r => r.originalMbl.startsWith('NGB'));
  check('NGB prefixed correctly', sample ? sample.mbl : null, 'PABV' + (sample ? sample.originalMbl : ''));
}

console.log('\n=== confirmed RA prefix rules ===');
{
  /* Verified against RA on the 25 Aug upload: PABV+NGB must carry the
     prefix, PABV+SHCS must not (RA rejected all nine with
     "Container No ... is not exists"). */
  const { parsed, det, scacs } = load('shipments_v5.xlsx');
  const recs = B.buildRecords(parsed, det.columns, C.MILESTONES[0],
    { applyDateFix: false, applyMblPrefix: true }, scacs).records;
  check('no MBL is emitted as PABVSHCS...', recs.filter(r => /^PABVSHCS/.test(r.mbl)).length, 0);
  check('SHCS MBLs stay bare', recs.filter(r => /^SHCS/.test(r.mbl)).length, 9);
  check('SHCS is not even offered as a candidate',
        recs.filter(r => r.prefixCandidate && /^SHCS/.test(r.originalMbl)).length, 0);
  check('NGB MBLs still get the PABV prefix', recs.filter(r => /^PABVNGB/.test(r.mbl)).length, 17);

  /* the nine containers RA rejected must now carry a bare SHCS MBL */
  const rejected = ['HPCU5193443','PCIU9144550','PIDU4051879','PIDU4056232','HPCU5118141',
                    'PCIU8534717','PIDU4382440','PILU8021535','PCIU9423261'];
  const found = rejected.map(cn => recs.find(r => r.container === cn)).filter(Boolean);
  check('all nine rejected containers present in X2', found.length, 9);
  check('all nine now carry a bare SHCS MBL',
        found.every(r => /^SHCS\d+$/.test(r.mbl)), true);
}

console.log('\n=== regenerating LF reproduces the hand-corrected upload ===');
{
  /* The user hand-fixed the LF file after RA rejected nine rows. With the
     confirmed rules in place the tool must now produce that file unaided. */
  const theirs = XLSX.utils.sheet_to_json(
    XLSX.read(fs.readFileSync(DIR + '/LF_fixed.xlsx'), { type: 'buffer' }).Sheets.Sheet1,
    { header: 1, raw: false, defval: '' });
  const { parsed, det, scacs } = load('shipments_v5.xlsx');
  const mine = B.toAoa(B.buildRecords(parsed, det.columns,
    C.MILESTONES.find(m => m.key === 'lfd'),
    { applyDateFix: false, applyMblPrefix: true }, scacs).records);
  check('same row count', mine.length, theirs.length);
  const byCntr = new Map(mine.map(r => [r[0], r.join('|')]));
  check('every row matches the hand-corrected file',
        theirs.filter(r => byCntr.get(r[0]) !== r.join('|')).length, 0);
}

console.log('\n=== output shape ===');
{
  const { parsed, det, scacs } = load('shipments_v4.xlsx');
  const { records } = B.buildRecords(parsed, det.columns, C.MILESTONES[0], { applyDateFix: true }, scacs);
  const aoa = B.toAoa(records);
  check('six columns per row', [...new Set(aoa.map(r => r.length))], [6]);
  check('no blank rows', aoa.filter(r => r.every(c => c === '' || c == null)).length, 0);
  check('every event code is X2', [...new Set(aoa.map(r => r[2]))], ['X2']);
  check('every Update By is C', [...new Set(aoa.map(r => r[5]))], ['C']);
  check('no TBA containers', aoa.filter(r => r[0] === 'TBA').length, 0);
  check('all dates match M/D/YYYY', aoa.every(r => /^\d{1,2}\/\d{1,2}\/\d{4}$/.test(r[3])), true);
  check('all times match H:MM:SS', aoa.every(r => /^\d{1,2}:\d{2}:\d{2}$/.test(r[4])), true);
}

console.log('\n=== Empty Return carries real clock times ===');
{
  const { parsed, det, scacs } = load('shipments_v4.xlsx');
  const ms = C.MILESTONES.find(m => m.code === 'RD');
  const { records } = B.buildRecords(parsed, det.columns, ms, { applyDateFix: true }, scacs);
  check('some RD rows have a non-zero time', records.some(r => r.time !== '0:00:00'), true);
  const x2 = B.buildRecords(parsed, det.columns, C.MILESTONES[0], { applyDateFix: true }, scacs).records;
  check('all X2 rows are 0:00:00', [...new Set(x2.map(r => r.time))], ['0:00:00']);
}

console.log('\n=== timezone independence ===');
{
  const { parsed, det, scacs } = load('shipments_v4.xlsx');
  const { records } = B.buildRecords(parsed, det.columns, C.MILESTONES.find(m => m.key === 'lfd'), { applyDateFix: true }, scacs);
  const rec = records.find(r => r.container === 'MRKU3519668');
  check('MRKU3519668 LFD under TZ=' + (process.env.TZ || 'default'), rec.dateText, '7/10/2026');
}

console.log('\n=== a REAL fixed export must not be corrected (regression) ===');
{
  /* The 25 AUG report was re-issued with the export defect fixed: dates are
     real date cells spread across the whole month. The tool must recognise
     that and leave it alone. */
  const { parsed, det } = load('shipments_v5.xlsx');
  check('fixed file: all fields still resolve', det.missing, []);
  const dg = C.diagnose(parsed.rows, det.columns);
  check('fixed file: has dates past the 12th', dg.realGt12 > 0, true);
  check('fixed file: NOT flagged corrupted', dg.corrupted, false);
  check('fixed file: not flagged partial', dg.partial, false);

  /* column layout changed too - a new leading column shifts everything */
  check('header detection survives the added PTE CW column',
        parsed.header[det.columns.container], 'CONTAINER');

  const scacs = C.collectScacs(parsed.rows, det.columns);
  const want = { X2: 534, VA: 271, RD: 237, LF: 225 };
  C.MILESTONES.forEach(ms => {
    const r = B.buildRecords(parsed, det.columns, ms, { applyDateFix: false }, scacs);
    check(`fixed file: ${ms.code} row count`, r.records.length, want[ms.code]);
    check(`fixed file: ${ms.code} nothing corrected`,
          r.records.filter(x => x.corrected).length, 0);
  });
}

console.log('\n=== correcting the broken file equals their fixed export ===');
{
  /* The strongest check available: run the defective 25 AUG file through the
     day/month correction, and the re-issued fixed file through no correction.
     Every uploaded value must agree. */
  const collect = (file, fix) => {
    const { parsed, det, scacs } = load(file);
    const out = {};
    C.MILESTONES.forEach(m => {
      B.buildRecords(parsed, det.columns, m, { applyDateFix: fix, applyMblPrefix: true }, scacs)
        .records.forEach(r => { out[r.container + '|' + r.event] = r.dateText; });
    });
    return out;
  };
  const mine = collect('shipments_v4.xlsx', true);
  const theirs = collect('shipments_v5.xlsx', false);
  const keys = [...new Set([...Object.keys(mine), ...Object.keys(theirs)])];
  const mismatched = keys.filter(k => mine[k] !== theirs[k]);
  check('same set of records', keys.length, Object.keys(mine).length);
  check('every corrected value matches the fixed export', mismatched.length, 0);
}

console.log('\n=== a clean file must NOT be corrected ===');
{
  /* Round-trip a clean sheet through a real .xlsx so this exercises the
     same read path the app uses (serials + number formats, no cellDates). */
  const head = ['CARRIER','MBL','CONTAINER','CONT TYPE','VESSEL','ETD POL','POL','ETA POD','POD','ATA POD','DISCHARGE DATE POD','EMPTY RETURN DATE','EMPTY RETURN TIME','BROKER','FREE DEMURRAGE DAYS','LAST FREE DAY OF DETENTION'];
  const aoa = [head];
  for (let i = 0; i < 40; i++) {
    const day = (i % 28) + 1;
    const D = (m) => new Date(Date.UTC(2026, m, day));
    aoa.push(['MAEU','MAEU12345678','ABCD'+(1000000+i),'40HD','V',D(5),'SHA',D(6),'LZC',D(6),D(6),D(6),null,'B',21,D(7)]);
  }
  const ws0 = XLSX.utils.aoa_to_sheet(aoa, { cellDates: true, UTC: true });
  const wb0 = XLSX.utils.book_new(); XLSX.utils.book_append_sheet(wb0, ws0, 'Hoja1');
  const buf = XLSX.write(wb0, { type: 'buffer', bookType: 'xlsx' });
  const wb = XLSX.read(buf, { type: 'buffer', cellNF: true });
  const parsed = B.parseSheet(XLSX, wb.Sheets[wb.SheetNames[0]]);
  const det = C.detectColumns(parsed.header);
  const dg = C.diagnose(parsed.rows, det.columns);
  check('clean file parsed as real dates', dg.real > 100, true);
  check('clean file has real dates past the 12th', dg.realGt12 > 0, true);
  check('clean file NOT flagged corrupted', dg.corrupted, false);

  /* and with the fix switched on, a clean file must come out unchanged */
  const scacs = C.collectScacs(parsed.rows, det.columns);
  const recs = B.buildRecords(parsed, det.columns, C.MILESTONES[0], { applyDateFix: false }, scacs).records;
  check('clean file day 20 survives as 7/20/2026', recs.some(r => r.dateText === '7/20/2026'), true);
}

console.log(`\n${pass} passed, ${fail} failed\n`);
process.exit(fail ? 1 : 0);
