# 角色包 —— 一鍵切換角色和衣裝

一支大型角色 LoRA 不是一個觸發詞，是好幾百個。Hololive Collection 一支就有
**75 位角色、319 套衣裝**，而這些資訊只存在於 CivitAI 說明頁上的一大坨文字裡。
每次要用都得回去翻那一坨，才是真正花時間的地方。

所以把它翻一次、存成資料，變成可以點的清單。

---

## 怎麼用

圖片分頁上方會多出一塊「🎤 角色包」：

1. **選期別**（JP 0期生 → 1期生 → … → EN Myth → … → ID 3期生，照出道順序）
   或直接在搜尋框打名字 —— 打 `suisei`、`すいせい` 都找得到
2. **點成員** → 下面出現他所有的衣裝
3. **點衣裝** → 按「填入提詞」

按下去會一次做完四件事：

- 提詞填好（觸發詞 → 這套衣服的外觀標籤 → 你自己打的字 → 品質標籤）
- 負面提詞換成作者建議的那組
- **這支 LoRA 自動勾選**，強度設成作者建議的值
- 底模不對的話會提醒你，旁邊就有「一鍵切換到 Pony」

三個勾可以關：品質標籤、保留自己打的字、套用建議負面詞。

> **「保留我自己打的字」是有記憶的。** 換成別的成員時，上一位的標籤會被剝掉，
> 只留你自己加的（`sitting on a bench, night` 這類）。不然每換一次人，
> 提詞就會愈疊愈長，最後兩個角色打架。

---

## 已經內建的包

| 包 | 內容 | 需要的底模 | LoRA 大小 |
| --- | --- | --- | --- |
| **Hololive Collection JP・EN・ID** by motimalu | 75 位 · 319 套衣裝 | **Pony Diffusion V6 XL** | 914MB |

狀態列會直接告訴你缺什麼，旁邊就是按鈕：

- `LoRA 還沒下載` → 按「下載 914MB」（**需要先在 `.env` 填 CivitAI API key**，
  CivitAI 的下載端點一定要帶金鑰）
- `還沒下載 Pony Diffusion V6 XL` → 按「下載這個底模」
- 底模選錯 → 按「一鍵切換到 Pony」。**這會走跟下拉選單同一條路**，
  所以 sampler、CLIP skip、`score_9, score_8_up, score_7_up` 那串前綴會一起換過去 ——
  不是只換個標籤而已。

### 這個包的幾個實情

- 作者是以**「1st costume」為主**訓練的，所以每位成員的第一套衣服最準，
  後面的衣裝資料量比較少。
- **有些成員 Pony 底模本身就認得**（作者提到 Houshou Marine 可以用 `aua` 這種
  底模自己的代號叫出來），不加 LoRA 也畫得出來，但細節會差。
- 已畢業的成員（桐生ココ、潤羽るしあ、魔乃アロエ、夜空メル、湊あくあ、
  九十九佐命）**放在原本的期別裡並標「已畢業」**，不另外分一區 ——
  你要找 4 期生的時候，ココ 本來就該在那裡。
- 授權是 Fair AI Public License 1.0-SD，作者寫明**僅供非商業同人用途**。

---

## 再加新的包（你之後丟 LoRA 給我的時候）

**你只要給我 CivitAI 連結就好。** 我會去讀那一頁，把成員和衣裝抓出來、排好順序，
存成一個 JSON 檔丟進 `app/packs/`。加一個包**不用改任何程式碼** ——
放一個檔案進去，重開 app 就出現了。

如果你想自己加，格式長這樣（`app/packs/我的包.json`）：

```json
{
  "id": "my-pack",
  "label": "包的名字",
  "file": "檔名.safetensors",
  "civitai": "https://civitai.com/models/…",
  "version_id": 886276,
  "download_url": "https://civitai.com/api/download/models/886276?fileId=…",
  "size": 913775292,
  "base_model": "Pony",
  "wants_model": "pony",
  "strength": 0.8,
  "scaffold": "1girl, virtual youtuber",
  "quality": "score_9, score_8_up, score_7_up, masterpiece, best quality",
  "negative": "作者建議的負面詞",
  "note": "任何要提醒自己的事",

  "groups": [
    { "id": "gen1", "label": "1期生", "members": ["someone", "another"] }
  ],
  "characters": [
    {
      "key": "someone", "name": "Someone", "jp": "誰か", "emoji": "🌸",
      "group": "gen1", "former": false,
      "costumes": [
        { "label": "1st costume",
          "trigger": "someone, someone \\(1st costume\\)",
          "tags": "long hair, blue eyes, …" }
      ]
    }
  ]
}
```

幾個要注意的：

- **`trigger` 裡的括號一定要 `\(` 這樣跳脫。** ComfyUI 把 `(字)` 當成加權語法，
  不跳脫的話 `(1st costume)` 會變成「把這幾個字加重 1.1 倍」，
  而不是一個衣裝名字。內建的包已經統一處理過（來源頁面自己都不一致）。
- `wants_model` 要填 app 認得的底模 id：`pony`、`illustrious`、`juggernaut`、`sdxl-base`。
- `groups` 的順序就是畫面上的順序。**排法有邏輯就好** —— 內建的包用出道順序。
- 沒被列進任何 group 的角色會自動被丟進「其他」，不會消失。
- **檔案壞掉不會讓 app 掛掉**，那個包會被略過，其他的照樣能用。
  少了 `file` 或沒有任何角色的包也會被略過。

