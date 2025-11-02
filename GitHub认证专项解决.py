#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
【GitHub认证专项解决】
放弃复杂方案，采用最简单直接的方法
目标：让代码能够推送到GitHub，建立基础记忆存储
"""

import os
import subprocess

class GitHub认证专项解决:
    def 检查当前状态(self):
        """检查当前GitHub状态"""
        print("🔍 【GitHub状态检查】")
        print("=" * 50)
        
        try:
            # 检查是否在正确的目录
            if not os.path.exists("我的智能体课程"):
                print("❌ 错误：不在正确的项目目录中")
                print("   请先执行: cd ~/my-ai-business")
                return False
            
            os.chdir("我的智能体课程")
            
            # 检查Git配置
            print("1. 检查Git配置...")
            配置命令 = [
                "git config --global user.name",
                "git config --global user.email", 
                "git remote -v"
            ]
            
            for 命令 in 配置命令:
                结果 = subprocess.run(命令, shell=True, capture_output=True, text=True)
                print(f"   {命令}: {结果.stdout.strip() if 结果.returncode == 0 else '未设置'}")
            
            # 检查本地更改
            print("2. 检查本地更改...")
            状态结果 = subprocess.run("git status", shell=True, capture_output=True, text=True)
            print(f"   仓库状态: {'有更改' if 'Changes' in 状态结果.stdout else '无更改'}")
            
            os.chdir("..")
            return True
            
        except Exception as e:
            print(f"❌ 状态检查失败: {e}")
            return False
    
    def 执行最简认证流程(self):
        """执行最简单的认证流程"""
        print("\n🎯 【执行最简GitHub认证流程】")
        print("=" * 50)
        
        try:
            os.chdir("我的智能体课程")
            
            print("步骤1: 添加所有文件到Git...")
            subprocess.run("git add .", shell=True, check=True)
            
            print("步骤2: 提交更改...")
            提交结果 = subprocess.run('git commit -m "专项解决GitHub认证"', shell=True, capture_output=True, text=True)
            if 提交结果.returncode != 0:
                print("⚠️ 提交可能无更改，继续执行推送...")
            
            print("步骤3: 执行推送（将要求认证）...")
            print("   当提示 'Username for 'https://github.com':' 时:")
            print("   → 输入: lw8707")
            print("   当提示 'Password for 'https://lw8707@github.com':' 时:")
            print("   → 粘贴你的GitHub Personal Access Token")
            print("   → Token获取: https://github.com/settings/tokens")
            
            # 执行推送
            推送结果 = subprocess.run("git push -u origin main", shell=True)
            
            if 推送结果.returncode == 0:
                print("🎉 GitHub认证成功！")
                return True
            else:
                print("❌ 推送失败，需要手动处理认证")
                return False
                
        except Exception as e:
            print(f"❌ 认证流程失败: {e}")
            return False
        finally:
            os.chdir("..")
    
    def 生成Token获取指南(self):
        """生成详细的Token获取指南"""
        指南 = """
📖 【GitHub Token获取详细指南】

由于无法发送截图，请按文字说明操作：

1. 打开手机浏览器，访问: https://github.com
2. 登录你的GitHub账户（用户名: lw8707）
3. 点击右上角头像 → Settings（设置）
4. 滚动到底部 → Developer settings（开发者设置）
5. 选择 Personal access tokens（个人访问令牌） → Tokens (classic)
6. 点击 Generate new token（生成新令牌） → Generate new token (classic)

7. 填写Token信息:
   - Note: Termux手机开发
   - Expiration: 90 days (90天)
   - 勾选权限: repo (全选)
   - 可选: workflow

8. 点击 Generate token（生成令牌）
9. 立即复制生成的Token（长串字符，只显示一次）

10. 回到Termux，在密码提示处粘贴这个Token

💡 重要提示：
- Token像密码，不要分享
- 如果失败，重新生成Token
- 确保有repo权限
- 网络连接稳定
"""
        print(指南)
    
    def 创建认证测试脚本(self):
        """创建认证测试脚本"""
        测试脚本 = """#!/bin/bash
# GitHub认证测试脚本

echo "🔧 GitHub认证测试"
cd 我的智能体课程

echo "1. 检查远程仓库..."
git remote -v

echo "2. 尝试推送..."
git push -u origin main

echo "3. 如果失败，请:"
echo "   - 检查Token权限"
echo "   - 重新生成Token" 
echo "   - 检查网络连接"
"""
        
        with open("测试GitHub认证.sh", "w") as f:
            f.write(测试脚本)
        
        print("✅ 已创建认证测试脚本: 测试GitHub认证.sh")
    
    def 运行完整解决方案(self):
        """运行完整的GitHub解决方案"""
        print("🚀 【开始GitHub认证专项解决】")
        
        # 检查状态
        if not self.检查当前状态():
            return False
        
        # 显示指南
        self.生成Token获取指南()
        
        # 创建测试脚本
        self.创建认证测试脚本()
        
        # 执行认证
        print("\n🎯 准备执行认证...")
        input("按回车键开始认证流程（确保已准备好Token）...")
        
        成功 = self.执行最简认证流程()
        
        if 成功:
            print("\n🎉 【GitHub认证成功完成！】")
            print("💾 现在我们的代码和记忆可以安全存储在云端了")
            print("🌐 访问: https://github.com/lw8707/gh-repo-create-autocode-video-gen---public")
        else:
            print("\n⚠️ 【需要手动处理认证】")
            print("请按照上面的指南获取Token，然后运行: bash 测试GitHub认证.sh")
        
        return 成功

# 运行专项解决方案
解决方案 = GitHub认证专项解决()
解决方案.运行完整解决方案()
