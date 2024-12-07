from google.cloud import storage

def upload_to_google_cloud(file_path, bucket_name):
    client = storage.Client()
    bucket = client.get_bucket(bucket_name)
    blob = bucket.blob(file_path)
    blob.upload_from_filename(file_path)
    print(f"File uploaded to {bucket_name}/{file_path}")

def download_from_google_cloud(file_path, bucket_name):
    client = storage.Client()
    bucket = client.get_bucket(bucket_name)
    blob = bucket.blob(file_path)
    blob.download_to_filename(file_path)
    print(f"File downloaded from {bucket_name}/{file_path}")
