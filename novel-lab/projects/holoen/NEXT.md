# 接續步驟（給下一個 session 或排程喚醒的 Claude）

狀態（2026-10-01 16:30 UTC，Justice 完成並收錄；下一階段：GPT 專案諮詢與重任務）：
- **Justice 完成**：四張角色卡（Elizabeth Rose Bloodflame、Gigi Murin、Cecilia Immergreen、Raora Panthera）、世界觀卡
  `hololive -Justice-`、`Justice Pairs`；GPT 三輪 xhigh 逐條核對審查（`runs/20261001-1032-character-Elizabeth-Rose-Bloodflame/gpt-free.md`
  ＝Liz＋Gigi，`…-Cecilia-Immergreen/gpt-free.md`＝Cecilia＋Raora，`…-world-hololive--Justice/gpt-free.md`＝世界觀卡＋其他卡的 Justice diff）
  已逐條併進各卡 Merge Record，作者裁決收錄（`--force`）。合併腳本在 scratchpad `fill/merge_{erb,gigi,cec,rao,wjus,wpairs}.py`、
  `fill/cast_jus2.py`、`cast_jus3.py`、`cross_bff.py`、`cross_lyra.py`（scratchpad 不進 git、容器回收就消失；以各 run 的 final.md 與 bible 為準）。
  - 主要更正：3D showcase 是 08-01/02/08/09 PDT（不是 08-09/10），08-16 PDT 團體 3D 聯動；Serendipity 官方 unit 名（Autofister、Bloodraven、
    B.F.F 等七組）與客串曲；LYRA 是五人 "III" remix 翻唱；Cecilia 出道的聊天室遊戲是 nullrefrepro 實作；Raora／Cecilia 出道美術分工
    有方向性；"Uncle Erb" 改成 Liz 自己標題的「Nephew」叔姪梗；Cecemoco＝Cecilia＋Mococo；只引用兩模型一致的片段（Gigi 的 but/and、
    Cecilia 的 sign-off、Raora 的 "Hear me out" 都切成共同片段）；Gigi／Cecilia／Raora 的預設語氣改得不單一（不是一直大叫／一直挖苦／一直笑）。
  - 連動修改並重新收錄 21 張既有卡（Calli 的 Relationships 壓到 349／350 字）。
  - 表演表：`export/elevenlabs/{Elizabeth-Rose-Bloodflame,Gigi-Murin,Cecilia-Immergreen,Raora-Panthera}.md` 已依合併後的卡更新。
  - 匯出：`export/characters.csv`（18 張）、`export/worldbuilding.csv`（24 張）。
- **作者新指示（2026-10-01 16:00）**：作者重置了 GPT 額度，另有一張重置券（10/4 到期），10/4 前盡量用滿但要合理有效率；讓 GPT 了解專案全貌、
  設計流程、和 Claude 討論怎麼交付給作者最好。做法寫在 project.md。
- **GPT 待跑**：`runs/20261001-1557-check-Project-Consult`（第 1 輪：A 交付形式、B 到 10/4 的流程、C 跨卡／結構問題、D 問題）。16:05 額度用完，
  重置 20:27 UTC；send_later `trig_01KjXFjeULyTFPxWgxZhmZSL`（20:29）回來跑 `lab.py gpt-resume`。
- **下一步**：讀 GPT 第 1 輪提案 → Claude 寫第 2 輪回覆（同一 run 的新 to-gpt.free.md 或新 run）→ GPT 定案 → 依序跑議定的重任務
  （全卷交叉一致性審計、舊卡近期補完、世界年表完整性）→ 合併、收錄、匯出、推送、中文回報。Hakos Baelz、Tsukumo Sana 等作者下令。
- 排程：Claude 自動續做 `trig_01V2bEJdsw5EnZpMBaPKL4tQ`（每小時 :20，提示已改成這一階段）。

（以下為較早的狀態紀錄）

狀態（2026-10-01 14:00 UTC，Justice：草稿完成，等 GPT 審查）：
- **作者新指示**：Advent 之後做 Justice；GPT 全部 xhigh；GPT 額度用完時 Claude 繼續做；雙方額度用完都排程回來；
  想辦法把 GPT 的長處用到最大（做法寫在 project.md）。
