#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
from collections import Counter

# 读取所有HTML文件名
with open('d:\\华为机考od2025\\all_html_files.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# 提取题目名称
problem_names = []
for line in lines:
    line = line.strip()
    match = re.search(r'\([ABCE]卷,\d+分\)\s*-\s*(.+?)（', line)
    if match:
        problem_name = match.group(1).strip()
        problem_names.append(problem_name)

# 统计重复
counter = Counter(problem_names)
duplicated = {name: count for name, count in counter.items() if count > 1}

print("重复次数最多的15个题目:")
for name, count in sorted(duplicated.items(), key=lambda x: x[1], reverse=True)[:15]:
    print(f"{name}: {count}次")

print(f"\n总共有 {len(duplicated)} 个题目存在重复")
print(f"平均每个重复题目出现 {sum(duplicated.values()) / len(duplicated):.1f} 次")