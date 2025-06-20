# 读取所有HTML文件名
$content = Get-Content 'd:\华为机考od2025\all_html_files.txt'

# 提取题目名称（去除卷号、分数和语言信息）
$problemNames = @()
foreach ($line in $content) {
    # 使用简单的字符串分割方法
    if ($line -match '- (.+?)（') {
        $problemName = $matches[1].Trim()
        $problemNames += $problemName
    }
}

# 统计
$totalFiles = $content.Count
$uniqueProblems = $problemNames | Sort-Object -Unique
$uniqueCount = $uniqueProblems.Count
$duplicateCount = $totalFiles - $uniqueCount

Write-Host "总HTML文件数: $totalFiles"
Write-Host "去重后题目数: $uniqueCount"
Write-Host "重复文件数: $duplicateCount"
Write-Host ""
Write-Host "前20个去重后的题目:"
$uniqueProblems | Select-Object -First 20 | ForEach-Object { Write-Host "- $_" }

# 保存去重后的题目列表
$uniqueProblems | Out-File 'd:\华为机考od2025\unique_problems.txt' -Encoding UTF8
Write-Host ""
Write-Host "去重后的完整题目列表已保存到: unique_problems.txt"