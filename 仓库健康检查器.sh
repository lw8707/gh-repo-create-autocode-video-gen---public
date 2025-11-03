#!/bin/bash
echo "🔍 GitHub仓库健康检查"
echo "========================"

echo "1. 当前仓库状态:"
git remote -v
echo ""

echo "2. SSH认证测试:"
ssh -T git@github.com
echo ""

echo "3. 仓库同步状态:"
git status --short
echo ""

echo "4. 最近提交记录:"
git log --oneline -5
echo ""

echo "✅ 如果SSH认证成功且git status正常，您的仓库是安全的！"
echo "📌 GitHub个人免费仓库不会自动删除，请放心。"
