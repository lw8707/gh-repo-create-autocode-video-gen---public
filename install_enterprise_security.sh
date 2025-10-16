#!/bin/bash
echo "🛡️ 安装企业级安全工具链..."

# 网络扫描和监控
pkg install -y nmap tcpdump tshark

# 加密工具增强  
pkg install -y gnutls libsodium cryptsetup

# 安全开发工具
pkg install -y radare2 binutils patchelf

# 容器安全工具
pkg install -y runc skopeo

echo "✅ 企业级安全工具安装完成"
echo "可用工具:"
echo "  - nmap: 网络扫描"
echo "  - tcpdump: 网络流量分析" 
echo "  - radare2: 逆向工程"
echo "  - gnutls: 加密通信"
