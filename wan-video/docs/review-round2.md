# 對 Round 2 審查的逐條回應

> 審查文件：`Hololive_Project_Final_Implementation_Review_Round2.docx`
> 分支 `claude/local-image-to-animation-ai-375zyw`

**六條全部確認屬實，六條全部照修。** 沒有一條是誤判，所以下面不是辯解，是紀錄
改了什麼、以及過程中順便挖出來的兩件審查沒提到的事。

審查文件另外提到有一個 companion patch（`Hololive_Project_Round2_Core.patch`），
**那個檔案沒有一起上傳，我沒有拿到**。以下全部是照文件裡的說明自己實作的，
所以行號和變數命名可能跟那份 patch 不完全一樣，但語意應該一致。

---

## P0-1：`next_pair()` 的去重鍵少了 seed —— 屬實，已修

`seen` 原本是 `(criterion, sorted(A,B))`。在 seed 11 投過 A/B 之後，
seed 22、33、44 的 A/B 全部被當成投過了。

這個 bug 的嚴重性正如審查所說：**跑固定 seed 然後只收其中一個 seed 的票，
比不跑固定 seed 還糟**，因為結果看起來是受控的。

```python
seen = {(v.criterion, v.seed, v.pair) for v in exp.votes if v.criterion == criterion}
...
if (criterion, seed, tuple(sorted((a_id, b_id)))) in seen:
    continue
```

**驗證**：把程式改回舊版，新測試會失敗（`the same A/B is still judged on the
second seed (None)`）；改回新版就過。下面每一條我都做了同樣的往回測。

## P0-2：平手只存一邊 —— 屬實，已修

`Vote` 加了 `other: str = ""`，以及 `pair` / `sides` 兩個 property。

審查說「舊的 tie 本來就沒有第二邊，資料不可還原；不要猜」——完全同意，
所以 legacy tie 的 `pair` 回傳 `(loser, loser)`，去重時不會對上任何真實配對，
`sides` 只回傳那一個已知的邊。代價是舊的 tie 配對可能再出現一次；
**多按一次的成本 vs 猜錯一個 variant 的成本，前者便宜太多。**

server 端加上審查給的驗證（有 winner 就不能等於 loser；沒有 winner 就必須帶
兩個不同的 variant），前端 tie 時送 `other: p.b.variant`。

`standings()` 的 tie 現在同時記到兩邊。往回測：舊版是 `(1, 0)`。

## P0-3：中途失敗會讓 seed 對齊位移 —— 屬實，已修

這條最容易被當成小事，但它產生的是**錯的結果不是缺的結果**。
`variant.jobs` 的「位置」是唯一在記錄「這張圖是哪個 seed」的東西，
所以失敗那格直接 `continue` 會讓後面每一張都往左滑一格 ——
seed 33 的圖會被標成 seed 22。

server 失敗時改成 `variant.jobs.append("")` 保留格子，
`next_pair()` 看到空字串就跳過那一格但**不重排**。

順帶依審查建議把「有沒有跑過」和「成功幾張」拆開：`job_count` 只數非空的，
新增 `has_run`。因為全部失敗時 `job_count` 是 0，用它擋「已經跑過了」
會讓整個實驗被重新排隊疊上去。

往回測：舊版會提供 `(22, ('', 'b22'))` 這種配對 —— 空字串本身都被當成一張圖了。

## P1：hash cache 用整秒 mtime —— 屬實，已修

`int(stat.st_mtime)` → `stat.st_mtime_ns`。

provenance 的唯一工作就是防止「同檔名但內容變了」，而同一秒內覆寫同大小檔案
正是那個情況。舊 key 會回傳前一個檔案的 digest，也就是**紀錄會說謊**。

測試用 `os.utime(path, ns=...)` 把兩次寫入釘在同一個整數秒、不同奈秒，
精確重現這個形狀。往回測：舊版失敗。

## P1：UI「共 X 次比較」double count —— 屬實，已修

`played` 是 per-variant 的，一次 A 勝 B 會讓兩列各 +1，加總等於把每次比較算兩次。
改成直接數該 criterion 的票數。

這個 bug 的實際傷害是：**在只有一半資料的時候顯示成「資料夠多了」**，
而旁邊那句「票數還太少，先別當結論」的門檻是 10。

## P1：`charpacks.py` evidence hardening —— 屬實，已修，而且比審查說的更嚴重

審查列了五點。前四點照改：

| 項目 | 改成 |
|---|---|
| danbooru count | 只叫 corpus prevalence，並列出中間隔著哪些東西（訓練快照、去重、caption 正規化、tag dropout、取樣權重） |
| 不吃畫師標籤的底模 | 從「加了也沒作用」改成「訓練標註裡沒有畫師名字，所以本專案不自動加 —— 加了會怎樣本專案沒有實測過」 |
| costume weighting | 從「strongest identity lever」改成「explicit control」，並寫明強弱排序是 fixed-seed benchmark 的工作 |
| `build_prompt` 的 `likeness_tags` | 預設從 `None`（會自動塞 `official art`）改成 `""`。必須由知道 checkpoint 的 caller 明確帶入 |

第五點「1-3% 不可套成每角色 fact」——**審查是對的，而且我去量了之後發現原本那個
數字本身就是錯的，不只是套用範圍的問題。**

