#!/usr/bin/env python3
import os
import subprocess
import json
from datetime import datetime

class SmartGitManager:
    def __init__(self):
        self.ignore_patterns = [
            '__pycache__/', '*.pyc', 'chunk_storage.json',
            '传承块*.txt', '备份快照_*/', '*.tmp', '*.bak'
        ]
    
    def analyze_git_status(self):
        """分析Git状态，智能分类文件"""
        print("🔍 智能分析Git状态...")
        
        result = subprocess.run(['git', 'status', '--porcelain'], 
                              capture_output=True, text=True)
        files = result.stdout.strip().split('\n') if result.stdout else []
        
        analysis = {
            "should_track": [],
            "should_ignore": [],
            "unknown": []
        }
        
        for file_info in files:
            if not file_info.strip():
                continue
                
            status = file_info[:2]
            filename = file_info[3:].strip('"')
            
            # 智能分类
            if any(pattern in filename for pattern in ['备份快照_', '__pycache__', '.pyc']):
                analysis["should_ignore"].append(filename)
            elif filename.endswith('.py') and '管理器' in filename:
                analysis["should_track"].append(filename)
            else:
                analysis["unknown"].append(filename)
        
        return analysis
    
    def create_git_health_report(self):
        """创建Git健康报告"""
        analysis = self.analyze_git_status()
        
        report = {
            "timestamp": datetime.now().isoformat(),
            "git_status_analysis": analysis,
            "recommendations": [
                "备份快照目录应本地保存，不上传Git",
                "Python缓存文件应被忽略", 
                "核心代码和文档必须Git跟踪"
            ],
            "health_score": self.calculate_health_score(analysis)
        }
        
        with open('Git健康报告.json', 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=2)
        
        return report
    
    def calculate_health_score(self, analysis):
        """计算Git健康分数"""
        total_files = len(analysis["should_track"]) + len(analysis["should_ignore"]) + len(analysis["unknown"])
        if total_files == 0:
            return 100
        
        ignored_ratio = len(analysis["should_ignore"]) / total_files
        unknown_ratio = len(analysis["unknown"]) / total_files
        
        # 理想状态：所有文件都被正确分类
        score = 100 - (unknown_ratio * 50)
        return max(0, min(100, score))

# 执行分析
if __name__ == "__main__":
    manager = SmartGitManager()
    report = manager.create_git_health_report()
    
    print("📊 Git健康报告:")
    print(f"  健康分数: {report['health_score']}/100")
    print(f"  应跟踪文件: {len(report['git_status_analysis']['should_track'])}")
    print(f"  应忽略文件: {len(report['git_status_analysis']['should_ignore'])}")
    print(f"  未知状态: {len(report['git_status_analysis']['unknown'])}")
    
    print("\n💡 建议:")
    for rec in report['recommendations']:
        print(f"  - {rec}")
