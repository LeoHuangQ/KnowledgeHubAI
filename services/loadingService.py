from util.docLoader import load_documents
from util.textSplitter import split_text
from util.embedding import create_embedding
from util.dbLoader import store_document

def loading_service(path):
    # Load documents from the specified path
    if(path != ""):
        documents = load_documents(path)
        print(f"Loaded {len(documents)} documents from {path}.")
        chunks = split_text(documents)
        print(f"Split documents into {len(chunks)} chunks.")
        texts = [chunk.page_content for chunk in chunks]
        print(f"Extracted text from chunks.")
        embeddings = create_embedding(texts)
        print(f"Created embeddings {len(embeddings)} for text chunks.")
        store_document(chunks, embeddings)
    
