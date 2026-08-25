/* ------------------------------------------------------------------
   RA Batch Upload - record builder
   Turns parsed source rows into the six-column RA upload format.
   ------------------------------------------------------------------ */
(function (root) {
  'use strict';
  var C = root.RACore;

  /* Parse a whole worksheet (SheetJS) into rows of normalised cells. */
  function parseSheet(XLSX, ws) {
    var rng = XLSX.utils.decode_range(ws['!ref']);
    var header = [];
    for (var c = rng.s.c; c <= rng.e.c; c++) {
      var hc = ws[XLSX.utils.encode_cell({ r: rng.s.r, c: c })];
      header.push(hc ? String(hc.v) : '');
    }
    var rows = [];
    for (var r = rng.s.r + 1; r <= rng.e.r; r++) {
      var cells = [], any = false;
      for (var cc = rng.s.c; cc <= rng.e.c; cc++) {
        var cell = C.readCell(ws[XLSX.utils.encode_cell({ r: r, c: cc })]);
        cells.push(cell);
        if (cell.kind !== 'empty') any = true;
      }
      if (any) rows.push({ excelRow: r + 1, cells: cells });
    }
    return { header: header, rows: rows };
  }

  function cellText(cell) {
    if (!cell) return '';
    if (cell.kind === 'empty') return '';
    if (cell.raw != null) return String(cell.raw).trim();
    if (cell.kind === 'number') return String(cell.value);
    if (cell.kind === 'serial-date' || cell.kind === 'text-date') return C.fmtDate(cell.date);
    return '';
  }

  /* Resolve one date cell into the value to upload.
       .date      - what will be written
       .corrected - true when day/month was swapped
       .suspect   - stored as a real date in a file diagnosed as corrupted
                    but not swappable (should not happen; surfaced if it does) */
  function resolveDate(cell, applyFix) {
    if (!cell || (cell.kind !== 'serial-date' && cell.kind !== 'text-date')) return null;
    if (cell.kind === 'text-date') return { date: cell.date, corrected: false, stored: cell.date };
    if (!applyFix) return { date: cell.date, corrected: false, stored: cell.date };
    var sw = C.swapDayMonth(cell.date);
    if (!sw) return { date: cell.date, corrected: false, stored: cell.date, suspect: true };
    return { date: sw, corrected: true, stored: cell.date };
  }

  /* Build the upload records for one milestone.
     opts: { applyDateFix, applyMblPrefix, prefixOverrides }  */
  function buildRecords(parsed, columns, milestone, opts, scacs) {
    opts = opts || {};
    var out = [], skipped = { noContainer: 0, noMbl: 0, noDate: 0 };
    var dateField = milestone.key;

    parsed.rows.forEach(function (row) {
      var container = cellText(row.cells[columns.container]);
      var mbl = cellText(row.cells[columns.mbl]);
      var carrier = cellText(row.cells[columns.carrier]).toUpperCase();

      var dc = columns[dateField] == null ? null : row.cells[columns[dateField]];
      var resolved = resolveDate(dc, opts.applyDateFix);

      if (!container) { if (resolved) skipped.noContainer++; return; }
      if (!mbl) { if (resolved) skipped.noMbl++; return; }
      if (!resolved) { skipped.noDate++; return; }

      /* time: only Empty Return carries a real clock time */
      var time = '0:00:00';
      if (milestone.code === 'RD' && columns.emptyTime != null) {
        var tc = row.cells[columns.emptyTime];
        if (tc && tc.kind === 'time') time = C.fmtTime(tc.fraction);
      }

      /* MBL prefix */
      var finalMbl = mbl, prefixed = false;
      var candidate = C.needsPrefix(carrier, mbl.toUpperCase(), scacs);
      if (candidate) {
        var key = carrier + '|' + mbl;
        var on = opts.prefixOverrides && Object.prototype.hasOwnProperty.call(opts.prefixOverrides, key)
          ? opts.prefixOverrides[key] : !!opts.applyMblPrefix;
        if (on) { finalMbl = carrier + mbl; prefixed = true; }
      }

      var rec = {
        excelRow: row.excelRow,
        container: container,
        mbl: finalMbl,
        originalMbl: mbl,
        carrier: carrier,
        event: milestone.code,
        date: resolved.date,
        dateText: C.fmtDate(resolved.date),
        time: time,
        updateBy: 'C',
        corrected: resolved.corrected,
        storedDate: resolved.stored,
        suspect: !!resolved.suspect,
        prefixCandidate: candidate,
        prefixed: prefixed,
        warnings: []
      };
      out.push(rec);
    });

    addWarnings(parsed, columns, milestone, out, opts);
    return { records: out, skipped: skipped };
  }

  /* Cross-field sanity checks. These do not block the export; they mark
     rows so the user can review or hold them back. */
  function addWarnings(parsed, columns, milestone, records, opts) {
    var byRow = {};
    parsed.rows.forEach(function (r) { byRow[r.excelRow] = r; });

    var seen = {};
    records.forEach(function (rec) {
      var row = byRow[rec.excelRow];
      var d = function (field) {
        if (columns[field] == null) return null;
        var res = resolveDate(row.cells[columns[field]], opts.applyDateFix);
        return res ? res.date : null;
      };
      var discharge = d('discharge'), eta = d('eta'), ata = d('ata');
      var freeCell = columns.freeDays == null ? null : row.cells[columns.freeDays];
      var freeDays = freeCell && freeCell.kind === 'number' ? freeCell.value : null;

      if (milestone.code === 'LF' && discharge && freeDays != null) {
        var delta = Math.round((rec.date - discharge) / 86400000);
        if (Math.abs(delta - freeDays) > 3) {
          rec.warnings.push('LFD is ' + delta + ' days after discharge but free time is ' + freeDays + ' days');
        }
      }
      if (milestone.code === 'RD' && discharge && rec.date < discharge) {
        rec.warnings.push('empty return is before the discharge date');
      }
      if (milestone.code === 'VA' && eta && rec.date < eta) {
        /* an early arrival is normal; only flag a large gap */
        if ((eta - rec.date) / 86400000 > 30) rec.warnings.push('ATA is more than 30 days before ETA');
      }
      if (milestone.code === 'X2' && ata && rec.date > ata) {
        rec.warnings.push('ETA is later than the recorded ATA');
      }
      if (rec.suspect) rec.warnings.push('stored as a date but day/month cannot be swapped - check manually');

      var key = rec.container + '|' + rec.event;
      if (seen[key]) rec.warnings.push('duplicate container for this event (also row ' + seen[key] + ')');
      else seen[key] = rec.excelRow;
    });
  }

  /* Six columns, exact sequence, no header row. */
  function toAoa(records) {
    return records.map(function (r) {
      return [r.container, r.mbl, r.event, r.dateText, r.time, r.updateBy];
    });
  }

  root.RABuild = {
    parseSheet: parseSheet, cellText: cellText, resolveDate: resolveDate,
    buildRecords: buildRecords, toAoa: toAoa
  };
})(typeof window !== 'undefined' ? window : globalThis);
