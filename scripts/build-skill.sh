#!/usr/bin/env sh
# 從目前的 commit 打包 Claude Skill：dist/health-coach-kit.skill
# .skill 就是 zip，裡面是 health-coach-kit/SKILL.md 和其他範本檔案。
# 排除的檔案寫在 .gitattributes（export-ignore），例如 dist/、scripts/、TESTING.md。
# 修改範本並 commit 之後執行一次，再把產生的檔案 commit 進來。
set -e
cd "$(dirname "$0")/.."
python3 scripts/build_bundle.py --check   # 合併版要先更新並 commit
mkdir -p dist
git archive --format=zip --prefix=health-coach-kit/ -o dist/health-coach-kit.skill HEAD
echo "已輸出 dist/health-coach-kit.skill（來源 commit：$(git rev-parse --short HEAD)）"
