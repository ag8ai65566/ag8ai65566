# Canonical Architecture · Dashboard Consistency Audit

**calc v3.4.0** · 2026-08-10 · 對應第二輪裁決 §16–§20、§31、§34 與第三輪 sprint

---

## A. 唯一的資料路徑

```
FRED (OFFICIAL_AGGREGATOR)  ─┐
SEC EDGAR (OFFICIAL_PRIMARY) ─┼─→ data/raw/<date>/*.raw  (原始回應 + sha256)
Yahoo (UNOFFICIAL_FREE)      ─┘            │
                                           ▼
Cboe (OFFICIAL_PRIMARY)     ─┘
                     lib/temporal.mjs ──→ gauges.mjs  ← lib/capex.mjs
                     （唯一的日期邏輯）    CANONICAL ENGINE      ← lib/capex-reconcile.mjs
                                           │  calc v3.4.0
                                           ▼
                          data/gauges.json ＋ data/holdings.json
                                           │      ↑ holdings.mjs ← lib/fundamentals.mjs
                          ┌────────────────┴────────────────┐
                          ▼                                 ▼
              render-dashboard.mjs                      test/*.test.mjs
                （只做格式化）                          （一致性閘門，35 項）
                          ▼
             reports/us-market-dashboard.html
```

| 檔案 | 角色 | 可以做 | 絕對不可以做 |
| --- | --- | --- | --- |
| `.claude/skills/henren-tape/scripts/gauges.mjs` | **CANONICAL ENGINE** | 全部金融計算 | — |
| `lib/temporal.mjs` | 日期邏輯（唯一來源） | 對齊、YoY、百分位 | 取得資料 |
| `lib/capex.mjs` | SEC XBRL 正規化 | 累計差分、跨公司彙總 | 判斷燈號 |
| `.claude/skills/us-market-brief/scripts/market-snapshot.mjs` | 價格快照引擎 | 報酬率、回撤、已實現波動 | — |
| `.claude/skills/us-market-brief/scripts/render-dashboard.mjs` | **RENDERER** | 版面、顏色、標籤、文案 | **任何金融計算，含四捨五入** |
| `.claude/skills/us-market-brief/scripts/holdings.mjs` | 持股引擎 | Serenity 閘門、集中度、相關係數 | — |
| `lib/fundamentals.mjs` | SEC 財報正規化 | 累計差分、比率、合理性三級 | 判斷燈號 |
| `lib/capex-reconcile.mjs` | 差分對帳 | 與直接申報單季值逐筆比對 | — |
| `config/data-sources.json` | 來源註冊表 | 定義權威等級與 SLA | — |

**已 DEPRECATED：** `reports/us-market-2026-08-10.md` — 數字手寫，含兩個已證實的錯誤，
檔頭已加警告橫幅。保留作歷史紀錄，不得再引用。

---

## B. Dashboard Consistency Audit

`test/` 每次執行都會驗證下列對應關係。**35 個測試全數通過。**

| Dashboard 顯示 | Engine 欄位 | 計算函式 | 資料來源 |
| --- | --- | --- | --- |
| 開關一 2.993 兆 | `gauges[fuel].observed.value` | `fuel` + `percentileInWindow` | FRED `WRESBAL` |
| 四週變化 P21.8 | `.empirical.change_4w_percentile_5y` | `percentileInWindow` | 同上 |
| 開關二 0.8（實際 0.796） | `gauges[ignition].observed.display_value` / `.exact_value` | `alignByEffectiveDate` | **Cboe** VIX / VIX3M（一手） |
| 開關三 **不評估** | `gauges[capex].decision = NO_DECISION` | `aggregateCapex` + `reconcileAll` | SEC EDGAR XBRL ×4 |
| capex $129.75B | `.observed.detail.total_bn` | `toQuarters`（累計差分） | 同上 |
| SOFR−IORB 0 bp | `gauges[sofr].observed.value` | `alignByEffectiveDate` | FRED `SOFR`/`IORB` |
| TGA 907.3 | `gauges[tga].observed.value` | 直接讀值 | FRED `WTREGEN` |
| RRP 1.45 | `gauges[rrp].observed.value` | 直接讀值 | FRED `RRPONTSYD` |
| HY OAS 2.71% P9.6 | `gauges[hyoas].observed.value` | `percentileInWindow` | FRED `BAMLH0A0HYM2` |
| NFCI −0.529 | `gauges[nfci].observed.value` | 直接讀值 | FRED `NFCI` |
| M2 差 −36.2 | `gauges[m2gap].observed.value` | `alignByEffectiveDate`+`yoyAtAnchor` | FRED `M2SL` + Yahoo `^IXIC` |
| 巴菲特 218.1% P94.9 | `gauges[buffett].observed.value` | `alignQuarterly` | FRED `NCBEILQ027S`/`GDP` |
| AI 籃子 5.9 倍 | `gauges[ai-basket-rel-vol].observed.value` | 中位數（非最大值） | Yahoo ×8 |