- 排程：Claude 自動續做 `trig_01V2bEJdsw5EnZpMBaPKL4tQ`（每小時 :20）；GPT 重跑 send_later `trig_015aKJi4ANzUxSwwRBKEtvUX`
  （15:01 UTC，跑 `lab.py gpt-resume`）。Justice 全部收錄、匯出、推送後刪除前者並用中文回報。
- **完成（Claude）**：四張角色卡草稿（runs `20261001-1032-character-{Elizabeth-Rose-Bloodflame,Gigi-Murin,
  Cecilia-Immergreen,Raora-Panthera}/claude-draft.md`，含聲音段落）；世界觀卡 `hololive -Justice-`、`Justice Pairs`
  （runs `20261001-1032-world-*`）；其他 14 人 Relationships 與 5 張世界觀卡已加 Justice（final.md，尚未重新收錄）；
  音檔報告 `research/audio-check/{elizabeth,gigi,cecilia,raora}.md`（兩模型核對）；X 發文 `research/x-posts.md`。
- **GPT 待跑（依序）**：三個 xhigh 逐條主張核對審查（`framework/prompts/gpt-claimcheck-review.md`），提示在
  `runs/20261001-1032-character-Elizabeth-Rose-Bloodflame/to-gpt.free.md`（Liz＋Gigi）、
  `runs/20261001-1032-character-Cecilia-Immergreen/to-gpt.free.md`（Cecilia＋Raora）、
  `runs/20261001-1032-world-hololive--Justice/to-gpt.free.md`（兩張世界觀卡＋其他卡的 Justice 修改 diff）。
  原本的研究任務（`20261001-1021-research-*`）因草稿已先完成而改由審查涵蓋（審查同時查證與補缺漏），不再跑。
  若 `novel-lab/.gpt-quota.json` 遺失：依序跑 `python3 novel-lab/tools/lab.py gpt <上面三個 run> free`。
- 隱私（不寫）：Raora 2025-11 起的手術休養、Cecilia 2026-07 起的休息與家庭事由、Elizabeth 2026-09 的半休、
  性向、試鏡次數、旅行、母語／國籍說法（口音只當聲音特徵寫）。
- 下一步：GPT 審查 → 逐條併進 final.md（Merge Record）→ `promote --force` → `export holoen` → 四份 ElevenLabs
  表演表 → NEXT.md／project.md → 推送 → 刪除每小時排程 → 中文回報。

（以下為較早的狀態紀錄）
狀態（2026-10-01，Advent 完成）：
- **Advent 全員完成並收錄（作者 2026-10-01 下令）**：角色卡 Shiori Novella、Koseki Bijou、Fuwawa Abyssgard、
  Mococo Abyssgard（Nerissa 先前已完成）；新世界觀卡 `FUWAMOCO`（雙胞胎單位／共用頻道）、`Advent Pairs`
  （團內與跨分部關係網）；`hololive -Advent-` 卡改寫成整團。
  - GPT 一輪審查 `runs/20261001-0549-world-Advent-Pairs/gpt-free.md`（high），逐條併進各卡 Merge Record，
    作者裁決收錄（`--force`）。主要更正：Shiori–Kronii 是「一起主持 Rating Your Clocks」（不寫誰的時鐘）；
    "2 Creatures + 1 Reaper" 只有 Fuwawa；Pero 一律寫成虛構吉祥物；子集合作不算全團（R.E.P.O. 時 Nerissa
    只是 "in Bird Spirit"）；存檔次數不寫成關係排名；Mococo 的「比較聰明／黏人」刪除；"æ" 是粉絲拼法不是 IPA；
    混音錄音的音高數字不進 Audio Tags；3D 日期標 PDT；-All for One- 首日先全員 "All for One" 再 "Genesis"。
  - 新增事實（官方頁查證）：GreyScaleX "Purrfect Pair" 周邊（2026-09-05 開賣）、hololive night（Dodger
    Stadium，2025-07-05，Ina／IRyS／Bijou）、Kiara 陪 Bijou 練難編舞（Serendipity 訪談 04）、
    Advent 3D 聯動（2024-08-17 PDT）。
  - 隱私：健康、家人、住處、睡眠等一律不寫；Mococo 的休息公告比照 Kiara 不寫。
  - 連動修改並重新收錄：Calli、Kiara、Kronii、Gura、Ina、Ame、IRyS、Fauna、Mumei、Nerissa 的 Relationships；
    VTuber Persona、hololive、History 2023-2026、Concerts、Cross-Branch 世界觀卡。
  - 音檔報告：`research/audio-check/shiori.md`、`bijou.md`、`fuwamoco.md`（兩模型核對；只引用兩模型一致的片段）。
  - 表演表：`export/elevenlabs/Shiori-Novella.md`、`Koseki-Bijou.md`、`Fuwawa-Abyssgard.md`、`Mococo-Abyssgard.md`。
  - 匯出：`export/characters.csv`（14 張）、`export/worldbuilding.csv`（22 張）。
