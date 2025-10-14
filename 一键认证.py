#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
【一键GitHub认证】
最简单的认证方法，避免所有复杂逻辑
"""

import os
import subprocess

def 一键认证():
    print("🚀 【一键GitHub认证】")
    print("=" * 50)
    
    # 自动处理目录
    当前目录 = os.getcwd()
    if 当前目录.endswith("我的智能体课程"):
        项目目录 = 当前目录
        根目录 = os.path.dirname(当前目录)
    else:
        根目录 = 当前目录
        项目目录 = os.path.join(当前目录, "我的智能体课程")
    
    print(f"📁 根目录: {根目录}")
    print(f"📁 项目目录: {项目目录}")
    
    # 检查项目目录是否存在
    if not os.path.exists(项目目录):
        print("❌ 项目目录不存在！")
        print("💡 请确保在正确的位置运行此脚本")
        return False
    
    print("\n🔧 开始认证流程...")
    
    try:
        # 进入项目目录
        os.chdir(项目目录)
        
        print("1. 📦 添加文件...")
        subprocess.run("git add .", shell=True, check=True)
        
        print("2. 💾 提交更改...")
        subprocess.run('git commit -m "一键认证提交"', shell=True)
        
        print("3. 🚀 推送到GitHub...")
        print("")
        print("   接下来会要求认证:")
        print("   - 用户名: lw8707")
        print("   - 密码: 粘贴GitHub Token")
        print("")
        print("💡 Token获取:")
        print("   访问: https://github.com/settings/tokens")
        print("   生成新Token，勾选 repo 权限")
        print("")
        
        # 执行推送
        结果 = subprocess.run("git push -u origin main", shell=True)
        
        if 结果.returncode == 0:
            print("\n🎉 【认证成功！】")
            print("💾 代码已安全保存到GitHub")
            print("🌐 查看: https://github.com/lw8707/gh-repo-create-autocode-video-gen---public")
            return True
        else:
            print("\n❌ 【认证失败】")
            print("💡 可能的原因:")
            print("   - Token错误或过期")
            print("   - 网络连接问题")
            print("   - 权限不足")
            return False
            
    except Exception as e:
        print(f"❌ 认证过程出错: {e}")
        return False
    finally:
        # 回到原始目录
        os.chdir(当前目录)

def 生成快速指南():
    """生成快速操作指南"""
    指南 = """
📖 【GitHub认证极简指南】

只有3步:

1. 获取Token:
   - 手机浏览器打开: https://github.com/settings/tokens
   - 点击 Generate new token (classic)
   - 名称: Termux | 过期: 90天 | 权限: repo
   - 生成并复制Token

2. 运行认证:
   - 执行: python 一键认证.py
   - 用户名输入: lw8707  
   - 密码处粘贴Token

3. 验证成功:
   - 看到: Writing objects: 100%
   - 回到命令提示符 $
   - 访问GitHub查看代码
"""
    print(指南)

# 运行一键认证
print("准备执行一键认证...")
生成快速指南()
print("\n" + "🎯" * 20)
成功 = 一键认证()
print("🎯" * 20)

if 成功:
    print("\n✅ 现在可以继续其他开发任务了！")
else:
    print("\n💡 请按照指南重新尝试")
