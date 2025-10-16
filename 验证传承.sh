#!/bin/bash
echo "🔍 传承系统验证"
echo "==============="

if [ -f "传承核心.md" ]; then
  echo "✅ 传承核心文件存在"
else
  echo "❌ 传承核心文件缺失"
fi

if [ -f "轮次记录.json" ]; then
  echo "✅ 轮次记录文件存在" 
else
  echo "❌ 轮次记录文件缺失"
fi

echo "📁 轮次目录:"
ls -d gen*/ 2>/dev/null || echo "暂无轮次目录"

echo "🎯 传承系统状态: 运行中"
