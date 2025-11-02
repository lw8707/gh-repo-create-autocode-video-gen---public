#!/bin/bash
# 安全文档创建 - 防止中断导致文档不完整
safe_create() {
    local file="$1"
    local content="$2"
    
    # 先创建临时文件
    local temp_file="${file}.temp_$$"
    echo "$content" > "$temp_file"
    
    # 验证内容完整性
    if [[ $(echo "$content" | wc -l) -eq $(wc -l < "$temp_file") ]]; then
        mv "$temp_file" "$file"
        echo "✅ $file 创建成功"
    else
        rm "$temp_file"
        echo "❌ $file 创建失败，内容不完整"
        return 1
    fi
}
