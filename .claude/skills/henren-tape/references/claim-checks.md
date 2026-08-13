# Claim log — @henren778's checkable claims vs the tape

Checked against Yahoo Finance closes and FRED series on 2026-08-10 (last equity close
2026-08-07). Rerun `../../us-market-brief/scripts/market-snapshot.mjs` and
`../scripts/gauges.mjs` before relying on any of this.

---

## ⛔ 這份評分不能當成準確率。讀下面這段再看表格。

**這裡的宣稱幾乎全部出自他自己的一支「對賬／復盤」影片。** 復盤影片按定義就是作者
**挑選出來的成功案例**。拿一個人自選的高光片段替他打分，然後得出「六項全中」，
**在統計上沒有意義**——不管那些數字本身多精準（它們確實精準）。

這個檔案的前一版把這個結果寫成「所以這個框架值得用」，並被引用進 `SKILL.md`。
那是錯的推論，已經移除。

**這份表格現在的定位是：機制合理性的佐證，不是命中率的證據。**
它能回答「他描述的機制在這些案例裡對不對得上盤面」，
**不能**回答「他下次會不會準」。後者需要的是事前樣本，記在
`../../../data/predictions.jsonl`（不可修改的預測帳本），從 2026-08-10 開始累積。

框架值得使用的理由，改為建立在它**內在的可分離性**上——三層各自有獨立、可量測的
代理變數，而且彼此可以互相否證——而不是建立在任何命中率上。

---

The point is **calibration, not fandom**. Score the misses too — including this file's own.

## ⚠️ Correction — 2026-08-10

The first version of this log scored the 腰斬 line as **"overstated"**, comparing it
against Meta's *current* price. That was wrong twice over, and the transcript shows why:

- **Wrong referent.** He is describing **Meta in 2021–2023** as a historical case study of
  "a $44.8B buyback did not stop the repricing" — not making a claim about Meta today.
- **Wrong direction.** Meta fell from **382.18 (2021-09-07) to 88.91 (2022-11-03) =
  −76.7%**. 腰斬 means −50%. He *understated* it.

This is exactly the failure mode the corpus file warns about — a title read without its
transcript is a claim stripped of its referent — and it landed on the first pass. The
lesson is kept here rather than quietly edited away.

## Verified — the 2026 second-wave call

| Claim | Tape | Verdict |
| --- | --- | --- |
| 納指洗完近一成 | ^IXIC 27,093.90 (2026-06-02) → 24,442.94 (2026-07-29) = **−9.78%** | ✅ accurate to two decimals |
| 二波窗口鎖死 7月底8月初 | Nasdaq bottomed **2026-07-29**; +9.20% since | ✅ pre-registered window, low landed inside it |
| 美光單日暴拉 18.4% | MU **+18.36% on 2026-07-30** — the session after the low | ✅ accurate to one decimal |
| 道指標普齊創新高 | ^GSPC at its 52w high 2026-08-07; ^DJI high 2026-08-05, −0.57% off | ✅ |
| 鬼故事是洗盤不是葬禮 | −9.78% index drawdown fully recovered; credit never widened | ✅ |
| 泡沫分層塌方，不是巨響崩盤 | SMH −24.62%, MU −39.10% June→July **while ^GSPC never made a lower low** | ✅ damage stayed local |
| 底部區間算在 26,000–27,600 (NDX 承接區 26,800–28,200) | ^IXIC low 24,442.94 — but he quotes **NDX futures**, a different index from the Composite | ⚪ not comparable on this data; needs the NDX series to score fairly |

## Verified — the three historical case studies

| Claim | Record | Verdict |
| --- | --- | --- |
| Meta 448億美元回購擋不住重新定價 | 2021 10-K: ~$44.81B repurchased. Stock **382.18 → 88.91 = −76.7%** | ✅ and then some |
| Meta FCF 從 384億 腰斬到 184億 | Matches Meta's reported 2021→2022 free cash flow collapse | ✅ |
| Meta 2023「效率之年」股價回到 353 | 2023 close **353.96**, +183.8% on the year | ✅ to the dollar |
| 英國 LDI：30年期殖利率四個交易日 +140bp | Bank of England's own gilt-market case study documents the Sept-2022 LDI fire-sale loop and the emergency long-gilt purchases | ✅ mechanism and scale corroborated |
| GameStop 空頭比例 122%、1月暴漲 | SEC's GameStop staff report documents short interest above 100% of float and the January 2021 volume explosion | ✅ |