- **已完成成員**：Myth 五人、Kronii、IRyS、Fauna、Mumei、Advent 五人（含 Nerissa）。其餘成員（Justice 等）等作者下令。
- **下一步候選**（作者下令前不做新成員）：Mococo 缺乾淨的個人說話樣本（只有薄的 2025 個人台和雙人台）；
  Shiori 可補一段純雜談窗口；Bijou 可補一段雜談窗口。

（以下為較早的狀態紀錄）
狀態（2026-10-01 06:40 UTC）：
- **Ceres Fauna、Nanashi Mumei 完成並收錄（作者 2026-10-01 下令）**：角色卡＋`Fauna and Mumei Pairs` 世界觀卡。
  GPT 一輪審查 `runs/20261001-0454-world-Fauna-and-Mumei-Pairs/gpt-free.md`（high）已逐條併進 Merge Record，
  作者裁決收錄（`--force`）。音檔報告 `research/audio-check/fauna.md`、`mumei.md`（兩模型核對；
  Fauna 一段會員限定音檔誤抓後未使用）；表演表 `export/elevenlabs/Ceres-Fauna.md`、`Nanashi-Mumei.md`。
  - 連動修改並重新收錄：8 張既有角色卡的 Relationships、Promise／hololive／Cross-Branch／兩張 History／
    Concerts／VTuber Persona 世界觀卡。GPT 指出並已更正：Mumei「最後一場個人遊戲台」說法錯誤
    （04-22 與 IRyS 的 Overwatch 之後還有 04-24 Promise R.E.P.O.）、"Bae's most frequent partner" 改為
    recurring、Lui 的 "bird sisters" 是標題不是台詞、Cecilia／Gigi 分開、"sultry" 從所有演出指示移除。
  - 新增事實（官方頁查證）：Fauna＆Mumei 原創合唱 "It's Not a Phase"（-Breaking Dimensions- 2024-08-24 首演，
    2024-12-22 發售）；Breaking Dimensions 的 Kiara–Mumei–Nerissa、Fauna–Shiori–Nerissa 三人曲；
    Mumei 與 Korone 合唱翻唱（2025-04-23）、"Outside the Box" 的 JP 來賓（Okayu、Korone、Nene、Koyori）。
  - 未採納（理由寫在 Merge Record）："I'm always on time" 保留（第二模型全文有）；IPA 保留並標 provisional
    （與其他八張卡一致，作者要求教發音）。
  - 匯出：`export/characters.csv`（10 張）、`export/worldbuilding.csv`（20 張）。
- **已完成成員**：Myth 五人、Kronii、IRyS、Nerissa、Fauna、Mumei。其餘成員等作者下令。

（以下為較早的狀態紀錄）
狀態（2026-10-01 04:20 UTC）：
- **完成並收錄（作者裁決，GPT 只審一輪）**：19 張世界觀卡＋8 個角色（Myth 五人、Kronii、IRyS、Nerissa）。
  GPT 審查 `runs/20260930-2309-world-hololive/gpt-free.md`（high）；意見已逐卡併進 final.md 的 Merge Record。
  已匯出：`export/characters.csv`（8 張，含 Audio Tags 欄）、`export/worldbuilding.csv`（19 張）、
  `export/sudowrite-paste.md`、`export/cards/`；`export/elevenlabs/` 八人表演表＋`sudowrite-style.md`（Style 規則）。
- 審查後新增的官方來源：Serendipity 訪談（IRyS–Bae、Nerissa–Elizabeth）、World Tour '24 官方報告、
  DANGERyS（2026-07-12 發售）、In My Feelings（2024-08-08）、Moona "100%"（2025-02-16）、ASOBI★MAWARI-TAI!。