自動化檢查（`integrity.test.mjs`）：

- `dashboard numbers match the engine exactly` — 逐格比對 HTML 是否包含 engine 的值
- `the renderer performs no financial calculation` — 正則掃描 renderer 找 `Math.log`/`Math.sqrt`/`*252`/`/1e9`/自訂 percentile
- `dashboard states the calculation version` — HTML 必須印出 calc 版本與 code commit
- `missing data never becomes a rule evaluation`
- `counts exclude undecided gauges`
- `no composite score is emitted`（比對 **key**，不是子字串）
- `a composite gauge inherits its weakest source authority`
- `no buy/sell language reaches the rendered output`（只抓斷言式句型）
- `signal validation is honest about being untested`

---

## C. Status Schema（審查 §34-C）

每一格帶五個維度：

```json
{
  "data_state": "CURRENT | LAGGED_BY_DESIGN | OVERDUE | STALE | MISSING | DATE_MISMATCH | SOURCE_FAILURE | NOT_WIRED",
  "source_authority": "OFFICIAL_PRIMARY | OFFICIAL_AGGREGATOR | LICENSED | UNOFFICIAL_FREE | MANUAL_SECONDARY | NO_AUTHORITATIVE_SOURCE",
  "measurement_integrity": "RAW | CHECKED",
  "signal_validation": "UNTESTED | RETROSPECTIVE_TESTED | OUT_OF_SAMPLE_TESTED | FORWARD_VALIDATED",
  "automation_mode": "AUTOMATED | HYBRID | MANUAL_REVIEW_REQUIRED | NOT_WIRED"
}
```

**2026-08-10 實際分布**

| 維度 | 分布 |
| --- | --- |
| data_state | LAGGED_BY_DESIGN 10、CURRENT 2、OVERDUE 2、STALE 1、RECONCILIATION_REQUIRED 1 |
| source_authority | OFFICIAL_AGGREGATOR 7、OFFICIAL_PRIMARY 2、UNOFFICIAL_FREE 2、MANUAL_SECONDARY 4、NO_AUTHORITATIVE_SOURCE 1 |
| measurement_integrity | CHECKED 12、RAW 4 |
| **signal_validation** | **UNTESTED 16** — 沒有任何一格經過統計驗證 |
| automation_mode | AUTOMATED 10、HYBRID 1、MANUAL_REVIEW_REQUIRED 5 |

`measurement_integrity=CHECKED` 與 `signal_validation=UNTESTED` 同時成立，正是審查 §5.2.D
要表達的狀態：**數字可能已經算對了，但這條規則有沒有預測力，沒有人證明過。**

---

## D. 這一輪修掉的東西

| 項目 | 修法 | 結果 |
| --- | --- | --- |
| 開關二 DATE_MISMATCH | Yahoo `^VIX3M` 自 2026-07-17 起收盤全 null；先改 FRED，再升級為 **Cboe 一手**（比 FRED 早一個 session） | 0.8（實際 0.796，P3），權威從 UNOFFICIAL_FREE 升到 OFFICIAL_PRIMARY |
| 巴菲特 DATE_MISMATCH | `alignQuarterly` 配對同一季，而不是各取最新 | 218.1%（P94.9），紅燈 |
| 季度序列年齡高估 | FRED 季度資料用「期間起始日」標記，年齡改由期間結束日算 | 巴菲特從誤判 STALE 回到 LAGGED_BY_DESIGN |
| 開關三 NOT_WIRED | 接上 SEC EDGAR XBRL，10-Q 累計數差分還原單季，四家彙總 | 資料接通，但差分對帳後改為 **NO_DECISION**（見下） |
| 開關三 差分未驗證 | `capex-reconcile.mjs` 逐筆對照直接申報單季值；發現 META 無可對照值 | 規則（QoQ）不評估；YoY 降為脈絡 |
| 合理性閘門拍門檻 | 三級化：STRUCTURAL / RECONCILIATION / OUTLIER；0.25 降為僅提醒 | SNDK 由「封鎖」變「提醒」 |
| `proven` 過強 | 改 `SUPPORTED` + `scope: CURRENT_PERIOD` + `coverage` | 一季的正數不再讀成長期紀錄 |
| 首頁紅綠計數 | 改為五層成熟度階梯 + 「經統計驗證訊號 0」 | 不再讀成市場評分 |
| 顯示精度 | `display_value` / `exact_value` 分離，稽核抽屜保留完整精度 | 2.99 vs 2.993；P95 vs P94.9 |
| 準備金速度門檻 | 自訂的 −3%/4週 實測落在 P21.8（不算快），改為底部十分位 | 開關一回綠燈 |
| 「Scored」用詞 | 改為 **Framework Triggers / 狠人規則已評估** | 不再暗示這是校準過的評分 |
| 紅黃綠語意 | 改為「規則觸發／接近／未觸發」，與 signal_validation 並列顯示 | 不再讀成「市場風險已證明升高」 |
| 手抄數字 | Dashboard 全部由 `data/gauges.json` 產生 | 一致性由測試強制 |

