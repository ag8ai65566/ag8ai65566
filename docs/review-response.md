# 對 Institutional-Grade 規格書的回應

**日期** 2026-08-10 · **對應文件** 股票投資研究系統 Institutional-Grade 升級規格 v1.0
**狀態** P0 已實作一部分；其餘分類為「已排程」「需求先釐清」「不同意」

審查抓到的東西是對的，而且比我自己的自評更狠。已經改的部分在 §1。
有五件事我想跟審查者辯論，在 §5——不是為了替架構辯護，是因為我認為在**釐清系統定位之前**
就照單全收，會把工程量花在錯的地方。

---

## 1. 已實作

### 1.1 P0-2 · Missing Data ⇒ NO_DECISION（**這條抓到一個正在說謊的綠燈**）

實作後第一次執行就發現：**`^VIX3M` 最近六個交易日的收盤全是 `null`。**

舊版的開關二做的是 `vix.at(-1) / vix3m.at(-1)`。因為 `null` 被 filter 掉，
`.at(-1)` 取到的是 **2026-07-17**。所以它拿 **8/7 的 VIX 除以 7/17 的 VIX3M**，
得到 0.725，報**綠燈**，寫進儀表板，也寫進了給使用者的分析。

那個綠燈完全是資料缺漏製造出來的。這正是規格書 §5 講的
「Missing → Neutral」——而且它發生在三個開關之一上。

現在的行為：
```
⚠️ 開關二 · 點火（代理指標）   DATE_MISMATCH
   ^VIX 收在 2026-08-07、^VIX3M 收在 2026-07-17，不同交易日不可相除。
```

狀態詞彙已改為規格書 §13 的形式：`CURRENT_AS_PUBLISHED` / `LAGGED_BY_DESIGN` /
`OVERDUE` / `STALE` / `DATE_MISMATCH` / `SOURCE_FAILURE` / `MISSING` /
`INSUFFICIENT_HISTORY` / `NOT_WIRED`。每一格帶 `decision: SCORED | NO_DECISION`，
**只有 SCORED 進入燈號計數**。

### 1.2 P0-4 · M2 / Nasdaq 時間對齊（**修正後燈號由黃翻紅**）

舊版拿 6 月的 M2 對 8 月的納指，讀數 −22（黃燈）。
新版以較慢序列（M2，2026-06-01）為錨點 `t`，兩邊都用 calendar-aware 的 YoY：

| | 舊（錯） | 新（對齊） |
| --- | --- | --- |
| 讀數 | −22 個百分點 | **−36.2 個百分點** |
| 燈號 | 🟡 | **🔴** |
| 描述的時點 | 無意義的混合 | 明確標示為 2026-06-01，不是今天 |

也就是說**這個 bug 一直在壓低一個紅燈**。新版另外回報
`nasdaq_close_used` 與兩邊的一年前基準日，並直接寫明「此讀數描述的是 6/1，不是今天」。

沒有再使用 `today - 365 days`。

### 1.3 P0-5 · Crowding 指標改名並改統計量

同意全部四個理由。舊版是 `max(籃子個股波動 / SPX 波動)`，命名為 Crowding。

- 改名為 **`AI 籃子相對波動`**——名稱符合實際計算內容。
- 從 **max 改為中位數**：11.1× → **5.9×**（仍是紅燈，但不再由單一極端值代表市場）。
- 完整分布（min / median / max / 每一檔）都回報，不只一個數字。
- 內嵌兩段警語：`naming_note` 說明真正的擁擠度需要部位資料（集中度、廣度、
  橫斷面相關性、成交量異常、選擇權部位），這些**尚未接線**；
  `selection_bias_note` 說明籃子是人工挑選的。

### 1.4 P0-3 · 準備金指標補上速度

原 thesis 是「**快速**跌破」，舊版只實作了 level。現在回報
`change_4w_pct`、`change_13w_pct`，以及**四週變化在五年分布中的百分位**。

過程中抓到我自己的一個過度擬合：我先寫了「四週跌 3% 即黃燈」，
實測 −3.41% 落在 **p21.8**——那根本不算快，等於製造假警報。
改成**底部十分位**才觸發。修正後開關一回到綠燈，註記寫明
「四週變化 −3.41% 落在 p21.8，不構成『快速』流失」。

