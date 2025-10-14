#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
【GitHub网页授权方案】
使用GitHub设备流程授权，避免复杂的Token输入
用户只需在网页点击授权即可
"""

import requests
import json
import time
import webbrowser

class GitHub网页授权:
    def 获取设备授权(self):
        """使用GitHub设备流程获取授权"""
        print("🚀 【GitHub网页授权流程】")
        print("=" * 50)
        
        # GitHub OAuth App配置
        客户端ID = "Iv1.5d8c1a76a106d0f7"  # GitHub的默认设备流程客户端ID
        授权URL = "https://github.com/login/device/code"
        TokenURL = "https://github.com/login/oauth/access_token"
        
        try:
            # 步骤1: 获取设备代码
            print("1. 请求设备授权码...")
            响应 = requests.post(授权URL, json={
                "client_id": 客户端ID,
                "scope": "repo"
            }, headers={"Accept": "application/json"})
            
            if 响应.status_code != 200:
                print("❌ 无法连接到GitHub授权服务")
                return None
            
            设备信息 = 响应.json()
            设备代码 = 设备信息.get("device_code")
            用户代码 = 设备信息.get("user_code")
            验证URL = 设备信息.get("verification_uri")
            间隔 = 设备信息.get("interval", 5)
            过期时间 = 设备信息.get("expires_in", 900)
            
            print(f"2. 请在浏览器中访问: {验证URL}")
            print(f"3. 输入用户代码: {用户代码}")
            print(f"4. 授权后返回这里继续...")
            
            # 尝试在Termux中打开浏览器
            try:
                import subprocess
                subprocess.run(f"termux-open-url '{验证URL}'", shell=True)
                print("✅ 已尝试打开浏览器...")
            except:
                print("💡 请手动复制链接到浏览器打开")
            
            # 步骤2: 等待用户授权
            print("\n⏳ 等待授权中...")
            print("   授权后会自动继续...")
            
            开始时间 = time.time()
            while time.time() - 开始时间 < 过期时间:
                time.sleep(间隔)
                
                Token响应 = requests.post(TokenURL, json={
                    "client_id": 客户端ID,
                    "device_code": 设备代码,
                    "grant_type": "urn:ietf:params:oauth:grant-type:device-code"
                }, headers={"Accept": "application/json"})
                
                if Token响应.status_code == 200:
                    Token数据 = Token响应.json()
                    if "access_token" in Token数据:
                        print("🎉 授权成功！")
                        return Token数据["access_token"]
                
                # 显示等待进度
                if int(time.time() - 开始时间) % 10 == 0:
                    print("  仍在等待授权...")
            
            print("❌ 授权超时，请重试")
            return None
            
        except Exception as e:
            print(f"❌ 授权过程出错: {e}")
            return None
    
    def 配置Git使用Token(self, Token):
        """配置Git使用获得的Token"""
        print("\n🔧 配置Git使用Token...")
        
        try:
            # 设置远程仓库URL包含Token
            仓库URL = f"https://{Token}@github.com/lw8707/gh-repo-create-autocode-video-gen---public.git"
            
            import subprocess
            os.chdir("我的智能体课程")
            
            # 更新远程仓库URL
            subprocess.run(f"git remote set-url origin {仓库URL}", shell=True, check=True)
            print("✅ 远程仓库URL已更新")
            
            # 测试推送
            print("🚀 测试推送...")
            结果 = subprocess.run("git push -u origin main", shell=True, capture_output=True, text=True)
            
            if 结果.returncode == 0:
                print("🎉 推送成功！")
                return True
            else:
                print(f"❌ 推送失败: {结果.stderr}")
                return False
                
        except Exception as e:
            print(f"❌ 配置失败: {e}")
            return False
        finally:
            os.chdir("..")
    
    def 运行网页授权流程(self):
        """运行完整的网页授权流程"""
        print("开始GitHub网页授权...")
        
        # 获取Token
        Token = self.获取设备授权()
        
        if Token:
            print(f"✅ 获得Token: {Token[:10]}...")
            
            # 配置Git
            if self.配置Git使用Token(Token):
                print("\n🎉 【GitHub授权完全成功！】")
                print("💾 现在可以自由推送代码到GitHub了")
                return True
            else:
                print("\n⚠️ Token有效但推送失败")
                return False
        else:
            print("\n❌ 授权失败")
            return False

import os

# 运行网页授权
授权器 = GitHub网页授权()
授权器.运行网页授权流程()
