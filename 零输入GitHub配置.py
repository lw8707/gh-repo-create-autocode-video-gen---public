#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
【零输入GitHub配置】
通过预配置的方式，避免所有手动输入
"""

import os
import subprocess

class 零输入GitHub配置:
    def 检查当前问题(self):
        """分析当前认证失败的具体原因"""
        print("🔍 【分析认证失败原因】")
        print("=" * 50)
        
        问题分析 = {
            "错误信息": "remote: Invalid username or token. Password authentication is not supported for Git operations.",
            "根本原因": "GitHub从2021年8月起不再支持密码认证，必须使用Personal Access Token",
            "当前状况": "用户可能正在输入密码而不是Token，或者Token没有正确配置",
            "解决方案": [
                "使用GitHub CLI工具简化认证",
                "配置SSH密钥避免密码输入",
                "使用预配置的Git凭据存储"
            ]
        }
        
        for 项目, 内容 in 问题分析.items():
            print(f"{项目}: {内容}")
        
        return 问题分析
    
    def 安装GitHub_CLI(self):
        """安装GitHub CLI工具，提供更简单的认证"""
        print("\n🔧 【安装GitHub CLI工具】")
        print("=" * 50)
        
        try:
            # 检查是否已安装
            检查结果 = subprocess.run("gh --version", shell=True, capture_output=True, text=True)
            if 检查结果.returncode == 0:
                print("✅ GitHub CLI已安装")
                return True
            
            print("正在安装GitHub CLI...")
            安装结果 = subprocess.run("pkg install gh -y", shell=True, capture_output=True, text=True)
            
            if 安装结果.returncode == 0:
                print("✅ GitHub CLI安装成功")
                return True
            else:
                print("❌ GitHub CLI安装失败")
                return False
                
        except Exception as e:
            print(f"❌ 安装过程出错: {e}")
            return False
    
    def 使用GitHub_CLI认证(self):
        """使用GitHub CLI进行认证"""
        print("\n🎯 【使用GitHub CLI认证】")
        print("=" * 50)
        
        print("GitHub CLI将打开浏览器进行认证...")
        print("请按以下步骤操作:")
        print("1. 浏览器打开后，登录您的GitHub账户")
        print("2. 授权GitHub CLI访问")
        print("3. 返回Termux继续")
        print("")
        input("按回车键开始...")
        
        try:
            # 执行GitHub CLI认证
            认证结果 = subprocess.run("gh auth login --web -h github.com -s repo", shell=True)
            
            if 认证结果.returncode == 0:
                print("🎉 GitHub CLI认证成功！")
                return True
            else:
                print("❌ GitHub CLI认证失败")
                return False
                
        except Exception as e:
            print(f"❌ 认证过程出错: {e}")
            return False
    
    def 配置SSH密钥(self):
        """配置SSH密钥认证，避免密码输入"""
        print("\n🔑 【配置SSH密钥认证】")
        print("=" * 50)
        
        try:
            # 检查是否已有SSH密钥
            SSH目录 = os.path.expanduser("~/.ssh")
            if not os.path.exists(SSH目录):
                os.makedirs(SSH目录)
            
            密钥文件 = os.path.join(SSH目录, "id_rsa")
            if os.path.exists(密钥文件):
                print("✅ SSH密钥已存在")
            else:
                print("生成新的SSH密钥对...")
                生成结果 = subprocess.run("ssh-keygen -t rsa -b 4096 -f ~/.ssh/id_rsa -N ''", shell=True, capture_output=True, text=True)
                if 生成结果.returncode == 0:
                    print("✅ SSH密钥生成成功")
                else:
                    print("❌ SSH密钥生成失败")
                    return False
            
            # 显示公钥
            print("\n📋 请将以下公钥添加到GitHub:")
            with open(os.path.join(SSH目录, "id_rsa.pub"), "r") as f:
                公钥内容 = f.read().strip()
                print(公钥内容)
            
            print("\n💡 添加步骤:")
            print("1. 访问: https://github.com/settings/keys")
            print("2. 点击 'New SSH key'")
            print("3. 标题: Termux手机")
            print("4. 粘贴上面的公钥内容")
            print("5. 点击 'Add SSH key'")
            
            input("\n添加完成后按回车继续...")
            
            # 测试SSH连接
            print("测试SSH连接...")
            测试结果 = subprocess.run("ssh -T git@github.com", shell=True, capture_output=True, text=True)
            if "successfully authenticated" in 测试结果.stdout:
                print("✅ SSH认证成功！")
                
                # 更新远程仓库为SSH URL
                os.chdir("我的智能体课程")
                subprocess.run("git remote set-url origin git@github.com:lw8707/gh-repo-create-autocode-video-gen---public.git", shell=True)
                print("✅ 已切换到SSH协议")
                os.chdir("..")
                
                return True
            else:
                print("❌ SSH认证失败")
                return False
                
        except Exception as e:
            print(f"❌ SSH配置失败: {e}")
            return False
    
    def 运行零输入方案(self):
        """运行零输入解决方案"""
        print("🚀 【开始零输入GitHub配置】")
        
        # 分析问题
        self.检查当前问题()
        
        print("\n🎯 提供两种解决方案:")
        print("方案A: 使用GitHub CLI（推荐）")
        print("方案B: 使用SSH密钥")
        
        选择 = input("请选择方案 (A/B): ").strip().upper()
        
        if 选择 == "A":
            if self.安装GitHub_CLI() and self.使用GitHub_CLI认证():
                print("\n🎉 GitHub CLI方案成功！")
                return True
            else:
                print("\n⚠️ GitHub CLI方案失败，尝试SSH方案")
                return self.配置SSH密钥()
        elif 选择 == "B":
            return self.配置SSH密钥()
        else:
            print("❌ 无效选择")
            return False

# 运行零输入方案
配置器 = 零输入GitHub配置()
成功 = 配置器.运行零输入方案()

if 成功:
    print("\n🎉 【零输入配置成功！】")
    print("💪 现在可以无障碍地使用GitHub了")
    print("🚀 尝试推送: cd 我的智能体课程 && git push")
else:
    print("\n❌ 配置失败，请尝试其他方法")
