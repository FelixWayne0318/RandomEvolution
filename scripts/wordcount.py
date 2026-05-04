#!/usr/bin/env python3
"""
统计 .md 文件中的中文字符数，对比预算并打印进度表。

用法:
    python scripts/wordcount.py
    python scripts/wordcount.py --total-only

预算定义在本文件 BUDGET 字典中，与 字数预算.md 同步。
"""

import argparse
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent

# 字数预算（单位：中文字符）
# (最低, 最高)
BUDGET = {
    "引言初稿.md":                          ( 6_000,  8_000),
    "第一部分_理论篇.md":                   (25_000, 35_000),
    "第二部分_应用篇/01_宇宙.md":           (10_000, 12_000),
    "第二部分_应用篇/02_生命.md":           (15_000, 15_000),
    "第二部分_应用篇/03_生态.md":           (10_000, 12_000),
    "第二部分_应用篇/04_社会.md":           (15_000, 15_000),
    "第二部分_应用篇/05_文明.md":           (15_000, 15_000),
    "第二部分_应用篇/06_经济.md":           (20_000, 25_000),
    "第二部分_应用篇/07_技术.md":           (15_000, 15_000),
    "第三部分_哲学篇.md":                   (12_000, 15_000),
    "第四部分_未来篇.md":                   (10_000, 12_000),
}

CJK_RE = re.compile(r'[一-鿿]')


def count_chinese(text: str) -> int:
    return len(CJK_RE.findall(text))


def progress_bar(ratio: float, width: int = 20) -> str:
    filled = max(0, min(width, int(ratio * width)))
    return '█' * filled + '░' * (width - filled)


def status_marker(cur: int, lo: int, hi: int) -> str:
    if cur == 0:
        return ' '
    if cur < lo * 0.3:
        return ' '
    if cur < lo:
        return ' ✏️'   # 起步
    if cur <= hi:
        return ' ✓'    # 在预算内
    if cur <= hi * 1.2:
        return ' ⚠️'   # 略超
    return ' 🔴'        # 严重超


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--total-only', action='store_true',
                        help='只输出总计行')
    args = parser.parse_args()

    rows = []
    total_cur = total_lo = total_hi = 0

    for path, (lo, hi) in BUDGET.items():
        full = REPO / path
        if not full.exists():
            cur = 0
        else:
            cur = count_chinese(full.read_text(encoding='utf-8'))
        rows.append((path, cur, lo, hi))
        total_cur += cur
        total_lo += lo
        total_hi += hi

    if not args.total_only:
        print(f"{'文件':<40} {'当前':>8}  {'最低':>8}  {'最高':>8}  进度")
        print('-' * 92)
        for path, cur, lo, hi in rows:
            ratio = cur / lo if lo > 0 else 0
            bar = progress_bar(ratio)
            marker = status_marker(cur, lo, hi)
            print(f"{path:<40} {cur:>8,}  {lo:>8,}  {hi:>8,}  {bar} {ratio*100:>5.1f}%{marker}")
        print('-' * 92)

    total_ratio = total_cur / total_lo if total_lo > 0 else 0
    bar = progress_bar(total_ratio)
    marker = status_marker(total_cur, total_lo, total_hi)
    print(f"{'合计':<40} {total_cur:>8,}  {total_lo:>8,}  {total_hi:>8,}  {bar} {total_ratio*100:>5.1f}%{marker}")
    print()
    print(f"图例:  ✏️ 起步  ✓ 在预算内  ⚠️ 略超 (超 0-20%)  🔴 严重超 (超过 20%)")


if __name__ == "__main__":
    main()
