#!/bin/bash
# 真正协调执行器 - 严格遵守只增不删原则

echo "🎯 启动真正协调执行器..."
echo "========================================"

# 颜色定义
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

# 核心原则验证
validate_principles() {
    echo -e "${BLUE}🔍 验证核心原则...${NC}"
    
    # 检查是否违反只增不删
    if [[ "$1" == *"delete"* ]] || [[ "$1" == *"remove"* ]] || [[ "$1" == *"override"* ]]; then
        echo -e "${RED}❌ 违反只增不删原则!${NC}"
        return 1
    fi
    
    echo -e "${GREEN}✅ 原则验证通过${NC}"
    return 0
}

# 资产保护检查
protect_assets() {
    local original_count=$(find . -type f | wc -l)
    echo -e "${YELLOW}📊 当前文件总数: $original_count${NC}"
    
    # 执行操作
    "$@"
    
    local new_count=$(find . -type f | wc -l)
    if [ $new_count -lt $original_count ]; then
        echo -e "${RED}🚨 文件数量减少! 违反只增不删原则!${NC}"
        return 1
    fi
    
    echo -e "${GREEN}✅ 资产保护验证通过${NC}"
    return 0
}

# 工具协调执行
coordinate_tools() {
    local tool_category=$1
    echo -e "${YELLOW}🔄 协调执行: $tool_category${NC}"
    
    case $tool_category in
        "legacy")
            # 传承工具协调 - 不删除任何版本
            [ -f "./传承验证.sh" ] && ./传承验证.sh
            [ -f "./传承验证.py" ] && python3 传承验证.py
            [ -f "./传承验证系统.py" ] && python3 传承验证系统.py
            # 所有版本都执行，不选择"最佳"版本
            ;;
        "development")
            # 开发工具协调 - 保留所有工具
            [ -f "n8n工作流集成器.py" ] && echo "📋 n8n工作流可用"
            [ -f "MCP服务器集成器.py" ] && echo "📋 MCP服务器可用"
            [ -f "统一工具路由器.py" ] && echo "📋 工具路由器可用"
            # 不统一，只协调
            ;;
        "security")
            # 安全工具协调 - 所有安全工具都重要
            [ -f "安全扫描.py" ] && echo "🛡️ 安全扫描可用"
            [ -f "安全健康检查系统.py" ] && echo "🛡️ 健康检查可用"
            [ -f "零信任安全.sh" ] && echo "🛡️ 零信任安全可用"
            ;;
        "video")
            # 视频工具协调 - 保留所有视频工具
            [ -f "视频能力开发/基础视频工具.sh" ] && echo "🎬 基础视频工具可用"
            [ -f "电影生成器.sh" ] && echo "🎬 电影生成器可用"
            [ -f "安全输出工具.py" ] && echo "🎬 安全输出工具可用"
            ;;
        "analysis")
            # 分析模式 - 只分析不修改
            analyze_assets
            ;;
        *)
            echo -e "${RED}❌ 未知类别: $tool_category${NC}"
            show_usage
            ;;
    esac
}

# 资产分析（只读）
analyze_assets() {
    echo -e "${BLUE}📊 资产分析报告（只读）${NC}"
    
    # 文件统计
    local total_files=$(find . -type f | wc -l)
    local sh_files=$(find . -name "*.sh" | wc -l)
    local py_files=$(find . -name "*.py" | wc -l)
    local md_files=$(find . -name "*.md" | wc -l)
    
    echo -e "📁 总文件数: $total_files"
    echo -e "🐚 Shell脚本: $sh_files"
    echo -e "🐍 Python脚本: $py_files"
    echo -e "📝 文档文件: $md_files"
    
    # 重复文件分析（只分析，不处理）
    echo -e "${YELLOW}🔍 重复文件分析（只分析）...${NC}"
    find . -name "*.sh" -o -name "*.py" -o -name "*.md" | \
    sort | uniq -d | while read file; do
        echo -e "📄 重复文件: $file"
    done
    
    echo -e "${GREEN}✅ 分析完成 - 未修改任何文件${NC}"
}

# 协调器路由
coordinator_router() {
    local request=$1
    shift
    
    echo -e "${BLUE}🔄 协调器路由: $request${NC}"
    
    case $request in
        "list-tools")
            # 列出所有工具，不评价优劣
            echo -e "${YELLOW}🛠️ 可用工具列表:${NC}"
            find . -name "*.sh" -o -name "*.py" | head -20
            ;;
        "check-health")
            # 健康检查，不修复
            echo -e "${YELLOW}🏥 系统健康检查:${NC}"
            [ -f "./传承验证.sh" ] && ./传承验证.sh
            [ -f "./运维状态监控.sh" ] && ./运维状态监控.sh
            ;;
        "backup-assets")
            # 创建备份，不删除原文件
            echo -e "${YELLOW}💾 创建资产备份...${NC}"
            backup_dir="协调备份_$(date +%Y%m%d_%H%M%S)"
            mkdir -p "$backup_dir"
            find . -maxdepth 1 -name "*.sh" -o -name "*.py" -o -name "*.md" | \
            head -10 | while read file; do
                cp "$file" "$backup_dir/" 2>/dev/null && echo "✅ 备份: $file"
            done
            ;;
        *)
            echo -e "${RED}❌ 未知请求: $request${NC}"
            ;;
    esac
}

# 显示使用说明
show_usage() {
    echo -e "${BLUE}使用方法:${NC}"
    echo "  ./真正协调执行器.sh [动作] [类别]"
    echo ""
    echo -e "${YELLOW}动作:${NC}"
    echo "  coordinate - 协调执行工具"
    echo "  analyze    - 分析资产（只读）"
    echo "  router     - 协调器路由"
    echo ""
    echo -e "${YELLOW}类别 (coordinate时使用):${NC}"
    echo "  legacy     - 传承工具"
    echo "  development - 开发工具"
    echo "  security   - 安全工具"
    echo "  video      - 视频工具"
    echo ""
    echo -e "${GREEN}示例:${NC}"
    echo "  ./真正协调执行器.sh coordinate legacy"
    echo "  ./真正协调执行器.sh analyze"
    echo "  ./真正协调执行器.sh router list-tools"
}

# 主函数
main() {
    local action=$1
    local category=$2
    
    echo -e "${BLUE}========================================${NC}"
    echo -e "${GREEN}🎯 真正协调执行器 - 遵守只增不删原则${NC}"
    echo -e "${BLUE}========================================${NC}"
    
    # 原则验证
    if ! validate_principles "$action"; then
        exit 1
    fi
    
    case $action in
        "coordinate")
            protect_assets coordinate_tools "$category"
            ;;
        "analyze")
            protect_assets analyze_assets
            ;;
        "router")
            protect_assets coordinator_router "$category"
            ;;
        "")
            show_usage
            ;;
        *)
            echo -e "${RED}❌ 未知动作: $action${NC}"
            show_usage
            ;;
    esac
    
    echo -e "${BLUE}========================================${NC}"
    echo -e "${GREEN}🎉 协调执行完成!${NC}"
    echo -e "${YELLOW}📊 文件总数: $(find . -type f | wc -l)${NC}"
    echo -e "${BLUE}========================================${NC}"
}

# 执行主函数
main "$@"
