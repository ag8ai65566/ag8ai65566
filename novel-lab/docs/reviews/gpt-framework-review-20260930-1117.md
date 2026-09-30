CHANGES

**第 1–5 項已處理；第 6–8 項仍部分處理。**

1. **已處理：資訊分層。** [shared-rules.md:31](/home/user/ag8ai65566/novel-lab/framework/prompts/shared-rules.md:31)保留四類資訊、禁止補造心理及未證實內容不得確定化入卡。

2. **已處理：寫法例外與時間線。** [gpt-brief.md:24](/home/user/ag8ai65566/novel-lab/framework/prompts/gpt-brief.md:24)、[rubric.md:12](/home/user/ag8ai65566/novel-lab/framework/prompts/rubric.md:12)已同步例外；[角色模板:110](/home/user/ag8ai65566/novel-lab/framework/templates/dossier-character.md:110)允許依時間線變更並記錄。

3. **已處理：Secrets。** [shared-rules.md:56](/home/user/ag8ai65566/novel-lab/framework/prompts/shared-rules.md:56)及卡片模板保留手動隱藏、知情範圍與可見線索的規則。

4. **已處理：Story 採用版本。** [lab.py:595](/home/user/ag8ai65566/novel-lab/tools/lab.py:595)模擬確認：多份 Story 若沒有或有兩份 `active: true`，停止匯出並保留舊檔；只有一份時只輸出該份。Synopsis 回審規則亦保留。

5. **已處理：平台上限與本地估算。** [欄位規格:2](/home/user/ag8ai65566/novel-lab/framework/sudowrite-fields.json:2)、[idea 模板:48](/home/user/ag8ai65566/novel-lab/framework/templates/dossier-idea.md:48)已明確區分。

6. **部分處理：固定資料包。** 任務 brief、模板、規則、評分表與上限確已凍結，但仍有三個缺口：
   - [lab.py:191](/home/user/ag8ai65566/novel-lab/tools/lab.py:191)、[261](/home/user/ag8ai65566/novel-lab/tools/lab.py:261)仍即時讀取階段提示及 `gpt-brief.md`；模擬修改後，同一任務的提示仍會改變。
   - [pack:369](/home/user/ag8ai65566/novel-lab/tools/lab.py:369)只建立 `context.md`，未同步凍結其餘輸入，尚未確保雙方初稿使用同一版本。
   - 上限只接在 `{{schema}}`；[review 提示](/home/user/ag8ai65566/novel-lab/framework/prompts/gpt-review.md:36)與 [verify 提示](/home/user/ag8ai65566/novel-lab/framework/prompts/gpt-verify.md:41)沒有這個插槽，模擬確認兩階段均未收到上限。請在建立資料包時完整凍結，並明確附入各階段。

7. **部分處理：收錄門檻。** 合併紀錄檢查已生效，粗體與前置空行也會被拒絕；但 [verdict:487](/home/user/ag8ai65566/novel-lab/tools/lab.py:487)仍用 `.rstrip()`，`APPROVE` 後接空白仍被接受。若維持「第一行精確相等」契約，應直接比較原始第一行。

8. **部分處理：匯出完整性。** 僅有 Name、Name 不一致均已拒絕，但模擬仍確認：
   - [欄位規格:43](/home/user/ag8ai65566/novel-lab/framework/sudowrite-fields.json:43)漏列角色的 `Catchphrases`、`Voice & Delivery`，以及世界觀的 `Rules`、`Sensory Details`、`Secrets`；缺這些段落仍成功匯出。請依成品模板補齊清單，區分 world／research。
   - [lab.py:565](/home/user/ag8ai65566/novel-lab/tools/lab.py:565)直接跳過零 `[SW]` 段落的檔案；即使宣告 `sw_section: Characters`，仍成功退出並清除舊匯出、漏掉該卡。宣告為卡片卻缺全部欄位時必須報錯。

先前兩個程式錯誤已修復：[status:676](/home/user/ag8ai65566/novel-lab/tools/lab.py:676)可顯示 `INVALID`；[未知分類檢查:570](/home/user/ag8ai65566/novel-lab/tools/lab.py:570)會在清除舊檔前停止。未確認其他新增回歸。

建議追蹤維持上一輪：第 3、4 項已採用；第 1、2、6、7 項部分採用；全卡總量提示、用量統計、其餘 Style Examples／Series 細節與新增任務類型仍暫緩。

以上程式案例均以記憶體模擬確認；未修改檔案，未讀取 `projects/*/runs/`。