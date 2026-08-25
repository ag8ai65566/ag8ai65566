/* ------------------------------------------------------------------
   RA Batch Upload - core logic
   Pure functions, no DOM. Shared by the browser app and the test suite.
   ------------------------------------------------------------------ */
(function (root) {
  'use strict';

  /* ---------- milestone definitions ------------------------------- */

  var MILESTONES = [
    { code: 'X2', key: 'eta',   label: 'Port ETA',     source: 'ETA POD' },
    { code: 'VA', key: 'ata',   label: 'Port ATA',     source: 'ATA POD' },
    { code: 'RD', key: 'empty', label: 'Empty Return', source: 'EMPTY RETURN DATE' },
    { code: 'LF', key: 'lfd',   label: 'Last Free Day', source: 'LAST FREE DAY OF DETENTION' }
  ];

  /* Header matching. Each field lists candidate header names, normalised.
     Matching is exact-first, then prefix, so 'LAST FREE DAY OF DETEN'
     (truncated in some exports) still resolves. */
  var FIELDS = {
    carrier:   ['CARRIER'],
    etd:       ['ETD POL', 'ETD'],
    mbl:       ['MBL', 'MBL#', 'MBL NO', 'MBL NUMBER'],
    container: ['CONTAINER', 'CONTAINER NO', 'CONTAINER #', 'CNTR'],
    eta:       ['ETA POD', 'ETA'],
    ata:       ['ATA POD', 'ATA'],
    discharge: ['DISCHARGE DATE POD', 'DISCHARGE DATE', 'DISCHARGE'],
    empty:     ['EMPTY RETURN DATE', 'EMPTY RETURN'],
    emptyTime: ['EMPTY RETURN TIME'],
    freeDays:  ['FREE DEMURRAGE DAYS', 'FREE DAYS'],
    lfd:       ['LAST FREE DAY OF DETENTION', 'LAST FREE DAY', 'LFD', 'LAST FREE DATE']
  };

  function norm(s) {
    return String(s == null ? '' : s).toUpperCase().replace(/[^A-Z0-9 ]/g, ' ')
      .replace(/\s+/g, ' ').trim();
  }

  function detectColumns(headerRow) {
    var found = {}, missing = [];
    var heads = headerRow.map(norm);
    Object.keys(FIELDS).forEach(function (field) {
      var cands = FIELDS[field].map(norm), idx = -1;
      for (var i = 0; i < heads.length && idx < 0; i++) {
        if (cands.indexOf(heads[i]) >= 0) idx = i;
      }
      if (idx < 0) {                       // fall back to prefix match
        for (var j = 0; j < heads.length && idx < 0; j++) {
          for (var k = 0; k < cands.length; k++) {
            if (heads[j] && cands[k].indexOf(heads[j]) === 0 && heads[j].length >= 6) { idx = j; break; }
            if (heads[j] && heads[j].indexOf(cands[k]) === 0 && cands[k].length >= 6) { idx = j; break; }
          }
        }
      }
      if (idx >= 0) found[field] = idx; else missing.push(field);
    });
    return { columns: found, missing: missing };
  }

  /* ---------- cell reading ---------------------------------------- */

  var EXCEL_EPOCH = Date.UTC(1899, 11, 30);   // serial 1 === 1900-01-01

  function serialToDate(serial) {
    return new Date(EXCEL_EPOCH + Math.floor(serial) * 86400000);
  }

  function isDateFormat(z) {
    if (!z) return false;
    var f = String(z).replace(/\[[^\]]*\]/g, '').replace(/"[^"]*"/g, '');
    return /[yd]/i.test(f);
  }

  function isTimeFormat(z) {
    if (!z) return false;
    var f = String(z).replace(/\[[^\]]*\]/g, '').replace(/"[^"]*"/g, '');
    return /[hs]/i.test(f) && !/[yd]/i.test(f);
  }

  var TEXT_DATE = /^\s*(\d{1,2})\/(\d{1,2})\/(\d{4})\s*$/;

  /* Reads one cell into a normalised shape.
       kind: 'empty' | 'text-date' | 'serial-date' | 'time' | 'number' | 'text'
     For dates, .date is a UTC Date built from the value exactly as stored. */
  function readCell(cell) {
    if (!cell || cell.v == null || cell.v === '') return { kind: 'empty' };
    if (cell.t === 'd' && cell.v instanceof Date) {
      var dv = cell.v;
      return { kind: 'serial-date',
               date: new Date(Date.UTC(dv.getFullYear(), dv.getMonth(), dv.getDate())) };
    }
    if (cell.t === 'n') {
      if (isDateFormat(cell.z) && cell.v >= 1) {
        return { kind: 'serial-date', date: serialToDate(cell.v), serial: cell.v };
      }
      if (isTimeFormat(cell.z) || (cell.v > 0 && cell.v < 1)) {
        return { kind: 'time', fraction: cell.v - Math.floor(cell.v) };
      }
      return { kind: 'number', value: cell.v };
    }
    var s = String(cell.v).trim();
    if (s === '' || s === 'N/A' || s === 'NA' || s === '-' || s === 'TBA') return { kind: 'empty', raw: s };
    var m = TEXT_DATE.exec(s);
    if (m) {
      var mo = +m[1], d = +m[2], y = +m[3];
      if (mo >= 1 && mo <= 12 && d >= 1 && d <= 31) {
        return { kind: 'text-date', date: new Date(Date.UTC(y, mo - 1, d)), raw: s };
      }
    }
    return { kind: 'text', raw: s };
  }

  /* ---------- day/month corruption diagnostic --------------------- */

  var DATE_FIELDS = ['etd', 'eta', 'ata', 'discharge', 'empty', 'lfd'];

  /* The signature: a dd/mm/yyyy parser converts 'a/b/yyyy' only when b<=12,
     so every converted cell lands on day 1-12 and every cell that stayed
     text has day>12. A clean file shows no such separation. */
  function diagnose(rows, columns) {
    var real = 0, realGt12 = 0, text = 0, textGt12 = 0;
    rows.forEach(function (row) {
      DATE_FIELDS.forEach(function (f) {
        if (columns[f] == null) return;
        var c = row.cells[columns[f]];
        if (!c) return;
        if (c.kind === 'serial-date') { real++; if (c.date.getUTCDate() > 12) realGt12++; }
        else if (c.kind === 'text-date') { text++; if (c.date.getUTCDate() > 12) textGt12++; }
      });
    });
    var total = real + text;
    var corrupted = real >= 20 && realGt12 === 0 && text > 0 && textGt12 === text;
    return {
      real: real, realGt12: realGt12, text: text, textGt12: textGt12,
      realShare: total ? real / total : 0,
      corrupted: corrupted,
      /* a file that is partly clean is still suspicious - surfaced separately */
      partial: !corrupted && real >= 20 && realGt12 > 0 && realGt12 / real < 0.15
    };
  }

  function swapDayMonth(d) {
    var day = d.getUTCDate();
    if (day > 12) return null;                     // not representable as a month
    return new Date(Date.UTC(d.getUTCFullYear(), day - 1, d.getUTCMonth() + 1));
  }

  /* ---------- MBL carrier prefix ---------------------------------- */

  /* RA stores some MBLs with the carrier SCAC prepended
     (NGB600492000 -> PABVNGB600492000). Only flag an MBL that starts with
     no SCAC seen anywhere in the CARRIER column, so OOCL/OOLU and other
     legitimate cross-carrier references are left alone.

     Whether RA wants the prefix is decided per MBL family, and the source
     report gives no reliable hint, so it can only be learned from what RA
     accepts. Confirmed against RA on the 25 Aug upload:
       PABV + NGB...   prefix required   - accepted
       PABV + SHCS...  prefix rejected   - "Container No ... is not exists"
     NO_PREFIX holds the families RA wants bare. */
  var NO_PREFIX = [
    { carrier: 'PABV', prefix: 'SHCS' }
  ];

  function isKnownBare(carrier, mbl) {
    for (var i = 0; i < NO_PREFIX.length; i++) {
      if (NO_PREFIX[i].carrier === carrier && mbl.indexOf(NO_PREFIX[i].prefix) === 0) return true;
    }
    return false;
  }

  function collectScacs(rows, columns) {
    var set = {};
    if (columns.carrier == null) return set;
    rows.forEach(function (row) {
      var c = row.cells[columns.carrier];
      var v = c && (c.raw != null ? c.raw : c.value);
      v = String(v == null ? '' : v).trim().toUpperCase();
      if (/^[A-Z]{4}$/.test(v)) set[v] = true;
    });
    return set;
  }

  function needsPrefix(carrier, mbl, scacs) {
    if (!carrier || !mbl) return false;
    if (mbl.indexOf(carrier) === 0) return false;
    if (isKnownBare(carrier, mbl)) return false;
    for (var s in scacs) if (mbl.indexOf(s) === 0) return false;
    return true;
  }

  /* ---------- formatting ------------------------------------------ */

  function fmtDate(d) {
    return (d.getUTCMonth() + 1) + '/' + d.getUTCDate() + '/' + d.getUTCFullYear();
  }

  function fmtTime(fraction) {
    if (fraction == null) return '0:00:00';
    var secs = Math.round(fraction * 86400);
    if (secs >= 86400) secs = 86399;
    var h = Math.floor(secs / 3600), m = Math.floor((secs % 3600) / 60), s = secs % 60;
    return h + ':' + String(m).padStart(2, '0') + ':' + String(s).padStart(2, '0');
  }

  function pad(n) { return String(n).padStart(2, '0'); }
  function isoDate(d) {
    return d.getUTCFullYear() + '-' + pad(d.getUTCMonth() + 1) + '-' + pad(d.getUTCDate());
  }

  root.RACore = {
    MILESTONES: MILESTONES, FIELDS: FIELDS,
    norm: norm, detectColumns: detectColumns,
    serialToDate: serialToDate, isDateFormat: isDateFormat, isTimeFormat: isTimeFormat,
    readCell: readCell, diagnose: diagnose, swapDayMonth: swapDayMonth,
    collectScacs: collectScacs, needsPrefix: needsPrefix,
    NO_PREFIX: NO_PREFIX, isKnownBare: isKnownBare,
    fmtDate: fmtDate, fmtTime: fmtTime, isoDate: isoDate,
    DATE_FIELDS: DATE_FIELDS
  };
})(typeof window !== 'undefined' ? window : globalThis);
