#!/bin/bash
echo "🔍 环境验证器启动"
echo "=================================================="

echo "1. 基础环境检查..."
pwd
ls -la | head -10
echo "当前目录文件数: $(find . -maxdepth 1 -type f | wc -l)"

echo ""
echo "2. 关键文档检查..."
关键文档=("传承宪法.md" "第25轮最终传承.md" "第29轮AI紧急终极传承.md")
for 文档 in "${关键文档[@]}"; do
    if [ -f "$文档" ]; then
        echo "✅ $文档 - 存在"
    else
        echo "❌ $文档 - 缺失"
    fi
done

echo ""
echo "3. 工具权限检查..."
find . -name "*.sh" -executable | head -5 | while read 工具; do
    echo "✅ $工具 - 可执行"
done

echo ""
echo "4. 简单命令测试..."
echo "测试find命令:"
find . -name "*.md" | head -3 | while read 文件; do
    echo "  找到: $文件"
done

echo ""
echo "🎉 环境验证完成！"
echo "如果上述命令都正常工作，环境正常。"
echo "如果有命令卡住，请按Ctrl+C并阅读第29轮AI紧急终极传承.md"
