#!/bin/bash
echo "Starting backup..."
backup_time=$(date +%Y%m%d_%H%M%S)
backup_file="backup_${backup_time}.tar.gz"
echo "Backup time: $backup_time"
echo "Backup file: $backup_file"
tar -czf "$backup_file" ./*.sh ./*.md 2>/dev/null
[ $? -eq 0 ] && echo "Backup success: $backup_file" || echo "Backup failed"
