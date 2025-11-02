#!/bin/bash
echo "🔧 'EOF'"
echo "================"

echo "1. 检查基础环境..."
pkg list-installed | grep -E "(python|git|curl|wget)" || {
    echo "❌ 基础环境不完整，正在修复..."
    pkg update -y
    pkg install -y python git curl wget
}

echo "2. 检查存储空间..."
df -h | grep /data

echo "3. 检查网络连接..."
ping -c 2 baidu.com > /dev/null 2>&1 && echo "✅ 网络正常" || echo "❌ 网络异常"

echo "4. 检查项目完整性..."
cd ~/my-ai-business/我的智能体课程 2>/dev/null && {
    echo "✅ 项目目录存在"
    ls -la | head -10
} || {
    echo "❌ 项目目录不存在，正在恢复..."
    mkdir -p ~/my-ai-business/我的智能体课程
    cd ~/my-ai-business/我的智能体课程
}

echo "5. 检查核心脚本..."
[ -f "./test_env.sh" ] && echo "✅ test_env.sh存在" || echo "❌ test_env.sh缺失"
[ -f "./一键上传.sh" ] && echo "✅ 一键上传.sh存在" || echo "❌ 一键上传.sh缺失"

echo "🔧 环境诊断完成"
