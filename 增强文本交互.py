#!/usr/bin/env python3
"""
pwd - 语音不可用时的备选方案
"""
import os
import sys

class 文本交互增强:
    def __init__(self):
        self.功能列表 = {
            "1": {"名称": "项目上传", "脚本": "一键上传.sh", "描述": "上传文件到GitHub"},
            "2": {"名称": "系统诊断", "脚本": "全面诊断.sh", "描述": "检查系统状态"},
            "3": {"名称": "资产盘点", "脚本": "资产盘点系统.sh", "描述": "查看项目文件"},
            "4": {"名称": "自动备份", "脚本": "自动备份.sh", "描述": "备份项目数据"}
        }
    
    def 显示菜单(self):
        print("🎯 项目功能菜单")
        print("==============")
        for 编号, 功能 in self.功能列表.items():
            print(f"{编号}. {功能['名称']} - {功能['描述']}")
        print("0. 退出")
    
    def 执行功能(self, 选择):
        if 选择 in self.功能列表:
            功能 = self.功能列表[选择]
            print(f"🚀 执行: {功能['名称']}")
            
            if os.path.exists(功能['脚本']):
                os.system(f"./{功能['脚本']}")
            else:
                print(f"❌ 脚本不存在: {功能['脚本']}")
        else:
            print("❌ 无效选择")

if __name__ == "__main__":
    系统 = 文本交互增强()
    
    while True:
        系统.显示菜单()
        选择 = input("请输入选择: ").strip()
        
        if 选择 == "0":
            print("👋 再见！")
            break
        else:
            系统.执行功能(选择)
