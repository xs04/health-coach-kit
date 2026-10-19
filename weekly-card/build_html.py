"""把週報資料（JSON）套進 template.html，輸出一個「不需要瀏覽器自動化」的獨立 HTML 檔。

給不能跑 Playwright 的環境用（例如 ChatGPT 的 Python 環境）：
  python build_html.py data.json weekly.html
產生的 weekly.html 用任何瀏覽器打開就是週報，使用者截圖即可。

如果環境剛好有 Python 版 Playwright，加上 --png 會直接輸出圖片：
  python build_html.py data.json weekly.html --png weekly.png
只用 Python 標準函式庫（--png 除外）。
"""

import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent


def build(data_path: str, out_html: str) -> Path:
    data = json.loads(Path(data_path).read_text(encoding="utf-8"))
    template = (HERE / "template.html").read_text(encoding="utf-8")
    # 在範本的主程式之前注入資料（等同 render.mjs 的 addInitScript）
    # 跳脫 "</"，避免資料裡的 "</script>" 提早結束 script 標籤
    payload = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    inject = "<script>window.CARD_DATA = " + payload + ";</script>\n"
    marker = "<script>"
    idx = template.rfind(marker)
    if idx == -1:
        raise SystemExit("template.html 格式不符：找不到 <script>")
    html = template[:idx] + inject + template[idx:]
    out = Path(out_html)
    out.write_text(html, encoding="utf-8")
    return out


def screenshot(html_path: Path, png_path: str) -> None:
    from playwright.sync_api import sync_playwright  # 選用：環境沒有就不要加 --png

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 1080, "height": 1350})
        page.goto(html_path.resolve().as_uri())
        page.wait_for_load_state("networkidle")
        page.locator("#card").screenshot(path=png_path)
        browser.close()


if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) < 2:
        raise SystemExit("用法：python build_html.py <data.json> <輸出.html> [--png <輸出.png>]")
    out = build(args[0], args[1])
    print(f"已輸出 {out}")
    if "--png" in args:
        png = args[args.index("--png") + 1]
        screenshot(out, png)
        print(f"已輸出 {png}")
