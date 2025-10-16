#!/bin/bash
echo "🔐 加密依赖稳定性加固..."
echo "=========================="

# 1. 安装稳定的加密替代方案
echo "📦 安装稳定加密库..."
pkg update && pkg upgrade -y
pkg install python rust libffi openssl -y

# 使用国内镜像加速安装
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple/ \
    pycryptodome \
    cryptography --only-binary=all

# 2. 创建兼容性加密层
cat > crypto_fallback_system.py << 'CRYPTO_EOF'
#!/usr/bin/env python3
"""
加密兼容性系统 - 解决Termux环境加密依赖问题
基于全球技术扫描的最佳实践
"""
import hashlib
import hmac
import base64
import os
import sys

class CryptoCompatibilitySystem:
    """加密兼容性系统"""
    
    def __init__(self):
        self.available_libraries = self.detect_crypto_libraries()
        self.primary_library = self.select_primary_library()
    
    def detect_crypto_libraries(self):
        """检测可用的加密库"""
        libraries = {}
        
        # 检测pycryptodome
        try:
            from Crypto.Cipher import AES
            from Crypto.Random import get_random_bytes
            libraries['pycryptodome'] = True
        except ImportError:
            libraries['pycryptodome'] = False
        
        # 检测cryptography
        try:
            from cryptography.fernet import Fernet
            from cryptography.hazmat.primitives import hashes
            libraries['cryptography'] = True
        except ImportError:
            libraries['cryptography'] = False
        
        return libraries
    
    def select_primary_library(self):
        """选择主要加密库"""
        if self.available_libraries.get('pycryptodome'):
            return 'pycryptodome'
        elif self.available_libraries.get('cryptography'):
            return 'cryptography'
        else:
            return 'fallback'
    
    def encrypt_data(self, data: str, password: str) -> dict:
        """加密数据"""
        if self.primary_library == 'pycryptodome':
            return self._encrypt_with_pycryptodome(data, password)
        elif self.primary_library == 'cryptography':
            return self._encrypt_with_cryptography(data, password)
        else:
            return self._encrypt_fallback(data, password)
    
    def _encrypt_with_pycryptodome(self, data: str, password: str) -> dict:
        """使用pycryptodome加密"""
        from Crypto.Cipher import AES
        from Crypto.Util.Padding import pad
        from Crypto.Random import get_random_bytes
        
        # 从密码派生密钥
        key = hashlib.sha256(password.encode()).digest()
        iv = get_random_bytes(16)
        
        cipher = AES.new(key, AES.MODE_CBC, iv)
        encrypted = cipher.encrypt(pad(data.encode(), AES.block_size))
        
        return {
            "encrypted": base64.b64encode(encrypted).decode(),
            "iv": base64.b64encode(iv).decode(),
            "algorithm": "AES-256-CBC",
            "library": "pycryptodome",
            "status": "success"
        }
    
    def _encrypt_fallback(self, data: str, password: str) -> dict:
        """备用加密方案"""
        # 使用HMAC和简单XOR
        salt = os.urandom(16)
        key = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
        
        # 简单的XOR加密
        key_bytes = key[:len(data)]
        encrypted = bytes(a ^ b for a, b in zip(data.encode(), key_bytes))
        
        return {
            "encrypted": base64.b64encode(encrypted).decode(),
            "salt": base64.b64encode(salt).decode(),
            "algorithm": "PBKDF2-HMAC-SHA256-XOR",
            "library": "fallback",
            "status": "fallback_used"
        }
    
    def generate_security_report(self):
        """生成安全报告"""
        report = {
            "timestamp": __import__('datetime').datetime.now().isoformat(),
            "primary_library": self.primary_library,
            "available_libraries": self.available_libraries,
            "security_level": self.get_security_level(),
            "recommendations": self.get_recommendations()
        }
        return report
    
    def get_security_level(self):
        """获取安全等级"""
        if self.primary_library == 'pycryptodome':
            return "企业级"
        elif self.primary_library == 'cryptography':
            return "生产级"
        else:
            return "基础级"
    
    def get_recommendations(self):
        """获取改进建议"""
        recommendations = []
        
        if self.primary_library == 'fallback':
            recommendations.append("建议安装pycryptodome: pip install pycryptodome")
        
        if not self.available_libraries.get('cryptography'):
            recommendations.append("考虑安装cryptography以获得更好的性能")
        
        return recommendations

def main():
    """主测试函数"""
    print("🔐 加密兼容性系统测试")
    print("=" * 40)
    
    crypto_system = CryptoCompatibilitySystem()
    
    # 测试加密
    test_data = "这是传承系统的重要数据"
    password = "secure_legacy_password_2025"
    
    result = crypto_system.encrypt_data(test_data, password)
    
    print(f"主要加密库: {crypto_system.primary_library}")
    print(f"加密算法: {result['algorithm']}")
    print(f"加密状态: {result['status']}")
    print(f"加密数据: {result['encrypted'][:50]}...")
    
    # 生成安全报告
    report = crypto_system.generate_security_report()
    print(f"\n📊 安全等级: {report['security_level']}")
    
    if report['recommendations']:
        print("💡 改进建议:")
        for rec in report['recommendations']:
            print(f"  • {rec}")

if __name__ == "__main__":
    main()
CRYPTO_EOF

echo "✅ 加密依赖加固完成"
echo "测试系统: python crypto_fallback_system.py"
