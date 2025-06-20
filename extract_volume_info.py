import os
import re
from collections import defaultdict

def extract_volume_and_problems():
    """
    从all_html_files.txt中提取题目名称和卷别信息
    """
    volume_problems = defaultdict(list)
    all_problems = []
    
    with open('all_html_files.txt', 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            
            # 提取卷别信息 (A卷、B卷、C卷、D卷、E卷)
            volume_match = re.search(r'[ABCDE]卷', line)
            volume = volume_match.group() if volume_match else '未知卷'
            
            # 提取题目名称
            # 匹配模式：卷别_题目名称_分数_语言.html
            problem_match = re.search(r'[ABCDE]卷[_-]([^_-]+)[_-]\d+分', line)
            if not problem_match:
                # 备用匹配模式
                problem_match = re.search(r'([^/\\]+)\.html$', line)
                if problem_match:
                    problem_name = problem_match.group(1)
                    # 清理文件名中的卷别、分数、语言信息
                    problem_name = re.sub(r'[ABCDE]卷[_-]?', '', problem_name)
                    problem_name = re.sub(r'[_-]?\d+分[_-]?', '', problem_name)
                    problem_name = re.sub(r'[_-]?(java|python|javascript|cpp|c)$', '', problem_name, flags=re.IGNORECASE)
                else:
                    continue
            else:
                problem_name = problem_match.group(1)
            
            # 清理题目名称
            problem_name = problem_name.strip('_-')
            
            if problem_name and problem_name not in [p['name'] for p in all_problems]:
                problem_info = {
                    'name': problem_name,
                    'volume': volume,
                    'file_path': line
                }
                all_problems.append(problem_info)
                volume_problems[volume].append(problem_name)
    
    return all_problems, volume_problems

def analyze_volume_focus():
    """
    分析各卷的侧重考察点
    """
    volume_analysis = {
        'A卷': {
            'focus': ['基础数据结构', '数组操作', '字符串处理', '简单算法'],
            'description': 'A卷主要考察基础算法和数据结构，适合入门级考生，题目相对简单，注重基本功的掌握。'
        },
        'B卷': {
            'focus': ['动态规划', '贪心算法', '数学计算', '模拟题'],
            'description': 'B卷难度适中，开始涉及一些经典算法思想，如动态规划和贪心，需要一定的算法基础。'
        },
        'C卷': {
            'focus': ['图论算法', '搜索算法', '复杂数据结构', '综合应用'],
            'description': 'C卷难度较高，涉及图论、搜索等复杂算法，需要较强的算法思维和编程能力。'
        },
        'D卷': {
            'focus': ['高级算法', '优化问题', '复杂逻辑', '系统设计'],
            'description': 'D卷为高难度题目，考察高级算法和复杂问题的解决能力。'
        },
        'E卷': {
            'focus': ['综合算法', '实际应用', '性能优化', '创新思维'],
            'description': 'E卷题目最多，涵盖各种难度和类型，从基础到高级都有，是主要的考试内容。'
        }
    }
    return volume_analysis

def calculate_knowledge_probability(all_problems):
    """
    计算各知识点的考察概率
    """
    # 根据题目名称推断算法类型
    algorithm_keywords = {
        '数组': ['数组', '矩阵', '排序', '查找'],
        '字符串': ['字符串', '单词', '文本', '编码', '解码'],
        '树': ['二叉树', '树', '哈夫曼', '目录'],
        '图论': ['迷宫', '路径', '网络', '连通'],
        '动态规划': ['背包', '最优', '计数', '路径'],
        '贪心': ['最大', '最小', '最优', '贪心'],
        '数学': ['计算', '数字', '统计', '概率'],
        '模拟': ['模拟', '游戏', '任务', '调度'],
        '搜索': ['搜索', 'BFS', 'DFS', '遍历'],
        '栈队列': ['栈', '队列', '括号', '表达式']
    }
    
    knowledge_count = defaultdict(int)
    total_problems = len(all_problems)
    
    for problem in all_problems:
        problem_name = problem['name']
        for knowledge, keywords in algorithm_keywords.items():
            if any(keyword in problem_name for keyword in keywords):
                knowledge_count[knowledge] += 1
    
    # 计算概率
    knowledge_probability = {}
    for knowledge, count in knowledge_count.items():
        probability = (count / total_problems) * 100
        knowledge_probability[knowledge] = {
            'count': count,
            'probability': round(probability, 1)
        }
    
    return knowledge_probability

if __name__ == '__main__':
    print("正在分析题目和卷别信息...")
    all_problems, volume_problems = extract_volume_and_problems()
    
    print(f"\n总共找到 {len(all_problems)} 个独特题目")
    
    print("\n各卷题目数量:")
    for volume, problems in volume_problems.items():
        print(f"{volume}: {len(problems)} 题")
    
    print("\n各卷侧重考察点分析:")
    volume_analysis = analyze_volume_focus()
    for volume, analysis in volume_analysis.items():
        if volume in volume_problems:
            print(f"\n{volume} ({len(volume_problems[volume])}题):")
            print(f"  侧重点: {', '.join(analysis['focus'])}")
            print(f"  描述: {analysis['description']}")
    
    print("\n知识点考察概率分析:")
    knowledge_prob = calculate_knowledge_probability(all_problems)
    for knowledge, data in sorted(knowledge_prob.items(), key=lambda x: x[1]['probability'], reverse=True):
        print(f"{knowledge}: {data['count']}题 ({data['probability']}%)")
    
    # 保存详细信息到文件
    with open('volume_analysis.txt', 'w', encoding='utf-8') as f:
        f.write("华为机考OD2025题目卷别分析\n")
        f.write("=" * 50 + "\n\n")
        
        f.write("各卷题目列表:\n")
        for volume, problems in volume_problems.items():
            f.write(f"\n{volume} ({len(problems)}题):\n")
            for i, problem in enumerate(problems, 1):
                f.write(f"{i:3d}. {problem}\n")
        
        f.write("\n\n各卷侧重考察点:\n")
        for volume, analysis in volume_analysis.items():
            if volume in volume_problems:
                f.write(f"\n{volume}:\n")
                f.write(f"  题目数量: {len(volume_problems[volume])}\n")
                f.write(f"  侧重点: {', '.join(analysis['focus'])}\n")
                f.write(f"  描述: {analysis['description']}\n")
        
        f.write("\n\n知识点考察概率:\n")
        for knowledge, data in sorted(knowledge_prob.items(), key=lambda x: x[1]['probability'], reverse=True):
            f.write(f"{knowledge}: {data['count']}题 ({data['probability']}%)\n")
    
    print("\n详细分析已保存到 volume_analysis.txt")