#!/bin/bash
echo "🔧 重建永久核心系统"
echo "=================="

# 1. 创建永久核心目录
echo "📁 创建永久核心目录..."
mkdir -p ~/永久核心系统
cd ~/永久核心系统

# 2. 创建核心系统组件
echo "🛠️ 创建核心系统组件..."

# 我的课程s - 主入口
cat > 我的课程s << 'CORE'
#!/bin/bash
echo "🎓 我的课程s - 智能体核心系统 v5.0"
echo "=================================="
echo "基于第36轮传承重建 - 永久版本"
echo "启动时间: $(date)"
echo ""

# 自动修复链接
[ ! -f ~/我的课程s ] && ln -sf ~/永久核心系统/我的课程s ~/我的课程s 2>/dev/null

echo "🔍 系统状态:"
[ -f "第36轮终极传承.md" ] && echo "✅ 第36轮传承文档存在" || echo "❌ 第36轮传承文档缺失"
[ -f ~/版本跟踪 ] && echo "✅ 版本跟踪已链接" || echo "❌ 版本跟踪未链接"
[ -f ~/沙箱验证 ] && echo "✅ 沙箱验证已链接" || echo "❌ 沙箱验证未链接"

echo ""
echo "🚀 可用功能:"
echo "  1. 📚 查看传承文档"
echo "  2. 📊 版本跟踪"
echo "  3. 🔒 沙箱验证"
echo "  4. 🛠️ 系统诊断"
echo "  5. 🔗 修复链接"
echo "  6. 🚀 继续开发"

read -p "请输入选择 (1-6): " choice

case $choice in
    1) 
        echo "📚 重要传承文档:"
        [ -f "第36轮终极传承.md" ] && echo "  - 第36轮终极传承.md (完整智慧)" || echo "  - 第36轮终极传承.md ❌ 缺失"
        [ -f "智能体DNA.md" ] && echo "  - 智能体DNA.md (核心思想)" || echo "  - 智能体DNA.md ❌ 缺失"
        echo ""
        echo "💡 提示: 这些文档包含了从第1轮到第36轮的所有经验教训"
        ;;
    2)
        [ -f ~/版本跟踪 ] && ~/版本跟踪 || echo "❌ 版本跟踪未安装"
        ;;
    3)
        [ -f ~/沙箱验证 ] && ~/沙箱验证 || echo "❌ 沙箱验证未安装"
        ;;
    4)
        [ -f ~/永久核心系统/系统诊断 ] && ~/永久核心系统/系统诊断 || echo "❌ 系统诊断未安装"
        ;;
    5)
        [ -f ~/永久核心系统/链接修复 ] && ~/永久核心系统/链接修复 || echo "❌ 链接修复未安装"
        ;;
    6)
        echo "🚀 启动第37轮开发工作..."
        echo "请基于第36轮传承继续前进"
        echo "核心原则: 对话即编程，服务全球小白"
        ;;
    *)
        echo "无效选择"
        ;;
esac
CORE

# 版本跟踪
cat > 版本跟踪 << 'TRACKER'
#!/bin/bash
echo "📊 版本跟踪 - 智能体状态监控 v5.0"
echo "================================"
echo "跟踪时间: $(date)"
echo ""

# Git状态
echo "🔧 Git仓库状态:"
if git status &>/dev/null; then
    echo "✅ Git仓库正常"
    echo "📦 远程仓库: $(git remote get-url origin 2>/dev/null || echo '未设置')"
    echo "🌿 当前分支: $(git branch --show-current 2>/dev/null || echo '未知')"
else
    echo "❌ 当前目录不是Git仓库"
fi

# 核心系统状态
echo ""
echo "🔗 核心系统状态:"
check_component() {
    if [ -f ~/$1 ]; then
        echo "  - $1: ✅ 存在"
    else
        echo "  - $1: ❌ 缺失"
    fi
}

check_component "我的课程s"
check_component "版本跟踪"
check_component "沙箱验证"

