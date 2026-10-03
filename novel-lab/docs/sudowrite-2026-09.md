# Sudowrite 現況調查（2026-09-30）

> 來源以官方文件（docs.sudowrite.com，大多標示 2026 年 1 月更新）與官方 changelog
> （feedback.sudowrite.com，讀到 2026-09-28 的 190 則）為主，網址列在文末。
> 標 **未證實** 的是官方沒寫、或只有第三方說法的事。Reddit、YouTube 這次抓不到，沒有社群實測資料。

## 一、先講結論：這對我們的框架代表什麼

1. **角色和世界觀可以用 CSV 一次匯入，而且不經 AI 改寫。** 所以我們的成品直接輸出成
   Sudowrite 官方模板格式的 CSV，最省事、最不會走樣。
2. **Sudowrite 靠名字辨認「現在提到的是誰」。** 卡片的 Other Names（暱稱、稱謂、綽號）
   一定要寫齊，否則寫到「阿晚」時它不會帶入「林晚」的卡片。
3. **上下文不夠時，Worldbuilding 和 Characters 最先被擠掉。** 卡片要把最重要的資訊放前面，
   不要寫成長篇散文。但官方也說「越具體，AI 寫得越好」——具體而不冗長。
4. **角色卡要反映「目前寫到的時間點」。** 整條弧線放在我們的調查檔案裡，Sudowrite 卡片只放
   當下的狀態，寫到轉折後再更新。
5. **劇透用「隱藏」處理。** 每張卡、每個特質都有眼睛圖示，隱藏後所有 AI 功能都看不到。
   我們把秘密放在獨立的 `Secrets` 特質，匯入後隱藏，寫到揭露章節再打開。
6. **中文可以用，但要明說。** Write 會跟著你的語言；Draft 和外掛有時會跑回英文。
   官方建議在 Extra Instructions、外掛提示裡加「全部以某語言輸出」這類指令（要用那個語言寫）。
   我們的 Style 欄位最後固定加一句語言指令。

## 二、「一次寫很多字」實際上是什麼

你提到 Sudowrite 現在可以一次寫完很長的小說。查到的官方資料是：

- **Draft**（打字機圖示，以前叫 Chapter Generator，更早叫 Story Engine）是寫長文的主力：
  依照你給的 **Scenes**（逐條列出的場景）一次寫一整章。官方部落格（2026-08-06 更新）說
  一章大約 **3,000–5,000 字以上**。**沒有字數設定**，長度由場景條數決定。產生前會先估
  字數與點數，2026-08-14 起估計值的上限就是最高收費；中途可以暫停。
- **Write**：一次 1–6 張卡，每張約 50–1,500 字，或選 Max words（約 2,000 字）。
- **First Draft**：空白文件一次最多 3,000 字。**Rewrite**：最多 6,000 字。
- **Chat（開啟 Allow edits）**：可以建立、編輯文件，更新 Story Bible，執行你核准的多步驟計畫。
- 到 2026-09-28 為止，官方文件和 changelog 裡**找不到**「一鍵寫完整本書」的功能。
  有一則第三方搜尋摘要提到「Story Engine 3.0 全書生成」，官方沒有對應資料，視為**未證實**。

所以實務流程是：**Story Bible → Outline（分章摘要）→ 每章的 Scenes → Draft 一章一章寫**。
我們的框架負責把 Story Bible 做到最好；Outline 與 Scenes 之後可以加一個任務類型來做。

## 三、Story Bible 的七個區塊

| 區塊 | 作用 | 誰會讀它 |
|---|---|---|
| Braindump | 你手寫的「電梯簡報＋我知道的一切」，官方建議至少幾百字 | Synopsis |
| Genre | 你手寫；要寫主題，不要只寫標籤（「友情變愛情的浪漫喜劇」而不是「浪漫」） | Synopsis、Outline、Scenes、正文 |
| Style | 你手寫，或用 Match My Style 分析範文產生；短句描述文風 | Draft、Write 的正文 |
| Synopsis | 由 Braindump＋Genre 生成（用 Muse） | Characters、Worldbuilding、Outline、Scenes |
| Characters | 角色卡；可從 Synopsis 一次生成，或手動、或匯入 | Outline、Scenes、Draft、Write、Quick Edit、Chat |
| Worldbuilding | 世界觀卡；用模板（Setting、Item、Clue…）或自訂 | Outline、Scenes、正文 |
| Outline | 幕與分章摘要；POV／時態在這裡設定；「Start Chapter」會建立連結的文件 | Scenes 生成、Draft |

