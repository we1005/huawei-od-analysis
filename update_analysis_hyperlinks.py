import os
import re

def find_html_files():
    """查找所有HTML文件并建立题目名称到路径的映射"""
    html_files = {}
    
    # 遍历所有子目录
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file).replace('\\', '/')
                if file_path.startswith('./'):
                    file_path = file_path[2:]
                
                # 从文件名中提取题目名称
                # 匹配模式：(卷,分数)- 题目名称（语言）.html
                match = re.search(r'\([ABCDE]卷,\d+分\)[-\s]*([^（]+)', file)
                if match:
                    problem_name = match.group(1).strip()
                    # 清理题目名称
                    problem_name = re.sub(r'[\s\-_]+$', '', problem_name)
                    html_files[problem_name] = file_path
                    
                    # 添加一些常见的变体
                    if '、' in problem_name:
                        parts = problem_name.split('、')
                        for part in parts:
                            part = part.strip()
                            if part:
                                html_files[part] = file_path
    
    return html_files

def find_best_match(problem_name, html_files):
    """寻找最佳匹配的HTML文件"""
    # 直接匹配
    if problem_name in html_files:
        return html_files[problem_name]
    
    # 部分匹配
    for html_name, path in html_files.items():
        if problem_name in html_name or html_name in problem_name:
            return path
    
    # 模糊匹配（去除特殊字符后比较）
    clean_problem = re.sub(r'[^\w\u4e00-\u9fff]', '', problem_name)
    for html_name, path in html_files.items():
        clean_html = re.sub(r'[^\w\u4e00-\u9fff]', '', html_name)
        if clean_problem in clean_html or clean_html in clean_problem:
            return path
    
    return None

def update_analysis_section():
    """更新整个README文件中剩余的题目名称为超链接"""
    # 读取README文件
    with open('README.md', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 查找HTML文件
    html_files = find_html_files()
    print(f"找到 {len(html_files)} 个HTML文件")
    
    # 查找题目名称的模式：**题目名称** - 描述
    pattern = r'\*\*([^*\[]+)\*\*\s*-\s*([^\n]+)'
    
    def replace_match(match):
        problem_name = match.group(1).strip()
        description = match.group(2).strip()
        
        # 跳过一些明显不是题目名称的内容
        skip_patterns = [
            r'\d+次',  # 如：2.6次
            r'\d+题',  # 如：35题
            r'约\d+题', # 如：约35题
            r'\d+分',  # 如：100分
            r'第\d+',  # 如：第一步
            r'len/',   # 如：len/2
        ]
        
        for skip_pattern in skip_patterns:
            if re.search(skip_pattern, problem_name):
                return match.group(0)  # 保持原样
        
        # 查找对应的HTML文件
        html_path = find_best_match(problem_name, html_files)
        
        if html_path:
            return f'**[{problem_name}]({html_path})** - {description}'
        else:
            return match.group(0)  # 保持原样
    
    # 在整个文件中进行替换
    updated_content = re.sub(pattern, replace_match, content)
    
    # 写回文件
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(updated_content)
    
    # 统计替换数量
    original_matches = len(re.findall(pattern, content))
    # 修正超链接统计的正则表达式 - 匹配实际格式: - **[题目名称](路径)** - 描述
    hyperlink_pattern = r'- \*\*\[.*?\]\(.*?\.html\)\*\* - '
    updated_matches = len(re.findall(hyperlink_pattern, updated_content))
    
    print(f"整个README文件：")
    print(f"- 找到 {original_matches} 个可能的题目名称")
    print(f"- 文件中现有超链接数量: {updated_matches}")
    
    # 再次检查剩余的未转换项目
    remaining_matches = re.findall(pattern, updated_content)
    actual_remaining = []
    
    for match in remaining_matches:
        problem_name = match[0].strip()
        # 更严格的过滤条件
        skip_patterns = [
            r'\d+次',  # 如：2.6次
            r'\d+题',  # 如：35题
            r'约\d+题', # 如：约35题
            r'\d+分',  # 如：100分
            r'第\d+',  # 如：第一步
            r'len/',   # 如：len/2
            r'^[A-Z]\w*$',  # 单个英文单词
            r'问题系列$',  # 以"问题系列"结尾
            r'相关.*操作$',  # 以"相关...操作"结尾
            r'类问题$',    # 以"类问题"结尾
            r'变种$',      # 以"变种"结尾
            r'相关$',      # 以"相关"结尾
            r'求解$',      # 以"求解"结尾
            r'问题$',      # 以"问题"结尾
        ]
        
        is_skip = False
        for skip_pattern in skip_patterns:
            if re.search(skip_pattern, problem_name):
                is_skip = True
                break
        
        if not is_skip:
            actual_remaining.append(match)
    
    print(f"- 剩余需要处理的题目: {len(actual_remaining)} 个")
    
    if actual_remaining:
        print("剩余需要处理的题目：")
        for i, match in enumerate(actual_remaining[:10]):  # 只显示前10个
            print(f"  {i+1}. {match[0]}")

if __name__ == '__main__':
    update_analysis_section()
    print("算法知识点详细分析部分的超链接更新完成！")