#!/bin/bash
echo "✅ 修复验"
echo "=============="

# 测试1: 环境基本功能
echo "1. 环境测试:"
./test_env.sh

# 测试2: 脚本语法检查
echo ""
echo "2. 脚本语法检查:"
for script in test_env.sh backup_fixed.sh github_fix.sh; do
    if bash -n "$script" 2>/dev/null; then
        echo "   ✅ $script 语法正确"
    else
        echo "   ❌ $script 语法错误"
    fi
done

# 测试3: 文件存在性检查
echo ""
echo "3. 核心文件状态:"
[ -f "一键上传.sh" ] && echo "   ✅ 一键上传.sh 存在" || echo "   ❌ 一键上传.sh 缺失"
[ -f "全面诊断.sh" ] && echo "   ✅ 全面诊断.sh 存在" || echo "   ❌ 全面诊断.sh 缺失"

# 测试4: GitHub连接测试
echo ""
echo "4. GitHub连接:"
ssh -T git@github.com 2>&1 | grep -q "successfully authenticated" && echo "   ✅ SSH认证正常" || echo "   ⚠️ SSH认证可能有问题"

echo ""
echo "🎯 验证完成 - 所有测试应该通过"
