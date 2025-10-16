#!/bin/bash
# 基于第9轮成熟方案的重建自动上传脚本
# 已验证的成功机制 - 简单可靠

echo "🚀 基于成熟方案的自动上传启动..."
cd ~/my-ai-business/我的智能体课程

# 检查更改
if [ -n "$(git status --porcelain)" ]; then
    echo "📦 发现更改，自动上传..."
    
    # 添加所有文件
    git add .
    
    # 创建提交信息
    COMMIT_MSG="自动上传: $(date '+%Y-%m-%d %H:%M:%S') - 第16轮成果"
    
    # 提交
    git commit -m "$COMMIT_MSG"
    
    # 推送到GitHub
    if git push origin main; then
        echo "✅ 上传成功: $COMMIT_MSG"
        echo "🔗 仓库地址: https://github.com/lw8707/gh-repo-create-autocode-video-gen---public"
    else
        echo "❌ 上传失败，尝试修复..."
        # 简单的重试机制
        sleep 2
        git push origin main || echo "⚠️ 重试失败，需要手动检查"
    fi
else
    echo "✅ 无更改需要上传"
fi
