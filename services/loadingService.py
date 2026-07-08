from util.docLoader import load_documents
from util.textSplitter import split_text
from util.embedding import create_embedding

def loading_service(path):
    # Load documents from the specified path
    if(path != ""):
        documents = load_documents(path)
        print(f"Loaded {len(documents)} documents from {path}.")
        chunks = split_text(documents)
        print(f"Split documents into {len(chunks)} chunks. example: {chunks[0]}")
        texts = [chunk.page_content for chunk in chunks]
        print(f"Extracted text from chunks. example: {texts[0]}")
        embeddings = create_embedding(texts)
        print(f"Created embeddings for text chunks. example: {embeddings[0]}")
        
    
