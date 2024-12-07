from Crypto.Cipher import AES, ChaCha20
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import boto3
import hvac
import pyotp

def generate_otp(secret):
    totp = pyotp.TOTP(secret)
    return totp.now()

def encrypt_data_with_aes(data, key):
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(data.encode('utf-8'), AES.block_size))
    return ct_bytes

def encrypt_data_with_rsa(data, public_key):
    rsa_cipher = PKCS1_OAEP.new(public_key)
    encrypted_data = rsa_cipher.encrypt(data.encode('utf-8'))
    return encrypted_data

def authenticate_with_mfa(otp):
    client = boto3.client('sts')
    mfa_token = otp
    response = client.get_session_token(
        SerialNumber='arn:aws:iam::123456789012:mfa/user',
        TokenCode=mfa_token
    )
    return response

def store_key_in_vault(secret_key, vault_url, token):
    client = hvac.Client(url=vault_url, token=token)
    client.secrets.kv.v2.create_or_update_secret('secret/my_key', secret={'key': secret_key})
    return f"Key stored at secret/my_key"
