#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
【智能目录检测】
自动检测当前目录状态并给出正确指令
"""

import os
import subprocess

def 检测目录状态():
    print("🔍 【智能目录检测】")
    print("=" * 50)
    
    当前目录 = os.getcwd()
    print(f"当前位置: {当前目录}")
    
    # 检查关键目录
    关键目录 = [
        "我的智能体课程",
        "记忆库", 
        "课程",
        "脚本"
    ]
    
    print("\n📁 目录结构检查:")
    目录状态 = {}
    for 目录 in 关键目录:
        存在 = os.path.exists(目录)
        目录状态[目录] = 存在
        print(f"   {'✅' if 存在 else '❌'} {目录}: {'存在' if 存在 else '缺失'}")
    
    # 判断当前目录类型
    if 当前目录.endswith("我的智能体课程"):
        print("\n🎯 当前在: 项目目录")
        print("💡 建议: 执行认证操作")
        return "项目目录"
    elif 所有目录存在(目录状态):
        print("\n🎯 当前在: 项目根目录")
        print("💡 建议: 可以执行各种操作")
        return "根目录"
    else:
        print("\n🎯 当前在: 未知目录")
        print("💡 建议: 切换到项目目录")
        return "未知目录"

def 所有目录存在(目录状态):
    """检查所有关键目录是否存在"""
    return all(目录状态.values())

def 提供操作建议(目录类型):
    """根据目录类型提供操作建议"""
    print("\n🎯 【操作建议】")
    print("=" * 50)
    
    if 目录类型 == "项目目录":
        print("1. GitHub认证: ./直接认证.sh")
        print("2. 返回根目录: cd ..")
        print("3. 检查状态: git status")
        
    elif 目录类型 == "根目录":
        print("1. GitHub认证: ./直接认证.sh")
        print("2. 进入项目: cd 我的智能体课程")
        print("3. 运行工作流: ./完整工作流程.sh")
        
    else:
        print("1. 找到项目目录: cd ~/my-ai-business")
        print("2. 检查目录: ls -la")
        print("3. 重新运行检测")

def 检查GitHub状态():
    """检查GitHub连接状态"""
    print("\n🌐 【GitHub状态检查】")
    print("=" * 50)
    
    try:
        # 检查是否在Git仓库中
        状态结果 = subprocess.run("git status", shell=True, capture_output=True, text=True)
        if 状态结果.returncode == 0:
            print("✅ Git仓库: 正常")
            
            # 检查远程仓库
            远程结果 = subprocess.run("git remote -v", shell=True, capture_output=True, text=True)
            if "origin" in 远程结果.stdout:
                print("✅ 远程仓库: 已配置")
            else:
                print("❌ 远程仓库: 未配置")
                
            # 检查是否有提交
            日志结果 = subprocess.run("git log --oneline -3", shell=True, capture_output=True, text=True)
            if 日志结果.returncode == 0 and 日志结果.stdout.strip():
                print("✅ 提交历史: 存在")
            else:
                print("⚠️ 提交历史: 无或很少")
                
        else:
            print("❌ Git仓库: 未初始化或有问题")
            
    except Exception as e:
        print(f"❌ GitHub检查失败: {e}")

# 运行检测
目录类型 = 检测目录状态()
检查GitHub状态()
提供操作建议(目录类型)

print("\n💪 根据建议选择下一步操作！")
