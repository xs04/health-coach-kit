# Gemini 的設定方式

> ⚠️ **未實際測試**。這份是依照 Gemini 一般的功能撰寫的，實際能做到的程度會依方案、地區和功能更新而不同。
> 設定時請 Gemini 先照 AGENTS.md 階段 0 逐項確認自己的能力，並如實告訴使用者。

Gemini 有兩種用法，能力差很多，先選一種：

| | Gemini App（網頁、手機） | Gemini CLI（電腦終端機） |
|---|---|---|
| 適合 | 一般使用者 | 會用終端機的人 |
| 讀這個 repo | 下載 ZIP 後上傳檔案，或放進 Gem 的知識檔案 | `git clone` 後在資料夾裡執行，會自動讀 `GEMINI.md` |
| Notion | 通常**沒有**內建的 Notion 連線 → 建議改用 **Google 試算表** | 可以接 Notion 的 MCP 伺服器 |
| 排程 | 部分方案有「排程動作」，可以定時發訊息 | 沒有內建排程 → 用手機鬧鐘或行事曆提醒 |
| 產週報圖 | 程式執行環境通常沒有瀏覽器 → `build_html.py` 產生 HTML，開啟後截圖 | 本機有 Node＋Playwright 就用 `render.mjs` 直接出 PNG |

## Gemini App

1. 建立一個 **Gem**：
   - 指示（Instructions）貼上：「照 AGENTS.md 和 safety.md 協助我。我用的是 Gemini App，平台細節看 platforms/gemini.md。」
   - 知識檔案上傳：`AGENTS.md`、`safety.md`、`onboarding/questions.md`、`notion/schema.md`、`prompts/` 兩個檔案、`weekly-card/` 所有檔案
2. 開啟這個 Gem，輸入：「照 AGENTS.md 幫我設定」

### 各階段的做法

| 階段 | 預期做法 | 做不到時 |
|---|---|---|
| 問卷 | 用編號選項 | — |
| 紀錄位置 | **Google 試算表**：建一份檔案，分成「飲食紀錄」「運動紀錄」「身體紀錄」三個工作表，欄位和 `notion/schema.md` 相同 | 不能寫入試算表時：Gemini 每晚輸出一行 CSV，使用者自己貼上 |
| 一週菜單 | 放在 Google 文件，或直接記在 Gem 的指示裡 | — |
| 每晚確認 | 用「排程動作」每天定時發訊息 | 排程動作沒辦法讀寫試算表時：只負責提醒，使用者回到 Gem 說「開始今晚確認」。完全沒有排程：用手機鬧鐘 |
| 週報 | 執行 `build_html.py` 產生 HTML，使用者開啟後截圖 | 不能執行程式時：用文字表格呈現 |

> 使用者堅持用 Notion：Gemini 輸出 CSV，使用者每週匯入 Notion 一次。

## Gemini CLI

1. `git clone` 這個 repo，在資料夾裡執行 `gemini`（會自動讀 `GEMINI.md`）
2. 想用 Notion：在 Gemini CLI 的設定裡加上 Notion 的 MCP 伺服器
3. 輸入：「照 AGENTS.md 幫我設定」

| 階段 | 做法 |
|---|---|
| 紀錄 | 透過 Notion MCP 寫入；沒有接就用本機 CSV 或 Google 試算表 |
| 每晚確認、週報 | 沒有內建排程：設手機或行事曆提醒，時間到了打開 CLI 說「開始今晚確認」「做這週的週報」 |
| 產圖 | `node weekly-card/render.mjs data.json out.png`（要先 `npm i playwright` 並安裝瀏覽器），或 `python weekly-card/build_html.py` |

## 特別注意

- **不要用圖片生成功能畫週報**：數字和文字容易畫錯，一定要用 `weekly-card/` 的範本。
- 重要設定（每日目標、紀錄檔案連結、運動計畫）寫進 Gem 的指示，不要只依賴對話記憶。
- 能力檢查的結果要誠實告訴使用者，例如：「我目前沒辦法連接 Notion，改用 Google 試算表」。
