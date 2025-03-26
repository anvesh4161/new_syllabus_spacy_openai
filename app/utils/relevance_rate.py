import openai
import numpy as np

openai.api_key = "your_api_key"

def get_embedding(text):
    response = openai.Embedding.create(
        input=text,
        model="text-embedding-ada-002"
    )
    return np.array(response["data"][0]["embedding"])

def calculate_similarity(text1, text2):
    vec1 = get_embedding(text1)
    vec2 = get_embedding(text2)
    return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))
