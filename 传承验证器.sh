#!/bin/bash
echo "🔍 传承完整性验证"
echo "=================="

# 检查核心文档
核心文档="传承宪法.md AI传承宝典.md 终极传承修复指南.md"
for 文档 in $核心文档; do
    if [ -f "$文档" ]; then
        echo "✅ $文档 - 存在"
    else
        echo "❌ $文档 - 缺失！需要修复"
    fi
done

# 检查最近提交
echo "最近提交:"
git log --oneline -3 2>/dev/null || echo "Git历史获取失败"

echo "🎯 如果所有✅都存在，传承系统完整！"
