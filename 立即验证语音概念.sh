#!/bin/bash
echo "🎯 立即验证语音编程概念"
echo "====================="

# 方法1：使用Termux自带功能
echo "1. 测试Termux语音API..."
if [ -x "$(command -v termux-speech-to-text)" ]; then
    echo "✅ 支持语音输入，可以直接使用"
    echo "💡 使用命令: termux-speech-to-text"
else
    echo "❌ 不支持直接语音输入，使用方案2"
fi

# 方法2：使用Python输入模拟
echo ""
echo "2. 启动文本模拟语音系统..."
python3 简单语音输入.py

# 方法3：增强菜单系统
echo ""
echo "3. 启动增强菜单系统..."
python3 增强文本交互.py

echo ""
echo "🎉 概念验证完成!"
echo "📝 下一步: 基于验证结果选择技术路线"
