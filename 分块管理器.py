#!/usr/bin/env python3
import os
import hashlib

class ChunkManager:
    def __init__(self):
        self.chunks = []
    
    def add_chunk(self, content):
        """添加内容块"""
        self.chunks.append(content)
        
    def build_file(self, filename):
        """构建完整文件"""
        full_content = "".join(self.chunks)
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(full_content)
        
        # 计算文件校验和
        md5 = hashlib.md5(full_content.encode('utf-8')).hexdigest()
        print(f"✅ 文件生成成功: {filename}")
        print(f"📊 文件大小: {len(full_content)} 字符")
        print(f"🔐 MD5校验: {md5}")
        return md5

manager = ChunkManager()
print("🚀 分块输入管理器已启动")
print("📝 请按顺序添加内容块...")
