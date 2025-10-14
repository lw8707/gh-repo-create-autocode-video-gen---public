#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
【小白成功检测器】
帮助小白判断命令是否执行成功
解决：看不懂终端输出、不确定是否成功的问题
"""

import os
import subprocess

class 成功检测器:
    def 检测基础环境(self):
        """检测Termux基础环境是否正常"""
        print("🔍 【环境状态检测】")
        print("=" * 40)
        
        检测项目 = [
            ("Python版本", "python --version"),
            ("Git版本", "git --version"),
            ("Node.js版本", "node --version"),
            ("当前目录", "pwd"),
            ("项目文件", "find . -name '*.py' | wc -l")
        ]
        
        全部成功 = True
        
        for 项目名称, 检测命令 in 检测项目:
            try:
                结果 = subprocess.run(检测命令, shell=True, capture_output=True, text=True)
                if 结果.returncode == 0:
                    print(f"✅ {项目名称}: 正常 - {结果.stdout.strip()}")
                else:
                    print(f"❌ {项目名称}: 异常")
                    全部成功 = False
            except Exception as e:
                print(f"⚠️ {项目名称}: 错误 - {e}")
                全部成功 = False
        
        print("=" * 40)
        if 全部成功:
            print("🎉 【环境状态】所有检测通过！")
        else:
            print("🔧 【环境状态】部分项目需要修复")
        
        return 全部成功
    
    def 检测项目状态(self):
        """检测我们的项目状态"""
        print("\n📁 【项目状态检测】")
        print("=" * 40)
        
        项目文件 = [
            "智能体记忆系统.py",
            "跨界面记忆同步.py", 
            "记忆恢复器.py",
            "GitHub集成准备.py",
            "记忆库/跨界面记忆.json"
        ]
        
        存在的文件 = []
        缺失的文件 = []
        
        for 文件 in 项目文件:
            if os.path.exists(文件):
                存在的文件.append(文件)
            else:
                缺失的文件.append(文件)
        
        print(f"✅ 存在的文件: {len(存在的文件)} 个")
        for 文件 in 存在的文件:
            print(f"   📄 {文件}")
        
        if 缺失的文件:
            print(f"❌ 缺失的文件: {len(缺失的文件)} 个")
            for 文件 in 缺失的文件:
                print(f"   ❓ {文件}")
        
        print("=" * 40)
        return len(缺失的文件) == 0
    
    def 生成成功指南(self):
        """生成小白成功判断指南"""
        指南 = """
🎯 【小白成功判断指南】

✅ 【成功标志】
1. 看到正常的命令提示符: $ 或 ~/my-ai-business $
2. 程序输出正常内容，没有红色错误信息
3. 能够输入新命令
4. 创建了预期的文件和目录

❌ 【失败标志】  
1. 看到红色错误信息（SyntaxError, ImportError等）
2. 程序卡住不动，无法输入新命令
3. 提示 "Command not found"
4. 没有创建预期的文件

🔄 【解决方案】
1. 成功 → 继续下一步
2. 失败 → 查看错误信息，修复问题
3. 卡住 → 按 Ctrl + C 中断，重新执行

📞 【求助时机】
1. 看不懂错误信息时
2. 不知道如何修复时  
3. 不确定是否成功时
4. 任何疑惑时立即求助
"""
        print(指南)

# 运行检测器
检测器 = 成功检测器()
环境正常 = 检测器.检测基础环境()
项目正常 = 检测器.检测项目状态()

if 环境正常 and 项目正常:
    print("\n🎊 【总体状态】一切正常，可以继续下一步！")
else:
    print("\n🔧 【总体状态】需要修复一些问题")

检测器.生成成功指南()
