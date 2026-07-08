from util.embedding import create_embedding
from util.dbLoader import search_documents
from util.dbLoader import build_context
from util.promptBuilder import build_prompt
from util.promptBuilder import stream_answer

async def rag_service(questions, top_k=10):
    embeddings = create_embedding(questions)
    # print("Embeddings created:", embeddings)
    results = search_documents(embeddings, top_k=top_k)
    context = build_context(results)
    print("Context built:", context)
    prompt = build_prompt(questions, context)
    async for token in stream_answer(prompt):
        yield token