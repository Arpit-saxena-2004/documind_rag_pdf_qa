from langsmith import traceable
@traceable(name = "get_retriever_fn")
def get_retriever(db, k= 8):
    return db.as_retriever(search_type = "similarity", search_kwargs = {"k": k})