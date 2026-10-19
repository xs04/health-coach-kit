# 每週週報：排程指令範本

> 給 AI：把 `{{ }}` 換成使用者的設定，整段當作排程的指令內容。
> 資料格式詳見 [weekly-card/README.md](../weekly-card/README.md)，範例是 [weekly-card/sample.json](../weekly-card/sample.json)。

---

【{{REPORT_DAY}} {{REPORT_TIME}} 週報】

1. 範圍：{{RANGE_RULE}}（例如：上週六到昨天，共 7 天），時區 {{TIMEZONE}}。
2. 從 Notion 讀資料：運動紀錄（{{WORKOUT_DB}}）、飲食紀錄（{{FOOD_DB}}）、身體紀錄（{{BODY_DB}}），以及「週報設定」（{{SETTINGS_PAGE}}）裡的吉祥物。
3. 照 weekly-card/README.md 的格式組出 JSON：
   - days：7 天，順序 {{DAY_ORDER}}。
     - workout 只能用：健身、游泳、教練課、跑步、走路、伸展、休息（「健身房」寫成「健身」）；兩種以上用「＋」連接。
     - status：done＝照計畫完成、swap＝有做但項目不同、skip＝計畫要練但沒練、rest＝休息日。運動計畫：{{WEEKLY_WORKOUT_PLAN}}。
     - b、l、d：早午晚的簡短名稱，9 字以內；和菜單不同加 `"off": true`；沒紀錄填 `{"t":"—"}`。
     - kcal、protein：當天合計，沒資料填 null。
     - kcalTarget：休息日 {{KCAL_REST_ARRAY}}、運動日 {{KCAL_TRAIN_ARRAY}}。
   - proteinTarget：{{PROTEIN_TARGET}}
   - stats 三格，每格都要有 target、gap、tone（good 或 bad）：
     - 平均蛋白質：gap 例如「✓ 多 8 g・5／7 天達標」
     - 平均熱量：target＝7 天每日目標區間的平均（下限、上限各自平均，四捨五入到 10）；sub 寫「照菜單吃 X%」
     - 腰圍或體重：有資料才放，沒有就改成「紀錄天數 X／7」
   - rules：灰色小字的計算方式，寫出熱量、蛋白質、運動、腰圍的達標規則，最後一行「熱量與蛋白質為估計值」。
   - review：本週檢討 3–4 條，type 為 good 或 fix，每條 26 字以內，**只根據實際紀錄**，要具體對應表格中的日期和數字。
   - mascot：照「週報設定」帶入（`"default"` 就省略這個欄位；`"none"` 或 `{lift, peek}` 照原樣放）。格式見 weekly-card/MASCOT.md。
   - footer：「第 N 週」，從 {{START_DATE}} 那週算第 1 週；紀錄少於 7 天時加上「紀錄 X／7 天」。
   - **不要**加對話框、口號、擬人化的句子；**不要**放病史、腸胃狀況、檢驗數值和真實姓名。
4. 產生圖片：
   - 能跑 Node＋Playwright：`node weekly-card/render.mjs <data.json> <out.png>`
   - 只能跑 Python：`python weekly-card/build_html.py <data.json> <out.html>`，有 Python 版 Playwright 就加 `--png <out.png>`
   - 都不能執行：用文字表格呈現同樣的內容
5. 自己看一次圖：沒有裁切、文字沒有被截斷（出現「…」就縮短後重做）、標籤沒有換行、吉祥物沒有擋到文字。
6. 傳給使用者，問檢討項目要不要修改；確認後使用者自己轉給教練。

---

## 可替換的欄位

| 欄位 | 例子 |
|---|---|
| `{{REPORT_DAY}}`、`{{REPORT_TIME}}` | 每週六、08:47 |
| `{{RANGE_RULE}}`、`{{DAY_ORDER}}` | 上週六到昨天；六日一二三四五 |
| `{{KCAL_REST_ARRAY}}`、`{{KCAL_TRAIN_ARRAY}}` | [1850, 2000]、[2100, 2300] |
| `{{START_DATE}}` | 開始紀錄的日期 |
| `{{SETTINGS_PAGE}}` | 「週報設定」頁面的 URL |