**流水線：** Braindump（＋Genre）→ Synopsis → Characters／Worldbuilding → Outline →
Scenes → Draft 寫正文。Style 不從別處生成，但影響所有正文。

### 角色卡
- 欄位：名字、Role（下拉選單，例：Protagonist、Supporting）、預設特質 **Pronouns、Groups、
  Other Names、Personality、Background、Physical Description、Dialogue Style**。
- 可以替單張卡加特質，也可以改所有卡的預設特質；2025-11-26 起每種 Role 可以有自己的特質模板。
- 每個特質都有 Generate／Rewrite，每張卡有版本紀錄。2026-09-25 起可以生成角色肖像
  （Appearance details 上限 2,500 字元，每張圖 5,000 點）。
- Role 下拉選單的完整選項官方沒列出（**未證實**）。

### 世界觀卡
- 欄位：名字、類型、各模板的特質、Other Names。官方只舉了 Setting、Item、Clue 三種模板當例子。
- 官方寫法建議：「如果一個資淺的作家或校對看得懂你的特質，AI 就處理得來。」

### Sudowrite 怎麼決定帶入哪些卡
- **Saliency Engine**：自動挑出相關的卡片與特質（外掛用 `{{characters}}` 時也是；用
  `{{characters_raw}}` 則全部帶入）。
- **Story Bible Detection**：在 Scenes 裡用底線標出認得的角色與元素。官方說 Draft 一直是
  靠「認得出來」才帶入卡片，建議用底線檢查錯字。→ **名字與 Other Names 一定要一致。**
- **隱藏（Visibility）**：眼睛圖示，卡片與單一特質都能隱藏，所有 AI 功能都看不到。
  官方沒有「永遠帶入」的開關。
- **上下文不夠時的丟棄順序**：Worldbuilding → Characters → 前一章 → 連結的大綱摘要 →
  Genre → Key Details → Tone → Style → 前文 → 選取的文字。

### GPT 審查時補充確認的官方細節（2026-09-30）
- Synopsis **空白**時，原本依賴它的功能會改讀 Braindump → 還沒定稿就讓 Synopsis 真的空著，不要貼提醒文字。
- `{{characters_raw}}`／`{{worldbuilding_raw}}` 會跳過相關性篩選，但**仍然不包含隱藏的內容** →
  外掛也拿不到被隱藏的 Secrets。
- 生成紀錄（History）上的 chiclets 可以看出這次實際用了哪些上下文 → 用 Scenes 底線確認有被認出來，
  生成後再用 chiclets 檢查需要的卡片有沒有被帶入。
- **卡片與特質預設全部可見**；CSV 匯入不帶隱藏設定 → Secrets 要在匯入後、第一次用 AI 前手動隱藏。
- 中文字數：Braindump／Synopsis 的 4,000 words 是官方上限，但**中文怎麼計數官方沒公布**；
  本框架「每個中文字算 1」只是保守估算。

## 四、字數上限

Sudowrite 以英文 word 計。中文怎麼算官方沒說，我們保守地把每個中文字當一個 word。

| 欄位 | 上限 | 來源 |
|---|---|---|
| Braindump | 4,000 words | changelog 2026-01-12 |
| Synopsis | 4,000 words | changelog 2025-12-22、2026-01-12 |
| Style Examples（範文） | 1,000 words，只用在 Draft | Muse 文件 |
| 角色卡數量 | 每個 Story Bible 最多 2,000 張，單一特質沒有公布上限 | Characters 文件 |
| 世界觀卡數量 | 最多 2,000 個 | CSV 模板 |
| Outline | 沒有字數上限，章數不限 | Outline 文件 |
| 角色／世界觀 AI 匯入（非 CSV） | 輸入 ≤ 60,000 words，每次 ≤ 30 項 | Import 文件 |
| 肖像 Appearance details | 2,500 字元 | Portraits 文件 |
| Genre、Style、Scenes、Extra Instructions | 官方沒公布（**未證實**） | — |

框架在 `framework/sudowrite-fields.json` 另外訂了「建議長度」（soft），超過只警告不擋。
中文內容超過官方上限時只顯示「本地估算可能超限、平台計數待確認」，不直接擋下。

