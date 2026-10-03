# 交接到 ElevenLabs Eleven v4：用原創聲音演出她的台詞（2026-09-30；2026-10-03 依聲音審計 v1 與工作流程研究 W1 修訂）

目標：Sudowrite 寫好的故事，交給 ElevenLabs 的 **Eleven v4** 用**原創設計的聲音**朗讀時，演出她有紀錄的用字、
習慣和喜劇節奏；不複製、不模仿成員本人的聲音。本文整理官方文件查到的做法，和這個專案的角色檔案怎麼接過去。
每張角色的具體表演表在 `projects/holoen/export/elevenlabs/`。

## 先講清楚：聲音本身不能用她本人的

- **ElevenLabs 使用政策**禁止「在沒有同意或合法權利的情況下，刻意複製他人的聲音」
  （"intentionally replicate the voice of another person: without consent or legal right"），
  也禁止用來性化或誤導他人。[ElevenLabs Use Policy §5](https://elevenlabs.io/use-policy)
- **COVER（hololive）**的二次創作規範明文：「不允許從旗下藝人的歌曲擷取聲音用於語音生成，也不視為二次創作。」
  （"we do not allow extraction of our talents' voices from our songs to be used in speech generation"）
  [Derivative Works Guidelines](https://hololivepro.com/en/terms/)。直播音訊雖然沒被逐字點名，
  但同一份規範也禁止「嚴重損害藝人形象」的內容，而 ElevenLabs 那條已經足以擋下。
- 所以：**不要用她們的直播或歌聲做 Instant／Professional Voice Clone，也不要刻意做「聽起來就是她」的仿聲。**
  這也是這個專案「不碰背後真人」的延伸。

好消息：你要的「口吻、習慣、抑揚頓挫」大部分**不在音色裡，而在文字和表演指示裡**，v4 正好最擅長這個。
做法是：Voice Design 的描述定義一個**獨立的虛構聲音**：為場景選擇咬字、質地和情緒幅度，不去對齊成員可辨識的聲音
或任何量測到的聲音特徵；她公開人設的用字習慣寫進腳本，表演指示都是提案，要試聽後才定（W1 WF-007）。

## Eleven v4 能用的控制項（官方）

來源：[Eleven v4 文件](https://elevenlabs.io/docs/overview/capabilities/text-to-speech/eleven-v4)、
[What is Eleven v4](https://elevenlabs.io/docs/help-center/product/core-capabilities/text-to-speech/what-is-eleven-v4)、
[Best practices](https://elevenlabs.io/docs/overview/capabilities/text-to-speech/best-practices)、
[v4 發表文](https://elevenlabs.io/blog/eleven-v4)、[TechCrunch 2026-09-28](https://techcrunch.com/2026/09/28/elevenlabs-new-v4-speech-model-supports-more-expression-control-and-90-languages/)。

| 控制項 | v4 的狀況 | 怎麼用在角色身上 |
|---|---|---|
| **行內標籤** `[...]` | 主要控制方式；可以**疊加**（`[casual] [under his breath]`），模型會照順序做；可以寫**自然語言指示**（`[said angrily in French accent]`、`[lower, thoughtful]`）；比 v3 更聽話，但官方說「not perfect yet」 | 每個角色一組標籤詞彙（見表演表） |
| **上下文** | v4 會讀整段的語氣、節奏和情境，對話中「會回應剛說的話」；長篇接續比 v3 穩 | 一次給完整的一段對話，不要一句一句單獨生成 |
| **標點** | 刪節號＝停頓與重量；全大寫＝加重；破折號＝短停頓／打斷；換行影響節奏 | 用來做 Ina 的慢、Kiara 的 "WAIT. WAIT." |
| **Stability** | 越低越有表現力、每次不同；越高越接近固定基準 | 活潑角色調低，冷靜角色調高（起始值見表演表） |
| **Similarity** | 越高越貼近參考聲音，但可能犧牲自然度 | 原創聲音約 75 起試 |
| Style／Speed 滑桿 | **v4 沒有** | 語速只能靠聲音本身（Voice Design 寫 pace）和標籤（`[rushed]`、`[slowly]`） |
| SSML `<break>` | **不支援** | 用 `[pause]`、`[long pause]`、刪節號、破折號 |
| 發音 | 支援行內 IPA：`/ˈaɪɹɪs/`（要有重音符號），效果因聲音而異 | 名字與專有名詞（見表演表） |
| 多語言 | 90+ 語言，日語品質提升最多；官方文件描述跨語言生成的口音行為，但那是模型層面的說明，**不代表這個原創聲音或成員本人的語言背景** | 德語、日語片語與語言切換都要用選定的原創聲音實際測；不指定地區口音 |
| Text to Dialogue | v4 支援多角色；每一輪有自己的 voice_id；每次請求建議**全部 2,000 字元以內**；用標點表現打斷 | 同一場景的多人對話 |
| 聲音品質 | 聲音的訓練資料裡有的表演最容易做出來；v4 也能做沒訓練過的（耳語、大叫） | 設計聲音時就把「會笑、會大叫」寫進描述 |

模型 ID：`eleven_v4`（品質）、`eleven_v4_turbo`（低延遲，給即時對話用）。

## 專案資料怎麼對應過去

| 角色檔案裡的東西 | 放到 ElevenLabs 的哪裡 |
|---|---|
| 實測音高／語速（[ASR] 量測） | **只是研究背景，不是合成目標**，不放進 Voice Design |
| Voice & Delivery（暫定演出方向） | **獨立的原創聲音設計描述**（自行選擇的質地、咬字和情緒幅度，標明暫定） |
| Dialogue Style、Catchphrases、口頭禪、填充詞 | **腳本文字本身**：v4 會照字演，所以「like, like」、重來、"okay okay okay" 要寫在字裡 |
| Tone Shifts（情境→語調） | **標籤**：每種情境對應一組標籤 |
| 笑聲、驚叫、招牌聲音（GWAK、Kikkeriki） | 說出口的招牌字：**標籤＋文字**，例如 `[startled squawk] GWAK!`；純非語言聲音（笑、尖叫）：**只寫標籤**，不要再拼出來 |
| 名字、日語、德語 | 測過的發音字典規則，或審過的行內 IPA 替換；日文字留在台詞裡，羅馬拼音和翻譯放在不唸的 `ROMAJI`／`GLOSS` 行（見 `docs/scene-script-format.md`）。`pronunciation.tsv` 只是不完整的暫定索引，要看每份表演表第 6 節，包括日文讀音指引 |
| Sounds off（不像她的東西） | **不要用的標籤**（例如給 Kronii 用 `[giggles]`） |

## 工作流程（建議）

1. **做聲音**：每個角色在 Voice Design 用表演表的描述做一個原創聲音，選最符合「音域和能量」的那個；
   存成 `holoen-<名字>`。旁白另外做一個中性聲音。
2. **寫故事**：在 Sudowrite 正常寫。角色卡的 Dialogue Style 已經要求她們的口頭禪和說話習慣。
3. **轉成朗讀腳本**（這一步最關鍵）。作者定案（2026-10-01）：**由 Sudowrite 在寫故事時直接加標籤**。
   做法：角色卡有一個 **Audio Tags** 欄位（每個角色的基準聲音、情境→標籤、招牌聲音、要寫進字裡的習慣、
   IPA、禁用標籤），匯出在 `characters.csv` 的 `Audio Tags` 欄；Story Bible 的 Style 貼上
   `projects/holoen/export/elevenlabs/sudowrite-style.md` 那段規則。Sudowrite 就會在每句對白前加標籤。
   人工或 Claude 再檢查一次時，照下面的原則：
   - 每句台詞前加上該角色、該情境的標籤（查表演表的 Tone Shifts 對照）；
   - 保留、甚至補強她的習慣：重複、自我打斷、填充詞、停頓；
   - 說出口的招牌字寫成標籤＋文字，純非語言聲音只寫標籤；專有名詞加 IPA（日本名字用假名讀音，都標「未測試」）；
   - 旁白和台詞分開。
   Sudowrite 加得不好的地方，可以請 Claude 依表演表修。
4. **生成**：要配音的場景先寫成場景腳本格式（`docs/scene-script-format.md`），用 `tools/scene_to_elevenlabs.py`
   轉成請求檔（明確寫 `model_id: eleven_v4`）和試聽單；每個請求 2,000 單位以內、最多十個聲音，長場景在戲劇段落處
   切成 s001a、s001b。保留產生的 JSON 和試聽單，記下端點、輸出格式、實際設定、發音字典版本、seed、生成日期、
   request ID 和選用的 take。seed 不保證每次聲音完全一樣。
5. **聽了再調**：太平淡→Stability 往下調、標籤寫得更具體（例如 `[deadpan, flat, a beat before the punchline]`）；
   太誇張或不像同一個人→Stability 往上調、減少標籤。

## 做不到或要注意的地方

- **音色不會是她本人**：這是規範，不是技術問題。像不像，靠的是節奏、習慣、用詞和情緒轉換。
- 標籤不是百分之百聽話（官方：not perfect yet）；同一句多試幾次。
- v4 沒有語速滑桿：慢的角色（Ina）要靠聲音設計＋`[unhurried]`＋刪節號；快的角色（Calli、Kiara）靠 `[rapid]`、少停頓。
- 語言切換要用選定的原創聲音實測發音、標籤效果與清楚度；不要指定地區口音或推論成員的語言背景（聲音審計 v1）。
- 粗口與挑逗台詞：ElevenLabs 政策禁止用來性化真人；本專案卡片上的內容已經是非露骨的公開梗，
  但朗讀時仍不要做成針對真人的性內容。

## 參考
- ElevenLabs：[Eleven v4 文件](https://elevenlabs.io/docs/overview/capabilities/text-to-speech/eleven-v4)、
  [Best practices](https://elevenlabs.io/docs/overview/capabilities/text-to-speech/best-practices)、
  [Text to Dialogue](https://elevenlabs.io/docs/overview/capabilities/text-to-dialogue)、
  [Voice Design v3 部落格](https://elevenlabs.io/blog/voice-design-v3)、[Use Policy](https://elevenlabs.io/use-policy)
- COVER：[Derivative Works Guidelines](https://hololivepro.com/en/terms/)
- 查核日：2026-09-30（v4 在 2026-09-28 發布，文件可能還會更新）
