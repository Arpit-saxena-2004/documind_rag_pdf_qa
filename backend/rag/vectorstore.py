from langchain_community.vectorstores import Chroma
from langsmith import traceable

@traceable(name = "get_vectorstore_fn")
def create_vectorstore(chunks, embeddings):
    return Chroma.from_documents(chunks, embeddings)