這正好示範規格書 §9 的論點：手挑的門檻會製造假訊號。

### 1.5 P0-1 · 移除未驗證綜合分數

儀表板上的「泡沫水位＝高（9/12）」「油量＝滿的（8/12）」**已完全移除**。
輸出裡帶一個明確欄位：

```json
"no_composite_score": "This build emits no bubble score, no market score, and no 0-100 index."
```

儀表板改為只呈現組成，並在頁面上直接解釋為什麼沒有總分。

### 1.6 P0-6 / P0-10 · 百分位門檻 + 每資料集 SLA

- 每個有足夠歷史的指標都同時回報 rolling percentile（5 年，信用利差另加 20 年）；
  樣本 < 30 回報 `INSUFFICIENT_HISTORY` 而不是硬算。
- 時效改由 `config/data-sources.json` 每個資料集自己的
  `expected_frequency` / `expected_publication_latency_days` / `acceptable_age_days` 判定。
  GDP 落後一季是 `LAGGED_BY_DESIGN`，日資料落後一週是 `OVERDUE`——舊版的全域 45 天分不出這兩者。

### 1.7 P0-9 / §14 / §32-D · Source Registry 與 Data Contract

新增 `config/data-sources.json`：每個來源標 `authority_level`
（`PRIMARY_OFFICIAL` / `OFFICIAL_AGGREGATOR` / `UNOFFICIAL_FREE` / `EXPERT_HYPOTHESIS`），
每個資料集有完整 contract。**gauges.mjs 找不到 registry 條目就拒絕產生數值。**

狠人的 authority_level 明確定為 `EXPERT_HYPOTHESIS`，並註明
「供給假說與待測門檻，不供給任何金融資料」。

### 1.8 Layer 1 最小版 · 原始回應與 hash

每次執行把原始回應存到 `data/raw/<date>/`，並把 sha256 前綴寫進每一格的 provenance。
`data/raw/` 進 gitignore（每次約 1MB），但 **hash 留在 `data/gauges.json` 裡且進版控**——
重抓後 hash 不同即證明來源在我們腳下改過。

### 1.9 §19 · Immutable Prediction Ledger

`data/predictions.jsonl` 已建立，含三筆事前、有明確 target 與證偽條件的宣稱，
評估日 2026-10-15 / 11-10。每筆的 `confidence_basis` 明寫
**`UNCALIBRATED — 此系統無歷史命中率，MEDIUM 只是作者主觀措辭，不是機率`**。

### 1.10 選擇偏差（**規格書沒提到，但我認為是最嚴重的一條**）

規格書 §20 講了 backtest 的 selection bias，但沒有連到一個更直接的問題：
**這套框架的可信度，是用他自己的「對賬影片」建立的。**

復盤影片按定義就是作者挑選出來的成功案例。我拿那個樣本打出「六項全中」，
然後把它寫進 `SKILL.md` 當成「所以框架值得用」。**那是無效推論。**

已改：`claim-checks.md` 頂端加了停止符號的警語區塊；結論句改寫為
「這是關於這個樣本的陳述，而樣本是他選的」；`SKILL.md` 裡以命中率為理由的句子
全部移除，改為建立在**三層的可分離性與可獨立量測性**上。
事前樣本改記在 `data/predictions.jsonl`。

---

## 2. 目前狀態（實作後）

```
已計分 10　·　未計分 6
🟢 4　🟡 2　🔴 4        ← 只計 SCORED

未計分：
⚠️ 開關二 · 點火          DATE_MISMATCH（^VIX3M 資料缺漏）
⚠️ 巴菲特指標             DATE_MISMATCH（分子 01-01、分母 04-01，差 90 天）
⛔ 開關三 · 逃生鈴         NOT_WIRED
⚪ 融資餘額 / 內部人比 / 預估本益比   STALE
```

**三個開關現在有兩個是 NO_DECISION。** 這比舊版「三個全綠」誠實得多，
也直接說明了系統目前的真實能力。

---

## 3. 已排程但未做（同意，但需要工程時間）

