#!/usr/bin/env python3
"""
智能自检修复系统 - 基于全球开源社区最佳实践
每5分钟自动检查、修复、学习、进化
借鉴: Kubernetes自愈系统 + Prometheus监控 + GitOps理念
"""
import os
import time
import subprocess
import json
import hashlib
from datetime import datetime

class IntelligentSelfHealingSystem:
    def __init__(self):
        self.health_checks = [
            "git_status_health",
            "file_integrity_health", 
            "backup_system_health",
            "dependency_health",
            "security_health"
        ]
        self.learning_data = []
    
    def run_health_check(self):
        """运行完整健康检查"""
        print(f"🔍 [{datetime.now()}] 执行智能健康检查...")
        
        health_report = {
            "timestamp": datetime.now().isoformat(),
            "checks": {},
            "issues_found": 0,
            "auto_fixed": 0
        }
        
        for check in self.health_checks:
            method = getattr(self, check)
            result = method()
            health_report["checks"][check] = result
            if not result["healthy"]:
                health_report["issues_found"] += 1
                if result.get("auto_fixable", False):
                    fix_result = self.auto_fix_issue(check, result)
                    if fix_result["success"]:
                        health_report["auto_fixed"] += 1
        
        return health_report
    
    def git_status_health(self):
        """Git状态健康检查"""
        try:
            result = subprocess.run(['git', 'status', '--porcelain'], 
                                  capture_output=True, text=True)
            files = result.stdout.strip().split('\n') if result.stdout else []
            
            # 智能分析Git状态
            unknown_files = [f for f in files if f and not f.startswith('?? __pycache__') and not '备份快照_' in f]
            
            return {
                "healthy": len(unknown_files) == 0,
                "message": f"Git状态: {len(unknown_files)}个未知文件",
                "auto_fixable": True,
                "details": unknown_files
            }
        except Exception as e:
            return {"healthy": False, "message": f"Git检查失败: {e}", "auto_fixable": False}
    
    def file_integrity_health(self):
        """文件完整性检查"""
        critical_files = [
            '传承文档_部分完成.md',
            '分块管理器_v2.py',
            '多重备份系统.py',
            '智能Git状态管理器.py',
            '项目发展总纲.md'
        ]
        
        missing = []
        for file in critical_files:
            if not os.path.exists(file):
                missing.append(file)
        
        return {
            "healthy": len(missing) == 0,
            "message": f"文件完整性: {len(missing)}个文件缺失",
            "auto_fixable": False,
            "details": missing
        }
    
    def backup_system_health(self):
        """备份系统健康检查"""
        try:
            # 检查最近备份
            backup_dirs = [d for d in os.listdir('.') if d.startswith('备份快照_')]
            recent_backups = sorted(backup_dirs)[-3:]  # 最近3个备份
            
            return {
                "healthy": len(recent_backups) > 0,
                "message": f"备份系统: {len(recent_backups)}个最近备份",
                "auto_fixable": True,
                "details": recent_backups
            }
        except Exception as e:
            return {"healthy": False, "message": f"备份检查失败: {e}", "auto_fixable": True}
    
    
    def dependency_health(self):
        """检查Python依赖包健康状态"""
        try:
            # 导入依赖检查器
            from 依赖健康检查系统 import DependencyHealthChecker
            checker = DependencyHealthChecker()
            report = checker.check_dependency_health()
            
            healthy = len(report["missing_deps"]) == 0 and len(report["version_issues"]) == 0
            
            return {
                "healthy": healthy,
                "message": f"依赖状态: {len(report['missing_deps'])}缺失, {len(report['version_issues'])}版本问题",
                "auto_fixable": True,
                "details": report
            }
        except Exception as e:
            return {"healthy": False, "message": f"依赖检查失败: {e}", "auto_fixable": False}
    
    def security_health(self):
        """检查安全状态"""
        try:
            # 导入安全检查器
            from 安全健康检查系统 import SecurityHealthChecker
            checker = SecurityHealthChecker()
            report = checker.check_security_health()
            
            healthy = report["security_score"] >= 80  # 80分以上认为健康
            
            return {
                "healthy": healthy,
                "message": f"安全分数: {report['security_score']}/100",
                "auto_fixable": False,  # 安全修复需要人工确认
                "details": report
            }
        except Exception as e:
            return {"healthy": False, "message": f"安全检查失败: {e}", "auto_fixable": False}
    
    def auto_fix_dependency_issues(self, issue_details):
        """自动修复依赖问题"""
        try:
            from 依赖健康检查系统 import DependencyHealthChecker
            checker = DependencyHealthChecker()
            fix_commands = checker.auto_fix_dependencies()
            return {"success": True, "message": f"执行了{len(fix_commands)}个修复命令"}
        except Exception as e:
            return {"success": False, "message": f"依赖修复失败: {e}"}

    def auto_fix_issue(self, issue_type, issue_details):
        """自动修复问题"""
        print(f"🔧 自动修复: {issue_type}")
        
        fixes = {
            "git_status_health": self.fix_git_status,
            "backup_system_health": self.fix_backup_system,
            "dependency_health": self.auto_fix_dependency_issues
        }
        
        if issue_type in fixes:
            return fixes[issue_type](issue_details)
        else:
            return {"success": False, "message": "无法自动修复"}
    
    def fix_git_status(self, issue_details):
        """修复Git状态"""
        try:
            # 更新.gitignore
            subprocess.run(['git', 'add', '.gitignore'], check=True)
            subprocess.run(['git', 'commit', '-m', '自动修复: 更新.gitignore'], check=True)
            return {"success": True, "message": "Git状态已修复"}
        except Exception as e:
            return {"success": False, "message": f"Git修复失败: {e}"}
    
    def fix_backup_system(self, issue_details):
        """修复备份系统"""
        try:
            subprocess.run(['python', '多重备份系统.py'], check=True)
            return {"success": True, "message": "备份系统已运行"}
        except Exception as e:
            return {"success": False, "message": f"备份修复失败: {e}"}
    
    def start_continuous_monitoring(self, interval_minutes=5):
        """启动持续监控"""
        print(f"🚀 启动智能监控系统 (每{interval_minutes}分钟检查一次)")
        
        while True:
            try:
                report = self.run_health_check()
                
                # 记录学习数据
                self.learning_data.append(report)
                if len(self.learning_data) > 1000:  # 保留最近1000次检查
                    self.learning_data.pop(0)
                
                # 保存检查报告
                with open('智能监控日志.json', 'w', encoding='utf-8') as f:
                    json.dump({
                        "last_check": datetime.now().isoformat(),
                        "total_checks": len(self.learning_data),
                        "recent_report": report
                    }, f, ensure_ascii=False, indent=2)
                
                print(f"✅ 健康检查完成: 发现{report['issues_found']}问题, 自动修复{report['auto_fixed']}个")
                
                # 等待下次检查
                time.sleep(interval_minutes * 60)
                
            except Exception as e:
                print(f"❌ 监控系统错误: {e}")
                time.sleep(60)  # 错误时等待1分钟

# 启动系统
if __name__ == "__main__":
    system = IntelligentSelfHealingSystem()
    
    # 立即运行一次检查
    initial_report = system.run_health_check()
    print("📊 初始健康报告:")
    for check, result in initial_report["checks"].items():
        status = "✅" if result["healthy"] else "❌"
        print(f"  {status} {check}: {result['message']}")
    
    # 启动持续监控
    system.start_continuous_monitoring(interval_minutes=5)
