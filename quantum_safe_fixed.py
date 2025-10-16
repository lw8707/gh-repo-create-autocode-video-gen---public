#!/usr/bin/env python3
import oqs
import base64

class QuantumSafeEncryption:
    def __init__(self):
        # 使用oqs支持的算法
        self.kem_alg = "Kyber512"
    
    def generate_quantum_keys(self):
        """生成量子安全密钥对"""
        try:
            with oqs.KeyEncapsulation(self.kem_alg) as kem:
                public_key = kem.generate_keypair()
                return public_key, "量子安全密钥生成成功"
        except Exception as e:
            return None, f"密钥生成失败: {e}"
    
    def quantum_encrypt_demo(self, message):
        """量子安全加密演示"""
        try:
            with oqs.KeyEncapsulation(self.kem_alg) as kem:
                # 生成密钥对
                public_key = kem.generate_keypair()
                
                # 加密过程
                ciphertext, shared_secret_server = kem.encap_secret(public_key)
                
                # 模拟解密端
                with oqs.KeyEncapsulation(self.kem_alg) as kem_client:
                    shared_secret_client = kem_client.decap_secret(ciphertext)
                
                # 验证共享密钥是否相同
                if shared_secret_server == shared_secret_client:
                    # 使用共享密钥加密消息（简化演示）
                    encrypted_msg = self.xor_encrypt(message, shared_secret_server)
                    return {
                        "success": True,
                        "public_key": base64.b64encode(public_key).decode(),
                        "ciphertext": base64.b64encode(ciphertext).decode(),
                        "encrypted_message": base64.b64encode(encrypted_msg).decode(),
                        "shared_secret_match": True
                    }
                else:
                    return {"success": False, "error": "共享密钥不匹配"}
                    
        except Exception as e:
            return {"success": False, "error": str(e)}
    
    def xor_encrypt(self, data, key):
        """简单的XOR加密用于演示"""
        key_bytes = key[:len(data)]
        return bytes(a ^ b for a, b in zip(data.encode(), key_bytes))

def main():
    print("🔬 量子安全加密演示 (修复版)")
    qse = QuantumSafeEncryption()
    
    # 测试加密
    message = "这是量子安全加密的测试消息"
    print(f"原始消息: {message}")
    
    result = qse.quantum_encrypt_demo(message)
    
    if result["success"]:
        print("✅ 量子安全加密成功!")
        print(f"公钥: {result['public_key'][:50]}...")
        print(f"密文: {result['ciphertext'][:50]}...")
        print(f"加密消息: {result['encrypted_message']}")
        print(f"共享密钥验证: {'通过' if result['shared_secret_match'] else '失败'}")
    else:
        print(f"❌ 加密失败: {result['error']}")

if __name__ == "__main__":
    main()
