#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
【GitHub认证详细指导】
一步一步指导完成GitHub CLI认证
"""

import subprocess
import time

def 显示认证步骤():
    """显示详细的认证步骤"""
    步骤 = """
🎯 【GitHub CLI认证详细步骤】

步骤1: 运行认证命令
   在Termux中输入: gh auth login --web -h github.com -s repo

步骤2: 复制验证码
   命令会显示: "First copy your one-time code: XXXX-XXXX"
   请记住这个代码

步骤3: 打开浏览器
   - 按回车键自动打开浏览器，或
   - 手动复制显示的网址到手机浏览器

步骤4: 在网页中操作
   - 在GitHub页面输入验证码
   - 点击 "Continue"
   - 点击 "Authorize"

步骤5: 返回Termux
   - 授权成功后返回Termux
   - 系统会自动完成认证

步骤6: 验证成功
   运行: gh auth status
   应该显示已登录状态

💡 注意事项:
   - 确保手机网络畅通
   - 如果浏览器没自动打开，手动复制网址
   - 验证码有时间限制，请尽快操作
   - 授权时确保登录了正确的GitHub账户
"""
    print(步骤)

def 检查准备状态():
    """检查系统准备状态"""
    print("🔍 【检查系统准备状态】")
    print("=" * 50)
    
    检查项目 = [
        ("GitHub CLI安装", "gh --version"),
        ("网络连接", "ping -c 1 github.com"),
        ("当前认证状态", "gh auth status")
    ]
    
    for 项目名称, 检查命令 in 检查项目:
        try:
            if 项目名称 == "当前认证状态":
                # 这个命令失败是正常的（未认证）
                结果 = subprocess.run(检查命令, shell=True, capture_output=True, text=True)
                if "not logged" in 结果.stderr.lower():
                    print(f"✅ {项目名称}: 未认证（正常状态）")
                else:
                    print(f"✅ {项目名称}: {结果.stdout.strip()}")
            else:
                结果 = subprocess.run(检查命令, shell=True, capture_output=True, text=True)
                if 结果.returncode == 0:
                    print(f"✅ {项目名称}: 正常")
                else:
                    print(f"❌ {项目名称}: 异常")
        except Exception as e:
            print(f"❌ {项目名称}: 错误 - {e}")

def 运行认证流程():
    """运行认证流程并指导用户"""
    print("\n🚀 【开始GitHub认证流程】")
    print("=" * 50)
    
    显示认证步骤()
    
    print("\n🎯 准备执行认证命令...")
    input("请按回车键开始认证流程...")
    
    try:
        # 执行认证命令
        print("执行: gh auth login --web -h github.com -s repo")
        print("请仔细查看下面的输出...")
        print("-" * 50)
        
        认证进程 = subprocess.Popen(
            "gh auth login --web -h github.com -s repo", 
            shell=True,
            text=True
        )
        
        # 等待进程完成
        认证进程.wait()
        
        print("-" * 50)
        print("\n认证命令执行完成")
        
        # 检查认证结果
        print("检查认证结果...")
        状态结果 = subprocess.run("gh auth status", shell=True, capture_output=True, text=True)
        
        if 状态结果.returncode == 0 and "logged in" in 状态结果.stdout.lower():
            print("🎉 GitHub认证成功！")
            return True
        else:
            print("❌ 认证尚未完成")
            print("请按照上面的步骤在浏览器中完成授权")
            return False
            
    except Exception as e:
        print(f"❌ 认证过程出错: {e}")
        return False

# 运行指导流程
检查准备状态()

print("\n" + "💡" * 20)
print("💡 重要提示：请仔细阅读上面的步骤")
print("💡 认证成功后，我们就能解决所有GitHub问题")
print("💡" * 20)

运行认证 = input("\n是否开始认证流程？(y/n): ").strip().lower()
if 运行认证 == 'y':
    成功 = 运行认证流程()
    if 成功:
        print("\n🎉 🎉 🎉 认证成功！ 🎉 🎉 🎉")
        print("💪 现在我们可以继续项目的其他部分了")
    else:
        print("\n⚠️ 认证需要手动完成")
        print("💡 请按照步骤在浏览器中完成授权")
else:
    print("\n💡 您可以在准备好时运行: gh auth login --web -h github.com -s repo")
