# 測試指南（給維護者和幫忙測試的人）

> 這份是用來**測試範本本身**的步驟，不是一般使用說明。一般使用請看 [README.md](README.md)。
> repo 是公開或私人都適用：每個平台都**先貼網址**，讀不到再用備案。

## 測試原則

- **模擬朋友的環境**：用朋友最可能使用的方式（一般聊天、貼網址），不要用維護者才有的捷徑。
- **用陌生人的視角**：repo 公開之後，最好用**沒有連 GitHub 的帳號**測一次。repo 擁有者自己的帳號有權限，讀得到不代表別人讀得到。
- **確認真的讀到**：請 AI 先引用 AGENTS.md 的第一行。引用不出來，或開始自己編流程，就是沒讀到。
- **不要動到正式資料**：如果你的 Notion 已經有正式的紀錄，請 AI 另外建一個名稱加上「（測試）」的頁面。
- **讓 AI 誠實回報**：做不到、讀不到、說明跟實際不一樣的地方，都要它說出來，最後整理成「範本問題清單」。

## 共通的測試指令

每個平台開新對話後，先貼這段（後面各平台會再補充）：

```
請讀 https://raw.githubusercontent.com/xs04/health-coach-kit/main/AGENTS.md ，照裡面的流程幫我設定。開始前先引用這份文件的第一行，讓我確認你真的讀到了。

（測試用）如果我的 Notion 已經有同名的頁面，那是正式資料，不要動它。請另外建一個名稱加上「（測試）」的頁面，所有東西都建在這底下。
如果你讀不到檔案，或有步驟做不到，請直接告訴我，不要自己猜。
最後請整理一份「範本問題清單」給我。
```

**讀不到網址時的備案**（例如 repo 還是私人的）：到 GitHub 按 **Code → Download ZIP**，解壓後照各平台的說明上傳檔案。

---

## 一、Claude

| 情境 | 做法 |
|---|---|
| A. 一般聊天（模擬一般朋友） | 確認 Notion 連線有開，貼上共通的測試指令。讀不到：用對話框的「＋」附加 GitHub repo，或上傳 `dist/health-coach-kit.skill` 再試 |
| B. 安裝 Skill | 上傳 `dist/health-coach-kit.skill`，開新對話說「我想開始記錄飲食，這次是測試，Notion 請建在名稱加上（測試）的頁面」 |
| C. Claude Code（實測過的方式） | 手機 Claude App 的 **Code** 或 claude.ai/code，選這個 repo 開新的工作階段，貼上共通的測試指令 |

---

## 二、ChatGPT（⚠️ 範本未實測）

1. 開新對話，**先在對話框的「＋」選取 Notion**（ChatGPT 不會自動開啟，也不會提醒），再貼上共通的測試指令，補一段：

```
開始前請先照 AGENTS.md 階段 0，誠實告訴我你能不能：讀寫 Notion、設定排程、執行 Python、讀圖片。做不到的部分改用 platforms/chatgpt.md 的替代做法。
```

   想測 AI 會不會主動提醒：故意**不選** Notion，看它有沒有照 platforms/chatgpt.md 教你開啟，而不是直接改用 CSV。

2. **讀不到網址時**：建立一個**專案（Project）**，上傳這些檔案：
   - `AGENTS.md`、`safety.md`
   - `onboarding/questions.md`、`notion/schema.md`
   - `prompts/nightly-checkin.md`、`prompts/weekly-report.md`
   - `platforms/chatgpt.md`
   - `weekly-card/` 的 `template.html`、`build_html.py`、`sample.json`、`SPEC.md`、`MASCOT.md`

   專案說明貼上：「照 AGENTS.md 和 safety.md 協助我。我用的是 ChatGPT，平台細節看 platforms/chatgpt.md。」然後在專案裡開新對話，貼上同樣的測試指令。

---

## 三、Gemini（⚠️ 範本未實測）

1. 開新對話，貼上共通的測試指令，再補一段：

```
開始前請先照 AGENTS.md 階段 0，誠實告訴我你能不能：連接 Notion 或 Google 試算表、設定排程動作、執行 Python、讀圖片。做不到的部分改用 platforms/gemini.md 的替代做法。紀錄如果用 Google 試算表，請建一份名稱加上「（測試）」的新檔案。
```

2. **讀不到網址時**：建立一個 **Gem**，知識檔案上傳上面 ChatGPT 列的那些檔案（`platforms/chatgpt.md` 換成 `platforms/gemini.md`）。指示貼上：「照 AGENTS.md 和 safety.md 協助我。我用的是 Gemini App，平台細節看 platforms/gemini.md。」然後開啟這個 Gem，貼上同樣的測試指令。

---

## 測試檢查表

| 項目 | 看什麼 |
|---|---|
| 讀取方式 | 用哪一種方式讀到的？貼網址、附加 repo，還是上傳檔案？ |
| 讀取確認 | AI 有沒有正確引用 AGENTS.md 的第一行？有沒有照連結去讀 `safety.md` 等其他檔案？ |
| 能力檢查 | 階段 0 的結果是否誠實？（ChatGPT、Gemini 最需要確認）連線沒開時，有沒有先教你怎麼開，而不是直接放棄？ |
| 問卷 | 題目會不會太多、順序順不順 |
| 目標和菜單 | 算出來的數字合不合理 |
| 紀錄位置 | 有沒有建在「（測試）」底下、欄位對不對 |
| 每晚確認 | 建好後有沒有立刻試跑一次 |
| 主動性 | 有沒有變成被動（「你告訴我我再記」「排程還沒啟用」然後就停下來）？Notion 已有資料時，有沒有照樣把排程、週報、吉祥物設定完？ |
| 完成檢查表 | 說「設定完成」之前，有沒有列出 AGENTS.md 階段 7 的檢查表，而且每項都完成或有交代？ |
| 吉祥物 | 有沒有問你想要什麼吉祥物？拍寵物照片後畫得像不像？有沒有先給你看、確認後才存？ |
| 週報 | 是不是用 `template.html` 產生（不是圖片生成）？手機直式？有沒有出現 SPEC.md 禁止的東西（睡眠、壓力、喝水、趨勢圖、下週建議、照片風格）？範例圖有沒有說明是假資料？ |

## 回報

把每個平台的「範本問題清單」，加上自己覺得卡住的地方，交給範本維護者修改。