- **作者裁決（2026-10-01）**：Kiara 不寫成休息中（2026-09-09 的公告不用）。
- **下一步候選**（作者下令前不做新成員）：繼續擴充世界觀（更多跨分部關係、X 發文、各成員演唱會細節）；
  用音檔補強既有角色（Kiara–Nerissa 的 KiaRissa 台詞、各人的笑聲）。

- **作者新指示（2026-10-01，已寫進 project.md）**：
  1. 世界觀要大量補：人際關係（含 JP／ID／GAMERS 等其他分部）、新成員加入、團體／個人演唱會、
     3D、Expo／fes 等活動都是共同記憶；X 公開發文是關鍵來源。GPT 額度 0 時 Claude 自己盡量完善。
  2. 目標是 EN 全員，但**名單外的成員等作者下令**（目前已下令：IRyS、Nerissa）。
  3. **Sudowrite 會自己加 ElevenLabs 標籤**：要把每個角色影響「聲音」的一切（說話方式、性格、口癖、
     口音、語速、音域、笑聲、招牌聲音、情境轉換、發音）完整教給 Sudowrite。
     計畫：角色卡加一個 [SW] 欄位「Audio Tags」（情境→標籤、招牌聲音、發音、不要做的），
     故事層 Style 加標籤格式規則；export 也輸出。內容來源＝`export/elevenlabs/<名字>.md`。
- 新世界觀卡（2026-10-01）：`hololive -Advent-`、`IRyS and Nerissa Pairs`（runs `20261001-0001-world-*`）；
  `hololive -Promise-` 改成涵蓋 IRyS。Kiara／Calli／Kronii／Ina 的 Relationships 已加 IRyS／Nerissa（final.md）。
- IRyS：草稿完成（runs `20260930-2334-character-IRyS`），音檔報告 `research/audio-check/irys.md`，
  表演表 `export/elevenlabs/IRyS.md`。`lab.py export` 現在會保留 `export/elevenlabs/`。

- **作者定案（新）**：以真實性為主，卡片優先用**真實台詞**（含粗口、挑逗）；音檔由 Claude 自己核對。
- **音檔核對已完成**（六人）：報告在 `research/audio-check/<名字>.md`，工具在 `novel-lab/tools/audiocheck/`。
  - 方法：ragtag 直播存檔 → whisper small.en 轉寫 + Praat 量音高 → **上卡片的句子再用 medium.en 第二模型核對**。
  - 檔案一律標 [ASR]，並寫「machine-transcribed … without independent listening verification」。不是人耳聽寫。
  - 第二模型推翻的句子已從卡片移除（Kronii 一處 hellos、Calli "Fucking adorable."、Kiara 整串 "so cute"、
    "Damn it"、Gura "god damn"/"Damn."、Ame "Bitch."）。
- **gen-1 Myth ＋ Kronii、Calli 六人全部收錄（2026-09-30 22:53 UTC）**，已匯出：
  `export/characters.csv`（6 張）、`export/sudowrite-paste.md`、`export/cards/*.csv`。
  - Kiara：GPT APPROVE 收錄。
  - Kronii、Calli、Ina、Ame：作者裁決 (b) 收錄（`--force`，記在各 run 的 `author-decision.md`，不算 GPT 核准）。
  - Gura：Claude 比照作者對上述四人的裁決收錄（第 2 輪上限、意見已照改），作者可推翻。
- **世界觀（2026-09-30 作者指示）**：13 張世界觀卡草稿完成（runs `20260930-2309-world-*`，各有 claude-draft.md）：
  hololive、VTuber Persona and Lore（最重要：她們知道自己是有人設的實況主）、Streaming Life、hololive -Myth-、
  hololive -Promise-、TakaMori、TakoTori、AmeSame、Bone Bros、Time and Death、Time Duo、Octo'Clock、Myth Pairs。
  六張角色卡已改成人設框架（"a VTuber whose lore… makes her…"、"her avatar…"）並更新 Relationships；
  Kronii 聲音描述更正（K8 其實有寫深嗓音／音域廣）。這些改動在 runs 的 final.md，**還沒重新收錄**。
  - 作者指示：GPT 只審一輪。`runs/20260930-2309-world-hololive/to-gpt.free.md` 已備好（13 張卡＋角色卡改動）。
  - **Codex 額度 02:22 UTC 重置**；send_later `trig_012rQiQwJKBepLjf73cYGMgw` 在 02:27 UTC 叫醒這個 session。
  - 審完：意見併進各 world run 的 final.md（claude-draft.md → final.md，加 Merge Record），六張角色卡也一起，
    然後 `promote --force --reason "作者指示 GPT 只審一輪"`，`export holoen`。
