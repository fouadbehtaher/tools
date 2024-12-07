import boto3

def store_key_in_hsm(key):
    hsm_client = boto3.client('kms')
    response = hsm_client.create_key(KeySpec='RSA_2048', KeyUsage='ENCRYPT_DECRYPT')
    return response['KeyId']
