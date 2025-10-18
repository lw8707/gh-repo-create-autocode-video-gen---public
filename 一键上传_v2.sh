#!/bin/bash
echo "🚀 开始上传文件到GitHub..."
cd ~/my-ai-business/我的智能体课程
git add .
git commit -m "自动提交: $(date)"
git push origin main
echo "✅ 上传完成!"
echo "🔗 查看: https://github.com/lw8707/gh-repo-create-autocode-video-gen---public"
