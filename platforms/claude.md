# Claude 的設定方式

> ✅ 紀錄、每晚確認、週報這些核心功能，在 **Claude Code 網頁版（claude.ai/code，雲端環境）** 實際跑過；範本化之後的完整設定流程，尚待實測。
> 其他 Claude 介面（一般聊天、桌面 App）可能少了某些功能，請照 AGENTS.md 階段 0 逐項確認。

## 使用者要先準備

| 項目 | 在哪裡設定 |
|---|---|
| 讀到這個 repo | 一般聊天：貼 README 的網址即可。repo 是私人的、或要用 Claude Code：在 claude.ai 設定連線 GitHub（私人 repo 還要請擁有者把你加為協作者） |
| Notion 連線 | claude.ai 設定 → Connectors → Notion，並授權要使用的頁面 |

## 開始

三種方式擇一：

| 方式 | 做法 |
|---|---|
| 一般聊天 | 貼上 README「怎麼開始」的那段話 |
| 安裝 Skill | 上傳 `dist/health-coach-kit.skill`，之後說「我想開始記錄飲食」即可 |
| Claude Code（實測過的方式） | claude.ai/code 開新的工作階段，**選這個 repo**（會自動讀 `CLAUDE.md`），輸入「照 AGENTS.md 幫我設定」 |

## 各階段在 Claude 上怎麼做

| 階段 | 做法 |
|---|---|
| 問卷 | 用 AskUserQuestion 選項卡片，一次最多 4 題 |
| 建 Notion | Notion 連線的建立資料庫工具，可以直接用 `notion/schema.md` 裡的 DDL |
| 排程 | 用「排程／Routine」功能，建立**回到同一個對話**的排程，這樣 Claude 記得使用者的背景。時間要指定時區，例如 `CRON_TZ=Asia/Taipei 55 21 * * *` |
| 產圖 | `node weekly-card/render.mjs data.json out.png`。會自動找專案內或全域安裝的 Playwright（雲端環境有預裝）；都找不到時會提示安裝方式，或改用 `python weekly-card/build_html.py` |
| 傳圖 | 用傳送檔案的工具把 PNG 傳給使用者 |

## 實測時遇到的注意事項

- **雲端環境會被回收**：對話閒置一段時間後，環境裡的檔案會不見。週報範本放在這個 repo 裡，排程觸發時會重新取得，所以不受影響；但**不要**把使用者的資料只存在環境的檔案裡，要寫進 Notion。
- **排程不能另外綁連線**：有些組織不允許排程另外設定 Notion 連線，這時建立「回到同一個對話」的排程，就能沿用對話本身的 Notion 連線。
- **先試跑一次**：建立每晚確認的排程後，立刻手動跑一次，讓使用者看到卡片的樣子。
- **時間避開整點**：整點的排程比較多，可能延遲幾分鐘；例如 22:00 可以改成 21:55。

## 沒有排程功能時

請使用者在手機設一個鬧鐘，時間到了在對話裡說「開始今晚確認」或「幫我做週報」，Claude 照 `prompts/` 的內容執行。
