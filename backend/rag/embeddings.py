from langchain_community.embeddings import HuggingFaceEmbeddings
from langsmith import traceable

@traceable(name= "get_embeddings_fn")
def get_embeddings():
    return HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2",
        model_kwargs={"device": "cpu"},   # change to "cuda" if GPU available
        encode_kwargs={"normalize_embeddings": True}
    )