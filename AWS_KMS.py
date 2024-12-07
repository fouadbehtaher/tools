import boto3

class KeyManagement:
    def __init__(self, region_name='us-east-1'):
        self.kms_client = boto3.client('kms', region_name=region_name)
    
    def create_key(self):
        response = self.kms_client.create_key(
            Description="My New Key",
            KeyUsage='ENCRYPT_DECRYPT',
            Origin='AWS_KMS'
        )
        return response['KeyMetadata']['KeyId']

    def encrypt_data(self, plaintext_data, key_id):
        response = self.kms_client.encrypt(
            KeyId=key_id,
            Plaintext=plaintext_data
        )
        return response['CiphertextBlob']
    
    def decrypt_data(self, ciphertext_blob):
        response = self.kms_client.decrypt(CiphertextBlob=ciphertext_blob)
        return response['Plaintext']
