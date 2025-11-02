#!/bin/bash
echo "💾 开始自动备份..."
backup_time=$(date +%Y%m%d_%H%M%S)
backup_file="course_backup_${backup_time}.tar.gz"
echo "备份时间: $backup_time"
echo "备份文件: $backup_file"
tar -czf "$backup_file" ./*.sh ./*.md 2>/dev/null
if [ $? -eq 0 ]; then
    echo "✅ 备份完成: $backup_file"
else
    echo "❌ 备份失败"
fi
