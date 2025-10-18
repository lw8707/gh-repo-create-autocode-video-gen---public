#!/bin/bash
echo "🔍 基于第21轮成功经验的诊断"
echo "=========================="

# 1. 检查第21轮恢复的核心文件
echo "1. 检查第21轮恢复的核心文件..."
核心文件=("一键上传.sh" "全面诊断.sh" "自动备份.sh" "全面恢复.sh" "Git恢复.sh")

for 文件 in "${核心文件[@]}"; do
    if [ -f "$文件" ]; then
        大小=$(stat -c%s "$文件" 2>/dev/null || stat -f%z "$文件" 2>/dev/null)
        echo "✅ $文件 - 存在 (大小: ${大小}字节)"
    else
        echo "❌ $文件 - 缺失"
    fi
done

# 2. 检查脚本执行问题
echo ""
echo "2. 分析脚本执行问题..."
for 文件 in "自动备份.sh" "一键上传.sh"; do
    if [ -f "$文件" ]; then
        echo "🔧 检查 $文件 语法..."
        bash -n "$文件" && echo "  ✅ 语法正确" || echo "  ❌ 语法错误"
        
        # 检查第一行shebang
        head -1 "$文件" | grep -q "^#!/" && echo "  ✅ Shebang正确" || echo "  ❌ Shebang缺失"
    fi
done

# 3. 检查GitHub连接状态
echo ""
echo "3. 检查GitHub连接..."
git remote -v
echo "Git状态: $(git status --short 2>/dev/null | wc -l)个变更"

# 4. 生成基于历史经验的建议
echo ""
echo "4. 基于历史经验的建议:"
echo "   📚 第13轮教训: 不要强制统一代码风格"
echo "   📚 第16轮经验: 分层备份防止数据丢失"  
echo "   📚 第19轮经验: 保持核心脚本不变"
echo "   📚 第21轮经验: 从GitHub完整恢复可行"

echo ""
echo "✅ 诊断完成 - 基于历史经验分析"
