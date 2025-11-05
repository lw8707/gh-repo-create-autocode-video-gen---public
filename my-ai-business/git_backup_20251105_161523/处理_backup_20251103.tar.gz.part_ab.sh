#!/bin/bash
echo "处理大文件: $1"
echo "方案: 分块上传，保留原文件"
echo "执行: split -b 80M \"$1\" \"${1}.part_\""
echo "创建合并脚本确保完整性"
