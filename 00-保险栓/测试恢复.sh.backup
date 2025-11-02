#!/bin/bash
echo "🧪 执行恢复测试..."

if [ ! -f "/sdcard/Download/项目备份.tar.gz" ]; then
    echo "❌ 错误：手机存储中找不到备份文件"
    echo "请手动将备份文件复制到手机Download目录"
    exit 1
fi

echo "✅ 手机存储中找到备份文件"

# 测试文件完整性
tar -tzf "/sdcard/Download/项目备份.tar.gz" > /dev/null 2>&1
if [ $? -ne 0 ]; then
    echo "❌ 错误：备份文件损坏"
    exit 1
fi

echo "✅ 备份文件完整"

echo ""
echo "🎯 恢复测试通过！"
echo "新对话可以按以下步骤恢复："
echo "1. 在文件管理中分享备份文件到Termux"
echo "2. 运行: tar -xzf 项目备份.tar.gz"
echo "3. 运行: cd my-ai-business/我的智能体课程 && ./全面诊断.sh"
