CHANGES

1. **已處理：資訊分層。** 四類資訊及未證實內容不得確定化入卡的規則仍保留。[shared-rules.md:31](/home/user/ag8ai65566/novel-lab/framework/prompts/shared-rules.md:31)

2. **已處理：寫法例外與時間線。** 引用、歷史、控制欄位的例外，以及時間線變更紀錄均保留。[rubric.md:12](/home/user/ag8ai65566/novel-lab/framework/prompts/rubric.md:12)、[角色模板:110](/home/user/ag8ai65566/novel-lab/framework/templates/dossier-character.md:110)

3. **已處理：Secrets。** 手動隱藏、知情範圍與可見線索規則仍完整。[shared-rules.md:56](/home/user/ag8ai65566/novel-lab/framework/prompts/shared-rules.md:56)

4. **已處理：Story 採用版本。** 模擬確認，多份 Story 只有一份 `active: true` 才能匯出；否則保留舊檔。Synopsis 回審規則亦保留。[lab.py:612](/home/user/ag8ai65566/novel-lab/tools/lab.py:612)、[idea 模板:13](/home/user/ag8ai65566/novel-lab/framework/templates/dossier-idea.md:13)

5. **已處理：平台上限與本地估算。** 兩者仍明確區分。[欄位規格:2](/home/user/ag8ai65566/novel-lab/framework/sudowrite-fields.json:2)

6. **部分處理：固定資料包。** `pack` 已完整凍結輸入，三階段均收到凍結上限；修改原始檔不會改變單一任務的提示。[lab.py:168](/home/user/ag8ai65566/novel-lab/tools/lab.py:168)  
   **仍有批次缺口：** 批次只附第一個 run 的 `gpt-brief`。模擬兩個 run 分別凍結 A／B 版本後合批，送出的提示只有 A，B 完全遺失。請逐任務附入自己的凍結說明，或拒絕混用不同版本的批次。[lab.py:375](/home/user/ag8ai65566/novel-lab/tools/lab.py:375)

7. **已處理：收錄門檻。** 原始第一行直接比較；模擬確認尾端空白、Tab、前置空行及粗體皆判為 `INVALID`。[lab.py:500](/home/user/ag8ai65566/novel-lab/tools/lab.py:500)

8. **部分處理：匯出完整性。** 四種模板與欄位清單已一致；逐一刪除共 30 個欄位均會阻擋。宣告 `sw_section` 卻沒有 `[SW]` 也會在清除舊檔前報錯。[欄位規格:38](/home/user/ag8ai65566/novel-lab/framework/sudowrite-fields.json:38)、[lab.py:581](/home/user/ag8ai65566/novel-lab/tools/lab.py:581)  
   **新增回歸：** 未驗證 `kind`，且 `.get(kind, [])` 會略過全部欄位檢查。模擬 `kind: charcter`、`sw_section: Characters`、只有 Name，仍成功匯出並清除舊檔；`kind: idea` 搭配 Characters 也能匯出缺 Name 的角色列。請先拒絕未知 `kind`，並驗證它與 `sw_section` 的對應，再執行欄位檢查。[lab.py:590](/home/user/ag8ai65566/novel-lab/tools/lab.py:590)

建議追蹤維持上輪：第 3、4 項已採用；第 1、2、6、7 項部分採用；全卡總量提示、用量統計、其餘 Style Examples／Series 細節與新增任務類型仍暫緩。

上述程式案例均以記憶體模擬確認；未修改檔案，未讀取 `projects/*/runs/`。