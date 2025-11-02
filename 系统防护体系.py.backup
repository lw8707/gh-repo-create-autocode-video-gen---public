#!/usr/bin/env python3
"""
系统防护体系 - 基于企业级安全架构
集成：输入验证、输出编码、会话管理、速率限制
参考：NIST网络安全框架、OWASP Top 10、零信任架构
"""
import re
import time
import hashlib
from collections import defaultdict

class 系统防护:
    def __init__(self):
        self.请求记录 = defaultdict(list)
        self.规则库 = self.加载安全规则()
        
    def 加载安全规则(self):
        """加载已知的安全规则"""
        return [
            # 终端转义序列
            (r'\x1b\[[0-9;]*[mK]', '终端转义序列'),
            # 八进制转义
            (r'\\[0-7]{3}', '八进制转义序列'),
            # 路径遍历
            (r'\.\./|\./|/~', '路径遍历攻击'),
            # 命令注入
            (r'[;&|`]', '命令注入特征'),
            # 资源耗尽
            (r'.{10000,}', '输入过长'),
        ]
    
    def 输入验证(self, 输入数据, 用户标识=None):
        """多层输入验证"""
        
        # 1. 速率限制
        if not self.检查速率限制(用户标识):
            raise SecurityException("请求过于频繁")
        
        # 2. 规则匹配
        for 模式, 描述 in self.规则库:
            if re.search(模式, 输入数据):
                raise SecurityException(f"检测到{描述}")
        
        # 3. 编码验证
        try:
            输入数据.encode('utf-8')
        except UnicodeEncodeError:
            raise SecurityException("编码格式异常")
        
        return 输入数据[:4096]  # 长度限制
    
    def 检查速率限制(self, 用户标识, 时间窗口=60, 最大请求数=100):
        """速率限制"""
        if not 用户标识:
            return True
            
        当前时间 = time.time()
        时间戳列表 = self.请求记录[用户标识]
        
        # 清理过期请求
        时间戳列表[:] = [ts for ts in 时间戳列表 if 当前时间 - ts < 时间窗口]
        
        if len(时间戳列表) >= 最大请求数:
            return False
            
        时间戳列表.append(当前时间)
        return True
    
    def 安全输出(self, 输出数据):
        """安全输出处理"""
        # 1. 移除控制字符
        安全输出 = re.sub(r'[\x00-\x1f\x7f-\x9f]', '', 输出数据)
        
        # 2. 转义HTML特殊字符
        转义映射 = {
            '&': '&amp;',
            '<': '&lt;', 
            '>': '&gt;',
            '"': '&quot;',
            "'": '&#x27;'
        }
        for 原字符, 转义字符 in 转义映射.items():
            安全输出 = 安全输出.replace(原字符, 转义字符)
            
        return 安全输出

class SecurityException(Exception):
    """安全异常"""
    pass

# 使用示例
if __name__ == '__main__':
    防护 = 系统防护()
    
    try:
        # 测试安全输入
        测试输入 = "正常文本内容"
        安全输入 = 防护.输入验证(测试输入, "test_user")
        安全输出 = 防护.安全输出(安全输入)
        
        print("✅ 系统防护测试通过")
        print(f"输入: {测试输入}")
        print(f"输出: {安全输出}")
        
    except SecurityException as e:
        print(f"❌ 安全异常: {e}")
