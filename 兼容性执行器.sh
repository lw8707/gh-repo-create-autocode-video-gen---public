#!/bin/bash
# 通用兼容性执行器
# 解决Termux环境下的兼容性问题

命令="$1"
参数="${@:2}"

case "$命令" in
    "safe_find")
        # 安全的find命令包装
        find . -name "$2" | while read 文件; do
            echo "找到: $文件"
        done
        ;;
    "safe_loop") 
        # 安全的循环包装
        find . -name "$2" | while read 项目; do
            echo "处理: $项目"
        done
        ;;
    "check_syntax")
        # 语法检查
        脚本="$2"
        if sh -n "$脚本" 2>/dev/null; then
            echo "✅ $脚本 语法正确"
        else
            echo "❌ $脚本 语法错误"
        fi
        ;;
    *)
        echo "可用命令: safe_find, safe_loop, check_syntax"
        ;;
esac
