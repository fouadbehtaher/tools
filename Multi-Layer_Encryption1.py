from Crypto.Cipher import AES
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad

def encrypt_with_aes(data, key):
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(data.encode('utf-8'), AES.block_size))
    return ct_bytes, cipher.iv

def encrypt_with_rsa(data, public_key):
    rsa_cipher = RSA.import_key(public_key)
    rsa_cipher = rsa_cipher.encrypt(data.encode('utf-8'), None)
    return rsa_cipher
