# 從這裡開始 — holoen {rev}{draft}

這是給作者的使用指南：資料在哪裡、每個檔案放進 Sudowrite 的哪一格、寫作時怎麼用、怎麼交給 ElevenLabs 配音、
之後怎麼更新。基準日 {baseline}；這一版有 **{nchar} 張角色卡**、**{nworld} 張世界觀卡**、{nchar} 份 ElevenLabs 表演表，
全部是完整卡（沒有精簡版）。檢查結果在 `validation.json`；**實際匯入和配音只有你能測（runtime untested）**，
請先做第 3 節的十分鐘測試。
{pending}
## 1. 資料在哪裡拿

- 位置：GitHub repo `ag8ai65566/ag8ai65566`，分支 `claude/sudowrite-novel-framework-2cmja7`，資料夾
  `novel-lab/projects/holoen/delivery/holoen-2026-09-30-{rev}…/`（資料夾名稱就是版本號；`-draft` 結尾的是草稿）。
- 下載整包：GitHub 網頁切到這個分支 → 綠色 **Code** 按鈕 → **Download ZIP**，解壓後進到上面的資料夾。
  只要單一檔案：打開檔案 → 右上角 **Download raw file**。
- 只拿發佈資料夾（`delivery/…`）裡的東西：它有版本號、檢查結果和每個檔案的雜湊。`export/` 是工作中的最新輸出，
  隨時會變，不要直接拿來匯入。

## 2. 這包裡有什麼、各自放哪裡

| 檔案 | 放到哪裡 | 怎麼放 |
|---|---|---|
| `sudowrite/characters.csv` | Story Bible → **Characters** | 標題旁 `•••` → Import → CSV（整包角色，一次） |
| `sudowrite/worldbuilding.csv` | Story Bible → **Worldbuilding** | 標題旁 `•••` → Import → CSV（整包世界觀，一次） |
| `sudowrite/cards/characters-<名字>.csv`、`worldbuilding-<名字>.csv` | 同上 | **只加一張新卡**時用（例如之後的新成員） |
| `sudowrite/style.txt` | Story Bible → **Style** | 整段貼上；後面可以接一兩句你自己的文風（合計約 120 字內） |
| `sudowrite/paste.md` | （不匯入）| 每張卡逐欄的內容，**更新既有卡片時逐欄複製貼上**用 |
| `sudowrite/scene-setup.md` | （不匯入）| 寫過去時間點的場景時，查每個人當時的狀態 |
| `performance/sheets/<名字>.md` | ElevenLabs | 每個角色的原創聲音設計、設定值、標籤表（第 6 節） |
| `performance/pronunciation.tsv` | ElevenLabs | 名字與專有名詞的 IPA（暫定，要先測） |
| `performance/voice-map.example.json` | 你自己的紀錄 | 填你做好的原創聲音 voice_id |
| `performance/test-results.csv` | 你自己的紀錄 | 寫測試結果（第 3、6 節） |
| `reference/bible/…` | （不匯入）| 每張卡上面的完整研究檔：來源、時間線、關係表、合併紀錄。想查「這句話哪裡來」時看 |
| `CHANGELOG.md`、`01-INDEX.md`、`manifest.json` | （不匯入）| 這版改了哪些欄位、卡片索引、檔案雜湊 |

角色卡的欄位：`Name, Role, Pronouns, Groups, Other Names, Personality, Background, Physical Description,
Dialogue Style`（Sudowrite 預設），加上自訂特質 `Catchphrases, Voice & Delivery, Audio Tags, Motivation,
Relationships, Secrets`。每個角色的 Role 都是 Protagonist。`Secrets` 這一版全空。

## 3. 第一次：先在測試專案做十分鐘匯入測試

1. 新建專案 `holoen-{rev}-smoke`（可丟棄）。不要在你正在寫的專案裡測匯入。
2. Characters 匯入 `sudowrite/characters.csv`，確認 **{nchar} 張**；Worldbuilding 匯入 `sudowrite/worldbuilding.csv`，
   確認 **{nworld} 個**。每個合併 CSV 只匯入一次。
