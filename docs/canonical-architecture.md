# Canonical Architecture · Dashboard Consistency Audit

**calc v4.0.0** · 2026-08-11 · 對應第二輪裁決 §16–§20、§31、§34、第三輪 sprint 與第四輪裁決

---

## A. 唯一的資料路徑

```
FRED (OFFICIAL_AGGREGATOR)  ─┐
SEC EDGAR (OFFICIAL_PRIMARY) ─┼─→ data/raw/<date>/*.raw  (原始回應 + sha256)
Yahoo (UNOFFICIAL_FREE)      ─┤            │
Cboe (OFFICIAL_PRIMARY)      ─┘            ▼
                     lib/temporal.mjs ──→ gauges.mjs  ← lib/capex.mjs
                     （唯一的日期邏輯）    CANONICAL ENGINE   ← lib/capex-reconcile.mjs
                                           │  calc v4.0.0    ← lib/capex-freshness.mjs
                                           │                 ← lib/snapshot-diff.mjs
                                           ▼
                          lib/output-contract.mjs  ← 契約檢查（違約即 exit 1）
                                           │
                          data/gauges.json ＋ data/holdings.json ＋ data/snapshots/<date>.json
                                           │      ↑ holdings.mjs ← lib/fundamentals.mjs
                          ┌────────────────┴────────────────┐
                          ▼                                 ▼
              render-dashboard.mjs                      test/*.test.mjs
                （只做格式化）                     （四類閘門，59 項）→ scripts/test-report.mjs
                          ▼                                 │
             reports/us-market-dashboard.html ←─────────────┘
                                                      data/test-report.json
```

整條路徑只有一個入口：**`npm run build`**。

Dashboard 曾經落後引擎三個版本，因為「重新產生」是一串要記得的指令，不是一個目標。
build 內部的順序不是隨便排的：測試比對的是**已經算繪出來的頁面**，所以必須跑在 render 之後，
而它產生的測試報告又要回到頁面上，因此 render 跑兩次；最後的 `npm test` 才是真正的閘門，
它驗的是即將被 commit 的那一份檔案。

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
| `lib/capex-freshness.mjs` | 三層新鮮度＋敏感度 | 期望／可得／已取得比對、決策穩健度、證據覆蓋 | 稱覆蓋率為信心水準 |
| `lib/snapshot-diff.mjs` | 兩次執行之間的差異 | 規則翻轉、狀態變化、絕對變動 | 判斷市場意義 |
| `lib/output-contract.mjs` | **輸出契約** | 拒絕未宣告鍵、禁用鍵、建議式文句 | 掃描靜態文案 |
| `scripts/test-report.mjs` | 測試分類報告 | 依「回答哪個問題」分組 | 改寫測試結果 |
| `config/data-sources.json` | 來源註冊表 | 定義權威等級與 SLA | — |

**已 DEPRECATED：** `reports/us-market-2026-08-10.md` — 數字手寫，含兩個已證實的錯誤，
檔頭已加警告橫幅。保留作歷史紀錄，不得再引用。

---

## B. Dashboard Consistency Audit

`test/` 每次執行都會驗證下列對應關係。**59 個測試全數通過**——但通過的是四類問題中的四類，
第五類（訊號驗證）**一個測試都沒有**，而那才是決定這套系統有沒有預測力的那一類。

| 類別 | 數量 | 回答的問題 |
| --- | --- | --- |
| `[temporal]` | 15 | 兩條序列是不是在同一個時間點上被比較？ |
| `[integrity]` | 27 | 畫面上的數字，是不是引擎算出來的那一個？ |
| `[contract]` | 7 | 這份輸出有沒有可能夾帶買賣建議、目標價或綜合評分？ |
| `[measurement]` | 10 | 這個標籤底下，量到的到底是哪一個財務概念？ |
| **`[validation]`** | **0** | **這些門檻在歷史上真的能分辨後續報酬嗎？（沒有測試存在）** |

