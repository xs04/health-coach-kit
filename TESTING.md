# 測試指南（給維護者和幫忙測試的人）

> 這份是用來**測試範本本身**的步驟，不是一般使用說明。一般使用請看 [README.md](README.md)。

## 測試原則

- **模擬朋友的環境**：用朋友最可能使用的方式（一般聊天、貼網址），不要用維護者才有的捷徑。
- **不要動到正式資料**：如果你的 Notion 已經有正式的紀錄，請 AI 另外建一個名稱加上「（測試）」的頁面。
- **讓 AI 誠實回報**：做不到、讀不到、說明跟實際不一樣的地方，都要它說出來，最後整理成「範本問題清單」。

## 共通準備

到 GitHub 的這個 repo 按 **Code → Download ZIP**，解壓縮到手機或電腦。ChatGPT 和 Gemini 讀不到 private repo 的網址，需要上傳這些檔案。

---

## 一、Claude

**情境 A：一般聊天（模擬一般朋友）**

1. 開新對話，確認 Notion 連線有開
2. 貼上：

```
請讀 https://github.com/xs04/health-coach-kit 的 AGENTS.md，照裡面的流程幫我設定。

（測試用）如果我的 Notion 已經有同名的頁面，那是正式資料，不要動它。請另外建一個名稱加上「（測試）」的頁面，所有東西都建在這底下。
如果你讀不到 repo，或有步驟做不到，請直接告訴我，不要自己猜。
最後請整理一份「範本問題清單」給我。
```

讀不到的話，改用對話框的「＋」附加 GitHub repo，或上傳 `health-coach-kit.skill` 之後再試一次。

**情境 B：Claude Code（模擬會用 GitHub 的朋友）**

選這個 repo 開新的工作階段（手機 Claude App 的 **Code**，或 claude.ai/code），貼上同一段話。

---

## 二、ChatGPT（⚠️ 範本未實測）

1. 建立一個新的**專案（Project）**
2. 上傳這些檔案到專案的檔案區：
   - `AGENTS.md`、`safety.md`
   - `onboarding/questions.md`、`notion/schema.md`
   - `prompts/nightly-checkin.md`、`prompts/weekly-report.md`
   - `platforms/chatgpt.md`
   - `weekly-card/` 的 `template.html`、`build_html.py`、`sample.json`
3. 專案說明（Instructions）貼上：

```
照 AGENTS.md 和 safety.md 協助我。我用的是 ChatGPT，平台細節看 platforms/chatgpt.md。
```

4. 在專案裡開新對話，貼上：

```
照 AGENTS.md 幫我設定。

（測試用）如果你能連到我的 Notion，請建一個名稱加上「（測試）」的新頁面，不要動既有的頁面。
開始前請先照 AGENTS.md 階段 0，誠實告訴我你能不能：讀寫 Notion、設定排程、執行 Python、讀圖片。做不到的部分改用 platforms/chatgpt.md 的替代做法。
最後請整理一份「範本問題清單」給我。
```

---

## 三、Gemini（⚠️ 範本未實測）

1. 建立一個新的 **Gem**
2. 指示（Instructions）貼上：

```
照 AGENTS.md 和 safety.md 協助我。我用的是 Gemini App，平台細節看 platforms/gemini.md。
```

3. 知識檔案上傳：
   - `AGENTS.md`、`safety.md`
   - `onboarding/questions.md`、`notion/schema.md`
   - `prompts/nightly-checkin.md`、`prompts/weekly-report.md`
   - `platforms/gemini.md`
   - `weekly-card/` 的 `template.html`、`build_html.py`、`sample.json`
4. 開啟這個 Gem，貼上：

```
照 AGENTS.md 幫我設定。

（測試用）開始前請先照 AGENTS.md 階段 0，誠實告訴我你能不能：連接 Notion 或 Google 試算表、設定排程動作、執行 Python、讀圖片。做不到的部分改用 platforms/gemini.md 的替代做法。
紀錄如果用 Google 試算表，請建一份名稱加上「（測試）」的新檔案。
最後請整理一份「範本問題清單」給我。
```

---

## 測試檢查表

| 項目 | 看什麼 |
|---|---|
| 讀取 | AI 有沒有真的讀到檔案？開始自己編流程，就代表沒讀到 |
| 能力檢查 | 階段 0 的結果是否誠實？（ChatGPT、Gemini 最需要確認） |
| 問卷 | 題目會不會太多、順序順不順 |
| 目標和菜單 | 算出來的數字合不合理 |
| 紀錄位置 | 有沒有建在「（測試）」底下、欄位對不對 |
| 每晚確認 | 建好後有沒有立刻試跑一次 |
| 吉祥物 | 有沒有問你想要什麼吉祥物？拍寵物照片後畫得像不像？有沒有先給你看、確認後才存？ |
| 週報 | 範例圖有沒有說明是假資料；產圖方式是否可行 |

## 回報

把每個平台的「範本問題清單」，加上自己覺得卡住的地方，交給範本維護者修改。
