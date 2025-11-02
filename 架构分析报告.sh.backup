#!/bin/bash
echo "🏗️ 项目架构分析报告 - 第21轮"
echo "=========================="

# 分析脚本分布
echo "=== 脚本文件分析 ==="
echo "总脚本数: $(find . -name "*.sh" | wc -l)"
echo "核心脚本: $(find . -name "*.sh" -exec grep -l "核心\\|核心功能\\|main" {} \; | wc -l)"
echo "工具脚本: $(find . -name "*.sh" -exec grep -l "工具\\|utility" {} \; | wc -l)"

# 分析文件类型分布
echo "=== 文件类型分布 ==="
echo "Shell脚本: $(find . -name "*.sh" | wc -l)"
echo "Python脚本: $(find . -name "*.py" | wc -l)"
echo "文档文件: $(find . -name "*.md" | wc -l)"
echo "配置文件: $(find . -name "*.json" -o -name "*.yaml" -o -name "*.yml" | wc -l)"

# 检查Git状态
echo "=== Git仓库状态 ==="
git remote -v
git log --oneline -5
echo "最近提交: $(git log -1 --format=%cd --date=relative)"