---

## E. 仍未做（依裁決屬 P1/P2）

| 項目 | 分級 | 阻礙 |
| --- | --- | --- |
| ALFRED vintage point-in-time | P1 | 回測的前提；FRED 只給最新修訂版 |
| Threshold backtest / 假警報率 | P1 | 依賴上一項，順序不可顛倒 |
| CapEx Layer B（融資租賃） | P1 | 需逐公司 filing notes 對照表 |
| CapEx Layer C（管理層指引） | P1 | 法說會內容無 XBRL tag，需 LLM 抽取＋人工複核 |
| Claim-level evidence | P1 | 裁決已降級 |
| Stooq 交叉檢查 / SOURCE_CONFLICT | P1 | 端點回 JS 瀏覽器驗證 |
| 融資餘額 / 0DTE / 前十大權重 / 內部人比 / 預估本益比 自動化 | P1 | 無免費權威來源；目前 MANUAL_REVIEW_REQUIRED |
| META capex 差分無法驗證 | **P0** | 該公司從不申報獨立單季值，現行對帳法結構上做不到 |
| `as_of_query` 從未執行 | P1 | `filed` 已存，但沒跑過一次 as-of 查詢 |
| 輸出 schema allowlist | P1 | 目前買賣護欄只有 regex，可被改寫繞過 |

---

## F. Research Tool Production Definition（裁決 §29）

```
[x] Canonical calculation engine exists              gauges.mjs, calc v3.4.0
[x] Dashboard uses only canonical outputs            測試強制
[x] Important numbers have provenance                8 欄位／格
[x] Date alignment bugs resolved                     兩個 DATE_MISMATCH 全修，含回歸測試
[x] Source authority clearly labeled                 registry + 逐格顯示
[x] Yahoo marked UNOFFICIAL_FREE                     且沿計算鏈傳遞（M2 gap 取最低）
[x] Missing data cannot silently pass                NO_DECISION，不進任何計數
[x] Proxy names match calculations                   AI 籃子相對波動；開關二標「代理」
[x] Henren rules separated from empirical context    四塊分離，永不合併
[x] Signal validation status visible                 全部 UNTESTED，明示
[x] NOT_WIRED signals clearly visible                capex Layer B/C 逐層列出
[x] Manual / hybrid data allowed and labeled         automation_mode
[x] No BUY / SELL / target price outputs             測試強制（斷言式句型）
[x] Calculation versions are traceable               calc version + code commit 印在頁面上
```

**14/14。** 依裁決 §37，系統現在可以被稱為 **Reliable Research & Risk Intelligence Tool**。

第三輪追加完成：capex 差分對帳（65 筆可驗證中 64 筆分毫不差）、規則與脈絡分軌、
合理性三級化、`proven → SUPPORTED`、首頁改為五層成熟度階梯、顯示精度與稽核精度分離、
帳本標記 LEGACY_EXPLORATORY、術語對照表。

**下一步不是 ALFRED，也不是加指標。** 依第三輪裁決 §18，中間還有一層
**Measurement Validity** 尚未完成——capex 有一家發行人結構上無法用現行方法驗證，
`as_of_query` 從未實際執行過。落實計畫見 `docs/roadmap-and-questions-v4.md`。