| 規格 | 為何未做 | 計畫 |
| --- | --- | --- |
| P0-7 ALFRED vintage | 需要逐序列 vintage 抓取與儲存 | registry 已預留 `vintage_source` 欄位；在做任何 backtest **之前**必須完成 |
| P0-8 SEC point-in-time fundamentals | 需要 companyfacts + `accepted_at` 索引 | registry 已註冊 `sec_edgar` 並標明 `point_in_time_key: accepted_at`；這是 Serenity 鏡頭能真正運作的前提 |
| §20 Backtesting | **依賴 P0-7**。沒有 vintage 就做回測，等於用修訂後的數字回測，結論無效 | 順序不可顛倒 |
| §26 Automated tests | 應該對每個已修的 P0 bug 寫回歸測試 | 下一批；`^VIX3M` 這個 case 是第一個測試 |
| §2 Layer 2 Evidence objects | 見 §5.3 —— 我對範圍有意見 | |

---

## 4. 技術性補充：CapEx 逃生鈴（規格書 §17）

同意「不能只抓 `PaymentsToAcquirePropertyPlantAndEquipment`」，但問題比列出的更嚴重：

**融資租賃（finance leases）。** 超大規模雲廠商的 AI 資料中心有相當部分是透過融資租賃
取得，這**完全不進現金 capex**。所以即使做出完美的 XBRL pipeline，
測到的仍然是一個系統性低估的量。這對「增速的導數」尤其致命——
租賃佔比若在變化，導數本身就被污染了。

**其次，他真正要看的東西可能根本不在 XBRL 裡。** 他的規則是看
「增速有沒有見頂」，而市場對此反應最劇烈的是**法說會上的 capex 指引**，
不是已發生的現金支出。指引沒有 XBRL tag。

所以我把這格標為 `NOT_WIRED` 而非「待抓取」，並在 registry 寫下 blocker。
它可能**無法完全自動化**，需要一張人工維護的
`cash_capex_definition` / `finance_lease` / `management_guidance` 對照表——
也就是規格書自己提的 Company CapEx Mapping。**同意這個方向，但想確認：
一個不可能完全自動化的訊號，在 Production Readiness Gate 裡該怎麼算？**

---

## 5. 想跟審查者討論的五件事

### 5.1 規格書防守的是一個這套系統沒有的功能——請先確認目標

規格書 §0、§1、§21、§22、§31 反覆針對：`STRONG BUY`、`87/100`、
`模型勝率 XX%`、`Position sizing recommendation`。

**這套系統從第一版起就明文禁止輸出買賣訊號與目標價**，四個 skill 的
SKILL.md 都寫了，實際輸出也沒有出現過。使用者問「該不該出清閃迪美光」時，
系統給的是層級診斷與觸發條件，明確拒答買賣。

所以有一大塊規格是在防守一個尚未存在的功能。這不是壞事，但它讓
**Production Readiness Gate 的 18 個勾選項，是為了「Validated Stock Recommendation Engine」設計的**。

想確認的問題：

> **目標是把它變成推薦引擎（那整份規格適用，工程量以人月計），
> 還是讓它停在研究工具（那 §21–22、§29 的 position sizing、
> expected return distribution 都不該進 roadmap）？**

我的建議是後者，並把系統正式定名為規格書 §35 說的
**Research & Risk Intelligence Platform**，然後把 Gate 縮成
「研究工具版」：可追溯、可重現、不騙人，但不承諾預測力。
兩者的工程量差一個數量級。

### 5.2 「Yahoo 不能是權威來源」——同意，但替代方案的成本與這個系統不成比例

SIP/exchange-grade 授權資料是對的答案，也是每年數千美元起跳。
這是**單一使用者的個人研究工具**。

我採取的立場，想請確認是否可接受：
**不假裝 Yahoo 是權威。** registry 明寫 `UNOFFICIAL_FREE`，
而且這個等級會**沿著計算鏈傳遞到報告裡**——例如 M2 gap 那格標
`mixed_authority: 以較低者為準`。加上 Stooq 作獨立交叉檢查，
歧異超過容忍值就報 `SOURCE_CONFLICT`（規格書 §24）。

也就是說：不升級來源，但**升級對來源的誠實度**。

