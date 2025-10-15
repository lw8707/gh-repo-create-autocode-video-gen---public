#!/bin/bash
# GitHub直接认证脚本

echo "🚀 GitHub直接认证"
echo "=================="

# 检查当前目录
if [ ! -d "我的智能体课程" ]; then
    echo "❌ 错误：请在项目根目录运行此脚本"
    echo "   当前目录: $(pwd)"
    exit 1
fi

cd "我的智能体课程"

echo "📁 当前目录: $(pwd)"
echo ""

echo "1. 检查Git状态..."
git status

echo ""
echo "2. 添加文件到Git..."
git add .

echo ""
echo "3. 提交更改..."
git commit -m "直接认证提交" || echo "⚠️ 提交可能无新更改"

echo ""
echo "4. 开始推送..."
echo "   接下来会要求输入用户名和Token"
echo "   用户名: lw8707"
echo "   密码: 粘贴你的GitHub Token"
echo ""
echo "💡 Token获取: https://github.com/settings/tokens"
echo "   确保有 repo 权限"
echo ""

git push -u origin main

if [ $? -eq 0 ]; then
    echo ""
    echo "🎉 认证成功！"
    echo "💾 代码已推送到GitHub"
else
    echo ""
    echo "❌ 认证失败"
    echo "💡 请检查Token是否正确"
fi

cd ..
