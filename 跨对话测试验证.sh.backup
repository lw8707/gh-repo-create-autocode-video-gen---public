#!/bin/bash
echo "🧪 跨对话测试验证系统"
echo "===================="

# 验证核心文件存在
echo "🔍 检查核心文件..."
必须文件=("新对话标准提示词.txt" "新对话立即上手指南.md" "一键上传.sh" "全面诊断.sh")
for 文件 in "${必须文件[@]}"; do
    if [ -f "$文件" ]; then
        echo "✅ $文件 - 存在"
    else
        echo "❌ $文件 - 缺失"
    fi
done

# 验证GitHub连接
echo ""
echo "🌐 验证GitHub连接..."
git remote -v
ssh -T git@github.com

# 显示最新状态
echo ""
echo "📊 最新提交:"
git log --oneline -3

echo ""
echo "🎯 测试验证完成!"
echo "💡 新对话请使用: cat 新对话标准提示词.txt"
