#!/bin/bash
echo "🔍 启动仓库深度分析..."
echo "=========================================="

# 1. 分析轮次历史
echo "📚 轮次历史分析："
find . -name "*第*轮*" -type f | head -20

# 2. 分析工具资产
echo ""
echo "🛠️ 工具资产分析："
find . -name "*.sh" -o -name "*.py" | wc -l
echo "总工具数: $(find . -name "*.sh" -o -name "*.py" | wc -l)"

# 3. 分析关键文档
echo ""
echo "📄 关键文档状态："
关键文档="传承宪法.md 第25轮最终传承.md 必须遵守的原则.md"
for doc in $关键文档; do
    if [ -f "$doc" ]; then
        echo "✅ $doc - 存在"
    else
        echo "❌ $doc - 缺失"
    fi
done

# 4. 分析Git状态
echo ""
echo "🔧 Git状态："
git status --short | head -10

echo ""
echo "🎯 分析完成！基于此研究提出反问。"
