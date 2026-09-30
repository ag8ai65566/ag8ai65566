AGREE-WITH-CHANGES

必改如下。產品事實查核日為 **2026-09-30**；我已讀取框架與 `tools/lab.py`，並查核相關官方文件。未修改檔案、未讀取 `projects/*/runs/`，也未實際操作 Sudowrite 帳號。

1. **[shared-rules.md](/home/user/ag8ai65566/novel-lab/framework/prompts/shared-rules.md)、[dossier-character.md](/home/user/ag8ai65566/novel-lab/framework/templates/dossier-character.md)、rubric.md → 原創角色的塑造方法，會逼既有人設補出不存在的心理設定 → 區分事實、觀察與創作。**

   「傷口、相信的謊言、未意識到的需要、破戒、完整弧線」適合部分原創角色，不宜要求每位公開人設都填滿。「每個設定都必須造成麻煩，否則刪掉」也會刪除聲音辨識需要的平常習慣。

   建議替換為：

   > 原創設定可設計動機、傷口與弧線。既有角色與公開人設須區分「官方設定」「公開言行觀察」「作者核准的同人改編」「未證實」；不得為填滿模板而推測隱藏心理。設定只要有助於辨識角色、維持連續性、建立生活感或產生場景，即可保留。

   「無此設定」「沒有找到證據」「不適用」也要分開；三者不是同一件事。未證實內容留在調查區，不以確定語氣進入 `[SW]`。評分表的「原創性」在忠實重建人設時應允許不適用，不能獎勵擅自改造原作。

2. **[gpt-brief.md](/home/user/ag8ai65566/novel-lab/framework/prompts/gpt-brief.md)、shared-rules.md → 通用規則混入 holoen 專案限定，且部分格式要求互相衝突 → 拆出專案規則並明定例外。**

   `ask_gpt()` 每次都附上含 holoen 設定的通用說明；未來別的小說也會收到「全英文、全部 Protagonist、不分時期」的指示。這些內容應只由目前專案的 `project.md` 注入。

   卡片寫法改成：

   > 描述性文字以第三人稱、當前狀態為主；歷史事件使用正確時態。逐字引用與示範台詞保留其自然人稱、時態和原文。Genre、Style 等控制欄位可使用寫作指令。機器辨識的 `[SW]` 欄名固定不翻譯。

   另外，「年齡、住址、職稱不能改」應改為「變更必須符合時間線並有紀錄」。holoen 的「不分時期」保留：早期與近期梗共同存在；來源仍記錄日期，但不把早期梗排除或標成只能在早期使用。

