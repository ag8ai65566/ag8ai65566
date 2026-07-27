# 網路與抓取環境

網路已經開通（2026-07-27 驗證）。這份文件記錄實測結果，以及在雲端 session 裡跑
瀏覽器需要的三個調整——在你自己的電腦上這些都不會生效，也不需要。

## 現況

| 網域 | curl | 瀏覽器 |
| --- | --- | --- |
| `tabelog.com` | ✓ 200 | ✓ 200 |
| `omakase.in` | ✗ 403 | ✓ 200 |
| `www.tableall.com` | ✓ 200 | ✓ 200 |
| `www.tablecheck.com` | ✓ 301 | ✓ 200 |

`omakase.in` 的 403 來自 **Cloudflare**，不是環境政策擋的——換 User-Agent 也一樣，
但真正的瀏覽器可以正常進入。判斷依據是 `recentRelayFailures` 是空的：

```bash
curl -sS "$HTTPS_PROXY/__agentproxy/status"
```

被政策擋掉的主機會出現在那個清單裡。所以**只要是要抓資料，一律走 Playwright**，
不要用 curl 判斷一個站通不通。

## 雲端 session 裡跑 Playwright 的三個調整

都在 `scraper/lib/browser.mjs` 的 `getBrowser()`，全部是條件式的：偵測不到雲端環境
就走 Playwright 預設值。

1. **執行檔路徑**——映像檔預載的 Chromium 版本和 npm 裝的 Playwright 對不上，而
   `playwright install` 是被禁止的。改成掃 `PLAYWRIGHT_BROWSERS_PATH` 底下實際存在
   的 build。
2. **Proxy**——Chromium 不讀 `HTTPS_PROXY`，要用 `proxy: { server }` 明講，否則所有
   連線都是 `ERR_CONNECTION_RESET`。
3. **憑證與 TLS 版本**——代理會重簽 TLS，而 Playwright 每次都開全新 profile，映像檔
   準備好的 NSS 憑證庫用不到。用 `--ignore-certificate-errors-spki-list` 把**那一張**
   CA 的公鑰雜湊釘進去（憑證驗證照常運作，只是多信任這一個簽發者），雜湊在執行時從
   `/root/.ccr/agent-proxy-ca.crt` 算出來，不寫死。另外代理對 Chromium 的 TLS 1.3
   handshake 會 reset，所以加 `--ssl-version-max=tls1.2`；這只影響到本機代理那一段，
   代理對真實網站仍然用它自己不受限的 TLS。

沒有任何一項是關掉憑證驗證，也沒有繞過政策。

## 帳號憑證怎麼放

登入用的帳密**不寫進這個 repo**，放環境變數，抓取腳本只從 `process.env` 讀：

```bash
export OMAKASE_EMAIL=...
export OMAKASE_PASSWORD=...
export TABLEALL_EMAIL=...
export TABLEALL_PASSWORD=...
```

`.gitignore` 已經擋掉 `.env`。登入後的 cookie 存在 `scraper/.auth/`，也是 gitignore 的。

## 如果之後又被擋

環境的網路層級在 claude.ai/code 的環境編輯畫面 → **Network access**。要放行的網域：

```text
tabelog.com
*.tabelog.com
tblg.k-img.com
omakase.in
*.omakase.in
tableall.com
*.tableall.com
tablecheck.com
*.tablecheck.com
```

並勾選 **Also include default list of common package managers**，否則 npm 與 GitHub
會一起被擋掉。

參考：<https://code.claude.com/docs/en/claude-code-on-the-web#network-access>
