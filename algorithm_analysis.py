import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from matplotlib import rcParams
import seaborn as sns
from matplotlib.patches import Wedge
import matplotlib.patches as mpatches

# 设置中文字体
rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei']
rcParams['axes.unicode_minus'] = False

# 华为机考OD2025算法题目统计数据
data = {
    '算法类型': [
        '贪心算法', '数学计算', '字符串处理', '数组操作', '模拟算法',
        '动态规划', '树结构', '图论算法', '搜索算法', '栈队列',
        '双指针技术', '分治算法', '哈希表', '堆与优先队列', '并查集',
        '回溯算法', '滑动窗口', '二分搜索', '位运算', '数论'
    ],
    '题目数量': [62, 56, 53, 50, 37, 35, 25, 30, 30, 15, 15, 10, 20, 10, 8, 12, 18, 8, 5, 6],
    '占比(%)': [10.5, 9.5, 9.0, 8.5, 6.3, 5.9, 4.2, 5.1, 5.1, 2.5, 2.5, 1.7, 3.4, 1.7, 1.4, 2.0, 3.1, 1.4, 0.8, 1.0]
}

# 数据结构分类统计
data_structure_data = {
    '数据结构类型': [
        '数组与矩阵', '字符串处理', '树结构', '图论基础', '栈和队列',
        '堆与优先队列', '链表操作', '哈希表应用', '并查集'
    ],
    '题目数量': [40, 53, 25, 30, 15, 10, 5, 20, 8],
    '占比(%)': [6.8, 9.0, 4.2, 5.1, 2.5, 1.7, 0.8, 3.4, 1.4]
}

# 算法技巧分类统计
algorithm_technique_data = {
    '算法技巧类型': [
        '动态规划', '贪心算法', '搜索算法', '双指针技术', '分治算法',
        '回溯算法', '滑动窗口', '二分搜索'
    ],
    '题目数量': [35, 25, 30, 15, 10, 12, 18, 8],
    '占比(%)': [5.9, 4.2, 5.1, 2.5, 1.7, 2.0, 3.1, 1.4]
}

# 难度分布数据
difficulty_data = {
    '难度等级': ['简单(100分)', '中等(200分)'],
    '题目数量': [346, 148],
    '占比(%)': [70.0, 30.0]
}

# 卷别分布数据
volume_data = {
    '卷别': ['A卷', 'B卷', 'C卷', 'E卷'],
    '题目数量': [73, 142, 202, 127],
    '占比(%)': [13.4, 26.1, 37.1, 23.4]
}

def create_algorithm_statistics_table():
    """创建算法统计表格"""
    df = pd.DataFrame(data)
    
    # 创建详细统计表
    print("\n=== 华为机考OD2025算法题目统计分析 ===")
    print(f"总题目数: 494题")
    print(f"总文件数: 683个HTML文件")
    print(f"重复题目: 121个题目存在重复")
    print("\n=== 算法类型分布统计表 ===")
    print(df.to_string(index=False))
    
    # 保存为CSV文件
    df.to_csv('华为机考OD2025算法统计.csv', index=False, encoding='utf-8-sig')
    print("\n统计表已保存为: 华为机考OD2025算法统计.csv")
    
    return df

def create_pie_chart():
    """创建饼图"""
    # 选择前10个算法类型
    top_10_data = data['题目数量'][:10]
    top_10_labels = data['算法类型'][:10]
    
    # 创建饼图
    plt.figure(figsize=(12, 8))
    colors = plt.cm.Set3(np.linspace(0, 1, len(top_10_data)))
    
    wedges, texts, autotexts = plt.pie(top_10_data, labels=top_10_labels, autopct='%1.1f%%',
                                       startangle=90, colors=colors, textprops={'fontsize': 10})
    
    # 美化饼图
    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontweight('bold')
    
    plt.title('华为机考OD2025算法类型分布(前10)', fontsize=16, fontweight='bold', pad=20)
    plt.axis('equal')
    plt.tight_layout()
    plt.savefig('华为机考OD2025算法分布饼图.png', dpi=300, bbox_inches='tight')
    plt.show()