## Verified — the live gauges he quotes

| Claim | Live reading | Verdict |
| --- | --- | --- |
| 準備金 8/6 從 2.94兆 回到 3兆出頭 | FRED WRESBAL **2026-08-05 = $2.993T** | ✅ |
| 準備金離 2.8兆 確認線還有安全帶 | 2.993T, +$193B of headroom | ✅ |
| RRP 緩衝已經用完 | FRED RRPONTSYD **2026-08-07 = $1.45B** — effectively zero | ✅ |
| 財政部 TGA 目標 9,500億，當時 9,018億 | FRED WTREGEN **2026-08-05 = $907.3B** | ✅ |
| 納指100 forward P/E 24.96 < 30 未觸發 | Not on a free feed; carried in `manual-gauges.json` at his reading | ⚪ unverified |
| 前十大權重 39.3%、0DTE 64%、融資餘額 1.416兆 | Same — no free live feed | ⚪ unverified, carried with dates |

## Not checkable

| Claim | Why |
| --- | --- |
| 垃圾股一個月暴漲27倍 | The transcript identifies GameStop; the exact 27x depends on the window and intraday prints used |
| 「一個月前就講了」的原始時間戳 | Would need the earlier video's publish record. The 7/29 low landing inside a stated late-July/early-August window is consistent with the claim, but this log cannot independently date the original |

## 2026-08-13 · 媒體說法與框架前提的檢查

這一段檢的不是他，是**本週媒體的說法**，以及**他的規則所依賴的一個前提**。

| 說法 | 這裡的資料 | 結果 |
| --- | --- | --- |
| 「AI 交易回歸」（多家財經媒體，8/12） | 指數成立：標普 7748.5，距 8/7 高點 7757.64 僅 −0.12%。但籃子內部近一個月 MSFT **+27.9%** 對 SNDK **−23.5%**，差 51 個百分點 | ⚠️ **對指數成立，對籃子不成立**。「AI 行情」已經不是一個籃子在動 |
| 四大 2026 全年 capex 約 $725B，年增 77% | SEC 申報 H1 實際合計 **$294.8B**（Q1 $129.75B ＋ Q2 $165.05B）。要達標，H2 需再 $430B，即環比再加速約 46% | ⚪ **未證實但不矛盾**，需 Q3 資料 |
| 標普創新高 | 52 週高點 7757.64（2026-08-07），與快照一致 | ✅ |

### 一個前提上的問題（本系統的觀察，不是他的話）

他的逃生鈴規則是：**capex 環比增速見頂回落 → 立刻平倉**。這條規則預設
「capex 增速是需求的代理，增速還在上升就代表需求還在」。

本季市場的反應與這個預設相反：Alphabet 上調 2026 資本支出後股價下跌約 7%，
Amazon、Meta、Microsoft 同步走弱。**市場把 capex 上升讀成投資報酬率的問題，
不是需求的證據。**

如果這個轉變持續，「等環比見頂回落再出場」會是一個**結構性遲到**的訊號——
價格先反映 ROI 疑慮，資料要再過一季才確認增速轉折。實際數字支持這個張力：
2026-Q2 環比 **+27.21%**、年增 **+87.03%**，兩者都是序列最高，
**逃生鈴按他的原話沒有響**，而 MU −24.9%、SNDK −42.4%、META −26.3%（距兩年高點）
已經跌完了。

這**不構成「他錯了」**。它是一個具名、可被推翻的觀察：
若下一季有雲廠商上調 capex 而股價正面反應，這個觀察就被推翻。

## How to read this scorecard

Every checkable claim in the sample lands, several to the decimal, and the live liquidity
readings reconcile exactly with FRED. **That is a statement about this sample, and the
sample is his.** See the block at the top of this file: a recap video selects for hits, so
no hit-rate can be inferred from it, however precise the individual numbers are.

What it *does* establish: the mechanisms he describes are real and are visible in the
tape — a positioning flush that leaves credit untouched, damage that stays local while
the index makes highs, a memory name gapping 18% the session after the low. That is worth
having as a lens.

The one row this log got wrong was wrong because *the log* read a title without its
source, not because he did. Working rule unchanged:
**borrow the structure, re-derive every number.** Forward, unselected scoring lives in
`../../../data/predictions.jsonl`.
