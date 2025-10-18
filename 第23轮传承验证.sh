#!/bin/bash
echo "🎯 第23轮传承验证"
echo "================"
echo "1. 确认目录: $(pwd)"
echo "2. 核心文件检查:"
[ -f "一键上传.sh" ] && echo "✅ 一键上传.sh存在" || echo "❌ 一键上传.sh缺失"
[ -f "资产盘点系统.sh" ] && echo "✅ 资产盘点系统.sh存在" || echo "❌ 资产盘点系统.sh缺失"
echo "3. GitHub状态: 待测试"
echo "🎉 基础验证完成"