> **請裁決：對一個個人研究工具，「誠實標示 UNOFFICIAL_FREE 並做交叉檢查」
> 是否可接受？還是只要來源不是 SIP 等級，任何價格衍生的結論都不該產出？**

### 5.3 Evidence Plane 的完整版，我認為 ROI 不對——提案輕量版

規格書 §2 Layer 2 要求每條 evidence 帶 15 個欄位
（含 `authority_score` / `independence_score` / `directness_score`），
§23 要求每個結論可展開完整 evidence chain 含 contradictory evidence。

方向完全同意，特別是 §16「公司自己說」vs「客戶 filing 顯示」不能等價——這是真的洞見。

但完整版是一個 evidence 資料庫專案。目前系統的產出是**一個儀表板加一份報告**。
先建 graph 再有內容，順序可能反了。

**提案（已部分實作）**：先做「每個**數字**帶 provenance」，
而不是「每個**論述**帶 evidence graph」。目前每一格已經帶
source / authority / effective_date / retrieved_at / age / transformation / raw_hash。

下一步做 §16 的三維評分，但只用在**文字結論**上，
且限縮為三個等級而非連續分數。等 evidence 條目累積到某個量再考慮圖結構。

> **請裁決：完整 Evidence Plane 是 P0 還是 P1？
> 我主張 P1，因為在資料層還有兩個 DATE_MISMATCH 的情況下建 evidence graph，
> 是在不可信的地基上蓋樓。**

### 5.4 Production Readiness Gate 是全有全無，建議改成逐指標分級

§31 的 18 個勾選項是全域的。一個個人工具可能永遠無法全部達成
（例如「Critical data have authoritative sources」在 §5.2 未解決前就過不了）。
全有全無的 gate 的實際後果是**永遠不會被通過，於是被忽略**。

**提案**：把 gate 下放到單一指標層級，每格帶自己的成熟度：

```
RAW        — 有讀數，來源已註冊，無驗證
CHECKED    — 時間對齊已驗證，freshness SLA 已定義，provenance 完整
VALIDATED  — 有定義 target、point-in-time 回測、樣本外驗證
```

報告頂端顯示：「本次結論中，3 格 VALIDATED、7 格 CHECKED、6 格 NO_DECISION」。
這比一個全域布林值資訊量大得多，也讓系統可以**逐格升級**而不是等一次大爆炸。

目前實際狀態是：**0 格 VALIDATED、10 格 CHECKED、6 格 NO_DECISION。**

> **請裁決：可否用逐指標分級取代全域 gate？**

### 5.5 一個規格書沒有回答的問題：這個框架本身該不該留

規格書 §2 和 §34 的回答很好——專家框架是 hypothesis engine，不是 ground truth，
護城河不該是「我們用了某個高手的框架」。我接受。

但還有一層沒被回答：**在 point-in-time 資料與回測都還沒有的情況下，
「狠人的門檻值」和「隨便一個門檻值」在資訊量上有差別嗎？**

目前所有門檻（2.8兆 / 2.5兆 / 3bp / 60% 0DTE / 35% 前十大權重）
都是他講的，沒有一個有假警報率。我已經在每格旁邊加了百分位——
但這其實是承認**百分位比他的門檻更有資訊量**。

那接下來的問題就是：

> **應該把他的門檻降級為「參考標記」，讓百分位成為主要判準？
> 還是保留他的門檻作為主判準，直到回測證明它們不如百分位？**

我傾向前者（資料優先於框架，符合規格書 §2 的架構原則），
但這會讓系統實質上**不再是「狠人框架的實作」**，而是
「一組流動性/擁擠度指標，附帶他的門檻作為註腳」。
這是產品定位的改變，不只是技術決策，所以我不單方面決定。

---

## 6. 一句話總結

規格書是對的：**Correctness > Freshness > Provenance > 報告好看。**
照這個順序做，第一次執行就抓到一個假綠燈和一個被壓低的紅燈——
這比之前任何一次「新增指標」都有價值。

我唯一的保留是**範圍**：在確認這是研究工具還是推薦引擎之前，
把工程量投進 evidence graph 與 portfolio risk layer，
可能是在一個還有兩格 DATE_MISMATCH 的地基上蓋樓。

**仅作信息跟踪，不构成投资建议。**
