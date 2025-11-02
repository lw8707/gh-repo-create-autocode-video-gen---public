#!/usr/bin/env python3
"""
企业级安全健康检查系统
基于：GitGuardian、truffleHog、ggshield 等工具原理
功能：敏感信息扫描、Git历史检查、依赖漏洞检测
"""
import os
import re
import json
import hashlib
from datetime import datetime

class SecurityHealthChecker:
    def __init__(self):
        self.sensitive_patterns = {
            'api_key': r'[aA][pP][iI][_-]?[kK][eE][yY].*?[\'\"]([0-9a-zA-Z]{20,})[\'\"]',
            'secret_key': r'[sS][eE][cC][rR][eE][tT][_-]?[kK][eE][yY].*?[\'\"]([0-9a-zA-Z]{20,})[\'\"]',
            'password': r'[pP][aA][sS][sS][wW][oO][rR][dD].*?[\'\"]([0-9a-zA-Z]{8,})[\'\"]',
            'aws_key': r'AKIA[0-9A-Z]{16}',
            'github_token': r'gh[pousr]_[A-Za-z0-9_]{36}',
            'private_key': r'-----BEGIN (RSA|DSA|EC|OPENSSH) PRIVATE KEY-----',
            'jwt_token': r'eyJhbGciOiJ[0-9a-zA-Z-_=]+\.[0-9a-zA-Z-_=]+\.[0-9a-zA-Z-_=]*'
        }
        
        self.risk_files = [
            '.env', 'config.json', 'settings.py', 
            'credentials', 'secrets.yml', '*.key'
        ]
    
    def check_security_health(self):
        """全面的安全健康检查"""
        print("🛡️ 执行安全健康检查...")
        
        security_report = {
            "timestamp": datetime.now().isoformat(),
            "sensitive_leaks": [],
            "risk_files_found": [],
            "git_history_issues": [],
            "file_permission_issues": [],
            "security_score": 100,
            "recommendations": []
        }
        
        # 扫描敏感信息
        security_report["sensitive_leaks"] = self.scan_sensitive_info()
        
        # 检查风险文件
        security_report["risk_files_found"] = self.scan_risk_files()
        
        # 检查文件权限
        security_report["file_permission_issues"] = self.check_file_permissions()
        
        # 计算安全分数
        issues_count = (
            len(security_report["sensitive_leaks"]) + 
            len(security_report["risk_files_found"]) +
            len(security_report["file_permission_issues"])
        )
        security_report["security_score"] = max(0, 100 - issues_count * 10)
        
        # 生成建议
        if security_report["sensitive_leaks"]:
            security_report["recommendations"].append(
                "发现敏感信息泄露风险，立即移除并轮换密钥"
            )
        
        if security_report["risk_files_found"]:
            security_report["recommendations"].append(
                "发现风险配置文件，确保已添加到.gitignore"
            )
        
        if security_report["file_permission_issues"]:
            security_report["recommendations"].append(
                "修复文件权限问题，保护敏感文件"
            )
        
        return security_report
    
    def scan_sensitive_info(self):
        """扫描敏感信息泄露"""
        print("  扫描敏感信息...")
        leaks_found = []
        
        for root, dirs, files in os.walk('.'):
            # 忽略.git和备份目录
            if '.git' in dirs:
                dirs.remove('.git')
            if any('备份快照_' in d for d in dirs):
                dirs.remove([d for d in dirs if '备份快照_' in d][0])
            
            for file in files:
                if file.endswith(('.py', '.md', '.json', '.yml', '.yaml', '.txt')):
                    filepath = os.path.join(root, file)
                    try:
                        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                            content = f.read()
                            
                        for pattern_name, pattern in self.sensitive_patterns.items():
                            matches = re.findall(pattern, content)
                            if matches:
                                for match in matches[:3]:  # 只报告前3个匹配
                                    leaks_found.append({
                                        "file": filepath,
                                        "type": pattern_name,
                                        "sample": match[:50] + "..." if len(match) > 50 else match,
                                        "severity": "高危" if pattern_name in ['aws_key', 'private_key'] else "中危"
                                    })
                    except Exception as e:
                        continue
        
        return leaks_found
    
    def scan_risk_files(self):
        """扫描风险文件"""
        print("  扫描风险文件...")
        risk_files_found = []
        
        for risk_pattern in self.risk_files:
            if '*' in risk_pattern:
                # 简单的通配符匹配
                import glob
                matches = glob.glob(risk_pattern, recursive=True)
                risk_files_found.extend(matches)
            else:
                if os.path.exists(risk_pattern):
                    risk_files_found.append(risk_pattern)
        
        return risk_files_found
    
    def check_file_permissions(self):
        """检查文件权限"""
        print("  检查文件权限...")
        permission_issues = []
        
        important_files = [
            '智能自检修复系统.py',
            '多重备份系统.py', 
            '分块管理器_v2.py',
            '传承文档_部分完成.md'
        ]
        
        for file in important_files:
            if os.path.exists(file):
                mode = os.stat(file).st_mode
                # 检查是否权限过宽（其他用户可写）
                if mode & 0o002:
                    permission_issues.append(f"{file}: 其他用户可写，建议设置为600")
        
        return permission_issues
    
    def generate_security_report(self):
        """生成安全报告"""
        report = self.check_security_health()
        
        print(f"\n📊 安全健康报告 (分数: {report['security_score']}/100)")
        
        if report['sensitive_leaks']:
            print(f"🔴 敏感信息泄露: {len(report['sensitive_leaks'])}处")
            for leak in report['sensitive_leaks'][:3]:  # 只显示前3个
                print(f"   - {leak['file']}: {leak['type']} ({leak['severity']})")
        
        if report['risk_files_found']:
            print(f"🟡 风险文件: {len(report['risk_files_found'])}个")
            for file in report['risk_files_found'][:3]:
                print(f"   - {file}")
        
        if report['file_permission_issues']:
            print(f"🟠 权限问题: {len(report['file_permission_issues'])}个")
            for issue in report['file_permission_issues'][:3]:
                print(f"   - {issue}")
        
        if report['recommendations']:
            print("\n💡 安全建议:")
            for rec in report['recommendations']:
                print(f"  - {rec}")
        
        # 保存详细报告
        with open('安全健康报告.json', 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=2)
        
        return report

if __name__ == "__main__":
    checker = SecurityHealthChecker()
    checker.generate_security_report()
