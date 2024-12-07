import boto3
import hvac
import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

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


def store_key_in_vault(secret_key, vault_url, token):
    client = hvac.Client(url=vault_url, token=token)
    secret_path = 'secret/my_key'
    client.secrets.kv.v2.create_or_update_secret(secret_path, secret={'key': secret_key})
    return f"Key stored at {secret_path}"

def retrieve_key_from_vault(vault_url, token):
    client = hvac.Client(url=vault_url, token=token)
    secret_path = 'secret/my_key'
    secret = client.secrets.kv.v2.read_secret_version(secret_path)
    return secret['data']['data']['key']
