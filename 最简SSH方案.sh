#!/bin/bash
# 最简SSH方案 - 避免所有密码输入

echo "🚀 最简SSH方案"
echo "=============="

# 生成SSH密钥
echo "1. 生成SSH密钥..."
ssh-keygen -t rsa -b 4096 -f ~/.ssh/id_rsa -N '' -q

# 显示公钥
echo ""
echo "2. 请复制以下公钥到GitHub:"
echo "========================================"
cat ~/.ssh/id_rsa.pub
echo "========================================"

echo ""
echo "3. 添加公钥到GitHub:"
echo "   访问: https://github.com/settings/keys"
echo "   点击 'New SSH key'"
echo "   标题: Termux手机"
echo "   粘贴上面的公钥"
echo "   点击 'Add SSH key'"

echo ""
echo "4. 测试SSH连接..."
ssh -T git@github.com

echo ""
echo "5. 切换到SSH协议..."
cd 我的智能体课程
git remote set-url origin git@github.com:lw8707/gh-repo-create-autocode-video-gen---public.git

echo ""
echo "6. 测试推送..."
git push -u origin main

if [ $? -eq 0 ]; then
    echo ""
    echo "🎉 SSH方案成功！"
    echo "💪 现在可以无障碍使用GitHub了"
else
    echo ""
    echo "❌ 推送失败，请检查SSH密钥是否添加正确"
fi

cd ..