- **IRyS、Nerissa Ravencroft**（作者：世界觀做完後接著做）：runs `20260930-2334-character-IRyS`、
  `20260930-2334-character-Nerissa-Ravencroft` 已建立；音檔 jobsG 轉寫中；Claude 研究與初稿進行中。
- **ElevenLabs v4 交接（作者 2026-09-30 問）**：指南 `novel-lab/docs/elevenlabs-v4.md`；六人表演表
  `export/elevenlabs/<名字>.md`（原創聲音描述、起始設定、腳本習慣、情境標籤、招牌聲音、IPA、不要做的事、示範）。
  **不複製成員本人聲音**（ElevenLabs Use Policy §5、COVER 規範）。IRyS／Nerissa 的表演表等她們的聲音段落完成後補。
- **近期權重**（作者定案，已寫進 project.md）：描述現在的預設說話方式時，近期直播權重較高；
  早期梗保留為共同記憶。六人都已照此檢查（Ame 換上 2024 台詞、Calli 招呼語順序、Gura 以 2024 為預設）。
- 下一步（額度允許時）：Council/Promise 其他成員，或繼續用音檔補強既有六人（例如 Kronii 的 GWAK、
  Calli 的笑聲，這些 whisper 寫不出來，需要別的方法）。
- **框架**：GPT 已 APPROVE（`docs/reviews/gpt-framework-review-20260930-1621.md`）。
- 作者定案：初稿 xhigh，審稿／驗收 high（lab.py 預設已是如此）。

合併與修改的規則：
- wiki 一律寫「X2 §Section」段落標記；wiki 原文可重抓：
  `https://virtualyoutuber.fandom.com/api.php?action=parse&page=<Page>&prop=wikitext&format=json`
- 檔案開頭有「Audio status」；clip 標題只證明「上傳者這樣描述」；頻率是估計（字幕／轉寫計數除外）。
- **只有兩個模型都同意的 [ASR] 句子可以上卡片**；第一模型的次數統計只是參考（small.en 遇日語會憑空寫英文）。
- 卡片去重：精確台詞只放 Catchphrases；Personality 寫行為；Dialogue Style 寫句法（可附 "Lines of hers:"）；
  Voice & Delivery 寫聲音，不放台詞。
- 不把玩笑寫成永久規則；引述要有確切來源段落，否則 [Unverified] 並移出卡片。
- 粗口與挑逗台詞照原樣保留（作者定案），wiki 打碼的字寫出來並標「censored in source / inferred」。
- 不寫真人資訊（寵物原型、家人、健康、國籍、畢業原因）。

```bash
L="python3 novel-lab/tools/lab.py"; R=novel-lab/projects/holoen/runs
K=$R/20260930-0704-character-Ouro-Kronii; C=$R/20260930-0704-character-Mori-Calliope
KI=$R/20260930-1113-character-Takanashi-Kiara; IN=$R/20260930-1113-character-Ninomae-Inanis
GU=$R/20260930-1113-character-Gawr-Gura; AM=$R/20260930-1113-character-Watson-Amelia

$L doctor                                   # 必須顯示「會透過 Codex CLI 呼叫 GPT」
$L gpt $KI $IN $GU $AM verify               # 四人第 1 輪（若 CHANGES：修正後第 2 輪）
$L gpt $K $C verify                         # Kronii/Calli 額外一輪
$L promote <run>   # 每個 APPROVE 的
$L export holoen
```

音檔核對重跑（scratchpad 內，需要 `pip install faster-whisper praat-parselmouth numpy imageio-ffmpeg`）：
見 `novel-lab/tools/audiocheck/README.md`。YouTube 本身仍擋這個容器；不要繞過它的防機器人機制。

回報給使用者時用中文摘要。之後的成員名單見 project.md。
