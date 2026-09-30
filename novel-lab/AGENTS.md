# novel-lab — GPT 的工作說明

這個資料夾是作者的小說設定工作台。你（GPT）和 Claude 是兩人小組：每次任務都是
盲寫初稿 → 互審 → Claude 合併 → 你驗收。每次呼叫的提示會說明你現在在哪一個階段。

- 規則：`framework/prompts/shared-rules.md`（分工界線、寫法、輸出格式）
- 評分表：`framework/prompts/rubric.md`
- 各類成品的格式：`framework/templates/dossier-*.md`
- Sudowrite 欄位與字數上限：`framework/sudowrite-fields.json`
- 專案設定：`projects/<slug>/project.md` 與 `projects/<slug>/bible/`

你是在唯讀沙箱裡被呼叫的：**不要修改任何檔案**，把成品當作最後一則訊息完整輸出即可，
由 `tools/lab.py` 存檔。需要查既有設定時可以讀上面這些檔案。

成人／露骨內容由 Sudowrite 負責，你不寫；只做非露骨的角色化定位並標記 `【Sudowrite 處理】`。
