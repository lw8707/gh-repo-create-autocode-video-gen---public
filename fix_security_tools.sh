#!/bin/bash
echo "🔧 修复安全工具链..."

# 安装替代安全扫描工具
pkg install -y nikto sqlmap -y
echo "✅ 安装替代安全工具: nikto, sqlmap"

# 安装容器替代方案
pkg install -y proot proot-distro -y
echo "✅ 安装容器替代方案: proot"

# 修复zk配置目录
mkdir -p ~/.zk
echo "✅ 创建zk配置目录"

# 验证已安装工具
echo "📊 已安装安全工具验证:"
which nmap && echo "✅ nmap: $(nmap --version | head -1)"
which radare2 && echo "✅ radare2: $(r2 -v | head -1)"
which nikto && echo "✅ nikto: $(nikto -v 2>/dev/null | head -1)"
which sqlmap && echo "✅ sqlmap: $(sqlmap --version | head -1)"

echo "🛡️ 安全工具链修复完成"