---

## 提詞是怎麼組起來的

```
觸發詞 ─────────────►  hoshimachi suisei, hoshimachi suisei \(1st costume\)
作者的 scaffold ────►  1girl, virtual youtuber
那套衣服的標籤 ─────►  blue hair, blue eyes, plaid headwear, beret, …
你自己打的字 ───────►  sitting on a bench, night
品質標籤（最後）────►  score_9, score_8_up, score_7_up, score_6_up, masterpiece, …
```

**品質標籤放最後**是照這支 LoRA 說明頁上每個範例的寫法 ——
Pony 把 score 標籤當成整體品質訊號，不是當成畫面內容。

**重複的標籤會被合併掉**。scaffold 寫了 `1girl`，有些衣裝的標籤也寫了 `1girl`，
重複兩次在 ComfyUI 眼裡等於偷偷加權，不是你要的。


---

## 為什麼生出來跟直播／設定圖不像

這是用角色 LoRA 最常見的失望，而且**不是 bug** —— 是訓練資料本來就長那樣。
我去 danbooru 實際數過：

| 角色 | 總圖數 | 其中官方圖 | 比例 |
| --- | --- | --- | --- |
| Houshou Marine | 17,804 | 298 | **1.7%** |
| Gawr Gura | 16,403 | 174 | **1.1%** |
| Hoshimachi Suisei | 15,155 | 337 | **2.2%** |
| Mori Calliope | 12,544 | 380 | **3.0%** |
| Minato Aqua | 9,590 | 195 | **2.0%** |
| Shirogane Noel | 7,263 | 190 | **2.6%** |

**官方圖只佔 1～3%。** 所以模型學到的「Mori Calliope」是**一萬多張同人圖的平均值**，
不是設定圖，也不是 Live2D 模型。認得出來是她，但就是不會跟官方一模一樣。

### 掛原畫師的 tag 為什麼沒有幫助（有時候還更糟）

這是最反直覺的一點。同樣是數出來的：

| 角色 | 原畫師 | 角色圖數 | 畫師圖數 | **畫師畫這個角色的** |
| --- | --- | --- | --- | --- |
| Mori Calliope | Yukisame | 12,544 | 112 | **30** |
| Hoshimachi Suisei | Teshima Nari | 15,155 | 663 | **14** |
| Gawr Gura | Amashiro Natsuki | 16,403 | 491 | **52** |
| Houshou Marine | Akasa Ai | 17,804 | 699 | 116 |
| Minato Aqua | Gaou | 9,590 | 950 | 151 |
| Shirogane Noel | Watao | 7,263 | 387 | 135 |

Suisei 的媽媽 Teshima Nari 在 danbooru 上總共 663 張，**其中畫 Suisei 的只有 14 張**。

所以 `artist:teshima_nari` 拉進來的是他**畫別人時**的畫風 —— 因為那才是這個 tag
的絕大部分訓練內容。你要的「這位畫師畫這個角色」那個交集，模型幾乎沒學過。

**這裡要說得精確一點**（第二個模型審查後修正）：這些數字支持的結論是
**「原畫師 tag 不是可靠的『身份』控制」**，它是**畫風**控制。至於「加了會不會
反而更不像」——擴散模型本來就擅長把很少同時出現的概念組合起來，所以那句話
我沒有證據，**要你自己固定 seed A/B 比過才算數**。

### 有效的做法（由強到弱）

**1. 拿官方設定圖當來源圖。** 這是唯一能把「官方長相」直接餵給模型的方法。

- **以圖生圖**：把設定圖丟進「＋來源圖」，重繪強度 **0.4～0.6**。
  低於 0.4 幾乎只是複製，高於 0.7 又會漂回同人平均值。
- 或者丟 **ControlNet** 鎖輪廓，提詞照常寫。

角色包每一位都附了官方設定圖庫的連結（fandom wiki），勾「貼近官方設定」就會出現。

**2. 加權服裝 tag ＋ `official art`。** 勾「貼近官方設定」就會做這件事。

原理是：**官方長相＝那一套衣服**，而服裝 tag 恰好是同人圖還原得最忠實的部分。
服裝 tag 的圖數也夠：`mori_calliope_(1st_costume)` 有 3,136 張、
`gawr_gura_(1st_costume)` 有 7,598 張。`official art` 是全站 533,688 張的大 tag，
模型很熟它的構圖與完成度。

強度滑桿建議 **1.2～1.3**，超過 1.4 服裝會開始壓過其他提詞。

**3. 只畫某一位的話，去 CivitAI 找單人 LoRA。**
75 人合集 LoRA 平均下來每個人都會軟一點，單人 LoRA 專門練一個人，像很多。

### 一個提醒

「貼近官方設定」和「原畫師畫風」是**反方向**的：前者要官方長相，
後者要某個人的畫風。兩個同時開，介面會提醒你 —— 建議二選一。

**沒驗過的**：上面說的重繪強度 0.4～0.6、權重 1.2～1.3 是根據結構的推論加社群共識，
不是我實測的（這容器沒有 GPU，一張圖都沒真的生成過）。圖數則全部是查 danbooru API 得到的。
