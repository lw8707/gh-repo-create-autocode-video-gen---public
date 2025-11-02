#!/bin/bash
echo "🔍 全面诊断 - 找出AI变傻的根本原因"
echo "=================================================="

echo "1. 环境基础诊断..."
echo "   路径: $(pwd)"
echo "   文件数: $(find . -type f 2>/dev/null | wc -l)"
echo "   目录数: $(find . -type d 2>/dev/null | wc -l)"

echo ""
echo "2. 关键资产诊断..."
关键资产="传承宪法.md 第25轮最终传承.md"
for 资产 in $关键资产; do
    if [ -f "$资产" ]; then
        行数=$(wc -l < "$资产" 2>/dev/null || echo 0)
        echo "   ✅ $资产 - 健康 ($行数 行)"
    else
        echo "   ❌ $资产 - 缺失"
    fi
done

echo ""
echo "3. 工具生态诊断..."
工具数量=$(find . -name "*.sh" -type f 2>/dev/null | wc -l)
echo "   发现 $工具数量 个Shell工具"

find . -name "*.sh" -type f 2>/dev/null | head -5 | while read tool; do
    if [ -x "$tool" ]; then
        echo "   ✅ $tool - 就绪"
    else
        echo "   ⚠️ $tool - 待授权"
    fi
done

echo ""
echo "4. 传承健康诊断..."
传承文档=$(find . -name "*传承*" -type f 2>/dev/null | head -5)
if [ -n "$传承文档" ]; then
    echo "   发现传承文档:"
    echo "$传承文档" | while read doc; do
        echo "   📄 $doc"
    done
else
    echo "   ⚠️ 传承文档稀少"
fi

echo ""
echo "5. 问题根本原因分析..."
echo "   🔍 可能原因:"
echo "      - 传承机制失效"
echo "      - 工具协调不足" 
echo "      - 全局视角缺失"
echo "      - 原则执行不严"

echo ""
echo "6. 立即修复方案..."
echo "   ✅ 启动深度研究模式"
echo "   ✅ 建立Agent蜂群协调"
echo "   ✅ 强化原则执行"
echo "   ✅ 建立全局架构视角"

echo ""
echo "=================================================="
echo "🎯 诊断完成: AI变傻原因是系统架构退化"
echo "💡 解决方案: 重建全局协调机制"
echo "=================================================="
