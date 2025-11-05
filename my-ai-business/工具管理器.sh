#!/bin/bash
echo "🛠️ 工具管理器 - 统一工具管理 v4.0"
echo "=============================="

TOOL_DIR="$HOME/tools"

# 确保工具目录存在
mkdir -p "$TOOL_DIR"

# 工具列表
declare -A TOOLS=(
    ["文件管理器"]="管理文件和目录"
    ["网络诊断"]="检查网络连接"
    ["系统监控"]="监控系统状态"
    ["Git助手"]="Git操作辅助"
    ["依赖检查"]="检查系统依赖"
)

# 安装工具
install_tool() {
    local tool_name=$1
    case $tool_name in
        "文件管理器")
            cat > "$TOOL_DIR/文件管理器.sh" << 'FILE_MGR'
#!/bin/bash
echo "📁 智能文件管理器 v2.0"
echo "==================="
echo "扫描可执行文件..."
find . -name "*.sh" -exec chmod +x {} \; 2>/dev/null
find . -name "*.py" -exec chmod +x {} \; 2>/dev/null
echo "✅ 文件权限修复完成"
echo ""
echo "📊 文件统计:"
echo "总文件: $(find . -type f | wc -l)"
echo "脚本文件: $(find . -name "*.sh" -type f | wc -l)"
echo "Python文件: $(find . -name "*.py" -type f | wc -l)"
FILE_MGR
            chmod +x "$TOOL_DIR/文件管理器.sh"
            ;;
        "网络诊断")
            cat > "$TOOL_DIR/网络诊断.sh" << 'NETWORK'
#!/bin/bash
echo "🌐 网络诊断工具 v2.0"
echo "================="
echo "1. 基础连接测试:"
ping -c 2 github.com && echo "✅ GitHub: 可达" || echo "❌ GitHub: 不可达"
echo ""
echo "2. SSH认证测试:"
ssh -T git@github.com && echo "✅ SSH认证: 正常" || echo "❌ SSH认证: 异常"
echo ""
echo "3. 端口检查:"
netstat -tuln 2>/dev/null | head -10 || echo "无法检查端口"
NETWORK
            chmod +x "$TOOL_DIR/网络诊断.sh"
            ;;
        "系统监控")
            cat > "$TOOL_DIR/系统监控.sh" << 'MONITOR'
#!/bin/bash
echo "📊 系统监控工具 v2.0"
echo "================="
echo "内存使用:"
free -h 2>/dev/null || echo "无法获取内存信息"
echo ""
echo "磁盘使用:"
df -h 2>/dev/null | head -6
echo ""
echo "CPU信息:"
cat /proc/cpuinfo | grep "processor" | wc -l | xargs echo "CPU核心数:"
MONITOR
            chmod +x "$TOOL_DIR/系统监控.sh"
            ;;
    esac
    echo "✅ 安装工具: $tool_name"
}

# 主函数
case "${1:-}" in
    "install")
        for tool in "${!TOOLS[@]}"; do
            install_tool "$tool"
        done
        ;;
    "list")
        echo "📋 可用工具:"
        for tool in "${!TOOLS[@]}"; do
            echo "  🛠️ $tool: ${TOOLS[$tool]}"
        done
        ;;
    "run")
        if [ -n "$2" ] && [ -f "$TOOL_DIR/$2.sh" ]; then
            "$TOOL_DIR/$2.sh"
        else
            echo "❌ 工具不存在: $2"
        fi
        ;;
    *)
        echo "用法:"
        echo "  ./工具管理器.sh install    # 安装所有工具"
        echo "  ./工具管理器.sh list       # 列出工具"
        echo "  ./工具管理器.sh run <工具> # 运行工具"
        ;;
esac
