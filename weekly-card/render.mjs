// 把週報資料（JSON）套進 template.html，輸出寬 1080、高度依內容的 PNG。
// 用法：node render.mjs <data.json> <輸出.png>
// 需要 Playwright（雲端環境已預裝；本機可用 npx playwright 或改用 executablePath）。

import { readFile } from "node:fs/promises";
import { fileURLToPath, pathToFileURL } from "node:url";
import path from "node:path";

const here = path.dirname(fileURLToPath(import.meta.url));
const [dataPath, outPath] = process.argv.slice(2);
if (!dataPath || !outPath) {
  console.error("用法：node render.mjs <data.json> <輸出.png>");
  process.exit(1);
}

// 找 Playwright：PW_MODULE 指定的路徑 → 專案內安裝的 → 全域安裝的（npm root -g）
async function loadPlaywright() {
  const candidates = [process.env.PW_MODULE, "playwright"].filter(Boolean);
  try {
    const { execSync } = await import("node:child_process");
    const globalRoot = execSync("npm root -g", { encoding: "utf8" }).trim();
    candidates.push(pathToFileURL(path.join(globalRoot, "playwright", "index.mjs")).href);
  } catch { /* 沒有 npm 就略過 */ }
  for (const c of candidates) {
    try { return await import(c); } catch { /* 試下一個 */ }
  }
  console.error("找不到 Playwright。請先執行：npm i playwright && npx playwright install chromium");
  console.error("或改用：python build_html.py <data.json> <輸出.html>（不需要瀏覽器自動化）");
  process.exit(1);
}
const pw = await loadPlaywright();
const { chromium } = pw.default ?? pw;

const data = JSON.parse(await readFile(dataPath, "utf8"));
const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 1080, height: 1350 }, deviceScaleFactor: 1 });
await page.addInitScript((d) => { window.CARD_DATA = d; }, data);
await page.goto(pathToFileURL(path.join(here, "template.html")).href);
await page.waitForLoadState("networkidle");
await page.locator("#card").screenshot({ path: outPath });
await browser.close();
console.log(`已輸出 ${outPath}`);
