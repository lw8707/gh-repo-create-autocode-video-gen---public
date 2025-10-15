#!/bin/bash
echo "🔐 GitHub认证自动化系统启动..."

# 检查认证状态（使用英文变量名避免问题）
auth_status=$(ssh -T git@github.com 2>&1 | grep "successfully authenticated")

if [ -n "$auth_status" ]; then
    echo "✅ GitHub认证正常"
    echo "最后认证时间: $(date)" > GitHub认证状态.txt
else
    echo "❌ GitHub认证失败，需要重新认证"
    echo "请执行以下步骤："
    echo "1. 访问: https://github.com/settings/keys"
    echo "2. 添加新的SSH密钥"
    echo "3. 公钥内容: $(cat ~/.ssh/id_ed25519.pub)"
fi

# 更新项目记忆
if [ -f "项目长期记忆_v2.1.json" ]; then
    echo "🔄 更新认证状态..."
    jq --arg date "$(date)" '.last_authentication = $date' 项目长期记忆_v2.1.json > temp.json && mv temp.json 项目长期记忆_v2.1.json
fi

echo "✅ 认证检查完成"
