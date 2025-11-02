#!/bin/bash
echo "🔍 高级功能环境检测"
echo "================="

# 检测FFmpeg
if [ -x "$(command -v ffmpeg)" ]; then
    echo "✅ FFmpeg已安装"
    ffmpeg -version | head -1
else
    echo "❌ FFmpeg未安装"
    echo "💡 建议: pkg install ffmpeg"
fi

# 检测编译环境
if [ -x "$(command -v gcc)" ] || [ -x "$(command -v clang)" ]; then
    echo "✅ 编译环境可用"
else
    echo "❌ 编译环境不可用"
    echo "💡 建议: pkg install clang make"
fi

# 检测存储空间
====$(df ~ | awk 'NR==2 {print $4}')
echo "📦 可用空间: $可用空间"

if [ "${可用空间%G}" -lt 2 ]; then
    echo "⚠️ 存储空间可能不足，建议清理后再安装大型模型"
else
    echo "✅ 存储空间充足"
fi

echo "🎯 根据检测结果决定集成策略"