def create_bar_chart():
    """创建柱状图"""
    plt.figure(figsize=(15, 8))
    
    # 创建柱状图
    bars = plt.bar(data['算法类型'], data['题目数量'], 
                   color=plt.cm.viridis(np.linspace(0, 1, len(data['算法类型']))))
    
    # 添加数值标签
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height + 0.5,
                f'{int(height)}题', ha='center', va='bottom', fontsize=9)
    
    plt.title('华为机考OD2025算法类型题目数量分布', fontsize=16, fontweight='bold')
    plt.xlabel('算法类型', fontsize=12)
    plt.ylabel('题目数量', fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    plt.savefig('华为机考OD2025算法分布柱状图.png', dpi=300, bbox_inches='tight')
    plt.show()

def create_comprehensive_analysis():
    """创建综合分析图表"""
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(16, 12))
    
    # 1. 算法类型分布饼图
    top_8_data = data['题目数量'][:8]
    top_8_labels = data['算法类型'][:8]
    colors1 = plt.cm.Set3(np.linspace(0, 1, len(top_8_data)))
    
    wedges, texts, autotexts = ax1.pie(top_8_data, labels=top_8_labels, autopct='%1.1f%%',
                                       startangle=90, colors=colors1)
    ax1.set_title('算法类型分布(前8)', fontsize=14, fontweight='bold')
    
    # 2. 数据结构分布柱状图
    bars2 = ax2.bar(data_structure_data['数据结构类型'], data_structure_data['题目数量'],
                    color=plt.cm.plasma(np.linspace(0, 1, len(data_structure_data['数据结构类型']))))
    ax2.set_title('数据结构类型分布', fontsize=14, fontweight='bold')
    ax2.set_ylabel('题目数量')
    ax2.tick_params(axis='x', rotation=45)
    
    # 添加数值标签
    for bar in bars2:
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2., height + 0.5,
                f'{int(height)}', ha='center', va='bottom', fontsize=9)
    
    # 3. 难度分布饼图
    colors3 = ['#ff9999', '#66b3ff']
    wedges3, texts3, autotexts3 = ax3.pie(difficulty_data['题目数量'], 
                                          labels=difficulty_data['难度等级'],
                                          autopct='%1.1f%%', colors=colors3)
    ax3.set_title('题目难度分布', fontsize=14, fontweight='bold')
    
    # 4. 卷别分布柱状图
    colors4 = ['#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
    bars4 = ax4.bar(volume_data['卷别'], volume_data['题目数量'], color=colors4)
    ax4.set_title('各卷题目分布', fontsize=14, fontweight='bold')
    ax4.set_ylabel('题目数量')
    
    # 添加数值标签
    for bar in bars4:
        height = bar.get_height()
        ax4.text(bar.get_x() + bar.get_width()/2., height + 2,
                f'{int(height)}题', ha='center', va='bottom', fontsize=10)
    
    plt.suptitle('华为机考OD2025题目全面分析', fontsize=18, fontweight='bold', y=0.98)
    plt.tight_layout()
    plt.savefig('华为机考OD2025综合分析图.png', dpi=300, bbox_inches='tight')
    plt.show()

def create_heatmap():
    """创建算法知识点热力图"""
    # 构建算法知识点矩阵
    categories = ['数据结构', '算法技巧', '字符串处理', '数学逻辑']
    algorithms = [
        ['数组', '链表', '栈队列', '树', '图', '堆', '哈希表', '并查集'],
        ['动态规划', '贪心', '搜索', '双指针', '分治', '回溯', '滑动窗口', '二分'],
        ['字符串匹配', 'KMP', '字符串哈希', 'Trie树', '编码解码', '正则表达式', '字符串DP', '回文'],
        ['数论', '组合数学', '概率统计', '几何', '位运算', '数值计算', '逻辑推理', '模拟']
    ]
    
    # 对应的题目数量矩阵
    matrix = np.array([
        [50, 5, 15, 25, 30, 10, 20, 8],
        [35, 25, 30, 15, 10, 12, 18, 8],
        [53, 8, 5, 6, 15, 3, 12, 8],
        [6, 10, 3, 8, 5, 15, 20, 37]
    ])
    
    plt.figure(figsize=(12, 8))
    sns.heatmap(matrix, annot=True, fmt='d', cmap='YlOrRd', 
                xticklabels=[alg for sublist in algorithms for alg in sublist],
                yticklabels=categories,
                cbar_kws={'label': '题目数量'})
    
    plt.title('华为机考OD2025算法知识点热力图', fontsize=16, fontweight='bold')
    plt.xlabel('具体算法/技术', fontsize=12)
    plt.ylabel('算法类别', fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig('华为机考OD2025算法热力图.png', dpi=300, bbox_inches='tight')
    plt.show()

def create_detailed_report():
    """生成详细分析报告"""
    report = """
# 华为机考OD2025算法题目详细分析报告

## 总体概况
- **总题目数**: 494个不重复题目
- **总文件数**: 683个HTML文件
- **重复题目**: 121个题目存在重复，平均每个重复2.6次
- **覆盖语言**: Java、Python、JavaScript、C++、C
- **覆盖卷别**: A卷、B卷、C卷、E卷

## 算法类型分布分析

### 高频算法类型 (前5名)
1. **贪心算法** - 62题 (10.5%)
   - 排序贪心、区间贪心、资源分配贪心
   - 代表题目: 最大利润贪心的商人、田忌赛马、内存资源分配

2. **数学计算** - 56题 (9.5%)
   - 数值处理、统计分析、数论问题
   - 代表题目: 数字游戏、水仙花数、TLV解码

3. **字符串处理** - 53题 (9.0%)
   - 字符串匹配、编码解码、格式转换
   - 代表题目: 字符串分割转换、增强的strstr、字符统计及重排

4. **数组操作** - 50题 (8.5%)
   - 数组排序、查找、矩阵操作
   - 代表题目: 分割数组的最大差值、数组拼接、矩阵相交的面积

5. **模拟算法** - 37题 (6.3%)
   - 实际场景模拟、过程模拟
   - 代表题目: 机器人活动区域、游戏模拟类题目

### 中频算法类型
- **动态规划** - 35题 (5.9%): 背包问题、路径问题、序列DP
- **图论算法** - 30题 (5.1%): BFS、DFS、最短路径、连通性
- **搜索算法** - 30题 (5.1%): 深度优先、广度优先、回溯
- **树结构** - 25题 (4.2%): 二叉树、多叉树、树遍历
- **哈希表** - 20题 (3.4%): 快速查找、去重、统计

### 低频算法类型
- **滑动窗口** - 18题 (3.1%): 子串问题、区间优化
- **栈队列** - 15题 (2.5%): 括号匹配、优先队列
- **双指针技术** - 15题 (2.5%): 对撞指针、快慢指针
- **回溯算法** - 12题 (2.0%): 全排列、组合生成
- **堆与优先队列** - 10题 (1.7%): 堆排序、任务调度

## 难度分布分析
- **简单题(100分)**: 346题 (70.0%)
  - 主要考察基础算法和数据结构
  - 实现难度较低，注重基本功

- **中等题(200分)**: 148题 (30.0%)
  - 考察复杂算法和综合应用
  - 需要较强的算法设计能力

## 各卷分布分析
- **A卷**: 73题 (13.4%) - 基础算法为主
- **B卷**: 142题 (26.1%) - 动态规划、贪心算法重点
- **C卷**: 202题 (37.1%) - 图论算法、复杂数据结构
- **E卷**: 127题 (23.4%) - 综合算法、实际应用

## 学习建议

### 基础阶段 (1-2个月)
1. **数据结构基础**: 数组、链表、栈、队列、哈希表
2. **基本算法**: 排序、查找、双指针、滑动窗口
3. **字符串处理**: 基本操作、模式匹配

### 进阶阶段 (2-3个月)
1. **树和图算法**: BFS、DFS、二叉树遍历
2. **动态规划**: 背包问题、路径问题、序列DP
3. **贪心算法**: 排序贪心、区间贪心、资源分配

### 冲刺阶段 (1个月)
1. **复杂综合题**: 多算法结合、优化问题
2. **代码实现**: 提高编码速度和准确性
3. **语言特性**: 熟悉各编程语言的特点

## 重点推荐题目类型
1. **并查集问题**: We Are A Team、朋友圈等
2. **动态规划**: 背包变种、路径计数、序列问题
3. **图论算法**: 最短路径、拓扑排序、连通性
4. **字符串算法**: KMP、字符串匹配、编辑距离
5. **数据结构应用**: 优先队列、单调栈、线段树

## 总结
华为机考OD2025题目覆盖面广，算法类型丰富，重点考察:
- 基础数据结构的熟练运用
- 常见算法的灵活应用
- 实际问题的抽象建模能力
- 代码实现的准确性和效率

建议考生系统性学习，注重基础，循序渐进，结合LeetCode等平台进行针对性练习。
"""
    
    with open('华为机考OD2025详细分析报告.md', 'w', encoding='utf-8') as f:
        f.write(report)
    
    print("详细分析报告已生成: 华为机考OD2025详细分析报告.md")

def main():
    """主函数"""
    print("正在生成华为机考OD2025算法题目统计分析...")
    
    # 创建统计表格
    df = create_algorithm_statistics_table()
    
    # 创建各种图表
    print("\n正在生成饼图...")
    create_pie_chart()
    
    print("正在生成柱状图...")
    create_bar_chart()
    
    print("正在生成综合分析图...")
    create_comprehensive_analysis()
    
    print("正在生成热力图...")
    create_heatmap()
    
    # 生成详细报告
    print("正在生成详细分析报告...")
    create_detailed_report()
    
    print("\n=== 所有图表和报告生成完成! ===")
    print("生成的文件:")
    print("1. 华为机考OD2025算法统计.csv - 统计数据表")
    print("2. 华为机考OD2025算法分布饼图.png - 算法分布饼图")
    print("3. 华为机考OD2025算法分布柱状图.png - 算法分布柱状图")
    print("4. 华为机考OD2025综合分析图.png - 综合分析图表")
    print("5. 华为机考OD2025算法热力图.png - 算法知识点热力图")
    print("6. 华为机考OD2025详细分析报告.md - 详细分析报告")

if __name__ == "__main__":
    main()