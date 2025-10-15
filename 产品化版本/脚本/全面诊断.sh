#!/bin/bash
echo "🔍 【全面系统诊断报告】"
echo "========================"
echo "诊断时间: $(date)"
echo ""

echo "📁 1. 文件系统状态:"
echo "------------------"
echo "当前目录: $(pwd)"
echo "总文件数: $(find . -name "*.py" -o -name "*.sh" -o -name "*.md" | grep -v backup | wc -l) 个"
echo "目录结构:"
ls -la
echo ""

echo "🔧 2. Git状态检查:"
echo "----------------"
git status
echo ""

echo "🌐 3. 远程连接状态:"
echo "-----------------"
git remote -v
ssh -T git@github.com
echo ""

echo "📊 4. 提交历史:"
echo "-------------"
git log --oneline -5
echo ""

echo "🔄 5. 本地与远程差异:"
echo "------------------"
git fetch origin
git status -uno
echo ""

echo "💾 6. 关键文件检查:"
echo "-----------------"
echo "重要脚本文件:"
ls -la *.sh *.py 2>/dev/null | head -10
echo ""

echo "📋 7. 问题诊断:"
echo "-------------"
if git status | grep -q "nothing to commit"; then
    echo "✅ 工作区干净"
else
    echo "🔄 工作区有未提交更改"
fi

if git status | grep -q "Your branch is up to date"; then
    echo "✅ 分支与远程同步"
else
    echo "🔄 分支需要与远程同步"
fi

echo ""
echo "🎯 【诊断完成】"
echo "请将以上完整输出复制给助手分析"
