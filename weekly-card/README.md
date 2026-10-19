# 週報圖

> **內容規格見 [SPEC.md](SPEC.md)（必須遵守）**：只能用這個範本產生、手機直式、只放規定的區塊。

| 檔案 | 用途 |
|---|---|
| `template.html` | 版面、配色、伯恩山插畫、運動圖示（全部是內嵌 SVG，不需要網路或圖片檔） |
| `render.mjs` | Node＋Playwright：JSON → PNG |
| `build_html.py` | 只用 Python 標準函式庫：JSON → 獨立 HTML（開啟後截圖）；有 Python 版 Playwright 可加 `--png` 直接出圖 |
| `make_link.py` | JSON → 線上檢視連結（給沒有範本檔案的環境，例如 ChatGPT） |
| `sample.json` | 範例資料（**虛構人物**） |
| `preview.png` | 範例圖 |
| `SPEC.md` | 圖卡規格：能放什麼、禁止什麼、傳出前的檢查表 |
| `MASCOT.md` | 吉祥物的規格，以及跟使用者決定吉祥物的流程 |

```bash
# Node（需要 playwright 套件和 Chromium）
node render.mjs sample.json out.png

# Python
python build_html.py sample.json out.html
python build_html.py sample.json out.html --png out.png   # 需要 Python 版 Playwright
```

### 線上檢視

`template.html` 也可以直接在瀏覽器打開：

| 網址 | 結果 |
|---|---|
| `https://xs04.github.io/health-coach-kit/weekly-card/template.html#d=<資料>` | 直接顯示週報（`make_link.py` 產生） |
| `https://xs04.github.io/health-coach-kit/weekly-card/template.html` | 顯示輸入框，貼上 JSON 按「產生」 |

資料在 `#` 後面，不會送到伺服器。需要 repo 公開並開啟 GitHub Pages（Settings → Pages → Deploy from a branch → `main`／`/ (root)`）。

圖片寬 1080 px，高度依內容自動調整（大約 1,700–1,800 px）。

> 產圖的環境要有**中文字型**（例如 Noto Sans TC、思源黑體、文泉驛），否則中文會變成方框。產生後先看一次圖，出現方框就安裝字型，或改用 `build_html.py` 讓使用者在自己的瀏覽器開啟。

## 資料格式

```jsonc
{
  "week": { "label": "W01", "start": "1/04（六）", "end": "1/10（五）" },
  "proteinTarget": 100,                       // 每日蛋白質達標門檻（g）
  "training": { "done": 3, "planned": 4, "minutes": 190 },
  "days": [                                   // 7 列
    {
      "weekday": "六", "date": "1/04",
      "workout": "健身＋跑步",                // 健身/游泳/教練課/跑步/走路/伸展/休息，其他名稱顯示星星
      "status": "done",                       // done | swap | skip | rest
      "b": { "t": "蛋餅＋豆漿" },             // 早餐；"off": true 表示和菜單不同（顯示棕色）
      "l": { "t": "雞腿便當" },               // 午餐
      "d": { "t": "—" },                      // 晚餐；沒紀錄用 "—"
      "kcal": 1980,                           // 沒資料用 null
      "kcalTarget": [1900, 2100],             // 當天熱量達標區間
      "protein": 104                          // 沒資料用 null
    }
  ],
  "stats": [                                  // 3 格
    { "label": "平均蛋白質", "value": "101", "unit": "g／天",
      "sub": "（選填）", "target": "100 g 以上",
      "gap": "✓ 多 1 g・4／6 天達標", "tone": "good" }   // tone: good=綠, bad=紅
  ],
  "rules": ["熱量：……", "蛋白質：……"],      // 灰色小字，每條一行；「標題：內容」的標題會加粗
  "review": [ { "type": "good", "text": "……" }, { "type": "fix", "text": "……" } ],
  "mascot": { "lift": "…", "peek": "…" },     // 選填；省略＝預設伯恩山，"none"＝不放。見 MASCOT.md
  "footer": "第 1 週・紀錄 6／7 天",
  "footerRight": ""                           // 頁尾右側（選填）
}
```

## 想改外觀

- 顏色：`template.html` 開頭的 `:root` 變數
- 運動圖示：`<g id="ic-…">`，24×24 的 SVG；新增種類要同時改 `ICONS` 對照表
- 吉祥物：不用改範本，在資料裡給 `mascot` 就能換，見 [MASCOT.md](MASCOT.md)
