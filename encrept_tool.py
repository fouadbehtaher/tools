from Crypto.Cipher import AES, ChaCha20
from Crypto.Util.Padding import pad, unpad
import rsa
import os
import base64

def generate_aes_key():
    key = os.urandom(16)  # توليد مفتاح عشوائي AES
    return key

def generate_chacha_key():
    key = os.urandom(32)  # توليد مفتاح عشوائي ChaCha20
    nonce = os.urandom(8)
    return key, nonce

def aes_encryption(data, key):
    cipher = AES.new(key, AES.MODE_CBC)
    encrypted_data = cipher.encrypt(pad(data.encode('utf-8'), AES.block_size))
    return cipher.iv + encrypted_data  # إضافة الـ IV مع البيانات المشفرة

# فك تشفير AES
def aes_decryption(encrypted_data, key):
    iv = encrypted_data[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    decrypted_data = unpad(cipher.decrypt(encrypted_data[AES.block_size:]), AES.block_size)
    return decrypted_data.decode('utf-8')

def chacha_encryption(data, key, nonce):
    cipher = ChaCha20.new(key=key, nonce=nonce)
    encrypted_data = cipher.encrypt(data.encode('utf-8'))
    return encrypted_data

def chacha_decryption(encrypted_data, key, nonce):
    cipher = ChaCha20.new(key=key, nonce=nonce)
    decrypted_data = cipher.decrypt(encrypted_data)
    return decrypted_data.decode('utf-8')

def rsa_encrypt_with_aes_and_chacha(data, rsa_public_key):
    aes_key = generate_aes_key()
    chacha_key, nonce = generate_chacha_key()
    
    aes_encrypted_data = aes_encryption(data, aes_key)
    chacha_encrypted_data = chacha_encryption(data, chacha_key, nonce)
    
    encrypted_aes_key = rsa.encrypt(aes_key, rsa_public_key)
    encrypted_chacha_key = rsa.encrypt(chacha_key, rsa_public_key)
    
    return encrypted_aes_key, encrypted_chacha_key, aes_encrypted_data, chacha_encrypted_data

def rsa_decrypt_with_aes_and_chacha(encrypted_aes_key, encrypted_chacha_key, aes_encrypted_data, chacha_encrypted_data, rsa_private_key):
    aes_key = rsa.decrypt(encrypted_aes_key, rsa_private_key)
    chacha_key = rsa.decrypt(encrypted_chacha_key, rsa_private_key)
    
    decrypted_aes_data = aes_decryption(aes_encrypted_data, aes_key)
    decrypted_chacha_data = chacha_decryption(chacha_encrypted_data, chacha_key, nonce)
    
    return decrypted_aes_data, decrypted_chacha_data
