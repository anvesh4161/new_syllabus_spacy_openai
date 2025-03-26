from app.models.embedding_generator import get_embedding
import json

def process_individual(request_id, text):
    embedding = get_embedding(text)
    result = {"request_id": request_id, "text": text, "embedding": embedding}
    return json.dumps(result, ensure_ascii=False)

if __name__ == "__main__":
    import sys
    print(process_individual(sys.argv[1], sys.argv[2]))
