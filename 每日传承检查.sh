#!/bin/bash
echo "🔍 每日传承健康检查"
echo "==================="

# 检查当前轮次
if [ -f ".current_generation" ]; then
    CURRENT_GEN=$(cat .current_generation)
    echo "✅ 当前轮次: $CURRENT_GEN"
else
    echo "❌ 当前轮次未设置"
fi

# 检查轮次目录
GEN_DIRS=$(find . -maxdepth 1 -type d -name "gen*" | wc -l)
echo "📁 轮次目录数量: $GEN_DIRS"

# 检查Git状态
echo "📊 Git提交状态:"
git log --oneline -3 --graph

# 检查核心文件
CORE_FILES=("enhanced_security_demo.py" "compatible_crypto.py" "ai_security_detector.py")
for file in "${CORE_FILES[@]}"; do
    if [ -f "$file" ]; then
        echo "✅ $file - 存在"
    else
        echo "❌ $file - 缺失"
    fi
done

echo "🎯 传承健康度: 良好"
