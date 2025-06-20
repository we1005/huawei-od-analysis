import os
import re
from pathlib import Path

def find_html_files():
    """查找所有HTML文件并建立题目名称到文件路径的映射"""
    html_files = {}
    base_dir = Path('.')
    
    # 遍历所有子目录查找HTML文件
    for html_file in base_dir.rglob('*.html'):
        file_name = html_file.name
        # 提取题目名称（去除卷别、分数、语言信息）
        # 例如："(E卷,100分) - IPv4地址转换成整数（Java & Python& JS & C++ & C ）.html"
        match = re.search(r'\([ABCE]卷,\d+分\)\s*-\s*([^（]+)', file_name)
        if match:
            problem_name = match.group(1).strip()
            # 使用相对路径
            relative_path = str(html_file).replace('\\', '/')
            html_files[problem_name] = relative_path
            
            # 处理一些特殊的题目名称映射
            # "计算数组中心位置" -> "数组中心位置"
            if "计算数组中心位置" in problem_name:
                html_files["数组中心位置"] = relative_path
            
            # "字符串重新排列、字符串重新排序" -> "字符串重新排列"
            if "字符串重新排列、字符串重新排序" in problem_name:
                html_files["字符串重新排列"] = relative_path
            
            print(f"找到题目: {problem_name} -> {relative_path}")
    
    return html_files

def find_best_match(problem_name, html_files):
    """查找最佳匹配的HTML文件"""
    # 直接匹配
    if problem_name in html_files:
        return html_files[problem_name]
    
    # 模糊匹配：查找包含关键词的题目
    for file_problem_name, file_path in html_files.items():
        # 如果HTML文件名包含README中的题目名称
        if problem_name in file_problem_name:
            return file_path
        # 如果README中的题目名称包含HTML文件名的主要部分
        if len(file_problem_name) > 3 and file_problem_name in problem_name:
            return file_path
    
    return None

def update_readme_with_hyperlinks():
    """更新README文件，将题目名称替换为超链接"""
    # 查找所有HTML文件
    html_files = find_html_files()
    
    # 读取README文件
    with open('README.md', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 查找所有题目名称模式：**题目名称** (X卷)
    pattern = r'\*\*([^*]+)\*\*\s*\(([ABCE])卷\)'
    
    def replace_with_hyperlink(match):
        problem_name = match.group(1).strip()
        volume = match.group(2)
        
        # 查找对应的HTML文件
        file_path = find_best_match(problem_name, html_files)
        
        if file_path:
            # 创建超链接格式
            return f'**[{problem_name}]({file_path})** ({volume}卷)'
        else:
            # 如果找不到对应文件，保持原样
            print(f"警告: 未找到题目 '{problem_name}' 对应的HTML文件")
            return match.group(0)
    
    # 替换所有匹配的题目名称
    updated_content = re.sub(pattern, replace_with_hyperlink, content)
    
    # 写回README文件
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(updated_content)
    
    print("README.md 文件已更新完成！")
    
    # 统计替换情况
    matches = re.findall(pattern, content)
    print(f"\n总共处理了 {len(matches)} 个题目名称")
    
    # 显示一些统计信息
    found_count = 0
    not_found = []
    for problem_name, volume in matches:
        problem_name = problem_name.strip()
        if find_best_match(problem_name, html_files):
            found_count += 1
        else:
            not_found.append(problem_name)
    
    print(f"成功创建超链接: {found_count} 个")
    print(f"未找到对应文件: {len(not_found)} 个")
    
    if not_found:
        print("\n未找到对应文件的题目:")
        for name in not_found[:10]:  # 只显示前10个
            print(f"  - {name}")
        if len(not_found) > 10:
            print(f"  ... 还有 {len(not_found) - 10} 个")

if __name__ == '__main__':
    update_readme_with_hyperlinks()