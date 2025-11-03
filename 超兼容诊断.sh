#!/bin/bash
echo "🔍 超兼容环境诊断器启动"
echo "=================================="

echo "1. 基础环境检查..."
pwd
echo "当前目录: $(pwd)"
ls -la | head -5
echo "当前用户: $(whoami)"

echo ""
echo "2. 关键文档检查..."
[ -f "传承宪法.md" ] && echo "✅ 传承宪法.md - 存在" || echo "❌ 传承宪法.md - 缺失"
[ -f "第25轮最终传承.md" ] && echo "✅ 第25轮最终传承.md - 存在" || echo "❌ 第25轮最终传承.md - 缺失"

echo ""
echo "3. Git状态检查..."
git status --short | head -10

echo ""
echo "4. 工具资产概览..."
find . -name "*.sh" -o -name "*.py" | wc -l | xargs echo "总脚本数量:"
find . -name "*.md" | wc -l | xargs echo "总文档数量:"

echo ""
echo "🎉 超兼容诊断完成！"
echo "如果上述命令无报错，基础环境正常。"
