#!/bin/bash
echo "=== 环境测试 ==="
echo "1. 基础功能: $(date)"
echo "2. 脚本数量: $(find . -name '*.sh' 2>/dev/null | wc -l)"
echo "3. 核心文件检查:"
for file in "一键上传.sh" "全面诊断.sh"; do
    [ -f "$file" ] && echo "   ✅ $file" || echo "   ❌ $file"
done
echo "=== 测试完成 ==="
