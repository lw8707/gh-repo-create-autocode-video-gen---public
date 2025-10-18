#!/bin/bash
echo "✅ 简单测试脚本工作正常"
echo "当前时间: $(date)"
echo "脚本数量: $(find . -name '*.sh' 2>/dev/null | wc -l)"
