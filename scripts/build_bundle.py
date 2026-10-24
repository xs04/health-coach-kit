#!/usr/bin/env python3
"""把設定流程需要的文件合併成一份 ALL-IN-ONE.md。

有些 AI（例如 ChatGPT）只能開使用者貼的網址，不能自己去開 AGENTS.md 裡提到的其他檔案。
合併成一份之後，使用者只要貼一個網址，AI 就能讀到全部內容。

用法：
  python3 scripts/build_bundle.py          # 重新產生
  python3 scripts/build_bundle.py --check  # 檢查是否和來源一致（不一致就回傳 1）
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "ALL-IN-ONE.md"

# 順序就是 AI 閱讀的順序：先流程和安全規則，再細節
FILES = [
    "AGENTS.md",
    "safety.md",
    "onboarding/questions.md",
    "notion/schema.md",
    "prompts/nightly-checkin.md",
    "prompts/weekly-report.md",
    "weekly-card/SPEC.md",
    "weekly-card/README.md",
    "weekly-card/MASCOT.md",
    "platforms/chatgpt.md",
    "platforms/gemini.md",
    "platforms/claude.md",
]

HEADER = """# health-coach-kit 合併版（ALL-IN-ONE）

> 給 AI：這份檔案是下面這些檔案的**完整合併版**，內容和個別檔案相同，由程式自動產生。
> 文件裡提到其他檔案（例如 `safety.md`、`onboarding/questions.md`）時，**直接在這份檔案裡找「檔案：路徑」那一段**，不需要再開其他網址。
> 例外：產生週報圖要用的 `weekly-card/template.html` 不在這裡，請照 `weekly-card/SPEC.md` 的「線上檢視」。
> 從「檔案：AGENTS.md」開始，照 AGENTS.md 的流程進行。

包含的檔案：
{toc}
"""


def build() -> str:
    toc = "\n".join(f"- {f}" for f in FILES)
    parts = [HEADER.format(toc=toc)]
    for f in FILES:
        body = (ROOT / f).read_text(encoding="utf-8").rstrip()
        parts.append(f"\n\n---\n\n<!-- ===== 檔案：{f} ===== -->\n\n## 檔案：{f}\n\n{body}\n")
    return "".join(parts)


if __name__ == "__main__":
    text = build()
    if "--check" in sys.argv:
        if not OUT.exists() or OUT.read_text(encoding="utf-8") != text:
            raise SystemExit("ALL-IN-ONE.md 和來源不一致，請執行 python3 scripts/build_bundle.py")
        print("ALL-IN-ONE.md 是最新的")
    else:
        OUT.write_text(text, encoding="utf-8")
        print(f"已輸出 {OUT.name}（{len(text.encode('utf-8')):,} bytes）")
