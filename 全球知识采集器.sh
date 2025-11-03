#!/bin/bash
echo "🌍 启动全球知识采集..."
echo "=========================================="

# 1. 克隆关键仓库
echo "📥 克隆关键知识库..."
目标仓库=(
    "https://github.com/lw8707/gh-repo-create-autocode-video-gen-公共.git"
    "https://github.com/microsoft/AI-For-Beginners.git"
    "https://github.com/huggingface/transformers.git"
)

for 仓库 in "${目标仓库[@]}"; do
    仓库名=$(basename "$仓库" .git)
    if [ ! -d "外部知识库/$仓库名" ]; then
        echo "正在克隆: $仓库名"
        git clone "$仓库" "外部知识库/$仓库名" 2>/dev/null && echo "✅ 成功克隆 $仓库名" || echo "❌ 克隆失败 $仓库名"
    else
        echo "✅ $仓库名 已存在"
    fi
done

# 2. 提取最佳实践
echo ""
echo "💡 提取最佳实践..."
find 外部知识库 -name "*.md" -o -name "*.py" -o -name "*.sh" | head -10 | while read 文件; do
    echo "发现: $文件"
done

echo ""
echo "🎯 知识采集完成！开始分析..."
