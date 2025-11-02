#!/bin/bash
# 剪贴板自动清理工具
echo "🔧 清理剪贴板中的危险字符..."
xsel -b | python3 紧急过滤器.py | xsel -b
echo "✅ 剪贴板已安全"
