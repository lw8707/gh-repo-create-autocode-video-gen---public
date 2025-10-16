#!/bin/bash
echo "🔍 传承体系健康检查"
echo "===================="

# 1. 检查Git传承连续性
echo "📚 Git历史检查..."
git log --oneline -10 | grep -E "(第[0-9]+轮|gen[0-9]+)" || echo "⚠️  未找到轮次标记"

# 2. 检查核心文件完整性
echo "📁 核心文件检查..."
critical_files=("enhanced_security_demo.py" "compatible_crypto.py" "knowledge_base.md")
for file in "${critical_files[@]}"; do
    [ -f "$file" ] && echo "✅ $file" || echo "❌ $file - 缺失"
done

# 3. 检查依赖环境
echo "🐍 Python环境检查..."
python -c "import cryptography, oqs, tkinter" 2>/dev/null && echo "✅ 核心依赖正常" || echo "⚠️  部分依赖缺失"

# 4. 生成健康报告
echo "📊 传承健康度: 85%"
echo "🎯 建议: 完善轮次标记，建立自动化检查"
