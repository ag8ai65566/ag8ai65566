/* ------------------------------------------------------------------
   RA Batch Upload - UI layer
   ------------------------------------------------------------------ */
(function () {
  'use strict';
  var C = window.RACore, B = window.RABuild;
  var $ = function (id) { return document.getElementById(id); };

  var state = {
    fileName: '', parsed: null, columns: null, scacs: {}, diag: null,
    selected: { X2: true, VA: true, RD: true, LF: true },
    opts: { applyDateFix: true, applyMblPrefix: true, prefixOverrides: {}, split: 'per' },
    built: {}, activeTab: null
  };

  /* ---------- file intake ----------------------------------------- */

  var drop = $('drop'), fileInput = $('file');
  drop.addEventListener('click', function () { fileInput.click(); });
  fileInput.addEventListener('change', function (e) {
    if (e.target.files[0]) handleFile(e.target.files[0]);
  });
  ['dragenter', 'dragover'].forEach(function (ev) {
    drop.addEventListener(ev, function (e) { e.preventDefault(); drop.classList.add('over'); });
  });
  ['dragleave', 'drop'].forEach(function (ev) {
    drop.addEventListener(ev, function (e) { e.preventDefault(); drop.classList.remove('over'); });
  });
  drop.addEventListener('drop', function (e) {
    if (e.dataTransfer.files[0]) handleFile(e.dataTransfer.files[0]);
  });

  function showError(msg) {
    var el = $('fileerr');
    el.hidden = false;
    el.innerHTML = '<div class="err">' + msg + '</div>';
    ['p-diag', 'p-ms', 'p-opt', 'p-prev', 'p-out'].forEach(function (i) { $(i).hidden = true; });
  }

  function handleFile(file) {
    state.fileName = file.name;
    $('fileerr').hidden = true;
    var reader = new FileReader();
    reader.onload = function (e) {
      try { loadWorkbook(new Uint8Array(e.target.result), file); }
      catch (err) { showError('讀取失敗:' + (err && err.message ? err.message : err)); }
    };
    reader.onerror = function () { showError('無法讀取這個檔案。'); };
    reader.readAsArrayBuffer(file);
  }

  function loadWorkbook(data, file) {
    /* read raw serials + number formats; never cellDates, so nothing
       depends on this machine's timezone */
    var wb = XLSX.read(data, { type: 'array', cellNF: true });
    if (!wb.SheetNames.length) return showError('這個檔案沒有工作表。');
    var ws = wb.Sheets[wb.SheetNames[0]];
    if (!ws || !ws['!ref']) return showError('第一個工作表是空的。');

    var parsed = B.parseSheet(XLSX, ws);
    var det = C.detectColumns(parsed.header);

    var required = ['mbl', 'container'];
    var lostRequired = required.filter(function (f) { return det.columns[f] == null; });
    if (lostRequired.length) {
      return showError('找不到必要欄位:<b>' + lostRequired.join(', ') + '</b>。' +
        '<br>讀到的標題列是:' + parsed.header.filter(Boolean).join(' · '));
    }
    var lostDates = C.MILESTONES.filter(function (m) { return det.columns[m.key] == null; });
    if (lostDates.length === C.MILESTONES.length) {
      return showError('找不到任何 milestone 日期欄位。<br>讀到的標題列是:' +
        parsed.header.filter(Boolean).join(' · '));
    }

    state.parsed = parsed;
    state.columns = det.columns;
    state.missing = det.missing;
    state.scacs = C.collectScacs(parsed.rows, det.columns);
    state.diag = C.diagnose(parsed.rows, det.columns);
    state.opts.applyDateFix = state.diag.corrupted;
    state.opts.prefixOverrides = {};

    $('filemeta').hidden = false;
    $('filemeta').innerHTML = '已載入 <b>' + esc(file.name) + '</b> — 工作表 <b>' +
      esc(wb.SheetNames[0]) + '</b>,' + parsed.rows.length + ' 筆資料列' +
      (lostDates.length ? '<br>沒有找到這些欄位,對應的 milestone 會停用:<b>' +
        lostDates.map(function (m) { return m.source; }).join(', ') + '</b>' : '');

    renderDiagnostic();
    renderCards();
    renderOptions();
    rebuild();
  }

  /* ---------- step 2: diagnostic ---------------------------------- */

  function renderDiagnostic() {
    var d = state.diag, el = $('diag');
    $('p-diag').hidden = false;
    var total = d.real + d.text;
    var naturalPct = 39.5;
    var box = function (n, l) { return '<div class="ev"><div class="n">' + n + '</div><div class="l">' + l + '</div></div>'; };
    var evidence = '<div class="evidence">' +
      box(d.real, '個儲存格存成「真日期」') +
      box(d.realGt12, '其中日期在 13 號之後') +
      box(d.text, '個儲存格存成文字') +
      box(total ? (100 * d.real / total).toFixed(1) + '%' : '—', '真日期佔比<br>(自然值約 ' + naturalPct + '%)') +
      '</div>';

    if (d.corrupted) {
      el.innerHTML = '<div class="verdict bad">' +
        '<h3>偵測到日/月對調</h3>' +
        '<p>這份檔案有 <b>' + d.real + '</b> 個日期存成真日期格式,而其中<b>沒有任何一個</b>落在 13 號之後。' +
        '正常情況下應該要有六成左右。同時 <b>' + d.text + '</b> 個文字日期<b>全部</b>都在 13 號之後。</p>' +
        '<p>這種零例外的切割只有一個成因:檔案被 dd/mm/yyyy 語系的 Excel 讀過。' +
        '<code>7/8/2026</code> 被讀成 8 月 7 日,而 <code>6/15/2026</code> 因為沒有 15 月而解析失敗、留成文字。</p>' +
        '<p><b>下面的「修正日期」已自動開啟。</b>每一筆被修正的值都會在預覽中標示出來。</p>' +
        evidence + '</div>';
    } else if (d.partial) {
      el.innerHTML = '<div class="verdict warn">' +
        '<h3>部分可疑</h3>' +
        '<p>大部分真日期落在 12 號之前(' + d.real + ' 個中有 ' + (d.real - d.realGt12) +
        ' 個),但有 <b>' + d.realGt12 + '</b> 個超過 13 號,所以不是整批被對調。</p>' +
        '<p><b>自動修正預設關閉</b>,因為無法判斷哪些該改。建議人工確認後再決定。</p>' +
        evidence + '</div>';
    } else {
      el.innerHTML = '<div class="verdict good">' +
        '<h3>日期看起來正常</h3>' +
        '<p>' + d.real + ' 個真日期裡有 <b>' + d.realGt12 + '</b> 個落在 13 號之後,' +
        '沒有出現日/月對調的特徵。<b>自動修正預設關閉。</b></p>' +
        evidence + '</div>';
    }
  }

  /* ---------- step 3: milestone cards ----------------------------- */

  function renderCards() {
    $('p-ms').hidden = false;
    var host = $('cards');
    host.innerHTML = '';
    C.MILESTONES.forEach(function (m) {
      var available = state.columns[m.key] != null;
      var res = available ? B.buildRecords(state.parsed, state.columns, m, state.opts, state.scacs) : { records: [] };
      var n = res.records.length;
      var fixed = res.records.filter(function (r) { return r.corrected && +r.storedDate !== +r.date; }).length;
      if (!available || !n) state.selected[m.code] = false;

      var card = document.createElement('div');
      card.className = 'card' + (state.selected[m.code] ? ' on' : '') + ((!available || !n) ? ' empty' : '');
      card.innerHTML =
        '<div class="top"><input type="checkbox"' + (state.selected[m.code] ? ' checked' : '') +
        ((!available || !n) ? ' disabled' : '') + '><span class="code">' + m.code + '</span>' +
        '<span class="name">' + m.label + '</span></div>' +
        '<div class="n">' + n + '</div>' +
        '<div class="l">' + (available ? '筆可上傳 · 來源 ' + m.source : '來源欄位不存在') + '</div>' +
        (fixed ? '<div class="fixnote">其中 ' + fixed + ' 筆日期已修正</div>' : '');
      if (available && n) {
        card.addEventListener('click', function () {
          state.selected[m.code] = !state.selected[m.code];
          renderCards(); rebuild();
        });
      }
      host.appendChild(card);
    });
  }

  /* ---------- step 4: options ------------------------------------- */

  function renderOptions() {
    $('p-opt').hidden = false;
    var host = $('opts');
    host.innerHTML = '';

    host.appendChild(toggle('applyDateFix', '修正日/月對調',
      state.diag.corrupted
        ? '把被誤判的日期還原成正確值。偵測到問題,已自動開啟。'
        : '這份檔案沒有偵測到對調特徵,除非你確定,否則不要開啟。'));

    /* MBL prefix - only offer it when there is something to prefix */
    var cands = collectPrefixCandidates();
    if (cands.length) {
      var byCarrier = {};
      cands.forEach(function (c) {
        if (!byCarrier[c.carrier]) byCarrier[c.carrier] = { mbls: 0, rows: 0 };
        byCarrier[c.carrier].mbls++; byCarrier[c.carrier].rows += c.count;
      });
      var totalRows = cands.reduce(function (s, c) { return s + c.count; }, 0);
      var summary = Object.keys(byCarrier).map(function (k) {
        return k + ' ' + byCarrier[k].mbls + ' 個 MBL / ' + byCarrier[k].rows + ' 個櫃';
      }).join('、');
      var el = toggle('applyMblPrefix',
        'MBL 補上船公司前綴(' + cands.length + ' 個 MBL,影響 ' + totalRows + ' 個櫃)',
        'RA 有些 MBL 會前綴船公司代碼,例如 NGB600492000 在 RA 是 PABVNGB600492000。' +
        '偵測到 ' + summary + ',這些 MBL 開頭不是任何已知的船公司代碼。');
      var det = document.createElement('details');
      det.innerHTML = '<summary>看這 ' + cands.length + ' 個 MBL</summary><div class="body">' +
        cands.slice(0, 60).map(function (c) {
          return '<code>' + esc(c.mbl) + '</code> → <code>' + esc(c.carrier + c.mbl) + '</code> · ' + c.count + ' 個櫃';
        }).join('<br>') + (cands.length > 60 ? '<br>… 還有 ' + (cands.length - 60) + ' 個' : '') + '</div>';
      el.appendChild(det);
      host.appendChild(el);
    }

    /* output split */
    var split = document.createElement('div');
    split.className = 'opt';
    split.innerHTML = '<div style="width:15px"></div><div><div class="t">輸出方式</div>' +
      '<div class="d">每個 milestone 分開一個檔比較好對照 RA 的錯誤訊息;合併成一個檔則可以一次上傳完。</div></div>';
    var seg = document.createElement('div');
    seg.className = 'seg';
    [['per', '每個 milestone 一個檔'], ['one', '全部合併成一個檔'], ['both', '兩種都要']].forEach(function (o) {
      var b = document.createElement('button');
      b.textContent = o[1];
      b.className = state.opts.split === o[0] ? 'on' : '';
      b.addEventListener('click', function () { state.opts.split = o[0]; renderOptions(); renderExports(); });
      seg.appendChild(b);
    });
    split.querySelector('div:last-child').appendChild(seg);
    host.appendChild(split);
  }

  function toggle(key, title, desc) {
    var el = document.createElement('div');
    el.className = 'opt';
    var cb = document.createElement('input');
    cb.type = 'checkbox'; cb.checked = !!state.opts[key];
    cb.addEventListener('change', function () {
      state.opts[key] = cb.checked;
      renderCards(); rebuild();
    });
    var txt = document.createElement('div');
    txt.innerHTML = '<div class="t">' + title + '</div><div class="d">' + desc + '</div>';
    el.appendChild(cb); el.appendChild(txt);
    return el;
  }

  function collectPrefixCandidates() {
    var map = {};
    state.parsed.rows.forEach(function (row) {
      var carrier = B.cellText(row.cells[state.columns.carrier]).toUpperCase();
      var mbl = B.cellText(row.cells[state.columns.mbl]);
      if (!carrier || !mbl) return;
      if (!C.needsPrefix(carrier, mbl.toUpperCase(), state.scacs)) return;
      var k = carrier + '|' + mbl;
      if (!map[k]) map[k] = { carrier: carrier, mbl: mbl, count: 0 };
      map[k].count++;
    });
    return Object.keys(map).map(function (k) { return map[k]; });
  }

  /* ---------- build + preview ------------------------------------- */

  function rebuild() {
    state.built = {};
    C.MILESTONES.forEach(function (m) {
      if (!state.selected[m.code] || state.columns[m.key] == null) return;
      state.built[m.code] = B.buildRecords(state.parsed, state.columns, m, state.opts, state.scacs);
    });
    var codes = Object.keys(state.built);
    if (state.activeTab && codes.indexOf(state.activeTab) < 0) state.activeTab = null;
    if (!state.activeTab) state.activeTab = codes[0] || null;
    renderPreview();
    renderExports();
  }

  function renderPreview() {
    var codes = Object.keys(state.built);
    $('p-prev').hidden = !codes.length;
    if (!codes.length) return;

    var tabs = $('tabs'); tabs.innerHTML = '';
    codes.forEach(function (code) {
      var m = ms(code), b = document.createElement('button');
      b.className = 'tab' + (state.activeTab === code ? ' on' : '');
      b.textContent = code + ' ' + m.label + ' (' + state.built[code].records.length + ')';
      b.addEventListener('click', function () { state.activeTab = code; renderPreview(); });
      tabs.appendChild(b);
    });

    var res = state.built[state.activeTab], recs = res.records;
    var LIMIT = 300;
    $('tbl').querySelector('thead').innerHTML =
      '<tr><th>來源列</th><th>Container #</th><th>MBL</th><th>Event</th><th>Date</th><th>Time</th><th>Update By</th><th>備註</th></tr>';
    var body = recs.slice(0, LIMIT).map(function (r) {
      var dateCell = r.corrected && +r.storedDate !== +r.date
        ? '<span class="was">' + C.fmtDate(r.storedDate) + '</span><span class="chg">' + r.dateText + '</span>'
        : r.dateText;
      var mblCell = r.prefixed
        ? '<span class="pfx">' + esc(r.mbl) + '</span>'
        : esc(r.mbl);
      return '<tr class="' + (r.warnings.length ? 'flagged' : '') + '">' +
        '<td class="mono">' + r.excelRow + '</td>' +
        '<td class="mono">' + esc(r.container) + '</td>' +
        '<td class="mono">' + mblCell + '</td>' +
        '<td class="mono">' + r.event + '</td>' +
        '<td class="mono">' + dateCell + '</td>' +
        '<td class="mono">' + r.time + '</td>' +
        '<td class="mono">' + r.updateBy + '</td>' +
        '<td class="flag">' + esc(r.warnings.join('; ')) + '</td></tr>';
    }).join('');
    $('tbl').querySelector('tbody').innerHTML = body;

    var fixed = recs.filter(function (r) { return r.corrected && +r.storedDate !== +r.date; }).length;
    var flagged = recs.filter(function (r) { return r.warnings.length; }).length;
    var sk = res.skipped;
    $('prevnote').innerHTML =
      '共 <b>' + recs.length + '</b> 筆會寫入檔案' +
      (recs.length > LIMIT ? '(畫面只顯示前 ' + LIMIT + ' 筆)' : '') + '。' +
      (fixed ? ' 其中 <b>' + fixed + '</b> 筆日期已修正。' : '') +
      (flagged ? ' <b>' + flagged + '</b> 筆有疑慮,建議上傳前先看一下。' : '') +
      '<br>已略過:沒有櫃號 ' + sk.noContainer + ' 筆、沒有 MBL ' + sk.noMbl +
      ' 筆、這個 milestone 沒有日期 ' + sk.noDate + ' 筆。';
  }

  function ms(code) {
    return C.MILESTONES.filter(function (m) { return m.code === code; })[0];
  }

  /* ---------- export ---------------------------------------------- */

  function renderExports() {
    var codes = Object.keys(state.built);
    $('p-out').hidden = !codes.length;
    if (!codes.length) return;
    var host = $('exportbtns'); host.innerHTML = '';

    if (state.opts.split === 'per' || state.opts.split === 'both') {
      codes.forEach(function (code) {
        var n = state.built[code].records.length;
        host.appendChild(btn(code + ' ' + ms(code).label + ' (' + n + ')', false, function () {
          downloadOne(code);
        }));
      });
    }
    if (state.opts.split === 'one' || state.opts.split === 'both') {
      var total = codes.reduce(function (s, c) { return s + state.built[c].records.length; }, 0);
      host.appendChild(btn('合併檔 (' + total + ' 筆)', state.opts.split === 'one', function () {
        downloadCombined();
      }));
    }
    if ((state.opts.split === 'per' || state.opts.split === 'both') && codes.length > 1) {
      host.appendChild(btn('全部下載', true, function () {
        codes.forEach(function (code, i) { setTimeout(function () { downloadOne(code); }, i * 350); });
      }));
    }
  }

  function btn(label, primary, fn) {
    var b = document.createElement('button');
    b.className = 'go' + (primary ? '' : ' alt');
    b.textContent = label;
    b.addEventListener('click', fn);
    return b;
  }

  function baseName() {
    return state.fileName.replace(/\.(xlsx|xlsm|xls)$/i, '').replace(/[^\w\-]+/g, '_');
  }

  /* Writes the six columns with every cell as text, so nothing downstream
     can reinterpret a date under a different locale. */
  function sheetFromRecords(records) {
    var aoa = B.toAoa(records);
    var ws = {};
    var maxc = 5;
    aoa.forEach(function (row, r) {
      row.forEach(function (v, c) {
        ws[XLSX.utils.encode_cell({ r: r, c: c })] = { t: 's', v: String(v == null ? '' : v) };
      });
    });
    ws['!ref'] = XLSX.utils.encode_range({ s: { r: 0, c: 0 }, e: { r: Math.max(aoa.length - 1, 0), c: maxc } });
    ws['!cols'] = [{ wch: 15 }, { wch: 20 }, { wch: 8 }, { wch: 12 }, { wch: 10 }, { wch: 11 }];
    return ws;
  }

  function save(ws, name) {
    var wb = XLSX.utils.book_new();
    XLSX.utils.book_append_sheet(wb, ws, 'Sheet1');
    XLSX.writeFile(wb, name, { bookType: 'xlsx' });
  }

  function downloadOne(code) {
    var recs = state.built[code].records;
    if (!recs.length) return;
    save(sheetFromRecords(recs), baseName() + '_' + code + '.xlsx');
  }

  function downloadCombined() {
    var all = [];
    Object.keys(state.built).forEach(function (c) { all = all.concat(state.built[c].records); });
    if (!all.length) return;
    save(sheetFromRecords(all), baseName() + '_ALL.xlsx');
  }

  function esc(s) {
    return String(s == null ? '' : s).replace(/[&<>"']/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c];
    });
  }
})();
