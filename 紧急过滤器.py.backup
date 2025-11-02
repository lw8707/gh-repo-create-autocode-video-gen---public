#!/usr/bin/env python3
"""
紧急过滤器 - 基于全球安全社区最佳实践
参考：OWASP输入验证、Linux终端安全、ANSI转义处理
"""
import sys
import re
import json

def 紧急过滤(text: str) -> str:
    """立即止血的输入过滤器"""
    
    # 1. 移除终端提示符（基于Bash/Zsh规范）
    text = re.sub(r'(?m)^[~/$#].*?[>#\$]\s+', '', text)
    
    # 2. 清除ANSI/CSI转义序列（基于ECMA-48标准）
    text = re.sub(r'\x1b\[[0-9;]*[mKJHfABCD]', '', text)
    
    # 3. 处理八进制转义序列（Unicode安全）
    text = re.sub(r'\\[0-7]{3}', '', text)
    
    # 4. 括号平衡保护（防止语法错误）
    stack = []
    output = []
    for char in text:
        if char in '([{':
            stack.append(char)
            output.append(char)
        elif char in ')]}':
            if stack and (
                (char == ')' and stack[-1] == '(') or
                (char == ']' and stack[-1] == '[') or 
                (char == '}' and stack[-1] == '{')
            ):
                stack.pop()
                output.append(char)
        else:
            output.append(char)
    
    # 5. 移除控制字符（ASCII控制字符）
    clean_text = ''.join(output)
    clean_text = re.sub(r'[\x00-\x1f\x7f-\x9f]', '', clean_text)
    
    # 6. 长度限制（防止资源耗尽）
    clean_text = clean_text[:4096]
    
    return clean_text

if __name__ == '__main__':
    # 从标准输入读取
    input_data = sys.stdin.read()
    cleaned = 紧急过滤(input_data)
    print(cleaned)
