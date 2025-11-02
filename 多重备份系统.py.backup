#!/usr/bin/env python3
import os
import shutil
import hashlib
import json
from datetime import datetime

class MultiBackupSystem:
    def __init__(self):
        self.backup_locations = [
            "本地Git仓库",
            "GitHub远程仓库", 
            "本地压缩包备份",
            "云存储备份（待配置）"
        ]
        
    def create_backup_snapshot(self):
        """创建备份快照"""
        print("📦 创建多重备份快照...")
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        snapshot_dir = f"备份快照_{timestamp}"
        os.makedirs(snapshot_dir, exist_ok=True)
        
        # 备份关键文件
        critical_files = [
            '传承文档_部分完成.md',
            '分块管理器_v2.py', 
            'chunk_storage.json',
            '项目发展总纲.md',
            'GitHub认证状态.txt'
        ]
        
        backed_up = []
        for file in critical_files:
            if os.path.exists(file):
                shutil.copy2(file, os.path.join(snapshot_dir, file))
                backed_up.append(file)
        
        # 创建备份元数据
        metadata = {
            "timestamp": timestamp,
            "backup_files": backed_up,
            "total_size": sum(os.path.getsize(f) for f in backed_up),
            "checksum": self.calculate_checksum(backed_up)
        }
        
        with open(os.path.join(snapshot_dir, "备份元数据.json"), 'w', encoding='utf-8') as f:
            json.dump(metadata, f, ensure_ascii=False, indent=2)
        
        print(f"✅ 备份快照创建完成: {snapshot_dir}")
        print(f"📊 备份文件: {len(backed_up)}个")
        return snapshot_dir
    
    def calculate_checksum(self, files):
        """计算文件校验和"""
        combined_hash = hashlib.md5()
        for file in files:
            with open(file, 'rb') as f:
                for chunk in iter(lambda: f.read(4096), b""):
                    combined_hash.update(chunk)
        return combined_hash.hexdigest()
    
    def verify_integrity(self):
        """验证系统完整性"""
        print("🔍 验证系统完整性...")
        
        essential_files = [
            '传承文档_部分完成.md',
            '分块管理器_v2.py',
            'chunk_storage.json',
            '.gitignore'
        ]
        
        missing = []
        for file in essential_files:
            if not os.path.exists(file):
                missing.append(file)
        
        if missing:
            print(f"❌ 缺失文件: {missing}")
            return False
        else:
            print("✅ 所有关键文件完整")
            return True

# 执行备份
if __name__ == "__main__":
    backup_system = MultiBackupSystem()
    
    print("🚀 启动多重备份系统")
    print("=" * 50)
    
    # 验证完整性
    if backup_system.verify_integrity():
        # 创建备份快照
        snapshot = backup_system.create_backup_snapshot()
        
        print("\n📋 备份位置:")
        for location in backup_system.backup_locations:
            print(f"  ✅ {location}")
            
        print(f"\n🎉 多重备份完成! 快照: {snapshot}")
    else:
        print("❌ 系统完整性验证失败，请先修复缺失文件")
