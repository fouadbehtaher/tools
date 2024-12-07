from Crypto.Cipher import AES
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes

def aes_encrypt(data):
    key = get_random_bytes(16)  # 128-bit key
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(data)
    return ciphertext

def rsa_encrypt(data):
    key = RSA.generate(2048)
    public_key = key.publickey()
    cipher = public_key.encrypt(data.encode(), None)
    return cipher

def multi_layer_encryption(data):
    encrypted_data = aes_encrypt(rsa_encrypt(data))
    return encrypted_data
