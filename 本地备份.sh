#!/bin/bash
echo "💾 创建本地备份..."
# 备份所有Python文件
find . -name "*.py" -exec cp {} {}.backup \;
# 备份所有Shell脚本
find . -name "*.sh" -exec cp {} {}.backup \;
# 备份所有Markdown文件
find . -name "*.md" -exec cp {} {}.backup \;
echo "✅ 本地备份完成！所有重要文件都已复制为.backup文件"
ls -la *.backup 2>/dev/null | wc -l
