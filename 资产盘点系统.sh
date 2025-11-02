#!/bin/bash
echo "📊 资产盘点系统 v4.0"
echo "=================="
echo "当前目录: $(pwd)"
echo "总文件数: $(find . -type f | wc -l)"
echo "脚本文件: $(find . -name "*.sh" | wc -l)"
echo "Python文件: $(find . -name "*.py" | wc -l)"
echo "文档文件: $(find . -name "*.md" | wc -l)"
echo "✅ 基础资产盘点完成"
