#!/usr/bin/env python3
"""把週報 JSON 轉成線上檢視連結（只用標準函式庫）。

用法：python make_link.py data.json
資料放在網址 # 後面，瀏覽器不會把這段送到伺服器。
"""
import base64
import json
import sys
from pathlib import Path

VIEWER = "https://xs04.github.io/health-coach-kit/weekly-card/template.html"


def make_link(data: dict) -> str:
    raw = json.dumps(data, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
    return VIEWER + "#d=" + base64.urlsafe_b64encode(raw).decode("ascii").rstrip("=")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("用法：python make_link.py data.json")
    print(make_link(json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))))
