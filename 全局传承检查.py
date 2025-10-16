#!/usr/bin/env python3
"""
第16轮全局传承完整性检查
基于完全理解现有仓库状态
"""

import os
import json
from pathlib import Path
import subprocess

class LegacyHealthChecker:
    def __init__(self):
        self.repo_path = Path(".").resolve()
        self.critical_files = [
            # 核心传承文件
            "终极传承体系.md", "先进技术集成器.py", 
            "一键传承上传.sh", "传承健康检查器.py",
            
            # 架构核心
            "AI增强传承系统.py", "n8n工作流集成器.py",
            "智能体生态系统.py", "AI编程工作流系统.py",
            
            # 文档总结
            "第16轮完成总结.md", "上传状态报告.md"
        ]
    
    def check_critical_files(self):
        """检查关键文件完整性"""
        print("🔍 检查关键文件完整性...")
        
        missing_files = []
        existing_files = []
        
        for file in self.critical_files:
            if os.path.exists(file):
                existing_files.append(file)
                print(f"✅ {file}")
            else:
                missing_files.append(file)
                print(f"❌ {file} - 缺失")
        
        return existing_files, missing_files
    
    def check_upload_mechanism(self):
        """检查上传机制状态"""
        print("🔧 检查上传机制状态...")
        
        upload_scripts = [
            "auto_upload_fixed.sh", "一键上传.sh", "auto_upload.sh",
            "自动备份.sh", "一键传承上传.sh"
        ]
        
        working_scripts = []
        for script in upload_scripts:
            if os.path.exists(script):
                # 检查脚本是否可执行
                if os.access(script, os.X_OK):
                    working_scripts.append(script)
                    print(f"✅ {script} - 可执行")
                else:
                    print(f"⚠️ {script} - 存在但不可执行")
        
        return working_scripts
    
    def check_git_health(self):
        """检查Git健康状况"""
        print("📊 检查Git健康状况...")
        
        checks = {}
        
        # 检查远程仓库
        result = subprocess.run(["git", "remote", "-v"], capture_output=True, text=True)
        checks['remote'] = "origin" in result.stdout
        
        # 检查分支状态
        result = subprocess.run(["git", "branch", "--show-current"], capture_output=True, text=True)
        checks['branch'] = result.stdout.strip() if result.returncode == 0 else "未知"
        
        # 检查未提交更改
        result = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True)
        checks['uncommitted'] = len(result.stdout.strip().split('\n')) if result.stdout.strip() else 0
        
        # 检查推送权限
        result = subprocess.run(["git", "push", "--dry-run"], capture_output=True, text=True)
        checks['push_access'] = result.returncode == 0
        
        for check, value in checks.items():
            status = "✅" if value else "❌"
            print(f"{status} {check}: {value}")
        
        return checks
    
    def generate_health_report(self):
        """生成健康检查报告"""
        print("📋 生成全局健康检查报告...")
        
        existing_files, missing_files = self.check_critical_files()
        working_scripts = self.check_upload_mechanism()
        git_health = self.check_git_health()
        
        report = {
            "generation": 16,
            "timestamp": subprocess.getoutput("date '+%Y-%m-%d %H:%M:%S'"),
            "critical_files": {
                "total": len(self.critical_files),
                "existing": len(existing_files),
                "missing": len(missing_files),
                "missing_list": missing_files
            },
            "upload_mechanism": {
                "working_scripts": working_scripts,
                "primary_script": "auto_upload_fixed.sh"
            },
            "git_health": git_health,
            "overall_health": "healthy" if len(missing_files) == 0 and git_health['push_access'] else "needs_attention"
        }
        
        # 保存报告
        with open("第16轮传承健康报告.json", "w") as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        
        print("✅ 健康报告已保存: 第16轮传承健康报告.json")
        return report

def main():
    checker = LegacyHealthChecker()
    report = checker.generate_health_report()
    
    print("\\n" + "=" * 60)
    print("🎯 第16轮全局传承健康检查完成")
    print("=" * 60)
    
    # 输出总结
    health_status = "✅ 健康" if report['overall_health'] == "healthy" else "⚠️ 需要关注"
    print(f"整体状态: {health_status}")
    print(f"关键文件: {report['critical_files']['existing']}/{report['critical_files']['total']} 存在")
    print(f"上传脚本: {len(report['upload_mechanism']['working_scripts'])} 个可用")
    print(f"Git推送: {'✅ 正常' if report['git_health']['push_access'] else '❌ 异常'}")
    
    if report['critical_files']['missing']:
        print("\\n🚨 缺失的关键文件:")
        for file in report['critical_files']['missing_list']:
            print(f"   - {file}")

if __name__ == "__main__":
    main()
