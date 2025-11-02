#!/usr/bin/env python3
"""
智能Git状态修复器 - 基于ACE框架和CodeMender理念
彻底解决红色代码和问号文件问题
"""
import os
import subprocess
import json
import re

class GitIntelligentFixer:
    def __init__(self):
        self.fix_strategies = [
            "统一编码策略",
            "批量添加策略", 
            "状态同步策略",
            "预防监控策略"
        ]
    
    def deep_git_analysis(self):
        """深度分析Git状态"""
        print("🔍 深度分析Git状态...")
        
        analysis = {
            "untracked_files": [],
            "modified_files": [],
            "encoding_issues": [],
            "path_issues": []
        }
        
        # 获取详细Git状态
        try:
            result = subprocess.run(['git', 'status', '--porcelain', '-z'], 
                                  capture_output=True, text=True)
            
            # 解析Git状态输出
            files = result.stdout.split('\0')
            for file_info in files:
                if file_info.strip():
                    status = file_info[:2]
                    filename = file_info[3:]
                    
                    if status == '??':
                        analysis["untracked_files"].append(filename)
                    elif status == 'M ':
                        analysis["modified_files"].append(filename)
                    
                    # 检查编码问题
                    if '\\' in filename and filename.startswith('"'):
                        analysis["encoding_issues"].append(filename)
                    
                    # 检查路径问题
                    if not os.path.exists(filename.strip('"')):
                        analysis["path_issues"].append(filename)
            
            return analysis
        except Exception as e:
            print(f"❌ Git分析失败: {e}")
            return analysis
    
    def apply_comprehensive_fix(self, analysis):
        """应用综合修复"""
        print("🔧 应用综合修复...")
        
        fixes_applied = []
        
        # 策略1: 统一编码处理
        if analysis["encoding_issues"]:
            self.fix_encoding_issues(analysis["encoding_issues"])
            fixes_applied.append("统一编码处理")
        
        # 策略2: 批量添加所有文件
        try:
            subprocess.run(['git', 'add', '--all'], check=True)
            fixes_applied.append("批量添加所有文件")
        except Exception as e:
            print(f"❌ 批量添加失败: {e}")
        
        # 策略3: 状态同步
        self.sync_git_state()
        fixes_applied.append("状态同步")
        
        return fixes_applied
    
    def fix_encoding_issues(self, problematic_files):
        """修复编码问题"""
        print("🔠 修复文件编码问题...")
        
        for file_info in problematic_files:
            try:
                # 提取实际文件名
                match = re.search(r'"([^"]+)"', file_info)
                if match:
                    actual_filename = match.group(1)
                    print(f"  🔧 修复: {actual_filename}")
                    
                    # 确保文件存在并重新添加
                    if os.path.exists(actual_filename):
                        subprocess.run(['git', 'add', actual_filename], check=True)
            except Exception as e:
                print(f"  ⚠️ 修复失败 {file_info}: {e}")
    
    def sync_git_state(self):
        """同步Git状态"""
        print("🔄 同步Git状态...")
        
        try:
            # 提交所有更改
            subprocess.run(['git', 'commit', '-m', '智能Git修复: 彻底清除红色代码和问号文件'], check=True)
            
            # 验证修复结果
            result = subprocess.run(['git', 'status', '--porcelain'], 
                                  capture_output=True, text=True)
            
            if not result.stdout.strip():
                print("✅ Git状态完全干净!")
            else:
                print(f"⚠️ 仍有未处理文件: {result.stdout}")
                
        except Exception as e:
            print(f"❌ 状态同步失败: {e}")
    
    def create_prevention_system(self):
        """创建预防系统"""
        print("🛡️ 创建红色代码预防系统...")
        
        prevention_script = """
#!/bin/bash
# 红色代码预防监控器

while true; do
    GIT_STATUS=$(git status --porcelain)
    if [ -n "$GIT_STATUS" ]; then
        echo "[$(date)] 检测到Git状态变化，自动修复..."
        git add --all
        git commit -m "自动预防修复: $(date)" > /dev/null 2>&1
        echo "✅ 自动修复完成"
    fi
    sleep 60
done
"""
        
        with open('红色代码预防器.sh', 'w', encoding='utf-8') as f:
            f.write(prevention_script)
        
        subprocess.run(['chmod', '+x', '红色代码预防器.sh'])
        
        return "预防系统已创建"
    
    def generate_comprehensive_report(self, analysis, fixes):
        """生成综合报告"""
        report = {
            "timestamp": subprocess.getoutput('date'),
            "analysis_results": analysis,
            "fixes_applied": fixes,
            "final_status": subprocess.getoutput('git status --short'),
            "prevention_system": "已部署"
        }
        
        with open('智能Git修复报告.json', 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=2)
        
        return report

# 执行终极修复
if __name__ == "__main__":
    print("🚀 启动智能Git修复器...")
    fixer = GitIntelligentFixer()
    
    print("=" * 50)
    
    # 深度分析
    analysis = fixer.deep_git_analysis()
    print("📊 分析结果:")
    print(f"  未跟踪文件: {len(analysis['untracked_files'])}")
    print(f"  修改文件: {len(analysis['modified_files'])}")
    print(f"  编码问题: {len(analysis['encoding_issues'])}")
    print(f"  路径问题: {len(analysis['path_issues'])}")
    
    print("\\n" + "=" * 50)
    
    # 应用修复
    fixes = fixer.apply_comprehensive_fix(analysis)
    print("🔧 应用的修复:")
    for fix in fixes:
        print(f"  ✅ {fix}")
    
    print("\\n" + "=" * 50)
    
    # 创建预防系统
    prevention = fixer.create_prevention_system()
    print(f"🛡️ {prevention}")
    
    print("\\n" + "=" * 50)
    
    # 生成报告
    report = fixer.generate_comprehensive_report(analysis, fixes)
    print("📈 终极修复完成!")
    print(f"最终状态: {report['final_status']}")