3. 打開 Fuwawa、Mococo 和另一個角色：雙胞胎是兩張卡、`Role` 是 Protagonist、自訂特質（含 `Audio Tags`）有內容。
   找一個多行或有標點的欄位，和 `sudowrite/paste.md` 對照。打開 FUWAMOCO 和一張 History 卡。
4. 把 `sudowrite/style.txt` 貼到 Style。Genre 填 `Light comic fantasy`，Braindump 填
   `Fuwawa Abyssgard and Mococo Abyssgard compare a map inside a fictional game.`，Synopsis 留白；
   視角設第三人稱、時態過去式。
5. 新建一個章節，Scenes 寫：`Scene date: 2026-09-30. Fuwawa Abyssgard and Mococo Abyssgard, the members of
   FUWAMOCO, compare a map inside a fictional game. Keep their speaking turns distinct.`
6. 看兩人和 FUWAMOCO 有沒有出現**偵測底線**（Sudowrite 認得這張卡的記號）。
7. 生成最短的一段，檢查：說話的人分得開、對白裡有 `[...]` 表演標籤、敘述沒有標籤。生成後在 History 的
   小標籤（chiclets）看這次實際帶入了哪些卡。
8. 結果寫進 `performance/test-results.csv`（版本 {rev}、用的模型）。測試專案先留著，有問題方便排查。

## 4. 正式開寫：你的專案怎麼設定

| Story Bible 區塊 | 填什麼 |
|---|---|
| **Braindump** | 你這篇故事的點子與你知道的一切（官方建議幾百字以上）。**不要**把角色卡內容貼進來：卡片已經在 Characters，重複只會佔上下文。 |
| **Genre** | 寫主題，不只寫標籤：例「成員之間的日常喜劇，帶一點溫馨」，而不是只寫「喜劇」。 |
| **Style** | 先貼 `style.txt`（教 Sudowrite 在對白裡寫 ElevenLabs 標籤），再接一兩句你的文風。不需要配音時可以不貼。 |
| **Synopsis** | 由 Braindump＋Genre 生成，或先留空（留空時 Sudowrite 會改讀 Braindump；不要貼提醒文字）。 |
| **Characters / Worldbuilding** | 用 CSV 匯入（第 2 節）。故事用不到的卡可以按眼睛圖示隱藏，減少干擾。 |
| **Outline** | 你的分章大綱；視角與時態用 POV/Tense 選單設定，不要只寫在 Style。 |

- 模型：正文用 **Muse** 或 **Excellent（Ballad）**；這兩個最不設限，標籤也寫得穩。我們的卡片只寫公開人設、
  不寫露骨內容；要寫成人向內容由 Sudowrite 處理（用模型選擇、Key Details、Extra Instructions 控制尺度）。
- 寫中文正文：在 Extra Instructions 寫「全部以繁體中文輸出；方括號裡的表演標籤保留英文」。卡片內容是英文，
  不用翻譯。

## 5. 寫作時：怎麼讓 Sudowrite 帶入對的卡

- **每個場景寫明三件事**：場景日期（例 `Scene date: 2026-10-05.`）、登場成員的**全名**（第一次出現時）、
  相關的世界觀名稱（例 FUWAMOCO、BaeRyS、Serendipity、TakaMori）。看偵測底線確認有被認出來。
- **人數**：上下文不夠時，Sudowrite 最先丟掉世界觀卡，再來是角色卡。一個場景以 2–5 位會說話的成員最穩；
  大合照場景（演唱會、全員合作）把重點放在幾位說話的人，其他人一句帶過。
- **暱稱**：卡片的 Other Names 已收錄常用稱呼（例 Bae、Gura、Biboo、Moom），內文可以直接用；但新場景第一次
  出現時仍建議用全名。
