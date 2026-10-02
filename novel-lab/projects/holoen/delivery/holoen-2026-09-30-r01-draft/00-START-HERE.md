# 從這裡開始 — holoen r01（草稿候選版，尚未通過全部檢查）

基準日 2026-09-30。這一版有 **18 張角色卡**、**24 張世界觀卡**、18 份 ElevenLabs 表演表。全部用完整卡（沒有精簡版）。
狀態：**靜態檢查通過與否見 `validation.json`；實際匯入和配音測試尚未執行（runtime untested）。**
索引：`01-INDEX.md`。改動：`CHANGELOG.md`。檔案雜湊與狀態：`manifest.json`。

## 1. 十分鐘匯入測試（請在新的、可丟棄的專案做）
1. 新建專案 `holoen-r01-smoke`。不要在你正在寫的專案裡測重複匯入。
2. Story Bible → Characters 標題旁 `•••` → Import → 上傳 `sudowrite/characters.csv`，確認 **18 張**。
   Worldbuilding 同樣匯入 `sudowrite/worldbuilding.csv`，確認 **24 個**。每個合併 CSV 只匯入一次。
3. 打開 Fuwawa、Mococo 和另一個角色：雙胞胎是兩張卡、`Role` 是 Protagonist、自訂特質（含 `Audio Tags`）有內容。
   找一個多行或有標點的欄位，和 `sudowrite/paste.md` 對照。打開 FUWAMOCO 和一張 History 卡。
4. 確認 Secrets 都是空的（這一版全空；以後若有內容，生成前要先按眼睛圖示隱藏）。
5. 把 `sudowrite/style.txt` 貼到 Style。測試用：Genre 填 `Light comic fantasy`，Braindump 填
   `Fuwawa Abyssgard and Mococo Abyssgard compare a map inside a fictional game.`，Synopsis 留白；設定第三人稱、過去式。
6. 新建一個章節／場景：`Scene date: 2026-09-30. Fuwawa Abyssgard and Mococo Abyssgard, the members of FUWAMOCO,
   compare a map inside a fictional game. Keep their speaking turns distinct.`
7. 看兩人和 FUWAMOCO 有沒有出現偵測底線；沒有就記下來，檢查名稱與可見性後再試。
8. 生成最短的一段：說話者分得開、對白有可用的表演標籤、敘述沒有標籤。把匯入和生成的結果分開記在
   `performance/test-results.csv`（含版本 r01 和使用的模型）。有問題就保留這個測試專案方便排查。

## 2. 三行原創聲音測試（ElevenLabs v4）
用兩個**你自己設計的原創聲音**（不要複製或模仿成員的真實聲音），A/B/A 輪流。以下是風格示範，不是引用：
```text
A: [calm] We can check the map again.
B: [startled] Ah! That door moved.
A: [laughs] Fuwawa, Mococo—your turn.
```
選 `eleven_v4`，用對應表演表的起始設定（UI 用百分比，API 用小數）。每行一個 turn、各自指定聲音。
聽：聲音分配對不對、語氣有沒有變、標籤有沒有被唸出來、笑聲有沒有重複、名字發音。
要測 IPA 的話，在另一份音訊稿裡**直接取代**那個名字，不要再附加一次發音。結果寫具體觀察，不要寫「全部通過」。

## 3. 寫作與歷史場景
每個場景寫明日期、登場的人（全名）、相關的世界觀元素。寫過去的時間點時，參考 `sudowrite/scene-setup.md`
的狀態表，並在專案副本裡先拿掉之後才發生的事。

## 4. 更新與回報
之後的版本請照 `CHANGELOG.md` 逐欄更新既有卡片（保留你自己的修改）；不要假設重複匯入 CSV 會合併。
回報問題時附：版本號、哪張卡哪個欄位、測試結果、最小重現步驟。測試紀錄放在發佈資料夾外面。
