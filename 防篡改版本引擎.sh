#!/bin/bash
echo "🔒 启动防篡改版本引擎..."
cd ~/my-ai-business/我的智能体课程

# 基于Git的版本控制（最可靠）
git add .
git commit -m "自动提交: $(date)" || echo "✅ 工作区干净"

# 生成版本快照
当前版本=$(git log --oneline -1 | cut -d' ' -f1)
echo "🔗 当前Git版本: $当前版本"

# 保存版本信息
echo "$当前版本" > 当前版本.txt
echo "$(date)" > 最后更新时间.txt

echo "✅ 防篡改版本引擎就绪 - 基于Git版本控制"