## 五、匯入與匯出

- **角色 CSV**（Characters 標題旁 ••• → Import → CSV，不經 AI）：一列一個角色、一欄一個特質、
  第一列是欄名。官方模板欄位：
  `Name,Role,Pronouns,Groups,Other Names,Personality,Background,Physical Description,Dialogue Style,<自訂特質…>`
- **世界觀 CSV**（Worldbuilding 標題旁 ••• → Import → CSV）：
  `Name,Role,Other Names,Description,<自訂特質…>`（這裡的 Role 就是類型，例：Setting）
- **Outline**：••• → Import Outline，可貼文字或上傳檔案；CSV 是兩欄（左欄章名、右欄內容），
  官方說這樣匯入不會被 AI 改動。
- **Braindump、Genre、Style、Synopsis** 沒有匯入功能，只能貼上（或請 Chat 幫你填）。
- **重複匯入會不會合併同名卡片，官方沒寫**（未證實）。更新既有卡片請逐欄貼上。
- **Import Novel**：匯入既有小說（建議 12 萬字以內），自動建立 Story Bible 與 5–7 個主要角色。
- **匯出**：專案可匯出 .zip 或合併成一份 .docx，但**不含 Story Bible**；Outline、Characters、
  Worldbuilding 可以各自匯出成 CSV。→ **我們的 repo 就是你的 Story Bible 備份。**
- **Series 資料夾**：同一系列的書共用 Characters 與 Worldbuilding（改一處全部同步）。

## 六、模型與成人內容（照官方說法整理）

- **Muse**（Muse 1.5）：Draft 和 Write 的預設，也負責 Expand 與 Synopsis。官方說它
  「什麼都會寫、沒有過濾」，是站上最不設限的模型。
- **Excellent** = Sudowrite 自家的 **Ballad 1.1**（2026-06-02 起，取代 Claude 3.7 Sonnet）；
  官方形容「非常寬鬆」。Rewrite 在 2026-09-22 改用 Ballad。
- **實驗模型**（Write、Draft、外掛都能選）：Claude（Opus 4.6–5.5、Sonnet 4.6–5.5、Fable 5.1）、
  GPT（5.4、5.6 系列、GPT-6 Astra／Sol／Luna）、Gemini、Kimi、GLM、Qwen、Grok 等。
  官方說 Claude 系列「中等」、OpenAI 系列「嚴格」、Grok「寬鬆」。
- **沒有「成人內容開關」。** 用模型選擇、Key Details（寫明尺度）、Extra Instructions、
  Tone Shift（Sensual／Romantic）來控制。
- 服務條款禁止涉及未成年人的性內容、違法用途等。外掛的標題與說明要維持 PG-13。

→ 框架裡標了【Sudowrite 處理】的部分，建議在 Sudowrite 用 **Muse 或 Excellent（Ballad）** 寫。

## 七、其他功能

- **Style 工具**：Match My Style 從範文產生 Style 描述；Style Examples 最多 1,000 字範文
  （格式 `Example 1: "…"`，全帳號共用，只用在 Draft）；Style Guide 2026-06-30 起搶先體驗（細節未證實）；
  My Voice（自訓模型）已停止開發。
- **外掛（Plugins）**：社群外掛上千個，可以選任何模型，能用 `{{braindump}}`、`{{characters}}`、
  `{{worldbuilding}}`、`{{outline}}` 等變數讀 Story Bible。
- **Canvas**：白板，有 Hero's Journey、Hollywood Beats、Story Circle、Romance 等大綱模板，可以生成大綱再複製出來。
- **方案**（2026-09 定價頁）：Hobby & Student 225,000 點／月（年繳 $10、月繳 $19）、
  Professional 1,000,000 點（$22／$29）、Max 2,000,000 點、可累積 12 個月（$44／$59）。
  不同模型耗點差很多：官方範例 200 字，GPT-5 Nano 約 70 點，Claude 4.1 Opus 超過 8,000 點。

## 八、官方的寫卡建議

