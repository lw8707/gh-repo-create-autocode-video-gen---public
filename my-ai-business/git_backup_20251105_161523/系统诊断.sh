#!/bin/bash
echo "🔍 系统全面诊断 v4.0"
echo "=================="
echo "诊断时间: $(date)"

# 1. 核心系统检查
echo ""
echo "1. 🎓 核心系统:"
[ -f "~/我的课程s" ] && echo "   ✅ 我的课程s: 存在" || echo "   ❌ 我的课程s: 缺失"
[ -L "~/我的课程s" ] && echo "   ✅ 我的课程s: 符号链接" || echo "   ❌ 我的课程s: 不是符号链接"
[ -f "~/版本跟踪" ] && echo "   ✅ 版本跟踪: 存在" || echo "   ❌ 版本跟踪: 缺失"
[ -f "~/沙箱验证" ] && echo "   ✅ 沙箱验证: 存在" || echo "   ❌ 沙箱验证: 缺失"

# 2. 工具系统检查
echo ""
echo "2. 🛠️ 工具系统:"
[ -f "工具管理器.sh" ] && echo "   ✅ 工具管理器: 存在" || echo "   ❌ 工具管理器: 缺失"
[ -f "Git问题解决器.sh" ] && echo "   ✅ Git解决器: 存在" || echo "   ❌ Git解决器: 缺失"
[ -d "~/tools" ] && echo "   ✅ 工具目录: 存在 ($(ls ~/tools/*.sh 2>/dev/null | wc -l)个工具)" || echo "   ❌ 工具目录: 缺失"

# 3. Git状态
echo ""
echo "3. 🔄 Git状态:"
if git status &>/dev/null; then
    echo "   ✅ Git仓库: 正常"
    echo "   分支: $(git branch --show-current 2>/dev/null)"
    echo "   远程: $(git remote -v | grep origin | head -1)"
    echo "   提交数: $(git log --oneline | wc -l)"
else
    echo "   ❌ Git仓库: 异常"
fi

# 4. 依赖检查
echo ""
echo "4. 📦 依赖状态:"
check_dep() {
    if command -v "$1" &>/dev/null; then
        echo "   ✅ $1: 正常"
    else
        echo "   ❌ $1: 缺失"
    fi
}
check_dep "git"
check_dep "python"
check_dep "node"
check_dep "curl"

# 5. 网络状态
echo ""
echo "5. 🌐 网络状态:"
if ping -c 1 github.com &>/dev/null; then
    echo "   ✅ GitHub连接: 正常"
else
    echo "   ❌ GitHub连接: 异常"
fi

# 6. 修复建议
echo ""
echo "6. 💡 修复建议:"
if [ ! -f "~/我的课程s" ]; then
    echo "   🛠️ 执行: ./全面重建系统.sh"
fi
if ! git status &>/dev/null; then
    echo "   🛠️ 执行: ./Git问题解决器.sh"
fi

echo ""
echo "✅ 诊断完成"
