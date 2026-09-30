APPROVE

1. **已處理：資訊分層。** 四類標記及未證實內容不得確定化入卡的規則保留。[shared-rules.md:31](/home/user/ag8ai65566/novel-lab/framework/prompts/shared-rules.md:31)
2. **已處理：寫法例外與時間線。** 引用、歷史、控制欄位例外與時間線變更紀錄均保留。[shared-rules.md:45](/home/user/ag8ai65566/novel-lab/framework/prompts/shared-rules.md:45)
3. **已處理：Secrets。** 手動隱藏、知情範圍、可見線索及秘密副本檢查仍完整。[shared-rules.md:56](/home/user/ag8ai65566/novel-lab/framework/prompts/shared-rules.md:56)
4. **已處理：Story 採用版本。** 多份 Story 須恰有一份 `active: true`；Synopsis 回審規則保留。[lab.py:631](/home/user/ag8ai65566/novel-lab/tools/lab.py:631)、[idea 模板:13](/home/user/ag8ai65566/novel-lab/framework/templates/dossier-idea.md:13)
5. **已處理：平台上限與本地估算。** 兩者仍明確區分。[欄位規格:2](/home/user/ag8ai65566/novel-lab/framework/sudowrite-fields.json:2)
6. **已處理：固定資料包。** 批次先凍結所有 run，再比較說明版本。記憶體模擬確認：四階段遇到不同版本均在 `prepare_run` 前停止；相同版本可繼續。[lab.py:382](/home/user/ag8ai65566/novel-lab/tools/lab.py:382)
7. **已處理：收錄門檻。** 仍直接比較原始第一行，不接受空白或 Markdown 包裝。[lab.py:516](/home/user/ag8ai65566/novel-lab/tools/lab.py:516)
8. **已處理：匯出完整性。** 已先驗證 `kind` 與 `sw_section` 對應。53 個模擬案例通過：未知／缺失／錯配類型、缺欄位均阻擋且不動舊匯出；四種合法對應可匯出，模板與欄位清單一致。後續雖仍用 `.get(kind, [])`，目前已無原先的繞過路徑。[lab.py:606](/home/user/ag8ai65566/novel-lab/tools/lab.py:606)

**新問題：未發現本輪修改造成的實際錯誤。** `effort_for()` 的階段預設、參數與環境變數優先順序，以及低於 high 的拒絕檢查均通過模擬。[lab.py:45](/home/user/ag8ai65566/novel-lab/tools/lab.py:45)

**建議追蹤：** 第 3、4 項已採用；第 1、2、6、7 項部分採用；全卡總量提示、用量統計、其餘 Style Examples／Series 細節與新增任務類型仍暫緩。

未修改檔案，未讀取 `projects/*/runs/`。