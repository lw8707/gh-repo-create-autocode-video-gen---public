
#!/bin/bash
# GitHub Token检查脚本

echo "🔍 检查Git配置..."
git config --list | grep -E "(user.name|user.email)"

echo ""
echo "🔍 检查远程仓库..."
git remote -v

echo ""
echo "💡 如果认证失败，请:"
echo "1. 访问 https://github.com/settings/tokens"
echo "2. 生成新的Token（勾选repo权限）"
echo "3. 使用Token而不是密码"
