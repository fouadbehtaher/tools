import boto3

class KeyManagement:
    def __init__(self):
        self.kms_client = boto3.client('kms')

    def create_key(self, key_id):
        response = self.kms_client.create_key(
            KeyId=key_id
        )
        return response

    def encrypt_data(self, key_id, data):
        response = self.kms_client.encrypt(
            KeyId=key_id,
            Plaintext=data
        )
        return response['CiphertextBlob']

    def decrypt_data(self, ciphertext):
        response = self.kms_client.decrypt(
            CiphertextBlob=ciphertext
        )
        return response['Plaintext']
