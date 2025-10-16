#!/bin/bash
# 第16轮永续自动上传监控
# 基于完全理解现有成熟方案

echo "🚀 启动第16轮永续自动上传监控..."
echo "监控目录: $(pwd)"
echo "目标仓库: https://github.com/lw8707/gh-repo-create-autocode-video-gen---public"

# 确保上传脚本存在且可执行
if [ ! -f "auto_upload_fixed.sh" ]; then
    echo "❌ 自动上传脚本不存在，正在重新创建..."
    python3 修复自动上传.py
fi

chmod +x auto_upload_fixed.sh

# 创建后台监控进程
nohup bash -c '
while true; do
    echo "$(date): 执行自动上传检查..."
    ./auto_upload_fixed.sh
    
    # 记录上传日志
    echo "$(date): 上传检查完成" >> upload_monitor.log
    
    # 5分钟检查一次
    sleep 300
done
' > upload_monitor.log 2>&1 &

MONITOR_PID=$!
echo $MONITOR_PID > upload_monitor.pid

echo "✅ 永续上传监控已启动 (PID: $MONITOR_PID)"
echo "📝 日志文件: upload_monitor.log"
echo "🛑 停止监控: kill $(cat upload_monitor.pid)"

# 立即执行一次上传
echo "📤 立即执行首次上传..."
./auto_upload_fixed.sh
