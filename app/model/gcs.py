import mimetypes

class GCS:
    def __init__(self, storage_client):
        self.client = storage_client

    def get_bucket(self, bucket_name):
        return self.client.get_bucket(bucket_name)
    
    def upload_file(self, bucket, blob_name, file_path):
        content_type = mimetypes.guess_type(file_path)[0]
        blob = bucket.blob(blob_name)
        blob.upload_from_filename(file_path, content_type=content_type)
        return blob
    
    def list_blobs(self, bucket_name):
        return self.client.list_blobs(bucket_name)


