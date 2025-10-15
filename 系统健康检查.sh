#!/bin/bash
echo "🏥 系统健康检查启动..."

# 检查核心组件
组件列表=("GitHub认证" "记忆系统" "脚本执行" "文件同步")

for 组件 in "${组件列表[@]}"; do
    echo "🔍 检查: $组件"
    case $组件 in
        "GitHub认证")
            ssh -T git@github.com >/dev/null 2>&1 && echo "✅ 正常" || echo "❌ 异常"
            ;;
        "记忆系统")
            [ -f "项目长期记忆_v2.1.json" ] && echo "✅ 正常" || echo "❌ 异常"
            ;;
        "脚本执行")
            [ -x "一键上传.sh" ] && echo "✅ 正常" || echo "❌ 异常"
            ;;
        "文件同步")
            git status >/dev/null 2>&1 && echo "✅ 正常" || echo "❌ 异常"
            ;;
    esac
done

echo "📊 健康检查完成"
echo "💡 建议: 定期运行此脚本监控系统状态"