- 具體、一致、清楚；刪掉過時或互相矛盾的內容。
- 卡片要反映目前寫到的時間點。
- Scenes 裡要把事情講明白：寫「Suzie 知道他殺了鄰居的狗並把牠埋了」，不要寫「他做的事」。
- 暱稱與團體寫在 Other Names、Groups，並用 Scenes 的底線確認有被認出來。
- Genre 要寫主題；Style 用短句描述（例：「冷峻、陰森，短句，充滿威脅感的對白」），每章前可以調整。
- 視角與時態用 POV/Tense 選單設定，不要只寫在 Style（Style 裡重複一句給外掛看即可）。
- 一個 Scene 只寫一個轉折，「寫變化，不寫氣氛」；語氣放在 Extra Instructions。
- 劇透（例如兇手的動機）先隱藏；系列作可以每本書一張卡，視需要顯示或隱藏。
- 「特質寫成具體行為」「用現在式」是我們框架的做法，**不是**官方建議。

## 工作流程接點（2026-10-02 查核，W1）

這個套件支援的交接是：CSV／逐欄貼上進 Sudowrite，然後把要配音的場景存成 UTF-8 場景腳本，交給離線轉換器
`tools/scene_to_elevenlabs.py`。沒有找到公開的 Sudowrite API（這是沒找到，不是確定沒有）；不要假設 Sudowrite 和
ElevenLabs 會直接串接，也不要假設 Rewrite、Describe 這些改寫工具會保留腳本格式（改寫後要再跑一次 `--lint-only`）。
每次生成實際用了哪個模型要記下來。官方 CSV 範本下載檔和目前完整的實驗模型清單這次沒有重新查到。

## 來源

