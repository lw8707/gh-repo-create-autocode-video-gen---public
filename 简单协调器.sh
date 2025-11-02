#!/bin/bash
echo "简单协调器 - 基于实际可用工具"

case "$1" in
    "list")
        echo "📁 文件列表:"
        ls -la
        ;;
    "docs")
        echo "📚 文档:"
        for f in *.md; do [ -f "$f" ] && echo "  $f"; done
        ;;
    "tools")
        echo "🛠️ 工具:"
        for f in *.sh; do [ -f "$f" ] && echo "  $f"; done
        ;;
    *)
        echo "用法: $0 [list|docs|tools]"
        ;;
esac
