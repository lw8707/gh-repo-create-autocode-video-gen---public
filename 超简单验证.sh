#!/bin/bash
echo "✅ 超简单验证 - 只使用基本命令"
echo "=================================="

echo "1. 基础状态:"
pwd
ls

echo ""
echo "2. Git状态:"
git status

echo ""
echo "3. 关键文件:"
[ -f "第28轮完整传承.md" ] && echo "✅ 第28轮完整传承.md" || echo "❌ 第28轮完整传承.md"
[ -f "传承宪法.md" ] && echo "✅ 传承宪法.md" || echo "❌ 传承宪法.md"

echo ""
echo "🎯 验证完成！按q退出分页"
