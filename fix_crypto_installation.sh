#!/bin/bash
echo "🔧 修复加密库安装问题..."

# 1. 安装完整的Rust工具链
pkg install rust rust-bin -y
echo "✅ Rust工具链安装完成"

# 2. 设置Rust环境变量
export RUSTUP_HOME=~/.rustup
export CARGO_HOME=~/.cargo
export PATH=$PATH:$CARGO_HOME/bin

# 3. 安装预编译的加密库替代方案
echo "📦 安装预编译的加密替代方案..."
pip install --no-deps pycryptodome -y
pip install pycrypto -y

# 4. 创建兼容性加密层
cat > compatible_crypto.py << 'CRYPTO_EOF'
#!/usr/bin/env python3
"""
兼容性加密层 - 解决Termux环境加密库依赖问题
基于全球技术扫描的最佳实践
"""
import hashlib
import hmac
import base64
import os
import sys

try:
    from Crypto.Cipher import AES
    from Crypto.Util.Padding import pad, unpad
    from Crypto.Random import get_random_bytes
    CRYPTO_AVAILABLE = True
except ImportError:
    CRYPTO_AVAILABLE = False
    print("⚠️  PyCryptodome不可用，使用备用加密方案")

class TermuxCompatibleCrypto:
    """Termux兼容的加密解决方案"""
    
    def __init__(self):
        self.algorithm = "AES-256-CBC" if CRYPTO_AVAILABLE else "HMAC-SHA256"
    
    def encrypt(self, data: str, password: str) -> dict:
        """加密数据"""
        if CRYPTO_AVAILABLE:
            return self._encrypt_aes(data, password)
        else:
            return self._encrypt_hmac(data, password)
    
    def _encrypt_aes(self, data: str, password: str) -> dict:
        """使用AES加密"""
        # 从密码派生密钥
        key = hashlib.sha256(password.encode()).digest()
        iv = get_random_bytes(16)
        
        cipher = AES.new(key, AES.MODE_CBC, iv)
        encrypted = cipher.encrypt(pad(data.encode(), AES.block_size))
        
        return {
            "encrypted": base64.b64encode(encrypted).decode(),
            "iv": base64.b64encode(iv).decode(),
            "algorithm": "AES-256-CBC",
            "status": "success"
        }
    
    def _encrypt_hmac(self, data: str, password: str) -> dict:
        """使用HMAC作为备用方案"""
        # 创建HMAC签名
        signature = hmac.new(
            password.encode(), 
            data.encode(), 
            hashlib.sha256
        ).digest()
        
        # 简单的XOR"加密"（仅用于演示）
        key_bytes = password.encode() * (len(data) // len(password) + 1)
        encrypted = bytes(a ^ b for a, b in zip(data.encode(), key_bytes[:len(data)]))
        
        return {
            "encrypted": base64.b64encode(encrypted).decode(),
            "signature": base64.b64encode(signature).decode(),
            "algorithm": "HMAC-XOR-Fallback",
            "status": "fallback_used"
        }
    
    def create_secure_hash(self, data: str) -> str:
        """创建安全哈希"""
        salt = os.urandom(16)
        return hashlib.pbkdf2_hmac(
            'sha256', 
            data.encode(), 
            salt, 
            100000
        ).hex()

def test_crypto_system():
    """测试加密系统"""
    print("🔐 测试加密系统兼容性...")
    crypto = TermuxCompatibleCrypto()
    
    test_data = "这是测试加密的数据"
    password = "secure_password_123"
    
    result = crypto.encrypt(test_data, password)
    print(f"加密算法: {result['algorithm']}")
    print(f"加密状态: {result['status']}")
    print(f"加密数据: {result['encrypted'][:50]}...")
    
    secure_hash = crypto.create_secure_hash(test_data)
    print(f"安全哈希: {secure_hash[:32]}...")
    
    return result

if __name__ == "__main__":
    test_crypto_system()
CRYPTO_EOF

echo "✅ 兼容性加密层已创建"
echo "运行测试: python compatible_crypto.py"
