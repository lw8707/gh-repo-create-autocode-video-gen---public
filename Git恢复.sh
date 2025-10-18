#!/bin/bash
echo "🔧 Git恢复工具"
echo "=============="

# 方法1: 尝试直接克隆到临时目录然后合并
echo "方法1: 尝试重新克隆..."
git clone https://github.com/lw8707/gh-repo-create-autocode-video-gen---public temp_repo_$$ 2>/dev/null

if [ $? -eq 0 ]; then
    echo "✅ 克隆成功，合并文件..."
    cp -r temp_repo_$$/* ./
    cp -r temp_repo_$$/.* ./ 2>/dev/null || true
    rm -rf temp_repo_$$
    echo "✅ 文件恢复完成"
else
    echo "❌ 克隆失败，使用备用方案"
    echo "备用方案: 手动初始化仓库"
    
    # 创建基础的.gitignore
    cat > .gitignore << 'GITIGNORE_EOF'
*.tmp
*.log
.DS_Store
GITIGNORE_EOF
    
    # 初始化提交
    git add .
    git commit -m "第21轮恢复: 基础重建" 2>/dev/null || echo "提交失败（可能无变化）"
    
    echo "✅ 本地Git仓库已准备就绪"
    echo "请在网络恢复后执行: git push -u origin main"
fi
