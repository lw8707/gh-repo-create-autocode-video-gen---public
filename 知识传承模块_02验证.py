# 知识传承模块2: 完整性验证
    def verify_knowledge_integrity(self):
        """验证知识体系完整性"""
        print("🔍 验证知识传承完整性...")
        
        integrity_report = {
            "verification_time": datetime.now().isoformat(),
            "critical_files": [],
            "missing_files": [],
            "backup_status": "未知",
            "git_status": "未知"
        }
        
        # 检查核心文件
        for file in self.heritage_files:
            if os.path.exists(file):
                file_info = {
                    "name": file,
                    "size": os.path.getsize(file),
                    "md5": self.calculate_md5(file),
                    "status": "存在"
                }
                integrity_report["critical_files"].append(file_info)
            else:
                integrity_report["missing_files"].append(file)
        
        # 检查备份状态
        backup_dirs = [d for d in os.listdir('.') if d.startswith('备份快照_')]
        integrity_report["backup_status"] = f"找到{len(backup_dirs)}个备份快照"
        
        return integrity_report
    
    def calculate_md5(self, filename):
        """计算文件MD5"""
        hash_md5 = hashlib.md5()
        with open(filename, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()
