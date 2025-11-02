#!/usr/bin/env python3
"""
智能自检修复系统升级补丁
添加：dependency_health 和 security_health 方法
基于全球最佳实践的安全和依赖检查
"""
import os

def upgrade_selfhealing_system():
    """升级智能自检修复系统"""
    
    # 读取原文件
    with open('智能自检修复系统.py', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 检查是否已经修复
    if 'def dependency_health(self):' in content and 'def security_health(self):' in content:
        print("✅ 智能自检系统已是最新版本")
        return True
    
    # 找到health_checks列表的位置
    health_checks_pattern = 'self.health_checks = ['
    if health_checks_pattern not in content:
        print("❌ 无法找到health_checks定义")
        return False
    
    # 在health_checks中添加新检查项
    new_health_checks = '''self.health_checks = [
            "git_status_health",
            "file_integrity_health", 
            "backup_system_health",
            "dependency_health",
            "security_health"
        ]'''
    
    content = content.replace(
        '''self.health_checks = [
            "git_status_health",
            "file_integrity_health", 
            "backup_system_health"
        ]''',
        new_health_checks
    )
    
    # 添加新的健康检查方法
    new_methods = '''
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
'''
    
    # 在auto_fix_issue方法前插入新方法
    auto_fix_pattern = 'def auto_fix_issue(self, issue_type, issue_details):'
    if auto_fix_pattern in content:
        parts = content.split(auto_fix_pattern)
        new_content = parts[0] + new_methods + '\n    ' + auto_fix_pattern + parts[1]
        
        # 更新auto_fix_issue方法，添加对新问题的修复
        if '"git_status_health"' in new_content and '"backup_system_health"' in new_content:
            # 在fixes字典中添加新条目
            fixes_dict = '''fixes = {
            "git_status_health": self.fix_git_status,
            "backup_system_health": self.fix_backup_system,
            "dependency_health": self.auto_fix_dependency_issues
        }'''
            
            new_content = new_content.replace(
                '''fixes = {
            "git_status_health": self.fix_git_status,
            "backup_system_health": self.fix_backup_system
        }''',
                fixes_dict
            )
        
        # 写入更新后的内容
        with open('智能自检修复系统.py', 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print("✅ 智能自检系统升级完成")
        return True
    else:
        print("❌ 无法找到auto_fix_issue方法")
        return False

if __name__ == "__main__":
    success = upgrade_selfhealing_system()
    if success:
        print("\n🔄 验证升级结果...")
        os.system('python 智能自检修复系统.py')
    else:
        print("❌ 升级失败，请手动检查")
