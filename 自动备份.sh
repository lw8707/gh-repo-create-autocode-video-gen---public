#!/bin/bash
echo "📦 自动备份中..."
cp -r ~/my-ai-business /sdcard/termux-backup/
date > /sdcard/termux-backup/last_backup.txt
echo "✅ 备份完成"
