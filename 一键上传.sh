#!/bin/bash
echo "📤 开始上传到GitHub..."
git add .
git commit -m "自动上传: $(date '+%Y-%m-%d %H:%M:%S')"
git push origin main
echo "✅ 上传完成"
