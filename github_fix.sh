#!/bin/bash
echo "🔧 GitHub认证修复"
echo "================="

# 方法1: 检查现有认证
echo "1. 检查当前Git配置:"
git remote -v
git config --list | grep -i user

# 方法2: 测试仓库访问
echo "2. 测试仓库访问:"
curl -I https://github.com/lw8707/gh-repo-create-autocode-video-gen---public 2>/dev/null | head -1

# 方法3: 提供修复方案
echo "3. 认证修复方案:"
echo "   ✅ SSH密钥方案:"
echo "      ssh-keygen -t ed25519 -C 'your_email@example.com'"
echo "      cat ~/.ssh/id_ed25519.pub"
echo "   ✅ 令牌更新方案:"
echo "      访问 GitHub -> Settings -> Developer settings -> Tokens"
echo "   ✅ 配置更新:"
echo "      git config --global user.name 'Your Name'"
echo "      git config --global user.email 'your_email@example.com'"

echo "✅ GitHub修复指南完成"
