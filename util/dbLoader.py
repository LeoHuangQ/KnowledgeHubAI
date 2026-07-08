import chromadb
import os

client = chromadb.PersistentClient(path=os.getcwd() +"/chroma_db/")
collection = client.get_or_create_collection("knowledge_hub")

def get_chroma_db():
    return client

def store_document(chunks, embeddings):
    for i in range(len(chunks)):
        collection.add(
            ids=[str(i)],
            documents=[chunks[i].page_content],
            embeddings=[embeddings[i]],
            metadatas=[{"source": chunks[i].metadata["source"]}]
        )

def search_documents(embeddings, top_k=3):
    results = []
    for embedding in embeddings:
        result = collection.query(
            query_embeddings=[embedding],
            n_results=top_k
        )
        results.append(result)
    # print("Search results:", results)
    # for i, doc in enumerate(results[0]["documents"][0]):
    #     print(f"\n===== Chunk {i+1} =====")
    #     print(doc[:300])
    return results

def build_context(results):
    context = ''
    for result in results:
        for i in range(len(result['documents'][0])):
            context += f"Content: {result['documents'][0][i]}\n\n"
    return context