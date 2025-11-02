#!/usr/bin/env python3
"""
诊断工具 - 找出程序卡住的具体原因
"""
import sys
import importlib

def 检查依赖():
    """检查必要的依赖库"""
    print("🔍 检查依赖库...")
    
    必要依赖 = ['jwt', 'asyncio', 'hashlib', 'hmac', 'secrets', 'datetime']
    
    for 依赖 in 必要依赖:
        try:
            importlib.import_module(依赖)
            print(f"✅ {依赖}: 已安装")
        except ImportError as e:
            print(f"❌ {依赖}: 未安装 - {e}")
    
    return True

def 检查编码():
    """检查编码相关问题"""
    print("\n🔍 检查编码设置...")
    
    try:
        print(f"Python版本: {sys.version}")
        print(f"默认编码: {sys.getdefaultencoding()}")
        print(f"文件系统编码: {sys.getfilesystemencoding()}")
        print("✅ 编码设置正常")
    except Exception as e:
        print(f"❌ 编码检查失败: {e}")

def 检查异步支持():
    """检查异步支持"""
    print("\n🔍 检查异步支持...")
    
    try:
        import asyncio
        print("✅ asyncio: 支持正常")
        
        # 测试简单异步函数
        async def 简单测试():
            return "异步测试通过"
        
        result = asyncio.run(简单测试())
        print(f"✅ 异步执行: {result}")
        
    except Exception as e:
        print(f"❌ 异步支持问题: {e}")

if __name__ == "__main__":
    print("🩺 开始系统诊断...")
    
    检查依赖()
    检查编码() 
    检查异步支持()
    
    print("\n🎯 诊断完成!")
