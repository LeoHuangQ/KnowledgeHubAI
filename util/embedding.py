from api.OpenAIClient import client

MODEL = "text-embedding-3-small"

def create_embedding(texts):
    response = client.embeddings.create(
        model=MODEL,
        input=texts
    )
    return [item.embedding for item in response.data]