from langchain_text_splitters import RecursiveCharacterTextSplitter
from langsmith import traceable

@traceable(name = "splitter_fn")
def split_docs(docs):
    splitter = RecursiveCharacterTextSplitter(chunk_size = 800, chunk_overlap = 150)
    return splitter.split_documents(docs)