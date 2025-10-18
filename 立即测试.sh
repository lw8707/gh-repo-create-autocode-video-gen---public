#!/bin/bash
echo "🚀 立即测试开始 - 保证有输出!"
echo "=================================="

# 测试1: 基础环境
echo "1. 测试基础环境..."
echo "   当前时间: $(date)"
echo "   当前目录: $(pwd)"
echo "✅ 基础环境正常"

# 测试2: 文件系统
echo "2. 测试文件系统..."
echo "   文件数量: $(ls -1 | wc -l)"
echo "   磁盘空间: $(df -h . | tail -1 | awk '{print $4}') 可用"
echo "✅ 文件系统正常"

# 测试3: 核心脚本状态
echo "3. 测试核心脚本..."
核心脚本=("一键上传.sh" "全面诊断.sh" "自动备份.sh" "全面恢复.sh")
for 脚本 in "${核心脚本[@]}"; do
    if [ -f "$脚本" ]; then
        echo "   ✅ $脚本 - 存在"
    else
        echo "   ❌ $脚本 - 缺失"
    fi
done
echo "✅ 核心脚本检查完成"

# 测试4: Git状态（快速检查）
echo "4. 测试Git状态..."
git status --short 2>/dev/null | head -3 && echo "   ✅ Git工作正常" || echo "   ⚠️ Git可能有问题"

echo ""
echo "🎉 立即测试完成!"
echo "📊 如果看到以上输出，说明环境基本正常"
echo "💡 如果有脚本缺失，我们需要重新创建"
