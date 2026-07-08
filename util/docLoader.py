from langchain_community.document_loaders import DirectoryLoader, TextLoader

DATA_PATH = "data/"

def load_documents(path):
    loader = DirectoryLoader(DATA_PATH+path, glob="*.txt", loader_cls=TextLoader)
    documents = loader.load()
    return documents