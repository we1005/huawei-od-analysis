import re

# 测试字符串
test_string = "- **[称砝码](ABCD卷/A卷/(A卷,100分)- 称砝码（Java & JS & Python）.html)** - 多重背包入门"

# 测试不同的正则表达式
patterns = [
    r'- \*\*\[([^\]]+)\]\([^)]+\)\*\* - ',
    r'- \*\*\[([^\]]+)\]\([^)]+\)\*\* -',
    r'- \*\*\[.*?\]\(.*?\.html\)\*\* -',
    r'- \*\*\[.*?\]\(.*?\.html\)\*\* - '
]

for i, pattern in enumerate(patterns):
    matches = re.findall(pattern, test_string)
    print(f"Pattern {i+1}: {pattern}")
    print(f"Matches: {len(matches)}")
    if matches:
        print(f"Found: {matches}")
    print()