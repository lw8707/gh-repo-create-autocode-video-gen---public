#!/bin/bash
echo "🔒 部署零信任安全架构..."

# 网络隔离
wg genkey | tee privatekey | wg pubkey > publickey
echo "✅ WireGuard密钥对生成完成"

# 安全扫描工具部署
pkg install nmap -y
pkg install lynis -y

# 创建安全监控
cat > /data/data/com.termux/files/usr/etc/security_monitor.sh << 'MONITOR_EOF'
#!/bin/bash
while true; do
    echo "$(date): 系统安全状态监控中..."
    netstat -tuln | grep -E ":(80|443|22)" >> security_log.txt
    sleep 300
done
MONITOR_EOF

chmod +x /data/data/com.termux/files/usr/etc/security_monitor.sh
nohup /data/data/com.termux/files/usr/etc/security_monitor.sh &
