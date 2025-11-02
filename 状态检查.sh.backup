#!/bin/bash
echo "🔍 系统状态检查"
echo "=============="

# 检查基础文件
echo "=== 文件检查 ==="
重要文件=("重建.sh" "全面恢复.sh" "Git恢复.sh" "环境报告.md" "恢复进度.md")
for 文件 in "${重要文件[@]}"; do
    if [ -f "$文件" ]; then
        echo "✅ $文件"
    else
        echo "❌ $文件"
    fi
done

# 检查Git状态
echo "=== Git状态 ==="
if [ -d ".git" ]; then
    git status --short 2>/dev/null || echo "无变化或未提交"
    git remote -v 2>/dev/null || echo "未设置远程仓库"
else
    echo "未初始化Git"
fi

# 检查脚本权限
echo "=== 脚本权限 ==="
ls -l *.sh

echo "✅ 状态检查完成"
