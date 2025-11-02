#!/bin/bash
echo "🔄 统一调用器"
echo "============"

command="$1"

case "$command" in
    "upload")
        echo "🚀 执行上传功能..."
        if [ -f "一键上传.sh" ]; then
            timeout 30s ./一键上传.sh
            result=$?
            if [ $result -eq 124 ]; then
                echo "❌ 上传超时"
            elif [ $result -eq 0 ]; then
                echo "✅ 上传成功"
            else
                echo "❌ 上传失败 (错误码: $result)"
            fi
        else
            echo "❌ 一键上传.sh 不存在"
        fi
        ;;
        
    "check")
        echo "🔍 系统健康检查..."
        echo "核心脚本状态:"
        for script in "一键上传.sh" "全面诊断.sh" "自动备份.sh" "全面恢复.sh"; do
            if [ -f "$script" ]; then
                echo "  ✅ $script - 存在"
            else
                echo "  ❌ $script - 缺失"
            fi
        done
        ;;
        
    "test")
        echo "🧪 执行测试..."
        ./simple_test.sh
        ;;
        
    *)
        echo "📚 可用命令:"
        echo "  ./unified_caller.sh upload  - 上传"
        echo "  ./unified_caller.sh check   - 健康检查"
        echo "  ./unified_caller.sh test    - 测试"
        ;;
esac
