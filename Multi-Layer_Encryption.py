from Crypto.PublicKey import RSA
from Crypto.Cipher import AES
from Crypto.Cipher import ChaCha20
from Crypto.Util.Padding import pad
import hvac
import pyotp
import boto3

def generate_otp(secret):
    totp = pyotp.TOTP(secret)
    return totp.now()

def encrypt_with_aes(data, key):
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(data.encode('utf-8'), AES.block_size))
    return ct_bytes

def encrypt_with_rsa(data, public_key):
    rsa_cipher = RSA.import_key(public_key)
    rsa_cipher = rsa_cipher.encrypt(data.encode('utf-8'), None)
    return rsa_cipher

def store_key_in_vault(secret_key, vault_url, token):
    client = hvac.Client(url=vault_url, token=token)
    client.secrets.kv.v2.create_or_update_secret('secret/my_key', secret={'key': secret_key})
    return "Key stored in Vault"

def authenticate_with_mfa(otp):
    client = boto3.client('sts')
    response = client.get_session_token(
        SerialNumber='arn:aws:iam::123456789012:mfa/user',
        TokenCode=otp
    )
    return response
