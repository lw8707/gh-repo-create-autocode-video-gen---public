#!/bin/bash
echo "🔧 修复SSH主机密钥验证问题"
echo "=========================="

# 1. 清除旧的known_hosts条目
echo "🗑️ 清除旧的GitHub主机密钥..."
ssh-keygen -R github.com
ssh-keygen -R 20.205.243.166

# 2. 添加GitHub的主机密钥到known_hosts
echo "🔑 添加GitHub主机密钥..."
mkdir -p ~/.ssh
chmod 700 ~/.ssh

# 添加GitHub的ED25519和RSA密钥
cat >> ~/.ssh/known_hosts << 'KNOWN_HOSTS'
github.com ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIOMqqnkVzrm0SdG6UOoqKLsabgH5C9okWi0dh2l9GKJl
github.com ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBEmKSENjQEezOmxkZMy7opKgwFB9nkt5YRrYMjNuG5N87uRgg6CLrbo5wAdT/y6v0mKV0U2w0WZ2YB/++Tpockg=
github.com ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEAq2A7hRGmdnm9tUDbO9IDSwBK6TbQa+PXYPCPy6rbTrTtw7PHkccKrpp0yVhp5HdEIcKr6pLlVDBfOLX9QUsyCOV0wzfjIJNlGEYsdlLJizHhbn2mUjvSAHQqZETYP81eFzLQNnPHt4EVVUh7VfDESU84KezmD5QlWpXLmvU31/yMf+Se8xhHTvKSCZIFImWwoG6mbUoWf9nzpIoaSjB+weqqUUmpaaasXVal72J+UX2B+2RPW3RcT0eOzQgqlJL3RKrTJvdsjE3JEAvGq3lGHSZXy28G3skua2SmVi/w4yCE6gbODqnTWlg7+wC604ydGXA8VJiS5ap43JXiUFFAaQ==
KNOWN_HOSTS

# 3. 设置正确的权限
chmod 600 ~/.ssh/known_hosts

# 4. 测试连接
echo "🧪 测试SSH连接..."
ssh -T git@github.com

if [ $? -eq 0 ]; then
    echo "✅ SSH连接测试成功！"
else
    echo "❌ SSH连接仍然失败，尝试备选方案..."
    # 备选方案：使用HTTPS协议
    git remote set-url origin https://github.com/lw8707/gh-repo-create-autocode-video-gen---public.git
    echo "🔄 已切换到HTTPS协议，请使用个人访问令牌"
fi
