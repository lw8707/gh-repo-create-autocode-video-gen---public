#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
【GitHub认证修复版】
修复目录路径问题，适应当前目录结构
"""

import os
import subprocess

class GitHub认证修复版:
    def __init__(self):
        # 自动检测当前目录
        self.当前目录 = os.getcwd()
        print(f"📁 当前目录: {self.当前目录}")
        
        # 判断是否在正确的目录中
        if self.当前目录.endswith("我的智能体课程"):
            self.项目根目录 = os.path.dirname(self.当前目录)
            self.项目目录 = self.当前目录
        else:
            self.项目根目录 = self.当前目录
            self.项目目录 = os.path.join(self.当前目录, "我的智能体课程")
    
    def 检查当前状态(self):
        """检查当前GitHub状态"""
        print("🔍 【GitHub状态检查】")
        print("=" * 50)
        
        try:
            # 检查项目目录是否存在
            if not os.path.exists(self.项目目录):
                print(f"❌ 项目目录不存在: {self.项目目录}")
                print("   请确保项目结构正确")
                return False
            
            # 进入项目目录检查
            os.chdir(self.项目目录)
            
            print("1. 检查Git配置...")
            配置命令 = [
                "git config --global user.name",
                "git config --global user.email", 
                "git remote -v"
            ]
            
            for 命令 in 配置命令:
                try:
                    结果 = subprocess.run(命令, shell=True, capture_output=True, text=True)
                    输出 = 结果.stdout.strip() if 结果.stdout else "未设置"
                    print(f"   {命令}: {输出}")
                except Exception as e:
                    print(f"   {命令}: 错误 - {e}")
            
            # 检查本地更改
            print("2. 检查本地更改...")
            状态结果 = subprocess.run("git status", shell=True, capture_output=True, text=True)
            if 状态结果.returncode == 0:
                if "Changes" in 状态结果.stdout or "更改" in 状态结果.stdout:
                    print("   仓库状态: 有未提交的更改")
                else:
                    print("   仓库状态: 无更改")
            else:
                print("   仓库状态: 检查失败")
            
            # 回到原始目录
            os.chdir(self.当前目录)
            return True
            
        except Exception as e:
            print(f"❌ 状态检查失败: {e}")
            # 确保回到原始目录
            os.chdir(self.当前目录)
            return False
    
    def 执行最简认证流程(self):
        """执行最简单的认证流程"""
        print("\n🎯 【执行最简GitHub认证流程】")
        print("=" * 50)
        
        try:
            # 进入项目目录
            os.chdir(self.项目目录)
            
            print("步骤1: 添加所有文件到Git...")
            添加结果 = subprocess.run("git add .", shell=True, capture_output=True, text=True)
            if 添加结果.returncode != 0:
                print("⚠️ 添加文件时出现问题")
            
            print("步骤2: 提交更改...")
            提交结果 = subprocess.run('git commit -m "修复目录问题后的提交"', shell=True, capture_output=True, text=True)
            if 提交结果.returncode != 0:
                print("⚠️ 提交可能无更改，继续执行推送...")
            
            print("步骤3: 执行推送（将要求认证）...")
            print("   当提示 'Username for 'https://github.com':' 时:")
            print("   → 输入: lw8707")
            print("   当提示 'Password for 'https://lw8707@github.com':' 时:")
            print("   → 粘贴你的GitHub Personal Access Token")
            print("")
            print("💡 Token获取方法:")
            print("   1. 访问: https://github.com/settings/tokens")
            print("   2. 生成新Token，勾选repo权限")
            print("   3. 复制Token字符串")
            print("")
            print("准备开始认证...")
            
            # 执行推送
            推送结果 = subprocess.run("git push -u origin main", shell=True)
            
            if 推送结果.returncode == 0:
                print("🎉 GitHub认证成功！")
                return True
            else:
                print("❌ 推送失败，需要手动处理认证")
                print("💡 请检查Token是否正确，或重新生成Token")
                return False
                
        except Exception as e:
            print(f"❌ 认证流程失败: {e}")
            return False
        finally:
            # 确保回到原始目录
            os.chdir(self.当前目录)
    
    def 生成极简指南(self):
        """生成极简操作指南"""
        指南 = """
🎯 【极简GitHub认证步骤】

1. 获取Token:
   - 浏览器打开: https://github.com/settings/tokens
   - 点击 Generate new token → Generate new token (classic)
   - 名称: Termux开发
   - 过期: 90 days
   - 权限: ✅ repo (全选)
   - 生成并复制Token

2. 在Termux中:
   - 看到 'Username:' 输入: lw8707
   - 看到 'Password:' 粘贴Token
   - 按回车

3. 成功标志:
   - 看到: Writing objects: 100%
   - 回到命令提示符 $
"""
        print(指南)
    
    def 运行修复方案(self):
        """运行修复后的解决方案"""
        print("🚀 【开始GitHub认证修复方案】")
        print(f"📁 项目根目录: {self.项目根目录}")
        print(f"📁 项目目录: {self.项目目录}")
        
        # 检查状态
        if not self.检查当前状态():
            print("❌ 状态检查失败，无法继续")
            return False
        
        # 显示指南
        self.生成极简指南()
        
        # 执行认证
        print("\n🎯 准备执行认证流程...")
        input("请按回车键开始（确保已准备好Token）...")
        
        成功 = self.执行最简认证流程()
        
        if 成功:
            print("\n🎉 【GitHub认证成功完成！】")
            print("💾 现在代码可以安全存储在GitHub了！")
            print("🌐 访问: https://github.com/lw8707/gh-repo-create-autocode-video-gen---public")
            
            # 创建成功标记文件
            with open("认证成功.txt", "w") as f:
                f.write(f"GitHub认证成功时间: {subprocess.getoutput('date')}")
            print("✅ 已创建认证成功标记文件")
        else:
            print("\n⚠️ 【认证需要手动处理】")
            print("💡 请按照上述指南获取正确Token")
        
        return 成功

# 运行修复方案
print("正在初始化GitHub认证修复版...")
修复方案 = GitHub认证修复版()
修复方案.运行修复方案()