- **時間點**：卡片描述的是 {baseline} 的狀態（例：Gura、Fauna、Mumei 已畢業，只以回憶出現；Ame 是 affiliate，
  可以客串）。寫更早的時間點時，查 `sudowrite/scene-setup.md` 的狀態表，在場景裡寫明當時的狀態；
  必要時在**專案副本**裡隱藏之後才發生的特質。
- **關係與梗**：Relationships 欄只寫公開的合作與梗；BaeRyS 的「結婚／離婚」、TakaMori 的「夫妻」這類都是
  表演出來的梗，不是真實戀愛。卡片刻意不寫背後的真人與私生活，寫作時也請比照。
- 生成後用 History 的 chiclets 檢查：該出現的卡有沒有被帶入。

## 6. 配音：交給 ElevenLabs v4

1. **做原創聲音**：每個角色在 Voice Design 貼上表演表第 1 節的描述，生成幾個預覽，挑最符合「音域和能量」的，
   存成 `holoen-<名字>`。**不要用直播或歌聲做 clone，也不要刻意做像本人的聲音**（ElevenLabs 政策與 COVER
   二次創作規範都禁止）。旁白另外做一個中性聲音。voice_id 記在 `voice-map.example.json`。
2. **設定**：表演表第 2 節（UI 用百分比，例 Stability 40%、Similarity 75%；API 用小數）；模型選 `eleven_v4`。
3. **貼稿**：從 Sudowrite 複製帶標籤的對白。多人對話用 **Text to Dialogue**（每一輪指定那個角色的聲音，
   一次 2,000 字元以內）；長段旁白用 Text to Speech 或 Studio，旁白不加標籤。同一場景盡量一次生成，讓 v4 讀到上下文。
4. **發音**：`pronunciation.tsv` 的 IPA 是暫定的；要測時，在另一份稿裡**直接把名字換成 IPA**，不要同時寫名字又寫 IPA。
5. **三行測試**（先做一次）：用兩個你自己的原創聲音 A/B/A 輪流（以下是風格示範，不是引用）：
   ```text
   A: [calm] We can check the map again.
   B: [startled] Ah! That door moved.
   A: [laughs] Fuwawa, Mococo—your turn.
   ```
   聽：聲音分配對不對、語氣有沒有變、標籤有沒有被唸出來、笑聲有沒有重複、名字發音。結果寫具體觀察，
   記在 `test-results.csv`。
6. 太平淡就把 Stability 往下調、標籤寫具體一點；太誇張就往上調、減少標籤。表演表第 7 節是「不要這樣演」。

## 7. 之後的版本怎麼更新

- 每個新版本是一個新的資料夾（`r02`、`r03`…）。先看 `CHANGELOG.md`：哪張卡、哪個欄位改了。
- **既有卡片：逐欄貼上**（從 `paste.md` 複製），保留你自己改過的地方。**不要重複匯入整包 CSV**：
  Sudowrite 沒說會不會合併同名卡片，可能變成兩張。
- **新增的卡**（例如之後的新成員）：只匯入 `sudowrite/cards/` 裡那一張的 CSV。
- 表演表有改動時，`performance/sheets/` 會一起更新；聲音不用重做，只要更新標籤習慣與設定。

## 8. 常見問題

- **卡片沒被帶入**：檢查名字拼法（例 Ina'nis 的撇號）、有沒有出現偵測底線、卡片是不是被隱藏了。
- **出現重複的卡**：刪掉多的那張，之後更新改用逐欄貼上。
- **標籤被唸出來或重複**：在 Style 後面加一句「每段對白最多三個標籤」，或在 ElevenLabs 那邊刪掉多餘的標籤再生成。
- **口音或語氣不對**：口音只當聲音特徵寫在卡上；調表演表的 Voice Design 描述和標籤，不要改成模仿本人。
- **回報問題**：附上版本號、哪張卡哪個欄位、測試結果、最小重現步驟。測試紀錄放在發佈資料夾外面。
