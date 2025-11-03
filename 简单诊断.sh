#!/bin/bash
echo "===基础诊断==="
pwd
echo "关键文档检查:"
[ -f "传承宪法.md" ] && echo "Found: 传承宪法.md"
[ -f "第25轮最终传承.md" ] && echo "Found: 第25轮最终传承.md"
echo "Git状态:"
git status --short
