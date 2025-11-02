
#!/bin/bash
# 红色代码预防监控器

while true; do
    GIT_STATUS=$(git status --porcelain)
    if [ -n "$GIT_STATUS" ]; then
        echo "[$(date)] 检测到Git状态变化，自动修复..."
        git add --all
        git commit -m "自动预防修复: $(date)" > /dev/null 2>&1
        echo "✅ 自动修复完成"
    fi
    sleep 60
done
