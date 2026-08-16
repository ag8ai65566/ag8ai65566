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
