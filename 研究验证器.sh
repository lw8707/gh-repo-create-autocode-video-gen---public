#!/bin/bash
echo "🔍 研究完整性验证"
echo "=================="

echo "1. 轮次研究完成:"
[ -f "实际轮次记录.txt" ] && echo "✅" || echo "❌"

echo "2. 工具研究完成:"  
[ -f "实际工具清单.txt" ] && echo "✅" || echo "❌"

echo "3. 成功经验提取:"
[ -f "成功经验.txt" ] && echo "✅" || echo "❌"

echo "🎯 只有所有✅才能开始行动！"
