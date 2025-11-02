#!/bin/bash
echo "🔧 本地开发流水线启动..."

# 1. 代码质量检查
echo "📋 运行代码检查..."
python -m pylint **/*.py --exit-zero
python -m bandit -r . -f json -o bandit_report.json

# 2. 安全扫描
echo "🛡️ 运行安全扫描..."
python enhanced_security_demo.py

# 3. 测试
echo "🧪 运行测试..."
if [ -d "tests" ]; then
    python -m pytest tests/ -v
else
    echo "⚠️ 未找到测试目录，跳过测试"
fi

# 4. 构建
echo "🏗️ 构建应用..."
if command -v pyinstaller >/dev/null 2>&1; then
    pyinstaller --onefile main.py 2>/dev/null || echo "⚠️ 构建失败，继续..."
else
    echo "⚠️ pyinstaller未安装，跳过构建"
fi

echo "✅ 本地流水线完成"
