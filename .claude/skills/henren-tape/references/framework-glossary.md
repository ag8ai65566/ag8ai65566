# 術語對照表 — 原文 → 實作

The framework is a Chinese-language YouTube channel; the code and docs are English; the
dashboard is Chinese again. Terminology has already drifted once across that boundary and
it cost the most important signal in the system, so every load-bearing term gets a row.

**A divergence is not a bug to hide — it is a decision to declare.** Any row marked
`YES` must be visible in the UI wherever that metric appears.

| 原文 | 字面意思 | 框架含義 | 實作的指標 | 偏離 |
| --- | --- | --- | --- | --- |
| **二階導數 / 環比增速** | second derivative / QoQ growth | 他明確指的是**環比**（QoQ）增速的變化 —— 加速度 | **規則用 QoQ**（`henren.rule_metric = 'QoQ'`）；YoY 只放在 `empirical` 當脈絡 | **已修正**。先前版本用 YoY 當主判，等於換掉了他的訊號 |
| 環比 | month/quarter over previous | QoQ | QoQ | 無 |
| 同比 | year over year | YoY | YoY | 無 |
| **洗盤** | wash-out | 部位清洗，趨勢未變 | 無自動判定；由 `henren-tape/SKILL.md` 的 5 項對照表人工判讀 | 未自動化 |
| **葬禮** | funeral | 基本面轉向的下跌 | 同上 | 未自動化 |
| **分層塌方** | layered collapse | 泡沫逐層破裂，指數不同步 | 無自動判定 | 未自動化 |
| **金絲雀** | canary | 產業鏈最上游的訂單／預付款／take-or-pay | 未接線 | **NOT_WIRED** |
| **燃料** | fuel | Fed H.4.1 準備金餘額 | FRED `WRESBAL` 水位 + 4/13 週變化 + 五年百分位 | 他只給水位門檻；速度百分位是本系統加的，已標示 |
| **點火** | ignition | 選擇權 put/call **偏度**極端倒掛 + 現貨抗跌 | Cboe VIX ÷ VIX3M **期限結構** | **YES** — 偏度 ≠ 期限結構，兩者可能相反。已標 `proxy: true` 並註明應改用 Cboe SKEW |
| **逃生鈴** | escape bell | 雲廠商 capex 環比增速見頂回落 | QoQ（規則），因差分未對帳而 `NO_DECISION` | 指標本身無偏離；**資料驗證未完成** |
| **擁擠** | crowding | 部位集中度 | **未實作**。現有的是 `AI 籃子相對波動` —— 已實現波動比值，不是部位資料 | **YES**，已改名，不再叫 Crowding |
| **增負差** | growth-negative gap | M2 年增 − 納指年增 | 同名，兩腿錨定同一日期 | 無（時間對齊已修） |
| **經典 8V 指標** | — | 他讀到 234%，語境為巴菲特指標 | Z.1 企業股權 ÷ GDP | 分母定義與他不同，數值對不齊，已標示 |
| **五步三開關** | 5 steps 3 switches | 二波打法 | 開關 1、2 已接線；開關 3 資料未對帳；五步為人工流程 | 見 `playbook.md` |

## 已發生過的漂移事故

**二階導 → QoQ → 實作成 YoY。** 他的原話明確是環比；轉成英文筆記時變成 "capex growth
rate"；實作時因為 QoQ 有季節性（2025Q1 −0.6%、2026Q1 +9.37%）而選了 YoY，
理由寫在程式註解裡，但**主判燈號用的是 YoY**。

結果是：一個標著「開關三」的綠燈，量的其實不是他的開關三。
第三輪審查裁定必須分軌，現已改為 QoQ 為規則、YoY 為脈絡。

**教訓**：跨語言的實作偏離不會在測試裡現形，因為兩邊都「算對了」。
只有把原文擺在旁邊比對才看得出來。這張表就是為此存在。

## 維護規則

- 任何新指標若對應到框架的某個名詞，**必須**在此登記一列。
- `偏離 = YES` 的列，UI 上該指標出現的地方**必須**顯示偏離說明。
- 翻譯以**他的原文**為準，不以英文中間層為準。
