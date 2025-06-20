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
    # 匹配模式：(X卷,XXX分)- 题目名称（语言信息）.html
    match = re.search(r'\([ABCE]卷,\d+分\)\s*-\s*(.+?)（', line)
    if match:
        problem_name = match.group(1).strip()
        problem_names.append(problem_name)

# 统计
total_files = len(lines)
unique_problems = list(set(problem_names))
unique_problems.sort()
unique_count = len(unique_problems)
duplicate_count = total_files - unique_count

# 统计每个题目出现的次数
problem_counter = Counter(problem_names)
duplicated_problems = {name: count for name, count in problem_counter.items() if count > 1}

print(f"总HTML文件数: {total_files}")
print(f"去重后题目数: {unique_count}")
print(f"重复文件数: {duplicate_count}")
print(f"有重复的题目数: {len(duplicated_problems)}")
print()

print("重复次数最多的前10个题目:")
for name, count in sorted(duplicated_problems.items(), key=lambda x: x[1], reverse=True)[:10]:
    print(f"- {name}: {count}次")
print()

print("前20个去重后的题目:")
for i, problem in enumerate(unique_problems[:20], 1):
    print(f"{i:2d}. {problem}")

# 保存去重后的题目列表
with open('d:\\华为机考od2025\\unique_problems.txt', 'w', encoding='utf-8') as f:
    for problem in unique_problems:
        f.write(problem + '\n')

print(f"\n去重后的完整题目列表已保存到: unique_problems.txt")

# 按卷分类统计
volume_stats = {'A卷': 0, 'B卷': 0, 'C卷': 0, 'E卷': 0}
for line in lines:
    for volume in volume_stats.keys():
        if f'({volume},' in line:
            volume_stats[volume] += 1
            break

print("\n按卷分类统计:")
for volume, count in volume_stats.items():
    print(f"{volume}: {count}个文件")