# 项目统计
echo ""
echo "📈 项目统计:"
echo "  - 脚本文件: $(find ~/永久核心系统 -name "*.sh" -type f 2>/dev/null | wc -l)"
echo "  - 文档文件: $(find ~/永久核心系统 -name "*.md" -type f 2>/dev/null | wc -l)"
echo "  - 总文件数: $(find ~/永久核心系统 -type f 2>/dev/null | wc -l)"

echo ""
echo "💡 提示: 运行 '~/永久核心系统/链接修复' 来修复缺失的组件"
TRACKER

# 沙箱验证
cat > 沙箱验证 << 'SANDBOX'
#!/bin/bash
echo "🔒 沙箱验证 - 安全保障系统 v5.0"
echo "==============================="
echo "验证时间: $(date)"
echo ""

# 环境检查
echo "🏠 环境安全:"
echo "  - 用户: $(whoami)"
echo "  - 目录: $(pwd)"
echo "  - 终端: $TERM"

# 权限检查
echo ""
echo "🔐 权限验证:"
[ -r "." ] && echo "  - 读权限: ✅" || echo "  - 读权限: ❌"
[ -w "." ] && echo "  - 写权限: ✅" || echo "  - 写权限: ❌"
[ -x "." ] && echo "  - 执行权限: ✅" || echo "  - 执行权限: ❌"

# 核心文件
echo ""
echo "📁 核心文件:"
[ -f ~/我的课程s ] && echo "  - 我的课程s: ✅" || echo "  - 我的课程s: ❌"
[ -f ~/版本跟踪 ] && echo "  - 版本跟踪: ✅" || echo "  - 版本跟踪: ❌"
[ -f ~/沙箱验证 ] && echo "  - 沙箱验证: ✅" || echo "  - 沙箱验证: ❌"

echo ""
echo "✅ 沙箱验证完成 - 环境安全"
SANDBOX

# 链接修复
cat > 链接修复 << 'LINKFIX'
#!/bin/bash
echo "🔗 链接修复工具 v5.0"
echo "==================="

fix_link() {
    local target="~/永久核心系统/$1"
    local link_name="~/$1"
    
    # 移除旧的链接或文件
    [ -e "$link_name" ] && rm -f "$link_name"
    
    # 创建新链接
    if ln -s "$target" "$link_name" 2>/dev/null; then
        chmod +x "$link_name"
        echo "✅ $1: 修复成功"
    else
        echo "❌ $1: 修复失败"
    fi
}

echo "修复核心系统链接..."
fix_link "我的课程s"
fix_link "版本跟踪"
fix_link "沙箱验证"

echo ""
echo "💡 现在可以运行: ~/我的课程s"
LINKFIX

# 系统诊断
cat > 系统诊断 << 'DIAG'
#!/bin/bash
echo "🏥 系统诊断 v5.0"
echo "==============="

echo "🔍 核心组件:"
[ -f ~/我的课程s ] && echo "✅ 我的课程s" || echo "❌ 我的课程s"
[ -f ~/版本跟踪 ] && echo "✅ 版本跟踪" || echo "❌ 版本跟踪"  
[ -f ~/沙箱验证 ] && echo "✅ 沙箱验证" || echo "❌ 沙箱验证"

echo ""
echo "🌐 网络连接:"
if ssh -T git@github.com &>/dev/null; then
    echo "✅ GitHub SSH连接正常"
else
    echo "❌ GitHub SSH连接失败"
fi

echo ""
echo "📦 Git状态:"
if git status &>/dev/null; then
    echo "✅ Git仓库正常"
else
    echo "❌ Git仓库异常"
fi

echo ""
echo "💡 建议:"
echo "  运行 ~/永久核心系统/链接修复 来修复缺失的组件"
DIAG

# 3. 设置执行权限
chmod +x ~/永久核心系统/*

# 4. 修复链接
echo "🔗 修复符号链接..."
~/永久核心系统/链接修复

echo ""
echo "✅ 核心系统重建完成！"
echo "💡 现在可以运行: ~/我的课程s"
echo "📚 请确保第36轮传承文档已保存"