---

## 審查沒提到、但查證過程中挖出來的兩件事

### 甲、「官方圖只佔 1-3%」這個數字錯了

原本的說法是「這些角色的官方圖只佔 1～3%」。那是抽查**最紅的幾位**得到的，
然後被寫成了全體的事實。

2026-08-23 對全部 75 位逐一量測（`counts/posts.json?tags=<角色> official_art`）：

| | |
|---|---|
| 範圍 | **0.62%（桐生可可）到 9.45%（時乃空）** |
| 中位數 | 3.70% |
| 加總 | 3.17%（424,064 張裡有 13,434 張） |
| 超過 5% 的 | **75 位裡有 28 位** |

而且分佈不是雜訊，它跟人氣相關 —— 而且是往**削弱**原本主張的方向：

```
Pearson r（log10 張數 vs 官方圖 %）   -0.646
張數 >= 10,000 的成員   中位數 2.08%
張數 <  2,000 的成員    中位數 7.79%
```

合理：官方圖大致按固定速率累積，同人圖隨人氣複利成長，
所以**越紅的成員官方圖佔比越薄**。1-3% 剛好就是最紅那幾位的區間。

**處理**：把每一位的實測值（`official_posts`）寫進角色包資料，UI 改成報
**眼前這位角色的實際數字**，並依她落在四分位的哪一段換說法：

- 低於 Q1（2.50%）：「屬於偏低的四分之一，模型能學到的主要是同人平均值」
- 高於 Q3（5.87%）：「屬於偏高的四分之一，**『只學到同人平均』對她比較講不通** ——
  不像的原因可能在別的地方」
- 中間：「大約落在中位數附近。官方圖仍是少數，但沒有少到可以斷定一定學不到」

所以 Gawr Gura（1.06%）那句話照講，時乃空（9.45%）那句話**直接收回**。
每一句後面都補上「這是 danbooru 的資料比例，不是量到的模型行為」。

### 乙、角色包裡有一個打錯的 danbooru tag

量測時 `hidoshi_ao` 回傳 **0 張**。正確的 tag 是 `hiodoshi_ao`（1,006 張），
她的服裝 tag 也一樣（`hiodoshi_ao_(1st_costume)`，517 張）。

也就是說**火威青這位角色的觸發詞一直是無效的** —— 生成她時那兩個 token
什麼都不對應。已修，順便把她的 `danbooru_posts` 從 0 補成 1,006。

這也是為什麼「量」比「說」值錢：這個 bug 只有在對全部 75 位跑一遍查詢時才會浮出來。

---

## 測試

| | 之前 | 現在 |
|---|---|---|
| Python | 2,713 | **2,742** |
| stub-DOM | 42 | **50** |
| 真 Chromium | 162 | 162（新增的投票檢查在這台機器上跳過，見下） |

新增的 regression 全部做過**往回測**：把程式改回修正前的版本，
對應的測試會失敗；改回來就過。**六個 bug 全部這樣確認過**，不是只確認「新版會過」：

```
seed 去重      舊版 → ✗ the same A/B is still judged on the second seed (None)
失敗格位移      舊版 → ✗ a failed middle cell is skipped, not shifted
                       （而且舊版還會把空字串本身當成一張圖去配對）
tie 雙邊        舊版 → ✗ a tie counts for both sides (1, 0)
mtime 奈秒      舊版 → ✗ the hash still changes, because the cache key is nanoseconds
tie payload    舊版 → ✗ a tie posts both variants（other 根本沒送出去）
比較次數        舊版 → ✗ the standings count votes（顯示「共 4 次比較」，實際 2 次）
```

前端那兩個是加在 `tests/ui_smoke.js`（stub DOM）而不是 Chromium：
Chromium 的實驗區塊需要機器上真的裝了一個 checkpoint 才會執行，
這個容器裡沒有，所以那一段整塊被跳過。stub DOM 那邊把 `fetch` 換掉，
直接檢查送出去的 payload 形狀跟那一行算術 —— 對這兩個 bug 來說已經足夠，
但**必須說清楚它不是在真瀏覽器裡跑的**。

---

## 關於 Stop rule 和 GPU gate

審查第 11 節的 PASS gate，前五項已完成：

- [x] P0 三個 benchmark integrity bug
- [x] regression tests 並全數通過
- [x] 前端 tie 與 comparison count
- [x] provenance hash 用 nanosecond mtime
- [x] charpacks 不再把 danbooru count / artist tag / costume weight 寫成未實測的模型定律
- [ ] **Stage A GPU benchmark** —— 這一項我做不到

最後一項不是還沒排到，是**這台機器沒有 GPU**，而且從專案開始到現在
**一張圖都沒有生成過**。所以：

- 審查說「不再靠評論收工，用結果收工」—— 同意，而且這正是
  `app/experiments.py` 存在的理由：固定 seed、內容雜湊的來源紀錄、盲測 pairwise。
- 但那台機器是使用者的。這一輪能做的是**把那台機器上跑出來的數字保證是可信的** ——
  也就是上面那三個 bookkeeping bug。修完之後，Stage A 跑出來的排名才有意義。

我同意 Stop rule：**除非出現新的實際 bug、測試失敗，或 GPU benchmark 暴露新問題，
不需要第三輪全面審查。**
