import boto3
from Crypto.Cipher import AES, ChaCha20
from Crypto.Util.Padding import pad, unpad
import rsa
import os
import base64

def generate_aes_key():
    key = os.urandom(16)
    return key

def generate_chacha_key():
    key = os.urandom(32)
    nonce = os.urandom(8)
    return key, nonce

def aes_encryption(data, key):
    cipher = AES.new(key, AES.MODE_CBC)
    encrypted_data = cipher.encrypt(pad(data.encode('utf-8'), AES.block_size))
    return cipher.iv + encrypted_data  # تضمين الـ IV

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

def generate_kms_key():
    client = boto3.client('kms')
    response = client.create_key(Description='Test Key for Encryption')
    key_id = response['KeyMetadata']['KeyId']
    return key_id

def encrypt_with_kms(data, key_id):
    client = boto3.client('kms')
    encrypted_data = client.encrypt(
        KeyId=key_id,
        Plaintext=data.encode('utf-8')
    )
    return encrypted_data['CiphertextBlob']

def decrypt_with_kms(ciphertext, key_id):
    client = boto3.client('kms')
    decrypted_data = client.decrypt(
        KeyId=key_id,
        CiphertextBlob=ciphertext
    )
    return decrypted_data['Plaintext'].decode('utf-8')
