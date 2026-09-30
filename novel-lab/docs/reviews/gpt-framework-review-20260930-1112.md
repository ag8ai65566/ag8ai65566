CHANGES

8 項必改中，**第 1、3 項已處理，其餘部分處理**；另確認兩個程式錯誤。

1. **已處理：事實、觀察與創作分層。**  
   [shared-rules.md:28](/home/user/ag8ai65566/novel-lab/framework/prompts/shared-rules.md:28)、角色模板開頭及 rubric 第 3、4 項已加入分類、禁止補造心理、保留生活細節及原創性不適用。

2. **部分處理：通用規則與格式例外。**  
   holoen 限定已移回專案；shared-rules 已明訂例外。但 [gpt-brief.md:24](/home/user/ag8ai65566/novel-lab/framework/prompts/gpt-brief.md:24)、[rubric.md:12](/home/user/ag8ai65566/novel-lab/framework/prompts/rubric.md:12)仍一律要求第三人稱現在式；[角色模板:110](/home/user/ag8ai65566/novel-lab/framework/templates/dossier-character.md:110)仍寫硬事實「之後不能改」。請同步例外及時間線變更規則，避免初稿與驗收依據矛盾。

3. **已處理：Secrets 操作與資訊分層。**  
   [README.md:40](/home/user/ag8ai65566/novel-lab/README.md:40)、shared-rules 第 8 點及兩份卡片模板已說明手動隱藏、AI 看不到秘密，並區分真相、知情範圍與可見線索。

4. **部分處理：Synopsis 回審與採用版本。**  
   [idea 模板:9](/home/user/ag8ai65566/novel-lab/framework/templates/dossier-idea.md:9)已補回審及單一採用方向。但 [lab.py:567](/home/user/ag8ai65566/novel-lab/tools/lab.py:567)遇多份 Story 只警告，仍把兩套內容全部匯出。須指定有效版本並據此篩選；尚未指定時停止匯出。

5. **部分處理：平台上限與本地估算。**  
   docs 與匯出程式已改成中文估算超限只警告。但 [sudowrite-fields.json:2](/home/user/ag8ai65566/novel-lab/framework/sudowrite-fields.json:2)仍未清楚標示該算法屬本地估算；[idea 模板:46](/home/user/ag8ai65566/novel-lab/framework/templates/dossier-idea.md:46)仍寫「上限 4,000 字」。請統一區分「平台 4,000 words」與「本地中文預算」，不必拘泥上一輪建議的 JSON 鍵名。

6. **部分處理：固定資料包。**  
   [lab.py:125](/home/user/ag8ai65566/novel-lab/tools/lab.py:125)已保存完整 project／bible、雜湊與未附清單。但 `build_prompt()` 仍即時讀取 brief、模板與規則，且完全未附欄位上限。模擬確認：`context.md` 不變，修改 brief／模板仍會改變提示。請把必要輸入一併固定，供雙方使用。

7. **部分處理：驗收收錄門檻。**  
   [lab.py:468](/home/user/ag8ai65566/novel-lab/tools/lab.py:468)起已拒絕 `APPROVED`、核對 final 雜湊並記錄作者裁決理由。但 `REQUIRED_FOR_PROMOTE` 未檢查合併紀錄；模擬中沒有任何合併紀錄仍可收錄。請檢查約定的紀錄檔或 final 內紀錄段落。另外，目前仍接受 `**APPROVE**`、前置空行，與「第一行精確比對」不一致。

8. **部分處理：匯出完整性。**  
   [lab.py:544](/home/user/ag8ai65566/novel-lab/tools/lab.py:544)已處理重複欄位、佔位文字、`None`、先驗證後寫出及清除舊檔。但必要欄位只檢查 Name；模擬中僅有 Name 的角色卡仍成功匯出。請依成品類型檢查必要欄位，區分「缺欄」與「允許留白」。Name 不一致目前也僅警告，尚未確立一致的名稱依據。

修改後確認的程式問題：

- **`status` 崩潰：** [lab.py:645](/home/user/ag8ai65566/novel-lab/tools/lab.py:645)的對照表未處理新增的 `INVALID`；不合格式的驗收結果會觸發 `KeyError: 'INVALID'`。補上顯示分支。
- **分類拼錯會漏卡並刪除舊匯出：** [lab.py:552](/home/user/ag8ai65566/novel-lab/tools/lab.py:552)接受未知 `sw_section`，後續只輸出三種已知分類。模擬 `Character` 時無警告、成功退出，卻清除舊匯出且不產生該卡。須在清除前拒絕未知分類。

建議追蹤：第 3、4 項已採用；第 1、2、6、7 項部分採用，包括差異審查、欄位分工、聲音頻率、官方細節及非露骨交接。第 5 項全卡總量提示，以及用量統計、其餘 Style Examples／Series 細節與新增任務類型，仍暫緩。

以上程式案例均以記憶體模擬確認；未修改檔案，未讀取 `projects/*/runs/`。