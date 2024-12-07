import hashlib
import rsa

def hash_sha256(data):
    sha256_hash = hashlib.sha256()
    sha256_hash.update(data.encode('utf-8'))
    return sha256_hash.hexdigest()

def rsa_encryption(data, public_key):
    encrypted_data = rsa.encrypt(data.encode('utf-8'), public_key)
    return encrypted_data

def rsa_decryption(encrypted_data, private_key):
    decrypted_data = rsa.decrypt(encrypted_data, private_key).decode('utf-8')
    return decrypted_data
