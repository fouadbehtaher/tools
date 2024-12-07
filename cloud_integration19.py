import boto3
from azure.storage.blob import BlobServiceClient
from google.cloud import storage

def invoke_lambda(function_name, payload):
    lambda_client = boto3.client('lambda', region_name='us-east-1')
    response = lambda_client.invoke(
        FunctionName=function_name,
        InvocationType='RequestResponse',
        Payload=payload
    )
    return response['Payload'].read().decode('utf-8')

def upload_to_azure_blob(storage_account_name, container_name, blob_name, data):
    connection_string = f"DefaultEndpointsProtocol=https;AccountName={storage_account_name};AccountKey=<your_account_key>;EndpointSuffix=core.windows.net"
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
    
    blob_client.upload_blob(data)
    print(f"Data uploaded to Azure Blob Storage: {container_name}/{blob_name}")

def upload_to_google_cloud(bucket_name, blob_name, data):
    client = storage.Client()
    bucket = client.get_bucket(bucket_name)
    blob = bucket.blob(blob_name)
    
    blob.upload_from_string(data)
    print(f"Data uploaded to Google Cloud Storage: {bucket_name}/{blob_name}")
