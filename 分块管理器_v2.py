#!/usr/bin/env python3
import os
import json
import hashlib

class ChunkManager:
    def __init__(self):
        self.storage_file = "chunk_storage.json"
        self.load_chunks()
    
    def load_chunks(self):
        """从文件加载已有的块"""
        if os.path.exists(self.storage_file):
            with open(self.storage_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.chunks = data.get('chunks', [])
        else:
            self.chunks = []
    
    def save_chunks(self):
        """保存块到文件"""
        with open(self.storage_file, 'w', encoding='utf-8') as f:
            json.dump({'chunks': self.chunks}, f, ensure_ascii=False, indent=2)
    
    def add_chunk(self, content):
        """添加内容块并持久化保存"""
        self.chunks.append(content)
        self.save_chunks()
        print(f"✅ 块添加成功! 当前总块数: {len(self.chunks)}")
        
    def build_file(self, filename):
        """构建完整文件"""
        full_content = "".join(self.chunks)
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(full_content)
        
        # 计算文件校验和
        md5 = hashlib.md5(full_content.encode('utf-8')).hexdigest()
        print(f"✅ 文件生成成功: {filename}")
        print(f"📊 文件大小: {len(full_content)} 字符")
        print(f"📁 总块数: {len(self.chunks)}")
        print(f"🔐 MD5校验: {md5}")
        return md5

# 创建全局管理器实例
manager = ChunkManager()
print(f"🚀 分块输入管理器V2已启动 (当前块数: {len(manager.chunks)})")
