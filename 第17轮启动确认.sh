#!/bin/bash
echo "🚀 第17轮启动确认检查..."
echo "================================"

# 检查核心文件
echo "📁 核心文件检查:"
files=("quantum_fixer.py" "anti_delete_monitor.py" "tool_matrix.py" "启动实时保护.sh")
for file in "${files[@]}"; do
    if [ -f "$file" ]; then
        echo "✅ $file - 存在"
    else
        echo "❌ $file - 缺失"
    fi
done

# 检查Python模块导入
echo ""
echo "🔧 Python模块检查:"
python3 -c "
try:
    from quantum_fixer import QuantumFixer
    print('✅ quantum_fixer - 可导入')
except: print('❌ quantum_fixer - 导入失败')

try:
    from anti_delete_monitor import AntiDeleteMonitor  
    print('✅ anti_delete_monitor - 可导入')
except: print('❌ anti_delete_monitor - 导入失败')

try:
    from tool_matrix import ToolMatrix
    print('✅ tool_matrix - 可导入') 
except: print('❌ tool_matrix - 导入失败')
"

# 检查Git状态
echo ""
echo "📊 Git状态检查:"
git status --porcelain

echo ""
echo "🎯 第17轮状态:"
if [ -f "quantum_fixer.py" ] && [ -f "anti_delete_monitor.py" ] && [ -f "tool_matrix.py" ]; then
    echo "✅ 保护系统完整 - 第18轮可以安全启动!"
    echo "💡 运行: ./启动实时保护.sh"
else
    echo "❌ 保护系统不完整 - 需要修复"
fi
