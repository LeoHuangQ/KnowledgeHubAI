import chromadb

client = chromadb.PersistentClient(path="../chroma/")
collection = client.get_or_create_collection("knowledge_hub")

def get_chroma_db():
    return client

# def store_document(chunks, embeddings):
    