- Story Bible 各區塊：[Braindump](https://docs.sudowrite.com/using-sudowrite/1ow1qkGqof9rtcyGnrWUBS/braindump/bgfrku4qGdfbiFH3ar9PE2)、
  [Genre](https://docs.sudowrite.com/using-sudowrite/1ow1qkGqof9rtcyGnrWUBS/genre/hCJPQqQYtUQm7ntdcRFJHg)、
  [Style](https://docs.sudowrite.com/using-sudowrite/1ow1qkGqof9rtcyGnrWUBS/style/4gqKgVVjdN6XTKo71HChqV)、
  [Synopsis](https://docs.sudowrite.com/using-sudowrite/1ow1qkGqof9rtcyGnrWUBS/synopsis/r4GGUdR23VKcK2WrQVdheb)、
  [Characters](https://docs.sudowrite.com/using-sudowrite/1ow1qkGqof9rtcyGnrWUBS/characters/a7tdE1ZB8KvAwMD3Mopwpd)、
  [Worldbuilding](https://docs.sudowrite.com/using-sudowrite/1ow1qkGqof9rtcyGnrWUBS/worldbuilding/uc5NfWSz4x8Wm3S19LZeo8)、
  [Outline](https://docs.sudowrite.com/using-sudowrite/1ow1qkGqof9rtcyGnrWUBS/outline/3owKyHXUm1bCdp41b2Npjk)、
  [What is Story Bible](https://docs.sudowrite.com/using-sudowrite/1ow1qkGqof9rtcyGnrWUBS/what-is-story-bible/jmWepHcQdJetNrE991fjJC)
- 帶入機制：[Saliency Engine](https://docs.sudowrite.com/using-sudowrite/1ow1qkGqof9rtcyGnrWUBS/saliency-engine/4KL8gFeLZNvk8CEeXpfwB2)、
  [Visibility](https://docs.sudowrite.com/using-sudowrite/1ow1qkGqof9rtcyGnrWUBS/visibility-settings/4KL8gFeLZP6ep8keUhKVGp)、
  [Chapter Continuity](https://docs.sudowrite.com/using-sudowrite/1ow1qkGqof9rtcyGnrWUBS/chapter-continuity/4KL8gFeLZQ6GSBjDWtSbV6)、
  [Story Bible Detection](https://feedback.sudowrite.com/changelog/mag-story-bible-detection-and-visibility-update)
- 寫作功能：[Scenes & Draft](https://docs.sudowrite.com/using-sudowrite/1ow1qkGqof9rtcyGnrWUBS/scenes--draft/49p5MTVxTKkVFEC5rVUzpY)、
  [Write](https://docs.sudowrite.com/using-sudowrite/1ow1qkGqof9rtcyGnrWUBS/write/pvxUvbQqYybfEosqx1sXjY)、
  [First Draft](https://docs.sudowrite.com/using-sudowrite/1ow1qkGqof9rtcyGnrWUBS/first-draft/gMcJCRTRFqB8w3hBWYAC5M)、
  [Chat](https://docs.sudowrite.com/using-sudowrite/1ow1qkGqof9rtcyGnrWUBS/chat/5vbuELXf6LZQnGfVzsEXCV)、
  [官方部落格：Scenes/Beats](https://www.sudowrite.com/blog/your-outline-sucks-heres-how-to-use-sudowrite-beats-to-fix-it/)、
  [Draft 估算](https://feedback.sudowrite.com/changelog/improved-draft-estimates-plus-a-bunch-of-fixes)、
  [Write Max words](https://feedback.sudowrite.com/changelog/new-to-write-max-words)
- 上限與改版：[Simplified Story Bible](https://feedback.sudowrite.com/changelog/simplified-story-bible)、
  [Three big improvements](https://feedback.sudowrite.com/changelog/three-big-improvements)、
  [Larger synopsis](https://feedback.sudowrite.com/changelog/text-highlighting-and-larger-synopsis)、
  [Role-based templates](https://feedback.sudowrite.com/changelog/new-role-based-character-templates)
- 模型與內容政策：[Muse](https://docs.sudowrite.com/using-sudowrite/1ow1qkGqof9rtcyGnrWUBS/sudowrite-muse/4k9bFDMSyic6mFPkYFHrkZ)、
  [Which AI model](https://docs.sudowrite.com/using-sudowrite/1ow1qkGqof9rtcyGnrWUBS/which-ai-model-should-i-use/veMq9xRH6KLCQPFm5XkQx7)、
  [Prose modes](https://docs.sudowrite.com/using-sudowrite/1ow1qkGqof9rtcyGnrWUBS/prose-modes--models/2X5FuivhsbwUiMNym5eUqm)、
  [Ballad 1.1](https://feedback.sudowrite.com/changelog/even-more-excellent-prose)、
  [服務條款](https://docs.sudowrite.com/legal-stuff/h8ppDEnJAwytH3jhJKu6c1/terms-and-conditions/sMnXucDXEq8wBDjjsQq37A)
- 匯入匯出：[Importing](https://docs.sudowrite.com/using-sudowrite/1ow1qkGqof9rtcyGnrWUBS/importing-files/rbGUgrZM6tNuXFG1hjDFyS)、
  [Exporting](https://docs.sudowrite.com/using-sudowrite/1ow1qkGqof9rtcyGnrWUBS/exporting-files/3NtVWXcnwYaRCmPW2iwcCB)、
  [Series](https://docs.sudowrite.com/using-sudowrite/1ow1qkGqof9rtcyGnrWUBS/series-support/3vfbZPCB1ANLm75FXmJf28)、
  [角色 CSV 模板](https://editor.sudowrite.com/assets/sudowrite-characters-import-template.csv)、
  [世界觀 CSV 模板](https://editor.sudowrite.com/assets/sudowrite-worldbuilding-import-template.csv)
- 語言：[Can I use Sudowrite in other languages?](https://docs.sudowrite.com/resources/ktuxRrzphwp3uTNneRtaos/can-i-use-sudowrite-in-other-languages/aR5Me5vw2J3wmLD9acqrvw)
- 方案：[Plans](https://docs.sudowrite.com/plans--account/wBnmhtSyMcWtk2BLzifGkz/what-plans-are-available/mwfVvj2rGcKYs1BQy4Pdcb)、
  [Pricing](https://sudowrite.com/pricing)
- 其他：[Tips & Tricks](https://docs.sudowrite.com/using-sudowrite/1ow1qkGqof9rtcyGnrWUBS/tips--tricks/eBjBne7foMi8uYFxWEPCai)、
  [POV/Tense](https://docs.sudowrite.com/using-sudowrite/1ow1qkGqof9rtcyGnrWUBS/setting-pov-and-tense/5gKBNzBQLB7C8yuBhHQ983)、
  [Canvas](https://docs.sudowrite.com/using-sudowrite/1ow1qkGqof9rtcyGnrWUBS/canvas/pQGLNzeYo1kLhGo14rdBy6)、
  [Plugins](https://docs.sudowrite.com/using-sudowrite/1ow1qkGqof9rtcyGnrWUBS/how-do-i-build-plugins/a3iVxJb4UZLKfSxf8BG3mY)、
  [Portraits](https://docs.sudowrite.com/using-sudowrite/1ow1qkGqof9rtcyGnrWUBS/portraits/8FB59VFrbbhcmBRYNicXis)
