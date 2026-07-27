# 開通網路權限（必要步驟）

系統要「即時」讀取 Tabelog、OMAKASE、TableCheck、TableAll，就必須讓這個雲端環境
連得到那些網域。目前連不到。

## 現況

環境的網路存取層級是 **Trusted**，只放行套件庫、GitHub 與 Anthropic 自家網域。
實測結果：

| 網域 | 結果 |
| --- | --- |
| `tabelog.com` | ✗ 403（CONNECT 被拒） |
| `omakase.in` | ✗ 403 |
| `www.tableall.com` | ✗ 403 |
| `api.github.com` | ✓ 200 |
| `registry.npmjs.org` | ✓ 200 |

診斷指令：

```bash
curl -sS "$HTTPS_PROXY/__agentproxy/status"
```

`recentRelayFailures` 會列出被擋掉的主機名稱與原因。

## 怎麼改

在 claude.ai/code 開啟這個環境的編輯畫面 → **Network access** 選 **Custom** →
在 **Allowed domains** 一行一個貼上：

```text
tabelog.com
*.tabelog.com
omakase.in
*.omakase.in
tableall.com
*.tableall.com
tablecheck.com
*.tablecheck.com
www.google.com
maps.googleapis.com
*.googleapis.com
*.gstatic.com
```

並勾選 **Also include default list of common package managers**，否則 npm 與
GitHub 也會一起被擋掉。

改完之後開新的 session，重跑上面的 `curl` 驗證，回報應該變成 200。

參考：<https://code.claude.com/docs/en/claude-code-on-the-web#network-access>

## 為什麼不繞過

代理的說明文件明確要求：組織政策的 403/407 不要重試、也不要繞路，回報即可。
所以這件事只能由帳號擁有者在環境設定裡開通。

## 帳號憑證怎麼放

開通之後，登入用的帳密**不寫進這個 repo**。做法是放進環境變數：

```bash
export OMAKASE_EMAIL=...
export OMAKASE_PASSWORD=...
export TABLEALL_EMAIL=...
export TABLEALL_PASSWORD=...
```

抓取腳本只從 `process.env` 讀。`.gitignore` 已經擋掉 `.env`。