| Dashboard 顯示 | Engine 欄位 | 計算函式 | 資料來源 |
| --- | --- | --- | --- |
| 開關一 2.993 兆 | `gauges[fuel].observed.value` | `fuel` + `percentileInWindow` | FRED `WRESBAL` |
| 四週變化 P21.8 | `.empirical.change_4w_percentile_5y` | `percentileInWindow` | 同上 |
| 開關二 0.82（實際 0.815） | `gauges[ignition].observed.display_value` / `.exact_value` | `alignByEffectiveDate` | **Cboe** VIX / VIX3M（一手） |
| 開關三 **已評估、但讀數已被更新的一季超過** | `gauges[capex].decision = RULE_EVALUATED_ON_SUPERSEDED_PERIOD` | `aggregateCapex` + `reconcileAll` + `decisionRobustness` | SEC EDGAR XBRL ×4 |
| capex $129.75B | `.observed.detail.total_bn` | `toQuarters`（累計差分） | 同上 |
| SOFR−IORB −3 bp | `gauges[sofr].observed.value` | `alignByEffectiveDate` | FRED `SOFR`/`IORB` |
| TGA 907.3 | `gauges[tga].observed.value` | 直接讀值 | FRED `WTREGEN` |
| RRP 0.97 | `gauges[rrp].observed.value` | 直接讀值 | FRED `RRPONTSYD` |
| HY OAS 2.7% P9.2 | `gauges[hyoas].observed.value` | `percentileInWindow` | FRED `BAMLH0A0HYM2` |
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
- `every gauge the engine produced reaches the page` — 一格都不准在版面上消失
- `the page never claims a capability the engine says it lacks` — 狀態字串不得當成布林值渲染
- `unusable data never becomes a clean rule evaluation`
- `an unverified transformation blocks the rule unless sensitivity shows it cannot matter`
- `signal validation is honest about being untested`

買賣語言的檢查已從這裡移走。它現在跑在 `test/contract.test.mjs`，比對的是結構化資料而不是
HTML——舊做法把引擎輸出、靜態文案、免責聲明壓成同一條字串，然後靠字面猜哪一句是系統主張，
**連續三次抓到自己的免責聲明**。

---

## C. Status Schema（審查 §34-C）

每一格帶五個維度：

```json
{
  "data_state": "CURRENT | LAGGED_BY_DESIGN | INGESTION_OVERDUE | SOURCE_PUBLICATION_LAG | OVERDUE | STALE | MISSING | DATE_MISMATCH | SOURCE_FAILURE | NOT_WIRED",
  "source_authority": "OFFICIAL_PRIMARY | OFFICIAL_AGGREGATOR | LICENSED | UNOFFICIAL_FREE | MANUAL_SECONDARY | NO_AUTHORITATIVE_SOURCE",
  "measurement_integrity": "RAW | CHECKED",
  "signal_validation": "UNTESTED | RETROSPECTIVE_TESTED | OUT_OF_SAMPLE_TESTED | FORWARD_VALIDATED",
  "automation_mode": "AUTOMATED | HYBRID | MANUAL_REVIEW_REQUIRED | NOT_WIRED"
}
```

**2026-08-11 實際分布**

| 維度 | 分布 |
| --- | --- |
| data_state | LAGGED_BY_DESIGN 10、CURRENT 2、OVERDUE 2、STALE 1、**INGESTION_OVERDUE 1** |
| source_authority | OFFICIAL_AGGREGATOR 7、OFFICIAL_PRIMARY 2、UNOFFICIAL_FREE 2、MANUAL_SECONDARY 4、NO_AUTHORITATIVE_SOURCE 1 |
| measurement_integrity | CHECKED 12、RAW 4 |
| **signal_validation** | **UNTESTED 16** — 沒有任何一格經過統計驗證 |
| automation_mode | AUTOMATED 10、HYBRID 1、MANUAL_REVIEW_REQUIRED 5 |

`measurement_integrity=CHECKED` 與 `signal_validation=UNTESTED` 同時成立，正是審查 §5.2.D
要表達的狀態：**數字可能已經算對了，但這條規則有沒有預測力，沒有人證明過。**

`INGESTION_OVERDUE` 是本輪新增的狀態，它存在的理由很具體：capex 停在 2026-Q1 並被標為
「設計上落後」，但當時四家中已有三家申報了 2026-Q2。**「來源本來就慢」變成了「管線沒去拿」的
遮羞布。** 這兩件事現在是不同的狀態值，而且判斷不是靠形容詞——`latest_available_period`
大於 `latest_ingested_period` 時，它就不可能是來源落後。