3. **gpt-brief.md、兩份卡片模板、README.md、[sudowrite-fields.json](/home/user/ag8ai65566/novel-lab/framework/sudowrite-fields.json) → 把預期隱藏寫成自動隱藏，容易直接洩漏秘密 → 修正操作承諾與資訊分層。**

   官方明確說卡片與特質**預設全部可見**；目前程式的 `hide_in_sudowrite` 只產生提醒，沒有設定平台可見性。所有「匯入後會被隱藏」「預設隱藏」統一改為：

   > 匯入後、首次使用 AI 功能前，由作者手動隱藏 Secrets，並確認眼睛圖示狀態。CSV 不承諾攜帶隱藏設定。

   隱藏代表 AI 看不到該資訊，不能期待它仍依秘密安排動機與伏筆。調查區應分開記錄「真相」「各角色知道什麼」「讀者已知什麼」「目前可描寫的表面行為／線索」；只把當下允許使用的線索送入可見欄位。同時檢查 Synopsis、Outline、Background 等位置是否另有秘密副本。[官方 Visibility 說明](https://docs.sudowrite.com/using-sudowrite/1ow1qkGqof9rtcyGnrWUBS/visibility-settings/4KL8gFeLZP6ep8keUhKVGp)

4. **[dossier-idea.md](/home/user/ag8ai65566/novel-lab/framework/templates/dossier-idea.md)、README.md → Synopsis 可交給 Sudowrite 生成，卻沒有回到雙方審核的步驟 → 補上設定回收流程。**

   Synopsis 會影響後續角色、世界觀、大綱與 Scenes；其中的新增人物、因果或結局都可能成為新設定。[官方 Synopsis 說明](https://docs.sudowrite.com/using-sudowrite/1ow1qkGqof9rtcyGnrWUBS/synopsis/r4GGUdR23VKcK2WrQVdheb)

   改成：

   > Synopsis 可由雙方共同定稿，或先由 Sudowrite 生成候選稿。生成稿須經 Claude 與 GPT 核對新增設定及因果後，才成為正式依據。

   三個方向中，只有採用方向進入 `[SW]`；其他方向留在調查區。專案有多份 idea 檔時，也要指定目前採用的版本，不能把多套 Braindump／Genre／Style 同時當成有效設定。

5. **sudowrite-fields.json、docs/sudowrite-2026-09.md、[lab.py](/home/user/ag8ai65566/novel-lab/tools/lab.py:395) → 本地字數估算被當成平台實際計數 → 分開標示官方上限與本地預算。**

   Braindump／Synopsis 的 **4,000 words** 可以確認；「每個中文字算一 word」則是框架自己的保守算法，不是 Sudowrite 規格。[官方上限更新](https://feedback.sudowrite.com/en/changelog/three-big-improvements)

   建議分開保存 `platform_limit`、`platform_unit`、`local_count_method`、`local_budget`。中文超出本地預算時顯示「超出本地保守估算，平台計數待確認」，不要直接宣稱「超過官方上限」。也不要用這個 word 估算值推導模型 token 或上下文占用。

6. **[lab.py：bible_context／build_prompt](/home/user/ag8ai65566/novel-lab/tools/lab.py:116) → 依檔名串接後截取前 24,000 字元，會漏掉相關設定，也無法保證兩邊收到相同版本 → 建立本次任務的固定資料包。**

   目前可能截斷半張卡，並讓排序較後的世界觀永遠不進提示。API／人工轉貼也不能可靠地靠「請到檔案裡查」補回。

   改成完整附上：專案規則、相關角色／世界觀、必要連續性、適用模板及欄位上限；列出採用的檔案與版本。超量時選取完整段落並明列未附資料。兩份盲稿使用相同資料包，各自查到的新證據在互審時再交換。

7. **[lab.py：verdict／promote](/home/user/ag8ai65566/novel-lab/tools/lab.py:412)、gpt-verify.md → 核准沒有綁定受審版本，且判定過寬 → 讓驗收真正成為收錄門檻。**

   現在以 `startswith("APPROVE")` 判定，`APPROVED` 等不合規字串也會通過；`final.md` 在核准後被修改，舊核准仍可用。

   改法：第一行精確比對 `APPROVE`／`CHANGES`；核准記錄綁定 `final.md` 的雜湊，收錄前重新核對；檢查約定的盲稿、互審與合併紀錄齊備。保留作者裁決途徑，但 `--force` 必須記錄裁決理由，不能記成 GPT 核准。

8. **[lab.py：sw_fields／export](/home/user/ag8ai65566/novel-lab/tools/lab.py:383) → 匯出尚未驗證資料完整性，可能悄悄覆蓋欄位或留下舊成品 → 驗證完成後才發布匯出結果。**

   記憶體內檢查確認：重複兩個 `[SW] Name` 時，前者會被後者無聲覆蓋；英文 `None` 也不會像中文「（無）」一樣轉成空白。程式另會先寫出成品，才因超出硬上限報錯；刪除卡片後，舊匯出檔也可能殘留。

   改法：檢查重複欄位、必要欄位、未填佔位文字、名稱一致性與空值標記；先完成驗證，再更新匯出目錄，並移除不再屬於當次匯出的舊檔。自訂欄位可保留，但拼錯欄名應提示確認。

建議如下。

1. **README.md、協作提示與 rubric.md → 完整流程值得保留，但不必把每次呼叫都用在重寫同樣的內容 → 依任務調整工作量。**

   **新角色、新世界規則、重要劇情方向採三次 GPT 呼叫，我認為合理。** 盲寫提供不同解法，互審找錯，驗收檢查合併損失；價值來自三個不同職責。兩邊都看過相同來源，仍可能一起出錯，因此共識不能取代證據。

   我建議：

   - 新設定與重大修改維持完整流程，先保留作者指定的 `xhigh`。
   - 小幅更新採雙方審查變更內容，沿用既有合格段落。
   - 字數、CSV、欄位齊全度由程式先檢查，模型集中處理聲音、因果與事實。
   - 若日後比較成本，可試驗驗收使用 `high`，以漏錯率與返工量決定是否保留。

   成本不能只看「三次」：長提示、兩份初稿、推理用量、搜尋與重試都要記錄。批次合併呼叫也不保證降低總 token。建議追蹤「每張合格卡的實際用量、耗時、返工次數」。

   分工方面，我可以負責考據衝突裁決表、連續性整理及聲音欄位的候選合併稿，Claude 組裝正式版，我再驗收。若整份改由 GPT 合併，應交換驗收者，讓 Claude 負責獨立驗收。

2. **dossier-character.md、sudowrite-fields.json → 欄位選擇大致正確，欠缺的是責任分配 → 保留核心欄位，避免內容重複。**

   「預設七個特質＋Motivation、Relationships、Secrets」合理；holoen 再加 `Catchphrases` 與 `Voice & Delivery` 也有充分理由。加上 Name、Role，現行模板共 **14 欄**。

   `character_columns` 只有九個基礎欄位不代表其他欄位會丟失：我查過 `write_csv()`，它會追加自訂欄位；這部分設計正確。

   | 欄位 | 建議專責內容 |
   |---|---|
   | Personality | 遇到壓力、反駁、失敗時如何選擇和行動 |
   | Motivation | 目前目標、利害與優先順序 |
   | Dialogue Style | 句法、措辭、回應方式、不同對象前的語氣 |
   | Catchphrases | 有來源的固定短句及觸發情境 |
   | Voice & Delivery | 停頓、重音、笑聲、速度與情緒變化 |
   | Relationships | 對特定人的期待、互動方式與張力 |
   | Secrets | 需要控制可見性的真相 |

   調查區再補「能力與限制」「當前處境」「知道／誤信什麼」即可，不必全部新增成 CSV 欄位。聲音檔案則補「常見、偶發、特定互動才出現」與來源時間碼，防止 AI 每句都塞招牌梗。

   `Other Names` 應收錄能辨認角色的別名；泛用稱呼與誰怎麼叫誰，放在關係／聲音資料。官方也說 `Groups` 有助於以團體名稱辨認相關成員，值得實際利用。[官方 Characters 說明](https://docs.sudowrite.com/using-sudowrite/1ow1qkGqof9rtcyGnrWUBS/characters/a7tdE1ZB8KvAwMD3Mopwpd)

3. **[dossier-world.md](/home/user/ag8ai65566/novel-lab/framework/templates/dossier-world.md) → 單一模板涵蓋太多類型，且缺少來源欄 → 加共同骨架與類型專用問題。**

   共通必填保留名稱、用途、限制、角色連結、連續性與來源；其他依類型選用：地點重交通與進出條件，勢力重權限與執行方式，魔法／科技重啟動條件、代價及失效方式，線索重取得方法、可支持的推論與誤讀。

   感官五項不必全部填；制度和歷史事件未必需要氣味。`Sensory Details` 改為「依場景選用的細節」，避免每次重複全套描寫。

   最值得補的是一個「正常運作例」與一個「邊界例」：例如能力能開普通門，遇到活體封印會失敗，失敗後消耗仍不退還。這比抽象的「能力有限」更能約束正文。

4. **dossier-idea.md → 三方向與故事骨架有用，但差異與選擇標準不夠明確 → 比較故事運作方式。**

   A／B／C 至少在主角目標、阻力來源、敘事形式、結局代價其中兩項有實質差異。新增「篇幅／單篇或系列」「讀者期待的主要體驗」「主角反覆遭遇的選擇」「不可改條件」。

   推薦方向應說明符合哪些作者條件；混合方向時指出保留哪條核心因果。最低點、中點等節點可依篇幅省略，短篇和日常同人不必強塞完整長篇結構。

5. **sudowrite-fields.json、project.md → 單欄 soft limits 可作寬鬆上限，全欄接近上限則容易膨脹 → 增加使用情境與全卡總量提示。**

   現有角色描述欄加總為 **2,650 words**，隱藏 Secrets 後仍約 **2,400 words**；世界觀相應為 **1,250／1,000 words**。這不代表每次全部進入上下文，但不能只檢查各欄是否合格。

   以下是建議起始範圍，**不是平台限制，也不是已驗證的最佳值**：

   | 欄位 | 一般小說卡 | holoen 完整聲音卡 |
   |---|---:|---:|
   | Personality | 150–250 | 250–400 |
   | Background | 150–300 | 250–500 |
   | Physical Description | 80–150 | 100–200 |
   | Dialogue Style | 120–220 | 180–250 |
   | Catchphrases | 有需要才填，40–120 | 150–250 |
   | Voice & Delivery | 有需要才填，60–120 | 180–250 |
   | Motivation | 60–120 | 只填有依據內容，最多 200 |
   | Relationships | 120–250 | 250–350 |
   | Secrets | 按需要，最多 250 | 按需要，最多 250 |
   | World Description | 150–300 | 同一般設定 |
   | Rules | 150–350 | 同一般設定 |
   | Sensory Details | 60–120 | 同一般設定 |

   Genre 通常 20–50 words、Style 約 40–100 words 即可，现有 80／120 可留作提醒上限。一般角色可先以可見內容 800–1,400 words 為目標；holoen 保留完整優先，不因總量提示自動刪除有來源的內容。

   先前置最重要資訊仍有價值，但官方只公布上下文類別的捨棄順序，沒有保證卡片前段一定保留。因此另產生短版「本場景不可寫錯的事項」，比單靠前置更可靠。[官方 Chapter Continuity 說明](https://docs.sudowrite.com/using-sudowrite/1ow1qkGqof9rtcyGnrWUBS/chapter-continuity/4KL8gFeLZQ6GSBjDWtSbV6)

6. **docs/sudowrite-2026-09.md、README.md → 調查方向正確，還有幾個影響操作的細節未充分利用 → 補成對接說明。**

   | 查核結果／可信度 | 框架應如何使用 |
   |---|---|
   | **高：Synopsis 空白時，原本依賴它的部分功能會改讀 Braindump。** [官方說明](https://docs.sudowrite.com/using-sudowrite/1ow1qkGqof9rtcyGnrWUBS/braindump/bgfrku4qGdfbiFH3ar9PE2) | 暫不做 Synopsis 時保持真正空白；不要把操作提醒貼入平台欄位。 |
   | **高：`characters_raw`／`worldbuilding_raw` 跳過相關性篩選，仍不包含隱藏資訊。** [官方說明](https://docs.sudowrite.com/using-sudowrite/1ow1qkGqof9rtcyGnrWUBS/saliency-engine/4KL8gFeLZNvk8CEeXpfwB2) | 外掛也不能靠 `_raw` 取回秘密；不要預設全部帶入更好。 |
   | **高：History 的 chiclets 可檢查實際使用的上下文。** [官方說明](https://docs.sudowrite.com/getting-started/dQph1snuwbfMWG9wRjsNug/the-basics/po46R9SPcwQ6D7Uzq7tbkP) | Scenes 的底線確認辨認結果；生成後再用 chiclets 診斷是否帶入需要的資料。 |
   | **高：Style Examples 目前限定 Draft 的 Muse／Excellent，而且全帳號共用。** [官方說明](https://docs.sudowrite.com/using-sudowrite/1ow1qkGqof9rtcyGnrWUBS/sudowrite-muse/4k9bFDMSyic6mFPkYFHrkZ) | 切換專案時記錄並更換範文；不能期待其他模式也讀取。 |
   | **高：Series 共用資料受資料夾層級限制，也能查看其他書的 Outline；章節文件只能連結本專案大綱。** [官方說明](https://docs.sudowrite.com/using-sudowrite/1ow1qkGqof9rtcyGnrWUBS/series-support/3vfbZPCB1ANLm75FXmJf28) | 增加卷別與目前狀態記錄，避免改寫續集人物時影響第一集修稿。 |
   | **高：中文輸出仍可能回到英文，官方建議在實際使用的指令欄明說輸出語言。** [官方說明](https://docs.sudowrite.com/resources/ktuxRrzphwp3uTNneRtaos/can-i-use-sudowrite-in-other-languages/aR5Me5vw2J3wmLD9acqrvw) | 語言要求要進入 Draft Extra Instructions／外掛提示；不能只依賴 Style。 |

   CSV 不經 AI 改寫這項調查正確，應繼續當作主要匯入方式。[官方匯入說明](https://docs.sudowrite.com/using-sudowrite/1ow1qkGqof9rtcyGnrWUBS/importing-files/rbGUgrZM6tNuXFG1hjDFyS)

   同名重匯的處理、中文精確計數、別名匹配的大小寫與標點規則，仍應列為未證實。正式投入前，用小型測試專案確認自訂欄位、換行、引號、空白值及隱藏操作即可，不必先做龐大的測試工程。

7. **shared-rules.md、brief／dossier 模板 → 成人內容分工方向可行，但單一標記無法傳遞場景結果 → 增加非露骨交接資料。**

   對適用的虛構角色，交接格式至少包括：

   > 場景入口：目前關係、各自目的。  
   > 界線：已表達的同意、拒絕與其他限制。  
   > 情感轉折：信任、誤解或權力關係如何改變。  
   > 場景出口：下一場開始前已成立的結果。  
   > 後續連續性：誰知道什麼、承諾什麼、仍誤會什麼。  
   > 【Sudowrite 處理】

   標記留在交接區；實際貼入 Scenes 的內容應能獨立理解。完成後只把非露骨的結果與設定變動回收到 bible。holoen 的親密關係欄維持不適用，不從公開互動推測私密關係；有來源的粗口、挑逗梗與黑色幽默照原樣保留。

   另明訂「孤立的聲音校準台詞」屬設定工作；連續場景正文仍由 Sudowrite 處理。Style Examples 優先取自作者原稿或已核准的 Sudowrite 成品。

新增任務類型的優先順序：

| 順序 | 任務 | 最小可用產出與理由 |
|---|---|---|
| 1 | **Outline／Scenes／章節交接** | 章節目標、POV／時態、場景入口、阻礙、選擇、結果、知情範圍、卡片更新點。直接補上設定到正文之間缺少的一段。 |
| 2 | **聲音校準與驗證** | 有來源的詞庫、情境樣本、原創示範標記、角色混淆檢查；由 Sudowrite 試寫，雙方只診斷。**目前 holoen 可把此項升到第一。** |
| 3 | **時間線與設定更新** | 事件時間、敘述順序、角色當前狀態、知情變化及變更影響。讓 bible 隨故事更新。 |
| 4 | **關係矩陣** | A 對 B 與 B 對 A 分開記錄目標、期待、稱呼與衝突；之後再產生關係圖。 |
| 5 | **Style Examples 選編與版本管理** | 從已核准文本選樣，說明節奏、敘述距離與對白比例，記錄目前帳號使用哪套範文。 |
| 6 | **系列作管理** | 共通設定、卷別狀態、版本快照及跨卷變更清單；等第二部作品開始時再擴充。 |

「Claude 做得比我會做的更好的地方」：把深入調查與可直接匯入的 `[SW]` 分開、採用不經 AI 改寫的 CSV，以及先提醒同名重匯可能產生重複卡，都是很實用的設計；声音檔案也比一般 Want／Need 模板更貼近這個專案。「我會做得不一樣的地方」：我會更早建立事實來源分層、角色與讀者的知情狀態，以及綁定版本的驗收機制；並讓調查內容經過場景需求篩選後進入正文。完整度應以保住有用且可信的差異衡量，不以填滿模板衡量。