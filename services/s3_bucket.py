import boto3

class S3Bucket:
    def __init__(self):
        self.s3 = boto3.client('s3')

    def read_csv(self, file_path):
        obj = self.s3.get_object(Bucket="your-bucket-name", Key=file_path)
        return obj["Body"].read().decode("utf-8").splitlines()

    def upload_json(self, file_path, data):
        self.s3.put_object(Bucket="your-bucket-name", Key=file_path, Body=json.dumps(data))
