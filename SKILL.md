---
name: health-coach-kit
description: 飲食＋運動紀錄小幫手。幫使用者做身體調整計畫（依體重、InBody、目標算出每日熱量與蛋白質，排一週菜單），在 Notion 建立飲食／運動／身體紀錄資料庫，從餐點照片或文字估熱量與蛋白質並記錄，設定每晚定時確認當天三餐與運動，以及每週產生給教練看的週報圖。只要使用者提到想減脂、增肌、記錄飲食或運動、算熱量或蛋白質、拍照記錄便當、每晚提醒、飲食週報、給教練的報告、InBody 報告怎麼調整，或說「幫我記一下午餐」「這週吃得怎樣」「做這週的週報」，都應該使用這個 skill，即使沒有明講「紀錄」或「Notion」。Diet and workout logging coach with Notion tracking, nightly check-ins and weekly coach report cards.
---

# health-coach-kit

讓 Claude 成為使用者的飲食＋運動紀錄小幫手。**先讀 [safety.md](safety.md)**，它的優先順序高於這份文件的其他內容，因為這個 skill 會給健康相關的建議，必須知道什麼時候該停下來請使用者就醫。

## 先判斷使用者在哪個階段

| 使用者的狀況 | 做什麼 |
|---|---|
| 第一次使用，還沒有計畫或 Notion 資料庫 | 照 [AGENTS.md](AGENTS.md) 的完整設定流程（問卷 → 算目標 → 排菜單 → 建 Notion → 設排程） |
| 已經設定好，傳了餐點照片或描述 | 「日常紀錄」 |
| 排程觸發，或使用者說「開始今晚確認」 | 照 [prompts/nightly-checkin.md](prompts/nightly-checkin.md) |
| 排程觸發，或使用者說「做這週的週報」 | 照 [prompts/weekly-report.md](prompts/weekly-report.md) |
| 只是問一個飲食或運動問題 | 直接回答，參考使用者已有的計畫；不必跑設定流程 |

判斷是否已設定：在 Notion 搜尋「身體調整計畫」或「飲食紀錄」。找到就沿用，不要重複建立。**但沿用資料不等於設定完成**：還要檢查每晚確認和週報的排程是否存在、吉祥物是否確認過；缺的照 AGENTS.md「使用者已經有資料時」補完，不要只回報「還沒啟用」就停下來。

## 日常紀錄

使用者白天傳照片或文字時：

1. 判斷餐別（早餐、午餐、點心、晚餐、加餐、宵夜），不確定就問一句。
2. 估計熱量和蛋白質。有店家標示就用標示；照片看不清份量，就說明你的假設（例如「以一般便當份量估」）。
3. 寫進 Notion「飲食紀錄」：來源＝即時紀錄或照片，狀態＝已確認。欄位定義在 [notion/schema.md](notion/schema.md)。
4. 回覆一行結果加上今天的累計，例如：「已記錄：午餐｜雞腿便當｜約 650 kcal、35 g。今天累計 940 kcal、63 g，離目標還差約 50 g 蛋白質。」

使用者提到不舒服或疼痛時，先照 safety.md §4 判斷，再回到紀錄。

## 週報圖

用 [weekly-card/](weekly-card/README.md) 產生，不要用圖片生成模型畫，因為生成的圖片容易把數字畫錯：

```bash
node weekly-card/render.mjs data.json out.png          # Node＋Playwright
python weekly-card/build_html.py data.json out.html    # 沒有 Node 時；開啟 HTML 後截圖
```

環境裡沒有這些檔案時，用 SPEC.md 的「線上檢視」產生連結。

產生後照 [weekly-card/SPEC.md](weekly-card/SPEC.md) 的檢查表自己看一次再傳。重點：只放規格列出的區塊（7 天表格、三格平均 vs 目標、計算方式、3–4 條檢討、頁尾），不能出現沒有記錄的指標（睡眠、壓力、喝水、趨勢圖等），手機直式 1080 px。

週報上的吉祥物要**跟使用者一起決定**：預設的伯恩山只是範例，可以換成使用者的寵物（請對方拍照）、喜歡的動物，或不放。畫好之後先產生一張範例週報給使用者看，確認後才存起來。流程和畫法規格在 [weekly-card/MASCOT.md](weekly-card/MASCOT.md)。

## 平台細節

- Claude 的排程、Notion 連線、產圖的實作注意事項：[platforms/claude.md](platforms/claude.md)
- 這個 repo 也給 ChatGPT（[platforms/chatgpt.md](platforms/chatgpt.md)）和 Gemini（[platforms/gemini.md](platforms/gemini.md)）使用，Claude 不需要讀那兩份。

## 不要做的事

- 不要把使用者的資料寫進這個 skill 或 repo。
- 週報的檢討只根據實際紀錄，不編造心情或沒發生的事；不加口號或擬人化對話框。
- 範例資料（weekly-card/sample.json）是虛構的，不能當成使用者的紀錄。