決策狀態同樣多了一個 `RULE_EVALUATED_ON_SUPERSEDED_PERIOD`。舊版本讓 capex 同時是
`NO_DECISION` 和 `rule_state: green`——判定明明成立，只是成立在一個已經不是最新的季度上，
而兩個標籤都沒說出這件事。

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
| META issuer-direct 單季值 | P1 | 轉錄器已備好（`config/issuer-direct-capex.json`），但欄位維持 `PENDING_TRANSCRIPTION`——第三方引用的數字不能當一手資料寫進來 |
| Signal Behavior Diagnostics | P1 | 需要多日快照；歷史剛開始累積 |
| ECONOMIC_OUTLIER 的資料品質佇列 | P2 | SNDK 資產週轉率 0.161 目前只有提醒，沒有追蹤流程 |
| Claim-level evidence | P1 | 裁決已降級 |
| Stooq 交叉檢查 / SOURCE_CONFLICT | P1 | 端點回 JS 瀏覽器驗證 |
| 融資餘額 / 0DTE / 前十大權重 / 內部人比 / 預估本益比 自動化 | P1 | 無免費權威來源；目前 MANUAL_REVIEW_REQUIRED |
| 交易所假日行事曆 | P2 | `tradingSessionsBetween` 目前只扣週末，不扣國定假日 |

**本輪已從這張表移除的三項**（連同它們當初的理由，因為理由本身也曾經是錯的）：

| 項目 | 當初寫的阻礙 | 實際結果 |
| --- | --- | --- |
| META capex 差分無法驗證 | 標為 **P0**，理由是「該公司從不申報獨立單季值，現行對帳法結構上做不到」 | 這句話把**一條取得路徑**（10-Q XBRL）說成了**整個概念**。META 透過 IR 發布單季數字，只是本管線沒接。真正的解法也不是等它——`decisionRobustness` 改問「未驗證的那一份足不足以翻轉判定」，答案是 ROBUST（±25% 內判定不變），所以規則恢復評估，連坐式封鎖取消 |
| `as_of_query` 從未執行 | 「`filed` 已存，但沒跑過一次 as-of 查詢」 | 已實測並納入測試：站在 2026-07-15 看不到 SNDK 於 2026-08-06 才申報的那一季 |
| 輸出 schema allowlist | 「目前買賣護欄只有 regex，可被改寫繞過」 | `lib/output-contract.mjs`：未宣告鍵一律拒收，禁用鍵一律拒收，建議式句型只掃「可能承載模型生成文字」的欄位。引擎違約直接 `exit 1`，不會產出檔案 |

---

## F. Research Tool Production Definition（裁決 §29）

```
[x] Canonical calculation engine exists              gauges.mjs, calc v4.0.0
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
[x] No BUY / SELL / target price outputs             輸出契約（schema + 句型），非 HTML 掃描
[x] Calculation versions are traceable               calc version + code commit 印在頁面上
[x] Data lateness distinguishes source from pipeline 三層新鮮度：expected / available / ingested
[x] Unverified components cannot silently block      敏感度測試取代連坐
[x] Evidence coverage never presented as confidence  命名規則寫進資料本身
[x] Every computed gauge reaches the page            測試強制（曾經少掉一張卡片）
```

**18/18。**

第四輪追加完成：三層新鮮度（把「來源慢」和「管線沒接」分開）、概念契約
（`CASH_PPE_CAPEX`，明確排除融資租賃並揭露缺口）、決策穩健度取代連坐、
輸出契約取代 HTML 掃描、快照歷史、測試依類別呈現、`npm run build` 單一入口。

**下一步仍然不是 ALFRED，也不是加指標。** 目前的瓶頸依序是：

1. **Signal Validation 一個測試都沒有。** 59 個測試證明的是「管線沒有騙人」，
   不是「這些門檻有用」。這一層要的是回測與樣本外檢驗，不是再多寫幾個單元測試。
2. **Measurement Validity 只完成了一半。** capex 的概念契約寫死了，但其他 15 格還沒有
   對應的契約——「這個標籤底下量到的是哪一個概念」目前只有 capex 答得出來。
3. **Signal Behavior Diagnostics 需要時間累積。** 快照從今天開始有，第二份出現之前，
   「上次之後有什麼變了」只能顯示它自己還沒有歷史。

落實計畫見 `docs/roadmap-and-questions-v4.md`。
