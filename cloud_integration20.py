import boto3
from google.cloud import storage
from azure.storage.blob import BlobServiceClient

def invoke_lambda(function_name, payload):
    lambda_client = boto3.client('lambda', region_name='us-east-1')
    response = lambda_client.invoke(
        FunctionName=function_name,
        InvocationType='RequestResponse',
        Payload=payload
    )
    return response['Payload'].read().decode('utf-8')

def upload_to_google_cloud(bucket_name, file_name, file_path):
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(file_name)
    blob.upload_from_filename(file_path)

def upload_to_azure_blob(container_name, file_path):
    blob_service_client = BlobServiceClient.from_connection_string("your_connection_string")
    container_client = blob_service_client.get_container_client(container_name)
    blob_client = container_client.get_blob_client("file_name")
    with open(file_path, "rb") as data:
        blob_client.upload_blob(data)
