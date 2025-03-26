from services.s3_bucket import S3Bucket
from services.webhook import Webhook
from app.models.embedding_generator import get_embedding
import json

s3 = S3Bucket()
webhook = Webhook()

def process_bulk(request_id):
    data = s3.read_csv(f"input/{request_id}.csv")
    processed_data = [{"text": row, "embedding": get_embedding(row)} for row in data]
    s3.upload_json(f"output/{request_id}.json", processed_data)
    webhook.notify_success(request_id)

if __name__ == "__main__":
    import sys
    process_bulk(sys.argv[1])
