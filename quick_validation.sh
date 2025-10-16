#!/bin/bash
echo "🚀 快速传承验证"
echo "================"
echo "🔍 检查核心文件..."
[ -f "CODE_EXECUTION_STANDARDS.md" ] && echo "✅ 执行规范存在" || echo "❌ 执行规范缺失"
[ -f "crypto_fallback_system.py" ] && echo "✅ 加密系统存在" || echo "❌ 加密系统缺失"
[ -f ".generation_pointer" ] && echo "✅ 轮次指针存在" || echo "❌ 轮次指针缺失"
echo "🎯 第15轮状态: 代码执行规范统一完成"
