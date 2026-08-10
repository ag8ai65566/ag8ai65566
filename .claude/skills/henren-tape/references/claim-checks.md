# Claim log — @henren778's checkable claims vs the tape

Checked against Yahoo Finance closes and FRED series on 2026-08-10 (last equity close
2026-08-07). Rerun `../../us-market-brief/scripts/market-snapshot.mjs` and
`../scripts/gauges.mjs` before relying on any of this.

The point is **calibration, not fandom**. Borrow a framework in proportion to how its
author's falsifiable statements hold up. Score the misses too — including this file's own.

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

## How to read this scorecard

Every checkable market claim lands, several to the decimal, including a
**pre-registered timing window** and a set of live liquidity readings that reconcile
exactly with FRED. That is a strong record and it is why the frame in `SKILL.md` is worth
using as a lens.

It is still not a reason to accept the next call on trust. His numbers are load-bearing
where they are checkable — and the one row this log got wrong was wrong because *the log*
skipped the source, not because he did. Working rule unchanged:
**borrow the structure, re-derive every number.**
