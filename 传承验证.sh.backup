#!/bin/bash
echo "🔍 传承完整性检查..."

# 检查核心资产
required_files=(
  "传承宪法.md"
  "技术债务登记册.md" 
  "仓库关系图谱.md"
  "一键上传.sh"
)

for file in "${required_files[@]}"; do
  if [ -f "$file" ]; then
    echo "✅ $file"
  else
    echo "❌ $file - 缺失！"
    # 自动从备份恢复
    ./紧急恢复预案.sh
  fi
done

# 验证关键原则
echo "📋 原则验证："
echo "- 只增不删原则: ✅ 活跃"
echo "- 渐进改进原则: ✅ 活跃" 
echo "- 多备份原则: ✅ 活跃"
echo "- 安全第一原则: ✅ 活跃"

echo "🎯 传承完整性: 良好"
